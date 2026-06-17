"""Structured research findings and deterministic compatibility rendering."""

import json
import re
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

SourceType = Literal["web", "text", "image", "table", "chart", "other"]


class CitationValidationError(ValueError):
    """Raised when wiki output does not use the supplied citation aliases."""


class ResearchSource(BaseModel):
    """A source collected during research and identified by a stable ID."""

    source_id: str = Field(
        min_length=1,
        description=(
            "Stable source identifier. Use a knowledge-base node UUID when available, "
            "otherwise use the canonical source URL."
        )
    )
    source_type: SourceType
    title: str | None = None
    url: str | None = None
    uuid: str | None = None
    name: str | None = None
    group_id: str | None = None
    labels: list[str] = Field(default_factory=list)
    attributes: dict[str, Any] = Field(default_factory=dict)
    content: str | None = None
    enhanced_str: str | None = None
    caption: str | None = None
    summary: str | None = None
    description: str | None = None
    body: str | None = None
    score: float | None = None


class ResearchFinding(BaseModel):
    """A research claim linked to the sources that support it."""

    content: str = Field(min_length=1)
    source_ids: list[str] = Field(min_length=1)


class StructuredResearch(BaseModel):
    """One researcher's findings with explicit, verifiable source links."""

    research_topic: str = Field(min_length=1)
    queries_and_tool_calls: list[str] = Field(default_factory=list)
    findings: list[ResearchFinding] = Field(default_factory=list)
    sources: list[ResearchSource] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_source_references(self) -> "StructuredResearch":
        """Reject duplicate source IDs and findings that cite unknown sources."""
        source_ids = [source.source_id for source in self.sources]
        duplicate_ids = sorted({item for item in source_ids if source_ids.count(item) > 1})
        if duplicate_ids:
            raise ValueError(f"Duplicate source IDs: {', '.join(duplicate_ids)}")

        known_source_ids = set(source_ids)
        unknown_source_ids = sorted({
            source_id
            for finding in self.findings
            for source_id in finding.source_ids
            if source_id not in known_source_ids
        })
        if unknown_source_ids:
            raise ValueError(f"Unknown source IDs: {', '.join(unknown_source_ids)}")
        return self


class StructuredResearchDraft(BaseModel):
    """Model-produced finding draft before source IDs are verified."""

    findings: list[ResearchFinding] = Field(default_factory=list)


def render_structured_research(research: StructuredResearch) -> str:
    """Render structured research as deterministic Markdown for legacy consumers."""
    sections = [f"# Research Topic\n{research.research_topic}"]

    if research.queries_and_tool_calls:
        sections.append(
            "## Queries and Tool Calls Made\n"
            + "\n".join(f"- {item}" for item in research.queries_and_tool_calls)
        )

    if research.findings:
        rendered_findings = []
        for finding in research.findings:
            citations = " ".join(f"[{source_id}]" for source_id in finding.source_ids)
            rendered_findings.append(
                f"- {finding.content}{f' {citations}' if citations else ''}"
            )
        sections.append("## Findings\n" + "\n".join(rendered_findings))

    if research.sources:
        rendered_sources = []
        for source in research.sources:
            label = source.title or source.name or source.caption or source.source_id
            location = f": {source.url}" if source.url else ""
            rendered_sources.append(f"- [{source.source_id}] {label}{location}")
        sections.append("## Sources\n" + "\n".join(rendered_sources))

    return "\n\n".join(sections)


def coerce_structured_research(
    value: StructuredResearch | StructuredResearchDraft | dict[str, Any],
    research_topic: str,
) -> StructuredResearch:
    """Validate model output and enforce the supervisor-assigned research topic."""
    if isinstance(value, StructuredResearchDraft):
        value = value.model_dump()
    research = (
        value
        if isinstance(value, StructuredResearch)
        else StructuredResearch.model_validate(value)
    )
    if research.research_topic != research_topic:
        research = research.model_copy(update={"research_topic": research_topic})
    return research


