# 言咒现行设计

Project ID：game-002。文档角色：Navigation。更新：2026-10-01。当前GDD 2.0 / TL-1，GDD-0；已采纳核心结构，内容与完整参数尚未闭合。

[核心设计](core-design.md) · [GDD总览](GDD.md) · [版本与旧版取证](baseline.md) · [当前问题](../governance/questions.md)

| 文档 | 维护内容 |
| --- | --- |
| [SYS-001](systems/01-grammar.md) | 词卡、完整法术、绑定与卡牌类别 |
| [SYS-002](systems/02-wands.md) | 一杖一法术、加工、交付、路由与返工 |
| [SYS-003](systems/03-combat.md) | 战斗行、敌方倒计时、时序、伤害和胜负 |
| [SYS-004](systems/04-elements-environment.md) | 环境资源、转化、维护与产物；旧文件名保留定位 |
| [SYS-005](systems/05-route-encounters.md) | 遭遇程序与路线接口 |
| [SYS-006](systems/06-rewards-growth.md) | 战中与战外资源、获取和成长边界 |
| [SYS-007](systems/07-interaction-save.md) | 可操作信息、暂停、保存与干涉系统边界 |
| [卡表](content/cards.md) | 新卡表设计合同与候选入口 |
| [法杖](content/wands.md) | 法杖内容重设计状态 |
| [敌人与遭遇](content/enemies-encounters.md) | 敌牌内容字段与迁移状态 |
| [参数](parameters.md) | 单位、已定约束与未定数值 |
| [验收](validation.md) | 新版规则、体验任务与停止条件，全部NotRun |
| [素材审查](source-review.md) | 纳入、替代、重设计与原始来源边界 |

旧RC1数字、空间规则与验收用例不再从本目录的“当前”身份继承；需要追溯时读固定旧提交。

兼容材料已按[CORE-048](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)补入TL-26–37（文档修订reuse.1）：构句／对象／支付、单向路线、库存与节点选择、保存及数量合同。使用旧材料时先核对[逐来源适用表](../exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)，不从历史正文补入未定新参数。
