"""Configuration management for the Open Deep Research system."""

import os
import json
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

class Configuration(BaseModel):
    """Main configuration class for the Deep Research agent."""
    
    # General Configuration
    max_structured_output_retries: int = Field(
        default=3,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 3,
                "min": 1,
                "max": 10,
                "description": "Maximum number of retries for structured output calls from models"
            }
        }
    )
    allow_clarification: bool = Field(
        default=False,
        metadata={
            "x_oap_ui_config": {
                "type": "boolean",
                "default": False,
                "description": "Whether to allow the researcher to ask the user clarifying questions before starting research"
            }
        }
    )
    max_concurrent_research_units: int = Field(
        default=5,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": 5,
                "min": 1,
                "max": 20,
                "step": 1,
                "description": "Maximum number of research units to run concurrently. This will allow the researcher to use multiple sub-agents to conduct research. Note: with more concurrency, you may run into rate limits."
            }
        }
    )
    # Research Configuration
    search_api: SearchAPI = Field(
        default=SearchAPI.NONE,
        metadata={
            "x_oap_ui_config": {
                "type": "select",
                "default": "tavily",
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
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Base URL shared by the workspace Query and Window APIs. Can also be set with the KNOWLEDGE_BASE_URL environment variable."
            }
        }
    )
    workspace_id: str | None = Field(
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Default workspace ID for knowledge base retrieval tools. Can also be set with the WORKSPACE_ID environment variable."
            }
        }
    )
    openai_base_url: str | None = Field(
        default=None,
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
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional base URL used only by the final wiki writer model. For OpenAI-compatible writer models, can also be set with FINAL_REPORT_BASE_URL."
            }
        }
    )
    knowledge_base_query_timeout_seconds: float = Field(
        default=600.0,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 120,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each knowledge-base Query API request"
            }
        }
    )
    knowledge_base_window_timeout_seconds: float = Field(
        default=600.0,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 120,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each knowledge-base Window API request"
            }
        }
    )
    compression_image_limit: int = Field(
        default=4,
        ge=0,
        le=12,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": 4,
                "min": 0,
                "max": 12,
                "step": 1,
                "description": "Maximum number of knowledge-base image/table/chart resources to pass to the compression VLM"
            }
        }
    )
    compression_image_max_bytes: int = Field(
        default=8_000_000,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 8000000,
                "min": 100000,
                "max": 50000000,
                "description": "Maximum bytes per image resource passed to the compression VLM"
            }
        }
    )
    save_wiki_markdown: bool = Field(
        default=True,
        metadata={
            "x_oap_ui_config": {
                "type": "boolean",
                "default": True,
                "description": "Whether to save the final wiki markdown document to disk"
            }
        }
    )
    wiki_output_dir: str = Field(
        default="wiki_outputs",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "wiki_outputs",
                "description": "Directory where generated wiki markdown files are saved"
            }
        }
    )
    wiki_output_filename: str | None = Field(
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional output markdown filename for a single pipeline run"
            }
        }
    )
    max_researcher_iterations: int = Field(
        default=6,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": 6,
                "min": 1,
                "max": 10,
                "step": 1,
                "description": "Maximum number of research iterations for the Research Supervisor. This is the number of times the Research Supervisor will reflect on the research and ask follow-up questions."
            }
        }
    )
    max_react_tool_calls: int = Field(
        default=10,
        metadata={
            "x_oap_ui_config": {
                "type": "slider",
                "default": 10,
                "min": 1,
                "max": 30,
                "step": 1,
                "description": "Maximum number of tool calling iterations to make in a single researcher step."
            }
        }
    )
    # Model Configuration
    summarization_model: str = Field(
        default="openai:gpt-4.1-mini",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "openai:gpt-4.1-mini",
                "description": "Model for summarizing research results from Tavily search results"
            }
        }
    )
    summarization_model_max_tokens: int = Field(
        default=8192,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 8192,
                "description": "Maximum output tokens for summarization model"
            }
        }
    )
    summarization_timeout_seconds: float = Field(
        default=600.0,
        gt=0,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 60,
                "min": 1,
                "max": 3600,
                "description": "Timeout in seconds for each webpage summarization model call"
            }
        }
    )
    max_content_length: int = Field(
        default=50000,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 50000,
                "min": 1000,
                "max": 200000,
                "description": "Maximum character length for webpage content before summarization"
            }
        }
    )
    brief_model: str = Field(
        default="openai:gpt-4.1",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "openai:gpt-4.1",
                "description": "Model for transforming the user request into the initial research brief"
            }
        }
    )
    brief_model_max_tokens: int = Field(
        default=10000,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 10000,
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
        default=None,
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "description": "Optional base URL used only by the initial research brief model. For OpenAI-compatible brief models, can also be set with BRIEF_BASE_URL."
            }
        }
    )
    research_model: str = Field(
        default="openai:gpt-4.1",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "openai:gpt-4.1",
                "description": "Model for conducting research. NOTE: Make sure your Researcher Model supports the selected search API."
            }
        }
    )
    research_model_max_tokens: int = Field(
        default=10000,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 10000,
                "description": "Maximum output tokens for research model"
            }
        }
    )
    compression_model: str = Field(
        default="openai:gpt-4.1",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "openai:gpt-4.1",
                "description": "Model for compressing research findings from sub-agents. NOTE: Make sure your Compression Model supports the selected search API."
            }
        }
    )
    compression_model_max_tokens: int = Field(
        default=8192,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 8192,
                "description": "Maximum output tokens for compression model"
            }
        }
    )
    final_report_model: str = Field(
        default="openai:gpt-4.1",
        metadata={
            "x_oap_ui_config": {
                "type": "text",
                "default": "openai:gpt-4.1",
                "description": "Model for writing the final report from all research findings"
            }
        }
    )
    final_report_model_max_tokens: int = Field(
        default=10000,
        metadata={
            "x_oap_ui_config": {
                "type": "number",
                "default": 10000,
                "description": "Maximum output tokens for final report model"
            }
        }
    )
    # MCP server configuration
    mcp_config: MCPConfig | None = Field(
        default=None,
        optional=True,
        metadata={
            "x_oap_ui_config": {
                "type": "mcp",
                "description": "MCP server configuration"
            }
        }
    )
    mcp_prompt: str | None = Field(
        default=None,
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
        return configurable[field_name]
    env_value = os.environ.get(field_name.upper())
    if env_value is not None:
        return _parse_env_value(env_value)
    return None


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