def coerce_structured_research_draft(
    value: StructuredResearch | StructuredResearchDraft | dict[str, Any],
) -> StructuredResearchDraft:
    """Validate model output as a finding-only draft."""
    if isinstance(value, StructuredResearch):
        value = {"findings": value.findings}
    research = (
        value
        if isinstance(value, StructuredResearchDraft)
        else StructuredResearchDraft.model_validate(value)
    )
    return research


def keep_findings_with_trusted_sources(
    findings: list[ResearchFinding],
    sources: list[ResearchSource],
) -> list[ResearchFinding]:
    """Drop unverifiable source references before final strict validation."""
    trusted_source_ids = {source.source_id for source in sources}
    trusted_findings = []

    for finding in findings:
        source_ids = list(dict.fromkeys(
            source_id
            for source_id in finding.source_ids
            if source_id in trusted_source_ids
        ))
        if not source_ids:
            continue
        trusted_findings.append(finding.model_copy(update={"source_ids": source_ids}))

    return trusted_findings


def keep_sources_used_by_findings(
    sources: list[ResearchSource],
    findings: list[ResearchFinding],
) -> list[ResearchSource]:
    """Keep only sources referenced by verified findings, preserving source order."""
    used_source_ids = {
        source_id
        for finding in findings
        for source_id in finding.source_ids
    }
    return [source for source in sources if source.source_id in used_source_ids]


def collect_trusted_sources(
    evidence_messages: list[Any],
) -> list[ResearchSource]:
    """Build a source registry from tool artifacts and verbatim tool identities."""
    trusted_sources: dict[str, ResearchSource] = {}
    result_types = {
        "text_results": "text",
        "image_results": "image",
        "table_results": "table",
        "chart_results": "chart",
    }

    def source_type_from_element(element: dict[str, Any]) -> SourceType:
        modal_type = str(element.get("modal_type") or "").upper()
        if modal_type == "TEXT":
            return "text"
        if modal_type == "IMAGE":
            return "image"
        if modal_type == "TABLE":
            return "table"
        if modal_type == "CHART":
            return "chart"

        labels = {
            str(label)
            for label in element.get("labels", [])
            if isinstance(label, str)
        }
        if "TextNode" in labels:
            return "text"
        if "ImageNode" in labels:
            return "image"
        if "TableNode" in labels:
            return "table"
        if "ChartNode" in labels:
            return "chart"
        return "other"

    def trust_element(element: dict[str, Any], source_type: SourceType | None = None) -> None:
        if not isinstance(element, dict) or not element.get("uuid"):
            return
        source_data = {
            field: element[field]
            for field in ResearchSource.model_fields
            if field in element
        }
        source_data.update({
            "source_id": element["uuid"],
            "source_type": source_type or source_type_from_element(element),
        })
        trusted_sources[element["uuid"]] = ResearchSource.model_validate(source_data)

    def trust_web_sources_from_content(content: Any) -> None:
        if not isinstance(content, str):
            return
        source_matches = re.finditer(
            r"--- SOURCE \d+: (?P<title>.*?) ---\s+"
            r"URL: (?P<url>\S+)\s+"
            r"SUMMARY:\s*(?P<summary>.*?)(?=\n\n-+\n|\Z)",
            content,
            flags=re.DOTALL,
        )
        matched_urls = set()
        for match in source_matches:
            url = match.group("url").strip()
            matched_urls.add(url)
            trusted_sources[url] = ResearchSource(
                source_id=url,
                source_type="web",
                title=match.group("title").strip(),
                url=url,
                summary=match.group("summary").strip(),
            )

        for url in re.findall(r"URL:\s*(https?://\S+)", content):
            normalized_url = url.strip()
            if normalized_url in matched_urls or normalized_url in trusted_sources:
                continue
            trusted_sources[normalized_url] = ResearchSource(
                source_id=normalized_url,
                source_type="web",
                url=normalized_url,
            )

    for message in evidence_messages:
        artifact = getattr(message, "artifact", None)
        if not isinstance(artifact, dict):
            trust_web_sources_from_content(getattr(message, "content", None))
            continue

        if artifact.get("type") == "knowledge_base_search":
            for query_result in artifact.get("results", []):
                if not isinstance(query_result, dict):
                    continue
                for result_key, source_type in result_types.items():
                    for item in query_result.get(result_key, []):
                        trust_element(item, source_type)
            trust_web_sources_from_content(getattr(message, "content", None))
            continue

        if artifact.get("type") in {
            "knowledge_base_document_window",
            "knowledge_base_text_window",
        }:
            window_result = artifact.get("result", {})
            if not isinstance(window_result, dict):
                continue
            center = window_result.get("center")
            if isinstance(center, dict):
                trust_element(center)
            for item in window_result.get("items", []):
                if isinstance(item, dict):
                    trust_element(item)
        trust_web_sources_from_content(getattr(message, "content", None))

    return list(trusted_sources.values())


