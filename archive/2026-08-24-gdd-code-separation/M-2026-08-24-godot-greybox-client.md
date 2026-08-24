# M-2026-08-24 Godot 灰盒客户端实现

| 字段 | 内容 |
| --- | --- |
| 素材 ID | `M-2026-08-24-godot-greybox-client` |
| 状态 | `Reclassified / Development Evidence` |
| 来源 inbox | [2026-08-24-godot-greybox-client.md](../../game-design-workflow/idea-inbox/2026-08-24-godot-greybox-client.md) |
| 关联战斗 GDD | [GDD-BATTLE-002](../../game-design-workflow/gdd/GDD-2026-08-22-glyph-synthesis-combat-system.md) |
| 实现工程 | https://github.com/Winterwhite11/fantacy-breakdown-godot-demo （本地：`Fantacy Breakdown/godot-demo/`） |
| 当前记录 | [代码开发进度索引](../../docs/code-development-index.md) |

## 合格摘要

可运行的 Godot 4 灰盒闭环：地图探索 → 遭遇战斗 → 牌堆 UI → 双轨字素合成。它是开发证据，不是合格 GDD 玩法素材，不能因为已经实现就改变设计状态。

## 迁移说明

1. 双轨合成和延迟洗牌属于玩法假设，已移入 `GDD-BATTLE-002`。
2. 场景、全局状态、脚本、数据文件与实现完成度统一进入代码开发进度索引或代码仓库。
3. 本文件仅保留历史追踪，不再作为新 GDD 的正式素材来源。
