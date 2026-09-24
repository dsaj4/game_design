# 探索项目注册表

登记版本：v1.2。更新日期：2026-09-23。权威范围：探索 Project ID、路径、隔离权限和生命周期。

创建依据：[WS-004](../../docs/workspace-decisions.md)、[ADR-0002](../../docs/adr/0002-game-exploration-workspaces.md)。用户已确认建立以下两个项目；这不构成玩法 Accepted。路径均相对仓库根。

| Project ID | 工作区根 | 用途 | 生命周期 | 背景状态 | 当前背景包 |
| --- | --- | --- | --- | --- | --- |
| game-002-optimization | yanzhou/exploration/optimization/ | 基于 game-002 背景探索优化 | Active / Core Design Context Active | Pack Active | baseline-2026-09-09-001 |
| new-roguelike | exploration/new-roguelike/ | 独立探索肉鸽设计 | Active / Raw Exploration | Blank Baseline | Not Applicable；不导入 game-002 |

## 权限与入口

| Project ID | 可读的项目背景 | 默认写入范围 | 正式设计输出 |
| --- | --- | --- | --- |
| game-002-optimization | 已激活的本项目背景包；生成时仅按[来源配置](../../yanzhou/exploration/optimization/context/generation-profile.json)读取 game-002 指定提交 | 仅 yanzhou/exploration/optimization/ | 本地候选与 GDD；回写 game-002 必须走 Draft Change |
| new-roguelike | 自身 context、明确选择的共享方法与媒体来源 | 仅 exploration/new-roguelike/ | 本地候选与 GDD；不能回写或继承另一游戏 |

- [优化项目入口](../../yanzhou/exploration/optimization/README.md)
- [新肉鸽项目入口](../new-roguelike/README.md)
- 共享评判框架只能按版本和适用范围选用，不能等同项目背景。
- 未激活背景包时，优化项目可完善问题和生成背景包，不能声称已经掌握完整 game-002 规则。
- 独立原型与模拟按各项目记录；不得继承根旧实验完成状态。优化项目时间背包局部吸收见方向吸收表，不表述为全部无采纳。

## 更新约定

新增项目、改变读写边界和跨项目回写权限属于管理变更，记录来源后同步根工作区地图。背景包激活时更新本表及项目 context 入口，记录 pack ID、source commit 和验证记录；已有包保持不变。当前活动包只提供核心设计背景，不代表玩法 Accepted。

## 方向与显式来源

[27方向索引](../../yanzhou/exploration/optimization/directions/README.md)与[基线/吸收](../../yanzhou/exploration/optimization/directions/baseline-and-absorption.md)登记各批次差异。用户明确指定的来源可以按当轮范围作为补充；必须登记提交及摘要，未指定时仍使用活动包。独立肉鸽保持Blank Baseline，本次未导入任何言咒方向。

## layout.1路径迁移

用户明确授权将言咒项目集中到yanzhou。game-002-optimization的物理根改为yanzhou/exploration/optimization/，资格、来源、预算和回写边界不变。v2背景包不重生成；新路径生成配置为[generation-profile-v3.json](../../yanzhou/exploration/optimization/context/generation-profile-v3.json)，仅供未来明确任务使用。new-roguelike继续在原根。
