import asyncio
import importlib.util
import json
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage

from open_deep_research.persistence import save_markdown_report, slugify_filename


def load_cli_module():
    cli_path = Path(__file__).parents[1] / "src" / "cli.py"
    spec = importlib.util.spec_from_file_location("wiki_cli", cli_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_save_markdown_report_sanitizes_and_deduplicates(tmp_path):
    first_path = save_markdown_report(
        "# Wiki",
        tmp_path,
        filename="../bad:name.md",
    )
    second_path = save_markdown_report(
        "# Wiki 2",
        tmp_path,
        filename="../bad:name.md",
    )

    assert first_path.name == "bad-name.md"
    assert second_path.name == "bad-name-1.md"
    assert first_path.read_text(encoding="utf-8") == "# Wiki"
    assert second_path.read_text(encoding="utf-8") == "# Wiki 2"

    chinese_path = save_markdown_report(
        "# H13",
        tmp_path,
        title_hint="H13钢",
    )

    assert chinese_path.name == "H13钢.md"


def test_slugify_filename_preserves_chinese_title():
    assert slugify_filename("压铸工艺") == "压铸工艺"
    assert slugify_filename("die casting / velocity") == "die casting - velocity"


def test_record_from_topic_builds_single_record():
    cli = load_cli_module()

    assert cli._record_from_topic(" 压铸速度 ", "speed") == {
        "id": "speed",
        "topic": "压铸速度",
    }


def test_read_json_object_rejects_non_object_config(tmp_path):
    cli = load_cli_module()
    config_path = tmp_path / "config.json"
    config_path.write_text("[]", encoding="utf-8")

    try:
        cli._read_json_object(config_path)
    except ValueError as exc:
        assert "must contain a JSON object" in str(exc)
    else:
        raise AssertionError("Expected ValueError")


def test_run_batch_writes_result_index_without_real_graph(monkeypatch, tmp_path):
    cli = load_cli_module()
    input_path = tmp_path / "input.jsonl"
    input_path.write_text(
        json.dumps({"id": "entry-1", "topic": "压铸速度"}) + "\n",
        encoding="utf-8",
    )
    output_dir = tmp_path / "out"
    results_path = tmp_path / "results.jsonl"
    calls = []

    async def fake_run_wiki_pipeline(user_content, **kwargs):
        calls.append({"user_content": user_content, **kwargs})
        return {
            "final_report_path": str(output_dir / "entry-1.md"),
            "final_report": "markdown",
        }

    monkeypatch.setattr(cli, "run_wiki_pipeline", fake_run_wiki_pipeline)

    results = asyncio.run(cli.run_batch(
        input_path,
        output_dir=output_dir,
        results_path=results_path,
        config={"search_api": "none"},
    ))

    assert calls == [{
        "user_content": "压铸速度",
        "config": {"search_api": "none"},
        "output_dir": str(output_dir),
        "output_filename": "entry-1.md",
        "api_url": None,
        "assistant_id": "Deep Researcher",
        "api_key": None,
    }]
    assert results == [{
        "id": "entry-1",
        "ok": True,
        "thread_id": None,
        "final_report_path": str(output_dir / "entry-1.md"),
        "client_final_report_path": None,
        "final_report": "markdown",
    }]
    assert results_path.read_text(encoding="utf-8").strip() == json.dumps(
        results[0],
        ensure_ascii=False,
    )


def test_run_batch_records_supports_direct_topic_without_input_file(monkeypatch, tmp_path):
    cli = load_cli_module()
    output_dir = tmp_path / "out"
    results_path = tmp_path / "results.jsonl"
    calls = []

    async def fake_run_wiki_pipeline(user_content, **kwargs):
        calls.append({"user_content": user_content, **kwargs})
        return {
            "final_report_path": str(output_dir / "speed.md"),
            "final_report": "markdown",
        }

    monkeypatch.setattr(cli, "run_wiki_pipeline", fake_run_wiki_pipeline)

    results = asyncio.run(cli.run_batch_records(
        [{"id": "speed", "topic": "压铸速度"}],
        output_dir=output_dir,
        results_path=results_path,
    ))

    assert calls[0]["user_content"] == "压铸速度"
    assert calls[0]["output_filename"] == "speed.md"
    assert calls[0]["api_url"] is None
    assert results[0]["ok"] is True
    assert results_path.exists()


def test_run_batch_records_passes_langgraph_api_options(monkeypatch, tmp_path):
    cli = load_cli_module()
    calls = []

    async def fake_run_wiki_pipeline(user_content, **kwargs):
        calls.append({"user_content": user_content, **kwargs})
        return {
            "thread_id": "thread-1",
            "client_final_report_path": "local.md",
            "final_report": "markdown",
        }

    monkeypatch.setattr(cli, "run_wiki_pipeline", fake_run_wiki_pipeline)

    results = asyncio.run(cli.run_batch_records(
        [{"id": "speed", "topic": "压铸速度"}],
        output_dir=tmp_path / "out",
        results_path=tmp_path / "results.jsonl",
        api_url="http://127.0.0.1:2024",
        assistant_id="Deep Researcher",
        api_key="test-key",
    ))

    assert calls[0]["api_url"] == "http://127.0.0.1:2024"
    assert calls[0]["assistant_id"] == "Deep Researcher"
    assert calls[0]["api_key"] == "test-key"
    assert results[0]["thread_id"] == "thread-1"
    assert results[0]["client_final_report_path"] == "local.md"


def test_run_wiki_pipeline_api_waits_for_langgraph_run_and_saves_client_copy(monkeypatch, tmp_path):
    cli = load_cli_module()
    calls = []

    class FakeThreads:
        async def create(self, **kwargs):
            calls.append(("threads.create", kwargs))
            return {"thread_id": kwargs["thread_id"]}

    class FakeRuns:
        async def wait(self, thread_id, assistant_id, **kwargs):
            calls.append(("runs.wait", {
                "thread_id": thread_id,
                "assistant_id": assistant_id,
                **kwargs,
            }))
            return {"final_report": "# Wiki"}

    class FakeClient:
        threads = FakeThreads()
        runs = FakeRuns()

    monkeypatch.setattr(cli, "get_client", lambda **kwargs: FakeClient())

    final_state = asyncio.run(cli.run_wiki_pipeline_api(
        {"messages": [{"role": "user", "content": "压铸速度"}]},
        {"configurable": {"research_model": "openai:model"}},
        api_url="http://127.0.0.1:2024",
        assistant_id="Deep Researcher",
        api_key=None,
        thread_id="thread-1",
        output_dir=str(tmp_path),
        output_filename="speed.md",
        title_hint="压铸速度",
    ))

    assert calls[0] == (
        "threads.create",
        {"thread_id": "thread-1", "if_exists": "do_nothing"},
    )
    assert calls[1][0] == "runs.wait"
    assert calls[1][1]["thread_id"] == "thread-1"
    assert calls[1][1]["assistant_id"] == "Deep Researcher"
    assert calls[1][1]["input"]["messages"][0]["content"] == "压铸速度"
    assert calls[1][1]["config"]["configurable"]["research_model"] == "openai:model"
    assert final_state["thread_id"] == "thread-1"
    assert final_state["client_final_report_path"] == str(tmp_path / "speed.md")
    assert (tmp_path / "speed.md").read_text(encoding="utf-8") == "# Wiki"


def test_wiki_writer_saves_markdown_in_thread(monkeypatch, tmp_path):
    from open_deep_research import deep_researcher

    calls = []

    class FakeModel:
        def with_config(self, config):
            return self

        async def ainvoke(self, messages):
            return AIMessage(content="# Wiki")

    async def fake_to_thread(func, *args, **kwargs):
        calls.append((func, args, kwargs))
        return func(*args, **kwargs)

    monkeypatch.setattr(deep_researcher, "configurable_model", FakeModel())
    monkeypatch.setattr(deep_researcher.asyncio, "to_thread", fake_to_thread)

    result = asyncio.run(deep_researcher.wiki_writer(
        {
            "messages": [HumanMessage(content="H13钢")],
            "notes": ["finding"],
            "research_results": [],
            "research_brief": "压铸速度",
        },
        {
            "configurable": {
                "save_wiki_markdown": True,
                "wiki_output_dir": str(tmp_path),
                "final_report_model": "openai:test",
            }
        },
    ))

    assert calls
    assert calls[0][0] is deep_researcher.save_markdown_report
    assert calls[0][1][3] == "H13钢"
    assert result["final_report"] == "# Wiki"
    assert result["final_report_path"] == str(tmp_path / "H13钢.md")
