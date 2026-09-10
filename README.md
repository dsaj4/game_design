# 游戏构思系统

本仓库管理互相独立的游戏工作区，共享流程、模板、知识 Wiki 和规则库。

## 当前工作区

- **[game-002：《言咒》](workspaces/game-002/README.md)**：默认独立工作区，Core Concept v0.5 / Stable Design Baseline。完整库存战前构句、循环法术与法杖配置、自动战斗及整体战后收益已形成核心；39份合格素材，证据Hypothesis。当前入口为[人工待决清单](workspaces/game-002/docs/design-decisions-needed.md)和[文档验收](workspaces/game-002/docs/design-alignment-audit.md)。
- **[上一款游戏归档](archive/2026-09-05-core-card-project/README.md)**：Parked / Archived，2026-09-05 暂停。

[玩法探索区](exploration/README.md)已建立最小骨架：[game-002 优化](exploration/game-002-optimization/README.md)已激活核心设计背景包 `baseline-2026-09-09-001`，[独立肉鸽探索](exploration/new-roguelike/README.md)从空白背景开始。[项目注册表](exploration/registry/project-registry.md)明确两者权限；尚未运行模拟或起草探索 GDD。架构已确认，见[玩法探索区框架](docs/architecture/game-exploration-framework.md)。

新游戏与上一款游戏无关，不是续作、改版或技术迁移。旧设定、素材资格、决策、测试、代码和排期不会自动继承。

## 快速开始

直接说一个想法、参考产品或验证问题。新输入进入 game-002 的 idea-inbox，经 grill-with-docs 资格确认后，才进入正式素材、GDD、提案和评估。

| 位置 | 职责 |
| --- | --- |
| workspaces/game-002/ | 新游戏独立的设计、研究、词汇、决策与开发索引 |
| exploration/ | 已建的优化/独立探索骨架、注册表与背景包生成规则；共享工具仍按阶段接入 |
| game-design-workflow/templates/ | 共享设计模板，仅使用索引列出的通用模板 |
| research/ | 共享理论、Wiki、研究模板与分析方法 |
| docs/game-design-agent-standards/ | 共享规则，保留 Inherited / Proposed 边界 |
| archive/ | 暂停项目、旧版本与知识清理前快照 |
| combat-lab/、semantic-card-engine/ | 上一款游戏的冻结实验，非新项目实现 |
| media-analysis-lab/ | 独立分析方法实验 |

## 入口

- [Agent 操作手册](AGENTS.md)
- [新手说明](docs/architecture-for-beginners.md)
- [工作区登记](docs/workspace-map.md)
- [总控中心](docs/control-center.md)
- [共享 Wiki、模板与规则](docs/shared-knowledge.md)
- [开发索引路由](docs/code-development-index.md)
- [GitHub 协作规范](docs/github-collaboration.md)
- [归档与隔离决定](docs/workspace-decisions.md)
