import pytest
from langchain_core.messages import AIMessage, ToolMessage
from pydantic import ValidationError

from open_deep_research.research import (
    CitationValidationError,
    ResearchFinding,
    ResearchSource,
    StructuredResearch,
    StructuredResearchDraft,
    build_writer_research_context,
    collect_queries_and_tool_calls,
    collect_trusted_sources,
    coerce_structured_research,
    coerce_structured_research_draft,
    finalize_wiki_citations,
    keep_findings_with_trusted_sources,
    keep_sources_used_by_findings,
    merge_structured_research,
    render_structured_research,
)


def test_structured_research_validates_and_renders_stable_source_ids():
    research = StructuredResearch(
        research_topic="Casting inspection requirements",
        queries_and_tool_calls=["knowledge_base_search: casting inspection"],
        findings=[
            ResearchFinding(
                content="The inspection includes a visual check.",
                source_ids=["text-node-1", "https://example.com/inspection"],
            )
        ],
        sources=[
            ResearchSource(
                source_id="text-node-1",
                source_type="text",
                uuid="text-node-1",
                name="TextNode0",
                group_id="manual-1",
                labels=["TextNode"],
                attributes={"catalog_path": "Inspection"},
                content="Perform a visual check.",
            ),
            ResearchSource(
                source_id="https://example.com/inspection",
                source_type="web",
                title="Inspection Guide",
                url="https://example.com/inspection",
            ),
        ],
    )

    rendered = render_structured_research(research)

    assert "[text-node-1]" in rendered
    assert "[https://example.com/inspection]" in rendered
    assert "[1]" not in rendered
    assert "Inspection Guide: https://example.com/inspection" in rendered


def test_structured_research_rejects_unknown_source_references():
    with pytest.raises(ValidationError, match="Unknown source IDs: missing-source"):
        StructuredResearch(
            research_topic="topic",
            findings=[ResearchFinding(content="claim", source_ids=["missing-source"])],
        )


def test_structured_research_rejects_duplicate_source_ids():
    with pytest.raises(ValidationError, match="Duplicate source IDs: source-1"):
        StructuredResearch(
            research_topic="topic",
            sources=[
                ResearchSource(source_id="source-1", source_type="text"),
                ResearchSource(source_id="source-1", source_type="image"),
            ],
        )


def test_coerce_structured_research_enforces_assigned_topic():
    research = coerce_structured_research(
        {
            "research_topic": "model changed the topic",
            "findings": [],
            "sources": [],
        },
        research_topic="assigned topic",
    )

    assert research.research_topic == "assigned topic"


def test_structured_research_draft_allows_unknown_source_references():
    draft = coerce_structured_research_draft(
        {
            "findings": [{
                "content": "claim",
                "source_ids": ["trusted-source", "model-invented-source"],
            }],
        }
    )

    assert isinstance(draft, StructuredResearchDraft)
    assert draft.findings[0].source_ids == [
        "trusted-source",
        "model-invented-source",
    ]


def test_keep_findings_with_trusted_sources_removes_unverified_references():
    findings = [
        ResearchFinding(
            content="partially supported claim",
            source_ids=["trusted-source", "model-invented-source"],
        ),
        ResearchFinding(
            content="unsupported claim",
            source_ids=["missing-source"],
        ),
    ]
    sources = [ResearchSource(source_id="trusted-source", source_type="text")]

    trusted_findings = keep_findings_with_trusted_sources(findings, sources)

    assert trusted_findings == [
        ResearchFinding(
            content="partially supported claim",
            source_ids=["trusted-source"],
        )
    ]


def test_keep_sources_used_by_findings_removes_unreferenced_sources():
    sources = [
        ResearchSource(source_id="used-source", source_type="text"),
        ResearchSource(source_id="unused-source", source_type="image"),
    ]
    findings = [
        ResearchFinding(content="supported claim", source_ids=["used-source"])
    ]

    used_sources = keep_sources_used_by_findings(sources, findings)

    assert used_sources == [
        ResearchSource(source_id="used-source", source_type="text")
    ]


def test_merge_structured_research_deduplicates_and_enriches_sources():
    first = StructuredResearch(
        research_topic="first",
        queries_and_tool_calls=["query one"],
        findings=[ResearchFinding(content="claim one", source_ids=["node-1"])],
        sources=[ResearchSource(
            source_id="node-1",
            source_type="text",
            uuid="node-1",
            labels=["TextNode"],
            content="short",
        )],
    )
    second = StructuredResearch(
        research_topic="second",
        queries_and_tool_calls=["query one", "query two"],
        findings=[ResearchFinding(content="claim two", source_ids=["node-1"])],
        sources=[ResearchSource(
            source_id="node-1",
            source_type="text",
            uuid="node-1",
            name="TextNode0",
            labels=["DocumentElement"],
            attributes={"page": 2},
            content="a longer source passage",
        )],
    )

    merged = merge_structured_research([first, second], "overall topic")

    assert merged.research_topic == "overall topic"
    assert merged.queries_and_tool_calls == ["query one", "query two"]
    assert [finding.content for finding in merged.findings] == ["claim one", "claim two"]
    assert len(merged.sources) == 1
    assert merged.sources[0].name == "TextNode0"
    assert merged.sources[0].labels == ["TextNode", "DocumentElement"]
    assert merged.sources[0].attributes == {"page": 2}
    assert merged.sources[0].content == "a longer source passage"


