# GDD 文档区

本目录保存按照 [GDD 写作要求与模板](../templates/gdd-writing-requirements-and-template.md)形成的具体 GDD。

## 硬性规则

- 用户提出“写 GDD、需求文档、系统规格或玩法设计文档”时，agent 必须主动采用统一模板，并先确认目标完成度：`GDD-0 / GDD-1 / GDD-2`。
- 写作前必须检索 `idea-materials/` 和 `idea-inbox/`。
- 正式素材作为可纳入候选主动提出；inbox 内容只能作为未确认候选，不能直接写入 GDD。
- 用户选中 inbox 候选后，先用 `grill-with-docs` 完成资格确认并晋级正式素材库。
- GDD 中的 `Hypothesis`、`Unknown` 和 `Out of Scope` 必须显式标记。
- 写入 GDD 不等于写入 `core-concept.md`；正式采纳仍走 Proposal、Evaluation、Draft Change 和 Decision Log。

## 文件命名

```text
GDD-YYYY-MM-DD-short-name.md
```

功能或系统拆分文档也使用相同前缀，并在文档控制表中填写稳定的文档 ID。

## 当前文档

- [GDD-BATTLE-001：唯一核心卡成语组合战斗系统](GDD-2026-08-21-card-battle-system.md) — `GDD-1 / Evaluation`，包含当前战斗规则、首批羊/舟组合、费用模型、自动化测试与胜率模拟协议。
- [GDD-WORLD-001：共享地图—战斗—撤离闭环](GDD-2026-08-22-shared-map-combat-loop.md) — `GDD-0 / Evaluation`，定义有限人工节点图、探索状态、战斗接口、隐藏撤离点与最小验证问题。
