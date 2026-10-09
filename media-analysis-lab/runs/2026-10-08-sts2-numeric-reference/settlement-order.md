# 本地《杀戮尖塔2》行动与触发结算参考

日期：2026-10-08。版本：order-reference.1。状态：Sourced / 静态源码阅读；运行与体验验证NotRun。与[数值参考](README.md)使用同一本地恢复工程。

## 来源与适用范围

用户要求继续从`E:\Game\slay the spire`寻找顺序结算逻辑。实际读取`recovered/SlayTheSpire2/src/Core/`下的文件；这是带本地改动的恢复工程，不能等同于《杀戮尖塔1》或某个官方发行版。以下结论只描述读取到的代码路径。未运行或修改工程，未复制第三方源码或资产。

它采用回合与行动流程，没有直接对应目标游戏“同一拍全部效果”的通用排序表。最有参考价值的结构是：**明确阶段 → 从合格队首选行动 → 按行动声明的步骤执行及处理触发 → 在指定边界检查终局 → 继续下一行动**。这是对下列多层流程的概括，不能理解成所有触发都进入同一先进先出队列。

## 已核对的行为

| 层次 | 本地代码事实 | 证据位置（相对src/Core） |
| --- | --- | --- |
| 选下一个行动 | 每位玩家有自己的队列；只比较合格队首，选择最小行动ID。等待玩家选择、阶段不符等队列会跳过；入队分配递增ID。不按“伤害／防护”标签统一重排 | GameActions/Multiplayer/ActionQueueSet.cs:94—145、163—230 |
| 执行与终局检查 | 执行器等待当前执行任务返回；交互行动可以暂停并在之后恢复。普通战斗行动返回后检查胜负，结束玩家回合等行动有专用路径 | GameActions/ActionExecutor.cs:123—187 |
| 敌人顺序 | 复制当前敌人列表，依次检查敌人仍在场并执行其回合；每个敌人之后检查终局，战斗结束就不继续后面的敌人 | Combat/CombatManager.cs:1061—1093 |
| 复合卡内部顺序 | IronWave明确先获得格挡，再执行攻击。顺序写在这张牌的步骤中，不是队列把所有卡的防御部分抽出来集中提前执行 | Models/Cards/IronWave.cs:28—35 |
| 多段攻击 | 每一击前检查攻击者是否死亡，并重新筛选存活目标；一击的伤害流程返回后才进入下一击。攻击结束后还有整次攻击的后置触发 | Commands/Builders/AttackCommand.cs:513—550、649—657 |
| 一击伤害内部 | 先算修饰后的伤害、处理受伤前触发，再扣格挡和生命。多目标路径先循环各目标生成结果，再循环结果处理破盾、生命变化、伤害后触发，最后处理收集到的死亡对象 | Commands/CreatureCmd.cs:240—285、370—411 |
| 触发可以嵌在当前步骤中 | ThornsPower在BeforeDamageReceived中直接等待一次反击伤害；因此本地这条荆棘路径发生在原伤害扣格挡／生命之前。原伤害在该调用返回后继续；下一击才有AttackCommand的死亡／目标复查 | Models/Powers/ThornsPower.cs:18—25；Hooks/Hook.cs:403—411；Commands/CreatureCmd.cs:263—271 |
| 定时状态有明确阶段 | PoisonPower挂在AfterSideTurnStart：只对本阶段参与者生效，先造成一次毒伤，拥有者仍活着才减层；特殊效果能增加触发次数 | Models/Powers/PoisonPower.cs:55—77 |
| 同阶段触发有阶段分组与枚举顺序 | 回合结束前分VeryEarly、Early、普通三轮派发；受伤后有普通和Late两轮。战斗监听者先按己方／敌方集合，再按对象的状态、遗物等列表组织，并在交付前检查对象仍属于当前状态 | Hooks/Hook.cs:417—432、1232—1262；Combat/CombatState.cs:410—492；Runs/RunState.cs:545—595 |
| 死亡处理与正式结束分开 | 死亡链包含死亡前、防止死亡、死亡后及移除状态等步骤。LoseCombat先登记待失败，在CheckWinCondition处理；该检查先处理待失败再处理战斗结束 | Commands/CreatureCmd.cs:439—570；Combat/CombatManager.cs:941—964、1046—1059 |