def test_writer_context_and_final_citations_use_only_known_sources():
    research = StructuredResearch(
        research_topic="topic",
        findings=[ResearchFinding(
            content="A supported finding",
            source_ids=["node-b", "https://example.com/a"],
        )],
        sources=[
            ResearchSource(
                source_id="node-b",
                source_type="image",
                uuid="node-b",
                caption="Inspection diagram",
                url="http://127.0.0.1:8000/images/diagram.png",
            ),
            ResearchSource(
                source_id="https://example.com/a",
                source_type="web",
                title="Web Guide",
                url="https://example.com/a",
            ),
        ],
    )

    context, citation_sources = build_writer_research_context(research)
    finalized = finalize_wiki_citations(
        "The requirement is documented [[S1]] and illustrated [[S2]]. "
        "[Invented link](https://invented.example).",
        citation_sources,
    )

    assert '"citation_ids": [' in context
    assert '"S2"' in context
    assert "documented [[S1]] and illustrated [[S2]]" in finalized
    assert "[Web Guide](https://example.com/a)" in finalized
    assert "[Inspection diagram](http://127.0.0.1:8000/images/diagram.png)" in finalized
    assert "https://invented.example" not in finalized
    assert finalized.count("## Sources") == 1
    assert "`node-b`" in finalized


def test_finalize_wiki_citations_expands_combined_citation_groups():
    citation_sources = {
        "S18": ResearchSource(
            source_id="text-18",
            source_type="text",
            title="Text Source",
        ),
        "S50": ResearchSource(
            source_id="image-50",
            source_type="image",
            caption="Image Source",
            url="http://127.0.0.1:8000/resource/image-50",
        ),
    }

    finalized = finalize_wiki_citations(
        "Combined evidence [[S18,S50]].",
        citation_sources,
    )

    assert "Combined evidence [[S18,S50]]." in finalized
    assert "- S18: Text Source (`text-18`)" in finalized
    assert (
        "- S50: [Image Source](http://127.0.0.1:8000/resource/image-50) (`image-50`)"
        in finalized
    )


def test_finalize_wiki_citations_removes_duplicate_image_link():
    citation_sources = {
        "S1": ResearchSource(
            source_id="image-1",
            source_type="image",
            caption="H13钢退火态光学显微镜组织",
            url=(
                "http://192.168.150.150:8000/api/v1/workspaces/"
                "die_casting_wiki_v2/document-elements/image-1/resource"
            ),
        ),
    }
    image_url = citation_sources["S1"].url

    finalized = finalize_wiki_citations(
        (
            f"该图像可用于说明退火态组织特征 [[S1]]。\n\n"
            f"![H13钢退火态粒状珠光体金相组织]({image_url}) "
            f"[H13钢退火态光学显微镜组织]({image_url})"
        ),
        citation_sources,
    )

    assert f"![H13钢退火态粒状珠光体金相组织]({image_url})" in finalized
    assert (
        f"![H13钢退火态粒状珠光体金相组织]({image_url}) "
        f"[H13钢退火态光学显微镜组织]({image_url})"
        not in finalized
    )
    assert "- S1:" in finalized


def test_finalize_wiki_citations_renders_readable_text_and_table_sources():
    citation_sources = {
        "S25": ResearchSource(
            source_id="8c9f1f9d-a30c-4425-9952-f02ebfc45d13",
            source_type="text",
            uuid="8c9f1f9d-a30c-4425-9952-f02ebfc45d13",
            content="H13钢属于热作模具钢，常用于压铸模具成型零件。",
            url=(
                "http://127.0.0.1:8000/api/v1/workspaces/wiki/"
                "document-elements/8c9f1f9d-a30c-4425-9952-f02ebfc45d13/resource"
            ),
        ),
        "S26": ResearchSource(
            source_id="8e8ac345-cdd0-4267-ad18-a7691d2b2e3f",
            source_type="table",
            uuid="8e8ac345-cdd0-4267-ad18-a7691d2b2e3f",
            caption="表 5.5-8 H11、H13 钢的室温力学性能",
            body="| 钢号 | 抗拉强度 | 屈服强度 |\n| H13 | 1500 MPa | 1200 MPa |",
        ),
    }

    finalized = finalize_wiki_citations(
        "H13钢可用于压铸模具 [[S25]]，性能数据见表 [[S26]]。",
        citation_sources,
    )

    assert (
        "- S25: [H13钢属于热作模具钢，常用于压铸模具成型零件。]"
        "(http://127.0.0.1:8000/api/v1/workspaces/wiki/"
        "document-elements/8c9f1f9d-a30c-4425-9952-f02ebfc45d13/resource)"
        in finalized
    )
    assert (
        "- S26: 表 5.5-8 H11、H13 钢的室温力学性能 "
        "(`8e8ac345-cdd0-4267-ad18-a7691d2b2e3f`) - "
        "| 钢号 | 抗拉强度 | 屈服强度 | | H13 | 1500 MPa | 1200 MPa |"
        in finalized
    )


