# 游戏构思002：《言咒》

Project ID：game-002。状态：Active / Stable Design Baseline。当前核心为Core Concept v0.6；证据为Hypothesis，数值平衡和玩家体验尚待验证。

玩家在战前使用完整词卡库存构句，每个组合对应一条循环法术；设置一法术一法杖的绑定、范围与顺序，在第0–10刻安排首次冷却。战斗自动运行，同刻按法术、敌人攻击、环境变化、状态效果处理。战后金币与法术产生的词卡整体领取或放弃。

当前有49份合格素材，涵盖构句、循环、状态、目标、局内成长、战场表现、语义世界范围、两种引用及数值重设计约束。C01–C08均按推荐处理，文档统一的人工冲突已结清；召唤、镶嵌和复杂环境机制后置；简单点燃/冰冻及真实元素生成物在已确认范围内，具体词效按类型另行讨论。数值设计重新建立，已形成[首轮攻防参数候选](game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md)，其限定计算及实现已独立复核；候选未采纳，尚无正式GDD或完整对局验证结论。[四层数值评估框架](game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)已建立；[全局规则审查](docs/global-rules-audit-2026-09-11.md)已完成，下一步回归[卡牌与流派设计—评测—采纳](docs/card-design-review-workflow.md)，待测内容积累到下次一起执行。

当前对象范围按[简单对象交互采纳](game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md)继续有效；当前新增[法术类型系统](docs/spell-type-index.md)：简易看省略主语，状态、元素、召唤看对应名词特征，一条法术可有多个类型。首批18词和26项例句已归类，后续按类型讨论。上一批具体词效、参数与纸面方案先搁置，分类不自动恢复这些内容。

- [核心构思](game-design-workflow/core-concept.md)
- [正式素材](game-design-workflow/idea-materials/README.md)
- [候选与原始表达入口](game-design-workflow/idea-inbox/README.md)
- [设计决定与后续工作](docs/design-decisions-needed.md)
- [逐文件审查与验收](docs/design-alignment-audit.md)
- [数值重设计任务](docs/numerical-redesign.md)
- [测试交接与回填](docs/test-handoff.md)
- [项目决策](game-design-workflow/decision-log.md)
- [项目总控](docs/control-center.md)
- [领域词汇](CONTEXT.md)
- [实现进度](docs/code-development-index.md)

本项目独立于其他游戏；共享方法见[知识入口](../../docs/shared-knowledge.md)，设计模板见[登记清单](../../game-design-workflow/templates/README.md)。

超时后的[疲劳方向](game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md)已按G002-CORE-014采纳：双方持续扣血且法术禁疗，仍按生命结果分胜负。具体执行与数值候选，后续审查纳入固定测试交接。
