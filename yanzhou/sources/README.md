# 设计来源链

> TL-1 + INS-1版本说明（2026-10-04）：本目录的既有日期型记录保留原资格、原采纳与原证据范围，其中历史“当前”不覆盖新版。TL-1仅使用[素材审查](../design/source-review.md)明示部分；[逐文件清单](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/reading-log.md)登记保留或替代，不把旧来源全文重写成新规则。

Project ID：game-002。文档角色：SourceCollection / Navigation。这里保存设计形成过程，现行规则统一在[design/](../design/README.md)。

| 阶段 | 目录 | 允许状态 |
| --- | --- | --- |
| 原始表达 | [inbox](inbox/README.md) | Raw / Unqualified；允许Unknown |
| 已完成资格确认 | [materials](materials/README.md) | Qualified及其明确范围；不自动Accepted |
| 玩法提案 | [proposals](proposals/README.md) | 有合格来源的假设与验证方案 |
| 评估 | [evaluations](evaluations/README.md) | 评议结果，注明证据范围 |
| 拟修改 | [draft-changes](draft-changes/README.md) | 拟改文本、授权与采纳范围 |
| 新GDD草案 | [gdd-drafts](gdd-drafts/README.md) | 使用登记模板；未采纳版本不覆盖现行design |

[决策记录](../governance/decision-log.md)说明何时采纳了哪些范围。文件名和原设计ID保持，旧素材使用记录的链接已定位新路径；原提交和历史哈希仍按原路径解释。


## 已完成过程记录

首批内容候选入口：[简易法术流设计登记（2026-10-11）](inbox/2026-10-11-simple-spell-first-batch-registration.md)。原件保持原始记录；后续明确范围已晋级，并按CORE-059进入首批案例，剩余未完成内容保留原资格。

六组已采纳设计的18份P/E/D已归档到[完成记录](../history/accepted-design-records/README.md)。原始输入、合格素材与仍有局部未决内容的过程文档留原处；归档不扩大采纳或验证范围。旧文档管理拟修改按固定Git取证。新增任务按需要创建正式文件，不预建空树。

## TL-1 本轮来源链

[DIR-028核心M](materials/M-2026-10-01-timeline-production-core.md)／[退役卡表固定记录](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/M-2026-10-01-resource-card-pool.md)／[P](proposals/P-2026-10-01-timeline-production-system.md)／[E](evaluations/E-2026-10-01-timeline-production-system.md)／[采纳D](draft-changes/D-2026-10-01-timeline-production-core.md)。2026-10-04已采纳M/P/E迁入本来源体系，原方向答复和审查按固定Git取证；卡表不列当前候选。

第9轮[兼容复用表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)限定21份原Qualified来源的当前使用部分，既有P/E追加本轮论证；[D兼容复用](draft-changes/D-2026-10-01-compatible-rules-reuse.md)记录CORE-048。原文与历史资格保留，现行复用以TL-26–37及CORE-049的局部替代为准。

## INS-1来源链（CORE-049）

[DIR-036 Raw原话](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-036-sentence-inscription-redesign/README.md) → [局部Qualified M](materials/M-2026-10-04-artifact-inscription-core.md) → [P](proposals/P-2026-10-04-artifact-inscription-core.md)／[E](evaluations/E-2026-10-04-artifact-inscription-core.md) → [采纳D](draft-changes/D-2026-10-04-artifact-inscription-core.md)。主系统采用已确认的铭刻结构；整个方向与未决卡效／打造／契合不自动提升资格。

## routing.1来源链（CORE-050）

[原话／调时答复](inbox/2026-10-04-routing-response-clarification.md) → [局部Qualified M](materials/M-2026-10-04-routing-response-clarification.md) → [E](evaluations/E-2026-10-04-routing-response-clarification.md) → [采纳D](draft-changes/D-2026-10-04-routing-response-clarification.md)。仅全敌牌正延迟、未来供料调度及供料调时范围进入当前规则；付费调牌序保持inbox Raw候选。

## 当前重建框架与后续采纳增量（2026-10-08）

- 既有规则增量：[CORE-051单一处理](draft-changes/D-2026-10-05-single-processing-time.md)、[CORE-052生产队列接口](draft-changes/D-2026-10-05-production-queue-interfaces.md)、[CORE-053共同拍序](draft-changes/D-2026-10-05-stage-one-common-timing.md)、[CORE-054敌情合同](draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)。原轮次Unknown按后续明确替代范围解释。
- 新增局部Qualified框架：[辅槽](materials/M-2026-10-08-augment-framework.md)、[行动／标记](materials/M-2026-10-08-action-card-framework.md)。已确认结构可引用，未自动完成全系统采纳或内容发行。
- 当前阶段沿[阶段1—4完成的用户前提](inbox/2026-10-08-augment-framework-review.md#原始想法与触发来源)；具体归位、未采纳差异和未提交原件身份见[法器整理](inbox/2026-10-08-artifact-framework-review.md)与[敌人整理](inbox/2026-10-08-enemy-framework-review.md)。旧阶段规划不覆盖当前进度。
- [重建后一致性审查](../governance/main-system-review-2026-10-08.md)及[剩余接口](../governance/questions.md#重建后接口核对2026-10-08)是后续工作入口；原来源不改写为新版规则。

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

[用户纠偏与具体流程草案](inbox/2026-10-12-development-design-round-07.md)：用户明确主交互依赖3D模型、真实桌面卡片放置/翻转；当前黑色文本框主UI不符合目标。具体推进含义及文字/系统界面边界R8/R9待答，仍为Raw / Unqualified，不进入M/E/D或权威规则。已按DOC-024暂停开发，唯一状态见[当前问题](../governance/questions.md#physical-table-round07)；技术保全不等于用户接受旧界面。
