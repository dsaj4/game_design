# game-002 背景包入口

Project ID：`game-002-optimization`。来源项目：`game-002`。

| 项目 | 当前值 |
| --- | --- |
| 生成规则 | [pack-generation-rules.md](pack-generation-rules.md)，v2（核心设计范围） |
| 来源配置 | [generation-profile.json](generation-profile.json)，v2（6 个来源） |
| 当前背景包 | `baseline-2026-09-09-001` |
| Source commit | `d0c36b9d464680a484f83b234db081b97124b701` |
| 验证结果 | Passed / Core Design Scope |
| 当前用途 | 已激活的核心设计背景；不包含实现、实验或研究计划 |

本包位于 [baseline-2026-09-09-001](baseline-2026-09-09-001/context-pack.md)，包含摘要、来源 manifest、验证记录和六个 Git blob 原始快照。

下一次生成后在此登记唯一活动 pack ID、来源提交、相对路径和验证结果；旧包保持原样。引用包意味着读取当时的背景，不意味着取得来源工作区的写权限。

## layout.1的来源配置

活动包仍为baseline-2026-09-09-001，原v2配置及包文件均保持字节。[新路径配置草稿](generation-profile-v3.json)已映射4项来源；原v2中的first-pass-global-design-baseline和core-numerical-framework-v01两项已不在当前工作区，明确记为Unresolved，因此generation_ready=false，禁止直接生成。未来明确生成任务须先审查这两项的适用来源和固定提交，本轮未自行替换。

本轮没有生成或激活新背景包。冻结来源文件内的相对链接若指向原来源树，按原提交解释，不把它们当现行导航；当前路径见[迁移表](../../../governance/path-map.json)。
