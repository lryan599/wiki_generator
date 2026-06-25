"""FastAPI app for generating structured findings from explicit retrieval queries."""

import asyncio
import os
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import ToolMessage
from pydantic import BaseModel, Field

from open_deep_research.deep_researcher import compress_research
from open_deep_research.research import StructuredResearch
from open_deep_research.utils import knowledge_base_search

DEFAULT_RETRIEVAL_MAX_CONCURRENCY = 5
RETRIEVAL_MAX_CONCURRENCY_ENV = "RETRIEVAL_MAX_CONCURRENCY"


class RetrievalQuery(BaseModel):
    """A single retrieval query with an optional workspace override."""

    query: str = Field(min_length=1)
    workspace_id: str | None = None


class RetrievalFindingsRequest(BaseModel):
    """Request body for concurrent query-to-findings generation."""

    queries: list[str | RetrievalQuery] = Field(min_length=1)
    workspace_id: str | None = None
    knowledge_base_url: str | None = None
    summarize_findings: bool = True
    text_topk: int = Field(default=10, ge=0, le=50)
    image_topk: int = Field(default=3, ge=0, le=20)
    table_topk: int = Field(default=3, ge=0, le=20)
    chart_topk: int = Field(default=3, ge=0, le=20)
    configurable: dict[str, Any] = Field(default_factory=dict)

    def normalized_queries(self) -> list[RetrievalQuery]:
        """Normalize string and object query forms into query objects."""
        normalized: list[RetrievalQuery] = []
        for item in self.queries:
            if isinstance(item, str):
                query = item.strip()
                if query:
                    normalized.append(RetrievalQuery(query=query))
                continue
            query = item.query.strip()
            if query:
                normalized.append(item.model_copy(update={"query": query}))
        if not normalized:
            raise ValueError("At least one non-empty query is required.")
        return normalized


class RetrievalResult(BaseModel):
    """Retrieval output generated for one query."""

    query: str
    workspace_id: str | None = None
    structured_research: StructuredResearch | None = None
    retrieval_result: dict[str, Any] | None = None


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
    query: RetrievalQuery,
    request: RetrievalFindingsRequest,
) -> tuple[ToolMessage, str | None, dict[str, Any]]:
    """Run one explicit query through the knowledge-base search tool."""
    workspace_id = query.workspace_id or request.workspace_id
    configurable = dict(request.configurable)
    if request.knowledge_base_url:
        configurable["knowledge_base_url"] = request.knowledge_base_url
    if workspace_id:
        configurable["workspace_id"] = workspace_id
    runtime_config = {"configurable": configurable}

    args: dict[str, Any] = {
        "queries": [query.query],
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


async def generate_result_for_query(
    query: RetrievalQuery,
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
            query=query.query,
            workspace_id=workspace_id,
            retrieval_result=retrieval_result,
        )

    compressed = await compress_research(
        {
            "research_topic": query.query,
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
        query=query.query,
        workspace_id=workspace_id,
        structured_research=structured_research,
    )


async def generate_findings_for_queries(
    request: RetrievalFindingsRequest,
) -> RetrievalFindingsResponse:
    """Generate retrieval results for all queries with a bounded concurrency limit."""
    queries = request.normalized_queries()
    semaphore = asyncio.Semaphore(get_retrieval_max_concurrency())

    async def run_query(query: RetrievalQuery) -> RetrievalResult:
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


@app.get("/health")
@app.get("/api/v1/retrieval/health")
async def health() -> dict[str, str]:
    """Return API health status."""
    return {"status": "ok"}


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
