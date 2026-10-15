# 言咒接入工作台前的结构整理

2026-10-14。项目game-002。文档角色：WorkspaceMaintenanceRecord。依据用户“开始清理结构问题”，整理存储、导航与恢复入口；设计资格、采纳范围及运行证据沿原记录。

## 文件归位

| 原位置（相对设计仓库） | 当前位置 | 处理 |
| --- | --- | --- |
| `yanzhou/inbox/2026-10-08-action-cards-mark-system.md` | `yanzhou/sources/inbox/2026-10-08-action-cards-mark-system.md` | 原字节保留，本机未跟踪 |
| `yanzhou/inbox/2026-10-08-action-cards-pool-design.md` | `yanzhou/sources/inbox/2026-10-08-action-cards-pool-design.md` | 原字节保留，本机未跟踪 |
| `yanzhou/inbox/2026-10-08-action-cards-stage-delivery.md` | `yanzhou/sources/inbox/2026-10-08-action-cards-stage-delivery.md` | 原字节保留，本机未跟踪 |
| `yanzhou/inbox/2026-10-08-artifact-augment-effects.md` | `yanzhou/sources/inbox/2026-10-08-artifact-augment-effects.md` | 原字节保留，本机未跟踪 |
| `yanzhou/inbox/2026-10-08-mark-system-rules-detailed.md` | `yanzhou/sources/inbox/2026-10-08-mark-system-rules-detailed.md` | 原字节保留，本机未跟踪 |
| `yanzhou-systems-design-guidance-2026-10-11.md` | `yanzhou/sources/inbox/2026-10-11-systems-design-guidance-draft.md` | 原字节保留，本机未跟踪 |
| `yanzhou/design/systems/augment-system-archive.md` | `yanzhou/sources/inbox/2026-10-08-augment-system-archive.md` | 原字节保留，本机未跟踪 |
| `game-design-workflow/templates/overall-system-framework-template.md` | `C:/YZRecovery/2026-10-14-012411/local-unclassified/overall-system-framework-template.md` | 原字节保留，本机未跟踪 |

7份言咒原稿进入标准sources/inbox；原“System Archive”稿退出现行design目录，作为来源保存。根指导稿与已有外部指导来源快照哈希不同，分别保留。旧source记录中的路径和哈希保持原义，可通过本表定位。

共享模板目录中的已填写稿转存本机待分类区，未认定其属于言咒或独立肉鸽，也未登记为通用模板。`docs/plans/2026-08-21-three-week-vertical-slice-development-plan.docx`原位保留并备份，项目归属Unknown；没有读取或发布其正文。

原稿与待分类文件不随本轮提交发布。新旧路径、原SHA-256和状态见[元数据清单](2026-10-14-yanzhou-structure-cleanup.json)。

## 导航校准

- 根README与工作区地图改用现有项目技能入口，保留用户对旧技能工作台与工具文件的删除。
- 项目注册及探索AGENTS同步DIR-037、DIR-038已分配事实；后续编号统一从探索README查询，当前下一编号为DIR-039。
- 项目首页从版本摘录改为引用版本基准；视觉入口连接开发索引、资产接入与阶段计划，早期HTML／模型保留各自批次身份。
- 文件索引接入本轮清理及恢复记录，不另建一份设计、问题或任务数据库。

## 本机恢复副本

恢复根：`C:/YZRecovery/2026-10-14-012411`。Git基线为设计仓库`a00fc56fc45fca189fbf49152d1f638c01043aea`及实现仓库`a2dc8a69475762643f1606dc969f09479641fa02`。

| 备份来源 | 已逐文件核对数量 | 字节量 |
| --- | ---: | ---: |
| `E:/Project/game/yanzhou` | 647 | 87.3 MiB |
| `E:/Project/yanzhou-godot` | 11584 | 10714.5 MiB |
| `E:/Project/yanzhou-battle-3d` | 6112 | 1563.8 MiB |
| `E:/Project/yanzhou-godot-baselines` | 454 | 419.6 MiB |
| `E:/Project/game/.git/codex-tasks` | 135 | 1.3 MiB |

另保留两仓库全部Git引用的bundle、开始时的状态、暂存／未暂存补丁及全部未提交文件副本。文件副本与源件逐一核对SHA-256；完整逐文件manifest留在本机恢复根，不随Git发布。该副本位于同机C盘，不代表异机或离线灾备。

恢复操作与工程边界见[Godot恢复说明](E:/Project/yanzhou-godot/docs/coordination/2026-10-14-workspace-recovery.md)。本轮没有备份凭据、原生CLI私有历史或无关第三方参考程序。

## 检查

检查13份本轮Markdown的206处本地链接及章节定位，错误0；8项归位／转存哈希全部一致。两仓库开始时的83项未提交文件／删除状态保留，迁移项按记录的新位置核对。

从两个Git bundle在新目录恢复固定提交、补丁和全部原有未提交输入，逐项哈希／删除状态核对通过；另恢复引擎项目、运行材质、Windows包、原始证据和工具程序5类样本并核对哈希。全部18,932份文件副本在保全时已逐一核验。Git差异空白检查通过；完整本机检查记录位于恢复根verification.json。

以上为静态文档、文件完整性与恢复检查；玩法、引擎运行、性能及真人体验NotRun。
