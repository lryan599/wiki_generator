"""Configuration management for the Open Deep Research system."""

import json
import os
from enum import Enum
from typing import Any, List

from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field


class SearchAPI(Enum):
    """Enumeration of available search API providers."""
    
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    TAVILY = "tavily"
    NONE = "none"


def _parse_env_value(value: str) -> Any:
    """Parse JSON-like environment values while leaving simple strings intact."""
    stripped = value.strip()
    if stripped == "":
        return None
    if stripped[0:1] in {"{", "["}:
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            return value
    return value


def _env_default(field_name: str, fallback: Any, parser: Any = None) -> Any:
    """Read an environment-backed default for schema generation."""
    env_value = os.environ.get(field_name.upper())
    if env_value is None:
        return fallback

    parsed_value = _parse_env_value(env_value)
    if parsed_value is None:
        return fallback

    if parser is None:
        return parsed_value
    return parser(parsed_value)


def _parse_str(value: Any) -> str:
    """Parse a string environment value."""
    return str(value)


def _parse_int(value: Any) -> int:
    """Parse an integer environment value."""
    return int(value)


def _parse_float(value: Any) -> float:
    """Parse a float environment value."""
    return float(value)


def _parse_bool(value: Any) -> bool:
    """Parse a boolean environment value."""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on"}:
            return True
        if normalized in {"0", "false", "no", "n", "off"}:
            return False
    raise ValueError(f"Invalid boolean environment value: {value!r}")


def _parse_search_api(value: Any) -> SearchAPI:
    """Parse a search API environment value."""
    if isinstance(value, SearchAPI):
        return value
    return SearchAPI(str(value))


class MCPConfig(BaseModel):
    """Configuration for Model Context Protocol (MCP) servers."""
    
    url: str | None = Field(
        default=None,
        optional=True,
    )
    """The URL of the MCP server"""
    tools: List[str] | None = Field(
        default=None,
        optional=True,
    )
    """The tools to make available to the LLM"""
    auth_required: bool | None = Field(
        default=False,
        optional=True,
    )
    """Whether the MCP server requires authentication"""


def _parse_mcp_config(value: Any) -> MCPConfig:
    """Parse an MCP config environment value."""
    if isinstance(value, MCPConfig):
        return value
    return MCPConfig.model_validate(value)


