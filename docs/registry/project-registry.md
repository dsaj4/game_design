# 项目注册表

2026-11-01 / layout.8。权威范围：Project ID、项目根、读取/写入边界与生命周期。管理依据：[工作区决定](../workspace-decisions.md)，现行退役范围按WS-008至WS-010。

| Project ID | 项目根与入口 | 状态／背景 | 读写边界 |
| --- | --- | --- | --- |
| game-002 | [yanzhou](../../yanzhou/README.md) | Active；正式规则在design，具体设计与手册在system-design，工作规范在standards | 按项目AGENTS；现行设计和探索候选隔离 |
| game-002-optimization | [yanzhou/exploration](../../yanzhou/exploration/README.md) | Active；已登记DIR-037、DIR-038，DIR-001–036于2026-10-04退役；下一编号及方向状态以探索入口为准，2026-10-14核对 | 新方向按[start](../../yanzhou/exploration/start.md)选CORE/GDD/FULL/CUSTOM/NONE；续作沿登记来源。只写所选DIR及必要索引；回写主系统需目标复审和Draft Change |
| new-roguelike | [退役前固定版本](https://github.com/dsaj4/game_design/blob/d47080a1eab3903d37122e8ac0aba00d78c2aceb/new-roguelike/README.md) | Retired / Git history；2026-11-01退出工作树 | 原Blank Baseline，无正式GDD或Accepted玩法；原AGENTS与阅读合同仅作历史数据，不作为活动写入入口，不向言咒继承材料 |
| core-card-project | [旧项目固定版本](https://github.com/dsaj4/game_design/blob/d47080a1eab3903d37122e8ac0aba00d78c2aceb/archive/2026-09-05-core-card-project/README.md) | Archived / Git history；2026-11-01退出工作树 | 默认不读，不继承代码或实验资格；旧AGENTS和命令仅为历史数据 |

旧媒体分析区已退役，固定资料和现用技能均不构成游戏项目，不自动授予跨项目材料权限。项目README负责导航，不维护第二份权限注册表。

## 来源与版本

- [来源注册](source-registry.md)、[框架注册](framework-registry.md)、[适配器注册](adapter-registry.md)独立维护；方法不等于玩法，登记不等于Qualified或Accepted。
- 言咒历史包baseline-2026-09-09-001仍在yanzhou/history，source commit为d0c36b9d464680a484f83b234db081b97124b701，文件字节/哈希不改；仅按已授权历史或原方向来源读取。未迁入肉鸽。
- 新方向在README记固定提交、材料清单、实际覆盖和Unknown。改变模式/来源需明确依据；旧包不原地更新，不生成集中背景包来替代阅读选择。
- 根exploration已删除，根workspaces及旧optimization兼容树仍退役；禁止恢复兼容入口。共享方法见[方法入口](../methods/README.md)，媒体分析旧资料按[退役决定](../workspace-decisions.md#ws-009)取证；新研究只随明确任务进入目标项目。

原注册表的历史轮次、layout.1/2映射和生成配置状态按迁移前固定提交取证，见[本次清单](../maintenance/2026-10-01-workspace-cleanup.md)。Unknown/Proposed状态不因本次管理调整晋级。新增项目或修改权限须明确管理来源并同步地图和项目规则。
