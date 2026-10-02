# 项目注册表

2026-10-01 / layout.4。权威范围：Project ID、项目根、读取/写入边界与生命周期。管理依据：[WS-005](../workspace-decisions.md)。

| Project ID | 项目根与入口 | 状态／背景 | 读写边界 |
| --- | --- | --- | --- |
| game-002 | [yanzhou](../../yanzhou/README.md) | Active；正式规则在design | 按项目AGENTS；现行设计和探索候选隔离 |
| game-002-optimization | [yanzhou/exploration](../../yanzhou/exploration/README.md) | Active / Direction Notes；言咒内的探索身份，不是另一个游戏 | 新方向按[start](../../yanzhou/exploration/start.md)选CORE/GDD/FULL/CUSTOM/NONE；续作沿登记来源。只写所选DIR及必要索引；回写主系统需目标复审和Draft Change |
| new-roguelike | [new-roguelike](../../new-roguelike/README.md) | Active / Raw Exploration；Blank Baseline | 与言咒平级且独立；默认NONE，按[本地规则](../../new-roguelike/AGENTS.md)和[阅读范围](../../new-roguelike/exploration/start.md)。没有正式GDD或Accepted玩法 |
| core-card-project | [旧项目归档](../../archive/2026-09-05-core-card-project/README.md) | Parked / Archived | 默认不读不写，不继承代码或实验资格 |

媒体分析区和技能工作台是工具/参考区域，不是游戏项目，不自动授予跨项目材料权限。项目README负责导航，不维护第二份权限注册表。

## 来源与版本

- [来源注册](source-registry.md)、[框架注册](framework-registry.md)、[适配器注册](adapter-registry.md)独立维护；方法不等于玩法，登记不等于Qualified或Accepted。
- 言咒历史包baseline-2026-09-09-001仍在yanzhou/history，source commit为d0c36b9d464680a484f83b234db081b97124b701，文件字节/哈希不改；仅按已授权历史或原方向来源读取。未迁入肉鸽。
- 新方向在README记固定提交、材料清单、实际覆盖和Unknown。改变模式/来源需明确依据；旧包不原地更新，不生成集中背景包来替代阅读选择。
- 根exploration已删除，根workspaces及旧optimization兼容树仍退役；禁止恢复兼容入口。共享方法见[方法入口](../methods/README.md)，媒体分析见[分析区](../../media-analysis-lab/README.md)。

原注册表的历史轮次、layout.1/2映射和生成配置状态按迁移前固定提交取证，见[本次清单](../maintenance/2026-10-01-workspace-cleanup.md)。Unknown/Proposed状态不因本次管理调整晋级。新增项目或修改权限须明确管理来源并同步地图和项目规则。
