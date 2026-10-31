# 言咒开发入口

2026-10-31设计同步。**现有CORE-067新2D首场已增加卡牌交互动效：[启动、操作与固定证据](card-motion-2026-10-29.md)。** 悬停／选用抬起、整牌拿起、槽位提示／落定、取消归位、生产入手和本列使用已接通；原两护符生产、五列／列间布牌、支付、后续／打断、疲劳、胜败及保存恢复沿当时CORE-067的EX-004。CORE-068背包布局、固定用途、待料／自动补料和新胜路，以及CORE-069核心可逆装配、独立辅助／叠加仅文档采纳，未接入该实现。卡面、法器与法术声画保持占位；完整材料／回收内容、真人理解与用户接受仍待后续。本页继续是当前能力唯一汇总，旧3D排程已结束使用。

制作链保留[首轮手牌HTML](../visual/first-battle-handflow-2026-10-28/README.md)及本轮新增状态的文字／HTML／关键状态／真实适配。HTML局部证据与引擎完整首场分别固定；程序执行不升级GDD成熟度、平衡或真人体验状态。

运行美术沿[十件逐件imagegen源件v02](../visual/tabletop-components-2026-10-28/imagegen-v02/README.md)，均保持独立原图及独立文字层；新功能延续同一Godot工程。原[静态场景v01](../visual/engine-scene-2026-10-28/README.md)、旧包与固定源件不覆盖，同期卡面／法器设计候选未取代占位。

## 新agent先读这5份

默认开发接手记CUSTOM，固定启动时完整提交。核心全读，任务按行为展开；用户范围优先。已注入的AGENTS计一次。术语、基准、问题只查涉及条目，不默认全文加载。

| 顺序 | 文件（相对game根） | 回答什么 |
| --- | --- | --- |
| 1 | [AGENTS.md](../../AGENTS.md) | 仓库边界与操作底线 |
| 2 | [yanzhou/AGENTS.md](../AGENTS.md) | 本项目路由与写入职责 |
| 3 | [yanzhou/development/README.md](README.md) | 当前能力、下一步与补读入口 |
| 4 | [yanzhou/design/GDD.md](../design/GDD.md) | 唯一核心正文：整款游戏、当前范围与关键行为 |
| 5 | [yanzhou/development/task-pack.md](task-pack.md) | 选行为包、按条件展开细则、形成最小交接输入 |

启动包只包含上述5份；任务包及被触发的细则另计。明确完整GDD时按READ-1的54份正文包读取，来源沿革不在其中。字符统计按实际固定提交计算，不在多个入口复制易过期总量；不是token数，也不含工具、聊天、技能或代码。

## 任务确定后再补什么

