# 工作区地图

最后更新：2026-08-24

这份文档回答一个实际问题：当我们有新内容时，具体应该写到哪里。

## 根目录地图

```text
E:/Project/game
├── game-design-workflow/   正式游戏构思主流程
├── research/               理论、竞品、假设与原型观察
├── docs/                   协作说明、导航、总控与代码开发进度索引
├── media-analysis-lab/     隔离的游戏拆解实验区
├── assets/                 本地参考素材
└── archive/                历史快照
```

## 目录职责

### `game-design-workflow/`

这里管理“是否进入正式设计主线”。

常见入口：

- 突然想到一个机制、卡牌效果、规则变化：
  先写入 `idea-inbox/`，通过 `grill-with-docs` 后再晋级 `idea-materials/`
- 想写 GDD、需求文档或系统规格：
  使用统一 GDD 模板，写入 `gdd/`，并先审查 `idea-materials/` 与相关 `idea-inbox/`
- 想认真讨论一个机制值不值得做：
  只有已有合格素材时写入 `idea-proposals/`；否则先完成资格确认
- 想给某个提案下判断：
  写入 `evaluations/`
- 想改正式设定：
  先写 `draft-changes/`，确认后再改 `core-concept.md`

### `research/`

这里管理“外部知识如何转化为设计判断”。

常见入口：

- 读到文章、书、理论：
  `01-theory-library/` 或 `02-theory-digests/`
- 提到一个竞品或参考游戏：
  `03-product-case-studies/`
- 想比较多个案例：
  `04-cross-game-comparisons/`
- 已形成可验证判断：
  `05-design-hypotheses/`
- 做了纸面推演、规则测试、试玩观察：
  `06-prototype-insights/`

### `docs/`

这里管理“如何协作、如何导航、如何总控”。

适合放：

- 协作规范
- 项目导航
- 新手说明
- 总控状态板
- 工作区结构说明
- 代码仓库入口、开发里程碑、实现状态与 GDD 偏差索引

不适合放：

- 新玩法提案
- 竞品分析正文
- 原型测试记录
- 详细代码架构、构建命令和 Bug 正文（应留在对应代码仓库）

### `media-analysis-lab/`

这里不是当前游戏主线目录，而是“分析工作流实验区”。

适合放：

- 游戏视频或图文拆解流程实验
- 素材包协议
- 质量检查
- 分析工具与运行产物

不适合放：

- 已确认进入主线的核心设计结论
- 未经转化就想直接影响 `core-concept.md` 的内容

### `assets/`

这里放本地参考素材和写法样例，不直接代表项目结论。

### `archive/`

这里保留历史快照。需要追溯上下文时可以看，但不要把它当当前工作目录。

## 一句话分流规则

| 你手上的内容 | 应该写入 |
| --- | --- |
| 一个零散点子 | `game-design-workflow/idea-inbox/`（Raw Idea / Unqualified） |
| 一个通过资格确认的想法素材 | `game-design-workflow/idea-materials/` |
| 一份 GDD/玩法系统规格文档 | `game-design-workflow/gdd/` |
| 一项代码实现、开发进度或技术阻塞 | `docs/code-development-index.md`；细节进入对应代码仓库 |
| 一个成形玩法假设 | `game-design-workflow/idea-proposals/` |
| 一个是否值得做的判断 | `game-design-workflow/evaluations/` |
| 一个准备写进正式设定的文本 | `game-design-workflow/draft-changes/` |
| 一篇理论或资料入口 | `research/01-theory-library/` |
| 一篇自己的理论摘要 | `research/02-theory-digests/` |
| 一款游戏的拆解 | `research/03-product-case-studies/` |
| 多款游戏的比较 | `research/04-cross-game-comparisons/` |
| 一个可验证设计判断 | `research/05-design-hypotheses/` |
| 一次测试后的观察 | `research/06-prototype-insights/` |
| 协作文档或导航文档 | `docs/` |
| 游戏拆解流程实验 | `media-analysis-lab/` |

## 当前推荐阅读顺序

### 想快速理解项目

1. `README.md`
2. `docs/control-center.md`
3. `game-design-workflow/core-concept.md`
4. `game-design-workflow/decision-log.md`
5. `research/00-index-and-roadmap/current-questions.md`

### 想作为总控 agent 开始工作

1. `AGENTS.md`
2. `docs/github-collaboration.md`
3. `docs/control-center.md`
4. `docs/workspace-map.md`
5. 按任务进入对应工作流目录

## 何时需要新建目录

只有在同时满足以下条件时，才考虑新建一级或二级目录：

1. 现有目录确实无法容纳该类内容。
2. 这类内容会持续出现，而不是一次性文件。
3. 新目录能用一句话说清职责。
4. 新目录创建后会立刻配套 `README.md`。

如果只是新增一种文档类型但仍属于现有流程，优先补模板或补说明，不要先扩目录。
