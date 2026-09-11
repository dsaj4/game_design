# 全局规则审查：回归卡牌与流派设计前

日期：2026-09-11。Project ID：game-002。状态：Documentation Review Completed；玩法与数值验证Deferred。审查基线提交：fb75812263f76992c7ebab5c66eb857a001abb63，Core Concept v0.6／G002-CORE-014。本页保留审查发现并追踪关闭依据；用户随后全部采用推荐处理，见[G002-CORE-015](../game-design-workflow/draft-changes/D-2026-09-11-global-rule-boundaries.md)。本页不是测试报告。

## 结论

现有战前配置、实体分配、循环释放、引用名单、护甲、类型及战后收益骨架可继续支撑卡牌与流派草拟。本轮找到四处可依据现有决定直接修正的表述，已同步；另外登记的12组歧义、候选边界或输入依赖，其推荐处理已获用户批量采纳。处理选择已关闭，具体卡牌字段和候选验证仍按下表推进。不能据此声称全局规则已完全闭合或平衡已通过。

新卡只需在成为可评测候选前补齐自己涉及的缺口，不必先完成所有后置系统。推荐从单执行者、明确目标和有限数量作用起步；时间改期、事件触发、生成物和额外成本各在首次使用时处理对应项。这是推进建议，不替用户选定第一批卡牌或新流派。

用户明确“先不急验证，累积到下一次一起测试”。本轮只读规则、审查文档并修正确定性措辞，没有执行模拟、算例复算、游戏测试或玩家测试，也没有分派测试任务。[测试交接](test-handoff.md)改为积累待批测。

## 范围与依据

- 阅读49份现行正式素材的规范段、关键依赖和Unknown，交叉核对核心、决策、术语、数值框架及交接。
- 检索24份inbox记录的状态与相关主题，用于确认来源、Parked边界和未晋级部分；未将其中搁置词效作为现行规则。
- 历史决策、历史测试结果按各自固定输入解释；未检索其他项目补充玩法，也未改写归档。
- 工作区两份既存语法素材删行保持原状，本轮不提交它们；发现与修正不依赖这两处未提交删行。
- 通过grill-with-docs进行领域与规则对照。新建议来源保存在[本轮inbox](../game-design-workflow/idea-inbox/2026-09-11-global-rules-review.md)，用户批量确认后已通过资格闸门并晋级[GR v1正式素材](../game-design-workflow/idea-materials/M-2026-09-11-global-rule-boundaries.md)。GDD引用该素材中的状态边界，GR07-C01及FAT-C仍为候选。

## 已修正的四处现用表述

| 编号 | 分类 | 审查前问题 | 本轮修正 | 文件 |
| --- | --- | --- | --- | --- |
| DC01 | 召唤类型条件冲突 | “实际单位参与才构成召唤类型”与G002-CORE-012按名词特征、配置固定冲突。 | 改为按战前召唤物名词归类；实际单位只决定是否能执行。 | [来源与修正](../game-design-workflow/idea-materials/M-2026-09-06-summon-unit-and-reference.md) |
| DC02 | 对象顺序表述过宽 | 状态素材把全部顺序写成战前固定，未覆盖SW02-A与R08的新生对象。 | 分别写实例公开固定顺序、条件本次名单及确定生成顺序；不追加本次名单。 | [来源与修正](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md) |
| DC03 | 材料权限措辞残留 | 遗体描述仍含“独立身份、材料和能力”，易被误读为恢复供材权限。 | 改为身份、状态与明示能力，并补现行R17的材料加工后置及掉卡须词义声明。 | [来源与修正](../game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md) |
| DC04 | 信息预览承诺过宽 | 路线素材写“整场攻击安排”，未区分基础计划与后续明确改期。 | 与核心、R25统一为当前已知安排、基础计划及变化原因，不承诺未来状态固定。 | [来源与修正](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md) |

