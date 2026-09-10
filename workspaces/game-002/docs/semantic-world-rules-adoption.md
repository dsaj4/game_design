# 语义世界32项规则采纳交付

日期：2026-09-10。状态：Accepted / R01–R32。决策：G002-CORE-010。核心：Core Concept v0.6。证据：Hypothesis。

## 结果与范围

用户在完整建议后回复“均采用推荐”。[原话与32项备选](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md)已通过六组资格复核，形成[正式执行素材](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)、提案、评估与采纳文本。核心、领域词汇、相关素材和入口已同步。本批无遗留人工选择。

R12允许明确法术位移与结构变化；R17允许明示独立遗体；R18允许复合对象短语；R23允许当前剩余冷却改期；R24在释放开始仲裁共享槽。名单、筛选、排序、成本、反应、权限和跨战框架均按对应R编号执行。

正式素材实数增至44份，inbox记录仍为14份。数值重新设计继续有效；具体对象、能力、词卡、区域、窗口、参数与玩家验证尚未完成。完整召唤、法杖起始资源与镶嵌、BF1–BF3具体机制保持后置。

修改前版本完整保留于Git提交0326023，已有原始快照保持原样。历史提案、评估和采纳时检查明确标注其范围，不以历史记录的待决状态覆盖当前规则。

## 代表性规则走查

本轮按正式规则作以下符号情境的文档推导。甲、乙等是假设对象，不是新对象或词卡设计；结果只证明这些情境有明确裁定，不是游戏运行、参数平衡或玩家测试。

| 情境 | 规则依据 | 推导结果 |
| --- | --- | --- |
| 画面同时显示真实火焰过程与火焰结束后的焦痕 | R01–R04 | 各自指回真实对象和当前能力；焦痕不凭视觉成为可消耗燃烧状态 |
| 整体与部件共用一份材料 | R04、R11、R16 | 归属与消费来源明示；同一份材料不因引用层级不同而重复计数 |
| 名单含甲乙，甲的效果使乙不再满足条件，同时生成丙 | SW02-A、R05、R08 | 乙轮到时跳过，丙不补入本次名单；丙按生成顺序进入世界排序，可被后续释放选择 |
| 两个条件在同一角色与效果步骤选到同一对象 | R07 | 只处理一次；不同明示效果步骤仍各自处理 |
| 条件没有匹配对象 | R09–R10 | 本轮无效果释放后继续周期，不产生成功事件；对象材料与一次性成本均不扣 |
| 甲缺少对象成本、乙可以合法结算 | R10 | 跳过甲；首次合法结算前检查并支付一次性成本，对乙支付其对象成本；不重复收费 |
| 一次性成本和对象成本来自同一来源 | R10–R11 | 来源需覆盖合计需求；不足不能先扣一项制造部分合法结算，也不从别处隐式补足 |
| 对象已入名单，轮到前移出当前法杖范围 | R12–R14 | 实例身份仍在，但当前作用距离不合法，跳过且不补位 |
| 已登记部件分离，未登记碎片随后产生 | R15–R16 | 部件保留自己的身份，碎片获得新身份；整体失去转出材料，状态不整份复制 |
| 敌人死亡且效果声明留下遗体 | R17及胜负规则 | 原单位身份和行动终止，明示遗体为独立环境对象；若胜利已成立，余下处理仍立即停止 |
| 名词位使用复合短语并指定多个端点 | R18–R20 | 每个新增词义需要实体卡；端点与配对必须明示，筛选条件不免费变成事件施法 |
| 当前刻的效果将另一道法术剩余冷却减至可释放 | R21–R23 | 已完成部分不回滚；该改期最早进入下一刻调度，实际释放完成后按基础冷却继续 |
| 一条法术释放时长跨越多刻 | R24 | 开始时竞争共享槽并结算一次直接效果；释放长度参与自身周期，不把视觉持续当作每刻新释放 |
| 状态阶段产生属于环境阶段的反应，之后形成传播 | R26–R28 | 已错过环境阶段，进入下一刻；传播按刻推进，同根因、同对象、同规则在同刻不重复触发 |
| 反应覆盖自己或友军 | R29 | 范围与能力满足即适用，保护须由明示条件或效果提供 |
| 复制实体并将其残留带向战后 | R30–R32、C06 | 不复制配置权限或绕过产出限制；环境与过程变化默认本场结束，合法已领取资源按既有跨战规则保留 |

## 后续工作

