"""FastAPI app for generating structured findings from explicit retrieval queries."""

import asyncio
import os
import re
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import ToolMessage
from langchain_core.tools import ToolException
from pydantic import BaseModel, Field

from open_deep_research.configuration import Configuration
from open_deep_research.deep_researcher import compress_research
from open_deep_research.research import StructuredResearch
from open_deep_research.utils import (
    _resolve_workspace_config,
    knowledge_base_search,
    query_workspace_async,
)

DEFAULT_RETRIEVAL_MAX_CONCURRENCY = 5
RETRIEVAL_MAX_CONCURRENCY_ENV = "RETRIEVAL_MAX_CONCURRENCY"
DEFAULT_WIKI_SEARCH_LIMIT = 8
DEFAULT_WIKI_SEARCH_CHUNK_TOP_K = 20
DEFAULT_WIKI_SEARCH_SIMILARITY_THRESHOLD = 0.2
DEFAULT_WIKI_SEARCH_WORKSPACE_ID = (
    os.getenv("WIKI_SEARCH_WORKSPACE_ID") or "die_casting_generated_wiki"
)
WIKI_SEARCH_SUMMARY_LIMIT = 240
ABSOLUTE_URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.IGNORECASE)


class RetrievalFindingsRequest(BaseModel):
    """Request body for concurrent query-to-findings generation."""

    queries: list[str] = Field(min_length=1)
    workspace_id: str | None = None
    knowledge_base_url: str | None = None
    summarize_findings: bool = True
    text_topk: int = Field(default=10, ge=0, le=50)
    image_topk: int = Field(default=3, ge=0, le=20)
    table_topk: int = Field(default=3, ge=0, le=20)
    chart_topk: int = Field(default=3, ge=0, le=20)

    def normalized_queries(self) -> list[str]:
        """Normalize query strings and drop empty items."""
        normalized: list[str] = []
        for item in self.queries:
            query = item.strip()
            if query:
                normalized.append(query)
        if not normalized:
            raise ValueError("At least one non-empty query is required.")
        return normalized


class WikiSearchRequest(BaseModel):
    """Request body for low-latency MkDocs search backed by the Query API."""

    query: str = Field(min_length=1)
    workspace_id: str | None = DEFAULT_WIKI_SEARCH_WORKSPACE_ID
    knowledge_base_url: str | None = None
    limit: int = Field(default=DEFAULT_WIKI_SEARCH_LIMIT, ge=1, le=50)
    chunk_top_k: int = Field(default=DEFAULT_WIKI_SEARCH_CHUNK_TOP_K, ge=1, le=100)
    similarity_threshold: float = Field(
        default=DEFAULT_WIKI_SEARCH_SIMILARITY_THRESHOLD,
        ge=0,
        le=1,
    )

    def normalized_query(self) -> str:
        """Normalize the query string."""
        query = self.query.strip()
        if not query:
            raise ValueError("Query must not be empty.")
        return query


class RetrievalResult(BaseModel):
    """Retrieval output generated for one query."""

    query: str
    workspace_id: str | None = None
    structured_research: StructuredResearch | None = None
    retrieval_result: dict[str, Any] | None = None


class WikiSearchResult(BaseModel):
    """One result formatted for MkDocs' built-in search renderer."""

    title: str
    location: str
    text: str = ""
    summary: str = ""
    score: float | None = None
    source_uuid: str | None = None
    workspace_id: str | None = None


class WikiSearchResponse(BaseModel):
    """Response body consumed by the MkDocs search worker."""

    results: list[WikiSearchResult]


class RetrievalFindingsResponse(BaseModel):
    """Response body for query-to-findings generation."""

    research_results: list[RetrievalResult]


