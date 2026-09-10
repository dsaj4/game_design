# 游戏构思002：《言咒》

Project ID：game-002。状态：Active / Stable Design Baseline。当前核心为Core Concept v0.6；证据为Hypothesis，数值平衡和玩家体验尚待验证。

玩家在战前使用完整词卡库存构句，每个组合对应一条循环法术；设置一法术一法杖的绑定、范围与顺序，在第0–10刻安排首次冷却。战斗自动运行，同刻按法术、敌人攻击、环境变化、状态效果处理。战后金币与法术产生的词卡整体领取或放弃。

当前有45份合格素材，涵盖构句、循环、状态、目标、局内成长、战场表现、语义世界范围、两种引用及数值重设计约束。C01–C08均按推荐处理，文档统一的人工冲突已结清；召唤、镶嵌和复杂环境机制后置；简单点燃/冰冻及真实元素生成物进入当前内容设计。数值设计重新建立，尚无正式GDD或完整对局验证结论。

当前对象范围按[简单对象交互采纳](game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md)收束：保留数量/状态变化，新增火焰、雷电、冰霜等真实法术生成物；收集法术作用合格对象后直接掉卡。位移、连接/支撑、指定方向/端点及环境材料加工暂缓。实例/条件引用、固定单次名单和自动循环骨架继续有效。[当前内容入口](docs/semantic-world-content-index.md)包含13个条目、10类作用与12项纸面情境；具体词义与参数待设计。

- [核心构思](game-design-workflow/core-concept.md)
- [正式素材](game-design-workflow/idea-materials/README.md)
- [候选与原始表达入口](game-design-workflow/idea-inbox/README.md)
- [设计决定与后续工作](docs/design-decisions-needed.md)
- [逐文件审查与验收](docs/design-alignment-audit.md)
- [数值重设计任务](docs/numerical-redesign.md)
- [项目决策](game-design-workflow/decision-log.md)
- [项目总控](docs/control-center.md)
- [领域词汇](CONTEXT.md)
- [实现进度](docs/code-development-index.md)

本项目独立于其他游戏；共享方法见[知识入口](../../docs/shared-knowledge.md)，设计模板见[登记清单](../../game-design-workflow/templates/README.md)。