def collect_queries_and_tool_calls(evidence_messages: list[Any]) -> list[str]:
    """Collect search and retrieval activity from model/tool messages."""
    activity = []

    for message in evidence_messages:
        for tool_call in getattr(message, "tool_calls", []) or []:
            name = tool_call.get("name", "tool")
            args = tool_call.get("args", {})
            args_text = json.dumps(args, ensure_ascii=False, sort_keys=True)
            if len(args_text) > 500:
                args_text = args_text[:497] + "..."
            activity.append(f"{name}: {args_text}")

        artifact = getattr(message, "artifact", None)
        if not isinstance(artifact, dict):
            continue
        if artifact.get("type") == "knowledge_base_search":
            for query_result in artifact.get("results", []):
                if isinstance(query_result, dict) and query_result.get("query"):
                    activity.append(f"knowledge_base_search: {query_result['query']}")
        elif artifact.get("type") in {
            "knowledge_base_document_window",
            "knowledge_base_text_window",
        }:
            result = artifact.get("result", {})
            center = result.get("center") if isinstance(result, dict) else None
            center_id = center.get("uuid") if isinstance(center, dict) else None
            if center_id:
                activity.append(f"{artifact['type']}: {center_id}")

    return list(dict.fromkeys(activity))


def merge_structured_research(
    research_units: list[StructuredResearch],
    research_topic: str,
) -> StructuredResearch:
    """Merge researcher outputs while deduplicating sources by stable source ID."""
    queries_and_tool_calls: list[str] = []
    findings: list[ResearchFinding] = []
    sources_by_id: dict[str, ResearchSource] = {}

    for research in research_units:
        queries_and_tool_calls.extend(research.queries_and_tool_calls)
        findings.extend(research.findings)
        for source in research.sources:
            existing = sources_by_id.get(source.source_id)
            if existing is None:
                sources_by_id[source.source_id] = source
                continue

            existing_data = existing.model_dump()
            incoming_data = source.model_dump()
            for field, incoming_value in incoming_data.items():
                if field == "labels":
                    existing_data[field] = list(dict.fromkeys(
                        existing_data[field] + incoming_value
                    ))
                elif field == "attributes":
                    existing_data[field] = {**incoming_value, **existing_data[field]}
                elif field in {"content", "enhanced_str", "summary", "body"}:
                    existing_value = existing_data[field]
                    if incoming_value and (
                        not existing_value or len(incoming_value) > len(existing_value)
                    ):
                        existing_data[field] = incoming_value
                elif existing_data[field] in (None, "") and incoming_value not in (None, ""):
                    existing_data[field] = incoming_value
            sources_by_id[source.source_id] = ResearchSource.model_validate(existing_data)

    return StructuredResearch(
        research_topic=research_topic,
        queries_and_tool_calls=list(dict.fromkeys(queries_and_tool_calls)),
        findings=findings,
        sources=list(sources_by_id.values()),
    )


