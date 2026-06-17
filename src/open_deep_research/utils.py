"""Utility functions and helpers for the Deep Research agent."""

import asyncio
import base64
import json
import logging
import os
import warnings
from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, Dict, List, Literal
from urllib.parse import quote, urlparse

import aiohttp
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    MessageLikeRepresentation,
    filter_messages,
)
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import (
    BaseTool,
    InjectedToolArg,
    StructuredTool,
    ToolException,
    tool,
)
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.config import get_store
from mcp import McpError
from tavily import AsyncTavilyClient

from open_deep_research.configuration import Configuration, SearchAPI
from open_deep_research.prompts import summarize_webpage_prompt
from open_deep_research.state import ResearchComplete, Summary

##########################
# Tavily Search Tool Utils
##########################
TAVILY_SEARCH_DESCRIPTION = (
    "A search engine optimized for comprehensive, accurate, and trusted results. "
    "Useful for when you need to answer questions about current events."
)
@tool(description=TAVILY_SEARCH_DESCRIPTION)
async def tavily_search(
    queries: List[str],
    max_results: Annotated[int, InjectedToolArg] = 5,
    topic: Annotated[Literal["general", "news", "finance"], InjectedToolArg] = "general",
    config: RunnableConfig = None
) -> str:
    """Fetch and summarize search results from Tavily search API.

    Args:
        queries: List of search queries to execute
        max_results: Maximum number of results to return per query
        topic: Topic filter for search results (general, news, or finance)
        config: Runtime configuration for API keys and model settings

    Returns:
        Formatted string containing summarized search results
    """
    # Step 1: Execute search queries asynchronously
    search_results = await tavily_search_async(
        queries,
        max_results=max_results,
        topic=topic,
        include_raw_content=True,
        config=config
    )
    
    # Step 2: Deduplicate results by URL to avoid processing the same content multiple times
    unique_results = {}
    for response in search_results:
        for result in response['results']:
            url = result['url']
            if url not in unique_results:
                unique_results[url] = {**result, "query": response['query']}
    
    # Step 3: Set up the summarization model with configuration
    configurable = Configuration.from_runnable_config(config)
    
    # Character limit to stay within model token limits (configurable)
    max_char_to_include = configurable.max_content_length
    
    # Initialize summarization model with retry logic
    summarization_model = init_chat_model(
        **get_chat_model_config(
            configurable.summarization_model,
            configurable.summarization_model_max_tokens,
            config,
        )
    ).with_structured_output(Summary).with_retry(
        stop_after_attempt=configurable.max_structured_output_retries
    )
    
    # Step 4: Create summarization tasks (skip empty content)
    async def noop():
        """No-op function for results without raw content."""
        return None
    
    summarization_tasks = [
        noop() if not result.get("raw_content") 
        else summarize_webpage(
            summarization_model, 
            result['raw_content'][:max_char_to_include],
            timeout_seconds=configurable.summarization_timeout_seconds,
        )
        for result in unique_results.values()
    ]
    
    # Step 5: Execute all summarization tasks in parallel
    summaries = await asyncio.gather(*summarization_tasks)
    
    # Step 6: Combine results with their summaries
    summarized_results = {
        url: {
            'title': result['title'], 
            'content': result['content'] if summary is None else summary
        }
        for url, result, summary in zip(
            unique_results.keys(), 
            unique_results.values(), 
            summaries
        )
    }
    
    # Step 7: Format the final output
    if not summarized_results:
        return "No valid search results found. Please try different search queries or use a different search API."
    
    formatted_output = "Search results: \n\n"
    for i, (url, result) in enumerate(summarized_results.items()):
        formatted_output += f"\n\n--- SOURCE {i+1}: {result['title']} ---\n"
        formatted_output += f"URL: {url}\n\n"
        formatted_output += f"SUMMARY:\n{result['content']}\n\n"
        formatted_output += "\n\n" + "-" * 80 + "\n"
    
    return formatted_output

async def tavily_search_async(
    search_queries, 
    max_results: int = 5, 
    topic: Literal["general", "news", "finance"] = "general", 
    include_raw_content: bool = True, 
    config: RunnableConfig = None
):
    """Execute multiple Tavily search queries asynchronously.
    
    Args:
        search_queries: List of search query strings to execute
        max_results: Maximum number of results per query
        topic: Topic category for filtering results
        include_raw_content: Whether to include full webpage content
        config: Runtime configuration for API key access
        
    Returns:
        List of search result dictionaries from Tavily API
    """
    # Initialize the Tavily client with API key from config
    tavily_client = AsyncTavilyClient(api_key=get_tavily_api_key(config))
    
    # Create search tasks for parallel execution
    search_tasks = [
        tavily_client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic
        )
        for query in search_queries
    ]
    
    # Execute all search queries in parallel and return results
    search_results = await asyncio.gather(*search_tasks)
    return search_results


##########################
# Knowledge Base Search Tool Utils
##########################
KNOWLEDGE_BASE_SEARCH_DESCRIPTION = (
    "Search a workspace knowledge base for relevant text, images, and tables. "
    "Returns curated evidence fields and document element UUIDs for follow-up window retrieval."
)
KNOWLEDGE_BASE_DOCUMENT_WINDOW_DESCRIPTION = (
    "Fetch nearby text, image, and table elements around a knowledge-base result. "
    "Use an element UUID returned by knowledge_base_search to recover its ordered document context."
)
KNOWLEDGE_BASE_TEXT_WINDOW_DESCRIPTION = (
    "Fetch nearby text nodes around a text result from the knowledge base. "
    "Use a TextNode UUID returned by knowledge_base_search when only textual context is needed."
)


def _validate_workspace_api_base_url(base_url: str) -> str:
    """Validate and normalize the shared workspace API base URL."""
    normalized_url = base_url.strip().rstrip("/")
    parsed_url = urlparse(normalized_url)
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
        raise ToolException(
            "KNOWLEDGE_BASE_URL must be an absolute HTTP(S) URL, for example http://127.0.0.1:8000."
        )
    return normalized_url


def _document_element_resource_url(
    element_node_id: str,
    workspace_id: str,
    base_url: str,
) -> str:
    """Build the public Resource API URL for a document element."""
    return (
        f"{base_url}"
        f"/api/v1/workspaces/{quote(workspace_id, safe='')}"
        f"/document-elements/{quote(element_node_id, safe='')}/resource"
    )