DC01是明确规则冲突；DC02–04是与较新已采纳范围衔接不足的表述。修正按G002-CORE-011／012、SW02-A和R08／25执行，没有引入第五法术类型、生成物新权限或新时序规则；这四处措辞修正本身不改变核心采纳状态；后续GR处理的采纳另按G002-CORE-015记录。

## 审查项与处理状态

以下12组不等于12项玩法缺陷。用户已采用全部推荐处理；每项剩余的是具体内容输入或验证，不再等待同一处理选择的确认。GR01–07为通用边界的未闭合部分；GR08–10是已登记内容／疲劳候选依赖；GR11是候选验收范围的张力；GR12是实际评测资源输入不足。

| ID | 主题 | 已采纳处理与保留状态 | 最晚具体输入时点 |
| --- | --- | --- | --- |
| GR01 | 参数归属与数值合法域 | Accepted：通用规则与逐词声明要求 | 新词卡进入可评测候选前 |
| GR02 | 冷却区间与取消后的续排 | Accepted：通用默认规则 | 时间类卡进入评测前 |
| GR03 | 角色数量、配对与筛选成本 | Accepted：声明要求；首批优先单执行者 | 多角色／复杂条件卡进入评测前 |
| GR04 | 状态归零与合法零值 | Accepted：通用默认规则与逐状态声明要求 | 状态数量操作进入评测前 |
| GR05 | 联合支付与生命代价 | Accepted：通用默认规则 | 带额外成本的卡进入评测前 |
| GR06 | 归零与完整事件结算 | Accepted：通用边界与内容声明要求 | 多步骤／死亡收益卡进入评测前 |
| GR07 | 派生事件与有限响应 | Accepted：声明要求；GR07-C01保留Candidate | 反应／触发型流派进入评测前 |
| GR08 | 生成物的身份与操作窗口 | Accepted：内容设计必填要求 | 首张元素／生成物卡进入评测前 |
| GR09 | 掉卡与产金的尝试记账 | Accepted：内容设计必填要求 | 首张产卡／产金卡进入评测前 |
| GR10 | 疲劳完整包与验证身份 | Accepted：继续候选合批的处理方式；FAT-C未升级 | 采用疲劳的下一批测试冻结前 |
| GR11 | 正常体验、极端配置与真实玩家 | Accepted：评价范围；具体阈值仍Candidate | 评测报告据此决定卡牌优劣前 |
| GR12 | 每批固定实际资源输入 | Accepted：评测输入与结论范围要求 | 每批可比较样本冻结前 |

### GR01：数值从词到整句如何得到

依据：[参数归属](../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md)、[修正读取](../game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md)。

审查时情境：现有两句分别把伤害量放在动词、护甲生成量放在名词；新组合的r仍逐句待设计。固定削弱使原本非负的量越过0时，最终截断点也未写全。

已采用的处理：每个词条声明自己贡献的参数及适用角色，操作语义声明整句效果与r的计算方法，不用整句名称暗设加成。推荐非负数量统一在完整修正后取整并截至0；τ、c、r、状态周期的整数域及零值许可另列，不能只写P为正。

影响与边界：影响跨句复用、成本和强化／削弱；具体默认值仍不在本次采用。

待合批检查：同一词两种合法组合与一条非法组合；固定／百分比负修正；0值与小数；r变化不重复产生直接效果。

### GR02：冷却区间、取消与改期后的续排

依据：[循环时间](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)、[R23／24](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)。

审查时情境：规则给了计划释放点及成功后续排，但未用统一区间说明冷却开始刻的敌攻是否打断；当前冷却被改期后又被打断／覆盖，如何产生下一轮缺少完整表。

已采用的处理：以半开区间明确冷却与释放：冷却包含开始、排除释放开始；取消的机会保留当时已确定的名义释放段与后续周期。改期只改当前机会，按其新的名义释放结束点续基础冷却；取消标记不因再次改期复活。同一过程多次改期按公开事件顺序处理。

影响与边界：未改期的两句参照仍可用；本次已按GR02同步R23，原简略口径由当前机会的名义释放段明确。

