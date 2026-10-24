# 言咒开发入口

2026-10-23。**先完善首场核心玩法，再开始同一游戏的2D表现。** 本页是开发接手和当前能力的唯一汇总；旧3D排程已结束使用，2D具体展示合同与工程尚未建立。

## 新agent先读这5份

默认开发接手记CUSTOM，固定启动时完整提交。核心全读，任务按行为展开；用户范围优先。已注入的AGENTS计一次。术语、基准、问题只查涉及条目，不默认全文加载。

| 顺序 | 文件（相对game根） | 回答什么 |
| --- | --- | --- |
| 1 | [AGENTS.md](../../AGENTS.md) | 仓库边界与操作底线 |
| 2 | [yanzhou/AGENTS.md](../AGENTS.md) | 本项目路由与写入职责 |
| 3 | [yanzhou/development/README.md](README.md) | 当前能力、下一步与补读入口 |
| 4 | [yanzhou/design/GDD.md](../design/GDD.md) | 唯一核心正文：整款游戏、当前范围与关键行为 |
| 5 | [yanzhou/development/task-pack.md](task-pack.md) | 选行为包、按条件展开细则、形成最小交接输入 |

启动包只包含上述5份；任务包及被触发的细则另计。明确完整GDD时按READ-1的53份正文包读取，来源沿革不在其中。字符统计按实际固定提交计算，不在多个入口复制易过期总量；不是token数，也不含工具、聊天、技能或代码。

## 任务确定后再补什么

| 任务 | 按需补读；先列具体文件与版本 |
| --- | --- |
| 改规则或完善首场 | [设计流程](../../docs/design-workflow.md)、相关rules／参数／案例／验收与对应正式来源；查决定只读相关ID，不默认加载整份decision-log |
| 实现已定行为 | [行为包与条件展开](task-pack.md)＋适用[开发规范](development-standard.md)；维护Godot再读[工程接手](E:/Project/yanzhou-godot/docs/development-handoff.md)及对应代码 |
| 新二维方向 | 先闭合[主系统问题](../governance/questions.md#开发前先看)，再限定与CORE-063的关系；建立探索时才读[READ-1](../exploration/start.md)及[探索AGENTS](../exploration/AGENTS.md) |
| 改工作台或登记方式 | [展示规格](workbench-spec.md) · [本机使用](workspace.md) |
| 制作或复用资产 | [资产接入](asset-readiness.md)、DA-1及所选AS／DM原件；不读全部制作史 |
| 人工理解／审校行为 | [场景审阅](design-review.md)，正常故事、反例与图示；意见回同轮 |
| 了解项目与人机协作 | [情景讲解与提示词](development-guide.md) · [阶段计划](production-plan.md) |
| 查3D留下的制作经验 | [制作与验证经验](development-standard.md#制作与验证经验) |

不默认加载历史批次、逐席位报告、旧测试交接、整个来源库或全部GDD。明确要求完整GDD时按READ-1的53文件清单执行，不能把核心正文阅读称作全量审查。明确禁止自动扩读的合同仍须遵守；缺材料先列缺口。

## 当前事实

| 对象 | 已有结果 | 仍缺什么或不能推断什么 |
| --- | --- | --- |
| 构思与规则 | GDD 2.8／GDD-0，CORE-065回合、手牌、付费整理与第10轮起疲劳已采纳；旧案例固定输入保留 | CORE-065实现与新验收尚未执行，仅完成文档一致性核对；主系统全部闭合、全局内容与平衡成立也不能据此推断 |
| 下一设计工作 | 同一游戏新表现、首场核心优先、按变化裁剪小循环已确认 | 下一项是新首场真实5位敌表与完整战斗输入；FB-Q01／02选择价值仍待检验，2D展示条款未采纳 |
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

最新源码HEAD、已交付运行源码、设计版本分开记录。第三方资产再分发条件沿原记录，不能由本机可查看推断。技术细节与旧失败经验统一在Godot工程接手；本轮未修改或运行游戏；CORE-065回合／整理／暂停／保存行为须另行实现取证，旧0.4与B13不能作为本版通过证据。

旧过程文档与DQ表已退出当前目录；历史原文可在game固定提交`f21058a54b096e0d6ad2b3b559e352b67596c239`按原路径用`git show`读取。资产原件、manifest和正式设计来源保留；旧失败、NotRun与案例限制不会因清理变成通过。本次不另建去向表。