DEFAULT_MAX_STRUCTURED_OUTPUT_RETRIES = _env_default("max_structured_output_retries", 3, _parse_int)
DEFAULT_ALLOW_CLARIFICATION = _env_default("allow_clarification", False, _parse_bool)
DEFAULT_MAX_CONCURRENT_RESEARCH_UNITS = _env_default("max_concurrent_research_units", 5, _parse_int)
DEFAULT_SEARCH_API = _env_default("search_api", SearchAPI.NONE, _parse_search_api)
DEFAULT_KNOWLEDGE_BASE_URL = _env_default("knowledge_base_url", None, _parse_str)
DEFAULT_WORKSPACE_ID = _env_default("workspace_id", None, _parse_str)
DEFAULT_OPENAI_BASE_URL = _env_default("openai_base_url", None, _parse_str)
DEFAULT_FINAL_REPORT_BASE_URL = _env_default("final_report_base_url", None, _parse_str)
DEFAULT_KNOWLEDGE_BASE_QUERY_TIMEOUT_SECONDS = _env_default("knowledge_base_query_timeout_seconds", 120.0, _parse_float)
DEFAULT_KNOWLEDGE_BASE_WINDOW_TIMEOUT_SECONDS = _env_default("knowledge_base_window_timeout_seconds", 120.0, _parse_float)
DEFAULT_COMPRESSION_IMAGE_LIMIT = _env_default("compression_image_limit", 4, _parse_int)
DEFAULT_COMPRESSION_IMAGE_MAX_BYTES = _env_default("compression_image_max_bytes", 8_000_000, _parse_int)
DEFAULT_SAVE_WIKI_MARKDOWN = _env_default("save_wiki_markdown", True, _parse_bool)
DEFAULT_WIKI_OUTPUT_DIR = _env_default("wiki_output_dir", "wiki_site/docs/entries", _parse_str)
DEFAULT_WIKI_OUTPUT_FILENAME = _env_default("wiki_output_filename", None, _parse_str)
DEFAULT_MAX_RESEARCHER_ITERATIONS = _env_default("max_researcher_iterations", 6, _parse_int)
DEFAULT_MAX_REACT_TOOL_CALLS = _env_default("max_react_tool_calls", 10, _parse_int)
DEFAULT_SUMMARIZATION_MODEL = _env_default("summarization_model", "openai:gpt-4.1-mini", _parse_str)
DEFAULT_SUMMARIZATION_MODEL_MAX_TOKENS = _env_default("summarization_model_max_tokens", 8192, _parse_int)
DEFAULT_SUMMARIZATION_TIMEOUT_SECONDS = _env_default("summarization_timeout_seconds", 60.0, _parse_float)
DEFAULT_MAX_CONTENT_LENGTH = _env_default("max_content_length", 50000, _parse_int)
DEFAULT_BRIEF_MODEL = _env_default("brief_model", "openai:gpt-4.1", _parse_str)
DEFAULT_BRIEF_MODEL_MAX_TOKENS = _env_default("brief_model_max_tokens", 10000, _parse_int)
DEFAULT_BRIEF_BASE_URL = _env_default("brief_base_url", None, _parse_str)
DEFAULT_RESEARCH_MODEL = _env_default("research_model", "openai:gpt-4.1", _parse_str)
DEFAULT_RESEARCH_MODEL_MAX_TOKENS = _env_default("research_model_max_tokens", 10000, _parse_int)
DEFAULT_COMPRESSION_MODEL = _env_default("compression_model", "openai:gpt-4.1", _parse_str)
DEFAULT_COMPRESSION_MODEL_MAX_TOKENS = _env_default("compression_model_max_tokens", 8192, _parse_int)
DEFAULT_FINAL_REPORT_MODEL = _env_default("final_report_model", "openai:gpt-4.1", _parse_str)
DEFAULT_FINAL_REPORT_MODEL_MAX_TOKENS = _env_default("final_report_model_max_tokens", 10000, _parse_int)
DEFAULT_MCP_CONFIG = _env_default("mcp_config", None, _parse_mcp_config)
DEFAULT_MCP_PROMPT = _env_default("mcp_prompt", None, _parse_str)


