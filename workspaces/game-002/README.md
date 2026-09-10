# 游戏构思002：《言咒》

Project ID：game-002。状态：Active / Stable Design Baseline。当前核心为Core Concept v0.6；证据为Hypothesis，数值平衡和玩家体验尚待验证。

玩家在战前使用完整词卡库存构句，每个组合对应一条循环法术；设置一法术一法杖的绑定、范围与顺序，在第0–10刻安排首次冷却。战斗自动运行，同刻按法术、敌人攻击、环境变化、状态效果处理。战后金币与法术产生的词卡整体领取或放弃。

当前有44份合格素材，涵盖构句、循环、状态、目标、局内成长、战场表现、语义世界范围、两种引用及数值重设计约束。C01–C08均按推荐处理，文档统一的人工冲突已结清；召唤、镶嵌和具体环境机制按确认范围后置。数值设计重新建立，尚无正式GDD或完整对局验证结论。

当前[SW01对象范围](game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)与[SW02两种引用](game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)已采纳：实例保持身份，条件战前固定而每次匹配当前对象，基础规则保持固定。SW02-A已确认完整法术开始处理时确定一次直接名单，本次不追加、重选或补位，仍逐对象读取当前合法性与材料。[R01–R32执行规则](game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)已全部采纳，允许明示位移与结构变化、复合对象短语、过程改期，并明确反应与资源权限。[首批内容草案](docs/semantic-world-content-index.md)已给出32类对象、18类能力、55个词条候选和40项代表句；新增内容保持Raw Idea / Unqualified，集中复核后进入参数设计与逐刻验证。本次文件和检查见[规则采纳交付](docs/semantic-world-rules-adoption.md)。

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
