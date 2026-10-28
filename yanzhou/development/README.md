# 言咒开发入口

2026-10-27。**CORE-067已采纳统一卡牌、手动布牌与立即回收，首场手动路线和四个任务包已同步；下一步闭合两组持牌及列间窗口的展示合同。** 本页是开发接手和当前能力的唯一汇总；旧3D排程已结束使用，2D完整展示合同与真实工程尚未建立。

2026-10-28本轮：[首场手牌→五列布牌→确认→列间再布牌HTML示意](../visual/first-battle-handflow-2026-10-28/README.md)已交付，提供单文件HTML及本机浏览器证据。限定EX-004首轮真实六张一次性牌；点击／拖到空列、显式互换、撤回、键盘落列和逐列停点已做UI检查。表现方案待审阅，正式2D工程与完整单战尚未启动，原规则／玩法验收NotRun保持。

同日按用户新顺序先做[基础美术组件源件](../visual/tabletop-components-2026-10-28/README.md)，法器与卡牌后置。首批10个完整PNG组件及30个控件分片已交付，资产／透明／合成检查与正式引擎接入分开记录；没有修改已固定的首轮HTML包。

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
| 实现已定行为 | [行为包与条件展开](task-pack.md)＋适用[开发规范](development-standard.md)；维护Godot再读[工程接手](E:/Project/yanzhou-godot/docs/development-handoff.md)及对应代码 |
| 新二维方向 | 按下方[开工交接](#新2d开工交接)确定本轮输入；建立探索时才读[READ-1](../exploration/start.md)及[探索AGENTS](../exploration/AGENTS.md) |
| 改工作台或登记方式 | [展示规格](workbench-spec.md) · [本机使用](workspace.md) |
| 制作或复用资产 | [资产接入](asset-readiness.md)、DA-1及所选AS／DM原件；不读全部制作史 |
| 人工理解／审校行为 | [场景审阅](design-review.md)，正常故事、反例与图示；意见回同轮 |
| 了解项目与人机协作 | [情景讲解与提示词](development-guide.md) · [阶段计划](production-plan.md) |
| 查3D留下的制作经验 | [制作与验证经验](development-standard.md#制作与验证经验) |

不默认加载历史批次、逐席位报告、旧测试交接、整个来源库或全部GDD。明确要求完整GDD时按READ-1的54文件清单执行，不能把核心正文阅读称作全量审查。明确禁止自动扩读的合同仍须遵守；缺材料先列缺口。

## 新2D开工交接

按上方5份启动，固定实际开工完整提交；机制以[CORE-067](../sources/draft-changes/D-2026-10-27-unified-card-model.md)为准，内容沿CORE-066迁移后的[首场包](task-packs/first-battle.md)。不从旧自动上桌、H3／整理点或手牌堆HTML反推新规则。

| 输入 | 当前使用方式 |
| --- | --- |
| 规则 | 三权限统一卡牌、全部产入两组手牌、免费手动上行、列间窗口、立即回收、配方直接交付已定；D／敌表／疲劳等保留，实现NotRun |
| 完整首场 | EX-004三种一次性牌与两护符／敌表保留；给出明确手动实例牌序及9轮胜、5轮无牌败和14轮手动疲劳对照，均为静态预期 |
| 回收与合成 | EX-003和验收仅有条件性机制情境；首场零材料、无真实回收卡，不能宣称这些内容已覆盖 |
| 2D展示 | [文字基准](../visual/baseline-2026-10-26/README.md)保留五列、工作台与C1—C3；旧库存语义已替换。[首轮HTML](../visual/first-battle-handflow-2026-10-28/README.md)已有底部持牌与列间操作的局部UI证据，完整两组／超多卡及其他状态仍待PRE2D-Q01 |
| 工程／资产 | 正式新实现仓库、引擎、代码起点及复用范围仍由实际任务明确；旧3D只作固定原版证据。DM-G002-020为外部本机HTML原型，不是正式引擎接入，也未运行真实游戏 |

## 当前事实

| 对象 | 已有结果 | 尚缺或不能推出 |
| --- | --- | --- |
| GDD 3.0／GDD-0 | CORE-067规则、验收预期、内容合同和四包已同步；C1—C5、Q01—Q06已明确，不重问 | 实现、程序模拟、真人理解与平衡全部NotRun |
| EX-004 | CORE-066实际初态／卡效／敌表，CORE-067明确手动路线；原同序效果的胜路静态保留，无出牌败路重写 | 无真实回收牌、合成配方与整局路线，旧运行结果不证明新机制 |
| 布局／卡面 | 五列、两法器／两预留、筹码与C1—C3继承；v06静态图及DM-G002-020首轮持牌／布牌／列间HTML已制作并做限定UI检查 | 完整两组、超多卡、生产／用途／打断／恢复／终局展示及用户接受待完成；旧HTML仍是2026-10-26原版参考 |
| 体验取舍 | 无H3与整理点，手动选择、重复使用及合成机会成本成为重点 | FB-Q01／02、囤牌查找及列间重复操作未验证 |
| 旧实现及工作台 | 原0.4、B13和工作台资料仍按下表固定版本使用 | 不是CORE-067或新2D实现；筹码详情与历史仍延期 |

## 固定运行与审阅入口

| 版本 | 固定输入与可查看入口 | 证据边界 |
| --- | --- | --- |
| GODOT-EX002-0.4 | 源码`9c50458a56a38f0c6ebd001d9e6a3ef34382adaa`；[运行包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe) · [交付JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json) | 旧界面完整单战底座 |
| B07／0.5候选 | 组合`e0077ffa10d22ad1c9dd91e8037aa2c021409098`；[保全JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-07-preserved-evidence.json) | 首次新建113.127ms尖峰Fail；候选长测中断；未登记0.5正式交付 |
| B13 | 运行`e975de8bdbbe70591d4099c34b799e76c4bff1d7`，设计`151a9a8bb8b100994607e37a66c5314886f66a22`；[包](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe) · [证据JSON](E:/Project/yanzhou-godot/docs/coordination/development-batch-13-evidence.json) | 45候选适配，6模型／9声音接主桌；各档80项主桌、87项检视，D复核16图；不是全部设计验收 |
| UI-REVIEW-02 | [工具说明](E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/README.md) | B13固定实图与HTML模拟；浏览器意见不自动采纳或接入游戏 |

最新源码HEAD、已交付运行源码、设计版本分开记录。第三方资产再分发条件沿原记录，不能由本机可查看推断。技术细节与旧失败经验统一在Godot工程接手；本轮未修改或运行游戏；CORE-067统一卡牌／布牌／回收／暂停／保存行为须另行实现取证，旧0.4与B13不能作为本版通过证据。

旧过程文档与DQ表已退出当前目录；历史原文可在game固定提交`f21058a54b096e0d6ad2b3b559e352b67596c239`按原路径用`git show`读取。资产原件、manifest和正式设计来源保留；旧失败、NotRun与案例限制不会因清理变成通过。本次不另建去向表。
