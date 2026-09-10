# SW02两种引用模型采纳交付

日期：2026-09-10。状态：Accepted / Reference Model。决策：G002-CORE-008。核心：Core Concept v0.6。证据：Hypothesis。

## 已完成的规则确认

- 实例绑定保持战前指定身份，失效跳过，不自动指向同名或其他对象。
- 条件绑定保持战前选择条件，每次释放匹配当前世界，符合条件的新生对象可以参与。
- 两种方式并存；词义、法杖允许范围、材料与当前合法性等约束继续适用。
- 名单确定时点、排序、具体条件表达及SW03–SW07细则仍待确认；数值重新设计。

## 来源与正式设计链

- [SW02具体提问及用户确认](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)。
- [合格引用素材](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)。
- [提案](../game-design-workflow/idea-proposals/P-2026-09-10-instance-and-conditional-binding.md)、[评估](../game-design-workflow/evaluations/E-2026-09-10-instance-and-conditional-binding.md)与[采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-instance-and-conditional-binding.md)。
- [核心](../game-design-workflow/core-concept.md)、[词汇](../CONTEXT.md)和[决策记录](../game-design-workflow/decision-log.md)。

## 表述统一范围

当前规则、预览、敌人失效、召唤引用、接口、数值输入和项目入口均区分实例身份固定与条件结果可变。实例既定顺序仍适用，条件名单的时点与排序明确列为待决，未把整场固定集合继续作为全部法术的共同约束。

五份标为Current Applicability的配置说明同步当前引用规则。C01–C08和SW01的采纳时文本、当次评估及检查报告保留为来源证据，并链接本次后续决定；不把其中当时的待决项作为当前问题。原始快照不改写，采纳前工作文件可从Git提交04820cd追溯。

## 当前待决

SW02-A推荐在完整法术开始处理时确定一次直接名单，此后不重选或追加；逐对象仍检查当前合法性与材料，本次新生或新符合条件的对象留到后续释放。这只是候选；排序、重叠引用、间接连锁与多刻释放细则仍独立设计。当前入口为[决定清单](design-decisions-needed.md)。

## 本次文件清单

新建引用素材、提案、评估、Draft Change与本记录；其余为相关规则及入口同步：

- [README.md](../../../README.md)
- [docs/control-center.md](../../../docs/control-center.md)
- [workspaces/game-002/AGENTS.md](../../../workspaces/game-002/AGENTS.md)
- [workspaces/game-002/CONTEXT.md](../../../workspaces/game-002/CONTEXT.md)
- [workspaces/game-002/README.md](../../../workspaces/game-002/README.md)
- [workspaces/game-002/docs/control-center.md](../../../workspaces/game-002/docs/control-center.md)
- [workspaces/game-002/docs/design-alignment-audit.md](../../../workspaces/game-002/docs/design-alignment-audit.md)
- [workspaces/game-002/docs/design-decisions-needed.md](../../../workspaces/game-002/docs/design-decisions-needed.md)
- [workspaces/game-002/docs/numerical-redesign.md](../../../workspaces/game-002/docs/numerical-redesign.md)
- [workspaces/game-002/docs/semantic-world-scope-adoption.md](../../../workspaces/game-002/docs/semantic-world-scope-adoption.md)
- [workspaces/game-002/game-design-workflow/README.md](../../../workspaces/game-002/game-design-workflow/README.md)
- [workspaces/game-002/game-design-workflow/core-concept.md](../../../workspaces/game-002/game-design-workflow/core-concept.md)
- [workspaces/game-002/game-design-workflow/decision-log.md](../../../workspaces/game-002/game-design-workflow/decision-log.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-automatic-battle-boundaries.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-automatic-battle-boundaries.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-casting-design-pillars.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-casting-design-pillars.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-core-system-stable-baseline.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-core-system-stable-baseline.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-timeline-backpack-core.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-09-timeline-backpack-core.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-accept-design-decisions.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-accept-design-decisions.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-current-design-alignment.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-current-design-alignment.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/draft-changes/README.md](../../../workspaces/game-002/game-design-workflow/draft-changes/README.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/evaluations/README.md](../../../workspaces/game-002/game-design-workflow/evaluations/README.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md](../../../workspaces/game-002/game-design-workflow/idea-inbox/2026-09-05-yanzhou-core-combat.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/README.md](../../../workspaces/game-002/game-design-workflow/idea-inbox/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-timeline-schedule-preview.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-defeated-enemy-target-and-state-lifecycle.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-coexistence-and-field-capacity.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-reference-availability.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-reference-availability.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-summon-word-references-and-target-locking.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-materials/README.md](../../../workspaces/game-002/game-design-workflow/idea-materials/README.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/README.md](../../../workspaces/game-002/game-design-workflow/idea-proposals/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-instance-and-conditional-binding.md](../../../workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-instance-and-conditional-binding.md](../../../workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-instance-and-conditional-binding.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-instance-and-conditional-binding.md)
- [workspaces/game-002/docs/semantic-world-binding-adoption.md](../../../workspaces/game-002/docs/semantic-world-binding-adoption.md)

## 检查记录

已检查所列45份文档：UTF-8有效，732处相对链接均可解析，正式素材实数与索引均为43，补丁空白检查通过。核心、引用素材和Draft Change包含完全一致的引用规则正文；现行规则与入口不再把整场固定对象集合作为通用限制，当前问题统一为SW02-A。

本轮没有编写或运行实现、数值模拟与玩家测试，模型和体验证据保持Hypothesis。
