import asyncio
import importlib.util
import json
import sys
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage

from open_deep_research.persistence import save_markdown_report, slugify_filename
from open_deep_research.research import StructuredResearchDraft


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


def test_save_markdown_report_adds_metadata_and_increments_version(tmp_path):
    metadata = {
        "confidence_score": 0.82,
        "confidence_level": "high",
        "confidence_basis": {
            "cited_sources": 6,
            "source_quality_score": 0.80,
            "freshness_score": 0.90,
            "evidence_coverage_score": 0.85,
        },
    }

    first_path = save_markdown_report(
        "# Wiki",
        tmp_path,
        title_hint="H13钢",
        metadata=metadata,
    )
    second_path = save_markdown_report(
        "# Wiki 2",
        tmp_path,
        title_hint="H13钢",
        metadata=metadata,
    )

    first_content = first_path.read_text(encoding="utf-8")
    second_content = second_path.read_text(encoding="utf-8")

    assert first_path.name == "H13钢.md"
    assert second_path.name == "H13钢-1.md"
    assert first_content.startswith('---\nversion: "v1"\n')
    assert 'generated_at: "' in first_content
    assert "confidence_score: 0.82" in first_content
    assert "confidence_basis:" in first_content
    assert second_content.startswith('---\nversion: "v2"\n')


def test_slugify_filename_preserves_chinese_title():
    assert slugify_filename("压铸工艺") == "压铸工艺"
    assert slugify_filename("die casting / velocity") == "die casting - velocity"


def test_record_from_topic_builds_single_record():
    cli = load_cli_module()

    assert cli._record_from_topic(" 压铸速度 ", "speed") == {
        "id": "speed",
        "topic": "压铸速度",
    }


def test_read_wiki_entries_parses_pipe_delimited_file(tmp_path):
    cli = load_cli_module()
    input_path = tmp_path / "wiki_entries.txt"
    input_path.write_text(
        "# comment\n"
        "H13钢|热作模具钢，描述可能不完整\n"
        "压铸速度|\n"
        "浇口速度\n",
        encoding="utf-8",
    )

    assert cli._read_wiki_entries(input_path) == [
        {
            "id": "H13钢",
            "name": "H13钢",
            "topic": "H13钢",
            "wiki_entry_name": "H13钢",
            "description": "热作模具钢，描述可能不完整",
            "wiki_entry_description": "热作模具钢，描述可能不完整",
        },
        {
            "id": "压铸速度",
            "name": "压铸速度",
            "topic": "压铸速度",
            "wiki_entry_name": "压铸速度",
        },
        {
            "id": "浇口速度",
            "name": "浇口速度",
            "topic": "浇口速度",
            "wiki_entry_name": "浇口速度",
        },
    ]


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
        "thread_id": calls[0]["thread_id"],
        "wiki_entry_name": None,
        "wiki_entry_description": None,
    }]
    assert results == [{
        "id": "entry-1",
        "name": None,
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
    assert calls[0]["thread_id"]
    assert calls[0]["wiki_entry_name"] is None
    assert results[0]["ok"] is True
    assert results_path.exists()


def test_run_batch_supports_wiki_entries_txt(monkeypatch, tmp_path):
    cli = load_cli_module()
    input_path = tmp_path / "wiki_entries.txt"
    input_path.write_text("H13钢|热作模具钢\n", encoding="utf-8")
    calls = []

    async def fake_run_wiki_pipeline(user_content, **kwargs):
        calls.append({"user_content": user_content, **kwargs})
        return {"final_report": "markdown"}

    monkeypatch.setattr(cli, "run_wiki_pipeline", fake_run_wiki_pipeline)

    results = asyncio.run(cli.run_batch(
        input_path,
        output_dir=tmp_path / "out",
        results_path=tmp_path / "results.jsonl",
        input_format="auto",
        api_url="http://127.0.0.1:2024",
    ))

    assert calls[0]["user_content"].startswith("目标词条：H13钢")
    assert "描述提示：热作模具钢" in calls[0]["user_content"]
    assert calls[0]["output_filename"] == "H13钢.md"
    assert calls[0]["thread_id"]
    assert calls[0]["wiki_entry_name"] == "H13钢"
    assert calls[0]["wiki_entry_description"] == "热作模具钢"
    assert results[0]["id"] == "H13钢"
    assert results[0]["name"] == "H13钢"
    assert results[0]["ok"] is True


def test_run_batch_limit_only_processes_first_k_records(monkeypatch, tmp_path):
    cli = load_cli_module()
    input_path = tmp_path / "wiki_entries.txt"
    input_path.write_text(
        "H13钢|热作模具钢\n"
        "压铸速度|工艺参数\n"
        "浇口速度|入口速度\n",
        encoding="utf-8",
    )
    calls = []

    async def fake_run_wiki_pipeline(user_content, **kwargs):
        calls.append({"user_content": user_content, **kwargs})
        return {"final_report": "markdown"}

    monkeypatch.setattr(cli, "run_wiki_pipeline", fake_run_wiki_pipeline)

    results = asyncio.run(cli.run_batch(
        input_path,
        output_dir=tmp_path / "out",
        results_path=tmp_path / "results.jsonl",
        input_format="wiki-entries",
        limit=2,
        max_concurrency=3,
    ))

    assert [result["id"] for result in results] == ["H13钢", "压铸速度"]
    assert [call["wiki_entry_name"] for call in calls] == ["H13钢", "压铸速度"]
    assert len({call["thread_id"] for call in calls}) == 2


def test_main_passes_limit_and_concurrency_to_batch(monkeypatch, tmp_path):
    cli = load_cli_module()
    input_path = tmp_path / "wiki_entries.txt"
    input_path.write_text("H13钢|热作模具钢\n", encoding="utf-8")
    calls = []

    async def fake_run_batch(input_path_arg, **kwargs):
        calls.append({"input_path": input_path_arg, **kwargs})
        return [{"id": "H13钢", "ok": True}]

    monkeypatch.setattr(cli, "run_batch", fake_run_batch)
    monkeypatch.setattr(sys, "argv", [
        "cli.py",
        str(input_path),
        "--env-file",
        str(tmp_path / "missing.env"),
        "--limit",
        "5",
        "--concurrency",
        "4",
        "--input-format",
        "wiki-entries",
        "--no-progress",
    ])

    cli.main()

    assert calls[0]["input_path"] == input_path
    assert calls[0]["limit"] == 5
    assert calls[0]["max_concurrency"] == 4
    assert calls[0]["input_format"] == "wiki-entries"
    assert calls[0]["show_progress"] is False


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
    assert calls[0]["thread_id"]
    assert calls[0]["wiki_entry_name"] is None
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


def test_brief_input_includes_structured_wiki_entry_metadata():
    from open_deep_research import deep_researcher

    formatted = deep_researcher._format_brief_input({
        "messages": [HumanMessage(content="批量生成")],
        "wiki_entry_name": "H13钢",
        "wiki_entry_description": "热作模具钢，描述可能不准确",
    })

    assert "<WikiEntryInput>" in formatted
    assert "wiki_entry_name: H13钢" in formatted
    assert "wiki_entry_description: 热作模具钢，描述可能不准确" in formatted
    assert "weak hint only" in formatted
    assert "<ConversationMessages>" in formatted


def test_wiki_writer_saves_markdown_in_thread(monkeypatch, tmp_path):
    from open_deep_research import deep_researcher

    calls = []
    model_configs = []

    class FakeModel:
        def with_config(self, config):
            model_configs.append(config)
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
                "final_report_api_key": "writer-key",
                "final_report_base_url": "http://127.0.0.1:9100/v1",
            }
        },
    ))

    assert calls
    assert calls[0][0] is deep_researcher.save_markdown_report
    assert calls[0][1][3] == "H13钢"
    assert calls[0][2]["return_content"] is True
    assert calls[0][2]["metadata"]["confidence_score"] == 0.0
    assert model_configs[0]["api_key"] == "writer-key"
    assert model_configs[0]["base_url"] == "http://127.0.0.1:9100/v1"
    assert result["final_report"].startswith('---\nversion: "v1"\n')
    assert "confidence_level: \"very_low\"" in result["final_report"]
    assert "# Wiki" in result["final_report"]
    assert result["final_report_path"] == str(tmp_path / "H13钢.md")