待合批检查：起点同刻受击、释放开始与释放结束同刻受击；先改期后取消、重复取消、被取消机会再改期。

### GR03：多个执行者与目标、筛选权限怎样组合

依据：[不同角色绑定](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)、[R05–08／18](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)。

审查时情境：同一法术能让不同角色各自选一组对象，但“2个执行者、3个目标”是2次、3次还是6次作用没有统一答案；选择配置能否免费添加新词义也会改变成本。

已采用的处理：首批优先单执行者；每种操作声明角色数量、同宿主／一对一／其他配对许可及去重单位，未声明不自动作全组合。同次名单固定不等于角色配对已经定义。筛选只配置已获词义的参数；新增语义仍由实体词卡承担，并明示条件字段和限量优先级。

影响与边界：全体选择不是默认多倍输出；多执行者时源方强度应按每个执行者分别说明。

待合批检查：2×3角色集合、角色重叠、同宿主约束、同一身份重复路径、平局优先级及对应实体成本。

### GR04：零数量、状态不存在和被禁止效果的区别

依据：[状态重施](../game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md)、[生成／读取](../game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md)、[禁疗候选](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md)。

审查时情境：状态被消耗至0后是否还保留身份、计时与存在条件，文档没有统一判定；“生成0”“读取0”“解除不存在状态”也不能仅按数值相同判断成功。

已采用的处理：每个状态声明零数量是否意味着清除，推荐数量型状态耗尽即清除；有无型状态独立声明。生成、读取可允许合法零值；消耗不足、对象不存在、规则禁止分别按合法性处理。先判断是否合法，再决定实际量，不用“没有实际收益”统一否决成功。

影响与边界：影响条件筛选、重施排序、合法成功和疲劳禁疗；不能改掉已采纳的合法零值原则。

待合批检查：消耗至0后同刻重施；零量生成；缺失状态读取／解除；被禁疗与合法零量的成功事件区别。

### GR05：一次费用、对象费用和生命支付是否能完整支付

依据：[R10](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)、[C01／02](../game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md)。

审查时情境：一次性费用和首个对象费用分别足够、合计却不足时，应在哪一步判失败？支付本身消耗必需状态或恰好耗尽执行者生命，也缺少明确处理。

已采用的处理：先联合检查本次一次性费用与首个可执行对象的全部固定费用，满足后一起提交，再逐对象处理后续费用；不允许先收一次费却没有任何可结算对象。默认生命支付后须存活，若设计自毁则专门声明；不得把费用不足当合法零值或自动退款已完成效果。

影响与边界：避免收费与效果的循环资格判断；不新增环境供材或跨对象转移。

待合批检查：各自足够合计不足、首个对象失效、费用耗尽宿主状态、生命恰好等于费用、多对象中途不足。

### GR06：生命归零到完整事件结束之间如何处理

依据：[完整事件后检查](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md)、[击败与身份](../game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)、[完整法术](../game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md)。

审查时情境：法术第一步令单位归零，后续步骤还引用它时，“当前合法性”与“完整事件后才判击败”尚缺清晰衔接；法术成功通知、死亡产物和胜负检查的先后会影响收集或触发。

已采用的处理：区分“已不能作为存活单位操作”与“完成事件后的离场／胜负”：后续步骤复查生命资格，原事件已合法结果保留；死亡派生与法术成功通知的相对顺序在涉及它们前明示。最后敌人死亡后不能依赖下一次释放或后续阶段继续收集。

影响与边界：不改变同检查点失败优先；单纯伤害末尾结束已可解释，复合死亡行为不能靠实现者自行裁定。

待合批检查：同法术归零后再次指向、源方中途失效、同死、击败最后敌人并产生待领取卡、遗体生成后没有下一轮。

### GR07：同阶段新事件与额外触发的次序和终止

依据：[R20／26／27](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)、[状态顺序](../game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md)。

审查时情境：已错过阶段转下一刻已明确；在当前阶段处理过程中产生的新事件，是本阶段追加还是下一刻处理，并未普遍闭合。循环条件也不能自动成为免费响应。

