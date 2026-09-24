# 探索项目注册表

登记版本：v1.4。更新日期：2026-09-24。权威范围：探索 Project ID、路径、隔离权限和生命周期。

创建依据：[WS-004](../../docs/workspace-decisions.md)、[ADR-0002](../../docs/adr/0002-game-exploration-workspaces.md)。用户已确认建立以下两个项目；这不构成玩法 Accepted。路径均相对仓库根。

| Project ID | 工作区根 | 用途 | 生命周期 | 背景状态 | 阅读入口／历史包 |
| --- | --- | --- | --- | --- | --- |
| game-002-optimization | yanzhou/exploration/ | 基于 game-002 背景探索优化 | Active / Direction Notes | Selectable Reading / READ-1 | [选择阅读材料](../../yanzhou/exploration/start.md)；旧包baseline-2026-09-09-001保留 |
| new-roguelike | exploration/new-roguelike/ | 独立探索肉鸽设计 | Active / Raw Exploration | Blank Baseline | Not Applicable；不导入 game-002 |

## 权限与入口

| Project ID | 可读的项目背景 | 默认写入范围 | 正式设计输出 |
| --- | --- | --- | --- |
| game-002-optimization | 新方向按[start.md](../../yanzhou/exploration/start.md)选择模式与固定版本，未指定时CORE；已有方向续作沿原登记来源。仅显式选择历史时读旧包 | 仅 yanzhou/exploration/所选DIR方向及必要索引 | 方向文件夹保存必要构思；正式输出按本地规则，回写 game-002 必须走 Draft Change |
| new-roguelike | 自身 context、明确选择的共享方法与媒体来源 | 仅 exploration/new-roguelike/ | 本地候选与 GDD；不能回写或继承另一游戏 |

- [优化项目入口](../../yanzhou/exploration/README.md)
- [新肉鸽项目入口](../new-roguelike/README.md)
- 共享评判框架只能按版本和适用范围选用，不能等同项目背景。
- 新方向无需生成或激活旧背景包即可按所选模式启动；只有完整读取GDD包才能声称已读完整GDD，其他范围如实说明。
- 独立原型与模拟按各项目记录；不得继承根旧实验完成状态。优化项目时间背包局部吸收见方向吸收表，不表述为全部无采纳。

## 更新约定

新增项目、改变读写边界和跨项目回写权限属于管理变更，记录来源后同步根工作区地图。若另有背景包生成任务，激活时登记pack ID、source commit和验证记录；已有包保持不变。普通方向阅读范围在其README登记；模式选择不代表玩法Accepted。

## 方向与显式来源

[27方向索引](../../yanzhou/exploration/README.md)与[基线/吸收](../../yanzhou/exploration/comparison.md#背景适配与主系统吸收)登记各批次差异。新方向按阅读模式解析来源清单；已有方向增补必须登记提交及范围，未指定切换时沿原来源。独立肉鸽保持Blank Baseline，本次未导入任何言咒方向。

## layout.1迁移记录（历史）

用户明确授权将言咒项目集中到yanzhou。game-002-optimization当时迁到yanzhou/exploration/optimization/；现用根以后文layout.2为准。原资格、来源与回写边界保留，历史运行预算不自动成为新任务授权。v2背景包不重生成；新路径生成配置为[generation-profile-v3.json](../../yanzhou/history/exploration-2026-09-24/context/generation-profile-v3.json)，仅供未来明确任务使用。new-roguelike继续在原根。


## layout.2按方向保存

G002-DOC-007：取消optimization中间层，P直接为yanzhou/exploration；27方向各自一份README，来源、问题和状态均在其中。[本地操作规则](../../yanzhou/exploration/AGENTS.md)替代旧流程路径映射。固定包baseline-2026-09-09-001迁入yanzhou/history/exploration-2026-09-24/context，保持原字节与source commit d0c36b9d464680a484f83b234db081b97124b701。它仍是已有方向原轮次的历史背景；新方向默认方式以READ-1为准，各已登记方向的显式来源范围继续有效。

旧生成配置和运行记录只作历史证据，未来更新背景须明确任务、完整来源清单与单独验证；generation-profile-v3仍为Draft / SourceMappingIncomplete，不可直接执行。独立new-roguelike无变更。


## READ-1：按模式选择游戏背景

G002-DOC-008新增核心设计浓缩与启动阅读合同。CORE只读core-design；GDD读16份固定包；FULL读全量主系统文本但不自动包含历史与其他方向；CUSTOM按清单；NONE只用本轮输入。必要规则读取与游戏背景分开。用户已选模式即授权该范围，无需再次确认；超范围不得自行扩读。每方向记录固定提交/哈希、实际覆盖与未读缺口，不新建集中运行或背景目录。独立new-roguelike不受本次默认值变更影响。