class Configuration(BaseModel):
    """Main configuration class for the Deep Research agent."""
    
    # General Configuration
    max_structured_output_retries: int = Field(
        default=DEFAULT_MAX_STRUCTURED_OUTPUT_RETRIES,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_MAX_STRUCTURED_OUTPUT_RETRIES,
                "min": 1,
                "max": 10,
                "description": "Maximum number of retries for structured output calls from models"
            }
        }
    )
    allow_clarification: bool = Field(
        default=DEFAULT_ALLOW_CLARIFICATION,
        metadata={
            "x_oap_ui_config": {
                "type": "boolean",
                "default": DEFAULT_ALLOW_CLARIFICATION,
                "description": "Whether to allow the researcher to ask the user clarifying questions before starting research"
            }
        }
    )
    max_concurrent_research_units: int = Field(
        default=DEFAULT_MAX_CONCURRENT_RESEARCH_UNITS,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": DEFAULT_MAX_CONCURRENT_RESEARCH_UNITS,
                "min": 1,
                "max": 20,
                "step": 1,
                "description": "Maximum number of research units to run concurrently. This will allow the researcher to use multiple sub-agents to conduct research. Note: with more concurrency, you may run into rate limits."
            }
        }
    )
    # Research Configuration
    search_api: SearchAPI = Field(
        default=DEFAULT_SEARCH_API,
        metadata={
            "x_oap_ui_config": {
                "type": "select",
                "default": DEFAULT_SEARCH_API.value,
                "description": "Search API to use for research. NOTE: Make sure your Researcher Model supports the selected search API.",
                "options": [
                    {"label": "Tavily", "value": SearchAPI.TAVILY.value},
                    {"label": "OpenAI Native Web Search", "value": SearchAPI.OPENAI.value},
                    {"label": "Anthropic Native Web Search", "value": SearchAPI.ANTHROPIC.value},
                    {"label": "None", "value": SearchAPI.NONE.value}
                ]
            }
        }
    )
    knowledge_base_url: str | None = Field(
        default=DEFAULT_KNOWLEDGE_BASE_URL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Base URL shared by the workspace Query and Window APIs. Can also be set with the KNOWLEDGE_BASE_URL environment variable."
            }
        }
    )
    workspace_id: str | None = Field(
        default=DEFAULT_WORKSPACE_ID,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Default workspace ID for knowledge base retrieval tools. Can also be set with the WORKSPACE_ID environment variable."
            }
        }
    )
    openai_base_url: str | None = Field(
        default=DEFAULT_OPENAI_BASE_URL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional base URL for OpenAI-compatible model APIs. Can also be set with the OPENAI_BASE_URL environment variable."
            }
        }
    )
    final_report_api_key: str | None = Field(
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "password",
                "description": "Optional API key used only by the final wiki writer model. Can also be set with the FINAL_REPORT_API_KEY environment variable."
            }
        }
    )
    final_report_base_url: str | None = Field(
        default=DEFAULT_FINAL_REPORT_BASE_URL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional base URL used only by the final wiki writer model. For OpenAI-compatible writer models, can also be set with FINAL_REPORT_BASE_URL."
            }
        }
    )
    knowledge_base_query_timeout_seconds: float = Field(
        default=DEFAULT_KNOWLEDGE_BASE_QUERY_TIMEOUT_SECONDS,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_KNOWLEDGE_BASE_QUERY_TIMEOUT_SECONDS,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each knowledge-base Query API request"
            }
        }
    )
    knowledge_base_window_timeout_seconds: float = Field(
        default=DEFAULT_KNOWLEDGE_BASE_WINDOW_TIMEOUT_SECONDS,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_KNOWLEDGE_BASE_WINDOW_TIMEOUT_SECONDS,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each knowledge-base Window API request"
            }
        }
    )
    compression_image_limit: int = Field(
        default=DEFAULT_COMPRESSION_IMAGE_LIMIT,
        ge=0,
        le=12,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": DEFAULT_COMPRESSION_IMAGE_LIMIT,
                "min": 0,
                "max": 12,
                "step": 1,
                "description": "Maximum number of knowledge-base image/table/chart resources to pass to the compression VLM"
            }
        }
    )
    compression_image_max_bytes: int = Field(
        default=DEFAULT_COMPRESSION_IMAGE_MAX_BYTES,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_COMPRESSION_IMAGE_MAX_BYTES,
                "min": 100000,
                "max": 50000000,
                "description": "Maximum bytes per image resource passed to the compression VLM"
            }
        }
    )
    save_wiki_markdown: bool = Field(
        default=DEFAULT_SAVE_WIKI_MARKDOWN,
        metadata={
            "x_oap_ui_config": {
                "type": "boolean",
                "default": DEFAULT_SAVE_WIKI_MARKDOWN,
                "description": "Whether to save the final wiki markdown document to disk"
            }
        }
    )
    wiki_output_dir: str = Field(
        default=DEFAULT_WIKI_OUTPUT_DIR,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_WIKI_OUTPUT_DIR,
                "description": "Directory where generated wiki markdown files are saved"
            }
        }
    )
    wiki_output_filename: str | None = Field(
        default=DEFAULT_WIKI_OUTPUT_FILENAME,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional output markdown filename for a single pipeline run"
            }
        }
    )
    max_researcher_iterations: int = Field(
        default=DEFAULT_MAX_RESEARCHER_ITERATIONS,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": DEFAULT_MAX_RESEARCHER_ITERATIONS,
                "min": 1,
                "max": 10,
                "step": 1,
                "description": "Maximum number of research iterations for the Research Supervisor. This is the number of times the Research Supervisor will reflect on the research and ask follow-up questions."
            }
        }
    )
    max_react_tool_calls: int = Field(
        default=DEFAULT_MAX_REACT_TOOL_CALLS,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": DEFAULT_MAX_REACT_TOOL_CALLS,
                "min": 1,
                "max": 30,
                "step": 1,
                "description": "Maximum number of tool calling iterations to make in a single researcher step."
            }
        }
    )
    # Model Configuration
    summarization_model: str = Field(
        default=DEFAULT_SUMMARIZATION_MODEL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_SUMMARIZATION_MODEL,
                "description": "Model for summarizing research results from Tavily search results"
            }
        }
    )
    summarization_model_max_tokens: int = Field(
        default=DEFAULT_SUMMARIZATION_MODEL_MAX_TOKENS,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_SUMMARIZATION_MODEL_MAX_TOKENS,
                "description": "Maximum output tokens for summarization model"
            }
        }
    )
    summarization_timeout_seconds: float = Field(
        default=DEFAULT_SUMMARIZATION_TIMEOUT_SECONDS,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_SUMMARIZATION_TIMEOUT_SECONDS,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each webpage summarization model call"
            }
        }
    )
    max_content_length: int = Field(
        default=DEFAULT_MAX_CONTENT_LENGTH,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_MAX_CONTENT_LENGTH,
                "min": 1000,
                "max": 200000,
                "description": "Maximum character length for webpage content before summarization"
            }
        }
    )
    brief_model: str = Field(
        default=DEFAULT_BRIEF_MODEL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_BRIEF_MODEL,
                "description": "Model for transforming the user request into the initial research brief"
            }
        }
    )
    brief_model_max_tokens: int = Field(
        default=DEFAULT_BRIEF_MODEL_MAX_TOKENS,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_BRIEF_MODEL_MAX_TOKENS,
                "description": "Maximum output tokens for the initial research brief model"
            }
        }
    )
    brief_api_key: str | None = Field(
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "password",
                "description": "Optional API key used only by the initial research brief model. Can also be set with the BRIEF_API_KEY environment variable."
            }
        }
    )
    brief_base_url: str | None = Field(
        default=DEFAULT_BRIEF_BASE_URL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional base URL used only by the initial research brief model. For OpenAI-compatible brief models, can also be set with BRIEF_BASE_URL."
            }
        }
    )
    research_model: str = Field(
        default=DEFAULT_RESEARCH_MODEL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_RESEARCH_MODEL,
                "description": "Model for conducting research. NOTE: Make sure your Researcher Model supports the selected search API."
            }
        }
    )
    research_model_max_tokens: int = Field(
        default=DEFAULT_RESEARCH_MODEL_MAX_TOKENS,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_RESEARCH_MODEL_MAX_TOKENS,
                "description": "Maximum output tokens for research model"
            }
        }
    )
    compression_model: str = Field(
        default=DEFAULT_COMPRESSION_MODEL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_COMPRESSION_MODEL,
                "description": "Model for compressing research findings from sub-agents. NOTE: Make sure your Compression Model supports the selected search API."
            }
        }
    )
    compression_model_max_tokens: int = Field(
        default=DEFAULT_COMPRESSION_MODEL_MAX_TOKENS,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_COMPRESSION_MODEL_MAX_TOKENS,
                "description": "Maximum output tokens for compression model"
            }
        }
    )
    final_report_model: str = Field(
        default=DEFAULT_FINAL_REPORT_MODEL,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": DEFAULT_FINAL_REPORT_MODEL,
                "description": "Model for writing the final report from all research findings"
            }
        }
    )
    final_report_model_max_tokens: int = Field(
        default=DEFAULT_FINAL_REPORT_MODEL_MAX_TOKENS,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": DEFAULT_FINAL_REPORT_MODEL_MAX_TOKENS,
                "description": "Maximum output tokens for final report model"
            }
        }
    )
    # MCP server configuration
    mcp_config: MCPConfig | None = Field(
        default=DEFAULT_MCP_CONFIG,
        optional=True,
        metadata={
            "x_oap_ui_config": {
                "type": "mcp",
                "description": "MCP server configuration"
            }
        }
    )
    mcp_prompt: str | None = Field(
        default=DEFAULT_MCP_PROMPT,
        optional=True,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Any additional instructions to pass along to the Agent regarding the MCP tools that are available to it."
            }
        }
    )


    @classmethod
    def from_runnable_config(
        cls, config: RunnableConfig | None = None
    ) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        configurable = config.get("configurable", {}) if config else {}
        field_names = list(cls.model_fields.keys())
        values: dict[str, Any] = {
            field_name: _get_config_value(field_name, configurable)
            for field_name in field_names
        }
        return cls(**{k: v for k, v in values.items() if v is not None})

    class Config:
        """Pydantic configuration."""
        
        arbitrary_types_allowed = True


def _get_config_value(field_name: str, configurable: dict[str, Any]) -> Any:
    """Read a config field from RunnableConfig first, then environment."""
    if field_name in configurable and configurable[field_name] is not None:
        if isinstance(configurable[field_name], str) and configurable[field_name].strip() == "":
            return _env_default(field_name, None)
        return configurable[field_name]
    env_value = os.environ.get(field_name.upper())
    if env_value is not None:
        return _parse_env_value(env_value)
    return None
