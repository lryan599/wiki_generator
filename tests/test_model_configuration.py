import os
from enum import Enum
from pathlib import Path

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, LLMResult

from open_deep_research.configuration import Configuration, _parse_env_value
from open_deep_research.research import StructuredResearch
from open_deep_research.utils import (
    OpenAICompatibleUsageMetadataCallback,
    get_chat_model_config,
    is_token_limit_exceeded,
)


_SCHEMA_ENV_DEFAULT_FIELDS = {
    "max_structured_output_retries",
    "allow_clarification",
    "max_concurrent_research_units",
    "search_api",
    "knowledge_base_url",
    "workspace_id",
    "openai_base_url",
    "final_report_base_url",
    "knowledge_base_query_timeout_seconds",
    "knowledge_base_window_timeout_seconds",
    "compression_image_limit",
    "compression_image_max_bytes",
    "save_wiki_markdown",
    "wiki_output_dir",
    "wiki_output_filename",
    "max_researcher_iterations",
    "max_react_tool_calls",
    "summarization_model",
    "summarization_model_max_tokens",
    "summarization_timeout_seconds",
    "max_content_length",
    "brief_model",
    "brief_model_max_tokens",
    "brief_base_url",
    "research_model",
    "research_model_max_tokens",
    "compression_model",
    "compression_model_max_tokens",
    "final_report_model",
    "final_report_model_max_tokens",
    "mcp_config",
    "mcp_prompt",
}


def _env_example_values() -> dict[str, str]:
    env_path = Path(__file__).resolve().parents[1] / ".env.example"
    values: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.lower()] = value
    return values


def _field_ui_config(field: object) -> dict | None:
    candidates: list[dict] = []
    json_schema_extra = getattr(field, "json_schema_extra", None)
    if isinstance(json_schema_extra, dict):
        candidates.append(json_schema_extra)
        metadata = json_schema_extra.get("metadata")
        if isinstance(metadata, dict):
            candidates.append(metadata)
    metadata_items = getattr(field, "metadata", ())
    for metadata_item in metadata_items:
        if isinstance(metadata_item, dict):
            candidates.append(metadata_item)

    for candidate in candidates:
        ui_config = candidate.get("x_oap_ui_config")
        if isinstance(ui_config, dict):
            return ui_config
    return None


def _default_value(value: object) -> object:
    if isinstance(value, Enum):
        return value.value
    return value


def test_configuration_defaults_match_env_example():
    env_values = _env_example_values()
    field_names = set(Configuration.model_fields)

    assert field_names <= set(env_values)

    env_default_values = {
        field_name: _parse_env_value(os.environ.get(field_name.upper(), env_values[field_name]))
        if field_name in _SCHEMA_ENV_DEFAULT_FIELDS
        else _parse_env_value(env_values[field_name])
        for field_name in field_names
    }
    env_default_config = Configuration(**env_default_values)
    code_default_config = Configuration()

    for field_name in sorted(field_names):
        assert getattr(code_default_config, field_name) == getattr(env_default_config, field_name)


def test_oap_ui_defaults_match_model_defaults():
    for field_name, field in Configuration.model_fields.items():
        ui_config = _field_ui_config(field)
        if not ui_config or "default" not in ui_config:
            continue

        assert ui_config["default"] == _default_value(field.default), field_name


def test_configuration_defaults_wiki_output_to_mkdocs_docs(monkeypatch):
    monkeypatch.delenv("WIKI_OUTPUT_DIR", raising=False)

    configurable = Configuration.from_runnable_config({})

    assert configurable.wiki_output_dir == "wiki_site/docs/entries"


