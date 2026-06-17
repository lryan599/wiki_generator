"""CLI for running the wiki generation pipeline."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import uuid
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langgraph_sdk import get_client

from open_deep_research.deep_researcher import deep_researcher
from open_deep_research.persistence import save_markdown_report, slugify_filename


def _read_json_object(path: Path) -> dict[str, Any]:
    """Read a JSON object config file."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        record = json.loads(stripped)
        if not isinstance(record, dict):
            raise ValueError(f"{path}:{line_number} must be a JSON object")
        records.append(record)
    return records


def _extract_user_content(record: dict[str, Any]) -> str:
    if isinstance(record.get("messages"), list) and record["messages"]:
        first_message = record["messages"][0]
        if isinstance(first_message, dict) and first_message.get("content"):
            return str(first_message["content"])

    for key in ("topic", "query", "content", "input"):
        if record.get(key):
            return str(record[key])

    raise ValueError("Each record must contain messages[0].content, topic, query, content, or input")


def _record_id(record: dict[str, Any], index: int) -> str:
    for key in ("id", "uuid", "name", "topic"):
        if record.get(key):
            return str(record[key])
    return f"item-{index}"


def _record_from_topic(topic: str, item_id: str | None = None) -> dict[str, Any]:
    """Build a single batch record from direct topic text."""
    normalized_topic = topic.strip()
    if not normalized_topic:
        raise ValueError("--topic must not be empty")
    record: dict[str, Any] = {"topic": normalized_topic}
    if item_id:
        record["id"] = item_id
    return record


async def run_wiki_pipeline(
    user_content: str,
    *,
    config: dict[str, Any] | None = None,
    output_dir: str | None = None,
    output_filename: str | None = None,
    thread_id: str | None = None,
    api_url: str | None = None,
    assistant_id: str = "Deep Researcher",
    api_key: str | None = None,
) -> dict[str, Any]:
    """Run one wiki generation pipeline invocation."""
    resolved_thread_id = thread_id or str(uuid.uuid4())
    configurable = {
        "thread_id": resolved_thread_id,
        "save_wiki_markdown": True,
    }
    if output_dir:
        configurable["wiki_output_dir"] = output_dir
    if output_filename:
        configurable["wiki_output_filename"] = output_filename
    if config:
        configurable.update(config)

    graph_input = {"messages": [{"role": "user", "content": user_content}]}
    graph_config = {"configurable": configurable}
    if api_url:
        return await run_wiki_pipeline_api(
            graph_input,
            graph_config,
            api_url=api_url,
            assistant_id=assistant_id,
            api_key=api_key,
            thread_id=resolved_thread_id,
            output_dir=output_dir,
            output_filename=output_filename,
            title_hint=user_content,
        )

    return await deep_researcher.ainvoke(
        graph_input,
        graph_config,
    )


async def run_wiki_pipeline_api(
    graph_input: dict[str, Any],
    graph_config: dict[str, Any],
    *,
    api_url: str,
    assistant_id: str,
    api_key: str | None,
    thread_id: str,
    output_dir: str | None,
    output_filename: str | None,
    title_hint: str,
) -> dict[str, Any]:
    """Run one pipeline invocation through the LangGraph API."""
    client_kwargs: dict[str, Any] = {"url": api_url}
    resolved_api_key = api_key or os.getenv("LANGGRAPH_API_KEY")
    if resolved_api_key:
        client_kwargs["api_key"] = resolved_api_key
    client = get_client(**client_kwargs)

    thread = await client.threads.create(thread_id=thread_id, if_exists="do_nothing")
    thread_id = thread["thread_id"]
    final_state = await client.runs.wait(
        thread_id,
        assistant_id,
        input=graph_input,
        config=graph_config,
        raise_error=True,
    )
    if isinstance(final_state, list):
        final_state = final_state[-1] if final_state else {}
    if not isinstance(final_state, dict):
        final_state = {"final_report": str(final_state)}
    final_state = {**final_state, "thread_id": thread_id}

    final_report = final_state.get("final_report")
    if isinstance(final_report, str) and output_dir:
        client_path = save_markdown_report(
            final_report,
            output_dir,
            output_filename,
            title_hint,
        )
        final_state["client_final_report_path"] = str(client_path)
    return final_state


async def run_batch(
    input_path: Path,
    *,
    output_dir: Path,
    results_path: Path,
    max_concurrency: int = 2,
    config: dict[str, Any] | None = None,
    api_url: str | None = None,
    assistant_id: str = "Deep Researcher",
    api_key: str | None = None,
) -> list[dict[str, Any]]:
    """Run the wiki pipeline for all records in a JSONL file."""
    return await run_batch_records(
        _read_jsonl(input_path),
        output_dir=output_dir,
        results_path=results_path,
        max_concurrency=max_concurrency,
        config=config,
        api_url=api_url,
        assistant_id=assistant_id,
        api_key=api_key,
    )


