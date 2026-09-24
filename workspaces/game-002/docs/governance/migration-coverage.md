# 核心闭环迁移覆盖

文档角色：MigrationAudit。2026-09-23 / doc.1。原战斗页“核心玩法闭环”跨多个系统，复核时逐段分配到责任系统，保留基础句式、库存、绑定、读值、支付、成功和失败语义。历史全文见[原文](../history/pre-organization/game-design-workflow/gdd/yanzhou-rc1/03-combat-and-status.md)。

| 原段落识别 | 当前责任系统 |
| --- | --- |
| 每场战斗前，玩家依次完成构句、构成法术、设置法杖三个配置… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 一个合法组合共同定义一条完整循环法术，组合中的词不分别施… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 状态引用须配置对应名词词卡，可在词义许可的句法角色中参与… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 每条循环法术绑定一根法杖，每根法杖承载一条法术。设置法杖… | [SYS-002](../../game-design-workflow/gdd/current/systems/02-wands.md) |
| 完成法杖配置后，玩家在第0–10刻内安排所有循环法术第一… | [SYS-002](../../game-design-workflow/gdd/current/systems/02-wands.md) |
| 所有循环法术的释放尝试投影到同一条纵向时间轴，共享槽在每… | [SYS-003](../../game-design-workflow/gdd/current/systems/03-combat.md) |
| 敌方当前已知攻击安排与明确变化原因公开；基础安排预设；首… | [SYS-003](../../game-design-workflow/gdd/current/systems/03-combat.md) |
| 战斗位于第一人称面对的2×5格长方形场景，敌人和环境对象… | [SYS-004](../../game-design-workflow/gdd/current/systems/04-elements-environment.md) |
| 法术对象引用支持实例绑定与条件绑定，两种方式并存。实例绑… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 两种绑定均遵守法杖允许范围、已分配词卡的词义及对象当前合… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 每次完整法术开始处理时，按当时的绑定与世界确定本次直接对… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 本次产生或新符合条件的对象留到后续释放重新匹配。本次名单… | [SYS-001](../../game-design-workflow/gdd/current/systems/01-grammar.md) |
| 每条法术逐个检查对象当前合法性及明示状态数量与成本。实例… | [SYS-003](../../game-design-workflow/gdd/current/systems/03-combat.md) |
| 战斗超时后进入疲劳，双方随战斗时间持续扣减生命；疲劳期间… | [SYS-003](../../game-design-workflow/gdd/current/systems/03-combat.md) |
| 战后保留金币与词卡的整体收益容器，整体领取或整体放弃。首… | [SYS-006](../../game-design-workflow/gdd/current/systems/06-rewards-growth.md) |

首版副词、敌攻改期及产卡产金接口按RC1已采纳范围澄清；未选后续产出约束只留来源。没有以去重为由删除两种外层句式或空名单成功/费用规则。旧章节兼容链接、逐卡参数链接和原始SHA由本次整理清单追踪。
