# game-002 决策记录

> 文档角色：DecisionRecord。当前规格为[GDD 2.1 / TL-1 + INS-1](../design/README.md)，GDD-0 / Hypothesis / NotRun。历史Accepted记录保留原确认，不等于全文仍适用；现行替代关系以CORE-037–058及[素材审查](../design/source-review.md)为准。

现行结构由CORE-037–047建立、CORE-048限定复用、CORE-049采用铭刻入口；CORE-050补明未来供料调度，CORE-051改为单一处理耗时与开工预留，CORE-052／053补齐队列接口与共同拍序，CORE-054补齐敌情与终局，CORE-055采纳批次冻结与消费锁定，CORE-056补齐D公式；DOC-012—016重建系统框架，新增Qualified内容未自动晋为CORE采纳。其中CORE-041的配置入口和法器直接资源交付、旧J／R／S及完工等待均按各次范围替代。旧CORE-006的掉血全杖打断、CORE-011的对象边界及旧镶嵌设计顺序不能覆盖新版。编号别名见[登记](id-registry.md)。

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

阶段调整保留18词作为分类对象，上一批6刻元素／一次使用、冰冻减伤、一次掉卡、参数及逐刻记录均为Parked。已有基础执行规则、对象范围和数值重设计约束继续有效。本次未恢复这些具体方案，后续按[类型入口](../design/systems/inscription-system/rules.md)展开。

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
| G002-BF-001 | 2026-09-12 | 用户要求第一人称2×5、敌人居中、地面／环境物性、生成物占位及火焰导致树草燃烧／烧焦；明确树草不继续传播 | 用户方向与单项确认；完整规则Draft Change，未改核心 | [素材](../sources/materials/M-2026-09-12-first-person-grid-battlefield.md)、[GDD](../design/systems/resource-system/rules.md)、[拟修改](../sources/draft-changes/D-2026-09-12-first-person-grid-battlefield.md) |

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

<a id="g002-doc-012"></a>

## 2026-10-08：系统文件夹与规则、体验、设计分离（G002-DOC-012）

状态：Accepted / Documentation；仅文档结构决定，既有玩法采纳、Qualified 范围与 Hypothesis / NotRun 分别保留。

用户原话：“当前框架将确定好的硬性规则描述的较为清晰，接下来将每个系统单独设立为一个文件夹，把已确定的规则（通用框架大部分内容）、玩家体验相关（如未确定的机制—行为—体验假设）、设计相关（如可能频繁调整的设计定位、风格、理想效果等）隔离为不同文件。然后以辅槽系统为例重写”。

SYS-001—007 移入各自同名目录，README 导航、rules 维护规则、experience 维护体验假设、design 维护定位与待定方案。211 个原正文段落逐段分配；原编号和独有失败路径保留。辅槽以已确认通用框架重写，不另增 SYS 编号、不发行具体卡效、不执行玩法实验。可调整的设计内容仍须区分已确认方向与候选。