def _is_multimodal_element(element: dict[str, Any]) -> bool:
    """Return whether an element should be referenced through the Resource API."""
    modal_type = str(element.get("modal_type") or "").upper()
    if modal_type in {"IMAGE", "TABLE", "CHART"}:
        return True

    labels = {
        str(label)
        for label in element.get("labels", [])
        if isinstance(label, str)
    }
    return bool(labels & {"ImageNode", "TableNode", "ChartNode"})


def _has_document_element_resource(element: dict[str, Any]) -> bool:
    """Return whether a document element advertises a downloadable resource."""
    return bool(element.get("url"))


def _select_fields(result: dict[str, Any], fields: tuple[str, ...]) -> dict[str, Any]:
    """Select meaningful fields from a retrieval result."""
    return {
        field: result[field]
        for field in fields
        if field in result and result[field] not in (None, "")
    }


def _normalize_query_result(
    query_result: dict[str, Any],
    query: str,
    workspace_id: str,
    base_url: str,
) -> dict[str, Any]:
    """Reduce a Query API response to evidence fields useful to the researcher."""
    metadata = query_result.get("metadata")
    if not isinstance(metadata, dict):
        raise ToolException("Query API response does not contain retrieval metadata.")

    normalized: dict[str, Any] = {
        "query": query,
        "text_results": [],
        "image_results": [],
        "table_results": [],
        "chart_results": [],
    }

    common_fields = ("uuid", "name", "group_id", "labels", "attributes")

    for result in metadata.get("text_results") or []:
        if isinstance(result, dict):
            selected = _select_fields(
                result,
                common_fields + ("content", "enhanced_str", "score"),
            )
            element_id = selected.get("uuid")
            if isinstance(element_id, str) and element_id:
                selected["url"] = _document_element_resource_url(
                    element_id,
                    workspace_id,
                    base_url,
                )
            normalized["text_results"].append(selected)

    multimodal_fields = common_fields + (
        "url",
        "caption",
        "summary",
        "description",
        "body",
        "score",
    )
    for result_type in ("image_results", "table_results", "chart_results"):
        for result in metadata.get(result_type) or []:
            if not isinstance(result, dict):
                continue
            selected = _select_fields(result, multimodal_fields)
            element_id = selected.get("uuid")
            if (
                isinstance(element_id, str)
                and element_id
                and _has_document_element_resource(selected)
            ):
                selected["url"] = _document_element_resource_url(
                    element_id,
                    workspace_id,
                    base_url,
                )
            normalized[result_type].append(selected)

    return normalized


def _format_knowledge_base_results(results: list[dict[str, Any]]) -> str:
    """Format normalized retrieval evidence without exposing raw API metadata."""
    sections = ["Knowledge base search results:"]
    result_labels = (
        ("text_results", "Text results"),
        ("image_results", "Image results"),
        ("table_results", "Table results"),
        ("chart_results", "Chart results"),
    )

    for query_index, result in enumerate(results, start=1):
        sections.append(f"\n## Query {query_index}: {result['query']}")
        for result_key, label in result_labels:
            items = result[result_key]
            if not items:
                continue
            sections.append(f"\n### {label}")
            for item_index, item in enumerate(items, start=1):
                sections.append(
                    f"{item_index}. " + json.dumps(item, ensure_ascii=False)
                )

        if not any(result[key] for key, _ in result_labels):
            sections.append("\nNo relevant results found.")

    return "\n".join(sections)


def _limit_knowledge_base_results(
    results: list[dict[str, Any]],
    text_topk: int = 10,
    image_topk: int = 3,
    table_topk: int = 3,
    chart_topk: int = 3,
) -> list[dict[str, Any]]:
    """Limit normalized Query API results by result type before tool output."""
    limits = {
        "text_results": max(text_topk, 0),
        "image_results": max(image_topk, 0),
        "table_results": max(table_topk, 0),
        "chart_results": max(chart_topk, 0),
    }
    limited_results = []

    for result in results:
        limited_result = dict(result)
        for result_key, limit in limits.items():
            items = limited_result.get(result_key)
            if isinstance(items, list):
                limited_result[result_key] = items[:limit]
        limited_results.append(limited_result)

    return limited_results


def _resolve_document_element_urls(
    window_result: dict[str, Any],
    workspace_id: str,
    base_url: str,
) -> dict[str, Any]:
    """Convert multimodal element URLs in a window to Resource API URLs."""
    elements = []
    center = window_result.get("center")
    if isinstance(center, dict):
        elements.append(center)

    items = window_result.get("items")
    if isinstance(items, list):
        elements.extend(item for item in items if isinstance(item, dict))

    for element in elements:
        element_id = element.get("uuid")
        labels = {
            str(label)
            for label in element.get("labels", [])
            if isinstance(label, str)
        }
        modal_type = str(element.get("modal_type") or "").upper()
        is_text_element = modal_type == "TEXT" or "TextNode" in labels
        if (
            isinstance(element_id, str)
            and element_id
            and (
                is_text_element
                or (_is_multimodal_element(element) and _has_document_element_resource(element))
            )
        ):
            element["url"] = _document_element_resource_url(
                element_id,
                workspace_id,
                base_url,
            )

    return window_result


async def _get_workspace_window_async(
    resource: Literal["document-elements", "text-nodes"],
    node_id: str,
    workspace_id: str,
    base_url: str,
    k: int = 4,
    timeout_seconds: float = 120.0,
) -> dict[str, Any]:
    """Call a workspace Window API endpoint and return its JSON response."""
    normalized_node_id = node_id.strip()
    normalized_workspace_id = workspace_id.strip()
    normalized_base_url = _validate_workspace_api_base_url(base_url)
    if not normalized_node_id:
        raise ToolException("node_id must not be empty.")
    if not normalized_workspace_id:
        raise ToolException("workspace_id must not be empty.")

    endpoint = (
        f"{normalized_base_url}"
        f"/api/v1/workspaces/{quote(normalized_workspace_id, safe='')}"
        f"/{resource}/{quote(normalized_node_id, safe='')}/window?k={k}"
    )
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(endpoint) as response:
                response_text = await response.text()
                if response.status >= 400:
                    raise ToolException(
                        f"Window API request failed with HTTP {response.status}: "
                        f"{response_text[:500]}"
                    )
    except asyncio.TimeoutError as exc:
        raise ToolException(
            f"Window API request timed out after {timeout_seconds:g} seconds."
        ) from exc
    except aiohttp.ClientError as exc:
        raise ToolException(f"Window API request failed: {exc}") from exc

    try:
        window_result = json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ToolException("Window API returned a non-JSON response.") from exc

    if not isinstance(window_result, dict):
        raise ToolException("Window API returned an invalid response object.")

    return _resolve_document_element_urls(
        window_result,
        normalized_workspace_id,
        normalized_base_url,
    )


