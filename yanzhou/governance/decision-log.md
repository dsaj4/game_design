# game-002 决策记录

> 文档角色：DecisionRecord。当前规格为[GDD 2.1 / TL-1 + INS-1](../design/README.md)，GDD-0 / Hypothesis / NotRun。历史Accepted记录保留原确认，不等于全文仍适用；现行替代关系以CORE-037–051及[素材审查](../design/source-review.md)为准。

现行结构由CORE-037–047建立、CORE-048限定复用、CORE-049采用铭刻入口；CORE-050补明未来供料调度，CORE-051改为单一处理耗时与开工预留；其中CORE-041的配置入口和法器直接资源交付、旧J／R／S及完工等待均按各次范围替代。旧CORE-006的掉血全杖打断、CORE-011的对象边界及旧镶嵌设计顺序不能覆盖新版。编号别名见[登记](id-registry.md)。

## 2026-09早期决定（历史索引）

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-ADMIN-001 | 2026-09-05 | 建立独立工作区，仅共享方法、结构与规范 | Accepted / Administration | 原始决策完整记录见下方 |
| G002-CORE-006 | 2026-09-09 | 战前完整库存构句、一组合一循环法术、一法术一法杖；配置顺序、0–10刻首次冷却与自动循环；同刻四阶段、生命伤害打断冷却、胜利终止、整体战后收益；目标引用适用G002-CORE-008 | Accepted：配置与循环依据；目标引用已按SW02完善；Hypothesis | [核心](../design/core-concept.md)、[战前配置适用文本](../sources/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md) |
| G002-DOC-001 | 2026-09-10 | 按用户授权逐份统一文档并保存原始快照；兼容部分保留，接口集中呈现；用户采纳范围按G002-CORE-007与G002-SCOPE-001执行 | Accepted / Documentation；Hypothesis | [文档统一](../sources/draft-changes/D-2026-09-10-current-design-alignment.md)、[决定清单](questions.md) |

## 决策证据索引

G002-ADMIN-001、G002-CORE-001至G002-CORE-006的完整原始决定、日期与状态均保存在[原始决策记录](../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/decision-log.md)。以下文件是当前适用范围说明，不能当作原始决定原文：

- G002-CORE-001：[施法设计支柱](../sources/draft-changes/D-2026-09-09-casting-design-pillars.md)。
- G002-CORE-002：[时间背包编排](../sources/draft-changes/D-2026-09-09-timeline-backpack-core.md)。
- G002-CORE-003、004：[自动战斗边界](../sources/draft-changes/D-2026-09-09-automatic-battle-boundaries.md)。
- G002-CORE-005：[稳定设计基线](../sources/draft-changes/D-2026-09-09-core-system-stable-baseline.md)。
- G002-CORE-006：[战前构句与法杖](../sources/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md)。

C01–C08按用户批量确认全部处理，当前没有本轮遗留人工冲突。数值重新设计已确认，具体参数与体验证据仍为Unknown / Hypothesis。

## 接口采纳与数值任务

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-007 | 2026-09-10 | C01伤害/支付分类与独立反馈，C02逐对象材料、公开固定顺序和完整法术成功，C06产出资格前置与产金成本，C08词卡时间合计用于冷却；数值全部重新设计 | Accepted / Core Concept v0.6；Hypothesis | [拟修改与来源](../sources/draft-changes/D-2026-09-10-accept-design-decisions.md)、[数值任务](../design/parameters.md) |
| G002-SCOPE-001 | 2026-09-10 | C03完整召唤后置，推进时设计战前单位占位与出生位置；C04当前不增加专属引用词卡；C05镶嵌细则与C07 BF1–BF3按推荐后置 | Accepted / Scope；具体机制Unknown | [决定清单](questions.md)、[合格范围素材](../sources/materials/M-2026-09-10-accepted-design-interfaces.md) |

确认前推荐、数值来源与文档验收已封存于[决策输入快照](../../archive/2026-09-10-game-002-decision-inputs/INDEX.md)，用于追溯，不作为参数基线。

## 语义世界对象范围

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-SCOPE-002 | 2026-09-10 | SW01：实体、部件、材料、属性状态、空间关系及飞行物、敌方攻击、法术冷却等过程纳入法术对象设计范围；各类按明确能力开放操作；胜负判定、全局结算顺序等基础规则保持固定 | Accepted / Scope；Hypothesis。具体引用与操作机制待定，Core Concept v0.6基础执行规则继续适用 | [用户确认](../sources/inbox/2026-09-10-semantic-world-object-scope.md)、[范围素材](../sources/materials/M-2026-09-10-semantic-world-object-scope.md)、[提案](../sources/proposals/P-2026-09-10-semantic-world-object-scope.md)、[评估](../sources/evaluations/E-2026-09-10-semantic-world-object-scope.md)、[采纳文本](../sources/draft-changes/D-2026-09-10-semantic-world-object-scope.md) |

SW01范围的后续引用模型按G002-CORE-008确认，单次名单按G002-CORE-009确认；其余具体机制继续设计，数值重新设计继续执行。

## 两种引用并存

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-008 | 2026-09-10 | SW02：实例绑定保持所指身份，失效跳过、不自动改指向；条件绑定战前固定选择条件，每次释放自动匹配当前对象，符合条件的新生对象可参与。两种方式并存，战前配置与既有语义、范围和材料约束继续适用 | Accepted / Reference Model；Hypothesis。名单时点后续由G002-CORE-009明确，排序及表达框架随后按G002-CORE-010明确，具体条目待设计 | [用户确认](../sources/inbox/2026-09-10-semantic-world-object-scope.md)、[素材](../sources/materials/M-2026-09-10-instance-and-conditional-binding.md)、[采纳文本](../sources/draft-changes/D-2026-09-10-instance-and-conditional-binding.md) |

SW02采纳只包含引用模型；用户随后单独确认SW02-A，见下表。

## 2026-09-10：单次直接对象名单

