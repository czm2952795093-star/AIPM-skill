# AIPM Skills 工具箱

一套为 AI 产品经理打造的 Skills，覆盖从灵感发现、商业判断、需求分析到项目规范的完整链路。

所有 skill 遵循 [Agent Skills](https://agentskills.io) 开放标准（`SKILL.md` + `references/` + `scripts/`），Windows 与 macOS 通用，Claude Code 与 Codex 通用。

## 为什么做这套 Skills？

市面上大多数 AI 工具要么是通用模板，要么是信息聚合。它们的问题在于：**没有针对 AI 产品经理这个岗位的专业判断力。**

比如你让通用 AI 帮你写 PRD，它会给你一份结构完整但空洞的模板，但不会告诉你"这个功能应该先定义兜底策略，因为 AI 产品的失败路径比成功路径更影响用户信任"。

**这套 Skills 的不同之处：**

- **内置 AI PM 领域知识**：每个 Skill 都内嵌了 AI 产品经理岗位的能力模型、专业框架
- **流程驱动而非问答驱动**：触发后会按照完整的专业流程主动推进，而不是等你一步步指定
- **Skill 间数据打通**：BRD → MRD → PRD → 编码，每一步的结论自动传递给下一步，不重复提问
- **实战验证**：每个 Skill 都经历了多轮真实场景的测试和迭代

## 包含哪些 Skills？

### 产品决策链（BRD → MRD → PRD → Code）

这是最核心的一条链路，覆盖从"我有一个想法"到"AI Agent 可以开始写代码"的全过程：

```
/product-insight-miner → 采集用户原声（可选，没数据时推荐先跑）
  ↓
/brd → 评估方向值不值得做 → BRD.md（含数据索引 + 交接区）
  ↓ 自动继承
/mrd → 深入分析市场需求 → MRD.md（含 P0/P1/P2 优先级 + 数据索引）
  ↓ 自动继承
/vibe-prd-writer → 生成完整项目规范 → PRD/ 文件夹（10 模块 + README 导航）
  ↓ 投喂
Claude Code / Cursor / Codex 读 PRD/README.md 开始编码
```

| Skill | 解决什么问题 | 触发方式 |
|-------|------------|---------|
| **product-insight-miner** | 没数据，想知道用户在抱怨什么 | "帮我挖掘用户痛点"、"去三个平台看看" |
| **brd** | 有想法但不确定值不值得做 | "帮我评估这个方向"、"这个能不能做" |
| **mrd** | 方向确认了，需要梳理市场需求 | "帮我写 MRD"、"从用户反馈里提炼需求" |
| **vibe-prd-writer** | 需求清楚了，要出一份 AI Agent 能执行的项目规范 | "帮我写个 PRD"、"我想做一个 XX" |
| **ai-agent-prd-writer** | 工作场景的正式 PRD（给开发团队看） | "帮我写正式的需求文档" |

#### BRD / MRD 的数据驱动特性

BRD 和 MRD 都**严格要求数据支撑**：

- **有数据就用数据**：用户粘贴原声 / 上传文件 / product-insight-miner 的产出
- **没数据就跑爬虫**：内置 DuckDuckGo 爬虫脚本（`brd/scripts/fetch_market_data.py`，Python 跨平台），自动采集并按来源打索引前缀（X=Twitter, R=Reddit, Z=知乎, H=小红书...）
- **所有结论挂索引**：`核心痛点是信息过载 [X3, R1, W5]`，每个索引可回溯到原始数据
- **禁止捏造**：没有数据支撑的数字/比例/增长率，一律不写

#### vibe-prd-writer 的特点

- 输出 `PRD/` 文件夹（10 模块独立文件 + README 导航），AI Agent 按需加载，不一次性塞爆上下文
- 自动继承 BRD.md / MRD.md / DESIGN.md 的数据
- Phase 3 会扫描已安装的前端设计 skill（design-consultation / web-design-pro），避免重复造轮子
- 三层自检：文件结构完整性 / 各模块内容质量 / 跨文件一致性

### 能力建设

| Skill | 解决什么问题 | 典型使用场景 |
|-------|------------|------------|
| **ai-product-teardown** | 面试前拆解目标公司产品、入职后理解竞品 | "帮我拆解一下 Cursor" |
| **ziven-article-cowriter** | 写干货长文、内容共创 | "帮我写一篇关于 AI Agent 的文章" |

### 知识沉淀

| Skill | 解决什么问题 | 典型使用场景 |
|-------|------------|------------|
| **obsidian-knowledge-saver** | 聊完就忘了、知识散落各处 | "帮我沉淀到知识库"、"lint 一下知识库" |

存的是知识点不是对话记录，同一知识点只有一条笔记（更新而非新增），整理的活交给 LLM。支持沉淀 / 消化 / 健康检查 / 初始化四种模式。理念来自 Zettelkasten + [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

## 快速开始

### 第一步：装好 Agent

- **Claude Code**：`npm install -g @anthropic-ai/claude-code`
- **Codex CLI**：`npm install -g @openai/codex`

### 第二步：把 skill 放进 skills 目录

两个工具读的是同一套 `SKILL.md`，只是目录不同：

| Agent | macOS / Linux | Windows |
|---|---|---|
| Claude Code | `~/.claude/skills/<skill-name>/` | `C:\Users\<你>\.claude\skills\<skill-name>\` |
| Codex | `~/.codex/skills/<skill-name>/` | `C:\Users\<你>\.codex\skills\<skill-name>\` |

**macOS / Linux：**

```bash
mkdir -p ~/.claude/skills ~/.codex/skills
cp -R brd ~/.claude/skills/
cp -R brd ~/.codex/skills/
```

**Windows（PowerShell）：**

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"  | Out-Null
Copy-Item -Recurse brd "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse brd "$env:USERPROFILE\.codex\skills\"
```

装完重启 Agent 或开新会话生效。

> `obsidian-knowledge-saver` 和 `ziven-article-cowriter` 优先用 **Desktop Commander MCP** 做文件读写；没有该 MCP 时自动退回 Agent 自带的文件工具，不影响使用。

### 第三步：直接用自然语言触发

Claude Code 里可以直接 `/skill-name` 调用；Codex 里用 `$skill-name` 或直接描述需求。正常说法就行：

```
"这个方向值不值得做"          → BRD
"帮我梳理市场需求"            → MRD
"帮我写个 PRD"               → vibe-prd-writer
"帮我挖掘用户痛点"            → product-insight-miner
"帮我拆解一下 Kimi"           → ai-product-teardown
"沉淀到知识库"                → obsidian-knowledge-saver
"帮我写一篇关于 RAG 的长文"    → ziven-article-cowriter
```

## 推荐使用路径

### 路径 A：从想法到产品（Vibe Coding）

```
1. 挖需求 → product-insight-miner（从小红书/X/Reddit 挖掘用户痛点）
2. 判方向 → brd（评估值不值得做，跑爬虫补数据）
3. 理需求 → mrd（梳理 P0/P1/P2 需求优先级）
4. 出规范 → vibe-prd-writer（生成 PRD/ 文件夹，直接喂给 AI Agent）
5. 写代码 → 把 PRD/ 丢进 Claude Code / Codex / Cursor 开干
```

### 路径 B：单点能力

```
1. 看产品 → ai-product-teardown（拆解竞品、还原架构）
2. 写内容 → ziven-article-cowriter（把想法整理成可发布的长文）
3. 攒资产 → obsidian-knowledge-saver（知识卡片持续积累）
```

两条路径可以并行，沉淀下来的知识会在下一次产品判断里复用。

## 环境要求

- **Python 3**：`brd` / `mrd` 的采集脚本、`ai-product-teardown` 的初始化脚本需要。Windows 用 `python`，macOS / Linux 用 `python3`
- **网络**：`product-insight-miner` 走 `web_search` / `web_fetch`；`brd` / `mrd` 走 DuckDuckGo 网页接口
- **可选 MCP**：Desktop Commander（Obsidian 落盘更稳）、Excalidraw（配图）

## 前置依赖

- `brd` / `mrd` 爬虫：`pip install requests beautifulsoup4`
- 其他 skill 无额外 Python 依赖

## 关于

这些 Skills 是在真实的 AI 产品工作、内容创作和求职准备中，把反复遇到的痛点提炼成的可复用工具。它们不是完美的，但每一个都解决了真实遇到的问题。

欢迎 Fork 和改造成适合你自己的版本。