async def get_document_element_window_async(
    element_node_id: str,
    workspace_id: str,
    base_url: str,
    k: int = 4,
    timeout_seconds: float = 120.0,
) -> dict[str, Any]:
    """Fetch an ordered multimodal window around a document element."""
    return await _get_workspace_window_async(
        resource="document-elements",
        node_id=element_node_id,
        workspace_id=workspace_id,
        base_url=base_url,
        k=k,
        timeout_seconds=timeout_seconds,
    )


async def get_text_node_window_async(
    text_node_id: str,
    workspace_id: str,
    base_url: str,
    k: int = 4,
    timeout_seconds: float = 120.0,
) -> dict[str, Any]:
    """Fetch an ordered text-only window around a TextNode."""
    return await _get_workspace_window_async(
        resource="text-nodes",
        node_id=text_node_id,
        workspace_id=workspace_id,
        base_url=base_url,
        k=k,
        timeout_seconds=timeout_seconds,
    )


async def get_document_element_resource_data_url_async(
    element_node_id: str,
    workspace_id: str,
    base_url: str,
    timeout_seconds: float = 120.0,
    max_bytes: int = 8_000_000,
) -> dict[str, str]:
    """Fetch a document element resource and return it as an image data URL."""
    normalized_node_id = element_node_id.strip()
    normalized_workspace_id = workspace_id.strip()
    normalized_base_url = _validate_workspace_api_base_url(base_url)
    if not normalized_node_id:
        raise ToolException("element_node_id must not be empty.")
    if not normalized_workspace_id:
        raise ToolException("workspace_id must not be empty.")

    endpoint = (
        f"{normalized_base_url}"
        f"/api/v1/workspaces/{quote(normalized_workspace_id, safe='')}"
        f"/document-elements/{quote(normalized_node_id, safe='')}/resource"
    )
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(endpoint) as response:
                if response.status >= 400:
                    response_text = await response.text()
                    raise ToolException(
                        f"Resource API request failed with HTTP {response.status}: "
                        f"{response_text[:500]}"
                    )
                content_type = response.headers.get("Content-Type", "").split(";")[0].strip()
                if not content_type.startswith("image/"):
                    raise ToolException(
                        f"Resource API returned non-image content type: {content_type or 'unknown'}"
                    )
                content_length = response.headers.get("Content-Length")
                if content_length:
                    try:
                        declared_size = int(content_length)
                    except ValueError:
                        declared_size = None
                    if declared_size and declared_size > max_bytes:
                        raise ToolException(
                            f"Resource image is too large: {declared_size} bytes exceeds {max_bytes}."
                        )
                payload = await response.read()
    except asyncio.TimeoutError as exc:
        raise ToolException(
            f"Resource API request timed out after {timeout_seconds:g} seconds."
        ) from exc
    except aiohttp.ClientError as exc:
        raise ToolException(f"Resource API request failed: {exc}") from exc

    if len(payload) > max_bytes:
        raise ToolException(
            f"Resource image is too large: {len(payload)} bytes exceeds {max_bytes}."
        )

    encoded = base64.b64encode(payload).decode("ascii")
    return {
        "source_id": normalized_node_id,
        "mime_type": content_type,
        "data_url": f"data:{content_type};base64,{encoded}",
    }


def is_missing_document_element_resource_error(error: BaseException) -> bool:
    """Return whether a Resource API error means the node has no downloadable file."""
    message = str(error)
    return (
        "Resource API request failed with HTTP 404" in message
        and "has no resource path" in message
    )


async def query_workspace_async(
    query: str,
    workspace_id: str,
    base_url: str,
    chunk_top_k: int = 10,
    similarity_threshold: float = 0.2,
    timeout_seconds: float = 120.0,
) -> dict[str, Any]:
    """Query one workspace and return normalized multimodal retrieval evidence."""
    normalized_query = query.strip()
    normalized_workspace_id = workspace_id.strip()
    normalized_base_url = _validate_workspace_api_base_url(base_url)
    if not normalized_query:
        raise ToolException("Query must not be empty.")
    if not normalized_workspace_id:
        raise ToolException("workspace_id must not be empty.")

    endpoint = (
        f"{normalized_base_url}"
        f"/api/v1/workspaces/{quote(normalized_workspace_id, safe='')}/query"
    )
    payload = {
        "query": normalized_query,
        "mode": "naive",
        "naive_kwargs": {"enable_multimodal": True},
        "only_need_data": True,
        "similarity_threshold": similarity_threshold,
        "chunk_top_k": chunk_top_k,
        "enable_rerank": False,
        "stream": False,
    }
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(endpoint, json=payload) as response:
                response_text = await response.text()
                if response.status >= 400:
                    raise ToolException(
                        f"Query API request failed with HTTP {response.status}: "
                        f"{response_text[:500]}"
                    )
    except asyncio.TimeoutError as exc:
        raise ToolException(
            f"Query API request timed out after {timeout_seconds:g} seconds."
        ) from exc
    except aiohttp.ClientError as exc:
        raise ToolException(f"Query API request failed: {exc}") from exc

    try:
        query_result = json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ToolException("Query API returned a non-JSON response.") from exc

    if not isinstance(query_result, dict):
        raise ToolException("Query API returned an invalid response object.")

    return _normalize_query_result(
        query_result,
        query=normalized_query,
        workspace_id=normalized_workspace_id,
        base_url=normalized_base_url,
    )