| 任务 | 按需补读；先列具体文件与版本 |
| --- | --- |
| 改规则或完善首场 | [设计流程](../../docs/design-workflow.md)、相关rules／参数／案例／验收与对应正式来源；查决定只读相关ID，不默认加载整份decision-log |
| 实现已定行为 | [行为包与条件展开](task-pack.md)＋[开发规范](development-standard.md)；新2D沿当前交付的工程README／代码，维护旧3D才读[旧工程接手](E:/Project/yanzhou-godot/docs/development-handoff.md) |
| 新二维方向 | 按下方[开工交接](#新2d开工交接)确定本轮输入；建立探索时才读[READ-1](../exploration/start.md)及[探索AGENTS](../exploration/AGENTS.md) |
| 改工作台或登记方式 | [展示规格](workbench-spec.md) · [本机使用](workspace.md) |
| 制作或复用资产 | [资产接入](asset-readiness.md)、DA-1及所选AS／DM原件；不读全部制作史 |
| 人工理解／审校行为 | [场景审阅](design-review.md)，正常故事、反例与图示；意见回同轮 |
| 了解项目与人机协作 | [情景讲解与提示词](development-guide.md) · [阶段计划](production-plan.md) |
| 查3D留下的制作经验 | [制作与验证经验](development-standard.md#制作与验证经验) |

不默认加载历史批次、逐席位报告、旧测试交接、整个来源库或全部GDD。明确要求完整GDD时按READ-1的54文件清单执行，不能把核心正文阅读称作全量审查。明确禁止自动扩读的合同仍须遵守；缺材料先列缺口。

## 新2D开工交接

按上方5份启动，固定实际开工完整提交；机制以[CORE-069](../sources/draft-changes/D-2026-10-31-spatial-auxiliaries.md)、[CORE-068](../sources/draft-changes/D-2026-10-31-backpack-production.md)及未被替换的CORE-067为准，内容沿CORE-066迁移后的[首场包](task-packs/first-battle.md)。不从旧自动上桌、H3／整理点或手牌堆HTML反推新规则。

| 输入 | 当前使用方式 |
| --- | --- |
| 规则 | 三权限统一卡牌、两组手牌、免费上行／列间窗口、回收及直接配方产物已定；EX-004实际具备的D／三种一次性牌／敌表／疲劳已实现，泛化材料／回收与配方未覆盖 |
| 完整首场 | EX-004两护符／三卡／敌表为唯一输入；旧CORE-067的9轮胜、5轮无牌败、14轮疲劳及10轮兑现对照有原程序证据；CORE-068固定用途的新对照为9轮胜，尚未执行。迅速已迁移为辅助，背包尺寸／法器与辅助占形／材料未补齐，战斗演算以合法连接为前提，实际旧操作证据沿交付记录 |
| 回收与合成 | EX-003和验收仅有条件性机制情境；首场零材料、无真实回收卡，不能宣称这些内容已覆盖 |
| 2D展示 | [文字基准](../visual/baseline-2026-10-26/README.md)保留五列、工作台与C1—C3；旧CORE-067已接EX-004分页持牌、列间、生产／用途／打断／恢复／终局；CORE-068的占格布局、待料与自动补料，以及CORE-069辅助／核心装配未接入，完整真实材料／回收等仍待PRE2D-Q01 |
| 工程／资产 | 唯一新2D工程`E:/Project/yanzhou-2d/`，Godot4.7.2；DM-G002-021续版GODOT-FIRST-BATTLE-03见当前入口。十件v02美术及两字体保留，卡牌表现只读已提交事实；旧包及证据保持，DM-G002-020保持HTML身份 |

## 当前事实

| 对象 | 已有结果 | 尚缺或不能推出 |
| --- | --- | --- |
| GDD 3.2／GDD-0 | CORE-069及四包已同步；已定事项不重问。现有EX-004实现证据仍限定CORE-067 | CORE-068／069实现与执行NotRun；生产格／形状、真实材料与回收及整局未覆盖，真人理解与平衡未验证 |
| EX-004 | 完整首场规则、四条路线及真实磁盘恢复通过指定检查；原生OS首轮与包内恢复另有证据 | 没有真实回收牌、材料合成或整局路线；不外推平衡或真人体验 |
| 布局／卡面 | 十件源图接入，五列／两法器两预留／底部持牌和关键状态已实现；分页不丢库存 | 正式卡面／法术、完整真实两组／回收交互、四法器展开及用户接受仍待完成 |
| 体验取舍 | 无H3与整理点，手动选择、重复使用及合成机会成本成为重点 | FB-Q01／02、囤牌查找及列间重复操作未验证 |
| 旧实现及工作台 | 原0.4、B13和工作台资料仍按下表固定版本使用 | 不是CORE-067或新2D实现；筹码详情与历史仍延期 |
| 新2D完整首场 | DM-G002-021续版03：独立Windows可玩单战及卡牌交互动效；32项动效／30项原界面、规则与恢复、指定OS路径、复制包及干净恢复通过 | 卡面／法器／法术声画占位；其他机器、长时性能、全输入路径和真人体验未验 |

## 固定运行与审阅入口

| 版本 | 固定输入与可查看入口 | 证据边界 |
| --- | --- | --- |
| GODOT-EX002-0.4 | 源码`9c50458a56a38f0c6ebd001d9e6a3ef34382adaa`；[运行包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe) · [交付JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json) | 旧界面完整单战底座 |
| B07／0.5候选 | 组合`e0077ffa10d22ad1c9dd91e8037aa2c021409098`；[保全JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-07-preserved-evidence.json) | 首次新建113.127ms尖峰Fail；候选长测中断；未登记0.5正式交付 |
| B13 | 运行`e975de8bdbbe70591d4099c34b799e76c4bff1d7`，设计`151a9a8bb8b100994607e37a66c5314886f66a22`；[包](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe) · [证据JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-13-evidence.json) | 45候选适配，6模型／9声音接主桌；各档80项主桌、87项检视，D复核16图；不是全部设计验收 |
| UI-REVIEW-02 | [工具说明](E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/README.md) | B13固定实图与HTML模拟；浏览器意见不自动采纳或接入游戏 |

最新源码HEAD、实际构建、设计版本与检查层次分开记录。旧3D本轮未重跑，新2D证据沿当前完整首场入口；旧0.4和B13不作为CORE-067通过证据，CORE-067实现也不作为CORE-068／069通过证据。范围外回收／配方仍待合法内容及取证；第三方再分发条件不因本机可查看扩大。

旧过程文档与DQ表已退出当前目录；历史原文可在game固定提交`f21058a54b096e0d6ad2b3b559e352b67596c239`按原路径用`git show`读取。资产原件、manifest和正式设计来源保留；旧失败、NotRun与案例限制不会因清理变成通过。本次不另建去向表。
