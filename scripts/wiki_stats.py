"""Summarize generated wiki markdown entries."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Any, Iterable


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUMERIC_RE = re.compile(r"^-?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$")
CITATION_RE = re.compile(r"\[\[([^\]]+)\]\]")
SOURCE_SECTION_TITLES = {
    "source",
    "sources",
    "reference",
    "references",
    "参考",
    "参考文献",
    "参考资料",
    "来源",
    "资料来源",
}


@dataclass
class EntryStats:
    """Statistics for a single markdown entry."""

    path: Path
    characters: int
    source_characters: int
    sections: int
    section_characters: int
    citations: int
    scores: dict[str, float] = field(default_factory=dict)


def split_front_matter(markdown: str) -> tuple[dict[str, Any], str]:
    """Return parsed YAML-like front matter and markdown body."""
    normalized = markdown.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized

    end = normalized.find("\n---\n", 4)
    if end == -1:
        return {}, normalized

    front_matter = normalized[4:end]
    body = normalized[end + len("\n---\n") :]
    return parse_simple_yaml(front_matter), body


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the simple nested mapping emitted by persistence.py."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if raw_value:
            parent[key] = parse_yaml_scalar(raw_value)
        else:
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))

    return root


def parse_yaml_scalar(value: str) -> Any:
    """Parse scalar values used in generated markdown metadata."""
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1].replace(r"\"", '"').replace(r"\\", "\\")

    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    if NUMERIC_RE.fullmatch(value):
        parsed = float(value)
        return int(parsed) if parsed.is_integer() and "." not in value.lower() else parsed
    return value


def iter_markdown_files(directory: Path, *, recursive: bool) -> Iterable[Path]:
    """Yield markdown files in stable path order."""
    pattern = "**/*.md" if recursive else "*.md"
    yield from sorted(path for path in directory.glob(pattern) if path.is_file())


def is_source_heading(line: str) -> bool:
    """Return whether a markdown heading starts a sources section."""
    match = HEADING_RE.match(line.rstrip("\n"))
    if not match:
        return False
    title = match.group(2).strip().strip("#").strip().lower()
    return title in SOURCE_SECTION_TITLES


def split_sources_section(body: str) -> tuple[str, str]:
    """Split body into content and trailing sources section."""
    lines = body.splitlines(keepends=True)
    in_fence = False
    offset = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        elif not in_fence and is_source_heading(line):
            return body[:offset].rstrip(), body[offset:].strip()
        offset += len(line)

    return body, ""


def count_section_characters(body: str) -> tuple[int, int]:
    """Count markdown heading sections and their aggregate character length."""
    lines = body.splitlines(keepends=True)
    in_fence = False
    current_start: int | None = None
    offset = 0
    sections: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        elif not in_fence and HEADING_RE.match(line.rstrip("\n")):
            if current_start is not None:
                sections.append(body[current_start:offset].strip())
            current_start = offset
        offset += len(line)

    if current_start is not None:
        sections.append(body[current_start:].strip())

    return len(sections), sum(len(section) for section in sections)


def count_unique_citations(body: str) -> int:
    """Count unique citation aliases such as [[S1]] and [[S1,S2]]."""
    aliases: list[str] = []
    for match in CITATION_RE.finditer(body):
        aliases.extend(
            alias
            for alias in re.split(r"[,，、;\s]+", match.group(1).strip())
            if re.fullmatch(r"S\d+", alias)
        )
    return len(set(aliases))


def iter_score_values(metadata: dict[str, Any], prefix: str = "") -> Iterable[tuple[str, float]]:
    """Yield numeric metadata values whose key name contains score."""
    for key, value in metadata.items():
        dotted_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            yield from iter_score_values(value, dotted_key)
        elif "score" in key.lower() and isinstance(value, int | float) and not isinstance(value, bool):
            yield dotted_key, float(value)


def analyze_entry(
    path: Path,
    *,
    encoding: str = "utf-8",
    include_sources: bool = False,
) -> EntryStats:
    """Analyze one markdown file."""
    content = path.read_text(encoding=encoding)
    metadata, body = split_front_matter(content)
    body = body.strip()
    content_body, sources_body = split_sources_section(body)
    counted_body = body if include_sources else content_body
    section_count, section_char_count = count_section_characters(counted_body)
    return EntryStats(
        path=path,
        characters=len(counted_body),
        source_characters=len(sources_body),
        sections=section_count,
        section_characters=section_char_count,
        citations=count_unique_citations(counted_body),
        scores=dict(iter_score_values(metadata)),
    )


def summarize_scores(entries: list[EntryStats]) -> dict[str, dict[str, float | int]]:
    """Aggregate per-key score statistics."""
    values_by_key: dict[str, list[float]] = {}
    for entry in entries:
        for key, value in entry.scores.items():
            values_by_key.setdefault(key, []).append(value)

    return {
        key: {
            "count": len(values),
            "average": round(mean(values), 4),
            "min": round(min(values), 4),
            "max": round(max(values), 4),
        }
        for key, values in sorted(values_by_key.items())
    }


def analyze_directory(
    directory: Path,
    *,
    recursive: bool = True,
    include_index: bool = False,
    include_sources: bool = False,
    encoding: str = "utf-8",
) -> dict[str, Any]:
    """Analyze markdown entries under a directory."""
    directory = directory.expanduser().resolve()
    if not directory.exists() or not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not an existing directory")

    files = list(iter_markdown_files(directory, recursive=recursive))
    skipped = [
        path
        for path in files
        if not include_index and path.name.lower() == "index.md"
    ]
    entry_files = [path for path in files if path not in skipped]
    entries = [
        analyze_entry(path, encoding=encoding, include_sources=include_sources)
        for path in entry_files
    ]

    total_entries = len(entries)
    total_characters = sum(entry.characters for entry in entries)
    total_source_characters = sum(entry.source_characters for entry in entries)
    total_sections = sum(entry.sections for entry in entries)
    total_section_characters = sum(entry.section_characters for entry in entries)
    total_citations = sum(entry.citations for entry in entries)

    return {
        "directory": str(directory),
        "total_markdown_files": len(files),
        "skipped_files": [str(path) for path in skipped],
        "total_entries": total_entries,
        "include_sources": include_sources,
        "total_characters": total_characters,
        "excluded_source_characters": 0 if include_sources else total_source_characters,
        "average_characters": round(total_characters / total_entries, 2) if total_entries else 0.0,
        "total_sections": total_sections,
        "average_sections": round(total_sections / total_entries, 2) if total_entries else 0.0,
        "total_citations": total_citations,
        "average_citations": round(total_citations / total_entries, 2) if total_entries else 0.0,
        "average_section_characters": (
            round(total_section_characters / total_sections, 2)
            if total_sections
            else 0.0
        ),
        "scores": summarize_scores(entries),
        "entries": [
            {
                "path": str(entry.path),
                "characters": entry.characters,
                "source_characters": entry.source_characters,
                "sections": entry.sections,
                "citations": entry.citations,
                "average_section_characters": (
                    round(entry.section_characters / entry.sections, 2)
                    if entry.sections
                    else 0.0
                ),
                "scores": entry.scores,
            }
            for entry in entries
        ],
    }


def format_text(summary: dict[str, Any], *, include_details: bool = False) -> str:
    """Format summary statistics as plain text."""
    lines = [
        "Wiki markdown statistics",
        f"Directory: {summary['directory']}",
        f"Markdown files scanned: {summary['total_markdown_files']}",
        f"Skipped files: {len(summary['skipped_files'])}",
        f"Total entries: {summary['total_entries']}",
        f"Sources included: {summary['include_sources']}",
        f"Total characters: {summary['total_characters']}",
        f"Excluded source characters: {summary['excluded_source_characters']}",
        f"Average characters per entry: {summary['average_characters']}",
        f"Total sections: {summary['total_sections']}",
        f"Average sections per entry: {summary['average_sections']}",
        f"Total citations: {summary['total_citations']}",
        f"Average citations per entry: {summary['average_citations']}",
        f"Average characters per section: {summary['average_section_characters']}",
        "",
        "Metadata score statistics:",
    ]

    if summary["scores"]:
        for key, stats in summary["scores"].items():
            lines.append(
                f"- {key}: count={stats['count']}, avg={stats['average']}, "
                f"min={stats['min']}, max={stats['max']}"
            )
    else:
        lines.append("- No numeric score fields found.")

    if include_details:
        lines.extend(["", "Entries:"])
        for entry in summary["entries"]:
            lines.append(
                f"- {entry['path']}: chars={entry['characters']}, "
                f"source_chars={entry['source_characters']}, "
                f"sections={entry['sections']}, "
                f"citations={entry['citations']}, "
                f"avg_section_chars={entry['average_section_characters']}"
            )

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        description="统计 wiki markdown 条目的字符数、小节数和 metadata 得分。",
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path("wiki_site/docs/entries"),
        help="要统计的 markdown 目录，默认 wiki_site/docs/entries。",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_false",
        dest="recursive",
        help="只统计目录第一层的 .md 文件。",
    )
    parser.add_argument(
        "--include-index",
        action="store_true",
        help="包含 index.md；默认跳过 index.md。",
    )
    parser.add_argument(
        "--include-sources",
        action="store_true",
        help="把 Sources/参考资料小节计入字符数和小节数；默认排除。",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="读取 markdown 文件的编码，默认 utf-8。",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="输出格式，默认 text。",
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="在 text 输出中附加每个条目的统计明细；json 始终包含明细。",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI."""
    args = build_parser().parse_args(argv)
    summary = analyze_directory(
        args.directory,
        recursive=args.recursive,
        include_index=args.include_index,
        include_sources=args.include_sources,
        encoding=args.encoding,
    )

    if args.format == "json":
        sys.stdout.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    else:
        sys.stdout.write(format_text(summary, include_details=args.details) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