async def run_batch_records(
    records: list[dict[str, Any]],
    *,
    output_dir: Path,
    results_path: Path,
    max_concurrency: int = 2,
    config: dict[str, Any] | None = None,
    api_url: str | None = None,
    assistant_id: str = "Deep Researcher",
    api_key: str | None = None,
) -> list[dict[str, Any]]:
    """Run the wiki pipeline for in-memory batch records."""
    semaphore = asyncio.Semaphore(max(max_concurrency, 1))

    async def run_one(index: int, record: dict[str, Any]) -> dict[str, Any]:
        item_id = _record_id(record, index)
        user_content = _extract_user_content(record)
        item_config = {**(config or {}), **record.get("config", {})}
        output_filename = record.get("output_filename") or f"{slugify_filename(item_id)}.md"

        async with semaphore:
            try:
                final_state = await run_wiki_pipeline(
                    user_content,
                    config=item_config,
                    output_dir=str(output_dir),
                    output_filename=output_filename,
                    api_url=api_url,
                    assistant_id=assistant_id,
                    api_key=api_key,
                )
                return {
                    "id": item_id,
                    "ok": True,
                    "thread_id": final_state.get("thread_id"),
                    "final_report_path": final_state.get("final_report_path"),
                    "client_final_report_path": final_state.get("client_final_report_path"),
                    "final_report": final_state.get("final_report"),
                }
            except Exception as exc:
                return {
                    "id": item_id,
                    "ok": False,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }

    results = await asyncio.gather(*[
        run_one(index, record)
        for index, record in enumerate(records, start=1)
    ])

    results_path.parent.mkdir(parents=True, exist_ok=True)
    with results_path.open("w", encoding="utf-8", newline="\n") as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False) + "\n")
    return results


def main() -> None:
    """CLI entry point for wiki generation."""
    parser = argparse.ArgumentParser(description="Run wiki generation for one topic or a JSONL batch")
    parser.add_argument("input", nargs="?", type=Path, help="Input JSONL file")
    parser.add_argument("--topic", help="Direct topic text for a single wiki generation run")
    parser.add_argument("--id", dest="item_id", help="Optional ID/filename stem for --topic mode")
    parser.add_argument("--output-dir", type=Path, default=Path("wiki_outputs"))
    parser.add_argument("--results", type=Path, default=Path("wiki_outputs/results.jsonl"))
    parser.add_argument("--max-concurrency", type=int, default=2)
    parser.add_argument("--api-url", help="LangGraph API URL. If omitted, run the graph in-process")
    parser.add_argument("--assistant-id", default="Deep Researcher", help="LangGraph assistant/graph ID")
    parser.add_argument("--api-key", help="LangGraph API key. Defaults to LANGGRAPH_API_KEY")
    parser.add_argument(
        "--config-json",
        default="{}",
        help="JSON object merged after --config-file into each LangGraph configurable config",
    )
    parser.add_argument(
        "--config-file",
        type=Path,
        help="JSON config file merged into each LangGraph configurable config",
    )
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    args = parser.parse_args()

    if args.env_file.exists():
        load_dotenv(args.env_file)

    file_config = _read_json_object(args.config_file) if args.config_file else {}
    inline_config = json.loads(args.config_json)
    if not isinstance(inline_config, dict):
        raise ValueError("--config-json must decode to a JSON object")
    config = {**file_config, **inline_config}

    if args.topic:
        records = [_record_from_topic(args.topic, args.item_id)]
        results = asyncio.run(run_batch_records(
            records,
            output_dir=args.output_dir,
            results_path=args.results,
            max_concurrency=1,
            config=config,
            api_url=args.api_url,
            assistant_id=args.assistant_id,
            api_key=args.api_key,
        ))
    else:
        if args.input is None:
            parser.error("provide either an input JSONL file or --topic")
        results = asyncio.run(run_batch(
            args.input,
            output_dir=args.output_dir,
            results_path=args.results,
            max_concurrency=args.max_concurrency,
            config=config,
            api_url=args.api_url,
            assistant_id=args.assistant_id,
            api_key=args.api_key,
        ))
    ok_count = sum(1 for result in results if result["ok"])
    print(f"Finished {len(results)} item(s): {ok_count} succeeded, {len(results) - ok_count} failed")
    print(f"Results: {args.results.resolve()}")


if __name__ == "__main__":
    main()
