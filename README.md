# 压铸技术 Wiki 生成器

本仓库基于 Open Deep Research / LangGraph 实现，面向压铸、铸造、材料与工艺知识库的自动词条生成和展示。系统会围绕目标词条进行检索、并行研究、证据压缩、引用校验和最终 Markdown 写作，生成的词条默认保存到 `wiki_site/docs/entries`，再由 MkDocs 构建为可搜索的静态 Wiki。

## 功能概览

- **深度研究工作流**：`Deep Researcher` LangGraph 会依次完成需求澄清、研究简报、并行研究、结构化证据压缩和 Wiki 写作。
- **知识库检索工具**：支持通过 KBA Query / Window / Resource API 检索文本、图片、表格和图表证据。
- **批量词条生成**：`src/cli.py` 支持单词条、`wiki_entries.txt` 和 JSONL 批量输入，可本地进程运行，也可提交到 LangGraph API。
- **Markdown 持久化**：生成文件会自动清洗文件名、避免覆盖、规范表格/公式/图片布局，并写入版本、生成时间和置信度元数据。
- **Wiki 站点**：MkDocs 站点内置中文搜索、词条索引、条目信息面板和智能问答入口。
- **运维脚本**：提供 Wiki 站点/检索服务启动、词条统计、失败线程重试等辅助脚本。

## 目录结构

```text
.
├── langgraph.json                 # LangGraph 图配置，入口为 Deep Researcher
├── mkdocs.yml                     # Wiki 静态站点配置
├── wiki_entries.txt               # 批量词条输入示例，每行一个词条
├── src/
│   ├── cli.py                     # 单条/批量生成 CLI
│   └── open_deep_research/
│       ├── deep_researcher.py     # 主 LangGraph 工作流
│       ├── configuration.py       # 环境变量和运行时配置
│       ├── utils.py               # 搜索、KBA、模型配置等工具
│       ├── research.py            # 结构化证据、引用和置信度逻辑
│       ├── persistence.py         # Markdown 保存和规范化
│       └── retrieval_api.py       # Wiki 智能问答使用的检索 API
├── scripts/
│   ├── start_wiki_services.sh     # 同时启动 MkDocs 和检索 API
│   ├── wiki_stats.py              # 统计已生成词条
│   ├── retry_failed_threads.py    # 重试/导出 LangGraph 线程
│   └── mkdocs_wiki_entries.py     # MkDocs 构建 hook
├── tests/                         # 单元测试和评测脚本
└── wiki_site/docs/                # MkDocs 文档根目录
    ├── chat.md                    # 智能问答页面
    ├── index.md                   # 首页
    └── entries/                   # 生成的词条 Markdown
```

## 环境准备

需要 Python 3.10+，推荐 Python 3.11。项目使用 `uv.lock` 固定依赖，优先使用 `uv` 安装。

```bash
uv venv

# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

uv sync
```

如果不用 `uv`，也可以安装为可编辑包：

```bash
python -m venv .venv
pip install -e .
```

开发工具可额外安装：

```bash
pip install -e ".[dev]"
```

## 配置 `.env`

先复制模板：

```bash
cp .env.example .env
```

Windows PowerShell：

```powershell
Copy-Item .env.example .env
```

常用配置如下：

| 变量 | 用途 |
| --- | --- |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` | OpenAI 或 OpenAI 兼容模型服务配置 |
| `ANTHROPIC_API_KEY` / `GOOGLE_API_KEY` / `TAVILY_API_KEY` | 对应模型或搜索服务密钥 |
| `SEARCH_API` | 外部搜索来源，可选 `none`、`tavily`、`openai`、`anthropic` |
| `KNOWLEDGE_BASE_URL` | KBA 服务根地址，例如 `http://127.0.0.1:8000` |
| `WORKSPACE_ID` | 默认知识库 workspace ID |
| `BRIEF_MODEL` / `RESEARCH_MODEL` / `COMPRESSION_MODEL` / `FINAL_REPORT_MODEL` | 各阶段模型 |
| `BRIEF_API_KEY` / `BRIEF_BASE_URL` | 初始研究简报阶段的专用模型配置 |
| `FINAL_REPORT_API_KEY` / `FINAL_REPORT_BASE_URL` | 最终 Wiki 写作阶段的专用模型配置 |
| `MAX_CONCURRENT_RESEARCH_UNITS` | 单次图运行内部并行研究数量 |
| `SAVE_WIKI_MARKDOWN` | 是否把最终 Wiki 保存为 Markdown，默认 `true` |
| `WIKI_OUTPUT_DIR` | 词条输出目录，默认 `wiki_site/docs/entries` |
| `MCP_CONFIG` / `MCP_PROMPT` | 可选 MCP 工具配置 |

