from pathlib import Path

from scripts.wiki_stats import (
    analyze_directory,
    count_unique_citations,
    parse_simple_yaml,
    split_front_matter,
    split_sources_section,
)


def test_parse_simple_yaml_reads_nested_score_metadata():
    metadata = parse_simple_yaml(
        'version: "v1"\n'
        "confidence_score: 0.82\n"
        "confidence_basis:\n"
        "  cited_sources: 6\n"
        "  source_quality_score: 0.8\n"
        'confidence_level: "high"\n'
    )

    assert metadata == {
        "version": "v1",
        "confidence_score": 0.82,
        "confidence_basis": {
            "cited_sources": 6,
            "source_quality_score": 0.8,
        },
        "confidence_level": "high",
    }


def test_split_front_matter_returns_body_without_metadata():
    metadata, body = split_front_matter(
        "---\n"
        "confidence_score: 0.5\n"
        "---\n\n"
        "## 概述\n\n正文"
    )

    assert metadata["confidence_score"] == 0.5
    assert body == "\n## 概述\n\n正文"


def test_split_sources_section_removes_trailing_sources():
    content, sources = split_sources_section(
        "## 概述\n"
        "正文\n\n"
        "## Sources\n"
        "- S1: very long source"
    )

    assert content == "## 概述\n正文"
    assert sources == "## Sources\n- S1: very long source"


def test_count_unique_citations_expands_groups_and_deduplicates():
    assert count_unique_citations("a [[S1,S2]] b [[S2，S3]] c [[bad]]") == 3


def test_analyze_directory_summarizes_entries_and_scores(tmp_path: Path):
    (tmp_path / "index.md").write_text("# Index\n", encoding="utf-8")
    (tmp_path / "A.md").write_text(
        "---\n"
        "confidence_score: 0.8\n"
        "confidence_basis:\n"
        "  source_quality_score: 0.7\n"
        "---\n\n"
        "## 概述\n"
        "abcd [[S1,S2]]\n\n"
        "### 细节\n"
        "ef [[S1]]\n\n"
        "## Sources\n"
        "- S1: excluded source text",
        encoding="utf-8",
    )
    (tmp_path / "B.md").write_text(
        "---\n"
        "confidence_score: 0.6\n"
        "confidence_basis:\n"
        "  source_quality_score: 0.5\n"
        "---\n\n"
        "## 介绍\n"
        "xy [[S3]]",
        encoding="utf-8",
    )

    summary = analyze_directory(tmp_path)
    summary_with_sources = analyze_directory(tmp_path, include_sources=True)

    assert summary["total_markdown_files"] == 3
    assert len(summary["skipped_files"]) == 1
    assert summary["total_entries"] == 2
    assert summary["total_sections"] == 3
    assert summary["average_sections"] == 1.5
    assert summary["total_citations"] == 3
    assert summary["average_citations"] == 1.5
    assert summary["include_sources"] is False
    assert summary["excluded_source_characters"] > 0
    assert summary_with_sources["include_sources"] is True
    assert summary_with_sources["total_sections"] == 4
    assert summary_with_sources["total_characters"] > summary["total_characters"]
    assert summary["scores"]["confidence_score"] == {
        "count": 2,
        "average": 0.7,
        "min": 0.6,
        "max": 0.8,
    }
    assert summary["scores"]["confidence_basis.source_quality_score"]["average"] == 0.6
