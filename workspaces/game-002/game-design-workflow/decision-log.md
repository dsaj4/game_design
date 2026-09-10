# game-002 决策记录

## 当前生效决定

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-ADMIN-001 | 2026-09-05 | 建立独立工作区，仅共享方法、结构与规范 | Accepted / Administration | 原始决策完整记录见下方 |
| G002-CORE-006 | 2026-09-09 | 战前完整库存构句、一组合一循环法术、一法术一法杖；配置顺序、固定目标、0–10刻首次冷却与自动循环；同刻四阶段、生命伤害打断冷却、胜利终止、整体战后收益 | Accepted：当前核心的配置与循环依据；Hypothesis | [核心](core-concept.md)、[战前配置适用文本](draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md) |
| G002-DOC-001 | 2026-09-10 | 按用户授权逐份统一文档并保存原始快照；兼容部分保留，接口集中呈现；用户采纳范围按G002-CORE-007与G002-SCOPE-001执行 | Accepted / Documentation；Hypothesis | [文档统一](draft-changes/D-2026-09-10-current-design-alignment.md)、[决定清单](../docs/design-decisions-needed.md) |

## 决策证据索引

G002-ADMIN-001、G002-CORE-001至G002-CORE-006的完整原始决定、日期与状态均保存在[原始决策记录](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/game-design-workflow/decision-log.md)。以下文件是当前适用范围说明，不能当作原始决定原文：

- G002-CORE-001：[施法设计支柱](draft-changes/D-2026-09-09-casting-design-pillars.md)。
- G002-CORE-002：[时间背包编排](draft-changes/D-2026-09-09-timeline-backpack-core.md)。
- G002-CORE-003、004：[自动战斗边界](draft-changes/D-2026-09-09-automatic-battle-boundaries.md)。
- G002-CORE-005：[稳定设计基线](draft-changes/D-2026-09-09-core-system-stable-baseline.md)。
- G002-CORE-006：[战前构句与法杖](draft-changes/D-2026-09-09-prebattle-spell-wand-assembly.md)。

C01–C08按用户批量确认全部处理，当前没有本轮遗留人工冲突。数值重新设计已确认，具体参数与体验证据仍为Unknown / Hypothesis。

## 接口采纳与数值任务

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-CORE-007 | 2026-09-10 | C01伤害/支付分类与独立反馈，C02逐对象材料、公开固定顺序和完整法术成功，C06产出资格前置与产金成本，C08词卡时间合计用于冷却；数值全部重新设计 | Accepted / Core Concept v0.6；Hypothesis | [拟修改与来源](draft-changes/D-2026-09-10-accept-design-decisions.md)、[数值任务](../docs/numerical-redesign.md) |
| G002-SCOPE-001 | 2026-09-10 | C03完整召唤后置，推进时设计战前单位占位与出生位置；C04当前不增加专属引用词卡；C05镶嵌细则与C07 BF1–BF3按推荐后置 | Accepted / Scope；具体机制Unknown | [决定清单](../docs/design-decisions-needed.md)、[合格范围素材](idea-materials/M-2026-09-10-accepted-design-interfaces.md) |

确认前推荐、数值来源与文档验收已封存于[决策输入快照](../../../archive/2026-09-10-game-002-decision-inputs/INDEX.md)，用于追溯，不作为参数基线。

## 语义世界对象范围

| ID | 日期 | 决定 | 状态与证据 | 来源 |
| --- | --- | --- | --- | --- |
| G002-SCOPE-002 | 2026-09-10 | SW01：实体、部件、材料、属性状态、空间关系及飞行物、敌方攻击、法术冷却等过程纳入法术对象设计范围；各类按明确能力开放操作；胜负判定、全局结算顺序等基础规则保持固定 | Accepted / Scope；Hypothesis。具体引用与操作机制待定，Core Concept v0.6基础执行规则继续适用 | [用户确认](idea-inbox/2026-09-10-semantic-world-object-scope.md)、[范围素材](idea-materials/M-2026-09-10-semantic-world-object-scope.md)、[提案](idea-proposals/P-2026-09-10-semantic-world-object-scope.md)、[评估](evaluations/E-2026-09-10-semantic-world-object-scope.md)、[采纳文本](draft-changes/D-2026-09-10-semantic-world-object-scope.md) |

下一步为SW02新生对象引用。SW02–SW07的候选建议尚未采纳；数值重新设计继续执行。