@tool(description=KNOWLEDGE_BASE_SEARCH_DESCRIPTION, response_format="content_and_artifact")
async def knowledge_base_search(
    queries: List[str],
    workspace_id: str | None = None,
    text_topk: int = 10,
    image_topk: int = 3,
    table_topk: int = 3,
    chart_topk: int = 3,
    chunk_top_k: Annotated[int, InjectedToolArg] = 10,
    similarity_threshold: Annotated[float, InjectedToolArg] = 0.2,
    config: RunnableConfig = None,
) -> str:
    """Search configured workspace content without invoking the Query API's LLM.

    Args:
        queries: Natural-language queries to run against the workspace
        workspace_id: Workspace to search; defaults to WORKSPACE_ID when configured
        text_topk: Maximum text results to return after retrieval
        image_topk: Maximum image results to return after retrieval
        table_topk: Maximum table results to return after retrieval
        chart_topk: Maximum chart results to return after retrieval
        chunk_top_k: Maximum results to request from the Query API for each content type
        similarity_threshold: Minimum vector similarity threshold
        config: Runtime configuration containing KNOWLEDGE_BASE_URL and WORKSPACE_ID

    Returns:
        Concise text containing curated text, image, table, and chart evidence
    """
    resolved_base_url, resolved_workspace_id = _resolve_workspace_config(
        config,
        workspace_id,
    )
    configurable = Configuration.from_runnable_config(config)

    normalized_queries = [query.strip() for query in queries if query.strip()]
    if not normalized_queries:
        raise ToolException("At least one non-empty query is required.")

    results = await asyncio.gather(*[
        query_workspace_async(
            query=query,
            workspace_id=resolved_workspace_id,
            base_url=resolved_base_url,
            chunk_top_k=chunk_top_k,
            similarity_threshold=similarity_threshold,
            timeout_seconds=configurable.knowledge_base_query_timeout_seconds,
        )
        for query in normalized_queries
    ])
    results = _limit_knowledge_base_results(
        results,
        text_topk=text_topk,
        image_topk=image_topk,
        table_topk=table_topk,
        chart_topk=chart_topk,
    )

    formatted_results = _format_knowledge_base_results(results)
    return formatted_results, {
        "type": "knowledge_base_search",
        "results": results,
    }


def _resolve_workspace_config(
    config: RunnableConfig,
    workspace_id: str | None,
) -> tuple[str, str]:
    """Resolve the shared Window and Query API configuration."""
    configurable = Configuration.from_runnable_config(config)
    resolved_base_url = configurable.knowledge_base_url
    resolved_workspace_id = workspace_id or configurable.workspace_id

    if not resolved_base_url:
        raise ToolException(
            "Knowledge base tools are not configured. Set the KNOWLEDGE_BASE_URL environment variable."
        )
    if not resolved_workspace_id:
        raise ToolException(
            "A workspace_id is required. Pass it to the tool or set WORKSPACE_ID."
        )

    return resolved_base_url, resolved_workspace_id


@tool(description=KNOWLEDGE_BASE_DOCUMENT_WINDOW_DESCRIPTION, response_format="content_and_artifact")
async def knowledge_base_document_window(
    element_node_id: str,
    workspace_id: str | None = None,
    k: int = 4,
    config: RunnableConfig = None,
) -> tuple[str, dict[str, Any]]:
    """Fetch mixed document elements near a knowledge-base result.

    Args:
        element_node_id: UUID of a TextNode, ImageNode, or TableNode
        workspace_id: Workspace to read; defaults to WORKSPACE_ID when configured
        k: Maximum number of additional context elements; response has at most k + 1 items
        config: Runtime configuration containing KNOWLEDGE_BASE_URL and WORKSPACE_ID

    Returns:
        JSON-formatted text containing the ordered multimodal document window
    """
    resolved_base_url, resolved_workspace_id = _resolve_workspace_config(
        config,
        workspace_id,
    )
    configurable = Configuration.from_runnable_config(config)
    result = await get_document_element_window_async(
        element_node_id=element_node_id,
        workspace_id=resolved_workspace_id,
        base_url=resolved_base_url,
        k=k,
        timeout_seconds=configurable.knowledge_base_window_timeout_seconds,
    )
    content = "Knowledge base document window:\n\n" + json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
    )
    return content, {
        "type": "knowledge_base_document_window",
        "result": result,
    }


@tool(description=KNOWLEDGE_BASE_TEXT_WINDOW_DESCRIPTION, response_format="content_and_artifact")
async def knowledge_base_text_window(
    text_node_id: str,
    workspace_id: str | None = None,
    k: int = 4,
    config: RunnableConfig = None,
) -> tuple[str, dict[str, Any]]:
    """Fetch nearby TextNodes around a knowledge-base text result.

    Args:
        text_node_id: UUID of the center TextNode
        workspace_id: Workspace to read; defaults to WORKSPACE_ID when configured
        k: Maximum number of additional text nodes; response has at most k + 1 items
        config: Runtime configuration containing KNOWLEDGE_BASE_URL and WORKSPACE_ID

    Returns:
        JSON-formatted text containing the ordered text-only document window
    """
    resolved_base_url, resolved_workspace_id = _resolve_workspace_config(
        config,
        workspace_id,
    )
    configurable = Configuration.from_runnable_config(config)
    result = await get_text_node_window_async(
        text_node_id=text_node_id,
        workspace_id=resolved_workspace_id,
        base_url=resolved_base_url,
        k=k,
        timeout_seconds=configurable.knowledge_base_window_timeout_seconds,
    )
    content = "Knowledge base text window:\n\n" + json.dumps(
        result,
        ensure_ascii=False,
        indent=2,
    )
    return content, {
        "type": "knowledge_base_text_window",
        "result": result,
    }


async def summarize_webpage(
    model: BaseChatModel,
    webpage_content: str,
    timeout_seconds: float = 60.0,
) -> str:
    """Summarize webpage content using AI model with timeout protection.
    
    Args:
        model: The chat model configured for summarization
        webpage_content: Raw webpage content to be summarized
        timeout_seconds: Maximum duration for the model call
        
    Returns:
        Formatted summary with key excerpts, or original content if summarization fails
    """
    try:
        # Create prompt with current date context
        prompt_content = summarize_webpage_prompt.format(
            webpage_content=webpage_content, 
            date=get_today_str()
        )
        
        # Execute summarization with timeout to prevent hanging
        summary = await asyncio.wait_for(
            model.ainvoke([HumanMessage(content=prompt_content)]),
            timeout=timeout_seconds,
        )
        
        # Format the summary with structured sections
        formatted_summary = (
            f"<summary>\n{summary.summary}\n</summary>\n\n"
            f"<key_excerpts>\n{summary.key_excerpts}\n</key_excerpts>"
        )
        
        return formatted_summary
        
    except asyncio.TimeoutError:
        # Timeout during summarization - return original content
        logging.warning(
            "Summarization timed out after %s seconds, returning original content",
            f"{timeout_seconds:g}",
        )
        return webpage_content
    except Exception as e:
        # Other errors during summarization - log and return original content
        logging.warning(f"Summarization failed with error: {str(e)}, returning original content")
        return webpage_content

