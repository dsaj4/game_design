# 游戏构思系统

本仓库管理互相独立的游戏工作区，共享流程、模板、知识 Wiki 和规则库。

## 当前工作区

- **[game-002：《言咒》](workspaces/game-002/README.md)**：默认独立工作区，Core Concept v0.6 / Stable Design Baseline。完整库存战前构句、循环法术与法杖配置、自动战斗及整体战后收益已形成核心；51份合格素材，证据Hypothesis。SW01对象范围、SW02实例/条件引用与SW02-A单次名单已确认，执行框架按G002-CORE-011收束为简单对象变化、法术生成物与对象掉卡；G002-CORE-012已引入四类特征与多类型，完成首批词名归类，后续按[法术类型入口](workspaces/game-002/docs/spell-type-index.md)讨论；上一批具体词效与参数先搁置；[四层数值框架](workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)已建立，涵盖法术、成长、整局和体验验收；[全局规则审查](workspaces/game-002/docs/global-rules-audit-2026-09-11.md)已完成，GR01–GR12处理方式按G002-CORE-015全部采纳，当前先补[修饰词与镶嵌系统](workspaces/game-002/docs/modifier-and-inlay-design.md)，再设计流派成套物品，测试积累后合批；超时疲劳方向已采纳，执行与数值候选。入口为[设计决定与后续工作](workspaces/game-002/docs/design-decisions-needed.md)和[本次文档验收](workspaces/game-002/docs/semantic-world-rules-adoption.md)。
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