| 编号 | 日期 | 决定 | 状态 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-009 | 2026-09-10 | SW02-A：完整法术开始处理时确定一次直接名单，本次不重选、追加或补位；逐对象仍检查当前合法性与材料，失效或固定消耗不足跳过且既有合法结果不回滚；本次新生或新符合条件对象留到后续释放 | Accepted / Target List；Hypothesis | [用户确认](../sources/inbox/2026-09-10-semantic-world-object-scope.md)、[合格素材](../sources/materials/M-2026-09-10-instance-and-conditional-binding.md)、[采纳文本](../sources/draft-changes/D-2026-09-10-single-release-target-list.md) |

用户同时要求一次性列出剩余决策。[R01–R32来源总表](../sources/inbox/2026-09-10-semantic-world-remaining-decisions.md)保留批量建议；用户随后全部采纳，见G002-CORE-010。

## 2026-09-10：语义世界执行规则

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-010 | 2026-09-10 | 用户全部采用R01–R32推荐：明确对象与能力、条件与成本、位移与身份、复合对象短语、多端点、过程窗口及改期、释放开始仲裁、环境反应、配置资源与跨战权限 | Accepted / Semantic World Rules；Hypothesis。32项无遗留人工选择；内容、数值与体验待验证 | [用户确认](../sources/inbox/2026-09-10-semantic-world-remaining-decisions.md)、[32条正式规则](../sources/materials/M-2026-09-10-semantic-world-executable-rules.md)、[提案](../sources/proposals/P-2026-09-10-semantic-world-executable-rules.md)、[评估](../sources/evaluations/E-2026-09-10-semantic-world-executable-rules.md)、[采纳文本](../sources/draft-changes/D-2026-09-10-semantic-world-executable-rules.md) |

R12允许明确法术位移与结构变化；R17允许明示独立遗体；R18允许名词位复合短语；R23允许改变当前剩余冷却；R24在释放开始仲裁共享槽。现用相关规则均按本决定同步，既有决定的采纳时文字从原始记录追溯。完整召唤、法杖起始资源与镶嵌、BF1–BF3仍后置；数值重新设计继续有效。

## 2026-09-10：简化对象交互与法术生成物

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-011 | 2026-09-10 | 以对象数量/状态变化为主；暂缓位移、连接、支撑、独立空间参照、定向/指定端点、环境份额/容器/配方/搬运加工；收集止于对象掉卡；增加火焰、雷电、冰霜等真实法术生成对象；允许继续设计不指定方向的抵挡/反弹及非指定接收者的作用转移 | Accepted / Scope and Flow；Hypothesis。具体效果与数值Unknown | [用户原话](../sources/inbox/2026-09-10-simple-object-interactions.md)、[素材](../sources/materials/M-2026-09-10-simple-object-interactions.md)、[提案](../sources/proposals/P-2026-09-10-simple-object-interactions.md)、[评估](../sources/evaluations/E-2026-09-10-simple-object-interactions.md)、[采纳](../sources/draft-changes/D-2026-09-10-simple-object-interactions.md) |

这是对SW01及R01–R32当前操作范围的收束，已有身份、引用、单次名单、状态数量、时间与收益骨架继续有效。简单点燃/冰冻进入内容设计；燃料、传播、导电网络、坍塌及完整召唤/镶嵌仍后置。本轮未采纳首批候选的逻辑卡、路径/配方或介入额度。输入原文见[快照](../../archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md)。

## 2026-09-11：按特征识别法术类型

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-012 | 2026-09-11 | 简易看省略主语；状态、元素、召唤看参与句义的对应名词特征；一条法术保留全部命中类型。完成首批18词及例句归类，后续按四类讨论并交叉索引；上一批具体词效、参数及原定保护细则推进先搁置 | Accepted / Spell Classification；具体效果与数值Parked或按已有状态，证据Hypothesis | [用户原话](../sources/inbox/2026-09-11-spell-type-system.md)、[素材](../sources/materials/M-2026-09-11-spell-type-system.md)、[提案](../sources/proposals/P-2026-09-11-spell-type-system.md)、[评估](../sources/evaluations/E-2026-09-11-spell-type-system.md)、[采纳文本](../sources/draft-changes/D-2026-09-11-spell-type-system.md) |

护甲按已有状态定义，“获得护甲”为简易＋状态；“火焰吞噬护甲”为元素＋状态；“恶魔释放火焰”为召唤＋元素。类型不由动词、输出效果、场上偶然存在的对象或本次成功与否决定。词义合法性与类型识别分别处理，状态主语简写例句不自动扩展通用语法或解锁复杂传播；完整召唤流程仍后置。

阶段调整保留18词作为分类对象，上一批6刻元素／一次使用、冰冻减伤、一次掉卡、参数及逐刻记录均为Parked。已有基础执行规则、对象范围和数值重设计约束继续有效。本次未恢复这些具体方案，后续按[类型入口](../design/systems/01-grammar.md)展开。

## 2026-09-11：类型扩展与流派设计

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-013 | 2026-09-11 | 简易、状态、元素、召唤为可扩展的当前基础类型；类型关联后续流派设计。后续遇到未归类法术时主动检查可判定、可复用的新特征，适合时提出新类型及例句、与现有类型的关系、流派价值和待验证问题；用户采纳后同步分类与相关记录，保留所有命中类型 | Accepted / Extensible Classification；证据Hypothesis，具体新类型及流派内容待提出 | [用户补充](../sources/inbox/2026-09-11-spell-type-system.md)、[素材](../sources/materials/M-2026-09-11-spell-type-system.md)、[采纳文本](../sources/draft-changes/D-2026-09-11-extensible-spell-types.md) |

用户本轮明确要求类型可扩展，并授权后续适合时主动提出新类型。新类型按自身明确的特征定义；当前状态、元素、召唤三类仍按名词特征判定。流派需要具体组合、核心操作、收益、时间与词卡成本、弱点和混搭关系，类型标签本身不产生加成。本次没有新增第五类，首批18词与26项例句的现有分类保留；具体词效、数值与后置系统保持各自状态。

