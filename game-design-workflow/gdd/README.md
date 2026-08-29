# GDD 文档区

本目录保存按照 [GDD 写作要求与模板](../templates/gdd-writing-requirements-and-template.md)形成的具体 GDD。

GDD 只保存核心玩法设计与设计决策：玩家处境、动作、规则、反馈、取舍、体验目标、设计假设和验证标准。代码架构、引擎、模块、脚本、编程数据结构、实现完成度与构建说明统一记录在[代码开发进度索引](../../docs/code-development-index.md)或对应代码仓库。

## 硬性规则

- 用户提出“写 GDD、需求文档、系统规格或玩法设计文档”时，agent 必须主动采用统一模板，并先确认目标完成度：`GDD-0 / GDD-1 / GDD-2`。
- 写作前必须检索 `idea-materials/` 和 `idea-inbox/`。
- 正式素材作为可纳入候选主动提出；inbox 内容只能作为未确认候选，不能直接写入 GDD。
- 用户选中 inbox 候选后，先用 `grill-with-docs` 完成资格确认并晋级正式素材库。
- GDD 中的 `Hypothesis`、`Unknown` 和 `Out of Scope` 必须显式标记。
- 写入 GDD 不等于写入 `core-concept.md`；正式采纳仍走 Proposal、Evaluation、Draft Change 和 Decision Log。
- 不允许创建“客户端 GDD”“代码设计 GDD”或用 GDD 记录开发进度；实现只能作为设计验证证据被链接。

## 文件命名

```text
GDD-YYYY-MM-DD-short-name.md
```

玩法功能或游戏系统拆分文档也使用相同前缀，并在文档控制表中填写稳定的文档 ID。

## 当前文档

- [GDD-BATTLE-003：字素卡、行动卡与统一情境战斗](GDD-2026-08-29-battle-system-003-unified-glyph-action-events.md) — `GDD-1 / Evaluation`，**当前战斗机制验证方向**；规则评估已完成，等待最小原型。
- [GDD-BATTLE-002：字素合成战斗系统](GDD-2026-08-22-glyph-synthesis-combat-system.md) — `GDD-1 / Evaluation`，003 的前置基线；保留字素与内容语义，双轨合成和旧行动经济不再作为当前写作基线。
- [GDD-BATTLE-001：唯一核心卡成语组合战斗系统](../../archive/2026-08-24-gdd-code-separation/GDD-2026-08-21-card-battle-system.md) — `Parked / Archived`，保留旧流程下的设计与代码证据。

代码进度入口：[代码开发进度索引](../../docs/code-development-index.md)。原 `GDD-CLIENT-001` 已在 2026-08-24 迁出本目录，历史内容仍可通过 Git 记录追溯。
