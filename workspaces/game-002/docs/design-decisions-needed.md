# 设计决定与后续工作

日期：2026-09-11。状态：G002-CORE-012法术类型与G002-CORE-013类型扩展、G002-CORE-014疲劳方向已采纳，对象范围继续按G002-CORE-011；Core Concept v0.6，证据Hypothesis。当前先建立[四层数值框架](../game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)，继续按[类型入口](spell-type-index.md)组织。

## 当前已确定

| 范围 | 当前规则 | 依据 |
| --- | --- | --- |
| 战前与自动循环 | 完整库存构句，一卡一位置且同场一法术，一法术一法杖；首次冷却起点0–10刻 | [核心](../game-design-workflow/core-concept.md) |
| 引用与名单 | 实例保持身份，条件战前固定；每次开始确定一次直接名单，不追加、不重选、不补位 | [引用素材](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md) |
| 时间与结果 | 释放开始仲裁，当前冷却改期最早下一刻；生命伤害打断、四阶段、整句成功与胜利终止 | [执行规则](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md) |
| 对象交互 | 以数量、强度、剩余时间或状态改变为主；点燃/冰冻等简单变化进入当前内容设计 | [简化素材](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md) |
| 法术生成物 | 增加真实火焰、雷电、冰霜对象；身份/来源/窗口与宿主状态、演出分开 | 同上 |
| 资源收集 | 法术作用于合格对象后对象掉卡；资格与同名额度先检查，合法卡进入待领取整体收益 | [收益素材](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md) |
| 超时疲劳 | 双方随时间扣减生命，法术不能恢复生命；沿用生命胜负，执行细则与数值候选 | [疲劳素材](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md) |
| 数值 | 全部重新设计；不使用示例默认值 | [数值任务](numerical-redesign.md) |
| 法术类型 | 简易看省略主语，状态/元素/召唤看名词特征；一条法术可同时命中多类；当前四类可以扩展，并为流派设计提供依据 | [类型素材](../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md) |

## 当前暂缓

- 位移、连接、支撑、独立空间参照、指定飞行方向与玩家指定新受术端点。场景位置与范围判定仍保留。
- 环境材料份额、容器供材/收材、配方/合成、材料转移加工与物体复制。
- 完整召唤/指挥、法杖起始资源与镶嵌细则。
- 燃料、自动传播、导电网络和坍塌等复杂环境机制；简单点燃/冰冻已进入当前设计。

## 已处理的接口

C01伤害/生命支付与反馈、C02逐对象数量/成本及整句成功、C06产出资格、C08词卡时间用于冷却继续适用。C03/C04完整召唤及未来单位占位、C05镶嵌仍后置。C07保留变化的发生/发展/结果表达，其复杂BF机制后置范围依上表；不再把简单点燃/冰冻一并阻挡。

R01–R32保留编号追踪，[现行规则表](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)直接陈述收束后的权限。G002-CORE-010是框架采纳记录，G002-CORE-011是当前范围修订；不要求重新回答这32项。

## 当前类型工作

已按用户明确指令采纳四类标准，完成首批18词归类及26项例句记录，包含全部用户例句；后续按[类型入口](spell-type-index.md)逐类讨论。护甲属于状态，因此“获得护甲”为简易＋状态；“恶魔释放火焰”为召唤＋元素。

上一批元素载体、冰冻减伤、对象一次掉卡、具体数值和逐刻方案先Parked，原定普通攻击保护/反弹/转移细则也暂停。基础执行规则与已采纳对象范围保持；数值重设计任务并未取消，但不把搁置方案作为默认值。

类型体系已确认可扩展，并关联后续流派设计。后续遇到未归类法术时主动检查可明确判定、可复用的新特征；适合时提出新类型的名称、特征、正反例、与现有类型的关系、流派价值和待验证问题，用户采纳后同步。当前没有新增类型或遗留人工选择，不需为扩展规则重复确认；TC23“我伤害敌人”保留现有结果，纳入后续扩展检查。