def test_write_research_brief_uses_dedicated_brief_model_config(monkeypatch):
    from open_deep_research import deep_researcher

    model_configs = []

    class FakeModel:
        def with_structured_output(self, schema):
            raise AssertionError("write_research_brief should not use response_format")

        def with_retry(self, **kwargs):
            return self

        def with_config(self, config):
            model_configs.append(config)
            return self

        async def ainvoke(self, messages):
            return AIMessage(content='```json\n{"research_brief":"brief"}\n```')

    monkeypatch.setattr(deep_researcher, "configurable_model", FakeModel())

    result = asyncio.run(deep_researcher.write_research_brief(
        {"messages": [HumanMessage(content="H13钢")]},
        {
            "configurable": {
                "brief_model": "openai:brief-model",
                "brief_model_max_tokens": 1234,
                "brief_api_key": "brief-key",
                "brief_base_url": "http://127.0.0.1:9050/v1",
                "research_model": "openai:research-model",
                "research_model_max_tokens": 9999,
            }
        },
    ))

    assert model_configs[0]["model"] == "openai:brief-model"
    assert model_configs[0]["max_tokens"] == 1234
    assert model_configs[0]["api_key"] == "brief-key"
    assert model_configs[0]["base_url"] == "http://127.0.0.1:9050/v1"
    assert result.update["research_brief"] == "brief"


def test_compress_research_applies_config_to_structured_runnable(monkeypatch):
    from open_deep_research import deep_researcher

    calls = []

    class FakeStructuredModel:
        def with_config(self, config):
            calls.append(("structured_config", config))
            return self

        async def ainvoke(self, messages):
            calls.append(("ainvoke", messages))
            return StructuredResearchDraft(findings=[])

    class FakeModel:
        def with_config(self, config):
            calls.append(("base_config", config))
            return self

        def with_structured_output(self, schema):
            calls.append(("structured_output", schema))
            return FakeStructuredModel()

    monkeypatch.setattr(deep_researcher, "configurable_model", FakeModel())

    result = asyncio.run(deep_researcher.compress_research(
        {
            "research_topic": "H13钢",
            "researcher_messages": [AIMessage(content="notes")],
        },
        {
            "configurable": {
                "compression_model": "openai:compress-model",
                "compression_model_max_tokens": 1234,
            }
        },
    ))

    assert calls[0] == ("structured_output", StructuredResearchDraft)
    assert calls[1][0] == "structured_config"
    assert calls[1][1]["model"] == "openai:compress-model"
    assert calls[1][1]["max_tokens"] == 1234
    assert calls[2][0] == "ainvoke"
    assert all(call[0] != "base_config" for call in calls)
    assert result["structured_research"].research_topic == "H13钢"