## 2026-09-11：超时疲劳

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-014 | 2026-09-11 | 超时进入疲劳，双方随时间扣生命，疲劳期间法术不能恢复生命；保留生命胜负与同检查点失败优先 | Accepted：FAT-A方向；FAT-C执行／数值Candidate，证据Hypothesis | [用户原话](../sources/inbox/2026-09-11-overtime-fatigue.md)、[素材](../sources/materials/M-2026-09-11-overtime-fatigue.md)、[提案](../sources/proposals/P-2026-09-11-overtime-fatigue.md)、[评估](../sources/evaluations/E-2026-09-11-overtime-fatigue.md)、[采纳文本](../sources/draft-changes/D-2026-09-11-overtime-fatigue.md) |

NF-D01的方向已确定为疲劳；不采用“到验收截止即直接失败”的处理。具体触发刻、扣血曲线、护甲／打断及同刻细则仍为候选。既有报告仅对应其固定输入；本次没有新增其他词效或实现。

## 2026-09-11：全局规则边界与卡牌评测要求

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-015 | 2026-09-11 | 全部采用GR01–GR12推荐处理：参数归属／取整、冷却与取消、角色配对声明、状态归零、联合支付、存活资格与完整事件、事件声明、生成物与产出字段、候选合批、正常／极端评价范围及实际资源输入 | Accepted：处理方式／GR v1；证据Hypothesis。GR07-C01、FAT-C与数值目标仍Candidate，具体卡牌字段待设计 | [用户确认](../sources/inbox/2026-09-11-global-rules-review.md)、[合格素材](../sources/materials/M-2026-09-11-global-rule-boundaries.md)、[提案](../sources/proposals/P-2026-09-11-global-rule-boundaries.md)、[评估](../sources/evaluations/E-2026-09-11-global-rule-boundaries.md)、[采纳文本](../sources/draft-changes/D-2026-09-11-global-rule-boundaries.md) |

本次逐项保留推荐的边界：GR07选择将同阶段派生延至下一刻作为待测候选，GR10选择保留完整FAT-C候选；不等于执行细则全部定稿。GR11评价范围已采纳，四层框架升至Candidate v0.3，数值不变。12项处理选择已结清；生成物、产出、死亡派生顺序与正式资源随相关内容补齐。测试交接TH-002/r4继续Draft／NotRun，用户下一次启动前不运行或分派，旧报告不改写。

## 2026-09-11：修饰词与系统设计顺序

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-016 | 2026-09-11 | 增加修饰词卡：形容词修饰名词，副词修饰动词；可多张直接挂原词，支付实体／时间成本；不兼容→适配→通用，特殊替代通用；数值仅修正本句，真实状态正常存续；适配看原词，同值按现有规则合并，不同附加效果从左到右。先补修饰词与镶嵌，再设计流派成套物品 | Accepted：Modifier v0.1基础模型；Hypothesis。具体词效、参数、获取及镶嵌细则仍待设计 | [四项确认](../sources/inbox/2026-09-11-modifier-card-system.md)、[素材](../sources/materials/M-2026-09-11-modifier-card-system.md)、[提案](../sources/proposals/P-2026-09-11-modifier-card-system.md)、[评估](../sources/evaluations/E-2026-09-11-modifier-card-system.md)、[采纳文本](../sources/draft-changes/D-2026-09-11-modifier-card-system.md) |

休整第三候选沿剩余合格词范围接纳有资格的修饰词，不改变前两位和三选一结构。词卡新大类不等于新法术类型。镶嵌进入当前设计顺序，取代此前排期上的后置安排；既有槽位、获取和事件候选未自动采纳。TH-002/r5只积累MDT01–MDT09，未运行或分派测试。

## 2026-09-12：固定镶嵌、类型强化与范围被动

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-017 | 2026-09-12 | 每杖自带一个固定镶嵌，象征身份并规定基础范围及可选特殊效果；强化整条法术并关联类型／特征。简易加速按第2、4、6……周期各减1刻冷却，覆盖／打断也计，不永久累积；燃烧强化为范围内各来源施加增层，周期伤害不重加层 | Accepted：IN-A及两项例子含义；Hypothesis。IN-C01–IN-C14补充、具体物品与数值仍Candidate／Unknown | [用户定义和确认](../sources/inbox/2026-09-12-wand-inlay-system.md)、[素材](../sources/materials/M-2026-09-12-wand-inlay-system.md)、[提案](../sources/proposals/P-2026-09-12-wand-inlay-system.md)、[评估](../sources/evaluations/E-2026-09-12-wand-inlay-system.md)、[采纳文本](../sources/draft-changes/D-2026-09-12-wand-inlay-system.md) |

用户授权agent先补获取、装配等规则，已形成固定身份＋可换槽位、商店渠道、同种／叠加、跨战及事件的完整候选，未将建议当作用户采纳。初始固定镶嵌的存在已明确；起始法杖数、范围参数和价格仍待设计。测试交接TH-002/r6增加IN-T01–IN-T10，未启动或分派测试。

## 效果登记工作流

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-DOC-002 | 2026-09-12 | 建立跨系统效果注册、分类与边界理清；后续主动登记用户提出的效果，检查未来实现输入完整性，不做代码或具体架构 | Accepted / Documentation；效果与参数状态各自保留，价值Hypothesis | [用户原话](../sources/inbox/2026-09-12-effect-registry.md)、[工作流素材](../sources/materials/M-2026-09-12-effect-registry.md)、[系统入口](../effects/README.md) |

本轮建立32项登记、67项显式案例关系及未决审查，接入项目AGENTS、设计流程与测试交接r7。没有修改Core Concept v0.6或采纳新的具体效果；IN-C、GR07-C01、FAT-C与Parked词效保持各自状态。本轮只做文档一致性及设计可落地审查，未运行／分派玩法测试。

## 第一人称格子战场设计记录