##########################
# Reflection Tool Utils
##########################

@tool(description="Strategic reflection tool for research planning")
def think_tool(reflection: str) -> str:
    """Tool for strategic reflection on research progress and decision-making.

    Use this tool after each search to analyze results and plan next steps systematically.
    This creates a deliberate pause in the research workflow for quality decision-making.

    When to use:
    - After receiving search results: What key information did I find?
    - Before deciding next steps: Do I have enough to answer comprehensively?
    - When assessing research gaps: What specific information am I still missing?
    - Before concluding research: Can I provide a complete answer now?

    Reflection should address:
    1. Analysis of current findings - What concrete information have I gathered?
    2. Gap assessment - What crucial information is still missing?
    3. Quality evaluation - Do I have sufficient evidence/examples for a good answer?
    4. Strategic decision - Should I continue searching or provide my answer?

    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps

    Returns:
        Confirmation that reflection was recorded for decision-making
    """
    return f"Reflection recorded: {reflection}"

##########################
# MCP Utils
##########################

async def get_mcp_access_token(
    supabase_token: str,
    base_mcp_url: str,
) -> Dict[str, Any] | None:
    """Exchange Supabase token for MCP access token using OAuth token exchange.
    
    Args:
        supabase_token: Valid Supabase authentication token
        base_mcp_url: Base URL of the MCP server
        
    Returns:
        Token data dictionary if successful, None if failed
    """
    try:
        # Prepare OAuth token exchange request data
        form_data = {
            "client_id": "mcp_default",
            "subject_token": supabase_token,
            "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
            "resource": base_mcp_url.rstrip("/") + "/mcp",
            "subject_token_type": "urn:ietf:params:oauth:token-type:access_token",
        }
        
        # Execute token exchange request
        async with aiohttp.ClientSession() as session:
            token_url = base_mcp_url.rstrip("/") + "/oauth/token"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            
            async with session.post(token_url, headers=headers, data=form_data) as response:
                if response.status == 200:
                    # Successfully obtained token
                    token_data = await response.json()
                    return token_data
                else:
                    # Log error details for debugging
                    response_text = await response.text()
                    logging.error(f"Token exchange failed: {response_text}")
                    
    except Exception as e:
        logging.error(f"Error during token exchange: {e}")
    
    return None

async def get_tokens(config: RunnableConfig):
    """Retrieve stored authentication tokens with expiration validation.
    
    Args:
        config: Runtime configuration containing thread and user identifiers
        
    Returns:
        Token dictionary if valid and not expired, None otherwise
    """
    store = get_store()
    
    # Extract required identifiers from config
    thread_id = config.get("configurable", {}).get("thread_id")
    if not thread_id:
        return None
        
    user_id = config.get("metadata", {}).get("owner")
    if not user_id:
        return None
    
    # Retrieve stored tokens
    tokens = await store.aget((user_id, "tokens"), "data")
    if not tokens:
        return None
    
    # Check token expiration
    expires_in = tokens.value.get("expires_in")  # seconds until expiration
    created_at = tokens.created_at  # datetime of token creation
    current_time = datetime.now(timezone.utc)
    expiration_time = created_at + timedelta(seconds=expires_in)
    
    if current_time > expiration_time:
        # Token expired, clean up and return None
        await store.adelete((user_id, "tokens"), "data")
        return None

    return tokens.value

async def set_tokens(config: RunnableConfig, tokens: dict[str, Any]):
    """Store authentication tokens in the configuration store.
    
    Args:
        config: Runtime configuration containing thread and user identifiers
        tokens: Token dictionary to store
    """
    store = get_store()
    
    # Extract required identifiers from config
    thread_id = config.get("configurable", {}).get("thread_id")
    if not thread_id:
        return
        
    user_id = config.get("metadata", {}).get("owner")
    if not user_id:
        return
    
    # Store the tokens
    await store.aput((user_id, "tokens"), "data", tokens)

async def fetch_tokens(config: RunnableConfig) -> dict[str, Any]:
    """Fetch and refresh MCP tokens, obtaining new ones if needed.
    
    Args:
        config: Runtime configuration with authentication details
        
    Returns:
        Valid token dictionary, or None if unable to obtain tokens
    """
    # Try to get existing valid tokens first
    current_tokens = await get_tokens(config)
    if current_tokens:
        return current_tokens
    
    # Extract Supabase token for new token exchange
    supabase_token = config.get("configurable", {}).get("x-supabase-access-token")
    if not supabase_token:
        return None
    
    # Extract MCP configuration
    mcp_config = config.get("configurable", {}).get("mcp_config")
    if not mcp_config or not mcp_config.get("url"):
        return None
    
    # Exchange Supabase token for MCP tokens
    mcp_tokens = await get_mcp_access_token(supabase_token, mcp_config.get("url"))
    if not mcp_tokens:
        return None

    # Store the new tokens and return them
    await set_tokens(config, mcp_tokens)
    return mcp_tokens

