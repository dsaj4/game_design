# 设计决定与后续工作

日期：2026-09-10。状态：G002-CORE-011简单对象交互范围已采纳；Core Concept v0.6，证据Hypothesis。当前入口：[内容总览](semantic-world-content-index.md)。

## 当前已确定

| 范围 | 当前规则 | 依据 |
| --- | --- | --- |
| 战前与自动循环 | 完整库存构句，一卡一位置且同场一法术，一法术一法杖；首次冷却起点0–10刻 | [核心](../game-design-workflow/core-concept.md) |
| 引用与名单 | 实例保持身份，条件战前固定；每次开始确定一次直接名单，不追加、不重选、不补位 | [引用素材](../game-design-workflow/idea-materials/M-2026-09-10-instance-and-conditional-binding.md) |
| 时间与结果 | 释放开始仲裁，当前冷却改期最早下一刻；生命伤害打断、四阶段、整句成功与胜利终止 | [执行规则](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md) |
| 对象交互 | 以数量、强度、剩余时间或状态改变为主；点燃/冰冻等简单变化进入当前内容设计 | [简化素材](../game-design-workflow/idea-materials/M-2026-09-10-simple-object-interactions.md) |
| 法术生成物 | 增加真实火焰、雷电、冰霜对象；身份/来源/窗口与宿主状态、演出分开 | 同上 |
| 资源收集 | 法术作用于合格对象后对象掉卡；资格与同名额度先检查，合法卡进入待领取整体收益 | [收益素材](../game-design-workflow/idea-materials/M-2026-09-06-normal-combat-word-rewards.md) |
| 数值 | 全部重新设计；不使用示例默认值 | [数值任务](numerical-redesign.md) |

## 当前暂缓

- 位移、连接、支撑、独立空间参照、指定飞行方向与玩家指定新受术端点。场景位置与范围判定仍保留。
- 环境材料份额、容器供材/收材、配方/合成、材料转移加工与物体复制。
- 完整召唤/指挥、法杖起始资源与镶嵌细则。
- 燃料、自动传播、导电网络和坍塌等复杂环境机制；简单点燃/冰冻已进入当前设计。

## 已处理的接口

C01伤害/生命支付与反馈、C02逐对象数量/成本及整句成功、C06产出资格、C08词卡时间用于冷却继续适用。C03/C04完整召唤及未来单位占位、C05镶嵌仍后置。C07保留变化的发生/发展/结果表达，其复杂BF机制后置范围依上表；不再把简单点燃/冰冻一并阻挡。

R01–R32保留编号追踪，[现行规则表](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-executable-rules.md)直接陈述收束后的权限。G002-CORE-010是框架采纳记录，G002-CORE-011是当前范围修订；不要求重新回答这32项。

## 下一步内容工作

已完成[第一批具体词义推荐](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-wording.md)：三元素载体、燃烧、冰冻减伤、生成物强度操作和对象有限掉卡，附18词新参数。另有[局部逐刻及24项边界记录](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-paper-checks.md)。当前为Raw Idea / Unqualified，未修改核心采纳范围。

具体推荐C-E1–C-E4已集中列出：元素完成一次作用、冰冻减少直接伤害而保持攻击时点、每个标记初始环境对象一次掉卡及首组参数。它们有可审阅文本但尚未采纳；没有将未知机制写成已确认规则。下一批补普通攻击抵挡、反弹自动归宿与非指定转移的接收/失败/重复规则；完整场景、平衡及玩家验证仍待开展，见[内容入口](semantic-world-content-index.md)。

## 来源

- [本次用户原话与资格确认](../game-design-workflow/idea-inbox/2026-09-10-simple-object-interactions.md)。
- [本次采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-simple-object-interactions.md)与[决策记录](../game-design-workflow/decision-log.md)。
- [C01–C08来源](../game-design-workflow/idea-inbox/2026-09-10-design-interface-questions.md)、[SW01/SW02来源](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)、[R01–R32来源](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-remaining-decisions.md)。
- [本轮交付](semantic-world-simplification.md)及[修改前快照](../../../archive/2026-09-10-game-002-semantic-simplification-inputs/INDEX.md)。