| ID | 日期 | 记录 | 状态 | 来源 |
| --- | --- | --- | --- | --- |
| G002-BF-001 | 2026-09-12 | 用户要求第一人称2×5、敌人居中、地面／环境物性、生成物占位及火焰导致树草燃烧／烧焦；明确树草不继续传播 | 用户方向与单项确认；完整规则Draft Change，未改核心 | [素材](../sources/materials/M-2026-09-12-first-person-grid-battlefield.md)、[GDD](../design/systems/04-elements-environment.md)、[拟修改](../sources/draft-changes/D-2026-09-12-first-person-grid-battlefield.md) |

BF-C01–15为本次补全的推荐方案，未将用户对单层传播的回答扩为全部采纳。局部范围变化已列具体替换文本；原正式基线与Parked内容保持。新增FX-060–062、FX-003／010 r2候选，测试交接r9仅积累。

## 2026-09-13：每刻末状态与自然衰减裁决

| ID | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- |
| G002-CORE-018 | 燃烧伤害／冰冻增甲每刻末处理；固定先燃烧后冰冻、同类公开单位顺序；自然衰减保留小数进度累计扣层；允许空心＋自噬长期储层 | Accepted：用户裁决及授权固定先后的落实方案；Hypothesis，新规则NotRun，旧CAL不外推 | [原话](../sources/inbox/2026-09-13-end-tick-status-rulings.md)、[素材](../sources/materials/M-2026-09-13-end-tick-status-rulings.md)、[提案](../history/accepted-design-records/P-2026-09-13-end-tick-status-rulings.md)、[评估](../history/accepted-design-records/E-2026-09-13-end-tick-status-rulings.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-end-tick-status-rulings.md) |

ST01–04明确首次生效、阶段内新状态延后、效果后衰减、清空重置进度及终局停止。其他状态不自动改为每刻周期；主动消耗、异种抵消和跨战边界保持。环境转化进度继承、每刻效果量与其余元素接口未定。本轮未改代码、未测试或采纳新参数。

## 2026-09-13：新版卡池裁决与GDD写作前收束