本轮采用 CUSTOM：七系统正文、辅槽允许材料、目录与治理规范；其他活动文档只处理链接元数据。原文基准为 `ff7e533cc4090292869477b686775cc34f4d9294`；历史快照与原始阅读 manifest 不刷新。未提交辅槽三原件已本地保全，记录见 [原输入保全](../sources/inbox/2026-10-08-augment-framework-review.md#文档拆分与原输入保全)。

入口：[系统目录](../design/systems/README.md)、[辅槽示例](../design/systems/inscription-system/augment-system/README.md)、[分文件职责](document-contract.md#系统文件夹与分文件职责)。GDD 阅读包随文件拆分更新为 33 份明确正文；读取资格不等于采纳。

静态检查：七系统的 44 个 TL 条款标题与原文实质句均保留，变更文件中的 1858 个本地链接无缺失，33 份阅读文件存在，三原件备份哈希一致。玩法验证未运行。

<a id="g002-doc-013"></a>

## 2026-10-08：六个主系统目录与空白通用框架（G002-DOC-013）

状态：Accepted / Documentation；不新增玩法采纳或验证结论。

用户原话：“重新给一版系统目录；应当包括法器系统、铭文系统（包含辅槽）、行动卡系统（标记系统）、敌人系统、资源系统和局外成长系统（尚未开发），并给一个空白的通用框架模板”。

现用主目录调整为法器、铭文、行动卡、敌人、资源、局外成长；辅槽归铭文、标记归行动卡。局外成长仅占位，范围和具体机制保持 Unknown，不将既有局内奖励、跨战携带或商店自动视为局外成长。标记本轮只建立阶段成果整理入口，不把它标为未开发，也不自动采纳全部细则。

既有路线、局内经济、交互与保存移到公共流程／合同。条款重归属：TL-01／44 归行动卡；TL-45 归法器；TL-42 归铭文；TL-16 与遭遇字段归敌人；TL-32 留局内路线。其他规则和所有旧 SYS／TL 身份保留，不重新使用编号。规则、体验、设计仍分文件维护。

本轮 CUSTOM 范围为现有系统正文、目录与模板规范；其他活动文档仅修复链接元数据。基准提交 `8f4722017ca586042bae98a2cb64d9b1f017892c`。原始阅读清单、历史快照和未提交阶段输入不刷新；已有用户修改单独保留。

交付：[六系统目录](../design/systems/README.md)、[公共流程](../design/common/README.md)、[空白模板](../../game-design-workflow/templates/system-framework/README.md)。模板以四文件包登记到共享模板清单，不预填项目规则。GDD 固定阅读包按新位置登记为 42 份，含明确标识的入口／占位正文。

静态检查：六个主目录、两个子目录及四文件模板齐全；44 个 TL 条款各保留一处正文，原实质内容保留；1974 个本地链接无缺失，42 份阅读文件存在。规则与体验均未新增实验结果。


<a id="g002-doc-014"></a>

## 2026-10-08：行动卡框架初填与示例独立文件（G002-DOC-014）

状态：Accepted / Documentation；仅文档组织决定。行动／标记通用结构仍标 Qualified／用户已确认，继承 TL 仍 Accepted，体验与平衡 NotRun。

用户要求结合旧版本、主要参考指定行动卡与标记文件开始填写行动卡系统，并在规范中新增独立示例文件。各系统、子系统及公共流程统一 README、rules、experience、design、examples 五文件；已有法器、资源、行动、辅槽示例迁出，未有示例的目录明确留空，局外成长继续尚未开发。

本轮 CUSTOM 范围、固定提交／输入哈希、主材料确认和 ACT-Q1／2 答复见 [来源记录](../sources/inbox/2026-10-08-action-card-framework-review.md)。用户确认：行动结算后独立登记未来标记，预告不占行动队列或额外翻牌；行动可读取并支付标记，完整检查成功才扣，失败不部分支付。这些结构经 [局部 Qualified 素材](../sources/materials/M-2026-10-08-action-card-framework.md)进入框架，未将 Raw 卡池、推荐数值或详细排序一起纳入。

旧规则与失败路径保留；内容合同中仍写“来源死亡未决”的过期摘要按已经采纳的 CORE-054 纠正。没有新发行内容、P／E／D、运行测试或实现证据。未决同拍时序、复合步骤、上限与生命周期等集中在设计页。

[文档规范](document-contract.md#系统文件夹与分文件职责)、[空白模板](../../game-design-workflow/templates/system-framework/README.md)、[行动卡入口](../design/systems/action-card-system/README.md)已同步。GDD 固定阅读包为 53 份；示例提供说明，不提高来源采纳或证据状态。

静态核对：11 个系统／子系统／公共流程目录及空白模板均有五文件；44 个既有 TL 条款各保留一处正文，137 段继承规则实质内容在规则或迁出示例中保留；本轮文件的 1224 个本地链接无缺失，新链接锚点可达，53 份阅读文件存在。三个未提交输入原件哈希未变。上述均为文档检查，不是玩法验证。

<a id="g002-doc-015"></a>

## 2026-10-08：法器系统框架整理（G002-DOC-015）

状态：Accepted / Documentation；依据用户“阅读此交接文档，整理法器系统相关内容”。沿 DOC-013／014 的既有目录与五文件职责，不变更 CORE 玩法采纳。

本轮 CUSTOM 基准 `71e7a0a18709e19e85ea171feb10b2ba2b432097`，实际输入与覆盖见 [来源记录](../sources/inbox/2026-10-08-artifact-framework-review.md)。法器 TL-03—07／38／45 保留 Accepted；已有辅槽及行动／标记素材以 Qualified 接口引用，不借整理升级。定位、设计取舍与未决接口归 design，体验因果与观察方式归 experience，六条短例展开并补充失败边界归 examples；导航补状态与相邻职责。

未提交 Raw 原件保留；减料、单批增产、虚拟供料、压缩预留及未确认具体效果不纳入法器框架。D 修饰的确定与叠加、标记失败／退款、共享状态总序、契合形式及内容参数仍未决，推荐分组保存在设计页，不当作用户答复。没有新 M／P／E／D、发行内容、运行实验或实现证据。

结构仍为 11 个五文件目录，GDD 固定阅读包仍为 53 份；未因本轮内容整理扩大阅读或创建第二套正文。交付入口：[法器系统](../design/systems/artifact-system/README.md)。

静态核对：11 个本任务文件中的 321 个本地链接可达，64 个新增链接及其中 32 个锚点有效；44 个 TL 身份各保留一处声明，法器原有 63 个条款句片段及状态表行保留在规则或迁出情境中，原六例覆盖已逐项对照。11 个五文件目录、空白模板及 53 份阅读文件存在，两个实际读取的未提交原件 SHA-256 未变。仅检查文档，玩法与体验均 NotRun。

<a id="g002-doc-016"></a>

## 2026-10-08：敌人系统框架整理（G002-DOC-016）

2026-10-11引用辨识：若从铭文／辅槽的原分支来源跳到本锚点，其原DOC-016应按[DOC-018映射](#g002-doc-018)解释；本条仍专指敌人整理。

状态：Accepted / Documentation；依据用户“阅读此交接文档，整理敌人系统相关内容”。沿现有五文件职责，未新增 CORE 玩法采纳或阶段工作。

固定输入 `a23c75d74187f45f04b50376658be0274049f3f8`，本轮 CUSTOM 覆盖、来源版本与局部原件哈希见 [敌人来源记录](../sources/inbox/2026-10-08-enemy-framework-review.md)。保留 TL-16 与 CORE-054 原 Accepted；将遭遇内容页的通用字段、首版限制和窗口条件归敌人 rules，压力取舍、已确认秘仪炼金方向及未定表现归 design，原体验目标展开为假设和观察方式，补六组独立规则示例。内容页原章节保留链接，具体候选表及数字不变。

标记只引用已有 Qualified 宿主／极性与预告边界，未开放改延迟、提前取消暗牌、任意事件链或敌方制造成本。首批敌人仍为候选，数值 Illustrative；完整参数、同拍复合、附属物、定时绑定与表现布局继续 Unknown。没有新 M／P／E／D、发行内容、实验或实现证据。

入口：[敌人系统](../design/systems/enemy-system/README.md)。11 个五文件目录与 GDD 固定阅读包 53 份的结构不变，文档职责与条款身份不变；其他人的未提交修改和原始输入保持原样。

静态核对：13 个本任务文件中的 398 个本地链接可达，94 个新增本地链接及其中 47 个锚点有效；44 个 TL 身份各保留一处声明，原 TL-16 及失败路径逐字保留，首批候选表与后续扩展处置未改。11 个五文件目录、空白模板和 53 份 GDD 阅读文件存在，五份实际局部读取的未提交原件 SHA-256 未变。其他既有未提交修改保持原样；检查仅覆盖文档，运行与体验均 NotRun。

<a id="g002-doc-017"></a>

## 2026-10-08：主系统重建后审查与旧表述清理（G002-DOC-017）

状态：Accepted / Documentation。用户要求阅读目前主系统，检查矛盾与模糊表述、清理落后版本并审查设计弊病。固定输入`cb8c8b2376cfe217e6d65a128d0fbf9909f83edb`，CUSTOM，完整69份已提交design及相关来源／入口；逐文件版本与实际阅读深度见cleanup-map的`main_system_audit_20261008`。

按CORE-051—054订正已解决接口仍写Unknown的残留、75项验收计数、打造链接与符号含义；当前入口改为阶段1—4完成后的框架核对。旧冲突记录加版本提示、原细节保留；过期长文件索引改职责导航，原路径清单按固定Git取证。AUD-031—033为文档订正，AUD-034—040为Open风险；旧AUD-021—030按新版本逐项复核，不把已解决规则重问或把残余风险全部关闭。

没有新增玩法采纳、发行、模型模拟或玩家测试。标记支付／定时、D快照及恢复等仅列待核对建议；用户原有删除、新草稿与AUD-021标题修改未并入本轮提交。交付见[审查报告](main-system-review-2026-10-08.md)、[当前问题](questions.md#重建后接口核对2026-10-08)及[清理记录](cleanup-report.md#2026-10-08主系统重建后审查)。

<a id="g002-core-055"></a>

## 2026-10-08：批次冻结、消费预警与玩家锁定（G002-CORE-055）

状态：Accepted / commitment.1；体验Hypothesis / NotRun。用户先明确保留开工D冻结、应付标记不被其他行动消费、下一轮消费预警及玩家锁定；随后对紧邻FZ-Q1—5回复“都按推荐”。[原话](../sources/inbox/2026-10-08-batch-freeze-consumption-lock.md#本批确认与晋级)／[M](../sources/materials/M-2026-10-08-batch-freeze-consumption-lock.md)／[E](../sources/evaluations/E-2026-10-08-batch-freeze-consumption-lock.md)／[D](../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md)。

确定开工冻结D及本批应付标记，完工扣除；冻结量不供其他支付或条件读取，打断释放下拍可用。玩家可锁定自有未承诺的指定数量，约束所有自动消费者至主动解锁，不撤回承诺或阻止伤害／自然失效。下一批开工前可操作窗口显示预计消耗和锁定后果、随条件更新、不逐批确认。必需不足等待，明示可选且允许回退才基础继续。一般行动生效侧支付不延期。

核心v0.13／CORE-SUM-8，GDD仍2.1／GDD-0；现用44个TL、83项NotRun预期（新增TL-V69—76）、137个FX不变。只局部采纳上述接口，其他Qualified框架不升级；时间公式、完整总序、冻结量上限／失效／战终、其他阶段退款与完整定时保存待定。无发行内容、玩法实验或实现结果；保留原有未提交修改。

本轮静态核对：84份Markdown的1,260处本地链接及174处锚点引用有效，新增56处本地链接无错误，32个固定Git对象可取证；44个TL、83项NotRun预期与137个FX身份无重号或缺漏，11个五文件目录及53份GDD包齐全。20条原有未提交路径逐项哈希／删除状态不变；没有运行玩法实验。

<a id="g002-core-056"></a>

## 2026-10-08：处理耗时公式（G002-CORE-056）

Accepted / time-formula.1，Hypothesis / NotRun。用户先授权“该公式逻辑你直接选定一种前后一致的规则即可”，后明确“既然杀戮尖塔也采用连乘，那就按照他的逻辑为最终参考”。[原话](../sources/inbox/2026-10-08-processing-time-formula.md)／[M](../sources/materials/M-2026-10-08-processing-time-formula.md)／[E](../sources/evaluations/E-2026-10-08-processing-time-formula.md)／[D](../sources/draft-changes/D-2026-10-08-processing-time-formula.md)。

法器TL-03采用固定增减后有效倍率连乘、最后一次向上取整并最低1拍；每个效果先按层数／覆盖／并存声明形成贡献，同快照计算，不读中间结果或按来源类别重复叠乘。已启用且条件成立的付费效果照常按声明冻结／扣除，不因取整无收益自动免单；预告显示最终D及费用。保留CORE-055本批冻结和完整条件检查，普通量值公式不变。

本地参考实际为SlayTheSpire2恢复工程，关键文件未跟踪，以哈希和只读范围标识；外部事实与言咒适配分开，不宣称正式版本全量验证。百分比合并加算方案未采纳。核心v0.14／CORE-SUM-9，GDD仍2.1／GDD-0，44条TL与137个FX不变，新增TL-V77—82后当前89项NotRun预期；无新发行内容、实现或玩法实验。真实数值、同类叠层映射、同拍总序和生命周期继续未决。

静态核对：85份Markdown、1,285处本地链接与177处锚点引用有效，新增42处本地链接无错误；32个固定Git对象、44个TL、89项NotRun预期、137个FX及53份GDD包完整。10个精确算术例和6种倍率排列结果符合所写公式；这仅检查算式，不是对局或实现测试。5份本地参考源文件哈希未变，20条原有未提交路径保持原状态。

<a id="g002-core-057"></a>

## 2026-10-08：同拍结算与事件边界（G002-CORE-057）

Accepted / timing.2，Hypothesis / NotRun。用户“结合言咒设计确认前后一致的规则”，承接本地参考研究直接选定。[原话](../sources/inbox/2026-10-08-settlement-order-reference.md#本轮直接选定与采纳)／[M](../sources/materials/M-2026-10-08-settlement-order-reference.md)／[E](../sources/evaluations/E-2026-10-08-settlement-order-reference.md)／[D](../sources/draft-changes/D-2026-10-08-settlement-order-reference.md)。具体排序为Codex在授权范围内的言咒适配，不伪造用户逐项答复或外部原规则。

保留五主阶段、既有防护及敌方优先。每组定时→敌方→玩家；复合牌按效果分组，不逆越依赖，多击逐击结清；主结果及一层合法反应、死亡清理之后检查终局。定时最早下拍、结束拍不含兑现，默认绑定宿主独立登记；维护→旧休眠恢复→统一开工；即时标记供后续步骤、新资源／退款仍下拍；冻结失效不补扣不重算D、打断不复活。保存步骤、名单、登记序和支付／维护状态。

核心v0.15／CORE-SUM-10，GDD仍2.1／GDD-0，44条TL和137个FX不变，新增TL-V83—96后103项NotRun预期。通用总序闭合不开放新卡、递归触发或首版敌方防护／同拍多牌内容。上限／刷新／周期预算、托管维护、附属物、批次内部关系与跨战归属继续未决；无玩法运行、实现或玩家体验证据。

静态核对：84份Markdown中的1,347处本地链接、187处锚点及32个固定Git对象可达；44个TL、103项NotRun预期、137个FX、11个五文件目录和53份GDD包完整。20条原有未提交路径的哈希／删除状态保持不变。仅文档一致性与条件推导核对，未执行玩法测试。

<a id="g002-core-058"></a>

## 2026-10-09：资源设计、材料分级与背包（G002-CORE-058）

Accepted / resource.1；体验Hypothesis / NotRun。用户在资源设计与R1—R20确认之后要求“更新到主系统中”。[原话](../sources/inbox/2026-10-08-resource-design-intent.md)／[M](../sources/materials/M-2026-10-08-resource-design-intent.md)／[E](../sources/evaluations/E-2026-10-08-resource-design-intent.md)／[D](../sources/draft-changes/D-2026-10-09-resource-system-design.md)。固定输入`54ad7597145127922759be7840c5d4d30ea786e1`，定向复核受影响正文，未使用他人未提交材料。

采纳核心约束、产出积累和环境表达；固有基础加工仍付材料、D与行动队列；材料身份／性质／阶级、多阶量值和效果差异及指定阶级等待；背包限种类与容量，战前投入、战后统一选留、身份阶级保留；普通耗材未完工战终退回、已完工不退；常态自动运行、公开基础取材与可错过发现。同步核心必填的铭刻适用域、用途／阶级选择与承诺、辅槽协同措辞及保存语义。

核心v0.16／CORE-SUM-11，GDD仍2.1／GDD-0。44个TL身份不变，新增TL-V97—106后113项预期均NotRun。具体流派、配方、各阶效果和参数、复杂分料、特殊对象合同延期，其他Qualified框架不整体升级；无新卡池、玩法测试或实现证据。

<a id="g002-doc-018"></a>

## 2026-10-11：跨分支铭文整理编号映射（G002-DOC-018）

Documentation。`51257ba5e00b0cae155940c11251134dffd6db69`中2026-10-08“铭文及辅槽系统框架整理”原使用DOC-016，与当前已登记的敌人整理重号。当前引用该铭文整理时唯一映射为DOC-018；敌人仍为DOC-016，原固定提交／来源不改号。此项只解决身份冲突，不代表完整合并该分支或新增玩法采纳。

<a id="g002-doc-019"></a>

## 2026-10-11：系统设计指导集成与一致性复核（G002-DOC-019）

Accepted / Documentation，依据用户直接要求按新指导更新各系统、检查冲突和设计缺口，以及“以本次附件和当前仓库为准”。输入和处置见[本轮审查](main-system-review-2026-10-11.md)。

从固定提交汇入法器、铭文／辅槽、行动卡的设计意图与原始确认记录，保留Qualified；更新六主系统、两个子系统及三个公共流程的设计／体验，订正已被CORE-055—058替代的Unknown与关联示例，补GDD带状态摘要和来源导航。附件不作为额外指令；战中重铭、手动逐卡选择、简化截止、旧符号、默认打造与标记上限等误导表达不纳入现行规则。

规则仍CORE-058，GDD 2.1／GDD-0、核心v0.16、44个TL、113项NotRun预期不变；没有新发行内容、原型、玩法测试或体验证据。旧来源、独有失败路径和用户原有工作树修改保留；当前剩余问题在questions，报告记录风险条件和下一步，不重复资格确认或自动采纳建议。

<a id="g002-core-059"></a>

## 2026-10-11：首批案例与固定用途（G002-CORE-059）

Accepted / first-example.1。用户“可以无材料”“三项均按推荐”与要求加入example，采纳[限定D](../sources/draft-changes/D-2026-10-11-simple-spell-example.md)：明示零材料配方；同一合法铭刻的有限固定用途只影响未来批次；两护符兼容迅速、一实体一处；EX-001暂不启用候选契合。具体数值只固定该案例。无单法器暂停、战中重铭或全局参数采纳。

核心v0.17／CORE-SUM-12，GDD 2.2／GDD-0，44个TL身份保持；新增TL-V107—110后共117项NotRun预期。案例与静态账目不证明玩法和体验。

<a id="g002-doc-020"></a>

## 2026-10-11：主系统开发阅读整理（G002-DOC-020）

Accepted / Documentation。用户明确要求UI／实装前彻底整理简化、集中问题并加入首批案例。主阅读线改为简短GDD→权威规则→EX-001；各系统设计／体验压缩为职责、取舍和观察信号；未决统一questions，版本来源集中baseline，独有历史解释按固定Git保留。具体规则、失败路径及保存义务保留；清理映射见cleanup-report。

保留11个五文件目录，新增跨系统examples两文件并把固定GDD阅读包从53增为55；EX身份独立于发行卡、FX和TL。未改用户原有未提交材料，不运行实现或玩法测试。

<a id="g002-doc-021"></a>

## 2026-10-11：正式开发准备（G002-DOC-021）

Accepted / Documentation。用户说明“设计界面已经完成”，要求开发前整理主系统与资产、制订规范和阶段目标；随后明确引擎尚未确定，考虑Unity和Godot，把评估加入计划。建立[开发规范](../development/development-standard.md)、[阶段计划](../development/production-plan.md)及[资产接入](../development/asset-readiness.md)，同步主系统／视觉／开发入口和TL-Q08当前范围。

开发视觉沿HTML v10、效果图v01、组件v01及Blender v02，原件不动；5包75文件校验一致。规则／EX-001内容未改，不新增CORE／TL／FX或发行身份，GDD仍2.2／GDD-0，117项预期NotRun。Unity／Godot待同题实测后选择，本轮不决定引擎或创建实现仓库，不运行玩法实验。旧交付证据和22条用户已有工作树路径保留。

<a id="g002-doc-022"></a>

## 2026-10-11：Godot选型与首版工程（G002-DOC-022）

Accepted / Development。用户先授权“开始实测”，许可澄清时选择“先完成Godot，Unity暂缓”，随后明确“直接确定使用godot”。据此采用Godot唯一工程，替代DOC-021原双引擎比较流程。Unity未实测，不以调研或Godot结果伪造比较优势。

唯一实现入口[E:/Project/yanzhou-godot](E:/Project/yanzhou-godot/README.md)，工具冻结、技术ADR、代码／构建和测量留该仓库。开发计划和索引记录[首版交付及未验范围](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/godot-start-2026-10-11.md)，新Demo登记为DM-G002-011，实际导入AS-G002-010@BATTLE-3D-02。

本轮检查EX-001 0—14拍、输入、拍末恢复与导入／打包，不修改规则或案例数值；原型按钮、两件模型与逻辑对象映射及占位卡面只用于实装核对，不补TL-Q08设计决定。GDD仍2.2／GDD-0，完整117项验收、完整单战、真人体验及平衡继续未完成，其他阶段不因此整体标完成。

<a id="g002-doc-023"></a>

## 2026-10-11：成品Demo任务分解（G002-DOC-023）

Accepted / Documentation。用户说明第一阶段已完成、目前只有基本逻辑，要求将画面表现、资产运用、物体动作、UI等按最终成品质量细分为HTML任务表。依据当前开发计划、资产接入、EX-001、Godot首版交付及实现仓库验证报告/真实截图，建立[成品任务表](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/demo-quality-taskboard.html)：52项必做覆盖范围与合同、运行美术、正式UI、动作音画、完整单战、体验与质量收束、离线包验收与接手；4项后续扩展不计成品完成率。

本次规划交付单元为可完整游玩的一场高完成度战斗Demo，沿既定视觉和首批内容；路线/商店等沿原P4/P5后续推进。表中待决引用原questions，技术任务与Bug留Godot仓库，不新增规则正文。建议性能预算和体验验证样本为任务准备建议，须执行时冻结；真人体验验证需对应实验任务授权，本轮未执行。

HTML提供领域/阶段/状态筛选、依赖跳转、展开详情、本地进度、JSON备份/导入、CSV导出和打印；本地状态不等于正式采纳或实现验收。新增任务默认待开始，并逐项说明原有底座；已有28项规则检查、原型输入和拍末恢复仍仅在原范围成立。不运行/修改游戏、源资产或案例，不更改P0—P5原实现结论。

页面与任务数据的实际检查见[检查记录](../development/reports/demo-quality-taskboard-checks-2026-10-11.json)：浏览器显示、筛选/展开、本地保存重载、CSV和JSON导出/导入，以及任务依赖核对；file协议直开因浏览器策略未自动验证，打印输出未验。22条原有工作树路径保持不变。

<a id="g002-doc-024"></a>

## 2026-10-11：开发设计裁决与专人对接（G002-DOC-024）

Accepted / DevelopmentPolicy。用户明确要求：“开发过程中如果遇到需要裁决的设计问题则暂停，交由专门的设计对接agent进行一轮解决后继续。”据此新增[开发规范第8节](../development/development-standard.md#8-设计裁决闸门)，并在AGC-1与项目AGENTS建立路由。

设计裁决触发当前开发批次暂停；专人查已有答案、准备方案、需要时批量交用户选择。总控核对回传、必要资格／采纳与权威记录后恢复；一轮结束但仍有Unknown或待裁决，继续暂停。纯工程缺口不单独触发裁决。此管理决定不采纳新玩法、修改EX-001或授权实验。

触发时核对结论：TL-Q08剩余操作合同及TL-Q07完整单战／疲劳参数需要一轮设计解决；此前两项用户确认保持，不重问。FB-Q01按已冻结范围延期，不自动加入主动启停。复用聊天 `01a12de2-58a7-76f3-bc2a-21bde665161b` 为“言咒设计对接”，继续使用GPT-6.1-sol；开发下一批曾暂停。后续用户已确认及CORE-060集成见下条，恢复状态见[总控记录](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demo-control-2026-10-11.md)。

<a id="g002-core-060"></a>

## 2026-10-11：首场操作合同与完整单战（G002-CORE-060）

Accepted / battle-demo.1。专门设计对接提出R1—R3完整推荐，用户直接回复“本批按推荐”，包括原案第1／2节逐项条件；总控已核实该userMessage（`01a12e19-99da-74e1-9a4b-3f7db737da2c`）。[原案](../sources/inbox/2026-10-11-development-design-round-01.md)→[Qualified M](../sources/materials/M-2026-10-11-development-design-round-01.md)→[限定E](../sources/evaluations/E-2026-10-11-development-design-round-01.md)→[D](../sources/draft-changes/D-2026-10-11-development-design-round-01.md)。

R1／R2写入交互rules：第0拍观察暂停后自动，2秒与三倍速、前半观察、打断停默认开／攻击停关、单步到下一观察；回看／详情暂停、归位不播放、焦点／数量／数字／键位完整。R3新增EX-002：沿固定首批配置与L16，16拍起每4拍双方损耗5×n，限定恢复与初始化；静态胜20／双亡败24，原EX-001不改。三个替代未采纳。

CORE-060／核心v0.18／GDD2.3仍GDD-0，不增加TL身份，不升级实现或体验证据。TL-Q08仅本场闭合，TL-Q07仅EX-002闭合，主动启停和其他扩展延期。总控按DOC-024复核来源、规则与输入版本后恢复既定开发；新设计取舍再交专人，不重问本轮答复。

<a id="g002-core-061"></a>

## 2026-10-12：首场表现与声音合同（G002-CORE-061）

Accepted / battle-presentation.1。用户在专门设计对接直接选择R4—R6全部推荐，总控核实userMessage `01a12e7c-27db-7fb0-b624-ba794708eb8a`。来源及Qualified／E／D见[采纳记录](../sources/draft-changes/D-2026-10-12-development-design-round-03.md)。合法暂停停点取消未完瞬态并归位，单步立即到下一观察配有序静态摘要；载入不重播旧音画，暂停截停战斗声且不续播、暂停环境循环，明确继续恢复环境，允许新UI声，退出清场。

核心v0.19／CORE-SUM-14、GDD2.4仍GDD-0；CORE-060、EX-001／002规则参数不变，其他替代未采用。总控完成权威集成后恢复第五批；音画运行、听感与真人可读性NotRun，新设计冲突仍按DOC-024处理。

### CORE-061第04轮限定解释（2026-10-12）

[第04轮来源核对](../sources/inbox/2026-10-12-development-design-round-04.md)为Derived clarification，不新增CORE身份或用户选择。新观察清上一拍滞后，未暂停的新揭示可给一次非阻塞提示；自动暂停、单步和新终局没有战斗音画例外，旧局不重播，不能用UI命名规避。音效资源清单不覆盖Accepted暂停政策，胜败音资源本场未启用。总控复核并同步现行交互规则后恢复第五批，无需重问R4—R6。

<a id="g002-core-062"></a>

## 2026-10-12：首场主窗口失焦与返回合同（G002-CORE-062）

Accepted / battle-focus.1。用户在专门设计对接选择R7-A，总控核实userMessage `01a12eb3-3dee-73e2-9b75-f1378382e519`。主窗口OS失焦／最小化请求合法完整事件边界暂停，返回仍停并明确继续；保留批次、队列、已提交输入、回看、弹层及同进程草稿，音画沿CORE-061，不补后台时间。显示试用恢复独立于战斗预算。来源与Qualified／E／D见[采纳记录](../sources/draft-changes/D-2026-10-12-development-design-round-05.md)。

核心v0.20／CORE-SUM-15、GDD2.5仍GDD-0，TL身份、R1—R6、CORE-061第04轮解释与案例数值不变。后台继续／返回自动继续未采用；失焦运行适配与体验NotRun。总控完成静态复核与固定输入后恢复第六批，新设计取舍仍按DOC-024交专人，不重问R7。

## 2026-10-12：桌面3D主交互（G002-CORE-063）

Accepted / physical-table.1。总控直接读取方向消息 `01a12f52-8c23-7161-a12f-f98cea96a554` 与设计对接答复 `01a12f60-c246-7581-84dd-c7ece4a242e4`；R8保持自动推进，R9采用用户修正：主页面全部操作入口为真实3D物件，点击暂停近观说明和系统界面才可独立成页且须图形化，删除纯文字UI，必要精确信息保留。来源、Qualified／E／D见[采纳记录](../sources/draft-changes/D-2026-10-12-development-design-round-07.md)。

真实卡片表现入列、合法揭示／使用、目标结果与离场；玩家已知牌不重新揭密，敌牌r与T分开，动画不驱动支付或推进。暂停／单步／载入沿CORE-060—062静态末态，书和晶球仍为布景。核心v0.21／CORE-SUM-16、GDD2.6仍GDD-0，案例数值不变，制作参数未逐项采纳；新3D运行和体验NotRun。

## 2026-10-12：重点交互四阶段制作（G002-DOC-025）

Accepted / DevelopmentPolicy。用户直接消息 `01a12f65-1b8e-7192-97ed-eb246bc10f65` 要求复用后端、重做交互表现，并由设计agent对每项重点交互依次完成文字结构、HTML示意、美术效果示意、真实实现。总控已读原消息核实，纳入[开发规范第9节](../development/development-standard.md#9-每项重点交互的四阶段制作)。

各阶段有可查看产物及复核，设计agent负责连续性，总控负责集成和恢复。复用既有DQ表，不把全局效果图或旧HUD技术验收当作全部重点交互完成；不新增逐页审批、玩法或实验授权。第07轮裁决闭合后先推进设计制作，真实实现仍须前三阶段及具体恢复记录。

### 2026-10-14：CORE-063 展示修订 physical-table.2

依据[本聊天用户原话与继续制作授权](../sources/inbox/2026-10-14-demoncards-presentation.md)及原D的[三阶段交付](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/demoncards-reference-2026-10-14/design-review-v01.md)，总控完成[M／P／E／D来源链](../sources/draft-changes/D-2026-10-14-demoncards-presentation.md)。必要名称／精确值／公开状态允许绑定3D物件的精简只读容器与悬停／键盘短提示；提示不暂停、不提交、不揭示。静态近观、原位Completion／Use、公开信息、消费锁与暂停继续有效；未暂停的新公开事实可作同身份r→T展示转位，不改真实队序或结算。

沿用CORE-063，无新玩法编号；尺寸／材质／时长为本轮可逆制作参数。Demoncards作为第一表现参照，新Godot视觉／动作／输入／用户接受分别取证；来源资格和制作授权不证明体验成立。

<a id="g002-doc-026"></a>

## 2026-10-18：设计开发规范与工作台收束（G002-DOC-026）

Accepted / Documentation and DevelopmentPolicy。用户要求在新的2D实现前，分别整理主系统、开发状态、工作台、工作流程和开发解释，并先确立规范体系。[本轮原话及Q1—Q3直接答复](../sources/inbox/2026-10-18-development-system-review.md)确认：2D是同一游戏的新表现方向，保留3D工程与证据；先闭合首场主动调度、积累兑现、首批内容与完整战斗输入；小循环按变化裁剪，复用已确认产物，工具调研按缺口触发。

[开发规范](../development/development-standard.md)作为规范总入口，新增[小循环规格](../development/iteration-spec.md)与[工作台展示规格](../development/workbench-spec.md)；[开发解释](../development/development-guide.md)说明每次交付的阶段与能力。当前进度统一在开发README，阶段计划只维护依赖／退出条件，开放问题只在questions；工作台保存展示与原文入口，执行合同不代替验收状态。新重点交互继续具备文字、HTML、美术和真实实现证据，小修引用旧产物并核对差异。

本轮清除当前入口的重复历史过程，原报告、失败、源资产及固定提交可追溯。只校准baseline的physical-table.2及导航，不新增CORE或修改玩法规则；Q1没有直接替代CORE-063，Q2没有采纳FB-Q01的具体方案。新二维展示条款及实际玩法变更继续资格／M／P或E／D／明确采纳。旧3D制作不自动续派，下一设计轮沿questions；无玩法实验或2D实现启动。

同日按用户“去向无需登记，专项清理和高价值合并”继续执行：删除旧过程正文与重复状态页，独有工程约束／失败经验合入工程接手与3D复盘；资产、冻结证据和正式设计来源保留。开发默认读取8文件CUSTOM启动包，具体任务补细则，探索仍沿READ-1；不新增迁移清单、玩法编号或实现授权。

<a id="g002-doc-027"></a>

## 2026-10-23：来源与验收轻量记录（G002-DOC-027）

Accepted / Documentation。用户明确要求精简来源审查、验收与输入记录，不再保存逐字原话，以版本统一和引用正确为记录要求。落实于[轻量记录规范](../../docs/design-workflow.md#言咒轻量记录)：意图与决定用摘要；同轮共用固定版本；使用处引用来源；验收保留情境与预期，实际结果链接证据；取消重复哈希清单、问答转录和双向台账。

本轮入口、READ-1、开发交接及共享模板同步，当前[结构研究](../sources/inbox/2026-10-23-design-reading-and-review.md)移除原话与重复清单。历史不批量重写，玩法采纳、实现及体验证据状态不变；核心正文与任务包的整体迁移仍为建议。

<a id="g002-doc-028"></a>

## 2026-10-23：核心、任务包与场景审阅（G002-DOC-028）

Accepted / Documentation。用户授权按[前述分析](../sources/inbox/2026-10-23-design-reading-and-review.md)开始精简改造。采用唯一GDD核心正文、按行为展开细则、派生任务包与场景审阅；核心覆盖整款游戏稳定设计并标当前首场范围，人工按选择／成本／时机／胜负／信息影响审校。落实于[文档合同](document-contract.md)、[任务入口](../development/task-pack.md)与[审阅规范](../development/design-review.md)。

迁移前输入固定为2e967f5e71cc387238131bd18feec47e6b546598；TL身份及玩法不变，TL-04／08／10／12／13／21／24正文移入核心，原页保留定位。原来源沿革按该提交取证，117项验收按行为归组；局外四个空页合为一页占位。CORE改读GDD，完整GDD包52份，开发默认启动5份。用途切换与打断重开为本轮两个派生包，执行与真人接手NotRun；工作台自动组包和专用审阅界面未实现。现有高影响边界不在整理中删除，未决玩法仍归questions。

静态核对：迁移的5段原文保持一致（仅相对链接随位置调整），117个验收ID保留。TL-V65补明停供适用的有耗材前提，TL-V75改引已闭合定时恢复合同，TL-V109分清实有与可消费层数；未改预期行为。新增／受影响引用与阅读包文件检查通过。核心6920字符；默认启动由25060降至15735字符（含空白、LF），约减37%；完整GDD正文包约9.40万字符。上述是文档统计，不是模型注意力或人工审阅效果的实测。

<a id="g002-doc-029"></a>

## 2026-10-23：复杂细则精简与对话审阅（G002-DOC-029）

Accepted / Documentation。用户要求处理冗余、过期与提前泛化，并通过对话说明改动；共同输入版本为c42ed2856e8b531bb0a223adedc55d449e053b1d，整理前正文按该提交原路径取证。不新增CORE或改案例参数，不保存原话或另建迁移表。

完整核对10份rules及相关核心、内容、示例、任务包和验收后，集中压缩行动／生产／资源／辅槽／标记／交互细则和三个长示例：支付、开工检查和暂停音画只在各自权威段维护；示例删掉重复资格／用途／未决叙述，复用既有验收；候选敌人数值退出当前内容页、回来源追溯。physical-table.2统一原位显牌与原位使用，删除早期抬起／翻转用语；首场自动暂停不再写未定，历史执行状态统一指开发证据。

提前泛化按实际使用收束：周期、维护、开工标记费、多目标／反应为条件展开，未使用的首场任务不据此创建功能。Accepted边界仍有效，公共机制改动仍查完整依赖，路线与经济短规则本轮未重写。对话已解释打断回收和失焦；用户反馈优先简化锁定／冻结／支付，已同步核心及两包：首场仅实有、锁定、可消费与生效付款，无开工标记费，不需要冻结／退款账目。未采纳取消锁定、提前付款或改变冻结后果等新玩法。

本轮10份重点细则／示例／内容页由34002降至22865字符，约减33%（含空白、LF；不是整个GDD的降幅）。117条验收行原文保持，规则身份未丢失；引用检查与关键支付、时序、恢复反例静态复核。没有运行游戏或独立开发接手，也不宣称全部规则形式等价或真人理解通过。审阅反馈与未覆盖范围见[本轮审阅](../development/design-review.md#2026-10-23-本轮审阅)。

### 同日续审：资源与标记的共用锁定

输入版本a5ef2ce52354d88451f4a3e8a445e38c8d6ebe36。用户明确保留资源与标记的锁定，并将其作为基础库存分配操作；已结束取消锁定的备选讨论。该范围与[CORE-055既有采纳](../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md#拟新增内容)一致，本次统一表达并强调解锁后按原消费时点／条件／顺序自动使用，不新增CORE或改变费用、批次承诺与当前范围。同步核心、术语、权威条款、两类资源接口、任务包及审阅记录；TL-V73补入两类对象解锁后的预期，117个验收身份保留。执行与体验未重新验证，不保存逐字答复。

<a id="g002-core-064"></a>

## 2026-10-23：所有暂停统一到拍末（G002-CORE-064）

Accepted / beat-pause.1，GDD 2.7／GDD-0。用户在对话审阅中要求暂停完成本拍全部应执行处理与动画，并明确接受揭示自动暂停也完成该拍开工、后续调整只能影响之后拍。来源与本轮唯一共同输入版本见[M](../sources/materials/M-2026-10-23-beat-end-pause.md)，评估及替换范围见[采纳D](../sources/draft-changes/D-2026-10-23-beat-end-pause.md)。

手动、揭示、失焦、详情／设置／回看统一收尾；单步完成一拍及动画后停，下一拍不开始。原CORE-060—063中观察即停、按事件停、取消未完动画及单步到下一观察的规定被替代；其余范围保留。终局仍在完整事件后停止余步，只呈现已经发生结果；正常退出先收尾，异常恢复保留最近结清事件、不自动补跑。

核心、权威细则、案例操作说明、两份派生包及验收同步；内容参数、44个TL身份和117个既有验收ID保留，CORE-064追加情境。实现与体验NotRun，旧0.4／B13证据不外推新行为。对话只留决定摘要，不新增原话或重复审查记录。
