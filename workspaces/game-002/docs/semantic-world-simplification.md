# 简单对象交互范围修订交付

日期：2026-09-10。Project ID：game-002。决策G002-CORE-011已采纳；Core Concept v0.6，证据Hypothesis。

## 本轮结果

用户明确要求对象受操作后直接发生变化，不深入位移、结构或材料加工。当前正文已收束为简单数量/状态变化，加入真实火焰、雷电、冰霜生成物，资源收集止于法术作用于合格对象后对象掉卡。范围已写入核心、R01–R32现行表与相关素材；具体效果和数值仍待设计。

[对象目录](../game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md)保留13个当前条目，[作用目录](../game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md)归纳10类方向，[代表情境](../game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md)改为12项简单作用检查。三份目录不再推进材料账、配方、连接路径或指定端点。

## 范围裁定

| 问题 | 本轮处理 |
| --- | --- |
| 单一数值难表达的空间/结构操作 | 暂缓位置目标、位移、连接、支撑、空间参照、指定飞行方向和玩家指定新受术端点；场景位置和法杖范围仍作判断 |
| 供材、容器与资源转化 | 暂缓环境材料份额、供收、配方、加工/运输与复制 |
| 状态消耗 | 保留已明确的护甲等宿主状态数量规则，统一名称，不能据此恢复通用供材 |
| 收集法术 | 合格对象受到明确收集作用后直接掉卡；资格/额度先检查，合法卡进入待领取；无手动拾取步骤 |
| 法术生成物 | 明确火焰、雷电、冰霜对象身份、来源和真实窗口；与宿主状态/演出分开 |
| 点燃/冰冻 | 进入当前简单变化设计；不默认伤害、停攻或元素连锁 |
| 抵挡/反弹/非指定转移 | 类别允许继续设计；不指定方向/接收者，不等于自动算法已经完成 |
| 其他后置系统 | 完整召唤、镶嵌、燃料、传播、导电网络和坍塌仍后置 |

## 来源与保存

[用户原话](../game-design-workflow/idea-inbox/2026-09-10-simple-object-interactions.md)已局部资格确认；[素材](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md)→[提案](../game-design-workflow/idea-proposals/P-2026-09-10-simple-object-interactions.md)→[评估](../game-design-workflow/evaluations/E-2026-09-10-simple-object-interactions.md)→[采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md)→[核心](../game-design-workflow/core-concept.md)与[决策记录](../game-design-workflow/decision-log.md)建立追溯。用户已明确提出修改，无额外方向确认。

8份关键输入保存在[原始快照](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md)，逐份源/副本哈希一致。阶段原话和历史采纳保留为证据；当前规范由核心、现行R表、素材与内容入口提供。

正式素材由44增至45，inbox由17增至18。未新增正式GDD，未修改游戏实现；没有将目录或纸面情境完成视为玩家验证。

## 检查记录

检查完成：51份本轮设计/索引文档严格UTF-8解码与写入内容核对通过；661处本地链接对应145个目标，全部存在；表格列数检查通过。8份原始字节快照SHA-256保持一致。R01–R32编号保留，当前目录13条、作用方向10类、情境12项，与各入口数量一致。

现行核心、正式素材、词汇及进度入口的范围扫描和语义复核未发现仍将位移、结构连接、环境供材/配方或指定端点作为当前可用操作的冲突。已核对生成物/状态/特效区分、后续释放引用、掉卡资格与整体收益，以及保护类仅作用未完成效果的边界。git差异空白检查通过。历史来源按其证据用途保留，不作为现行操作权限。

这些结论只覆盖文档与纸面规则，未运行游戏、未验证平衡或玩家理解；未知的自动接收算法与数值未被填写成已确认结果。

## 本轮文件清单

共59份，包括8份字节快照及其索引；其余为设计正文、来源和导航。没有纳入工作区原有debug.log及无关研究目录变动。

| 文件 | 处理 |
| --- | --- |
| [README.md](../../../README.md) | 同步入口/来源/术语 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/CONTEXT.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/CONTEXT.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/docs/semantic-world-content-index.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/docs/semantic-world-content-index.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/core-concept.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/core-concept.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md) | 原始输入保存 |
| [archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md) | 原始输入保存 |
| [docs/control-center.md](../../../docs/control-center.md) | 同步入口/来源/术语 |
| [workspaces/game-002/AGENTS.md](../AGENTS.md) | 同步入口/来源/术语 |
| [workspaces/game-002/CONTEXT.md](../CONTEXT.md) | 同步入口/来源/术语 |
| [workspaces/game-002/README.md](../README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/README.md](README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/control-center.md](control-center.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/design-decisions-needed.md](design-decisions-needed.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/numerical-redesign.md](numerical-redesign.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/semantic-world-content-index.md](semantic-world-content-index.md) | 同步入口/来源/术语 |
| [workspaces/game-002/docs/semantic-world-simplification.md](semantic-world-simplification.md) | 本交付 |
| [workspaces/game-002/game-design-workflow/README.md](../game-design-workflow/README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/core-concept.md](../game-design-workflow/core-concept.md) | 同步核心 |
| [workspaces/game-002/game-design-workflow/decision-log.md](../game-design-workflow/decision-log.md) | 记录G002-CORE-011 |
| [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md](../game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md) | 采纳记录 |
| [workspaces/game-002/game-design-workflow/draft-changes/README.md](../game-design-workflow/draft-changes/README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-simple-object-interactions.md](../game-design-workflow/evaluations/E-2026-09-10-simple-object-interactions.md) | 新增评估 |
| [workspaces/game-002/game-design-workflow/evaluations/README.md](../game-design-workflow/evaluations/README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md) | 简化当前内容 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md) | 简化当前内容 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md) | 简化当前内容 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-simple-object-interactions.md](../game-design-workflow/idea-inbox/2026-09-10-simple-object-interactions.md) | 原话与资格 |
| [workspaces/game-002/game-design-workflow/idea-inbox/README.md](../game-design-workflow/idea-inbox/README.md) | 同步入口/来源/术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md](../game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md](../game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md](../game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md](../game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-prebattle-expressibility.md](../game-design-workflow/idea-materials/M-2026-09-06-prebattle-expressibility.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-preset-starting-inventory.md](../game-design-workflow/idea-materials/M-2026-09-06-preset-starting-inventory.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md](../game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md](../game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md](../game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md](../game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md](../game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-battlefield-state-change-expression.md](../game-design-workflow/idea-materials/M-2026-09-10-battlefield-state-change-expression.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md](../game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md) | 新增合格范围 |
| [workspaces/game-002/game-design-workflow/idea-materials/README.md](../game-design-workflow/idea-materials/README.md) | 同步范围/状态数量术语 |
| [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-simple-object-interactions.md](../game-design-workflow/idea-proposals/P-2026-09-10-simple-object-interactions.md) | 新增提案 |
| [workspaces/game-002/game-design-workflow/idea-proposals/README.md](../game-design-workflow/idea-proposals/README.md) | 同步入口/来源/术语 |

## 下一步

按[当前内容入口](semantic-world-content-index.md)补齐元素生成物、简单状态、保护/作用转移和对象掉卡的具体词义，再重新设计参数与真实逐刻验证。反弹归宿、转移接收、冰冻行动影响及掉卡次数仍Unknown，不在本次范围修订中擅自决定。