| ID | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- |
| G002-CORE-019 | 采用RC01–12完整推荐：首次来源、有限完整复诵、蓄势兑现、一次替换、即时一层触发、逐刻过程、消耗与自耗完成、跨杖操控与生成适配 | Accepted；Hypothesis，新规则NotRun | [RC素材](../sources/materials/M-2026-09-13-card-pool-rule-rulings.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-SCOPE-003 | 首版S2全部25项＋E3全部30项，战前／战斗／路线／休整／商店／单阶段首领；其余创意储备；先定缺口再写GDD | Accepted范围；S2方向Confirmed，参数未定 | [用户选择](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[范围素材](../sources/materials/M-2026-09-13-first-release-content-scope.md) |
| G002-CORE-020 | 每格独立地面＋一个占位体，玩家棋盘外；本格地面＋正交邻格作用，不含自身／斜角／环绕；前排树木不自动遮挡后排施法 | Accepted；Hypothesis | [空间素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-021 | 无同种时只在范围内首个存活敌人的正交相邻合法空格生成；无此类格回退，即使其他格空着；同种仍优先补层 | Accepted；Hypothesis | 同上；用户“只在所选敌人旁生成（推荐）” |
| G002-CORE-022 | 各环境形态阶段与最终转化阈值均按当前对应元素状态层数判断，不累计历史施加量；已达到形态只前进、不自动回退 | Accepted；Hypothesis／NotRun | [用户选择](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[确认素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-023 | 对应法术正在持续释放且范围覆盖即提供环境转化条件；环境阶段末统一检查形态与转化，释放最后一刻有效，本次转化新元素下一刻自动作用 | Accepted；Hypothesis／NotRun | [用户选择](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[确认素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-024 | 环境转化产生新元素身份并继承当前对应层数；旧实例绑定与当次名单不自动转向新元素，后续条件选取仍可选新元素 | Accepted；Hypothesis／NotRun | [用户确认](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-025 | 环境转化归对应持续释放覆盖法杖，多杖后置优先；采用其生成特性及新元素固有属性，继承当前层数与小数衰减进度，不复制旧无关资源 | Accepted；Hypothesis／NotRun | [本轮确认](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-026 | 两种转化原地生成新元素，允许范围多同种；普通释放仍同种优先；仅合格环境占位物可转化，地面保留身份 | Accepted；Hypothesis／NotRun | 同上；两次原地替换与地面边界选择 |
| G002-CORE-027 | 异种补生采用对应持续释放覆盖与后置来源，合法邻近抵消亦可触发；正余量原地补生不重复加成，新状态衰减进度从零 | Accepted；Hypothesis／NotRun | [本轮选择](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |
| G002-CORE-028 | 环境阶段开始固定自动元素身份名单，失效跳过、中途新生下刻；转化检查沿R08公开顺序，状态资格独立沿ST02，旧身份名额不转移 | Accepted；Hypothesis／NotRun | [用户确认](../sources/inbox/2026-09-13-full-game-gdd-preparation.md)、[素材](../sources/materials/M-2026-09-13-first-release-content-scope.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-card-pool-rule-rulings.md) |

本轮未创建新GDD、未改代码或启动测试。原始库与历史实验保留；[26组写作前缺口](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/audits/pre-gdd-design-decisions-2026-09-13.md)中DG01–03已确认；DG06／07已确定当前量、形态保留、释放覆盖与环境阶段末检查；DG08身份及继承已闭合；DG09原地替换、地面边界及补生许可／来源已闭合；DG10阶段名单与顺序已收束；继续DG04／05范围与宿主资格。


## 2026-09-13：继续确认规则，批量采用既有推荐

| ID | 已采用范围 | 状态与证据 | 来源 |
| --- | --- | --- | --- |
| G002-CORE-029 | BR01–09：自身／宿主范围、阵营能力、正L与过程并存、公式结构、原动作与触发、2可换槽与激活、同组最强、疲劳执行、节点保存和同场开头锁定重播 | Accepted；Hypothesis／NotRun | [合格素材](../sources/materials/M-2026-09-13-pre-gdd-recommendation-batch.md)、[采纳文本](../history/accepted-design-records/D-2026-09-13-pre-gdd-recommendation-batch.md) |
| G002-SCOPE-004 | BR10–11：法术掉卡／产金首版后置，保留金币整体收益；共享词同实体、不加稀有度／隐藏调权；桌面鼠标键盘与功能信息要求 | Accepted范围；实际内容／平台发行／表现待补 | 同上 |
| G002-DOC-004（历史别名DOC-002／BR12） | BR12：实际内容、渠道及完整候选参数先成套，再写GDD；补表方向不能冒充表已完成，旧测试保留原输入身份 | Accepted／Documentation | 同上；用户本轮“继续确认规则，均按推荐处理” |

退出恢复另有用户明确答复“从本场开头恢复，全部锁定（推荐）”，并入BR09。IN-C和FAT-C只在BR明示范围内升级，旧候选数字不自动采纳。DG19、DG23本轮关闭，共10／26组关闭；其余组按[清单](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/audits/pre-gdd-design-decisions-2026-09-13.md)补实际规格。原库保留，未创建新GDD、未改代码或运行新玩法测试。

## 2026-09-14：火冰宿主资格

| ID | 已采用范围 | 状态与证据 | 来源 |
| --- | --- | --- | --- |
| G002-CORE-030 | HG01：玩家／敌人承载并兑现火冰攻防；树木／草地可持层参与形态、抵消与汲取但无生命／护甲；石地不接受；元素保持共享层数与抵消规则 | Accepted；Hypothesis／NotRun | [用户确认](../sources/inbox/2026-09-14-host-range-starting-content.md)、[合格素材](../sources/materials/M-2026-09-14-element-status-host-eligibility.md)、[采纳文本](../history/accepted-design-records/D-2026-09-14-element-status-host-eligibility.md) |

HG02／WG01／SG01为待审阵营、实际范围与起始资源推荐；[CG逐卡接口](../sources/inbox/2026-09-14-card-interface-completion.md)亦待审。HG01不代表这些新选择或全部DG05已经确定。当前仍10／26组关闭，继续实际内容及参数补齐。

## 2026-09-14：阵营、实际范围与起始资源

| ID | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- |
| G002-CORE-031 | HG02玩家／敌人／环境／创建元素／预设元素的阵营与固有属性；WG01三种固定法杖、10格锚点与裁边及角色范围；SG01起始4根原木杖、12张词卡、空可换槽、4出战上限及库存容量 | Accepted；Hypothesis／NotRun | [原问题与“确认”](../sources/inbox/2026-09-14-host-range-starting-content.md)、[合格素材](../sources/materials/M-2026-09-14-factions-wand-ranges-and-starting-loadout.md)、[采纳文本](../history/accepted-design-records/D-2026-09-14-factions-wand-ranges-and-starting-loadout.md) |

用户本次“确认”回应HG02／WG01／SG01成组推荐，HG01此前的单独采纳仍成立。DG04、DG05、DG17关闭，累计13／26；DG15补齐容量子项，货架与UX开战门槛待审。UX默认配置／跨战失效引用归DG24／25继续裁决，不作为DG17的资源未定项。原木杖额外出售留给RG-C01；PG／EG／RG／UX新数值和CG新接口不随本次升级。旧决策时点文字与候选完整保留，无新GDD或玩法测试。


## 2026-09-14：完成首版设计缺口（CORE-032–036）

用户原话：“确认。明确授权后续无需确认直接补齐”。CG按直接确认采用；PG／EG／RG／UX由agent在该授权内按既有推荐整包裁决，不逐项重问。首版范围保持S2 25项＋E3 30项，合并53实体；26组设计缺口全部已有具体条款、参数、例外和验证方法，状态Closed / Accepted。体验与平衡仍Hypothesis，新规则NotRun。

- G002-CORE-032：[首版卡池实体、角色、事件与效果组](../sources/materials/M-2026-09-14-card-interface-completion.md)。
- G002-CORE-033：[首版时间、公式、卡牌参数与获取渠道](../sources/materials/M-2026-09-14-first-release-parameters-and-channels.md)。
- G002-CORE-034：[首版环境形态、痕迹与转化阈值](../sources/materials/M-2026-09-14-environment-forms-and-thresholds.md)。
- G002-CORE-035：[首版完整路线、敌人、遭遇、成长与疲劳](../sources/materials/M-2026-09-14-run-route-encounters-and-fatigue.md)。
- G002-CORE-036：[首版玩家旅程、交互、保存与功能表现](../sources/materials/M-2026-09-14-interface-platform-and-experience.md)。

采用理由：让首版从实体构句、自动战斗、路线经济到保存与呈现形成可交接的完整规则。原始候选、旧数值与失败路径保留；素材门槛、提案、评估和拟修改已完成。[Proposal](../history/accepted-design-records/P-2026-09-14-complete-first-release-design.md)／[Evaluation](../history/accepted-design-records/E-2026-09-14-complete-first-release-design.md)／[Draft Change](../history/accepted-design-records/D-2026-09-14-complete-first-release-design.md)。规则存在反例或玩法验证失败时回到相应规则ID修订，不以旧实验结果覆盖RC1。先完成此采纳同步，再编写全游戏GDD Wiki。


## 2026-09-14：全游戏GDD Wiki交接（G002-DOC-003）

依据用户先收束设计缺口再写全游戏GDD的要求，以及后续无需确认直接补齐的授权，完成[全游戏GDD RC1](../design/GDD.md)，GDD-2 / Accepted。此文档及其Wiki正文为开发第一材料；有矛盾再查构思系统。68正式素材／47inbox逐项审查，53实体全表及12遭遇完整给出；旧素材、单项BF草案、早期卡池与历史证据保留。此次只整理已采纳规则，不启动新测试，不把规则采用或文档静态检查当作体验验证。

## 2026-09-23：主系统与探索区全量文档整理

| ID | 决定 | 状态与来源 |
| --- | --- | --- |
| G002-DOC-005 | 统一current规格、七系统职责、参数和内容来源；旧正文留历史，探索方向独立索引与比较，候选不自动回写；BR12修复为DOC-004 | Accepted / Documentation；用户明确开始全量整理；[Draft Change](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/sources/draft-changes/D-2026-09-23-document-organization.md) |

本次未新增CORE玩法决定。原26组选择已采纳；AUD-010保持Open。旧输入与两份已有素材删行未纳入本次修改。

## 2026-09-23：言咒项目独立目录（G002-DOC-006）

用户授权新建yanzhou并重新梳理物理目录，提交推送新分支。Accepted / Documentation / layout.1。主系统与优化分别映射，Project ID及资格/回写权限不变；旧路径保留兼容入口和明确冻结来源。未修改玩法、不解决AUD-010、不运行新玩法测试。[Draft Change](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/sources/draft-changes/D-2026-09-23-yanzhou-project-layout.md) · [目录规范](directory-layout.md)。


## 2026-09-24：探索按方向简化（G002-DOC-007）

Accepted / Documentation / layout.2。用户明确要求“exploration内部的结构也简化一下，以方向为单位能储存必要构思即可”。取消optimization包装层与活动区流程目录；27方向各用一个文件夹、README直接保存构思，比较及基线吸收合并到comparison。旧原始记录、合格材料、运行与固定包归入history/exploration-2026-09-24。原Candidate ID、局部资格和吸收边界保留；没有新CORE决定、没有新玩法验证，AUD-010保持Open。[Draft Change](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/sources/draft-changes/D-2026-09-24-simplify-exploration.md) · [报告](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/exploration-simplification-report.md)。


## 2026-09-24：核心设计浓缩与可选探索背景（G002-DOC-008）

Accepted / Documentation。用户要求补充GDD概括浓缩，并控制启动探索时阅读的游戏材料。新增[核心设计](../design/core-design.md)，保留core-concept为版本入口；新增[READ-1启动合同](../exploration/start.md)，支持CORE、固定GDD包、全量主系统文本、自选及空白。新方向默认CORE并先说明；旧方向续作沿原来源，切换需当轮明确要求。历史、其他方向与外部材料分别授权；实际文件、固定版本及覆盖直接记录在方向README。当前任务已读背景不能被抹除，须如实声明边界。

不新增CORE玩法决定，不修改现行参数、原候选资格或AUD-010。依据已提交GDD整理摘要，未启动玩法测试。[Draft Change](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/sources/draft-changes/D-2026-09-24-core-design-and-reading-modes.md)。


## 2026-09-30：四批清理与兼容目录退役（G002-DOC-009）

Accepted / Documentation / layout.3。用户明确要求“将前4批都一起进行，并且大胆清理history中的无用材料、完全删除旧兼容目录”。收束五个日常入口和操作规范，删除两套旧兼容目录；重复历史快照、迁移与机器审查附件改固定Git取证，独有探索证据与冻结背景保留。134个FX集中登记，18份已完成P/E/D归档，探索索引按近期记录/其余待选分组，不擅自改变资格或Parked状态。自动生成文件索引并检查活动链接。

未新增CORE决定，AUD-010仍Open；不运行玩法实验。未提交旧素材、视觉文件和临时产物逐字节备份到仓库外，不自动发布或合并为正式来源。[管理Draft Change](../sources/draft-changes/D-2026-09-30-document-cleanup.md) · [报告](cleanup-report.md)。

## 2026-10-01：时间产线正式基线（G002-CORE-037–047）

用户授权以新设计逐页检查并尝试正式化，且已答INT-01–13。决定逐项如下；全部为Accepted / Hypothesis / NotRun。

| ID | 已采纳范围 |
| --- | --- |
| G002-CORE-037 | A时间产线、自动运行与关键威胁应对、一杖一法术、有限队列、实际顺延、敌牌倒计时、固定每战费用及保存接口 |
| G002-CORE-038 | 卡牌主战场重做空间；只有明确打断效果中断指定法杖 |
| G002-CORE-039 | 重设计卡表，旧53实体不再作为新版发行池 |
| G002-CORE-040 | 恢复最近结清的一刻及已提交操作 |
| G002-CORE-041 | 材料—动作—目标；词卡与耗材分开 |
| G002-CORE-042 | 高阶产物维护不足休眠、保留增幅、补料自动恢复 |
| G002-CORE-043 | 无合法目标空放离队，不退制造成本、不补发 |
| G002-CORE-044 | 维护优先，再按战前杖序分料；入行同序，失败者等待 |
| G002-CORE-045 | 保留递增疲劳，参数与终局上界重定 |
| G002-CORE-046 | 允许部分资源和高阶产物跨战，拒绝全部清空 |
| G002-CORE-047 | 卡表标记可携带、基础环境料清空、共用容量与战后选择偏好；只留数量，增幅和运行状态重置 |

[Qualified来源、P/E及具体替换D](../sources/draft-changes/D-2026-10-01-timeline-production-core.md)。现行改为GDD-0 / 2.0；历史CORE-032的GDD-2属于RC1，不代表新结构仍完整就绪。完整同拍排序、新发行池与参数、托管战终归属及UI仍待审；干涉能力后续设计。本轮不启动玩法测试，也不把新候选数字一并采纳。

## 2026-10-01：兼容材料复用（G002-CORE-048）

Accepted / Hypothesis / NotRun。用户要求“将之前材料中不冲突且可以复用的部分合并，完善当前设计中，将对应表述更新确保兼容一致”。据此复核旧Qualified条款，将TL-26–37写入当前系统：实体词义、绑定与修饰；对象护甲与分阶段支付；战前可表达性；固定单向路线；本局库存／收益包／休整／商店；决策保存、可达性与参数来源合同。

己方目标选取适配到生效时，材料不是执行者，制造成本不因空放退款，携带选择与收益包分开。明确复用休整3选1及新局0金币，不恢复同名3张、旧开局、旧卡池、格子、旧冷却或参数。已揭示敌牌是否随来源死亡取消仍Unknown。此前INT-01–13与TL-01–25继续优先，具体干涉能力延期。

[复用记录](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)／[D](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)。本次只完善TL-1文档，修订reuse.1；成熟度仍GDD-0，没有新玩法测试。

## 2026-10-04：法器铭刻主系统采纳（G002-CORE-049）

Accepted / Hypothesis / NotRun。用户明确要求“将其回写到主系统中”，据DIR-036已确认结构与三项答复形成局部Qualified M/P/E及[D](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)，更新GDD 2.1 / TL-1 + INS-1、Core Concept v0.8 / CORE-SUM-3，仍GDD-0。

采用TL-38–45：法器统一产行动卡；暗句仅名词＋动词组合中的若干核心空缺，全部必填且核心不可打造；辅槽修饰可空、法器预设挂接、数量原则上不超过核心槽，可新增／解锁；材料类别绑定造物／制造内容；暗句确定行动类别、卡效独立；法器有核心铭文特别增幅，形式未定。

CORE-041的材料—动作—目标入口被替代，铭文实体占用与耗材分账保留。完整自由构句、任意修饰挂接与法器直接资源交付退出当前规则；效果目标、材料托管、有限队列、实际顺延、节点经济及保存边界兼容继承。高阶材料来源／加工Unknown，资源维护与携带只在内容明确提供时适用。

具体法器与卡池、卡效／制造映射、打造成本／时机／持久范围、契合形式与叠加不随之采纳；剑与盾之符为方向种子，模型例子仍候选。无新实验或实现证据，原方向Raw内容与原CORE背景版本保留。


## 2026-10-04探索方向退役（G002-DOC-010）

用户原话：“经我审查目前方向价值不高，部分测试、UI等低价值信息可以后续重做，开始执行删除”。据此删除DIR-001至DIR-036，清空活动方向与旧卡表／UI候选入口。只迁移DIR-028、036已采纳来源所需的六份M/P/E，修正活动引用；其余构思、独有失败路径、原确认和证据按固定Git取证，未提交字节先在仓库外校验备份。

状态：Accepted / Documentation；不改变CORE-037–049、GDD 2.1 / TL-1 + INS-1的采纳范围，不关闭TL／INS未决项，不启动或宣称新实验。外部实现仓库与既有冻结history未删除；新方向从DIR-037继续。逐项处理与恢复见[清理报告](cleanup-report.md#2026-10-04探索方向退役)及[清单](cleanup-map.json)。


## 2026-10-04主系统审查与旧版效果清理（G002-DOC-011）

用户要求：“阅读目前yanzhou主系统，我已完成版本大更新，检查矛盾模糊表述、清理落后版本、并检查目前系统中游戏设计的潜在弊病和不完善之处”。据此按固定输入审查现行规则及相关来源，订正INS-1输出／旧候选／版本导航等残留，将旧效果详细条目与三份旧审查改固定Git取证，保留137个身份与锚点、原资格、未选方案及失败路径。

状态：Accepted / Documentation。AUD-015–020为文档订正，AUD-021–030为Open设计风险；TL-Q11细化现有临时路由缺口。未新增CORE采纳，未选择REVIEW-Q1–6推荐，未改变GDD-0／Hypothesis／NotRun。原工作树8项删除和2项未跟踪内容不代为提交。详见[审查](conflict-register.md)及[清理报告](cleanup-report.md#2026-10-04主系统审查与旧版效果清理)。

## 2026-10-04：敌情与供料调度澄清（G002-CORE-050）

Accepted / Hypothesis / NotRun，局部修订routing.1。用户明确说明全部敌方行动牌延时生效；路由促使玩家将未来资源临时分配给攻击、防御、运转，牺牲下一轮积累换取防御；随后确认“先仅通过供料调整未来开工时间；额外调时能力待定（推荐）”。按[原话→Qualified M→E→D](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md)更新当前规则。

TL-09统一为全敌牌Δ＞0。TL-05／06／23／30细化CORE-044：战前法器序是基础分料顺序，未来未承诺批次允许临时调整供料去向及优先级；到期维护优先、已托管料和成品不改，同刻争入行仍沿战前法器序。规避指定打断先通过供料调整未来开工，不新增正在加工批次的暂停／改速能力。三端不固定物理口数；“5回合”是例子，不形成参数。

AUD-021／022修订为意图已澄清、实际窗口与可读性待验证。持续快攻导致拥堵可作为操作后果；用户第4项的“消耗费用调整牌序”只保留inbox Raw候选，未通过本次玩法资格或采纳。具体资源积累链、恢复触发／覆盖、卡表／时序／数值仍Unknown。无玩法实验，主版本及GDD-0不变。

## 2026-10-05：法器单一处理耗时与容量预留（G002-CORE-051）

Accepted / Hypothesis / NotRun，局部修订processing.1。用户先要求“简化处理法器生产与编排的耗时，仅设处理时间耗时，无生产周期冷却、无完工后等待；”，随后对S1-Q6–8回复“本批全部按推荐”。据[原话→Qualified M→E→D](../sources/draft-changes/D-2026-10-05-single-processing-time.md)限定回写。

唯一处理耗时D为至少1拍的整数；取消交付J、休歇R、独立生产周期／冷却和首次起点S。配置合法、完整材料和容量同时满足才开工，托管材料并预留本批所需入行位置；无位不开工，加工中也占容量，完工立即将预留转为行动卡入行，不滞留成品。免费供料调整不挪用既有预留。后续批次无独立冷却，仍需条件检查。

此次替代CORE-037相关生产时间与完工等待部分，局部调整CORE-044／050的完工容量争用前提；同拍实际入行处理仍沿战前法器序。新开工预留的争用顺序、预留是否固定牌序、中断释放与下一批启动阶段没有一并采纳。S1-Q1／5仍未回答，有限队列和每拍至多一张生效继续保留。

GDD仍2.1／GDD-0，核心v0.9／CORE-SUM-4；TL-V02／20原预期退出当前集，新增TL-V41–45，全部NotRun。无新发行实体、FX、实验或实现证据。

## 2026-10-05：生产预留、入行与临时供料接口（G002-CORE-052）

Accepted / Hypothesis / NotRun，局部修订processing.2。用户对紧邻的Q9、Q10、Q11、Q1、Q5推荐表回复“下一批全部按推荐”。按[原话→Qualified M→E→D](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)限定采纳，Q10的Q9容量预留前提成立，不重复询问。

预留只占容量，不预定未来牌序；实际入行后才进入正常队列，同拍入行沿战前法器序。维护先付，再按当前有效供料优先级依次联合检查完整材料和可用容量，默认战前法器序；条件齐备才托管、预留并开工，不足者本次跳过。中断结清解除该批预留，释放容量和退料最早下一拍复用，本拍不能再次分配。

入行后最早下一拍翻开，仍受正常队列及每拍至多一张限制，不保证下拍必定生效。临时供料只保留一份方案，玩家指定结束拍，到期分料前恢复基础方案；新方案替换旧方案，到期不恢复已替换的旧临时方案。托管、预留、已入行牌及已发生后果保持，不额外授予免费撤销、插队或当前加工改速权限。

本次补齐CORE-051／050的五项未知，保留唯一D、无冷却、无完工等待和严格早于T取消。完整同拍顺序、正常离队容量复用阶段、多牌内部关系、到期与新操作受理先后、维护内部顺序、实际内容与数值仍Unknown；不关闭整个TL-Q02／04／11。

GDD仍2.1／GDD-0，核心v0.10／CORE-SUM-5；新增TL-V46–52，现用59项预期全部NotRun。无新发行实体、FX、实验或实现证据。旧批次的未决记录按当时范围保留。

## 2026-10-05：阶段一共同拍序（G002-CORE-053）

Accepted / Hypothesis / NotRun，局部修订timing.1。用户对已列明S1-Q12／13／14回复“Q12–14全部按推荐”。按[原话→Qualified M→E→D](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md)限定回写，不重复询问，不将阶段推进授权扩大为未列明内容采纳。

每拍在行动结算与幸存完工后统一检查一次开工，a拍开工、a+D拍完工即入行；正常行动离队空位可用于本拍末开工，完工者可同拍续开。中断回收料与容量仍下拍可用；若有其他可用料及独立空位，被中断法器可本拍末重开，不增加整机冷却。T拍打断只作用当时正在处理的批次，不追溯影响本拍末新开工。

每拍先使上一拍待用资源／容量可用并恢复到期临时方案，再揭示敌牌与提供结算前观察／暂停／提交窗口；新方案结束拍>当前拍，用于本拍末，旧到期不抹去新方案，结算途中输入留下一窗口。不强制逐拍点击，UI自动暂停表现仍未定。基础补给也最早下拍可用，初始库存第0拍可用；第0拍先揭示观察再开工，D=1时0开工、1入行、最早2生效。

保留维护先于新分料、普通队列、严格提前取消、防护→伤害／打断→幸存完工及完整事件后终局停止；复杂总序、维护内部、多牌批次、敌牌失效和实际卡池／数值仍Unknown。四组主情境及四项边界已作文档复核，案例丙原入行历史已修正；临时数字和案例限制不升级为正式规则。

阶段一共同规则、预算、情境与未知归属交付完成，可以进入阶段二并与阶段三配套；阶段二内容尚未交付。GDD仍2.1／GDD-0，核心v0.11／CORE-SUM-6，新增TL-V53–60后现用67项预期全部NotRun。无新发行实体、FX、实验或实现证据；旧记录按原轮次保留。

## 2026-10-05：阶段二敌情合同与卡面种类（G002-CORE-054）

Accepted / Hypothesis / NotRun，局部修订enemy.1。用户在阶段二工作包中逐轮答复：通用组件与UI不地方化、卡面种类为攻击／防御／打断／其他、首版敌人用“秘仪与炼金”；“同一敌人不混用多地域意象；打断剩余时间最长的施法；来源敌人死亡后视为立即胜利”，两项释义选择“揭示时锁定该法器”“每场只有一个来源敌人”；随后对剩余推荐回复“本批全部按推荐”。按[原话→Qualified M→E→D](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)限定回写。

敌程序为固定循环时间表，开战即公开每张暗牌的位置、翻开拍与种类，内容仍翻开时公开。指定打断翻开时锁定剩余R＝a+D−r最大的施法所在法器（含R=0，并列取战前法器序靠前），无施法则无锁定对象；到期打断该法器当时的批次，无批次或目标消失即落空，不改选、不转为伤害。每场一个来源敌人，死亡即胜，未到期敌牌作废，附属物不计胜负；替代TL-13“敌人全灭判胜”，消解TL-29来源死亡Unknown。伤害与打断大类内本拍到期的敌方行动先于玩家行动。

行动卡敌我共用攻击▲／防御■／打断⊘／其他✱通用符号并配文字；地域牌组只改花色、配色、材质与装饰笔触。危险开工带与预计生效拍进入展示要求。内容合同新增首版约束（同一来源不同拍到期、首批无敌方防护、截击仅用于特色敌并保留反应路线），以及首版“秘仪与炼金”方向、世界观假设、取材范围与出处核实约束。绿狮、万溶之液、雷比斯为首批候选，不是发行内容。

仍Unknown：真实组件与数值、附属物、其他类子类、多地域融合、图谱页排版、复合效果与完整事件粒度、维护总序、意象出处核实。阶段二首批文档交付完成，下一步与阶段三配套。GDD仍2.1／GDD-0，核心v0.12／CORE-SUM-7，新增TL-V61–68后现用75项预期全部NotRun。无新发行实体、FX、实验或实现证据。
