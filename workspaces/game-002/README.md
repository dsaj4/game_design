# 游戏构思 002

Project ID：game-002
状态：Active / Idea Qualification
创建日期：2026-09-05

这是全新的独立游戏构思，与上一款游戏无关，不是续作、改版或技术迁移。
已收到暂定名《言咒》的组合施法与 Roguelike 构筑初稿，正在澄清；这些内容尚未成为正式核心构思。平台、目标玩家和实现方式仍为 Unknown。

当前有 3 份 inbox 记录：[原始初稿与澄清](game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md)、[词汇循环双路线评议](game-design-workflow/idea-inbox/2026-09-05-vocabulary-cycle-alternatives.md)及[方案 A 词汇卡组循环细化](game-design-workflow/idea-inbox/2026-09-05-deck-vocabulary-cycle.md)。用户已选择 A 继续细化，B 整套循环暂不推进；A 中按用户要求预留联想、回忆等牌序干预。[时间预算与施法打断](game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)、[时间补牌与多张牌序预览](game-design-workflow/idea-materials/M-2026-09-05-timeline-draw-preview.md)、[固定词类与语义兼容](game-design-workflow/idea-materials/M-2026-09-05-fixed-grammatical-roles.md)、[新词直接加入本局卡组](game-design-workflow/idea-materials/M-2026-09-05-new-word-deck-inclusion.md)、[战场状态跨行动保留](game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md)、[普通战斗胜负目标](game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)、[普通胜利后的生命保留](game-design-workflow/idea-materials/M-2026-09-05-post-victory-health-persistence.md)及[休整恢复与构筑取舍](game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-deck-choice.md)、[局内分叉路线](game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md)已分别晋级为 Qualified GDD Material，共 9 份，证据状态均为 Hypothesis。其余机制和具体数值继续澄清，确认后再实现。尚无正式 GDD、玩法提案或代码任务。附件自称 GDD v0.1，不代表整稿通过资格确认。

## 开始

最新讨论：固定三类不混用，且同时要求谓语能处理宾语、主语能承接谓语结果；两层兼容原则已确认并扩充既有合格素材，有限跨位建议未采纳。已有状态引用须投入对应宾语卡、制造状态本身不自动获得词卡，也已确认并扩充构句素材。词卡各自带耗时、整句基础耗时相加也已确认并扩充时间素材。基础版暂不启用独立字数上限也已确认，原稿保留待扩展阶段再评估。战斗之间收下的普通新词直接加入本局卡组、不设每战免费换牌备用库已确认并独立晋级。普通战斗后的词卡奖励允许全部跳过也已确认并扩充入组素材。同名独立副本与本局卡组同名最多三张已确认并扩充素材。临时复制、删除仅影响当前战斗已确认，副本战后消失、被本场移除的原有卡下一场恢复，持续范围已扩充入组素材；临时副本不占本局三张名额、允许使本场同名数量超过三张也已确认并扩充素材；临时副本正常弃置、参与洗回也已确认并扩充供给素材；用户要求基础复制相关设计待复制效果卡牌出现后再讨论，具体能力及默认置顶建议均已后置、未采纳；已有通用规则保留。敌方行动结束即开始下一次准备、战斗时间轴与补牌计时连续已确认并扩充时间素材；敌方准备开始时确定并公开行动及执行时间、准备中仅因明确效果变更并告知玩家，也已确认并扩充时间素材；战场状态本场跨施法、跨敌方行动保留，仅按自身规则或明确效果变化、消失，也已确认并独立晋级；引用本身不附加消耗、消耗与变化由具体操作决定也已确认，已扩充构句与状态素材；满足其他条件时允许在引用材料未出现前提前施法也已确认，已扩充构句素材并同步状态与时间素材；必需材料完全缺失时整句落空、弃牌且不退时间也已确认，已扩充时间、供给素材并同步构句与状态素材；基础版不提供通用主动取消也已确认，已扩充时间素材并同步供给、构句素材；普通战斗击败全部敌人获胜、玩家生命耗尽则失败也已确认并独立晋级；普通战败结束本局、继续游玩需重开也已确认并扩充胜负素材；普通胜利不自动回满生命、剩余生命继续保留也已确认并独立晋级；临时战场状态默认在整场结束时清除也已确认并扩充状态素材；终点首领战胜利即通关并结束本局已确认；途中休整的恢复与构筑互斥已确认并独立晋级；休整改善方式已确定为随机卡包三张词卡选一张，升级暂缓；先选拿牌或恢复再开包、开包后可全部放弃、候选排除本局同名满三张的词已确认；开包后放弃不返还恢复机会，同包三张候选互不重名已确认；休整卡包主谓宾各一张、各类内部随机已确认；选择收益前检查完整卡包、某类无合格词时不提供拿牌并保留恢复已确认；休整一次有限回血、最多补至生命上限已确认，轻伤可补满；2026-09-06 下一次休整的位置提前可知已确认，具体路线与间隔后定；局内分叉路线已确认并独立晋级；当前评议选路前是否公开下一步活动类型、战斗的敌人类型与主要机制。界面、逐事件等待操作与停点、具体数值及联想回忆等扩展继续后置。

直接提出一个想法、参考产品或验证问题，先记录到本工作区 inbox，通过资格闸门再进入正式设计链。

- [原始想法](game-design-workflow/idea-inbox/README.md)
- [核心构思占位](game-design-workflow/core-concept.md)
- [项目决策](game-design-workflow/decision-log.md)
- [当前问题](research/00-index-and-roadmap/current-questions.md)
- [项目总控](docs/control-center.md)
- [开发索引](docs/code-development-index.md)
- [项目词汇](CONTEXT.md)
- [共享模板](../../game-design-workflow/templates/README.md)
- [共享 Wiki 与规则](../../docs/shared-knowledge.md)

不检索或继承旧项目素材、测试和排期。共享知识只提供方法，设计需要独立确认。