@pytest.mark.parametrize(
    ("draft", "message"),
    [
        ("Draft without citations", "contains no citation IDs"),
        ("Draft with [[S99]]", "Unknown citation IDs: S99"),
    ],
)
def test_finalize_wiki_citations_rejects_invalid_citations(draft, message):
    source = ResearchSource(source_id="node-1", source_type="text")

    with pytest.raises(CitationValidationError, match=message):
        finalize_wiki_citations(draft, {"S1": source})


def test_collect_trusted_sources_uses_knowledge_base_artifact_metadata():
    message = ToolMessage(
        content='Text result with uuid "text-1"',
        tool_call_id="call-1",
        name="knowledge_base_search",
        artifact={
            "type": "knowledge_base_search",
            "results": [{
                "query": "inspection",
                "text_results": [{
                    "uuid": "text-1",
                    "name": "TextNode0",
                    "group_id": "manual-1",
                    "labels": ["TextNode"],
                    "attributes": {"page": 2},
                    "content": "Trusted text",
                }],
                "image_results": [],
                "table_results": [],
                "chart_results": [],
            }],
        },
    )
    sources = collect_trusted_sources([message])

    assert sources == [ResearchSource(
        source_id="text-1",
        source_type="text",
        uuid="text-1",
        name="TextNode0",
        group_id="manual-1",
        labels=["TextNode"],
        attributes={"page": 2},
        content="Trusted text",
    )]


def test_collect_trusted_sources_uses_window_artifact_items():
    message = ToolMessage(
        content='Window contains uuid "image-1"',
        tool_call_id="call-1",
        name="knowledge_base_document_window",
        artifact={
            "type": "knowledge_base_document_window",
            "result": {
                "center": {
                    "uuid": "text-1",
                    "modal_type": "TEXT",
                    "labels": ["TextNode"],
                    "content": "Center text",
                },
                "items": [{
                    "uuid": "image-1",
                    "modal_type": "IMAGE",
                    "labels": ["ImageNode"],
                    "url": "http://127.0.0.1:8000/images/figure.jpg",
                    "caption": "Figure caption",
                    "summary": "Figure summary",
                }],
            },
        },
    )

    sources = collect_trusted_sources([message])

    assert sources == [
        ResearchSource(
            source_id="text-1",
            source_type="text",
            uuid="text-1",
            labels=["TextNode"],
            content="Center text",
        ),
        ResearchSource(
            source_id="image-1",
            source_type="image",
            uuid="image-1",
            labels=["ImageNode"],
            url="http://127.0.0.1:8000/images/figure.jpg",
            caption="Figure caption",
            summary="Figure summary",
        ),
    ]


def test_collect_trusted_sources_extracts_web_sources_from_tool_content():
    message = ToolMessage(
        content=(
            "Search results:\n\n"
            "--- SOURCE 1: Real Guide ---\n"
            "URL: https://example.com/real\n\n"
            "SUMMARY:\nTrusted summary\n\n"
            "--------------------------------------------------------------------------------\n"
        ),
        tool_call_id="call-1",
        name="tavily_search",
    )

    sources = collect_trusted_sources([message])

    assert sources == [ResearchSource(
        source_id="https://example.com/real",
        source_type="web",
        title="Real Guide",
        url="https://example.com/real",
        summary="Trusted summary",
    )]


def test_collect_queries_and_tool_calls_uses_model_calls_and_artifacts():
    ai_message = AIMessage(
        content="",
        tool_calls=[{
            "name": "knowledge_base_search",
            "args": {"queries": ["inspection"]},
            "id": "call-1",
        }],
    )
    tool_message = ToolMessage(
        content="Knowledge base search results",
        tool_call_id="call-1",
        name="knowledge_base_search",
        artifact={
            "type": "knowledge_base_search",
            "results": [{
                "query": "inspection",
                "text_results": [],
                "image_results": [],
                "table_results": [],
                "chart_results": [],
            }],
        },
    )

    activity = collect_queries_and_tool_calls([ai_message, tool_message])

    assert activity == [
        'knowledge_base_search: {"queries": ["inspection"]}',
        "knowledge_base_search: inspection",
    ]


def test_researcher_output_keeps_legacy_compressed_research_compatible():
    from open_deep_research.state import ResearcherOutputState

    output = ResearcherOutputState(
        compressed_research="legacy markdown",
        raw_notes=["raw tool output"],
    )

    assert output.compressed_research == "legacy markdown"
    assert output.structured_research is None