app = FastAPI(title="Open Deep Research Retrieval API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


async def search_knowledge_base_for_query(
    query: str,
    request: RetrievalFindingsRequest,
) -> tuple[ToolMessage, str | None, dict[str, Any]]:
    """Run one explicit query through the knowledge-base search tool."""
    workspace_id = request.workspace_id
    configurable: dict[str, Any] = {}
    if request.knowledge_base_url:
        configurable["knowledge_base_url"] = request.knowledge_base_url
    if workspace_id:
        configurable["workspace_id"] = workspace_id
    runtime_config = {"configurable": configurable}

    args: dict[str, Any] = {
        "queries": [query],
        "text_topk": request.text_topk,
        "image_topk": request.image_topk,
        "table_topk": request.table_topk,
        "chart_topk": request.chart_topk,
    }
    if workspace_id:
        args["workspace_id"] = workspace_id

    tool_message = await knowledge_base_search.ainvoke(
        {
            "name": "knowledge_base_search",
            "args": args,
            "id": f"retrieval-{uuid4()}",
            "type": "tool_call",
        },
        runtime_config,
    )
    if not isinstance(tool_message, ToolMessage):
        raise TypeError("knowledge_base_search did not return a ToolMessage.")

    return tool_message, workspace_id, runtime_config


def extract_retrieval_result(tool_message: ToolMessage) -> dict[str, Any]:
    """Extract the normalized Query API result from a knowledge-base tool message."""
    artifact = tool_message.artifact
    if not isinstance(artifact, dict) or artifact.get("type") != "knowledge_base_search":
        raise TypeError("knowledge_base_search returned an invalid artifact.")

    results = artifact.get("results")
    if not isinstance(results, list) or not results:
        raise TypeError("knowledge_base_search returned no retrieval results.")

    retrieval_result = results[0]
    if not isinstance(retrieval_result, dict):
        raise TypeError("knowledge_base_search returned an invalid retrieval result.")

    return retrieval_result


def build_wiki_search_runtime_config(
    request: WikiSearchRequest,
) -> tuple[dict[str, Any], str, str, float]:
    """Resolve Query API config for wiki search."""
    configurable: dict[str, Any] = {}
    if request.knowledge_base_url:
        configurable["knowledge_base_url"] = request.knowledge_base_url
    if request.workspace_id:
        configurable["workspace_id"] = request.workspace_id
    runtime_config = {"configurable": configurable}
    base_url, workspace_id = _resolve_workspace_config(
        runtime_config,
        request.workspace_id,
    )
    timeout_seconds = Configuration.from_runnable_config(
        runtime_config,
    ).knowledge_base_query_timeout_seconds
    return runtime_config, base_url, workspace_id, timeout_seconds


def _first_string(*values: Any) -> str | None:
    """Return the first non-empty string from values."""
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _item_attributes(item: dict[str, Any]) -> dict[str, Any]:
    """Return item attributes when they are object-like."""
    attributes = item.get("attributes")
    if isinstance(attributes, dict):
        return attributes
    return {}


def _is_url(value: str) -> bool:
    """Return whether value is an absolute URL."""
    return bool(ABSOLUTE_URL_RE.match(value))


def _wiki_location_from_path(value: str) -> str | None:
    """Convert a source path to a MkDocs location when possible."""
    path = value.strip().replace("\\", "/")
    if not path:
        return None
    if _is_url(path):
        return path

    markers = ("wiki_site/docs/", "docs/")
    for marker in markers:
        if marker in path:
            path = path.split(marker, 1)[1]
            break

    path = path.lstrip("/")
    if not path:
        return None

    if path.endswith(".md"):
        path = path[:-3]
        if path == "index":
            return ""
        if path.endswith("/index"):
            path = path[: -len("/index")]
        return path.rstrip("/") + "/"

    if path.startswith("entries/"):
        return path.rstrip("/") + "/"

    return None


def _wiki_location_from_title(value: str) -> str | None:
    """Convert a known wiki entry title or filename to a MkDocs entry location."""
    title = value.strip()
    if not title or _is_url(title):
        return None

    path_location = _wiki_location_from_path(title)
    if path_location is not None:
        return path_location

    if title.endswith(".md"):
        title = title[:-3]
    title = title.strip().strip("/")
    if not title or "/" in title:
        return None
    return f"entries/{title}/"


def _wiki_location_from_item(item: dict[str, Any]) -> str | None:
    """Resolve an item to an internal MkDocs location or external resource URL."""
    attributes = _item_attributes(item)
    path = _first_string(
        item.get("location"),
        item.get("path"),
        item.get("source"),
        item.get("source_path"),
        item.get("file_path"),
        item.get("file_name"),
        item.get("filename"),
        item.get("relative_path"),
        item.get("source_uri"),
        item.get("uri"),
        attributes.get("mkdocs_location"),
        attributes.get("wiki_location"),
        attributes.get("location"),
        attributes.get("path"),
        attributes.get("source"),
        attributes.get("source_path"),
        attributes.get("file_path"),
        attributes.get("file_name"),
        attributes.get("filename"),
        attributes.get("relative_path"),
        attributes.get("source_uri"),
        attributes.get("uri"),
        attributes.get("catalog_path"),
    )
    if path:
        location = _wiki_location_from_path(path)
        if location is not None:
            return location

    title = _first_string(
        attributes.get("entry_title"),
        attributes.get("wiki_title"),
        attributes.get("document_title"),
        attributes.get("source_title"),
        attributes.get("title"),
        attributes.get("catalog_path"),
        attributes.get("file_name"),
        attributes.get("filename"),
        item.get("entry_title"),
        item.get("wiki_title"),
        item.get("document_title"),
        item.get("source_title"),
        item.get("title"),
    )
    if title:
        location = _wiki_location_from_title(title)
        if location is not None:
            return location

    return _first_string(item.get("url"))


def _title_from_location(location: str | None) -> str | None:
    """Infer a readable title from a MkDocs location or path."""
    if not location or _is_url(location):
        return None
    path = location.strip("/").replace("\\", "/")
    if not path:
        return None
    name = path.rsplit("/", 1)[-1]
    if name.endswith(".md"):
        name = name[:-3]
    return name or None


def _wiki_search_title(
    item: dict[str, Any],
    query: str,
    location: str | None,
) -> str:
    """Build a display title for a wiki search result."""
    attributes = _item_attributes(item)
    return _first_string(
        attributes.get("entry_title"),
        attributes.get("wiki_title"),
        attributes.get("title"),
        attributes.get("document_title"),
        attributes.get("source_title"),
        attributes.get("catalog_path"),
        _title_from_location(location),
        item.get("caption"),
        item.get("summary"),
        item.get("description"),
        item.get("name"),
        query,
    ) or query


def _collapse_whitespace(value: str) -> str:
    """Collapse whitespace in a string."""
    return re.sub(r"\s+", " ", value).strip()


def _strip_markdown_front_matter(value: str) -> str:
    """Remove leading YAML front matter from a markdown chunk."""
    if not value.startswith("---"):
        return value

    match = re.match(r"^---\s*\r?\n.*?\r?\n---\s*(?:\r?\n|$)", value, re.DOTALL)
    if not match:
        return value
    return value[match.end() :]


def _wiki_search_summary(item: dict[str, Any]) -> str:
    """Build a compact result summary."""
    text = _first_string(
        item.get("enhanced_str"),
        item.get("content"),
        item.get("summary"),
        item.get("description"),
        item.get("caption"),
        item.get("body"),
    )
    if not text:
        return ""
    text = _strip_markdown_front_matter(text)
    text = _collapse_whitespace(text)
    if len(text) <= WIKI_SEARCH_SUMMARY_LIMIT:
        return text
    return text[: WIKI_SEARCH_SUMMARY_LIMIT - 1].rstrip() + "..."


def build_wiki_search_response(
    retrieval_result: dict[str, Any],
    *,
    query: str,
    workspace_id: str | None,
    limit: int,
) -> WikiSearchResponse:
    """Convert normalized Query API results into MkDocs search results."""
    results: list[WikiSearchResult] = []
    seen_locations: set[str] = set()

    for item in retrieval_result.get("text_results") or []:
        if not isinstance(item, dict):
            continue

        location = _wiki_location_from_item(item)
        if not location or location in seen_locations:
            continue
        seen_locations.add(location)

        summary = _wiki_search_summary(item)
        result = WikiSearchResult(
            title=_wiki_search_title(item, query, location),
            location=location,
            text=summary,
            summary=summary,
            score=item.get("score") if isinstance(item.get("score"), (int, float)) else None,
            source_uuid=item.get("uuid") if isinstance(item.get("uuid"), str) else None,
            workspace_id=workspace_id,
        )
        results.append(result)
        if len(results) >= limit:
            break

    return WikiSearchResponse(results=results)


async def generate_wiki_search_results(
    request: WikiSearchRequest,
) -> WikiSearchResponse:
    """Run a low-latency workspace search and format it for MkDocs."""
    query = request.normalized_query()
    _, base_url, workspace_id, timeout_seconds = build_wiki_search_runtime_config(
        request,
    )
    retrieval_result = await query_workspace_async(
        query=query,
        workspace_id=workspace_id,
        base_url=base_url,
        chunk_top_k=request.chunk_top_k,
        similarity_threshold=request.similarity_threshold,
        timeout_seconds=timeout_seconds,
    )
    return build_wiki_search_response(
        retrieval_result,
        query=query,
        workspace_id=workspace_id,
        limit=request.limit,
    )


async def generate_result_for_query(
    query: str,
    request: RetrievalFindingsRequest,
) -> RetrievalResult:
    """Run one explicit query through search and optional findings compression."""
    tool_message, workspace_id, runtime_config = await search_knowledge_base_for_query(
        query,
        request,
    )
    retrieval_result = extract_retrieval_result(tool_message)

    if not request.summarize_findings:
        return RetrievalResult(
            query=query,
            workspace_id=workspace_id,
            retrieval_result=retrieval_result,
        )

    compressed = await compress_research(
        {
            "research_topic": query,
            "researcher_messages": [tool_message],
            "tool_call_iterations": 1,
        },
        runtime_config,
    )
    structured_research = compressed.get("structured_research")
    if structured_research is None:
        raise RuntimeError(compressed.get("compressed_research") or "No structured research returned.")

    if not isinstance(structured_research, StructuredResearch):
        structured_research = StructuredResearch.model_validate(structured_research)

    return RetrievalResult(
        query=query,
        workspace_id=workspace_id,
        structured_research=structured_research,
    )


async def generate_findings_for_queries(
    request: RetrievalFindingsRequest,
) -> RetrievalFindingsResponse:
    """Generate retrieval results for all queries with a bounded concurrency limit."""
    queries = request.normalized_queries()
    semaphore = asyncio.Semaphore(get_retrieval_max_concurrency())

    async def run_query(query: str) -> RetrievalResult:
        async with semaphore:
            return await generate_result_for_query(query, request)

    results = await asyncio.gather(*(run_query(query) for query in queries))
    return RetrievalFindingsResponse(research_results=results)


def get_retrieval_max_concurrency() -> int:
    """Read the API query concurrency limit from the environment."""
    raw_value = os.getenv(RETRIEVAL_MAX_CONCURRENCY_ENV)
    if raw_value in (None, ""):
        return DEFAULT_RETRIEVAL_MAX_CONCURRENCY

    try:
        value = int(raw_value)
    except ValueError as exc:
        raise RuntimeError(
            f"{RETRIEVAL_MAX_CONCURRENCY_ENV} must be an integer."
        ) from exc
    if not 1 <= value <= 20:
        raise RuntimeError(
            f"{RETRIEVAL_MAX_CONCURRENCY_ENV} must be between 1 and 20."
        )
    return value


def _tool_exception_status_code(exc: ToolException) -> int:
    """Map retrieval tool failures to API-facing status codes."""
    message = str(exc)
    if "KNOWLEDGE_BASE_URL" in message or "not configured" in message:
        return 500
    if "timed out" in message:
        return 504
    if message.startswith("Query API request failed with HTTP"):
        return 502
    return 422


def _raise_tool_http_exception(exc: ToolException) -> None:
    """Raise an HTTPException for a retrieval tool failure."""
    raise HTTPException(
        status_code=_tool_exception_status_code(exc),
        detail=str(exc),
    ) from exc


@app.get("/health")
@app.get("/api/v1/retrieval/health")
async def health() -> dict[str, str]:
    """Return API health status."""
    return {
        "status": "ok",
        "knowledge_base_configured": str(bool(os.getenv("KNOWLEDGE_BASE_URL"))).lower(),
    }


@app.post(
    "/api/v1/retrieval/findings",
    response_model=RetrievalFindingsResponse,
    response_model_exclude_none=True,
)
async def retrieval_findings(
    request: RetrievalFindingsRequest,
) -> RetrievalFindingsResponse:
    """Generate structured findings for explicit retrieval queries."""
    try:
        return await generate_findings_for_queries(request)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Failed to generate retrieval findings.",
                "error": str(exc),
                "error_type": type(exc).__name__,
            },
        ) from exc


