import sys
import types

from pydantic import BaseModel

langchain_core = types.ModuleType("langchain_core")
messages = types.ModuleType("langchain_core.messages")
tools = types.ModuleType("langchain_core.tools")


class ToolMessage:
    pass


class ToolException(Exception):
    pass


messages.ToolMessage = ToolMessage
tools.ToolException = ToolException
sys.modules.setdefault("langchain_core", langchain_core)
sys.modules.setdefault("langchain_core.messages", messages)
sys.modules.setdefault("langchain_core.tools", tools)

configuration = types.ModuleType("open_deep_research.configuration")


class Configuration:
    knowledge_base_query_timeout_seconds = 120

    @staticmethod
    def from_runnable_config(config):
        return Configuration()


configuration.Configuration = Configuration
sys.modules.setdefault("open_deep_research.configuration", configuration)

deep_researcher = types.ModuleType("open_deep_research.deep_researcher")


async def compress_research(*args, **kwargs):
    return {}


deep_researcher.compress_research = compress_research
sys.modules.setdefault("open_deep_research.deep_researcher", deep_researcher)

research = types.ModuleType("open_deep_research.research")


class StructuredResearch(BaseModel):
    pass


research.StructuredResearch = StructuredResearch
sys.modules.setdefault("open_deep_research.research", research)

utils = types.ModuleType("open_deep_research.utils")


def _resolve_workspace_config(config, workspace_id):
    return "http://example.invalid", workspace_id or "die_casting_generated_wiki"


async def query_workspace_async(*args, **kwargs):
    return {}


class FakeKnowledgeBaseSearch:
    async def ainvoke(self, *args, **kwargs):
        return ToolMessage()


utils._resolve_workspace_config = _resolve_workspace_config
utils.query_workspace_async = query_workspace_async
utils.knowledge_base_search = FakeKnowledgeBaseSearch()
sys.modules.setdefault("open_deep_research.utils", utils)

from open_deep_research.retrieval_api import (
    DEFAULT_WIKI_SEARCH_WORKSPACE_ID,
    WikiSearchRequest,
    _wiki_location_from_path,
    build_wiki_search_response,
)


def test_wiki_search_request_defaults_to_generated_wiki_workspace():
    request = WikiSearchRequest(query="H13钢")

    assert request.workspace_id == DEFAULT_WIKI_SEARCH_WORKSPACE_ID
    assert request.workspace_id == "die_casting_generated_wiki"


def test_wiki_location_from_path_maps_markdown_entry_to_mkdocs_location():
    assert (
        _wiki_location_from_path("wiki_site/docs/entries/H13钢.md")
        == "entries/H13钢/"
    )
    assert _wiki_location_from_path("entries/H13钢.md") == "entries/H13钢/"
    assert _wiki_location_from_path("docs/index.md") == ""


def test_build_wiki_search_response_formats_text_chunks_for_mkdocs():
    response = build_wiki_search_response(
        {
            "query": "H13钢",
            "text_results": [
                {
                    "uuid": "chunk-1",
                    "score": 0.91,
                    "content": "H13钢是常用热作模具钢，常用于压铸模具。",
                    "attributes": {
                        "source_path": "wiki_site/docs/entries/H13钢.md",
                        "entry_title": "H13钢",
                    },
                },
            ],
        },
        query="H13钢",
        workspace_id="die_casting_generated_wiki",
        limit=8,
    )

    assert len(response.results) == 1
    result = response.results[0]
    assert result.title == "H13钢"
    assert result.location == "entries/H13钢/"
    assert result.summary == "H13钢是常用热作模具钢，常用于压铸模具。"
    assert result.score == 0.91
    assert result.source_uuid == "chunk-1"
    assert result.workspace_id == "die_casting_generated_wiki"


def test_build_wiki_search_response_deduplicates_locations():
    response = build_wiki_search_response(
        {
            "query": "H13钢",
            "text_results": [
                {
                    "content": "first",
                    "attributes": {"wiki_location": "entries/H13钢/"},
                },
                {
                    "content": "second",
                    "attributes": {"source_path": "wiki_site/docs/entries/H13钢.md"},
                },
            ],
        },
        query="H13钢",
        workspace_id="die_casting_generated_wiki",
        limit=8,
    )

    assert len(response.results) == 1
    assert response.results[0].summary == "first"


def test_build_wiki_search_response_can_infer_location_from_entry_title():
    response = build_wiki_search_response(
        {
            "query": "热疲劳",
            "text_results": [
                {
                    "content": "热疲劳裂纹是压铸模常见失效形式。",
                    "attributes": {"entry_title": "热疲劳裂纹"},
                },
            ],
        },
        query="热疲劳",
        workspace_id="die_casting_generated_wiki",
        limit=8,
    )

    assert len(response.results) == 1
    assert response.results[0].title == "热疲劳裂纹"
    assert response.results[0].location == "entries/热疲劳裂纹/"


def test_build_wiki_search_response_uses_catalog_path_and_strips_front_matter():
    response = build_wiki_search_response(
        {
            "query": "H13钢",
            "text_results": [
                {
                    "content": (
                        "---\n"
                        'version: "v3"\n'
                        'generated_at: "2026-06-18T05:13:52+00:00"\n'
                        "---\n"
                        "# H13钢\n\n"
                        "H13钢是常用热作模具钢。"
                    ),
                    "attributes": {"catalog_path": "H13钢"},
                },
            ],
        },
        query="H13钢",
        workspace_id="die_casting_generated_wiki",
        limit=8,
    )

    assert len(response.results) == 1
    assert response.results[0].title == "H13钢"
    assert response.results[0].location == "entries/H13钢/"
    assert response.results[0].summary == "# H13钢 H13钢是常用热作模具钢。"
