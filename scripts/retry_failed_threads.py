"""Retry failed LangGraph threads and save generated markdown locally."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from open_deep_research.persistence import save_markdown_report, slugify_filename

DEFAULT_DEPLOYMENT_URL = "http://localhost:8123"
DEFAULT_ASSISTANT_ID = "Deep Researcher"
DEFAULT_LOCAL_TZ = "Asia/Shanghai"
DEFAULT_AFTER_LOCAL = "2026-06-18T00:00:00"
DEFAULT_OUTPUT_DIR = "wiki_site/docs/entries"
LIMIT = 100


def parse_ts(ts: str) -> datetime:
    """Parse a LangGraph timestamp as UTC."""
    if ts.endswith("Z"):
        ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts).astimezone(timezone.utc)


def parse_local_datetime(value: str, tz_name: str) -> datetime:
    """Parse a local datetime string and attach the configured timezone."""
    local_tz = ZoneInfo(tz_name)
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=local_tz)
    return parsed.astimezone(local_tz)


def extract_state_values(state: Any) -> dict[str, Any]:
    """Return the LangGraph state values from SDK state shapes."""
    if isinstance(state, dict):
        values = state.get("values")
        if isinstance(values, dict):
            return values
        return state

    values = getattr(state, "values", None)
    if isinstance(values, dict):
        return values
    return {}


def title_hint_from_thread(thread: dict[str, Any], values: dict[str, Any]) -> str:
    """Find a stable title hint for the output markdown filename."""
    metadata = thread.get("metadata") or {}
    for source in (values, metadata):
        for key in (
            "wiki_entry_name",
            "name",
            "topic",
            "id",
            "output_filename",
        ):
            value = source.get(key)
            if value:
                return str(value)
    return str(thread["thread_id"])


def output_filename_from_thread(thread: dict[str, Any], values: dict[str, Any]) -> str:
    """Resolve the markdown filename to use for a retried thread."""
    metadata = thread.get("metadata") or {}
    for source in (values, metadata):
        output_filename = source.get("wiki_output_filename") or source.get(
            "output_filename"
        )
        if output_filename:
            return f"{slugify_filename(Path(str(output_filename)).name.removesuffix('.md'))}.md"

    return f"{slugify_filename(title_hint_from_thread(thread, values))}.md"


async def list_threads_after(
    client: Any,
    after_utc: datetime,
    *,
    before_utc: datetime | None = None,
    status: str | None,
    limit: int = LIMIT,
) -> list[dict[str, Any]]:
    """Find threads updated in the requested time range."""
    results: list[dict[str, Any]] = []
    offset = 0

    while True:
        search_kwargs: dict[str, Any] = dict(
            limit=limit,
            offset=offset,
            sort_by="updated_at",
            sort_order="desc",
        )
        if status is not None:
            search_kwargs["status"] = status
        batch = await client.threads.search(**search_kwargs)
        if not batch:
            break

        should_stop = False
        for thread in batch:
            updated_at = parse_ts(thread["updated_at"])
            if before_utc is not None and updated_at >= before_utc:
                continue
            if updated_at >= after_utc:
                results.append(thread)
            else:
                should_stop = True
                break

        if should_stop or len(batch) < limit:
            break
        offset += len(batch)

    return results


async def list_error_threads_after(
    client: Any,
    after_utc: datetime,
    *,
    limit: int = LIMIT,
) -> list[dict[str, Any]]:
    """Find error threads updated after the cutoff."""
    return await list_threads_after(
        client,
        after_utc,
        status="error",
        limit=limit,
    )


async def save_thread_markdown(
    client: Any,
    thread: dict[str, Any],
    *,
    output_dir: Path,
) -> Path | None:
    """Fetch a thread's final report from state and save it to output_dir."""
    state = await client.threads.get_state(thread["thread_id"])
    values = extract_state_values(state)
    final_report = values.get("final_report")
    if not isinstance(final_report, str) or not final_report.strip():
        return None

    return save_markdown_report(
        final_report,
        output_dir,
        output_filename_from_thread(thread, values),
        title_hint_from_thread(thread, values),
    )


async def retry_thread(
    client: Any,
    thread: dict[str, Any],
    sem: asyncio.Semaphore,
    *,
    output_dir: Path,
) -> dict[str, Any]:
    """Retry one thread, wait for completion, and save its markdown report."""
    async with sem:
        thread_id = thread["thread_id"]
        metadata = thread.get("metadata") or {}
        assistant_id = (
            metadata.get("assistant_id")
            or metadata.get("graph_id")
            or DEFAULT_ASSISTANT_ID
        )

        try:
            run = await client.runs.create(
                thread_id,
                assistant_id,
                input=None,
                config={
                    "configurable": {
                        "save_wiki_markdown": True,
                        "wiki_output_dir": str(output_dir),
                    },
                },
                metadata={
                    "retry_reason": "bulk_retry_failed_threads_after_2026_06_18",
                    "original_thread_updated_at": thread.get("updated_at"),
                },
            )
            await client.runs.join(thread_id, run["run_id"])
            final_run = await client.runs.get(thread_id, run["run_id"])
            status = final_run.get("status")
            saved_path = await save_thread_markdown(
                client,
                thread,
                output_dir=output_dir,
            )
            return {
                "ok": status == "success" and saved_path is not None,
                "thread_id": thread_id,
                "updated_at": thread.get("updated_at"),
                "assistant_id": assistant_id,
                "run_id": run["run_id"],
                "run_status": status,
                "client_final_report_path": str(saved_path) if saved_path else None,
            }
        except Exception as exc:
            return {
                "ok": False,
                "thread_id": thread_id,
                "updated_at": thread.get("updated_at"),
                "assistant_id": assistant_id,
                "error_type": type(exc).__name__,
                "error": str(exc),
            }


