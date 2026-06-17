import asyncio

import pytest
from langchain_core.tools import ToolException

from open_deep_research import utils
from open_deep_research.configuration import SearchAPI


class FakeResponse:
    def __init__(self, payload, status=200, headers=None):
        self.payload = payload
        self.status = status
        self.headers = headers or {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        return False

    async def text(self):
        if isinstance(self.payload, bytes):
            return self.payload.decode("utf-8", errors="replace")
        return self.payload

    async def read(self):
        if isinstance(self.payload, bytes):
            return self.payload
        return self.payload.encode("utf-8")


class FakeSession:
    requests = []
    get_requests = []
    timeouts = []
    response = None

    def __init__(self, timeout):
        self.timeout = timeout
        self.timeouts.append(timeout.total)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        return False

    def post(self, url, json):
        self.requests.append((url, json))
        return self.response

    def get(self, url):
        self.get_requests.append(url)
        return self.response


def test_query_workspace_async_requests_and_normalizes_multimodal_data(monkeypatch):
    FakeSession.requests = []
    FakeSession.timeouts = []
    FakeSession.response = FakeResponse(
        """{
          "elapsed_time": 0.1,
          "llm_calls": 0,
          "response": null,
          "metadata": {
            "labels": ["TextNode", "ImageNode"],
            "text_results": [{
              "uuid": "text-1",
              "name": "TextNode0",
              "group_id": "doc-1",
              "labels": ["TextNode"],
              "content": "text evidence",
              "enhanced_str": "enhanced evidence",
              "score": 0.9,
              "attributes": {"catalog_path": "Chapter 1"}
            }],
            "image_results": [{
              "uuid": "image-1",
              "name": "ImageNode0",
              "group_id": "doc-1",
              "labels": ["ImageNode"],
              "url": "images/example.jpg",
              "caption": "Figure 1",
              "summary": "diagram",
              "score": 0.8,
              "attributes": {}
            }],
            "table_results": [{
              "uuid": "table-1",
              "body": "| a | b |",
              "summary": "table summary",
              "score": 0.7
            }],
            "chart_results": [{
              "uuid": "chart-1",
              "url": "charts/example.png",
              "description": "trend chart",
              "score": 0.6
            }]
          }
        }"""
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    result = asyncio.run(
        utils.query_workspace_async(
            query="casting checks",
            workspace_id="manual workspace",
            base_url="http://127.0.0.1:8000/",
            chunk_top_k=7,
            similarity_threshold=0.4,
            timeout_seconds=45,
        )
    )

    request_url, request_payload = FakeSession.requests[0]
    assert request_url == (
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/query"
    )
    assert request_payload["naive_kwargs"] == {"enable_multimodal": True}
    assert request_payload["only_need_data"] is True
    assert request_payload["enable_rerank"] is False
    assert "only_need_rerank_data" not in request_payload
    assert request_payload["chunk_top_k"] == 7
    assert request_payload["similarity_threshold"] == 0.4
    assert FakeSession.timeouts == [45]
    assert result["query"] == "casting checks"
    assert result["text_results"] == [{
        "uuid": "text-1",
        "name": "TextNode0",
        "group_id": "doc-1",
        "labels": ["TextNode"],
        "attributes": {"catalog_path": "Chapter 1"},
        "content": "text evidence",
        "enhanced_str": "enhanced evidence",
        "url": (
            "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
            "document-elements/text-1/resource"
        ),
        "score": 0.9,
    }]
    assert result["image_results"][0] == {
        "uuid": "image-1",
        "name": "ImageNode0",
        "group_id": "doc-1",
        "labels": ["ImageNode"],
        "attributes": {},
        "url": (
            "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
            "document-elements/image-1/resource"
        ),
        "caption": "Figure 1",
        "summary": "diagram",
        "score": 0.8,
    }
    assert result["table_results"][0] == {
        "uuid": "table-1",
        "body": "| a | b |",
        "summary": "table summary",
        "score": 0.7,
    }
    assert result["chart_results"][0]["url"] == (
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
        "document-elements/chart-1/resource"
    )
    assert "metadata" not in result
    assert "elapsed_time" not in result


def test_format_knowledge_base_results_exposes_only_normalized_evidence():
    formatted = utils._format_knowledge_base_results([{
        "query": "casting checks",
        "text_results": [{"uuid": "text-1", "content": "text evidence"}],
        "image_results": [{
            "uuid": "image-1",
            "name": "ImageNode0",
            "group_id": "doc-1",
            "labels": ["ImageNode"],
            "attributes": {"page": 2},
            "url": "http://127.0.0.1:8000/images/example.jpg",
            "summary": "diagram",
        }],
        "table_results": [],
        "chart_results": [],
    }])

    assert "## Query 1: casting checks" in formatted
    assert "### Text results" in formatted
    assert "### Image results" in formatted
    assert '"uuid": "image-1"' in formatted
    assert '"name": "ImageNode0"' in formatted
    assert '"group_id": "doc-1"' in formatted
    assert '"labels": ["ImageNode"]' in formatted
    assert '"attributes": {"page": 2}' in formatted
    assert "elapsed_time" not in formatted
    assert "metadata" not in formatted


def test_limit_knowledge_base_results_applies_type_specific_top_k():
    results = [{
        "query": "casting checks",
        "text_results": [{"uuid": f"text-{index}"} for index in range(4)],
        "image_results": [{"uuid": f"image-{index}"} for index in range(4)],
        "table_results": [{"uuid": f"table-{index}"} for index in range(4)],
        "chart_results": [{"uuid": f"chart-{index}"} for index in range(4)],
    }]

    limited = utils._limit_knowledge_base_results(
        results,
        text_topk=2,
        image_topk=1,
        table_topk=0,
        chart_topk=-1,
    )

    assert [item["uuid"] for item in limited[0]["text_results"]] == [
        "text-0",
        "text-1",
    ]
    assert [item["uuid"] for item in limited[0]["image_results"]] == ["image-0"]
    assert limited[0]["table_results"] == []
    assert limited[0]["chart_results"] == []
    assert len(results[0]["text_results"]) == 4


def test_query_workspace_async_rejects_missing_metadata(monkeypatch):
    FakeSession.response = FakeResponse('{"response": null, "metadata": null}')
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    with pytest.raises(ToolException, match="retrieval metadata"):
        asyncio.run(
            utils.query_workspace_async(
                query="query",
                workspace_id="workspace",
                base_url="http://127.0.0.1:8000",
            )
        )


def test_query_workspace_async_resolves_image_url(monkeypatch):
    FakeSession.response = FakeResponse(
        '{"metadata":{"text_results":[],"image_results":['
        '{"uuid":"image-1","url":"images/example.jpg"}],'
        '"table_results":[],"chart_results":[]}}'
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    result = asyncio.run(
        utils.query_workspace_async(
            query="query",
            workspace_id="workspace",
            base_url="http://127.0.0.1:8000",
        )
    )

    assert result["image_results"][0]["url"] == (
        "http://127.0.0.1:8000/api/v1/workspaces/workspace/"
        "document-elements/image-1/resource"
    )


def test_query_workspace_async_rejects_invalid_base_url():
    with pytest.raises(ToolException, match="absolute HTTP"):
        asyncio.run(
            utils.query_workspace_async(
                query="query",
                workspace_id="workspace",
                base_url="localhost:8000",
            )
        )


def test_knowledge_base_search_preserves_normalized_results_as_artifact(monkeypatch):
    request_kwargs = []

    async def fake_query_workspace_async(**kwargs):
        request_kwargs.append(kwargs)
        return {
            "query": kwargs["query"],
            "text_results": [{
                "uuid": f"text-{index}",
                "name": "TextNode0",
                "group_id": "manual-1",
                "labels": ["TextNode"],
                "attributes": {},
                "content": "trusted evidence",
            } for index in range(12)],
            "image_results": [{"uuid": f"image-{index}"} for index in range(5)],
            "table_results": [{"uuid": f"table-{index}"} for index in range(5)],
            "chart_results": [{"uuid": f"chart-{index}"} for index in range(5)],
        }

    monkeypatch.setattr(utils, "query_workspace_async", fake_query_workspace_async)
    tool_message = asyncio.run(utils.knowledge_base_search.ainvoke(
        {
            "name": "knowledge_base_search",
            "args": {"queries": ["inspection"]},
            "id": "call-1",
            "type": "tool_call",
        },
        {
            "configurable": {
                "knowledge_base_url": "http://127.0.0.1:8000",
                "workspace_id": "manual-1",
                "search_api": SearchAPI.NONE.value,
                "knowledge_base_query_timeout_seconds": 25,
            }
        },
    ))

    assert tool_message.content.startswith("Knowledge base search results:")
    assert tool_message.artifact["type"] == "knowledge_base_search"
    assert len(tool_message.artifact["results"][0]["text_results"]) == 10
    assert len(tool_message.artifact["results"][0]["image_results"]) == 3
    assert len(tool_message.artifact["results"][0]["table_results"]) == 3
    assert len(tool_message.artifact["results"][0]["chart_results"]) == 3
    assert tool_message.artifact["results"][0]["text_results"][0]["uuid"] == "text-0"
    assert '"uuid": "text-10"' not in tool_message.content
    assert '"uuid": "image-3"' not in tool_message.content
    assert request_kwargs[0]["timeout_seconds"] == 25


def test_knowledge_base_search_accepts_custom_type_specific_top_k(monkeypatch):
    async def fake_query_workspace_async(**kwargs):
        return {
            "query": kwargs["query"],
            "text_results": [{"uuid": f"text-{index}"} for index in range(5)],
            "image_results": [{"uuid": f"image-{index}"} for index in range(5)],
            "table_results": [{"uuid": f"table-{index}"} for index in range(5)],
            "chart_results": [{"uuid": f"chart-{index}"} for index in range(5)],
        }

    monkeypatch.setattr(utils, "query_workspace_async", fake_query_workspace_async)
    tool_message = asyncio.run(utils.knowledge_base_search.ainvoke(
        {
            "name": "knowledge_base_search",
            "args": {
                "queries": ["inspection"],
                "text_topk": 1,
                "image_topk": 2,
                "table_topk": 0,
                "chart_topk": 1,
            },
            "id": "call-1",
            "type": "tool_call",
        },
        {
            "configurable": {
                "knowledge_base_url": "http://127.0.0.1:8000",
                "workspace_id": "manual-1",
                "search_api": SearchAPI.NONE.value,
            }
        },
    ))

    result = tool_message.artifact["results"][0]
    assert [item["uuid"] for item in result["text_results"]] == ["text-0"]
    assert [item["uuid"] for item in result["image_results"]] == [
        "image-0",
        "image-1",
    ]
    assert result["table_results"] == []
    assert [item["uuid"] for item in result["chart_results"]] == ["chart-0"]


def test_document_element_window_requests_context_and_resolves_urls(monkeypatch):
    FakeSession.get_requests = []
    FakeSession.timeouts = []
    FakeSession.response = FakeResponse(
        """{
          "center": {
            "uuid": "image/node 1",
            "modal_type": "IMAGE",
            "url": "images/center.jpg"
          },
          "items": [
            {"uuid": "text-1", "modal_type": "TEXT", "url": null},
            {"uuid": "image/node 1", "modal_type": "IMAGE", "url": "/images/center.jpg"},
            {"uuid": "table-1", "modal_type": "TABLE", "url": null, "body": "| a | b |"}
          ],
          "k": 4,
          "total": 10,
          "start_global_element_index": 2,
          "end_global_element_index": 6
        }"""
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    result = asyncio.run(
        utils.get_document_element_window_async(
            element_node_id="image/node 1",
            workspace_id="manual workspace",
            base_url="http://127.0.0.1:8000/",
            k=4,
            timeout_seconds=35,
        )
    )

    assert FakeSession.get_requests == [
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
        "document-elements/image%2Fnode%201/window?k=4"
    ]
    assert result["center"]["url"] == (
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
        "document-elements/image%2Fnode%201/resource"
    )
    assert result["items"][1]["url"] == (
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
        "document-elements/image%2Fnode%201/resource"
    )
    assert result["items"][2]["url"] is None
    assert result["items"][2]["body"] == "| a | b |"
    assert FakeSession.timeouts == [35]


def test_text_node_window_uses_text_endpoint(monkeypatch):
    FakeSession.get_requests = []
    FakeSession.response = FakeResponse(
        """{
          "center": {"uuid": "text-1", "content": "center"},
          "items": [{"uuid": "text-1", "content": "center"}],
          "k": 8,
          "total": 1,
          "start_global_chunk_index": 0,
          "end_global_chunk_index": 0
        }"""
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    result = asyncio.run(
        utils.get_text_node_window_async(
            text_node_id="text-1",
            workspace_id="workspace",
            base_url="http://127.0.0.1:8000",
            k=8,
        )
    )

    assert FakeSession.get_requests == [
        "http://127.0.0.1:8000/api/v1/workspaces/workspace/"
        "text-nodes/text-1/window?k=8"
    ]
    assert result["center"]["content"] == "center"


def test_document_element_resource_returns_image_data_url(monkeypatch):
    FakeSession.get_requests = []
    FakeSession.timeouts = []
    FakeSession.response = FakeResponse(
        b"\x89PNG\r\n\x1a\nimage-bytes",
        headers={"Content-Type": "image/png; charset=binary"},
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    result = asyncio.run(
        utils.get_document_element_resource_data_url_async(
            element_node_id="image/node 1",
            workspace_id="manual workspace",
            base_url="http://127.0.0.1:8000/",
            timeout_seconds=20,
            max_bytes=100,
        )
    )

    assert FakeSession.get_requests == [
        "http://127.0.0.1:8000/api/v1/workspaces/manual%20workspace/"
        "document-elements/image%2Fnode%201/resource"
    ]
    assert FakeSession.timeouts == [20]
    assert result == {
        "source_id": "image/node 1",
        "mime_type": "image/png",
        "data_url": "data:image/png;base64,iVBORw0KGgppbWFnZS1ieXRlcw==",
    }


def test_document_element_resource_rejects_non_image_content(monkeypatch):
    FakeSession.response = FakeResponse(
        "plain text",
        headers={"Content-Type": "text/plain; charset=utf-8"},
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    with pytest.raises(ToolException, match="non-image content type"):
        asyncio.run(
            utils.get_document_element_resource_data_url_async(
                element_node_id="text-1",
                workspace_id="workspace",
                base_url="http://127.0.0.1:8000",
            )
        )


def test_missing_document_element_resource_error_is_skippable():
    error = ToolException(
        'Resource API request failed with HTTP 404: '
        '{"detail":"TableNode 5680a7c1-2817-463c-a209-15f9c3c4895a has no resource path"}'
    )

    assert utils.is_missing_document_element_resource_error(error)
    assert not utils.is_missing_document_element_resource_error(
        ToolException('Resource API request failed with HTTP 404: {"detail":"not found"}')
    )


def test_non_image_document_element_resource_error_is_skippable():
    error = ToolException("Resource API returned non-image content type: text/plain")

    assert utils.is_non_image_document_element_resource_error(error)
    assert not utils.is_non_image_document_element_resource_error(
        ToolException("Resource API request failed with HTTP 404")
    )


def test_window_tools_preserve_results_as_artifacts(monkeypatch):
    async def fake_document_window_async(**kwargs):
        return {
            "center": {"uuid": "image-1", "modal_type": "IMAGE"},
            "items": [{"uuid": "image-1", "modal_type": "IMAGE"}],
        }

    async def fake_text_window_async(**kwargs):
        return {
            "center": {"uuid": "text-1", "content": "center"},
            "items": [{"uuid": "text-1", "content": "center"}],
        }

    monkeypatch.setattr(
        utils,
        "get_document_element_window_async",
        fake_document_window_async,
    )
    monkeypatch.setattr(utils, "get_text_node_window_async", fake_text_window_async)
    config = {
        "configurable": {
            "knowledge_base_url": "http://127.0.0.1:8000",
            "workspace_id": "manual-1",
            "search_api": SearchAPI.NONE.value,
            "knowledge_base_window_timeout_seconds": 30,
        }
    }

    document_message = asyncio.run(utils.knowledge_base_document_window.ainvoke(
        {
            "name": "knowledge_base_document_window",
            "args": {"element_node_id": "image-1"},
            "id": "call-1",
            "type": "tool_call",
        },
        config,
    ))
    text_message = asyncio.run(utils.knowledge_base_text_window.ainvoke(
        {
            "name": "knowledge_base_text_window",
            "args": {"text_node_id": "text-1"},
            "id": "call-2",
            "type": "tool_call",
        },
        config,
    ))

    assert document_message.content.startswith("Knowledge base document window:")
    assert document_message.artifact == {
        "type": "knowledge_base_document_window",
        "result": {
            "center": {"uuid": "image-1", "modal_type": "IMAGE"},
            "items": [{"uuid": "image-1", "modal_type": "IMAGE"}],
        },
    }
    assert text_message.content.startswith("Knowledge base text window:")
    assert text_message.artifact == {
        "type": "knowledge_base_text_window",
        "result": {
            "center": {"uuid": "text-1", "content": "center"},
            "items": [{"uuid": "text-1", "content": "center"}],
        },
    }


def test_window_api_propagates_http_error(monkeypatch):
    FakeSession.get_requests = []
    FakeSession.response = FakeResponse(
        '{"detail":"DocumentElementNode missing not found"}',
        status=400,
    )
    monkeypatch.setattr(utils.aiohttp, "ClientSession", FakeSession)

    with pytest.raises(ToolException, match="HTTP 400"):
        asyncio.run(
            utils.get_document_element_window_async(
                element_node_id="missing",
                workspace_id="workspace",
                base_url="http://127.0.0.1:8000",
            )
        )


def test_get_all_tools_adds_knowledge_base_search(monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_BASE_URL", "http://127.0.0.1:8000")
    monkeypatch.setenv("WORKSPACE_ID", "workspace")

    tools = asyncio.run(
        utils.get_all_tools({"configurable": {"search_api": SearchAPI.NONE.value}})
    )
    tool_names = {
        item.name if hasattr(item, "name") else item.get("name")
        for item in tools
    }

    assert "knowledge_base_search" in tool_names
    assert "knowledge_base_document_window" in tool_names
    assert "knowledge_base_text_window" in tool_names