已采用的处理：首批事件型内容先声明观察事件、扣费／计次、入队时点、阶段、同刻顺序和有限响应规则；未声明时不增加额外施法。可先将同阶段新派生事件统一延至下一刻作为候选，避免递归；明确属于当前完整效果的有限子步骤仍在当前事件内完成。

影响与边界：GR07-C01仍为选定待测候选，不覆盖已有状态周期／到期顺序；声明与有限响应要求已采纳，复杂传播和镶嵌触发继续后置。

待合批检查：同阶段产生事件、跨已过阶段、两个触发互相响应、合法零值成功反复触发及终局停止。

### GR08：生成物在哪出现、可操作到何时

依据：[生成物范围](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md)、[法杖范围](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)。

审查时情境：允许真实元素对象已有方向，但生成位置或锚点、实例身份、数量、结束时点和作用阶段仍未定义，无法判断下一句是否能引用。

已采用的处理：随生成物词条填写出现位置的固定规则、身份粒度、来源、主变化量、窗口、结束方式及下一次可引用条件；不开放战中选落点，也不自动采用6刻或一次使用。只需补当前卡会用到的字段。

影响与边界：不阻碍纯直接作用卡；来源离场与生成物消失是否关联须明示。

待合批检查：生成后后续条件引用、来源离场、窗口结束同刻、范围边缘、新同名对象不续绑旧实例。

### GR09：产出资格、次数和失败尝试如何记账

依据：[整体产出](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md)、[产金成本](../game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md)、[R31](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)。

审查时情境：先检查资格和三张上限已有规则；“每对象一次”尚未采纳。满额、空产出池或概率未中时是否消耗次数／费用，及同事件多个产出争最后名额仍需词条定义。

已采用的处理：产出卡明示次数归属对象／效果／战斗、候选池、概率和空池处理、何时消耗额度与费用、对象变化。推荐先校验资格，再按明确规则尝试与计次；不要默认失败重抽到成功。先用确定产出减少首批依赖；概率机制只在该卡需要时补齐。

影响与边界：不新增手动拾取或材料加工；疲劳结束保证不代替有限产出限制。

待合批检查：多个对象争最后副本名额、满额和空池、未命中概率、整体放弃、最后敌人死亡后的产出时机。

### GR10：疲劳方向已定，完整执行仍是候选

依据：[FAT-A／FAT-C](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md)。

审查时情境：双方扣血和法术禁疗已采纳，但FAT-C独立生命损耗、不打断、护甲不抵消及环境阶段同扣尚未成为正式规则，不能直接与C01二分法混用。

已采用的处理：保留整套FAT-C的候选身份并合批审查；需实测时允许明确以候选规则运行，但报告不得称正式基线。若未来采纳独立损耗类别，同步核心、C01、打断与统计口径。禁疗不解除战斗治疗后置范围。

影响与边界：当前无需重复选择是否引入疲劳；不把进入疲劳当作已结束，也不让新生命机制绕过有限收尾。

待合批检查：复用交接F06–F08，补候选与正式分类对照；不重复建立相同用例。

### GR11：无秒杀的适用范围和跨战残血风险

依据：[NF30／EX03／04／05](../game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)、[剩余生命](../game-design-workflow/idea-materials/M-2026-09-05-post-victory-health-persistence.md)。

审查时情境：EX03对同阶段发布战斗很宽，EX04却区分健康入场与残血。玩家主动带残血进危险路线、极端低防配置早败，不应自动等价于常规战斗设计缺陷；“唯一最优”也不能从一个场景判断。

已采用的处理：分开常规体验群体、合法极端配置、真实玩家分布；所有配置检查有限终局，秒杀阈值对预先登记的正常入场条件评估，残血／主动风险单独报告并保留警报。合理失败不是静默删样本；速度、损耗与资源的非支配关系跨场景比较。

影响与边界：评价范围已按GR11采纳；EX具体阈值仍为候选，没有据此放行具体例外，也不修改既有测试结果。

