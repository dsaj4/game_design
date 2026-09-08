# 工作区地图

最后更新：2026-09-07

| Project ID | 入口 | 状态 | 默认 |
| --- | --- | --- | --- |
| game-002 | [新游戏](../workspaces/game-002/README.md) | Active / Numerical Design & Archetype Definition | 是 |
| core-card-project | [上一款游戏](../archive/2026-09-05-core-card-project/README.md) | Parked / Archived | 否 |

新游戏与上一款游戏无关，不继承设定、素材资格、决策、测试、代码或排期。

## 路径规则

先确定工作区根 W。默认 W 为 workspaces/game-002/。
共享流程中的项目路径相对 W；共享模板、Wiki、规则库路径相对仓库根。
Markdown 链接始终按所在文件解析，不隐式重定向。

| 内容 | 位置 |
| --- | --- |
| inbox、素材、GDD、提案、评估、拟修改、核心构思 | W/game-design-workflow/ |
| 项目问题、来源选择、摘要、案例、比较、假设、观察、复盘 | W/research/ |
| 项目玩法词汇 | W/CONTEXT.md |
| 项目总控与代码进度 | W/docs/ |
| 通用设计模板 | game-design-workflow/templates/ |
| 通用研究模板 | research/templates/ |
| 共享知识与规范 | [shared-knowledge.md](shared-knowledge.md) |
| 上一款游戏设计和研究 | archive/2026-09-05-core-card-project/ |
| 上一款游戏实验代码 | combat-lab/、semantic-card-engine/，冻结原位 |
| 分析方法实验 | media-analysis-lab/ |

新建项目只复用结构与方法，项目内容库、决策和排期从空白开始。

## 玩法探索区（Proposed / 尚未建立）

玩法探索区的架构设计见 [玩法探索区项目框架](architecture/game-exploration-framework.md) 和 [ADR-0002](adr/0002-game-exploration-workspaces.md)。该区域尚未建立，不是当前有效的工作区路径。

规划中的两个独立 Project ID：

| Project ID | 用途 | 背景边界 |
| --- | --- | --- |
| `game-002-optimization` | 基于 game-002 context pack 探索优化 | 只能通过 Draft Change 请求回写 game-002 |
| `new-roguelike` | 自由探索肉鸽设计 | 从空白起点开始，不继承 game-002 |

外部媒体分析、评判框架、数值模拟/原型契约和 GDD 标准规划放在探索区 `shared/`。现有 `media-analysis-lab/`、`combat-lab/`、`semantic-card-engine/` 暂保持原位，通过引用或适配器逐步接入。
