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
    monkeypatch.setenv("SUMMARIZATION_TIMEOUT_SECONDS", "15")

    configurable = Configuration.from_runnable_config({})

    assert configurable.knowledge_base_url == "http://127.0.0.1:8000"
    assert configurable.openai_base_url == "http://127.0.0.1:9000/v1"
    assert configurable.workspace_id == "workspace"
    assert configurable.knowledge_base_query_timeout_seconds == 45
    assert configurable.knowledge_base_window_timeout_seconds == 30
    assert configurable.summarization_timeout_seconds == 15


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
