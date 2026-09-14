---
id: I-20260914-timeline-construction
type: Research Insight
project_id: game-002-optimization
status: Research
created: 2026-09-14
updated: 2026-09-14
question_ids: [Q-20260914-timeline-construction]
source_ids: [SRC-TIME-RC1, SRC-TIME-BD2, SRC-TIME-OM, SRC-TIME-TZ, SRC-TIME-PB]
method: web-research
author: agent
version: v1
---

# 时间轴施法构筑：跨品类研究

结论状态：`Provisional`。用户要求在核心时间轴施法构筑上创新，并授权参考其他品类。唯一项目仍为 `game-002-optimization`；不读取其他本地探索方向。新机制正文隔离在[原始候选](../idea-inbox/2026-09-14-timeline-construction.md)，当前问题见[Q](../questions/Q-20260914-timeline-construction.md)。

## 主要结论

**Agent 推断：可以直接把时间安排变成构筑资源。** 最值得讨论的三个问题是：两次法术之间的等待能否重新分配；本次法术能否付代价等一个合适目标；下一句是否必须跟着上一句的实际结果启动。它们分别改变时间分布、等待承诺和法杖之间的关系。

当前 GDD 已有完成冷却、按周期减冷却、跳冷却与复诵；本轮不把这些改名当新增。建议先比较两次循环的冷却预算重排，再研究法杖跟随；有限候发可独立比较，但如果只是自动纠错，未必值得新增。

这不是实测结论，也没有证明现有 RC1 缺乏深度。其他产品说明机制可表达，不证明移植后好玩或市场首创。

## 搜索范围与筛选

- 日期／检索时区：2026-09-14，Asia/Shanghai；本地版本复核时钟为10:32 +08:00。网页逐次抓取的精确时分未单独记录，以下时间为来源核对登记口径。
- 查询主题：`Bravely Default II Brave Default BP`、`Zachtronics Opus Magnum program`、`Tzolkin gears`、`Phantom Brigade timeline`；另检索 Transistor、Spirit Island 快慢阶段、格斗前后摇、FFXII Gambit。
- 优先采用开发者、发行商或其商店正文；搜索摘要只作线索，主要结论均回到已打开原文。
- 最终采用四个核心案例，覆盖回合 RPG、编程解谜、工人放置桌游与时间轴战术。没有购买、安装、下载游戏或运行试玩。
- Transistor 官方 FAQ 只确认策略规划与即时动作结合，不足以支撑本轮所需的恢复期细则；FFXII 主要返回社区和转存手册，Spirit Island 返回分散说明，格斗帧数缺直接匹配条款。均不据此作本轮精确机制论证，也不把这些检索线索写成已验证案例。
- 不使用商业价格、销量、评分或流行度推导机制适用性；不引用旧 Phantom Brigade 补丁推定2.x当前热量公式。

## 来源登记

以下外部源所属项目均为 `game-002-optimization`，类型为公开网页，状态 `Retrieved`；固定定位为所列URL＋本次访问日期（没有保存网页快照，不保证以后内容不变）。许可边界为链接与原创短摘要，不存整页、图片、媒体或第三方原文。规则事实属于 `Source Claim / Reported`，不是本次试玩观察。

### SRC-TIME-RC1：用户指定全游戏 GDD

- 类型：项目背景／用户指定文件。位置：[主GDD](../../../workspaces/game-002/game-design-workflow/gdd/GDD-2026-09-14-yanzhou-full-game.md)及其构句、战斗分册。
- 版本日期：1.0 RC1 / 2026-09-14；来源提交 `87840a221af330a2c715fc9c390eae982a00aebd`。
- 获取时间：2026-09-14 10:32 +08:00复核；状态 `Retrieved`。
- 主GDD SHA256：`8BCEA638DBB4A72194100AE0189CFB6DBB871ACFDF118E2FD508330AC2D170C6`。
- 战斗分册SHA256：`96B73E32242FE2AC8E30E2255933DEF77EBF37B804313FA4817C458D38F65ADA`。与上一轮相同，相关工作区无变更。
- 定位：主GDD §1、§3不变量；构句CG01、CG-T01、CG-G01；战斗核心闭环、RC02／03、BR03、GR02。
- 范围：用户已有跨项目读取授权继续有效；写入仅限探索根。活动背景包仍为 `baseline-2026-09-09-001`，未更换。更完整版本边界见[上一轮来源记录](2026-09-14-rc1-strategy-source-record.md)。