async def run(
    *,
    deployment_url: str,
    api_key: str | None,
    after_local: datetime,
    before_local: datetime | None,
    output_dir: Path,
    concurrency: int,
    retry: bool,
    save_existing: bool,
    status: str | None,
    results_path: Path | None,
) -> list[dict[str, Any]]:
    """Run the retry workflow."""
    from langgraph_sdk import get_client

    client_kwargs: dict[str, Any] = {"url": deployment_url}
    if api_key:
        client_kwargs["api_key"] = api_key
    client = get_client(**client_kwargs)

    after_utc = after_local.astimezone(timezone.utc)
    before_utc = before_local.astimezone(timezone.utc) if before_local else None
    threads = await list_threads_after(
        client,
        after_utc,
        before_utc=before_utc,
        status=status,
    )
    status_label = status or "all"

    print(f"AFTER_LOCAL = {after_local.isoformat()}")
    print(f"AFTER_UTC   = {after_utc.isoformat()}")
    if before_local:
        print(f"BEFORE_LOCAL = {before_local.isoformat()}")
        print(f"BEFORE_UTC   = {before_utc.isoformat()}")
    print(f"Found {len(threads)} {status_label} thread(s)")

    if not retry and not save_existing:
        for thread in threads[:20]:
            print(thread["thread_id"], thread.get("updated_at"), thread.get("metadata"))
        print(
            "Dry run only. Pass --retry to rerun, or --save-existing to export existing final_report values."
        )
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    if retry:
        sem = asyncio.Semaphore(max(concurrency, 1))
        results = await asyncio.gather(
            *(
                retry_thread(client, thread, sem, output_dir=output_dir)
                for thread in threads
            )
        )
    else:
        results = []
        for thread in threads:
            saved_path = await save_thread_markdown(
                client, thread, output_dir=output_dir
            )
            results.append(
                {
                    "ok": saved_path is not None,
                    "thread_id": thread["thread_id"],
                    "updated_at": thread.get("updated_at"),
                    "client_final_report_path": str(saved_path) if saved_path else None,
                }
            )

    for result in results:
        if result["ok"]:
            print(
                f"[OK] thread={result['thread_id']} "
                f"run={result.get('run_id')} "
                f"status={result.get('run_status')} "
                f"path={result.get('client_final_report_path')}"
            )
        else:
            print(
                f"[FAIL] thread={result['thread_id']} "
                f"status={result.get('run_status')} "
                f"error={result.get('error_type')}: {result.get('error')}"
            )

    if results_path:
        results_path.parent.mkdir(parents=True, exist_ok=True)
        with results_path.open("w", encoding="utf-8", newline="\n") as file:
            for result in results:
                file.write(json.dumps(result, ensure_ascii=False) + "\n")

    return results


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deployment-url", default=DEFAULT_DEPLOYMENT_URL)
    parser.add_argument("--api-key")
    parser.add_argument("--after-local", default=DEFAULT_AFTER_LOCAL)
    parser.add_argument(
        "--before-local",
        help="Exclusive local upper bound, for example 2026-06-25T00:00:00",
    )
    parser.add_argument("--timezone", default=DEFAULT_LOCAL_TZ)
    parser.add_argument("--output-dir", type=Path, default=Path(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--concurrency", type=int, default=5)
    parser.add_argument(
        "--results", type=Path, default=Path("wiki_outputs/retry_failed_threads.jsonl")
    )
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    parser.add_argument(
        "--status",
        choices=["error", "idle", "busy", "interrupted", "all"],
        help=(
            "Thread status to scan. Defaults to error for retry/dry-run and idle "
            "for --save-existing."
        ),
    )
    parser.add_argument(
        "--retry", action="store_true", help="Actually rerun the failed threads"
    )
    parser.add_argument(
        "--save-existing",
        action="store_true",
        help="Do not rerun; only export final_report values already present in thread state",
    )
    args = parser.parse_args()

    if args.env_file.exists():
        from dotenv import load_dotenv

        load_dotenv(args.env_file)

    after_local = parse_local_datetime(args.after_local, args.timezone)
    before_local = (
        parse_local_datetime(args.before_local, args.timezone)
        if args.before_local
        else None
    )
    status = args.status
    if status is None:
        status = "error" if args.retry or not args.save_existing else "idle"
    status_filter = None if status == "all" else status
    asyncio.run(
        run(
            deployment_url=args.deployment_url,
            api_key=args.api_key or os.getenv("LANGGRAPH_API_KEY"),
            after_local=after_local,
            before_local=before_local,
            output_dir=args.output_dir,
            concurrency=args.concurrency,
            retry=args.retry,
            save_existing=args.save_existing,
            status=status_filter,
            results_path=args.results,
        )
    )


if __name__ == "__main__":
    main()
