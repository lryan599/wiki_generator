from langchain.chat_models import init_chat_model

from open_deep_research.configuration import Configuration
from open_deep_research.research import StructuredResearch
from open_deep_research.utils import get_chat_model_config, is_token_limit_exceeded


def test_configuration_loads_separate_openai_and_knowledge_base_urls(monkeypatch):
    monkeypatch.setenv("KNOWLEDGE_BASE_URL", "http://127.0.0.1:8000")
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1")
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
    assert str(model.openai_api_base) == "http://127.0.0.1:9000/v1"


def test_non_openai_model_config_ignores_openai_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:9000/v1")

    model_config = get_chat_model_config("anthropic:claude-sonnet-4", 4096, {})

    assert "base_url" not in model_config


def test_structured_output_json_eof_is_treated_as_token_limit():
    try:
        StructuredResearch.model_validate_json('{"research_topic":"topic","findings":[{"content":"unfinished')
    except Exception as exc:
        error = exc
    else:
        raise AssertionError("Expected invalid JSON validation error")

    assert is_token_limit_exceeded(error, "openai:gpt-4.1")
