# 言咒开发入口

2026-10-18。**先完善首场核心玩法，再开始同一游戏的2D表现。** 本页是开发接手和当前能力的唯一汇总；旧3D排程已结束使用，2D具体展示合同与工程尚未建立。

## 新agent先读这8份

默认用于开发接手／主系统完善，记CUSTOM并固定启动时HEAD。下列清单含构思主系统，不递归打开链接；用户指定范围优先。已注入的AGENTS计一次，不必重复读取。启动包用于理解和选任务，具体实现前仍须补齐相关细则。

| 顺序 | 文件（相对game根） | 回答什么 |
| --- | --- | --- |
| 1 | [AGENTS.md](../../AGENTS.md) | 仓库边界与操作底线 |
| 2 | [yanzhou/AGENTS.md](../AGENTS.md) | 本项目路由与写入职责 |
| 3 | [yanzhou/development/README.md](README.md) | 当前能力、下一步与补读入口 |
| 4 | [yanzhou/design/core-design.md](../design/core-design.md) | 构思主系统：循环、系统关系、玩家取舍 |
| 5 | [yanzhou/CONTEXT.md](../CONTEXT.md) | 领域术语，避免把同一个词理解成不同机制 |
| 6 | [yanzhou/design/baseline.md](../design/baseline.md) | 当前采纳版本和适用范围 |
| 7 | [yanzhou/governance/questions.md](../governance/questions.md) | 真正开放的问题，先处理首场核心缺口 |
| 8 | [yanzhou/development/iteration-spec.md](iteration-spec.md) | 一轮怎样定义、制作、审阅和收口 |

**预计默认启动约2.5万字符／8文件。** 若明确要求完整GDD，56份GDD与启动包去重，加READ-1及探索操作规则，共65份、约14.2万字符。维护既有Godot再加工程README与接手文档2份、约0.6万字符；任务细则、开发规范及相关代码另按范围计入。 按UTF-8文本解码后的Unicode字符数计，含空白、换行统一LF；不是token数。只统计上述文件，不含系统指令、工具定义、聊天、技能或具体任务代码。

## 任务确定后再补什么

| 任务 | 按需补读；先列具体文件与版本 |
| --- | --- |
| 改规则或完善首场 | [设计流程](../../docs/design-workflow.md)、相关rules／参数／案例／验收与对应正式来源；查决定只读相关ID，不默认加载整份decision-log |
| 实现已定行为 | [开发规范](development-standard.md)＋所实现行为的rules、案例、参数与验收；维护Godot再读[工程接手](E:/Project/yanzhou-godot/docs/development-handoff.md)及对应代码 |
| 新二维方向 | 先闭合[主系统问题](../governance/questions.md#开发前先看)，再限定与CORE-063的关系；建立探索时才读[READ-1](../exploration/start.md)及[探索AGENTS](../exploration/AGENTS.md) |
| 改工作台或登记方式 | [展示规格](workbench-spec.md) · [本机使用](workspace.md) |
| 制作或复用资产 | [资产接入](asset-readiness.md)、DA-1及所选AS／DM原件；不读全部制作史 |
| 了解开发全流程 | [开发解释](development-guide.md) · [阶段计划](production-plan.md) |
| 查3D留下的设计与制作经验 | [主系统与3D复盘](../governance/development-review-2026-10-18.md) |

不默认加载历史批次、逐席位报告、旧测试交接、整个来源库或全部GDD。明确要求完整GDD时按READ-1的56文件清单执行，不能把核心摘要称作全文审查。明确禁止自动扩读的合同仍须遵守；缺材料先列缺口。

## 当前事实

| 对象 | 已有结果 | 仍缺什么或不能推断什么 |
| --- | --- | --- |
| 构思与规则 | GDD 2.6／GDD-0，CORE-060—063及physical-table.2；EX-001和EX-002各自固定 | 主系统全部闭合、全局内容与平衡成立 |
| 下一设计工作 | 同一游戏新表现、首场核心优先、按变化裁剪小循环已确认 | FB-Q01主动调度、FB-Q02积累兑现、首批内容与取得链仍待设计；2D展示条款未采纳 |
| 完整单战0.4 | 旧界面胜败、事件保存恢复、播放／回看与失焦的限定证据 | 新3D或未来2D同等回归 |
| 最新3D预览B13 | 资源适配、两档源码／复制包检查与指定实图复核 | OS实体输入、长测、听感、用户视觉接受、完整新单战或真人理解通过 |
| 标准卡面／少文字主桌 | [卡面文字](../visual/standard-card-2026-10-17/README.md)；C1短名／全称、C2主体图＋固定效果、C3条件图形／详情分支已确认；[少文字候选](../sources/inbox/2026-10-17-minimal-battle-ui.md)有局部HTML和单图 | 卡面HTML／效果／实装未完成，少文字整套方案未采纳；不重问C1—C3 |
| 工作台 | 当前、循环、审阅、资产、地图、使用六页；原文预览、执行合同、Files | 每轮记录仍人工维护；会话active／closed不是功能完成，没有自动阶段同步或全资产画廊 |

## 固定运行与审阅入口

| 版本 | 固定输入与可查看入口 | 证据边界 |
| --- | --- | --- |
| GODOT-EX002-0.4 | 源码`9c50458a56a38f0c6ebd001d9e6a3ef34382adaa`；[运行包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe) · [交付JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json) | 旧界面完整单战底座 |
| B07／0.5候选 | 组合`e0077ffa10d22ad1c9dd91e8037aa2c021409098`；[保全JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-07-preserved-evidence.json) | 首次新建113.127ms尖峰Fail；候选长测中断；未登记0.5正式交付 |
| B13 | 运行`e975de8bdbbe70591d4099c34b799e76c4bff1d7`，设计`151a9a8bb8b100994607e37a66c5314886f66a22`；[包](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe) · [证据JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-13-evidence.json) | 45候选适配，6模型／9声音接主桌；各档80项主桌、87项检视，D复核16图；不是全部设计验收 |
| UI-REVIEW-02 | [工具说明](E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/README.md) | B13固定实图与HTML模拟；浏览器意见不自动采纳或接入游戏 |

最新源码HEAD、已交付运行源码、设计版本分开记录。第三方资产再分发条件沿原记录，不能由本机可查看推断。技术细节与旧失败经验统一在Godot工程接手；本轮文档清理未重跑游戏。

旧过程文档与DQ表已退出当前目录；历史原文可在game固定提交`f21058a54b096e0d6ad2b3b559e352b67596c239`按原路径用`git show`读取。资产原件、manifest和正式设计来源保留；旧失败、NotRun与案例限制不会因清理变成通过。本次不另建去向表。