待合批检查：健康入场／残血同一遭遇、极端无输出、固定预算与获取机会、多场景对照及偏好变化。

### GR12：库存、范围、成长和获取资格尚需明确输入

依据：[基础可表达性](../game-design-workflow/idea-materials/M-2026-09-06-prebattle-expressibility.md)、[初始资源](../game-design-workflow/idea-materials/M-2026-09-07-new-run-starting-resources.md)、[词池资格](../game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md)、[成长预算](../game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md)。

审查时情境：现有6卡2杖是测试装置，正式起始资源与范围未定；只给新流派全部核心卡，会把获取与组件机会成本忽略，2.30／1.60成长预算也没有实际资源支撑。

已采用的处理：每批固定词池、实际副本、法杖数与允许范围、起始生命、敌人矩阵、获取资格和替换方式；小批先用明确测试装置，结论限于该装置。卡牌可设计，正式成长／路线／经济评价在对应输入齐备后再做，不强行补出全局内容。

影响与边界：不要求现在设计完整镶嵌、地图或经济；不以未知输入当作测试通过。

待合批检查：同预算替换、缺核心组件、不同副本数、范围内外、词池不足与获取渠道、跨战生命账本。

## 当前不需要重新决定的部分

| 已明确内容 | 为什么不列为新冲突 |
| --- | --- |
| 单卡单位置、同名最多三张、一法术一法杖 | 资源与实体分配一致；未知的是规模，不是可以复用同一实体 |
| 开始释放时争槽、靠后法杖覆盖、直接效果只结算一次 | r可以影响周期而不意味着持续多次伤害；这本身不是矛盾 |
| 实例／条件绑定并存、本次名单不追加、逐对象读当前状态 | 名单固定与状态变化可以并存；GR03补的是角色配对 |
| 同种状态合并、有限剩余时长相加、周期保持 | 已有明确选择；强弱状态混加是否过强是待测平衡，不能当未决规则重问 |
| 合法零值可以成功、多个类型不重复计一次成功 | 既有原则保持；GR04补合法性边界，GR07补未来事件响应 |
| 生命检查失败优先、胜利停止后续战斗处理 | 同次双方死亡已有唯一结果；GR06补复杂事件内部与派生结果的先后 |
| 休整卡包不足只保留恢复、商店空池允许离开 | 不需要再发明补偿／刷新，按现行获取规则处理 |
| 疲劳禁疗与战斗治疗后置 | 禁疗是疲劳方向的一项限制，不表示治疗卡已开放 |
| 简易／状态／元素／召唤按特征多分类 | 名词＋动词的状态例句只被用作分类，完整句法许可仍待对应内容；不视为自由语序已采纳 |
| 召唤指挥、镶嵌、复杂传播、位移与材料加工 | 已后置，不要求为回归普通卡牌设计而先实现这些子系统 |

## 回归卡牌设计的交付边界

采用[卡牌设计—评测—采纳流程](card-design-review-workflow.md)。可以开始记录词条与流派设想，文档评议和待测积累同步进行；只有被某张卡实际依赖的GR项目才成为它的评测前置。

第一批候选须能说明词义、实体成本、参数归属、完整合法组合、反例及预期取舍；流派须有实际组合、弱点和同预算替代方案。若只写了“火系流派”“按状态触发”或只有名称，继续留在inbox。类型标签不代替流派机制。

审查阶段没有创建具体卡牌或流派GDD。用户随后确认全部推荐处理，现已形成GR v1素材、提案、评估与G002-CORE-015采纳记录；具体词效仍按卡牌逐项设计。下一批测试启动前将卡牌候选、所需全局决定、框架与疲劳包一起固定版本；不同候选规则可以分组测试，但不能混入同一结果集后比较。

## 覆盖清单

下列文件均参与现用规则审查；“覆盖”是文档对照，不表示内容可执行或测试通过。各文件的Candidate／Parked／Unknown边界保留。

