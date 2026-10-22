# AIPM Skills

AI 产品经理（AI Product Manager）的 skills 合集。每个 skill 一个独立目录，遵循 `SKILL.md` + `references/` 的约定，可直接用于支持 skills 的 Agent 环境。

## Skills

| Skill | 用途 | 典型触发场景 |
|---|---|---|
| [ai-agent-prd-writer](ai-agent-prd-writer/) | AI Agent 产品 PRD 全流程撰写，支持引导模式（模糊需求逐步追问）与高效模式（信息齐备直接出稿），并带本地文件版本管理 | 写 PRD、写需求文档、功能设计、需求梳理 |
| [ai-product-teardown](ai-product-teardown/) | AI 产品六层逆向拆解：市场 → 商业 → 用户 → 技术 → 模型 → 基础，定位是引导用户自己拆的教练 | 拆解某个 AI 产品、竞品分析、架构还原、面试准备 |
| [brd](brd/) | 商业需求文档（BRD）引导式生成：先判断一个方向值不值得做，所有结论强制挂数据索引，自带 DuckDuckGo 采集脚本 | 写 BRD、商业需求文档、评估方向可行性、该不该做 |
| [mrd](mrd/) | 市场需求文档（MRD）引导式生成：从用户原声提炼市场需求，自动读取 BRD 交接区复用同一批数据，指标体系强制挂索引 | 写 MRD、市场需求文档、从用户反馈里提炼需求 |
| [product-insight-miner](product-insight-miner/) | 三平台（小红书 / X / Reddit）产品灵感挖掘：采集用户痛点 → 聚类 → 频率×强度优先级矩阵 → 生成单文件 HTML 洞察报告 | 挖掘产品灵感、找用户痛点、竞品吐槽调研、找产品机会 |
| [obsidian-knowledge-saver](obsidian-knowledge-saver/) | Obsidian 知识库管理：把对话和素材沉淀为原子笔记，自动维护索引与操作日志，支持初始化 / 沉淀 / 消化 / 健康检查四种模式 | 沉淀到知识库、整理成笔记、写入 Obsidian、知识库 lint |

## 目录结构

```
AIPM-skill/
├── README.md
└── <skill-name>/
    ├── SKILL.md          必需，含 frontmatter（name / description）
    ├── references/       可选，框架、规范、示例
    ├── templates/        可选，产出物模板
    └── scripts/          可选，辅助脚本
```

## 依赖说明

- `brd/scripts/fetch_market_data.py` 需要 `requests` 和 `beautifulsoup4`：`pip install requests beautifulsoup4`；
- 该脚本默认输出到当前目录下的 `./market_data/`，在哪个目录跑就把数据落在哪里；
- `mrd` 复用同一个脚本，在 `mrd/` 目录下用 `../brd/scripts/fetch_market_data.py` 调用；
- `product-insight-miner` 依赖 `web_search` / `web_fetch` 工具，报告输出到当前目录的 `./outputs/`；
- `obsidian-knowledge-saver` 的文件操作依赖 Desktop Commander MCP（`list_directory` / `read_file` / `write_file` / `create_directory` / `start_search`），未安装时需替换为等价的文件读写能力。

## 新增 skill

1. 根目录新建 `<skill-name>/` 目录；
2. 放入 `SKILL.md`，frontmatter 至少包含 `name` 和 `description`，description 要写清触发条件；
3. 按需补充 `references/`、`templates/`、`scripts/`；
4. 在上面的 Skills 表格里加一行。

## 提交约定

- 一个 skill 一个 commit，message 形如 `feat: add <skill-name> skill`；
- 文件统一 UTF-8 + LF 换行。