def wrap_mcp_authenticate_tool(tool: StructuredTool) -> StructuredTool:
    """Wrap MCP tool with comprehensive authentication and error handling.
    
    Args:
        tool: The MCP structured tool to wrap
        
    Returns:
        Enhanced tool with authentication error handling
    """
    original_coroutine = tool.coroutine
    
    async def authentication_wrapper(**kwargs):
        """Enhanced coroutine with MCP error handling and user-friendly messages."""
        
        def _find_mcp_error_in_exception_chain(exc: BaseException) -> McpError | None:
            """Recursively search for MCP errors in exception chains."""
            if isinstance(exc, McpError):
                return exc
            
            # Handle ExceptionGroup (Python 3.11+) by checking attributes
            if hasattr(exc, 'exceptions'):
                for sub_exception in exc.exceptions:
                    if found_error := _find_mcp_error_in_exception_chain(sub_exception):
                        return found_error
            return None
        
        try:
            # Execute the original tool functionality
            return await original_coroutine(**kwargs)
            
        except BaseException as original_error:
            # Search for MCP-specific errors in the exception chain
            mcp_error = _find_mcp_error_in_exception_chain(original_error)
            if not mcp_error:
                # Not an MCP error, re-raise the original exception
                raise original_error
            
            # Handle MCP-specific error cases
            error_details = mcp_error.error
            error_code = getattr(error_details, "code", None)
            error_data = getattr(error_details, "data", None) or {}
            
            # Check for authentication/interaction required error
            if error_code == -32003:  # Interaction required error code
                message_payload = error_data.get("message", {})
                error_message = "Required interaction"
                
                # Extract user-friendly message if available
                if isinstance(message_payload, dict):
                    error_message = message_payload.get("text") or error_message
                
                # Append URL if provided for user reference
                if url := error_data.get("url"):
                    error_message = f"{error_message} {url}"
                
                raise ToolException(error_message) from original_error
            
            # For other MCP errors, re-raise the original
            raise original_error
    
    # Replace the tool's coroutine with our enhanced version
    tool.coroutine = authentication_wrapper
    return tool

async def load_mcp_tools(
    config: RunnableConfig,
    existing_tool_names: set[str],
) -> list[BaseTool]:
    """Load and configure MCP (Model Context Protocol) tools with authentication.
    
    Args:
        config: Runtime configuration containing MCP server details
        existing_tool_names: Set of tool names already in use to avoid conflicts
        
    Returns:
        List of configured MCP tools ready for use
    """
    configurable = Configuration.from_runnable_config(config)
    
    # Step 1: Handle authentication if required
    if configurable.mcp_config and configurable.mcp_config.auth_required:
        mcp_tokens = await fetch_tokens(config)
    else:
        mcp_tokens = None
    
    # Step 2: Validate configuration requirements
    config_valid = (
        configurable.mcp_config and 
        configurable.mcp_config.url and 
        configurable.mcp_config.tools and 
        (mcp_tokens or not configurable.mcp_config.auth_required)
    )
    
    if not config_valid:
        return []
    
    # Step 3: Set up MCP server connection
    server_url = configurable.mcp_config.url.rstrip("/") + "/mcp"
    
    # Configure authentication headers if tokens are available
    auth_headers = None
    if mcp_tokens:
        auth_headers = {"Authorization": f"Bearer {mcp_tokens['access_token']}"}
    
    mcp_server_config = {
        "server_1": {
            "url": server_url,
            "headers": auth_headers,
            "transport": "streamable_http"
        }
    }
    # TODO: When Multi-MCP Server support is merged in OAP, update this code
    
    # Step 4: Load tools from MCP server
    try:
        client = MultiServerMCPClient(mcp_server_config)
        available_mcp_tools = await client.get_tools()
    except Exception:
        # If MCP server connection fails, return empty list
        return []
    
    # Step 5: Filter and configure tools
    configured_tools = []
    for mcp_tool in available_mcp_tools:
        # Skip tools with conflicting names
        if mcp_tool.name in existing_tool_names:
            warnings.warn(
                f"MCP tool '{mcp_tool.name}' conflicts with existing tool name - skipping"
            )
            continue
        
        # Only include tools specified in configuration
        if mcp_tool.name not in set(configurable.mcp_config.tools):
            continue
        
        # Wrap tool with authentication handling and add to list
        enhanced_tool = wrap_mcp_authenticate_tool(mcp_tool)
        configured_tools.append(enhanced_tool)
    
    return configured_tools


##########################
# Tool Utils
##########################

async def get_search_tool(search_api: SearchAPI):
    """Configure and return search tools based on the specified API provider.
    
    Args:
        search_api: The search API provider to use (Anthropic, OpenAI, Tavily, or None)
        
    Returns:
        List of configured search tool objects for the specified provider
    """
    if search_api == SearchAPI.ANTHROPIC:
        # Anthropic's native web search with usage limits
        return [{
            "type": "web_search_20250305", 
            "name": "web_search", 
            "max_uses": 5
        }]
        
    elif search_api == SearchAPI.OPENAI:
        # OpenAI's web search preview functionality
        return [{"type": "web_search_preview"}]
        
    elif search_api == SearchAPI.TAVILY:
        # Configure Tavily search tool with metadata
        search_tool = tavily_search
        search_tool.metadata = {
            **(search_tool.metadata or {}), 
            "type": "search", 
            "name": "web_search"
        }
        return [search_tool]
        
    elif search_api == SearchAPI.NONE:
        # No search functionality configured
        return []
        
    # Default fallback for unknown search API types
    return []
    
async def get_all_tools(config: RunnableConfig):
    """Assemble complete toolkit including research, search, and MCP tools.
    
    Args:
        config: Runtime configuration specifying search API and MCP settings
        
    Returns:
        List of all configured and available tools for research operations
    """
    # Start with core research tools
    tools = [tool(ResearchComplete), think_tool]
    
    # Add configured search tools
    configurable = Configuration.from_runnable_config(config)
    search_api = SearchAPI(get_config_value(configurable.search_api))
    search_tools = await get_search_tool(search_api)
    tools.extend(search_tools)

    # The private knowledge base complements the selected web search provider.
    if configurable.knowledge_base_url:
        knowledge_base_search.metadata = {
            **(knowledge_base_search.metadata or {}),
            "type": "search",
            "name": "knowledge_base_search",
        }
        knowledge_base_document_window.metadata = {
            **(knowledge_base_document_window.metadata or {}),
            "type": "retrieval",
            "name": "knowledge_base_document_window",
        }
        knowledge_base_text_window.metadata = {
            **(knowledge_base_text_window.metadata or {}),
            "type": "retrieval",
            "name": "knowledge_base_text_window",
        }
        tools.extend([
            knowledge_base_search,
            knowledge_base_document_window,
            knowledge_base_text_window,
        ])
    
    # Track existing tool names to prevent conflicts
    existing_tool_names = {
        tool.name if hasattr(tool, "name") else tool.get("name", "web_search") 
        for tool in tools
    }
    
    # Add MCP tools if configured
    mcp_tools = await load_mcp_tools(config, existing_tool_names)
    tools.extend(mcp_tools)
    
    return tools

