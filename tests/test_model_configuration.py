from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, LLMResult

from open_deep_research.configuration import Configuration
from open_deep_research.research import StructuredResearch
from open_deep_research.utils import (
    OpenAICompatibleUsageMetadataCallback,
    get_chat_model_config,
    is_token_limit_exceeded,
)


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
