# 游戏构思系统

本仓库管理互相独立的游戏工作区，共享流程、模板、知识 Wiki 和规则库。

## 当前工作区

- **[game-002：新游戏构思](workspaces/game-002/README.md)**：默认工作区，Active / Idea Qualification。暂定名《言咒》的初稿已分拆出 30 份合格素材：时间机制、时间补牌与多张预览、固定词类、新词直接入组、战场状态跨行动保留、普通战斗胜负与本局结束、普通胜利后的生命保留、战斗间休整的恢复与构筑取舍、局内分叉路线、预设起始卡组与新局重置、普通战斗词卡奖励、伤害与护甲及打断关系、单份状态计时与到期、同种状态重施与叠加、状态读值与同刻内部顺序、普通敌人击败后的对象与状态、基础句对象选择与锁定、召唤单位与关联卡的基础循环、省略句与显式主语、法术类型与全局道具触发、召唤物离场与关联卡失效、召唤物生命承伤与敌方选取、召唤关联卡生成与入手、召唤物共存与场上容量、召唤词引用与目标锁定、词性分类与卡包适配、开局手牌保障与可表达性、整句效果与词义复用、防护状态的定义与生成、施法效果的来源与修正；其余内容继续澄清，正式核心玩法、目标玩家和实现方式均未定。2026-09-06 新增[灵活句式、词性复用与多法术类型评议](workspaces/game-002/game-design-workflow/idea-inbox/2026-09-06-flexible-grammar-and-spell-types.md)，相关旧素材进入适用性复审；SG1-SG5、FG1-FG5、ST1-ST6、SL1-SL6、SH1-SH6、SC1-SC6、SN1-SN5 及 SR1-SR6 已分别局部晋级，WC1-WC5 词性分类与卡包适配已独立晋级，OH1-OH5 开局手牌保障与可表达性已独立晋级，SM1-SM3 整句效果与词义复用已独立晋级，PA1-PA3 防护状态的定义与生成已独立晋级，ER1-ER3 施法效果的来源与修正已独立晋级，当前继续澄清 PS1-PS3 周期状态的强化继承。
- **[上一款游戏归档](archive/2026-09-05-core-card-project/README.md)**：Parked / Archived，2026-09-05 暂停。

新游戏与上一款游戏无关，不是续作、改版或技术迁移。旧设定、素材资格、决策、测试、代码和排期不会自动继承。

## 快速开始

直接说一个想法、参考产品或验证问题。新输入进入 game-002 的 idea-inbox，经 grill-with-docs 资格确认后，才进入正式素材、GDD、提案和评估。

| 位置 | 职责 |
| --- | --- |
| workspaces/game-002/ | 新游戏独立的设计、研究、词汇、决策与开发索引 |
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