1. 填写对象、能力、词卡与过程窗口条目，注明合法和失败情境；后置机制按既有范围启动。
2. 按数值重设计任务提出对局目标、参数和资源规模，保留理由与来源。
3. 用具体配置作逐刻与跨战验证，再验证玩家能否解释对象和时间变化。

## 本次文件范围

共53份文件，只提交以下范围。

- [README.md](../../../README.md)
- [docs/control-center.md](../../../docs/control-center.md)
- [workspaces/game-002/AGENTS.md](../AGENTS.md)
- [workspaces/game-002/CONTEXT.md](../CONTEXT.md)
- [workspaces/game-002/README.md](../README.md)
- [workspaces/game-002/docs/README.md](README.md)
- [workspaces/game-002/docs/control-center.md](control-center.md)
- [workspaces/game-002/docs/design-decisions-needed.md](design-decisions-needed.md)
- [workspaces/game-002/docs/numerical-redesign.md](numerical-redesign.md)
- [workspaces/game-002/docs/semantic-world-rules-adoption.md](semantic-world-rules-adoption.md)
- [workspaces/game-002/docs/semantic-world-target-list-adoption.md](semantic-world-target-list-adoption.md)
- [workspaces/game-002/game-design-workflow/README.md](../game-design-workflow/README.md)
- [workspaces/game-002/game-design-workflow/core-concept.md](../game-design-workflow/core-concept.md)
- [workspaces/game-002/game-design-workflow/decision-log.md](../game-design-workflow/decision-log.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-automatic-battle-boundaries.md](../game-design-workflow/draft-changes/D-2026-09-09-automatic-battle-boundaries.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-casting-design-pillars.md](../game-design-workflow/draft-changes/D-2026-09-09-casting-design-pillars.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-core-system-stable-baseline.md](../game-design-workflow/draft-changes/D-2026-09-09-core-system-stable-baseline.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md](../game-design-workflow/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-timeline-backpack-core.md](../game-design-workflow/draft-changes/D-2026-09-09-timeline-backpack-core.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-semantic-world-executable-rules.md](../game-design-workflow/draft-changes/D-2026-09-10-semantic-world-executable-rules.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-single-release-target-list.md](../game-design-workflow/draft-changes/D-2026-09-10-single-release-target-list.md)
- [workspaces/game-002/game-design-workflow/draft-changes/README.md](../game-design-workflow/draft-changes/README.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-instance-and-conditional-binding.md](../game-design-workflow/evaluations/E-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-executable-rules.md](../game-design-workflow/evaluations/E-2026-09-10-semantic-world-executable-rules.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md](../game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/evaluations/README.md](../game-design-workflow/evaluations/README.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/README.md](../game-design-workflow/idea-inbox/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md](../game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md](../game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md](../game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md](../game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md](../game-design-workflow/idea-materials/M-2026-09-06-compositional-spells-and-word-meaning.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md](../game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md](../game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md](../game-design-workflow/idea-materials/M-2026-09-06-spell-effect-sources-and-modifiers.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md](../game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-reference-availability.md](../game-design-workflow/idea-materials/M-2026-09-06-summon-reference-availability.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md](../game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md](../game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md](../game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-battlefield-state-change-expression.md](../game-design-workflow/idea-materials/M-2026-09-10-battlefield-state-change-expression.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md](../game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-materials/README.md](../game-design-workflow/idea-materials/README.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-instance-and-conditional-binding.md](../game-design-workflow/idea-proposals/P-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-executable-rules.md](../game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-executable-rules.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md](../game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/README.md](../game-design-workflow/idea-proposals/README.md)
- [workspaces/game-002/research/03-product-case-studies/2026-09-09-prebattle-ui-reference.md](../research/03-product-case-studies/2026-09-09-prebattle-ui-reference.md)

## 文档检查

本次53份文件通过UTF-8严格解码，713处相对链接全部可解析。正式素材中R01–R32连续、无重复，32条规则与用户已选推荐逐字对应；核心、正式素材和采纳文本包含一致的执行框架摘要。正式素材实数及索引均为44，inbox实数及索引均为14。

现用核心、术语、素材、问题入口与项目UI适用说明中，不再保留位置无条件固定、禁止独立遗体、运行时间无条件固定或排序框架待定的冲突表述。采纳前的建议、替代方向、提案/评估和检查记录明确标为阶段证据。Git补丁空白检查通过。本轮没有游戏实现、参数模拟或玩家测试结论。