def get_notes_from_tool_calls(messages: list[MessageLikeRepresentation]):
    """Extract notes from tool call messages."""
    return [tool_msg.content for tool_msg in filter_messages(messages, include_types="tool")]

##########################
# Model Provider Native Websearch Utils
##########################

def anthropic_websearch_called(response):
    """Detect if Anthropic's native web search was used in the response.
    
    Args:
        response: The response object from Anthropic's API
        
    Returns:
        True if web search was called, False otherwise
    """
    try:
        # Navigate through the response metadata structure
        usage = response.response_metadata.get("usage")
        if not usage:
            return False
        
        # Check for server-side tool usage information
        server_tool_use = usage.get("server_tool_use")
        if not server_tool_use:
            return False
        
        # Look for web search request count
        web_search_requests = server_tool_use.get("web_search_requests")
        if web_search_requests is None:
            return False
        
        # Return True if any web search requests were made
        return web_search_requests > 0
        
    except (AttributeError, TypeError):
        # Handle cases where response structure is unexpected
        return False

def openai_websearch_called(response):
    """Detect if OpenAI's web search functionality was used in the response.
    
    Args:
        response: The response object from OpenAI's API
        
    Returns:
        True if web search was called, False otherwise
    """
    # Check for tool outputs in the response metadata
    tool_outputs = response.additional_kwargs.get("tool_outputs")
    if not tool_outputs:
        return False
    
    # Look for web search calls in the tool outputs
    for tool_output in tool_outputs:
        if tool_output.get("type") == "web_search_call":
            return True
    
    return False


##########################
# Token Limit Exceeded Utils
##########################

def is_token_limit_exceeded(exception: Exception, model_name: str = None) -> bool:
    """Determine if an exception indicates a token/context limit was exceeded.
    
    Args:
        exception: The exception to analyze
        model_name: Optional model name to optimize provider detection
        
    Returns:
        True if the exception indicates a token limit was exceeded, False otherwise
    """
    error_str = str(exception).lower()
    
    # Step 1: Determine provider from model name if available
    provider = None
    if model_name:
        model_str = str(model_name).lower()
        if model_str.startswith('openai:'):
            provider = 'openai'
        elif model_str.startswith('anthropic:'):
            provider = 'anthropic'
        elif model_str.startswith('gemini:') or model_str.startswith('google:'):
            provider = 'gemini'
    
    # Step 2: Check provider-specific token limit patterns
    if provider == 'openai':
        return (
            _check_openai_token_limit(exception, error_str) or
            _check_structured_output_truncation(exception, error_str)
        )
    elif provider == 'anthropic':
        return (
            _check_anthropic_token_limit(exception, error_str) or
            _check_structured_output_truncation(exception, error_str)
        )
    elif provider == 'gemini':
        return (
            _check_gemini_token_limit(exception, error_str) or
            _check_structured_output_truncation(exception, error_str)
        )
    
    # Step 3: If provider unknown, check all providers and structured-output truncation.
    # Some OpenAI-compatible providers return a cut-off JSON body for structured
    # output instead of a provider-specific length error. Treat that as a
    # retryable budget issue so callers can reduce context before trying again.
    return (
        _check_openai_token_limit(exception, error_str) or
        _check_anthropic_token_limit(exception, error_str) or
        _check_gemini_token_limit(exception, error_str) or
        _check_structured_output_truncation(exception, error_str)
    )

def _check_structured_output_truncation(exception: Exception, error_str: str) -> bool:
    """Check if structured JSON output was truncated before it could be parsed."""
    exception_type = str(type(exception)).lower()
    class_name = exception.__class__.__name__
    is_pydantic_validation_error = (
        class_name == "ValidationError" and
        ("pydantic" in exception_type or "pydantic_core" in exception_type)
    )
    if not is_pydantic_validation_error:
        return False

    truncation_markers = (
        "invalid json",
        "json_invalid",
        "eof while parsing",
        "unexpected eof",
        "unterminated string",
    )
    return any(marker in error_str for marker in truncation_markers)

def _check_openai_token_limit(exception: Exception, error_str: str) -> bool:
    """Check if exception indicates OpenAI token limit exceeded."""
    # Analyze exception metadata
    exception_type = str(type(exception))
    class_name = exception.__class__.__name__
    module_name = getattr(exception.__class__, '__module__', '')
    
    # Check if this is an OpenAI exception
    is_openai_exception = (
        'openai' in exception_type.lower() or 
        'openai' in module_name.lower()
    )
    
    # Check for typical OpenAI token limit error types
    is_request_error = class_name in ['BadRequestError', 'InvalidRequestError']
    
    if is_openai_exception and is_request_error:
        # Look for token-related keywords in error message
        token_keywords = ['token', 'context', 'length', 'maximum context', 'reduce']
        if any(keyword in error_str for keyword in token_keywords):
            return True
    
    # Check for specific OpenAI error codes
    if hasattr(exception, 'code') and hasattr(exception, 'type'):
        error_code = getattr(exception, 'code', '')
        error_type = getattr(exception, 'type', '')
        
        if (error_code == 'context_length_exceeded' or
            error_type == 'invalid_request_error'):
            return True
    
    return False

def _check_anthropic_token_limit(exception: Exception, error_str: str) -> bool:
    """Check if exception indicates Anthropic token limit exceeded."""
    # Analyze exception metadata
    exception_type = str(type(exception))
    class_name = exception.__class__.__name__
    module_name = getattr(exception.__class__, '__module__', '')
    
    # Check if this is an Anthropic exception
    is_anthropic_exception = (
        'anthropic' in exception_type.lower() or 
        'anthropic' in module_name.lower()
    )
    
    # Check for Anthropic-specific error patterns
    is_bad_request = class_name == 'BadRequestError'
    
    if is_anthropic_exception and is_bad_request:
        # Anthropic uses specific error messages for token limits
        if 'prompt is too long' in error_str:
            return True
    
    return False

