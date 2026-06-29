"""Generate wiki entry metadata and normalize generated wiki pages."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any

from mkdocs.structure.files import File, Files, InclusionLevel

OUTPUT_PATH = "assets/data/wiki-entries.json"
ENTRIES_DIR = "entries"
SEARCH_INDEX_PATH = Path("search") / "search_index.json"
SEARCH_WORKER_PATH = Path("search") / "worker.js"
FENCE_RE = re.compile(r"^\s*(```|~~~)")
TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
TABLE_RE = re.compile(r"(<table>\s*.*?\s*</table>)", re.DOTALL)
CJK_RE = re.compile(r"[\u3400-\u9fff]+")
SEARCH_WORKER_FIELD_MARKER = "      this.field('text');\n      this.ref('location');"
SEARCH_WORKER_FIELD_REPLACEMENT = (
    "      this.field('text');\n"
    "      this.field('tokens');\n"
    "      this.ref('location');"
)
ENTRY_META_FIELDS = (
    ("version", "版本"),
    ("generated_at", "生成时间"),
    ("confidence_score", "置信度分数"),
    ("confidence_level", "置信度等级"),
)
CONFIDENCE_LEVEL_LABELS = {
    "very_high": "很高",
    "high": "高",
    "medium": "中",
    "low": "低",
    "very_low": "很低",
}
CONFIDENCE_BASIS_FIELDS = (
    ("cited_sources", "引用来源"),
    ("source_quality_score", "来源质量"),
    ("freshness_score", "时效性"),
    ("evidence_coverage_score", "证据覆盖"),
)


def _entry_title(src_uri: str) -> str:
    return Path(src_uri).stem


def _entry_sort_key(entry: dict[str, str]) -> tuple[str, str]:
    return (entry["title"].casefold(), entry["source"].casefold())


def _chinese_ngrams(text: str, min_length: int = 2, max_length: int = 3) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()

    for match in CJK_RE.finditer(text):
        segment = match.group(0)
        upper_length = min(max_length, len(segment))
        for length in range(min_length, upper_length + 1):
            for start in range(0, len(segment) - length + 1):
                term = segment[start : start + length]
                if term not in seen:
                    seen.add(term)
                    terms.append(term)

    return terms


def _is_entry_uri(src_uri: str) -> bool:
    return (
        src_uri.startswith(f"{ENTRIES_DIR}/")
        and src_uri.endswith(".md")
        and Path(src_uri).name.lower() != "index.md"
    )


def _split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith(r"\|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    buffer: list[str] = []
    escaped = False

    for char in stripped:
        if escaped:
            buffer.append("\\")
            buffer.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(buffer).strip())
            buffer = []
        else:
            buffer.append(char)

    if escaped:
        buffer.append("\\")
    cells.append("".join(buffer).strip())
    return cells


def _split_separator_row(line: str) -> list[str]:
    stripped = line.strip()
    if re.fullmatch(r"[\s|:+-]+", stripped):
        stripped = stripped.replace("+", "|")
    return _split_table_row(stripped)


def _is_table_separator(line: str) -> bool:
    if "|" not in line:
        return False

    cells = _split_separator_row(line)
    nonempty_cells = [cell.strip() for cell in cells if cell.strip()]
    return bool(nonempty_cells) and all(
        TABLE_SEPARATOR_RE.match(cell) for cell in nonempty_cells
    )


def _normalize_table_cells(cells: list[str], column_count: int) -> list[str]:
    if len(cells) > column_count:
        cells = cells[: column_count - 1] + [r" \| ".join(cells[column_count - 1 :])]
    elif len(cells) < column_count:
        cells = cells + [""] * (column_count - len(cells))
    return cells


def _format_table_row(cells: list[str]) -> str:
    return f"| {' | '.join(cells)} |"


def _clean_markdown_wrapper_lines(lines: list[str]) -> list[str]:
    output: list[str] = []
    pending_scroll_divs = 0

    for line in lines:
        stripped = line.strip()
        lowered = stripped.lower()

        if lowered in {"<article>", "</article>"}:
            continue

        if lowered.startswith("<div") and "overflow-x" in lowered and "auto" in lowered:
            pending_scroll_divs += 1
            continue

        if pending_scroll_divs and lowered == "</div>":
            pending_scroll_divs -= 1
            continue

        output.append(line)

    return output


def _normalize_markdown_tables(markdown: str) -> str:
    lines = _clean_markdown_wrapper_lines(markdown.splitlines())
    output: list[str] = []
    in_fence = False
    index = 0

    while index < len(lines):
        line = lines[index]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append(line)
            index += 1
            continue

        is_table_start = (
            not in_fence
            and index + 1 < len(lines)
            and "|" in line
            and _is_table_separator(lines[index + 1])
        )
        if not is_table_start:
            output.append(line)
            index += 1
            continue

        if output and output[-1].strip():
            output.append("")

        header_row = _split_table_row(line)
        separator_row = _split_separator_row(lines[index + 1])
        column_count = max(len(header_row), len(separator_row))
        header_cells = _normalize_table_cells(header_row, column_count)
        output.append(_format_table_row(header_cells))

        index += 1
        separator_cells = _normalize_table_cells(
            _split_separator_row(lines[index]), column_count
        )
        separator_cells = [
            cell if TABLE_SEPARATOR_RE.match(cell.strip()) else "---"
            for cell in separator_cells
        ]
        output.append(_format_table_row(separator_cells))

        index += 1
        while index < len(lines) and lines[index].strip() and "|" in lines[index]:
            row_cells = _normalize_table_cells(
                _split_table_row(lines[index]), column_count
            )
            output.append(_format_table_row(row_cells))
            index += 1

        if index < len(lines) and lines[index].strip():
            output.append("")

    normalized = "\n".join(output)
    if markdown.endswith("\n"):
        normalized += "\n"
    return normalized


def _is_entry_page(page: Any) -> bool:
    file = getattr(page, "file", None)
    src_uri = getattr(file, "src_uri", "")
    return _is_entry_uri(src_uri)


def _format_generated_at(value: Any) -> str:
    if not isinstance(value, str):
        return str(value)

    raw_value = value.strip()
    if not raw_value:
        return ""

    try:
        parsed = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError:
        return raw_value

    suffix = ""
    if parsed.tzinfo is not None and parsed.utcoffset() == timezone.utc.utcoffset(None):
        suffix = " UTC"
    return parsed.strftime("%Y-%m-%d %H:%M") + suffix


def _format_meta_value(key: str, value: Any) -> str:
    if value is None:
        return ""
    if key == "generated_at":
        return _format_generated_at(value)
    if key == "confidence_level" and isinstance(value, str):
        return CONFIDENCE_LEVEL_LABELS.get(value, value)
    if isinstance(value, float):
        return f"{value:.2f}".rstrip("0").rstrip(".")
    return str(value)


def _format_meta_item(label: str, value: str) -> str:
    return (
        '<div class="wiki-entry-info-row">'
        f'<dt class="wiki-entry-info-label">{escape(label)}</dt>'
        f'<dd class="wiki-entry-info-value">{escape(value)}</dd>'
        "</div>"
    )


def _format_meta_section(title: str, items: list[str]) -> str:
    if not items:
        return ""
    return (
        '<section class="wiki-entry-info-section">'
        f'<div class="wiki-entry-info-section-title">{escape(title)}</div>'
        '<dl class="wiki-entry-info-list">'
        + "".join(items)
        + "</dl>"
        "</section>"
    )


def _format_entry_info_panel(page: Any) -> str:
    meta = getattr(page, "meta", None)
    if not isinstance(meta, dict) or not meta:
        return ""

    items: list[str] = []
    for key, label in ENTRY_META_FIELDS:
        value = _format_meta_value(key, meta.get(key))
        if value:
            items.append(_format_meta_item(label, value))

    confidence_basis = meta.get("confidence_basis")
    basis_items: list[str] = []
    if isinstance(confidence_basis, dict):
        for key, label in CONFIDENCE_BASIS_FIELDS:
            value = _format_meta_value(key, confidence_basis.get(key))
            if value:
                basis_items.append(_format_meta_item(label, value))

    if not items and not basis_items:
        return ""

    version = _format_meta_value("version", meta.get("version"))
    generated_at = _format_meta_value("generated_at", meta.get("generated_at"))
    confidence_score = _format_meta_value(
        "confidence_score", meta.get("confidence_score")
    )
    confidence_level = _format_meta_value(
        "confidence_level", meta.get("confidence_level")
    )

    summary_parts = [part for part in (version, generated_at) if part]
    summary_meta = ""
    if summary_parts:
        summary_meta = (
            '<span class="wiki-entry-info-summary-meta">'
            + escape(" · ".join(summary_parts))
            + "</span>"
        )

    badges: list[str] = []
    if confidence_level:
        badges.append(
            '<span class="wiki-entry-info-badge wiki-entry-info-badge-level">'
            f"置信度 {escape(confidence_level)}"
            "</span>"
        )
    if confidence_score:
        badges.append(
            '<span class="wiki-entry-info-badge wiki-entry-info-badge-score">'
            f"{escape(confidence_score)}"
            "</span>"
        )
    badges_html = ""
    if badges:
        badges_html = '<span class="wiki-entry-info-badges">' + "".join(badges) + "</span>"

    return (
        '<details class="wiki-entry-info-panel">'
        '<summary class="wiki-entry-info-summary">'
        '<span class="wiki-entry-info-summary-main">'
        '<span class="wiki-entry-info-summary-title">条目信息</span>'
        + summary_meta
        + "</span>"
        + badges_html
        + "</summary>"
        + '<div class="wiki-entry-info-body">'
        + _format_meta_section("基本信息", items)
        + _format_meta_section("置信度依据", basis_items)
        + "</div>"
        + "</details>"
    )


def _augment_search_index(site_dir: Path) -> None:
    search_index_path = site_dir / SEARCH_INDEX_PATH
    if not search_index_path.exists():
        return

    index = json.loads(search_index_path.read_text(encoding="utf-8"))
    docs = index.get("docs")
    if not isinstance(docs, list):
        return

    changed = False
    for doc in docs:
        if not isinstance(doc, dict):
            continue

        title = doc.get("title")
        if not isinstance(title, str):
            continue

        tokens = " ".join(_chinese_ngrams(title))
        if tokens and doc.get("tokens") != tokens:
            doc["tokens"] = tokens
            changed = True

    if changed:
        search_index_path.write_text(
            json.dumps(index, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )


def _patch_search_worker(site_dir: Path) -> None:
    worker_path = site_dir / SEARCH_WORKER_PATH
    if not worker_path.exists():
        return

    worker_js = worker_path.read_text(encoding="utf-8")
    if "this.field('tokens');" in worker_js:
        return
    if SEARCH_WORKER_FIELD_MARKER not in worker_js:
        return

    worker_js = worker_js.replace(
        SEARCH_WORKER_FIELD_MARKER,
        SEARCH_WORKER_FIELD_REPLACEMENT,
        1,
    )
    worker_path.write_text(worker_js, encoding="utf-8")


def on_files(files: Files, config: dict[str, Any]) -> Files:
    entries: list[dict[str, str]] = []

    for file in files:
        src_uri = file.src_uri
        if not (_is_entry_uri(src_uri) and file.inclusion.is_included()):
            continue

        title = _entry_title(src_uri)
        entries.append(
            {
                "title": title,
                "location": f"{src_uri[:-3]}/",
                "source": src_uri,
            }
        )

    entries.sort(key=_entry_sort_key)
    payload = json.dumps(
        {"entries": entries},
        ensure_ascii=False,
        separators=(",", ":"),
    )
    files.append(
        File.generated(
            config,
            OUTPUT_PATH,
            content=payload,
            inclusion=InclusionLevel.INCLUDED,
        )
    )
    return files


def on_page_markdown(
    markdown: str,
    page: Any,
    config: dict[str, Any],
    files: Files,
) -> str:
    if not _is_entry_page(page):
        return markdown
    return _normalize_markdown_tables(markdown)


def on_page_content(
    html: str,
    page: Any,
    config: dict[str, Any],
    files: Files,
) -> str:
    if not _is_entry_page(page):
        return html
    html = TABLE_RE.sub(r'<div class="wiki-table-wrapper">\1</div>', html)
    entry_info_panel = _format_entry_info_panel(page)
    if entry_info_panel:
        return entry_info_panel + html
    return html


def on_post_build(config: dict[str, Any]) -> None:
    site_dir = Path(config["site_dir"])
    _augment_search_index(site_dir)
    _patch_search_worker(site_dir)