| 现行素材 | 本轮处理 |
| --- | --- |
| [战场状态的存续与引用](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md) | DC02现用表述修正 |
| [循环法术的时间与打断](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md) | 规范与依赖对照；证据状态保持 |
| [词性、句式与语义兼容](../game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md) | 规范与依赖对照；证据状态保持 |
| [战斗胜负与本局结束](../game-design-workflow/idea-materials/M-2026-09-05-normal-combat-outcomes.md) | 规范与依赖对照；证据状态保持 |
| [普通胜利后的生命保留](../game-design-workflow/idea-materials/M-2026-09-05-post-victory-health-persistence.md) | 规范与依赖对照；证据状态保持 |
| [休整的恢复与词卡取舍](../game-design-workflow/idea-materials/M-2026-09-05-rest-recovery-and-word-choice.md) | 规范与依赖对照；证据状态保持 |
| [战前编排与周期预览](../game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md) | 规范与依赖对照；证据状态保持 |
| [战外词卡库存与实体副本](../game-design-workflow/idea-materials/M-2026-09-05-word-inventory-and-copies.md) | 规范与依赖对照；证据状态保持 |
| [护甲的生成与存续](../game-design-workflow/idea-materials/M-2026-09-06-armor-identity-generation-and-persistence.md) | 规范与依赖对照；证据状态保持 |
| [法杖范围与对象引用](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md) | 规范与依赖对照；证据状态保持 |
| [局内分叉路线](../game-design-workflow/idea-materials/M-2026-09-06-branching-run-routes.md) | DC04现用表述修正 |
| [整句效果与词义复用](../game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md) | 规范与依赖对照；证据状态保持 |
| [伤害、护甲与冷却打断](../game-design-workflow/idea-materials/M-2026-09-06-damage-armor-and-interruption.md) | 规范与依赖对照；证据状态保持 |
| [敌人击败后的对象与状态](../game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md) | DC03现用表述修正 |
| [省略句与显式主语](../game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md) | 规范与依赖对照；证据状态保持 |
| [战后词卡与整体收益](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md) | 规范与依赖对照；证据状态保持 |
| [战前库存的可表达性](../game-design-workflow/idea-materials/M-2026-09-06-prebattle-expressibility.md) | 规范与依赖对照；证据状态保持 |
| [预设起始库存与新局重置](../game-design-workflow/idea-materials/M-2026-09-06-preset-starting-inventory.md) | 规范与依赖对照；证据状态保持 |
| [效果来源与修正读取](../game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md) | 规范与依赖对照；证据状态保持 |
| [法术类型与效果条件](../game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md) | 规范与依赖对照；证据状态保持 |
| [同种状态的重施与叠加](../game-design-workflow/idea-materials/M-2026-09-06-status-reapplication-and-stacking.md) | 规范与依赖对照；证据状态保持 |
| [状态计时与到期](../game-design-workflow/idea-materials/M-2026-09-06-status-timing-and-expiration.md) | 规范与依赖对照；证据状态保持 |
| [状态读值与内部顺序](../game-design-workflow/idea-materials/M-2026-09-06-status-values-and-resolution-order.md) | 规范与依赖对照；证据状态保持 |
| [召唤物共存与容量约束](../game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md) | 规范与依赖对照；证据状态保持 |
| [召唤物离场与引用失效](../game-design-workflow/idea-materials/M-2026-09-06-summon-departure-and-reference-invalidation.md) | 规范与依赖对照；证据状态保持 |
| [召唤物生命与承伤](../game-design-workflow/idea-materials/M-2026-09-06-summon-health-damage-and-enemy-targeting.md) | 规范与依赖对照；证据状态保持 |
| [召唤身份引用的可用边界](../game-design-workflow/idea-materials/M-2026-09-06-summon-reference-availability.md) | 规范与依赖对照；证据状态保持 |
| [召唤单位与指令语义](../game-design-workflow/idea-materials/M-2026-09-06-summon-unit-and-reference.md) | DC01现用表述修正 |
| [召唤词语义与单位绑定](../game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md) | 规范与依赖对照；证据状态保持 |
| [词性与休整候选结构](../game-design-workflow/idea-materials/M-2026-09-06-word-classes-and-reward-packs.md) | 规范与依赖对照；证据状态保持 |
| [战斗金币与耗时奖励](../game-design-workflow/idea-materials/M-2026-09-07-combat-gold-and-efficiency-bonus.md) | 规范与依赖对照；证据状态保持 |
| [商店商品资格](../game-design-workflow/idea-materials/M-2026-09-07-merchandise-eligibility.md) | 规范与依赖对照；证据状态保持 |
| [新局初始资源](../game-design-workflow/idea-materials/M-2026-09-07-new-run-starting-resources.md) | 规范与依赖对照；证据状态保持 |
| [周期状态的强化继承](../game-design-workflow/idea-materials/M-2026-09-07-periodic-state-modifier-inheritance.md) | 规范与依赖对照；证据状态保持 |
| [商店节点与消费机会](../game-design-workflow/idea-materials/M-2026-09-07-shop-nodes-and-spending-opportunities.md) | 规范与依赖对照；证据状态保持 |
| [商店货架与交易](../game-design-workflow/idea-materials/M-2026-09-07-shop-shelves-and-transactions.md) | 规范与依赖对照；证据状态保持 |
| [支撑系统与流派设计规则](../game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md) | 规范与依赖对照；证据状态保持 |
| [法杖与镶嵌配置](../game-design-workflow/idea-materials/M-2026-09-07-wand-inlay-configuration.md) | 规范与依赖对照；证据状态保持 |
| [已采纳接口规则与后置范围](../game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md) | 规范与依赖对照；证据状态保持 |
| [法术改变战场状态的体验与表现要求](../game-design-workflow/idea-materials/M-2026-09-10-battlefield-state-change-expression.md) | 规范与依赖对照；证据状态保持 |
| [实例绑定与条件绑定](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md) | 规范与依赖对照；证据状态保持 |
| [数值重新设计的范围与验证约束](../game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md) | 规范与依赖对照；证据状态保持 |
| [语义世界的对象交互与执行规则](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md) | 规范与依赖对照；证据状态保持 |
| [法术可操作对象范围](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md) | 规范与依赖对照；证据状态保持 |
| [简单对象交互与法术生成物](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md) | 规范与依赖对照；证据状态保持 |
| [四层数值框架：法术、成长、整局与体验](../game-design-workflow/idea-materials/M-2026-09-11-numerical-evaluation-framework.md) | 规范与依赖对照；证据状态保持 |
| [超时疲劳：双方扣血与法术禁疗](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md) | 规范与依赖对照；证据状态保持 |
| [简易法术与护甲：参数定义及首轮测试候选](../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md) | 规范与依赖对照；证据状态保持 |
| [法术类型系统：特征、多类型与首批分类](../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md) | 规范与依赖对照；证据状态保持 |

## 后续维护

GR01–GR12处理选择已按G002-CORE-015全部关闭，权威定义见GR v1素材；当前正式素材为50份，本页覆盖表的49份是原审查范围。后续卡牌按实际依赖补齐内容字段，GR07-C01与FAT-C按候选版本积累；新的独立变更仍走资格／提案／评估／Draft Change。测试按[固定交接](test-handoff.md)合批积累，本轮所有新待测项均NotRun。

2026-09-11采纳回填：用户“待明确部分均采用推荐处理”；来源、资格、提案、评估和具体采纳文本已双向关联。GR v1为当前规则补充，四层框架v0.3同步评价范围，交接r4继续Draft／NotRun。原审查时未采纳版本保留于571c6db0cd958f9e5fd0a82814293354395a35cc。

2026-09-11后续顺序：用户已要求先完善修饰词与镶嵌，再设计流派成套物品，见[系统入口](modifier-and-inlay-design.md)。本文保留本次GR审查时的观察和决定；镶嵌排期随后已调整，具体触发规则未因调整而采纳。