@app.get(
    "/api/v1/wiki-search",
    response_model=WikiSearchResponse,
    response_model_exclude_none=True,
)
async def wiki_search_get(
    q: str = Query(min_length=1),
    workspace_id: str | None = Query(default=DEFAULT_WIKI_SEARCH_WORKSPACE_ID),
    knowledge_base_url: str | None = None,
    limit: int = Query(default=DEFAULT_WIKI_SEARCH_LIMIT, ge=1, le=50),
    chunk_top_k: int = Query(default=DEFAULT_WIKI_SEARCH_CHUNK_TOP_K, ge=1, le=100),
    similarity_threshold: float = Query(
        default=DEFAULT_WIKI_SEARCH_SIMILARITY_THRESHOLD,
        ge=0,
        le=1,
    ),
) -> WikiSearchResponse:
    """Search wiki chunks through the Query API without LLM summarization."""
    request = WikiSearchRequest(
        query=q,
        workspace_id=workspace_id,
        knowledge_base_url=knowledge_base_url,
        limit=limit,
        chunk_top_k=chunk_top_k,
        similarity_threshold=similarity_threshold,
    )
    try:
        return await generate_wiki_search_results(request)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except ToolException as exc:
        _raise_tool_http_exception(exc)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Failed to search wiki.",
                "error": str(exc),
                "error_type": type(exc).__name__,
            },
        ) from exc


@app.post(
    "/api/v1/wiki-search",
    response_model=WikiSearchResponse,
    response_model_exclude_none=True,
)
async def wiki_search_post(
    request: WikiSearchRequest,
) -> WikiSearchResponse:
    """Search wiki chunks through the Query API without LLM summarization."""
    try:
        return await generate_wiki_search_results(request)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except ToolException as exc:
        _raise_tool_http_exception(exc)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "message": "Failed to search wiki.",
                "error": str(exc),
                "error_type": type(exc).__name__,
            },
        ) from exc