def build_writer_research_context(
    research: StructuredResearch,
) -> tuple[str, dict[str, ResearchSource]]:
    """Build a curated writer payload with short deterministic citation aliases."""
    sorted_sources = sorted(research.sources, key=lambda source: source.source_id)
    citation_sources = {
        f"S{index}": source
        for index, source in enumerate(sorted_sources, start=1)
    }
    aliases_by_source_id = {
        source.source_id: alias for alias, source in citation_sources.items()
    }

    payload = {
        "findings": [
            {
                "content": finding.content,
                "citation_ids": [
                    aliases_by_source_id[source_id]
                    for source_id in finding.source_ids
                ],
            }
            for finding in research.findings
        ],
        "sources": [
            {
                "citation_id": alias,
                **source.model_dump(exclude_none=True),
            }
            for alias, source in citation_sources.items()
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2), citation_sources


def _compact_source_text(value: Any, max_length: int = 120) -> str:
    """Normalize source text for labels and source-list evidence snippets."""
    if value in (None, ""):
        return ""
    text = re.sub(r"\s+", " ", str(value)).strip()
    if len(text) <= max_length:
        return text
    return text[: max_length - 3].rstrip() + "..."


def _source_kind_label(source: ResearchSource) -> str:
    labels = {
        "web": "Web",
        "text": "TextNode",
        "image": "ImageNode",
        "table": "TableNode",
        "chart": "ChartNode",
        "other": "Source",
    }
    return labels.get(source.source_type, "Source")


def _source_label(source: ResearchSource) -> str:
    """Choose a readable label instead of falling back directly to UUIDs."""
    direct_label = (
        source.title
        or source.caption
        or source.name
        or source.attributes.get("catalog_path")
    )
    label = _compact_source_text(direct_label)
    if label:
        return label

    evidence_label = _compact_source_text(
        source.summary
        or source.description
        or source.content
        or source.body
        or source.enhanced_str,
        max_length=80,
    )
    if evidence_label:
        return evidence_label

    return f"{_source_kind_label(source)} {source.uuid or source.source_id}"


def _source_evidence_excerpt(source: ResearchSource) -> str:
    """Return a short source evidence excerpt for non-clickable sources."""
    return _compact_source_text(
        source.content
        or source.body
        or source.summary
        or source.description
        or source.enhanced_str,
        max_length=180,
    )


def finalize_wiki_citations(
    wiki_content: str,
    citation_sources: dict[str, ResearchSource],
) -> str:
    """Validate inline citation aliases and append a program-generated source list."""
    referenced_aliases: list[str] = []

    def parse_citation_aliases(raw_aliases: str) -> list[str]:
        aliases = [
            alias
            for alias in re.split(r"[,，、;\s]+", raw_aliases.strip())
            if alias
        ]
        invalid_aliases = [
            alias for alias in aliases if not re.fullmatch(r"S\d+", alias)
        ]
        if invalid_aliases:
            raise CitationValidationError(
                f"Invalid citation IDs: {', '.join(invalid_aliases)}"
            )
        return aliases

    citation_groups = list(re.finditer(r"\[\[([^\]]+)\]\]", wiki_content))
    citation_aliases = [
        alias
        for group in citation_groups
        for alias in parse_citation_aliases(group.group(1))
    ]
    unknown_aliases = sorted({
        alias for alias in citation_aliases if alias not in citation_sources
    })
    if unknown_aliases:
        raise CitationValidationError(
            f"Unknown citation IDs: {', '.join(unknown_aliases)}"
        )
    if not citation_aliases:
        raise CitationValidationError("The wiki draft contains no citation IDs.")

    for alias in citation_aliases:
        if alias not in referenced_aliases:
            referenced_aliases.append(alias)

    finalized = wiki_content

    finalized = re.sub(
        r"(?P<image>!\[[^\]]*\]\((?P<url>[^)\s]+)\))\s+\[[^\]]+\]\((?P=url)\)",
        lambda match: match.group("image"),
        finalized,
    )

    allowed_urls = {
        source.url for source in citation_sources.values() if source.url
    }

    def sanitize_link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        return match.group(0) if url in allowed_urls else label

    finalized = re.sub(
        r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)",
        sanitize_link,
        finalized,
    ).rstrip()

    source_lines = []
    for alias in referenced_aliases:
        source = citation_sources[alias]
        label = _source_label(source)
        source_identity = source.uuid or source.source_id
        if source.url:
            source_lines.append(
                f"- {alias}: [{label}]({source.url}) (`{source_identity}`)"
            )
        else:
            evidence_excerpt = _source_evidence_excerpt(source)
            detail = f" - {evidence_excerpt}" if evidence_excerpt else ""
            source_lines.append(
                f"- {alias}: {label} (`{source_identity}`){detail}"
            )

    return finalized + "\n\n## Sources\n" + "\n".join(source_lines)
