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