### SRC-TIME-BD2：BRAVELY DEFAULT II

- 作者／发布方：Nintendo；产品：Square Enix回合RPG，所查页面为Nintendo Switch版本。
- URL：[Nintendo产品页](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-games/BRAVELY-DEFAULT-II-1698006.html)。
- 页面发布日期：Unknown；页面列游戏发售2021-02-26。获取时间：2026-09-14 10:32 +08:00登记。
- 定位：Using Brave and Default、Brave、Default，访问时正文239–249行。
- 来源摘要：Default积累BP并防御，Brave花BP增加行动；透支后可能无法在后续回合行动。这里只采用行动积累／支出／透支约束，不混用系列其他作品的负BP上限。

### SRC-TIME-OM：Opus Magnum

- 作者／发布方：Zachtronics；编程／工程解谜；所查PC商店列Windows、macOS、Linux。
- URL：[开发者教学介绍](https://zachtronics.com/zachademics/)、[开发者Steam正文](https://store.steampowered.com/app/558990/Opus_Magnum/)。
- 页面发布日期：Unknown；教学页标题标2017。获取日期：2026-09-14，Asia/Shanghai；精确时分Unknown。
- 定位：Zachademics的Opus Magnum段落27–28行；Steam的Design Machines／Open-Ended Puzzles，226–227行。
- 来源摘要：用符号指令控制机械部件操作分子；开放式解法可以分别追求简单、快速和紧凑。
- 证据限制：本次原文不充分说明循环指令、同步阻塞与空指令的全部语义，不能把下文跟随时钟称为对该游戏某条同步指令的直接移植。

### SRC-TIME-TZ：Tzolk'in: The Mayan Calendar

- 作者／发布方：Czech Games Edition；动态工人放置桌游。
- URL：[CGE官方详细介绍](https://www.czechgames.com/for-press-games/tzolkin-the-mayan-calendar)。
- 页面发布日期：Unknown；页面列游戏发行2012年Q4。获取日期：2026-09-14，Asia/Shanghai；精确时分Unknown。
- 定位：Detailed Overview，333–336行。
- 来源摘要：工人放上联动齿轮后随转动抵达不同位置；回合选择放入或取回，取回位置决定行动。更后的位置更有价值，但工人全部占用且不能跳过回合时必须取回一些。
- 证据限制：这是公开产品规则概述，不覆盖扩展与所有例外。

### SRC-TIME-PB：Phantom Brigade

- 作者／发布方：Brace Yourself Games；机甲时间轴战术；官方页链接Steam和Epic。
- URL：[开发者产品页](https://braceyourselfgames.com/phantom-brigade/)。
- 页面发布日期：Unknown；About区使用2.0措辞，页面同时列2026-06-25的2.2新闻，不把它误标为当前仅有2.0。
- 获取时间：2026-09-14 10:32 +08:00登记。定位：About the game与Features，17–25行。
- 来源摘要：预知敌方动作、在时间轴规划精确反制，再执行观看实时展开。
- 证据限制：不使用未从该页确认的固定五秒长度、热量方程或全部预测精度作为结论。

## 证据与可借鉴结构

| 证据ID | 层级 | 来源事实与定位 | 对《言咒》的转化推断 |
| --- | --- | --- | --- |
| E-TIME-01 | Reported | SRC-TIME-BD2：BP可积累、花费、透支并产生后续行动代价 | 时间可在相邻行动间重新分配；先享受收益要留下明确空档 |
| E-TIME-02 | Reported | SRC-TIME-OM：可编程部件与多种优化目标 | 玩家应构筑多句之间的协作，并比较速度、稳定性、资源占用，而非只有减冷却 |
| E-TIME-03 | Reported | SRC-TIME-TZ：等待提高可得行动价值，也占住工人 | 等待要占住法杖的下一轮生产能力；不能只让所有延迟都获得免费增伤 |
| E-TIME-04 | Reported | SRC-TIME-PB：预知、安排时机、执行 | 时间关系与代价应在战前能看懂；本项目保留整场自动，不移植频繁战中重下指令 |
| E-TIME-05 | Reported | SRC-TIME-RC1：词时间形成冷却、首次起点0–10、每刻后杖赢开始槽；取消保留名义续排 | 目前可以安排相位与明示改期，但释放机会主要仍落在点上；候发与跟随需要新增规则 |
| E-TIME-06 | Reported | SRC-TIME-RC1：完成冷却、节律、耗印跳冷却、复诵已有 | 新候选必须解释预算守恒、等待承诺或相对依赖，不以加速／追加动作本身充当创新 |

## 机制如何影响行为

| 产品 | 玩家处境→可见信息→行动→规则结果→下次选择 | 可能的体验价值（Agent推断） | 应避免直接搬入 |
| --- | --- | --- | --- |
| BD II | 有眼前压力→看到BP→防御存点或集中行动→形成以后能否行动的差异→调整后续攻守 | 决定什么时候支付行动代价 | 战中菜单指令、完整职业与BP资源条 |
| Opus Magnum | 有目标产物→看到部件与指令→组织机器→运行与优化→换用另一结构 | 自己设计的协作能持续工作 | 任意脚本、复杂循环语言、无限部件与解谜型单关重试要求 |
| Tzolk'in | 工人有限→看到后续动作位置→放置或取回→收益与可用工人改变→决定再投入 | 等待和兑现都有机会成本 | 多人抢位、全套经济与喂养系统 |
| Phantom Brigade | 敌方行动可预测→看到时间安排→选择反制时刻→执行→观察效果 | 精确预判与可解释执行 | 战中反复编辑、机甲移动、物理破坏与装备系统 |

这些是压缩的机制分析，不是完整产品拆解。玩家是否喜欢上述体验未由本轮调查。

## 可转化假设与当前判断

详细设计只放入[原始候选](../idea-inbox/2026-09-14-timeline-construction.md)：

| 本地候选 | 核心变化 | 理论上的新增选择 | 首要反例 |
| --- | --- | --- | --- |
| R1 冷却预算重排 | 同一法术相邻两周期一短一长，总量保持 | 提前兑现 vs 留长空档；与其他杖交错 | 短战永远提前更强，偿还没有实际发生 |
| R2 有限候发 | 无对象时短暂占住本次机会，推迟后续周转 | 保证一次有用释放 vs 更频繁尝试 | 成为不付代价的自动防空放功能 |
| R3 法杖跟随 | 一根杖的下一次冷却由指定上游实际结果启动 | 准确前后关系 vs 独立行动频率与抗故障 | 全部法杖固定长链，失去搭配与独立响应 |

推荐先试R1。R3更可能改变核心构筑形态；R2适合检查可靠性是否值得资源成本。三项先独立比较，不预设最终全采用。只有资格确认后才冻结实际词表、成本、试验输入并进入正式提案。

## 不应当作新增深度的改法

- 只把所有冷却减短：可能增加输出，不能单独证明策略增加。
- 每个空白刻都送增伤：容易形成固定最优间隔，且与既有蓄势用途重叠。
- 冲突自动排队且没有代价：会削弱同刻争槽的选择，可能只是调度便利。
- 前摇免费移到不受打断的后摇：先拿收益且更安全，可能严格优于原版；没有对等暴露就不推荐。
- 增加战中按键踩拍：改变玩家技能要求和自动战斗合同，本轮不采用。

## 未知、限制与下一步

外部机制事实足以支持上述方向值得讨论；《言咒》是否更深、更好懂、更好玩仍为Unknown。没有真人试玩、对局模拟、完整平衡或市场唯一性证明。

下一步先明确优先的时间取舍：控制快慢分布，还是编写法杖之间的启动关系。推荐R1作为低范围起点；用户本轮没有采纳具体规则。各候选已列最小反例与成功／失败信号，数值均是解释用假定，不能用作制作基准。