分类无需再确认四类标准。后续具体内容缺口按类记录：状态主语例句的完整语法/词义；元素的具体作用；召唤词义与完整流程边界；各类与交叉类型的收益。类型识别不替代句法和语义合法性，本次不据“燃烧蔓延／燃烧加倍”解锁新通用句式或复杂传播。

## 当前参数设计

用户已明确本轮同时给出参数定义和首轮测试数值，见[启动记录](../game-design-workflow/idea-inbox/2026-09-11-parameter-design-start.md)。现有[攻防Candidate v0.1](../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md)完成局部资格确认：通用参数、4种测试词、伤害敌人／获得护甲两句、共同敌人、4个代表配置及节奏敏感性。具体参数尚未Accepted；没有恢复被搁置的元素、冰冻或掉卡方案。

本轮结果供设计评议：以12刻敌方节奏作为入门测试候选，8、10刻作为压力样本。两种方案在快慢与损伤上有区别；护甲被击穿时会连带失去冷却机会，需要后续内容提供可解释的应对。限定计算与实现已独立复核；用户随后明确先建立四层框架，其他词效暂不展开。正式资源、经济和整局平衡仍待设计。

## 当前框架与待决问题

[四层框架Candidate v0.2](../game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)已经给出收益／时间方法、五个进度点的双方预算、跨战账本与EX01–EX09体验门槛。用户明确设计范围；具体指标目标仍为候选，不写成已通过结论。

| 编号 | 问题 | 推荐与当前状态 |
| --- | --- | --- |
| NF-D01 | 超时采用何种终局压力 | 已处理：G002-CORE-014采纳疲劳，双方随时间扣血且法术禁疗；不直接超时判负 |
| NF-D01-C | 疲劳执行细则与具体参数 | FAT-C01–08为候选：触发／周期／曲线、护甲与打断、同刻及禁疗；先独立审查，未作为正式默认值。EX02计入完整疲劳阶段 |
| NF-I01 | 阶段资源、获取分布、路线／恢复／价格尚未形成完整输入 | 按框架分层补齐；成长2.30／1.60等是目标预算，不是假定已获得属性 |
| NF-I02 | 卡池策略宽度、1倍速秒数与玩家理解证据不足 | 标NotEvaluable；不能从两句与自动检查证明无唯一最优或体验通过 |

## 测试交接

[固定测试交接](test-handoff.md)持续维护。上一批TH-2026-09-11-001已完成限定计算与demo验证，历史报告保留；新批次TH-2026-09-11-002修订r2，增加疲劳包与账本审查。r1保留原输入追溯；旧证据复评和含疲劳的新情境分开。执行状态以交接页为准，不重新执行已经通过且输入未变的完整726组，仅在发现差异或扩大范围时追加必要验证。

## 来源

- [本次用户原话与资格确认](../game-design-workflow/idea-inbox/2026-09-10-simple-object-interactions.md)。
- [本次采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md)与[决策记录](../game-design-workflow/decision-log.md)。
- [C01–C08来源](../game-design-workflow/idea-inbox/2026-09-10-design-interface-questions.md)、[SW01/SW02来源](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)、[R01–R32来源](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md)。
- [本轮交付](semantic-world-simplification.md)及[修改前快照](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md)。

当前分类来源：[2026-09-11用户原话](../game-design-workflow/idea-inbox/2026-09-11-spell-type-system.md)及[采纳文本](../game-design-workflow/draft-changes/D-2026-09-11-spell-type-system.md)。

类型扩展来源：[用户补充](../game-design-workflow/idea-inbox/2026-09-11-spell-type-system.md)及[G002-CORE-013采纳](../game-design-workflow/draft-changes/D-2026-09-11-extensible-spell-types.md)。

当前阶段来源：[本轮用户原话](../game-design-workflow/idea-inbox/2026-09-11-numerical-evaluation-framework.md)。

疲劳来源：[用户原话](../game-design-workflow/idea-inbox/2026-09-11-overtime-fatigue.md)、[G002-CORE-014](../game-design-workflow/draft-changes/D-2026-09-11-overtime-fatigue.md)。