def test_configuration_loads_separate_openai_and_knowledge_base_urls(monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_BASE_URL", "http://127.0.0.1:8000")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1")
    monkeypatch.setenv("BRIEF_MODEL", "openai:brief-model")
    monkeypatch.setenv("BRIEF_MODEL_MAX_TOKENS", "1234")
    monkeypatch.setenv("BRIEF_API_KEY", "brief-key")
    monkeypatch.setenv("BRIEF_BASE_URL", "http://127.0.0.1:9050/v1")
    monkeypatch.setenv("FINAL_REPORT_API_KEY", "writer-key")
    monkeypatch.setenv("FINAL_REPORT_BASE_URL", "http://127.0.0.1:9100/v1")
    monkeypatch.setenv("WORKSPACE_ID", "workspace")
    monkeypatch.setenv("KNOWLEDGE_BASE_QUERY_TIMEOUT_SECONDS", "45")
    monkeypatch.setenv("KNOWLEDGE_BASE_WINDOW_TIMEOUT_SECONDS", "30")
    monkeypatch.setenv("COMPRESSION_IMAGE_LIMIT", "6")
    monkeypatch.setenv("COMPRESSION_IMAGE_MAX_BYTES", "1234567")
    monkeypatch.setenv("SAVE_WIKI_MARKDOWN", "false")
    monkeypatch.setenv("WIKI_OUTPUT_DIR", "custom_outputs")
    monkeypatch.setenv("SUMMARIZATION_TIMEOUT_SECONDS", "15")

    configurable = Configuration.from_runnable_config({})

    assert configurable.knowledge_base_url == "http://127.0.0.1:8000"
    assert configurable.openai_base_url == "http://127.0.0.1:9000/v1"
    assert configurable.brief_model == "openai:brief-model"
    assert configurable.brief_model_max_tokens == 1234
    assert configurable.brief_api_key == "brief-key"
    assert configurable.brief_base_url == "http://127.0.0.1:9050/v1"
    assert configurable.final_report_api_key == "writer-key"
    assert configurable.final_report_base_url == "http://127.0.0.1:9100/v1"
    assert configurable.workspace_id == "workspace"
    assert configurable.knowledge_base_query_timeout_seconds == 45
    assert configurable.knowledge_base_window_timeout_seconds == 30
    assert configurable.compression_image_limit == 6
    assert configurable.compression_image_max_bytes == 1234567
    assert configurable.save_wiki_markdown is False
    assert configurable.wiki_output_dir == "custom_outputs"
    assert configurable.summarization_timeout_seconds == 15


def test_configuration_parses_json_env_values_and_ignores_empty_strings(monkeypatch):
    monkeypatch.setenv(
        "MCP_CONFIG",
        '{"url":"http://127.0.0.1:9001","tools":["lookup"],"auth_required":true}',
    )
    monkeypatch.setenv("MCP_PROMPT", "")

    configurable = Configuration.from_runnable_config({})

    assert configurable.mcp_config.url == "http://127.0.0.1:9001"
    assert configurable.mcp_config.tools == ["lookup"]
    assert configurable.mcp_config.auth_required is True
    assert configurable.mcp_prompt is None


def test_runnable_config_overrides_environment(monkeypatch):
    monkeypatch.setenv("RESEARCH_MODEL", "openai:env-model")

    configurable = Configuration.from_runnable_config({
        "configurable": {"research_model": "openai:runtime-model"}
    })

    assert configurable.research_model == "openai:runtime-model"


def test_openai_model_config_uses_compatible_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1/")

    model_config = get_chat_model_config("openai:custom-model", 4096, {})
    model = init_chat_model(**model_config)

    assert model_config["base_url"] == "http://127.0.0.1:9000/v1"
    assert model_config["stream_usage"] is True
    assert isinstance(model_config["callbacks"][0], OpenAICompatibleUsageMetadataCallback)
    assert str(model.openai_api_base) == "http://127.0.0.1:9000/v1"


def test_final_report_model_config_can_override_key_and_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "research-key")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1")

    default_config = get_chat_model_config("openai:research-model", 4096, {})
    writer_config = get_chat_model_config(
        "openai:writer-model",
        8192,
        {},
        api_key="writer-key",
        base_url="http://127.0.0.1:9100/v1/",
    )

    assert default_config["api_key"] == "research-key"
    assert default_config["base_url"] == "http://127.0.0.1:9000/v1"
    assert writer_config["api_key"] == "writer-key"
    assert writer_config["base_url"] == "http://127.0.0.1:9100/v1"
    assert writer_config["stream_usage"] is True
    assert isinstance(writer_config["callbacks"][0], OpenAICompatibleUsageMetadataCallback)


def test_non_openai_model_config_ignores_openai_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1")

    model_config = get_chat_model_config("anthropic:claude-sonnet-4", 4096, {})

    assert "base_url" not in model_config
    assert "stream_usage" not in model_config
    assert "callbacks" not in model_config


def test_openai_usage_callback_copies_token_usage_to_usage_metadata():
    message = AIMessage(
        content="",
        response_metadata={
            "token_usage": {
                "prompt_tokens": 10,
                "completion_tokens": 5,
                "total_tokens": 15,
                "prompt_tokens_details": {"cached_tokens": 3},
                "completion_tokens_details": {"reasoning_tokens": 2},
            }
        },
    )
    result = LLMResult(
        generations=[[ChatGeneration(message=message, generation_info={})]]
    )

    OpenAICompatibleUsageMetadataCallback().on_llm_end(result)

    assert message.usage_metadata == {
        "input_tokens": 10,
        "output_tokens": 5,
        "total_tokens": 15,
        "input_token_details": {"cache_read": 3},
        "output_token_details": {"reasoning": 2},
    }


def test_structured_output_json_eof_is_treated_as_token_limit():
    try:
        StructuredResearch.model_validate_json('{"research_topic":"topic","findings":[{"content":"unfinished')
    except Exception as exc:
        error = exc
    else:
        raise AssertionError("Expected invalid JSON validation error")

    assert is_token_limit_exceeded(error, "openai:gpt-4.1")