def _check_gemini_token_limit(exception: Exception, error_str: str) -> bool:
    """Check if exception indicates Google/Gemini token limit exceeded."""
    # Analyze exception metadata
    exception_type = str(type(exception))
    class_name = exception.__class__.__name__
    module_name = getattr(exception.__class__, '__module__', '')
    
    # Check if this is a Google/Gemini exception
    is_google_exception = (
        'google' in exception_type.lower() or 
        'google' in module_name.lower()
    )
    
    # Check for Google-specific resource exhaustion errors
    is_resource_exhausted = class_name in [
        'ResourceExhausted', 
        'GoogleGenerativeAIFetchError'
    ]
    
    if is_google_exception and is_resource_exhausted:
        return True
    
    # Check for specific Google API resource exhaustion patterns
    if 'google.api_core.exceptions.resourceexhausted' in exception_type.lower():
        return True
    
    return False

# NOTE: This may be out of date or not applicable to your models. Please update this as needed.
MODEL_TOKEN_LIMITS = {
    "openai:gpt-4.1-mini": 1047576,
    "openai:gpt-4.1-nano": 1047576,
    "openai:gpt-4.1": 1047576,
    "openai:gpt-4o-mini": 128000,
    "openai:gpt-4o": 128000,
    "openai:o4-mini": 200000,
    "openai:o3-mini": 200000,
    "openai:o3": 200000,
    "openai:o3-pro": 200000,
    "openai:o1": 200000,
    "openai:o1-pro": 200000,
    "anthropic:claude-opus-4": 200000,
    "anthropic:claude-sonnet-4": 200000,
    "anthropic:claude-3-7-sonnet": 200000,
    "anthropic:claude-3-5-sonnet": 200000,
    "anthropic:claude-3-5-haiku": 200000,
    "google:gemini-1.5-pro": 2097152,
    "google:gemini-1.5-flash": 1048576,
    "google:gemini-pro": 32768,
    "cohere:command-r-plus": 128000,
    "cohere:command-r": 128000,
    "cohere:command-light": 4096,
    "cohere:command": 4096,
    "mistral:mistral-large": 32768,
    "mistral:mistral-medium": 32768,
    "mistral:mistral-small": 32768,
    "mistral:mistral-7b-instruct": 32768,
    "ollama:codellama": 16384,
    "ollama:llama2:70b": 4096,
    "ollama:llama2:13b": 4096,
    "ollama:llama2": 4096,
    "ollama:mistral": 32768,
    "bedrock:us.amazon.nova-premier-v1:0": 1000000,
    "bedrock:us.amazon.nova-pro-v1:0": 300000,
    "bedrock:us.amazon.nova-lite-v1:0": 300000,
    "bedrock:us.amazon.nova-micro-v1:0": 128000,
    "bedrock:us.anthropic.claude-3-7-sonnet-20250219-v1:0": 200000,
    "bedrock:us.anthropic.claude-sonnet-4-20250514-v1:0": 200000,
    "bedrock:us.anthropic.claude-opus-4-20250514-v1:0": 200000,
    "anthropic.claude-opus-4-1-20250805-v1:0": 200000,
}

def get_model_token_limit(model_string):
    """Look up the token limit for a specific model.
    
    Args:
        model_string: The model identifier string to look up
        
    Returns:
        Token limit as integer if found, None if model not in lookup table
    """
    # Search through known model token limits
    for model_key, token_limit in MODEL_TOKEN_LIMITS.items():
        if model_key in model_string:
            return token_limit
    
    # Model not found in lookup table
    return None

def remove_up_to_last_ai_message(messages: list[MessageLikeRepresentation]) -> list[MessageLikeRepresentation]:
    """Truncate message history by removing up to the last AI message.
    
    This is useful for handling token limit exceeded errors by removing recent context.
    
    Args:
        messages: List of message objects to truncate
        
    Returns:
        Truncated message list up to (but not including) the last AI message
    """
    # Search backwards through messages to find the last AI message
    for i in range(len(messages) - 1, -1, -1):
        if isinstance(messages[i], AIMessage):
            # Return everything up to (but not including) the last AI message
            return messages[:i]
    
    # No AI messages found, return original list
    return messages

##########################
# Misc Utils
##########################

def get_today_str() -> str:
    """Get current date formatted for display in prompts and outputs.
    
    Returns:
        Human-readable date string in format like 'Mon Jan 15, 2024'
    """
    now = datetime.now()
    return f"{now:%a} {now:%b} {now.day}, {now:%Y}"

def get_config_value(value):
    """Extract value from configuration, handling enums and None values."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    elif isinstance(value, dict):
        return value
    else:
        return value.value

def get_api_key_for_model(model_name: str, config: RunnableConfig):
    """Get API key for a specific model from environment or config."""
    should_get_from_config = os.getenv("GET_API_KEYS_FROM_CONFIG", "false")
    model_name = model_name.lower()
    if should_get_from_config.lower() == "true":
        api_keys = config.get("configurable", {}).get("apiKeys", {})
        if not api_keys:
            return None
        if model_name.startswith("openai:"):
            return api_keys.get("OPENAI_API_KEY")
        elif model_name.startswith("anthropic:"):
            return api_keys.get("ANTHROPIC_API_KEY")
        elif model_name.startswith("google"):
            return api_keys.get("GOOGLE_API_KEY")
        return None
    else:
        if model_name.startswith("openai:"): 
            return os.getenv("OPENAI_API_KEY")
        elif model_name.startswith("anthropic:"):
            return os.getenv("ANTHROPIC_API_KEY")
        elif model_name.startswith("google"):
            return os.getenv("GOOGLE_API_KEY")
        return None


def get_chat_model_config(
    model_name: str,
    max_tokens: int,
    config: RunnableConfig,
) -> dict[str, Any]:
    """Build runtime configuration for a chat model."""
    model_config: dict[str, Any] = {
        "model": model_name,
        "max_tokens": max_tokens,
        "api_key": get_api_key_for_model(model_name, config),
        "tags": ["langsmith:nostream"],
    }
    if model_name.lower().startswith("openai:"):
        openai_base_url = Configuration.from_runnable_config(config).openai_base_url
        if openai_base_url:
            model_config["base_url"] = openai_base_url.strip().rstrip("/")
    return model_config


def get_tavily_api_key(config: RunnableConfig):
    """Get Tavily API key from environment or config."""
    should_get_from_config = os.getenv("GET_API_KEYS_FROM_CONFIG", "false")
    if should_get_from_config.lower() == "true":
        api_keys = config.get("configurable", {}).get("apiKeys", {})
        if not api_keys:
            return None
        return api_keys.get("TAVILY_API_KEY")
    else:
        return os.getenv("TAVILY_API_KEY")
