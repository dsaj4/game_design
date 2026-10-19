# 言咒开发状态

2026-10-18 · ImplementationIndex。当前工作是**整理规范与主系统，之后再启动2D实现方向**。旧3D制作排程转为保留记录；本轮没有运行游戏或重新验证旧包。

## 当前事实

| 对象 | 已有结果 | 尚不能说明什么 |
| --- | --- | --- |
| 设计基准 | [GDD 2.6／GDD-0、CORE-060—063及physical-table.2](../design/baseline.md)；EX-001回归和EX-002完整单战各自固定 | 主系统全部设计完成、全局内容和平衡已成立 |
| 规则与完整单战 | 0.4包有完整胜败、保存恢复、播放／回看及失焦的限定技术证据 | 新3D／未来2D已经完成同等范围回归 |
| 最新3D运行预览 | B13资源适配，源码与复制包两档各80项主桌、87项检视；D指定16图复核 | OS实体输入、长测、听感、最终美术接受或真人理解通过 |
| 最新UI设计稿 | 标准卡面文字v01；C1—C3已有用户选择；少文字主桌有局部HTML和单图 | 新卡面HTML／效果图／实装完成，少文字候选整包已采纳 |
| 工作台 | 现有卡片与文档预览、执行合同、文件查看；本轮整理入口见[工作台说明](workspace.md) | 会话active／closed等于功能完成，或已实现全自动任务同步 |
| 下一方向 | 用户计划新开2D，先完善主系统 | 已替换CORE-063、已创建2D工程、已决定复用方式 |

## 现在从哪里开始

| 想知道什么 | 入口 |
| --- | --- |
| 一共有哪些规范 | [开发规范与职责总表](development-standard.md) |
| 一轮怎样做、怎样审 | [制作小循环](iteration-spec.md) |
| 工作台该展示什么、现在能做什么 | [工作台展示规格](workbench-spec.md) · [本机使用](workspace.md) |
| 实现了这个还差几步 | [开发解释](development-guide.md) · [阶段与启动条件](production-plan.md) |
| 主系统先完善什么 | [当前问题](../governance/questions.md#开发前先看) |
| 3D期间设计改了什么、留下什么问题 | [主系统与3D复盘](../governance/development-review-2026-10-18.md) |
| 素材能否使用、原件在哪里 | [资产接入](asset-readiness.md) · [AS／DM统一目录](../../docs/registry/demo-assets.md) |
| 真实代码、构建和技术报告 | [Godot工程入口](E:/Project/yanzhou-godot/README.md) |

## 固定交付与未完成证据

以下是各版本的独立证据，不按日期或检查数量合并成“全部通过”。

| 版本 | 固定输入与交付 | 证据范围与保留问题 |
| --- | --- | --- |
| GODOT-EX002-0.4 | 运行源码 `9c50458a56a38f0c6ebd001d9e6a3ef34382adaa`；[包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe) · [原报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-12-batch-06-integration.md) | 旧界面的完整单战与恢复底座，不能替代后来3D表现专项验收 |
| B07／0.5候选 | 组合源码 `e0077ffa10d22ad1c9dd91e8037aa2c021409098`；[保全报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-12-batch-07-integration.md) · [性能报告](E:/Project/yanzhou-godot/docs/reviews/2026-10-12-batch-07-performance.md) | 首次新建113.127ms尖峰Fail；组合包图形／长测因前台切换未完成；未登记0.5正式交付 |
| B13最新3D预览 | 运行源码 `e975de8bdbbe70591d4099c34b799e76c4bff1d7`，设计输入 `151a9a8bb8b100994607e37a66c5314886f66a22`；[本批报告](reports/demoncards-candidates-2026-10-15.md) · [Windows包](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe) | 45候选适配，6模型／9声音接主桌，其他检视；19曲线／13时间轴样例；范围外未验保留 |
| UI-REVIEW-02 | [审阅工具说明](../visual/ui-review-2026-10-15/review-v02.md) · [代码入口](E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/README.md) | B13真实截图及模拟编辑；不是游戏，也未自动接入新标准卡面 |
| 标准卡面文字v01 | [设计入口](../visual/standard-card-2026-10-17/README.md) · [确认来源](../sources/inbox/2026-10-17-standard-card-face.md) | 文字候选，HTML／效果图未制作；当前先完善主系统，之后复核适用方向 |

Godot审阅起点HEAD为`f5c702907cfa157565764435e759611dd471d0cf`，它含后续文档与UI审阅记录；**HEAD不等于B13运行源码**。技术报告给出各自代码、包与资产指纹。外部第三方资产的再分发条件沿原记录，不能由本机可查看推断。

## 历史定位

- 0.1—B13、旧HTML／模型、各次用户反馈及失败原报告留原位；AS／DM身份不重编号。
- 原[完整开发索引](https://github.com/dsaj4/game_design/blob/dbb90b663fbfbb44683f87d444d0fd8e86e08904/yanzhou/development/README.md)按固定提交保留。旧RC1与退役DIR的证据只按原项目、原规则和原版本解释。
- [旧DQ任务表](demo-quality-taskboard.html)保留52项必做／4项后续的原拆分与浏览器本地进度。它是旧3D单战范围参考，不能直接充当2D待办或当前完成率。
- 本次清理与恢复映射见[清理报告](../governance/cleanup-report.md#2026-10-18设计开发规范整理)。
