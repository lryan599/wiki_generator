"""Persistence helpers for generated wiki markdown files."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping


def slugify_filename(value: str | None, fallback: str = "wiki") -> str:
    """Create a filesystem-safe filename stem while preserving user text."""
    raw_value = (value or "").strip()
    slug = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "-", raw_value)
    slug = re.sub(r"\s+", " ", slug).strip(" .-_")
    if not slug:
        slug = fallback
    return slug


def _deduplicate_path(path: Path) -> Path:
    """Return a non-existing path by appending a numeric suffix when needed."""
    return _allocate_versioned_path(path)[0]


def _allocate_versioned_path(path: Path) -> tuple[Path, int]:
    """Return a non-existing path and its generated document version number."""
    if not path.exists():
        return path, 1

    for index in range(1, 10_000):
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        if not candidate.exists():
            return candidate, index + 1
    raise FileExistsError(f"Could not allocate a unique output path for {path}")


def _format_yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return str(value)
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _render_yaml_lines(data: Mapping[str, Any], indent: int = 0) -> list[str]:
    lines = []
    prefix = " " * indent
    for key, value in data.items():
        if isinstance(value, Mapping):
            lines.append(f"{prefix}{key}:")
            lines.extend(_render_yaml_lines(value, indent + 2))
        else:
            lines.append(f"{prefix}{key}: {_format_yaml_scalar(value)}")
    return lines


def add_markdown_metadata(
    markdown: str,
    metadata: Mapping[str, Any],
    *,
    version: int,
    generated_at: datetime | None = None,
) -> str:
    """Prepend generated wiki metadata as YAML front matter."""
    timestamp = (generated_at or datetime.now().astimezone()).replace(microsecond=0)
    front_matter: dict[str, Any] = {
        "version": f"v{version}",
        "generated_at": timestamp.isoformat(),
        **metadata,
    }
    body = re.sub(r"\A---\n.*?\n---\n\n?", "", markdown, flags=re.DOTALL).lstrip()
    return "---\n" + "\n".join(_render_yaml_lines(front_matter)) + "\n---\n\n" + body


def _split_table_row(line: str) -> list[str]:
    """Split a Markdown table row while preserving escaped pipes."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith(r"\|"):
        stripped = stripped[:-1]
    return [
        cell.replace(r"\|", "|").strip()
        for cell in re.split(r"(?<!\\)\|", stripped)
    ]


def _render_table_row(cells: list[str]) -> str:
    """Render normalized Markdown table cells."""
    escaped = [cell.replace("|", r"\|") for cell in cells]
    return "| " + " | ".join(escaped) + " |"


def _is_table_separator(line: str) -> bool:
    cells = _split_table_row(line)
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell)
        for cell in cells
    )


def _normalize_latex_commands(match: re.Match[str]) -> str:
    """Collapse duplicated backslashes inside a math expression."""
    expression = re.sub(
        r"\\\\(?=[A-Za-z])",
        lambda _: "\\",
        match.group(2),
    )
    return match.group(1) + expression + match.group(3)


def normalize_markdown_for_mkdocs(markdown: str) -> str:
    """Normalize generated tables for Python-Markdown and MkDocs."""
    has_trailing_newline = markdown.endswith(("\n", "\r"))
    markdown = markdown.replace(r"\\(", r"\(").replace(r"\\)", r"\)")
    markdown = markdown.replace(r"\\[", r"\[").replace(r"\\]", r"\]")
    for pattern in (
        r"(\$\$)(.*?)(\$\$)",
        r"(\\\[)(.*?)(\\\])",
        r"(\\\()(.*?)(\\\))",
        r"(?<!\$)(\$)(?!\$)(.*?)(?<!\$)(\$)(?!\$)",
    ):
        markdown = re.sub(
            pattern,
            _normalize_latex_commands,
            markdown,
            flags=re.DOTALL,
        )
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    normalized: list[str] = []
    index = 0

    while index < len(lines):
        if re.match(r"^\s*!\[[^\]]*\]\([^)]+\)(?:\[\[S\d+(?:,S\d+)*\]\])?\s*$", lines[index]):
            if normalized and normalized[-1].strip():
                normalized.append("")
            normalized.append(lines[index].strip())
            if index + 1 < len(lines) and lines[index + 1].strip():
                normalized.append("")
            index += 1
            continue

        if re.match(r"^\s*(?:\d+[.)]|[-+*])\s+", lines[index]):
            normalized.append(lines[index])
            index += 1
            while (
                index < len(lines)
                and re.match(r"^\s*(?:\d+[.)]|[-+*])\s+", lines[index])
            ):
                normalized.append(lines[index])
                index += 1
            if index < len(lines) and lines[index].strip():
                normalized.append("")
            continue

        if re.fullmatch(r"\s*\$\$.+\$\$\s*", lines[index]):
            if normalized and normalized[-1].strip():
                normalized.append("")
            normalized.append(lines[index].strip())
            if index + 1 < len(lines) and lines[index + 1].strip():
                normalized.append("")
            index += 1
            continue

        if (
            index + 1 < len(lines)
            and lines[index].lstrip().startswith("|")
            and _is_table_separator(lines[index + 1])
        ):
            if normalized and normalized[-1].strip():
                normalized.append("")

            header_cells = _split_table_row(lines[index])
            column_count = len(header_cells)
            normalized.append(_render_table_row(header_cells))
            normalized.append(_render_table_row(_split_table_row(lines[index + 1])))
            index += 2

            while index < len(lines) and lines[index].lstrip().startswith("|"):
                cells = _split_table_row(lines[index])
                if len(cells) > column_count:
                    overflow = cells[column_count:]
                    if all(
                        re.fullmatch(r"\[\[S\d+(?:,S\d+)*\]\]", cell)
                        for cell in overflow
                    ):
                        cells[column_count - 1] = " ".join(
                            [cells[column_count - 1], *overflow]
                        ).strip()
                        cells = cells[:column_count]
                if len(cells) < column_count:
                    cells.extend([""] * (column_count - len(cells)))
                normalized.append(_render_table_row(cells))
                index += 1

            if index < len(lines) and lines[index].strip():
                normalized.append("")
            continue

        normalized.append(lines[index])
        index += 1

    result = "\n".join(normalized).rstrip()
    return result + ("\n" if has_trailing_newline else "")


def prepare_markdown_report(
    markdown: str,
    output_dir: str | Path,
    filename: str | None = None,
    title_hint: str | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> tuple[Path, str]:
    """Resolve the output path and return the exact markdown content to save."""
    target_dir = Path(output_dir).expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    if filename:
        filename_stem = slugify_filename(Path(filename).name.removesuffix(".md"))
    else:
        filename_stem = slugify_filename(title_hint)

    target_path, version = _allocate_versioned_path(target_dir / f"{filename_stem}.md")
    if metadata is not None:
        markdown = add_markdown_metadata(markdown, metadata, version=version)
    markdown = normalize_markdown_for_mkdocs(markdown)
    return target_path, markdown


def save_markdown_report(
    markdown: str,
    output_dir: str | Path,
    filename: str | None = None,
    title_hint: str | None = None,
    metadata: Mapping[str, Any] | None = None,
    return_content: bool = False,
) -> Path | tuple[Path, str]:
    """Save a markdown report and return the absolute output path."""
    target_path, markdown = prepare_markdown_report(
        markdown,
        output_dir,
        filename,
        title_hint,
        metadata,
    )
    target_path.write_text(markdown, encoding="utf-8", newline="\n")
    if return_content:
        return target_path, markdown
    return target_path
