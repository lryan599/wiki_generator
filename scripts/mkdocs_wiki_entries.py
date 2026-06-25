"""Generate a lightweight wiki entry manifest for the MkDocs sidebar."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mkdocs.structure.files import File, Files, InclusionLevel

OUTPUT_PATH = "assets/data/wiki-entries.json"
ENTRIES_DIR = "entries"


def _entry_title(src_uri: str) -> str:
    return Path(src_uri).stem


def _entry_sort_key(entry: dict[str, str]) -> tuple[str, str]:
    return (entry["title"].casefold(), entry["source"].casefold())


def on_files(files: Files, config: dict[str, Any]) -> Files:
    entries: list[dict[str, str]] = []

    for file in files:
        src_uri = file.src_uri
        if not (
            src_uri.startswith(f"{ENTRIES_DIR}/")
            and src_uri.endswith(".md")
            and Path(src_uri).name.lower() != "index.md"
            and file.inclusion.is_included()
        ):
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
