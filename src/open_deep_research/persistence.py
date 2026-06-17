"""Persistence helpers for generated wiki markdown files."""

from __future__ import annotations

import re
from pathlib import Path


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
    if not path.exists():
        return path

    for index in range(1, 10_000):
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise FileExistsError(f"Could not allocate a unique output path for {path}")


def save_markdown_report(
    markdown: str,
    output_dir: str | Path,
    filename: str | None = None,
    title_hint: str | None = None,
) -> Path:
    """Save a markdown report and return the absolute output path."""
    target_dir = Path(output_dir).expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    if filename:
        filename_stem = slugify_filename(Path(filename).name.removesuffix(".md"))
    else:
        filename_stem = slugify_filename(title_hint)

    target_path = _deduplicate_path(target_dir / f"{filename_stem}.md")
    target_path.write_text(markdown, encoding="utf-8", newline="\n")
    return target_path
