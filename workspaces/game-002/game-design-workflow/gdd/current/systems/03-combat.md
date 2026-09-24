# 自动战斗、时序与状态（已迁移）

文档角色：CompatibilityNavigation。目录修订layout.1 / 2026-09-23。

[打开新位置](../../../../../../yanzhou/design/systems/03-combat.md) · [言咒项目入口](../../../../../../yanzhou/README.md) · [迁移说明](../../../../../../yanzhou/governance/layout-migration-report.md)

此路径只作旧链接兼容，不维护正文。历史提交及来源哈希仍按原日期/原路径解释。新写入按yanzhou/AGENTS.md；探索候选的资格与主系统回写权限不变。

<a id="41-设计目的与玩家承诺"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#41-设计目的与玩家承诺)

<a id="410-未知项与依赖"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#410-未知项与依赖)

<a id="42-mda推理"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#42-mda推理)

<a id="43-输入状态与输出"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#43-输入状态与输出)

<a id="44-核心规则"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#44-核心规则)

<a id="45-成本限制与取舍"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#45-成本限制与取舍)

<a id="46-失败取消与玩法异常"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#46-失败取消与玩法异常)

<a id="47-交互信息与反馈"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#47-交互信息与反馈)

<a id="48-正例与反例"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#48-正例与反例)

<a id="49-系统验收标准"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#49-系统验收标准)

<a id="br01-自身宿主和元素范围"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br01-自身宿主和元素范围)

<a id="br02-阵营与能力资格"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br02-阵营与能力资格)

<a id="br03-正释放时长与并存过程"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br03-正释放时长与并存过程)

<a id="br04-公式结构实付与零量"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br04-公式结构实付与零量)

<a id="br05-原动作后置触发与自耗"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br05-原动作后置触发与自耗)

<a id="br08-疲劳的执行类别与同刻处理"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#br08-疲劳的执行类别与同刻处理)

<a id="cg-r01主动与消散爆炸的范围"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#cg-r01主动与消散爆炸的范围)

<a id="cg-r02反刺的攻击者与范围"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#cg-r02反刺的攻击者与范围)

<a id="cg-s01元素执行与状态归属"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#cg-s01元素执行与状态归属)

<a id="cg-t01完成冷却的当刻窗口"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#cg-t01完成冷却的当刻窗口)

<a id="gr01参数归属与数值合法域"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr01参数归属与数值合法域)

<a id="gr02冷却区间与取消后的续排"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr02冷却区间与取消后的续排)

<a id="gr03角色数量配对与筛选成本"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr03角色数量配对与筛选成本)

<a id="gr04状态归零与合法零值"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr04状态归零与合法零值)

<a id="gr05联合支付与生命代价"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr05联合支付与生命代价)

<a id="gr06归零与完整事件结算"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr06归零与完整事件结算)

<a id="gr07派生事件与有限响应"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#gr07派生事件与有限响应)

<a id="rc01-回响给下一条其他简易法术"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc01-回响给下一条其他简易法术)

<a id="rc02-复诵一次追加不改变正常节拍"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc02-复诵一次追加不改变正常节拍)

<a id="rc03-蓄势强化一次完整攻防结果跳冷却不储存多次"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc03-蓄势强化一次完整攻防结果跳冷却不储存多次)

<a id="rc04-同种合并先来定性质后来只加量"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc04-同种合并先来定性质后来只加量)

<a id="rc05-结果替换一次替换冲突配装互斥"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc05-结果替换一次替换冲突配装互斥)

<a id="rc06-触发效果原事件后立即结算只接一层"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc06-触发效果原事件后立即结算只接一层)

<a id="rc07-元素持续释放逐刻检查自动邻近在环境阶段"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc07-元素持续释放逐刻检查自动邻近在环境阶段)

<a id="rc08-消耗明确全部与限量按实付产生结果"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc08-消耗明确全部与限量按实付产生结果)

<a id="rc09-耗尽本体当前动作完成随后结算消散特效"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc09-耗尽本体当前动作完成随后结算消散特效)

<a id="rc10-操控与邻近一次事件只施加一次"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc10-操控与邻近一次事件只施加一次)

<a id="rc11-事件定义直接伤害抵消清除各认自己的事件"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc11-事件定义直接伤害抵消清除各认自己的事件)

<a id="rc12-修饰词本句改变与生成物特性分开"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rc12-修饰词本句改变与生成物特性分开)

<a id="rg06完整疲劳基准"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#rg06完整疲劳基准)

<a id="st01-每刻末状态结算"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#st01-每刻末状态结算)

<a id="st02-固定先后与阶段边界"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#st02-固定先后与阶段边界)

<a id="st03-自然衰减保留小数进度"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#st03-自然衰减保留小数进度)

<a id="st04-允许空心自噬长期储层"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#st04-允许空心自噬长期储层)

<a id="sys-003自动战斗与状态时序"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#sys-003自动战斗与状态时序)

<a id="四阶段与状态机"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#四阶段与状态机)

<a id="基础合同与完整闭环"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#基础合同与完整闭环)

<a id="当前仍需消歧的事件边界"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#当前仍需消歧的事件边界)

<a id="新版卡池共同规则-rc0112"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#新版卡池共同规则-rc0112)

<a id="有限终局的明确前提及数学上界"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#有限终局的明确前提及数学上界)

<a id="状态刻末结算与元素衰减"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#状态刻末结算与元素衰减)

<a id="状态身份与寿命补充"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#状态身份与寿命补充)

<a id="自动战斗时序与状态"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#自动战斗时序与状态)

<a id="通用求值与费用边界"></a>

[对应正文](../../../../../../yanzhou/design/systems/03-combat.md#通用求值与费用边界)