最小可运行配置通常需要模型密钥。如果要使用知识库检索，还必须设置 `KNOWLEDGE_BASE_URL` 和 `WORKSPACE_ID`。

## 启动 LangGraph API

本地开发建议先启动 LangGraph API，再用 Studio UI 调试图运行。

```bash
mkdir -p logs
langgraph dev --port 2024 --no-reload --allow-blocking | tee logs/langgraph.log
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force logs | Out-Null
langgraph dev --port 2024 --no-reload --allow-blocking | Tee-Object logs/langgraph.log
```

启动后可访问：

- API: `http://127.0.0.1:2024`
- Studio UI: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`
- API Docs: `http://127.0.0.1:2024/docs`

生产部署可继续使用 `langgraph up` 或 `langgraph deploy`，具体取决于部署环境和凭据配置。

## 生成 Wiki 词条

### 单个词条

直接在当前进程中运行图：

```bash
python src/cli.py --topic "压铸速度" --id "压铸速度"
```

通过已经启动的 LangGraph API 运行：

```bash
python src/cli.py --topic "压铸速度" --id "压铸速度" --api-url http://127.0.0.1:2024
```

### 批量生成

`wiki_entries.txt` 每行格式为：

```text
词条名称|可选描述提示
H13钢|热作模具钢，描述可能不完整
压铸速度
```

批量提交：

```bash
python src/cli.py wiki_entries.txt --input-format wiki-entries --concurrency 2
```

通过 LangGraph API 批量提交：

```bash
python src/cli.py wiki_entries.txt \
  --api-url http://127.0.0.1:2024 \
  --assistant-id "Deep Researcher" \
  --concurrency 2
```

常用参数：

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `input` | 无 | 输入文件，支持 `wiki_entries.txt` 或 JSONL |
| `--topic` | 无 | 单词条模式，不需要输入文件 |
| `--id` | 无 | 单词条输出文件名 stem |
| `--output-dir` | `wiki_site/docs/entries` | Markdown 输出目录 |
| `--results` | `wiki_outputs/results.jsonl` | 批量运行结果索引 |
| `--limit` | 无 | 只处理前 N 条 |
| `--concurrency` | `2` | 并发提交的独立图运行数量 |
| `--api-url` | 无 | LangGraph API 地址；省略时在本进程运行 |
| `--config-file` | 无 | JSON 配置文件，会合并到 LangGraph `configurable` |
| `--config-json` | `{}` | 命令行内联 JSON 配置 |

JSONL 输入每行是一个 JSON 对象，常用字段包括 `id`、`topic`、`name`、`wiki_entry_name`、`description`、`output_filename`、`thread_id` 和 `config`。

示例：

```jsonl
{"id":"H13钢","wiki_entry_name":"H13钢","description":"热作模具钢","config":{"search_api":"none"}}
{"id":"压铸速度","topic":"压铸速度"}
```

生成成功后，Markdown 默认写入 `wiki_site/docs/entries`。如果同名文件已存在，会自动追加 `-1`、`-2` 等后缀，避免覆盖已有词条。

## 查看 Wiki 站点

生成好的词条由 MkDocs 展示。只启动静态 Wiki：

```bash
python -m mkdocs serve -f mkdocs.yml --dev-addr 0.0.0.0:8765
```

然后打开：

```text
http://<server-ip>:8765
```

`mkdocs.yml` 使用 `scripts/mkdocs_wiki_entries.py` 作为构建 hook，会自动生成词条索引、增强中文搜索、规范表格 HTML，并在词条页顶部展示版本、生成时间和置信度信息。

## 智能问答和检索 API

Wiki 的智能问答页面在 `wiki_site/docs/chat.md`，当前只嵌入 Dify chatbot iframe；回答内容、Markdown、公式和引用展示均交由 Dify 前端渲染。Dify 工作流还可以配合本仓库的检索 API，将用户问题转换为结构化检索结果。

单独启动检索 API：

```bash
python -m uvicorn open_deep_research.retrieval_api:app --host 0.0.0.0 --port 8010
```

健康检查：

```text
GET http://<server-ip>:8010/api/v1/retrieval/health
```

