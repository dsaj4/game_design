# 设计来源链

> 现行范围说明（2026-10-23）：CORE-065已采纳回合、手牌与付费整理，CORE-066补齐限定完整首场输入。既有日期型记录保留原资格、原采纳及证据范围；下文旧来源链中的“当前／本轮”只指原日期。现行适用关系以[素材审查](../design/source-review.md)及权威规则为准，不把旧来源全文改写为新版，也不因新条款采纳而整体晋级早期Raw候选。

Project ID：game-002。文档角色：SourceCollection / Navigation。这里保存设计依据与决定摘要，现行规则统一在[design/](../design/README.md)。新增记录按[轻量规范](../../docs/design-workflow.md#言咒轻量记录)：不保存逐字原话，共用固定版本，在使用处准确引用。

| 阶段 | 目录 | 允许状态 |
| --- | --- | --- |
| 意图与确认摘要 | [inbox](inbox/README.md) | Raw / Unqualified；允许Unknown |
| 已完成资格确认 | [materials](materials/README.md) | Qualified及其明确范围；不自动Accepted |
| 玩法提案 | [proposals](proposals/README.md) | 有合格来源的假设与验证方案 |
| 评估 | [evaluations](evaluations/README.md) | 评议结果，注明证据范围 |
| 拟修改 | [draft-changes](draft-changes/README.md) | 拟改文本、授权与采纳范围 |
| 新GDD草案 | [gdd-drafts](gdd-drafts/README.md) | 使用登记模板；未采纳版本不覆盖现行design |

[决策记录](../governance/decision-log.md)说明何时采纳了哪些范围。文件名和原设计ID保持，旧素材使用记录的链接已定位新路径；原提交和历史哈希仍按原路径解释。


## 当前完整首场来源链（CORE-066）

[意图与授权摘要](inbox/2026-10-23-round-first-battle.md) → [Qualified M](materials/M-2026-10-23-round-first-battle.md) → [P](proposals/P-2026-10-23-round-first-battle.md)／[E](evaluations/E-2026-10-23-round-first-battle.md) → [Accepted D](draft-changes/D-2026-10-23-round-first-battle.md)。按用户授权自行冻结EX-004起始套组、完整敌表、初态及胜败／恢复预期，CORE-065机制不变；实现、运行与体验NotRun。

## 当前回合改制来源链（CORE-065）

[意图与确认摘要](inbox/2026-10-23-round-hand-settlement.md) → [Qualified M](materials/M-2026-10-23-round-hand-settlement.md) → [P](proposals/P-2026-10-23-round-hand-settlement.md)／[E](evaluations/E-2026-10-23-round-hand-settlement.md) → [Accepted D](draft-changes/D-2026-10-23-round-hand-settlement.md)。正式采纳范围包括付费调序、桌手互换与手牌提前入行；原全敌牌正延迟和连续拍队列等仅按明确替代关系保留历史。实现、运行及体验验证仍NotRun，不能从采纳推出通过。

## 已完成过程记录

首批内容候选入口：[简易法术流设计登记（2026-10-11）](inbox/2026-10-11-simple-spell-first-batch-registration.md)。原件保持原始记录；后续明确范围已晋级，并按CORE-059进入首批案例，剩余未完成内容保留原资格。

六组已采纳设计的18份P/E/D已归档到[完成记录](../history/accepted-design-records/README.md)。原始输入、合格素材与仍有局部未决内容的过程文档留原处；归档不扩大采纳或验证范围。旧文档管理拟修改按固定Git取证。新增任务按需要创建正式文件，不预建空树。

## TL-1原轮来源链（2026-10-01）

[DIR-028核心M](materials/M-2026-10-01-timeline-production-core.md)／[退役卡表固定记录](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/M-2026-10-01-resource-card-pool.md)／[P](proposals/P-2026-10-01-timeline-production-system.md)／[E](evaluations/E-2026-10-01-timeline-production-system.md)／[采纳D](draft-changes/D-2026-10-01-timeline-production-core.md)。2026-10-04已采纳M/P/E迁入本来源体系，原方向答复和审查按固定Git取证；卡表不列当前候选。

第9轮[兼容复用表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)限定21份原Qualified来源的当轮使用部分，既有P/E追加当轮论证；[D兼容复用](draft-changes/D-2026-10-01-compatible-rules-reuse.md)记录CORE-048。原文与历史资格保留，后续CORE-049至065的限定替代见现行素材审查，不从旧表恢复已退役接口。

## INS-1来源链（CORE-049）

[DIR-036 Raw原话](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-036-sentence-inscription-redesign/README.md) → [局部Qualified M](materials/M-2026-10-04-artifact-inscription-core.md) → [P](proposals/P-2026-10-04-artifact-inscription-core.md)／[E](evaluations/E-2026-10-04-artifact-inscription-core.md) → [采纳D](draft-changes/D-2026-10-04-artifact-inscription-core.md)。主系统采用已确认的铭刻结构；整个方向与未决卡效／打造／契合不自动提升资格。

## routing.1来源链（CORE-050）

[原话／调时答复](inbox/2026-10-04-routing-response-clarification.md) → [局部Qualified M](materials/M-2026-10-04-routing-response-clarification.md) → [E](evaluations/E-2026-10-04-routing-response-clarification.md) → [采纳D](draft-changes/D-2026-10-04-routing-response-clarification.md)。当轮采纳全敌牌正延迟、未来供料调度及供料调时，付费调牌序当时未采纳。CORE-065现已替代全敌牌正延迟，并通过新的合格来源采纳限定付费整理；旧inbox自身仍保留原资格。

## 2026-10-08重建框架与当时采纳增量

- 既有规则增量：[CORE-051单一处理](draft-changes/D-2026-10-05-single-processing-time.md)、[CORE-052生产队列接口](draft-changes/D-2026-10-05-production-queue-interfaces.md)、[CORE-053共同拍序](draft-changes/D-2026-10-05-stage-one-common-timing.md)、[CORE-054敌情合同](draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)。原轮次Unknown按后续明确替代范围解释。
- 新增局部Qualified框架：[辅槽](materials/M-2026-10-08-augment-framework.md)、[行动／标记](materials/M-2026-10-08-action-card-framework.md)。已确认结构可引用，未自动完成全系统采纳或内容发行。
- 当前阶段沿[阶段1—4完成的用户前提](inbox/2026-10-08-augment-framework-review.md#原始想法与触发来源)；具体归位、未采纳差异和未提交原件身份见[法器整理](inbox/2026-10-08-artifact-framework-review.md)与[敌人整理](inbox/2026-10-08-enemy-framework-review.md)。旧阶段规划不覆盖当前进度。
- [重建后一致性审查](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/main-system-review-2026-10-08.md)及[剩余接口](../governance/questions.md#开放项与范围)是后续工作入口；原来源不改写为新版规则。

[同拍结算原话](inbox/2026-10-08-settlement-order-reference.md)→[Qualified M](materials/M-2026-10-08-settlement-order-reference.md)→[E](evaluations/E-2026-10-08-settlement-order-reference.md)→[CORE-057 D](draft-changes/D-2026-10-08-settlement-order-reference.md)：timing.2限定采纳；前轮Raw研究与本轮适配分别保留，不扩大具体内容资格。

## 2026-10-11首批案例与固定用途

[用户答复](inbox/2026-10-11-simple-spell-first-batch-registration.md#2026-10-11进入ui与实装前的明确更新) → [M](materials/M-2026-10-11-simple-spell-example.md) → [E](evaluations/E-2026-10-11-simple-spell-example.md) → [CORE-059 D](draft-changes/D-2026-10-11-simple-spell-example.md) → [EX-001](../design/examples/simple-spell.md)。

## 2026-10-11开发设计对接首轮

[原案与R1—R3直接答复](inbox/2026-10-11-development-design-round-01.md) → [M](materials/M-2026-10-11-development-design-round-01.md) → [E](evaluations/E-2026-10-11-development-design-round-01.md) → [CORE-060 D](draft-changes/D-2026-10-11-development-design-round-01.md)。首场交互合同与EX-002已采纳，原EX-001及首版证据不变，运行与体验NotRun。

## 2026-10-12：首场表现与声音

[第03轮原案及R4—R6答复](inbox/2026-10-12-development-design-round-03.md) → [Qualified M](materials/M-2026-10-12-development-design-round-03.md) → [限定E](evaluations/E-2026-10-12-development-design-round-03.md) → [CORE-061 D](draft-changes/D-2026-10-12-development-design-round-03.md)。三项推荐已采纳，其他替代未采用；表现运行与体验仍NotRun。

## 主窗口失焦与返回（2026-10-12）

[第05轮原案与R7直接答复](inbox/2026-10-12-development-design-round-05.md) → [Qualified M](materials/M-2026-10-12-development-design-round-05.md) → [限定E](evaluations/E-2026-10-12-development-design-round-05.md) → [CORE-062 D](draft-changes/D-2026-10-12-development-design-round-05.md)。R7-A失焦停、返回仍停并明确继续已采纳；后台继续／返回自动继续未采用。失焦适配及体验NotRun。

## 第06轮工程职责核对（2026-10-12）

[性能预算冻结职责与测量边界](inbox/2026-10-12-development-design-round-06.md)为Derived clarification：已有开发授权允许技术负责人冻结本批推荐目标，无新用户裁决或玩法采纳，不新增M／E／D与CORE。总控已记录工程合同并恢复第七批，性能结果仍NotRun。当前实施状态以[开发入口](../development/README.md)为准，前轮交回时的NotRun保持历史语境。

## 第07轮桌面3D主交互（2026-10-12）

[用户纠偏与具体流程](inbox/2026-10-12-development-design-round-07.md)保留原Raw及答复过程；R8／R9已明确，并经[M／E／D](draft-changes/D-2026-10-12-development-design-round-07.md)限定采纳为CORE-063。10月14日[physical-table.2](draft-changes/D-2026-10-14-demoncards-presentation.md)追加必要文本与公开投影动作衔接。CORE-065已将该表现合同限定为旧3D演示，不作为新2D默认宿主；实现与接受范围另看开发证据。当前2D待设计事项见[questions](../governance/questions.md)，不从历史暂停倒推现状。