## 三个不能省略的限制

1. **结算边界有多层。** 当前一击、整次多段攻击、整张牌、整个阶段都不是同一个边界。多目标一击也不是简单的“打完一个敌人的全部死亡链，再打下一个”。不能用“一个完整事件”几个字替代这些选择。
2. **有序派发不总等于逐项全部结束。** 部分阶段触发等待到“完成或等待玩家选择”便能继续派发，最后统一等待完成。BeforeTurnEnd的三轮只有末尾统一等待；AfterTurnEnd则在普通轮结束后等待全部完成，再派发Late。多人交互的这些恢复规则不能直接当作单人自动结算的需要。见Hook.cs:1232—1291及HookPlayerChoiceContext.cs:98—119。
3. **停止新触发与收尾已开始的触发分开。** Hook.cs:31—63的保护在一次派发开始时检查战斗是否结束／正在结束；已开始的枚举不逐监听者重查终局，但仍受对象存在性筛选。伤害、死亡等若干收尾触发走专用路径。不能概括为“血量归零立即中止一切”，也不能概括为“整张卡无条件执行到底”。

## 可借鉴的方法

先为阶段、行动和内部步骤分别写明次序；每个状态声明准确触发点；同阶段使用可解释的稳定次序；新产生的触发声明是嵌入当前步骤还是等后续阶段；明确存活／目标复查和终局检查位置。这能让预告与结果拥有同一解释。

以上是结构参考，不提供加工、维护、资源到账或玩家锁定的现成规则，也不证明这些规则有趣或容易理解。具体优先级、复合效果是否拆分、死亡后哪些步骤继续，仍由使用参考的项目独立决定。

## 读取版本

本地HEAD为`f49460a1bc788616f752845e8f0ecc6ab217b476`；关键文件未跟踪，HEAD不能固定所读内容。以下SHA-256标识本次文件内容。表内正文所列区段为实读依据；其余区域没有声称完整审查。

| 相对src/Core的文件 | SHA-256 |
| --- | --- |
| GameActions/ActionExecutor.cs | 97e81c9687aeedf7de5dcc629e749c67ff922c64cebce9e9b8bf2c6627a9f3ad |
| GameActions/Multiplayer/ActionQueueSet.cs | 3646fe6a5df520d5b3d723892a3a95a0e5f693d2a73917981e3aeb9fd43e7e42 |
| GameActions/Multiplayer/HookPlayerChoiceContext.cs | 883e2bb59b2c04f9638e04e170b85fbf8f7a208782ce1a264ae3a459f111890e |
| Combat/CombatManager.cs | 7ae1b7259e72befa07f4aceaa9ab0e23783fc55876bcde6090b9b2cfae65a43e |
| Combat/CombatState.cs | 6dc71f2ed75e40551749f77a45d4dd39fd2999904c8d84ef36419efc152fe759 |
| Runs/RunState.cs | 2049583b323c7864016a966efa4b462ed2a95b16789f235ad3f84fbef02e1b0d |
| Commands/Builders/AttackCommand.cs | 97b89ff8492addaa398a6f8c59022a173052fc529677c3270d43e0184a6b8e66 |
| Commands/CreatureCmd.cs | f52882086d141dea85b8de65b8e526db5418e390d3f5ba3f2191d3d7f8a6420b |
| Hooks/Hook.cs | e6a1bbdf2e7b3a2f941b2de5dff283cd2538b220e703e771b53d9042e97111d4 |
| Models/Cards/IronWave.cs | 842df21871b44f19af5e9848dc71ebfb5fe9c9832aa308584b95a0b20b0f2ca4 |
| Models/Powers/ThornsPower.cs | 96167a3d1513ad6da621861e3f64fc2d8ddc7cad618b54131c0955297c22912c |
| Models/Powers/PoisonPower.cs | 7cf6dfc3987122ccc4a8a0d175871435a30bf0a756b171eb30019a693441b609 |