生成检索 findings：

```bash
curl -X POST http://127.0.0.1:8010/api/v1/retrieval/findings \
  -H "Content-Type: application/json" \
  -d '{
    "queries": ["H13钢在压铸模中的热疲劳性能"],
    "workspace_id": "your-workspace-id",
    "summarize_findings": true,
    "text_topk": 10,
    "image_topk": 3,
    "table_topk": 3,
    "chart_topk": 3
  }'
```

Linux 环境下可以同时启动 MkDocs 和检索 API：

```bash
chmod +x scripts/start_wiki_services.sh
./scripts/start_wiki_services.sh
```

默认服务和日志：

- MkDocs: `http://0.0.0.0:8765`
- Retrieval API: `http://0.0.0.0:8010`
- MkDocs 日志: `logs/mkdocs.log`
- Retrieval API 日志: `logs/retrieval_api.log`
- PID 文件: `logs/wiki_services.pid`

可通过环境变量调整启动脚本：

```bash
MKDOCS_HOST=0.0.0.0 \
MKDOCS_PORT=8765 \
API_HOST=0.0.0.0 \
API_PORT=8010 \
LOG_DIR=./logs \
./scripts/start_wiki_services.sh
```

## 依赖服务

- **模型服务**：至少配置一个可用的聊天模型。OpenAI 兼容服务可通过 `OPENAI_BASE_URL`、`BRIEF_BASE_URL`、`FINAL_REPORT_BASE_URL` 指向不同 endpoint。
- **KBA 服务**：词条生成和检索 API 的知识库工具依赖 Query、Window 和 Resource API，主要使用：
  - `POST /api/v1/workspaces/{workspace_id}/query`
  - `GET /api/v1/workspaces/{workspace_id}/document-elements/{uuid}/window?k=4`
  - `GET /api/v1/workspaces/{workspace_id}/text-nodes/{uuid}/window?k=4`
  - `GET /api/v1/workspaces/{workspace_id}/document-elements/{uuid}/resource`
- **Dify 服务**：Wiki 智能问答页面的前端嵌入地址在 `wiki_site/docs/chat.md` 的 `data-dify-src` 中配置。

## 维护脚本

统计已生成词条：

```bash
python scripts/wiki_stats.py wiki_site/docs/entries
```

输出 JSON 统计：

```bash
python scripts/wiki_stats.py wiki_site/docs/entries --format json
```

查看某段时间后的失败 LangGraph 线程：

```bash
python scripts/retry_failed_threads.py \
  --deployment-url http://localhost:8123 \
  --after-local 2026-06-18T00:00:00
```

实际重试失败线程并导出结果：

```bash
python scripts/retry_failed_threads.py \
  --deployment-url http://localhost:8123 \
  --after-local 2026-06-18T00:00:00 \
  --retry \
  --concurrency 5
```

只导出已有 `final_report`，不重新运行：

```bash
python scripts/retry_failed_threads.py \
  --deployment-url http://localhost:8123 \
  --status idle \
  --save-existing
```

## 测试和代码检查

运行单元测试：

```bash
pytest
```

运行重点测试：

```bash
pytest tests/test_wiki_persistence.py tests/test_knowledge_base_search.py
```

代码检查：

```bash
ruff check
mypy
```

评测脚本入口：

```bash
python tests/run_evaluate.py
```

## 常见问题

**生成时报 `Knowledge base tools are not configured`**

设置 `KNOWLEDGE_BASE_URL`，并确保 `WORKSPACE_ID` 已配置或在工具调用中传入。

**词条没有写入磁盘**

确认 `SAVE_WIKI_MARKDOWN=true`，并检查 `WIKI_OUTPUT_DIR` 是否指向可写目录。CLI 默认写入 `wiki_site/docs/entries`。

**同名词条出现 `-1`、`-2` 后缀**

这是预期行为，保存逻辑不会覆盖已有文件。如需替换旧词条，请先手动处理旧文件。

**MkDocs 页面表格或公式显示异常**

生成保存时会做一次 Markdown 规范化，MkDocs 构建 hook 也会补充处理表格。如果是历史文件，可以重新保存或重新生成对应词条。

**检索 API 返回 500**

优先检查 KBA 服务可达性、`WORKSPACE_ID` 是否正确、`KNOWLEDGE_BASE_URL` 是否是完整 HTTP(S) 地址，以及模型压缩阶段是否有可用 API key。
