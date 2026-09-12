# 效果与案例覆盖

维护：2026-09-12。编号必须带来源前缀：类型/TC01、简单句/T01、参数/T01与测试/T01不是同一用例。链接到效果只代表登记关系，不代表句法合法、参数采纳或已经通过效果验收。

## 类型案例：26项

来源：[类型素材TC01–TC26](../../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md)。分类原样引用，完整效果按各ID补齐。

| 来源限定ID | 原案例 | 全部基础类型 | 效果登记 | 状态与边界 |
| --- | --- | --- | --- | --- |
| 类型/TC01 | 获得 护甲 | 简易＋状态 | [FX-002](entries/FX-002.md) | 已有语义例；具体量另定 |
| 类型/TC02 | 造成伤害 | 简易 | [FX-001](entries/FX-001.md) | 只识别特征；具体词卡切分与受术对象不在本次补齐 |
| 类型/TC03 | 燃烧 蔓延 | 状态 | [FX-009](entries/FX-009.md)、[FX-003](entries/FX-003.md) | 用户类型例；名词＋动词的完整句法及传播效果待状态类讨论 |
| 类型/TC04 | 燃烧 加倍 | 状态 | [FX-008](entries/FX-008.md)、[FX-003](entries/FX-003.md) | 用户类型例；具体操作与宾语省略许可另定 |
| 类型/TC05 | 释放 火焰 | 简易＋元素 | [FX-010](entries/FX-010.md) | 只采用分类；生成后的具体行为Parked |
| 类型/TC06 | 火焰 吞噬 护甲 | 状态＋元素 | [FX-023](entries/FX-023.md)、[FX-010](entries/FX-010.md)、[FX-002](entries/FX-002.md) | 只采用分类；不推定消耗归属或转化效果 |
| 类型/TC07 | 召唤 恶魔 | 简易＋召唤 | [FX-021](entries/FX-021.md) | 完整召唤流程仍Parked |
| 类型/TC08 | 恶魔 释放 火焰 | 元素＋召唤 | [FX-021](entries/FX-021.md)、[FX-010](entries/FX-010.md) | 不推定单位出生、绑定和火焰行为 |
| 类型/TC09 | 点燃 敌人 | 简易 | [FX-003](entries/FX-003.md) | 产生燃烧的预期效果不提供状态名词 |
| 类型/TC10 | 冰冻 敌人 | 简易 | [FX-004](entries/FX-004.md) | 不因动词与状态同名增添状态类型 |
| 类型/TC11 | 熄灭 燃烧 | 简易＋状态 | [FX-005](entries/FX-005.md) | 具体解除规则Parked |
| 类型/TC12 | 解除 冰冻状态 | 简易＋状态 | [FX-006](entries/FX-006.md)、[FX-004](entries/FX-004.md) | 与“冰冻敌人”区分 |
| 类型/TC13 | 释放 雷电 | 简易＋元素 | [FX-011](entries/FX-011.md) | 具体效果Parked |
| 类型/TC14 | 释放 冰霜 | 简易＋元素 | [FX-012](entries/FX-012.md) | 具体效果Parked |
| 类型/TC15 | 强化 火焰 | 简易＋元素 | [FX-013](entries/FX-013.md)、[FX-010](entries/FX-010.md) | 强化量与期限Parked |
| 类型/TC16 | 削弱 雷电 | 简易＋元素 | [FX-014](entries/FX-014.md)、[FX-011](entries/FX-011.md) | 削弱量与消散条件Parked |
| 类型/TC17 | 抵挡 冰霜 | 简易＋元素 | [FX-015](entries/FX-015.md)、[FX-012](entries/FX-012.md) | 抵挡机制Parked |
| 类型/TC18 | 火焰 点燃 敌人 | 元素 | [FX-010](entries/FX-010.md)、[FX-003](entries/FX-003.md) | 没有状态名词，只有元素类型；载体方案Parked |
| 类型/TC19 | 雷电 伤害 敌人 | 元素 | [FX-011](entries/FX-011.md)、[FX-001](entries/FX-001.md) | 直接伤害结果不改变类型 |
| 类型/TC20 | 冰霜 冰冻 敌人 | 元素 | [FX-012](entries/FX-012.md)、[FX-004](entries/FX-004.md) | 没有状态名词，只有元素类型 |
| 类型/TC21 | 收集 树木 | 简易 | [FX-020](entries/FX-020.md) | 当前无已采纳资源类型；词效Parked |
| 类型/TC22 | 伤害 敌人 | 简易 | [FX-001](entries/FX-001.md) | 与是否造成实际生命伤害分别判断 |
| 类型/TC23 | 我 伤害 敌人 | 未命中当前基础类型 | [FX-001](entries/FX-001.md) | 当前保留未命中；纳入扩展检查，不以未归类本身定义新类 |
| 类型/TC24 | 解除 恶魔的燃烧 | 简易＋状态＋召唤 | [FX-006](entries/FX-006.md)、[FX-021](entries/FX-021.md)、[FX-003](entries/FX-003.md) | 简易＋状态＋召唤；实际词卡与关系权限仍逐项检查 |
| 类型/TC25 | 召唤 火焰 | 简易＋元素 | [FX-010](entries/FX-010.md) | 特征对照，不宣告此搭配语义合法，也不判召唤类型 |
| 类型/TC26 | 强化 恶魔 | 简易＋召唤 | [FX-022](entries/FX-022.md)、[FX-021](entries/FX-021.md) | 属于召唤类型不等于本次新生成单位 |

## 简单句情境：12项

来源：[简单句情境T01–T12](../../game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md)。这些情境的具体实现方案仍Parked；下表类型来自已明确的句子特征，未具名过程卡不是新批准词卡。

| 来源限定ID | 情境 | 效果登记 | 分类与边界 |
| --- | --- | --- | --- |
| 简单句/T01 | 点燃树木 | [FX-003](entries/FX-003.md) | 简易；环境宿主资格与燃烧规格待定 |
| 简单句/T02 | 冰冻敌人 | [FX-004](entries/FX-004.md) | 简易；不能自动解释为停止攻击 |
| 简单句/T03 | 释放火焰 | [FX-010](entries/FX-010.md) | 简易＋元素；真实身份与窗口待定 |
| 简单句/T04 | 削弱现存火焰 | [FX-014](entries/FX-014.md)、[FX-010](entries/FX-010.md) | 简易＋元素；归零结果待定 |
| 简单句/T05 | 释放雷电＋抵挡雷电 | [FX-011](entries/FX-011.md)、[FX-015](entries/FX-015.md) | 两句均简易＋元素；真实交互窗口及两份雷电实体卡 |
| 简单句/T06 | 释放冰霜／冰冻敌人 | [FX-012](entries/FX-012.md)、[FX-004](entries/FX-004.md) | 前者简易＋元素，后者简易；不是同一对象 |
| 简单句/T07 | 抵挡未完成攻击 | [FX-015](entries/FX-015.md) | 原场景方向；实际词卡及完整类型依句子 |
| 简单句/T08 | 反弹雷电 | [FX-016](entries/FX-016.md)、[FX-011](entries/FX-011.md) | 简易＋元素；自动接收规则未定 |
| 简单句/T09 | 转移攻击 | [FX-017](entries/FX-017.md) | 简易；不能增添玩家指定接收者 |
| 简单句/T10 | 收集树木 | [FX-020](entries/FX-020.md) | 简易；止于对象掉卡 |
| 简单句/T11 | 获得护甲 | [FX-002](entries/FX-002.md) | 简易＋状态；参照参数另有固定版本 |
| 简单句/T12 | 加速〔法术的冷却〕 | [FX-018](entries/FX-018.md) | 简易；当前剩余时间，不修改基础周期 |

原a＜b＜e等生成窗口边界归FX-010–012／015；具体a、b、e与结束阶段随效果冻结，纸面关系不提供默认6刻。

## 修饰词与镶嵌：5项

来源：[Modifier v0.1](../../game-design-workflow/idea-materials/M-2026-09-11-modifier-card-system.md)、[Inlay v0.1](../../game-design-workflow/idea-materials/M-2026-09-12-wand-inlay-system.md)。

| 本登记案例ID | 案例 | 类型与归类 | 效果登记及关系 |
| --- | --- | --- | --- |
| ER-M01 | 获得〔寒冷的→护甲〕 | 简易＋状态；形容词通用分支 | [FX-024](entries/FX-024.md)、[FX-002](entries/FX-002.md)、[FX-004](entries/FX-004.md)；自己获得更多护甲，自己附加冰冻 |
| ER-M02 | 〔寒冷的→寒冰〕吞噬护甲 | 状态＋元素，沿用来源对寒冰的元素案例定位；寒冰具体身份未定 | [FX-025](entries/FX-025.md)、[FX-023](entries/FX-023.md)、[FX-004](entries/FX-004.md)；特殊替代通用，不永久改写现存对象 |
| ER-M03 | 〔寒冷的→火焰〕吞噬护甲 | 不兼容而非法；不登记为可执行法术 | [FX-025](entries/FX-025.md)的非法反例；不能因类型命中绕过兼容 |
| ER-I01 | 简易法术加速 | 镶嵌；匹配法术的简易类型 | [FX-026](entries/FX-026.md)；偶数周期−1，含覆盖／打断计次 |
| ER-I02 | 燃烧效果强化 | 镶嵌范围被动；本身不属于某种法术类型 | [FX-027](entries/FX-027.md)、[FX-003](entries/FX-003.md)；合法燃烧施加新增＋1，各来源；非周期伤害 |

暂没有具名副词卡案例，不为了覆盖类别虚构副词效果。不同附加左右顺序与同值合并作为MD框架检查，并非额外效果卡。

## Parked逐刻情境：24项

来源：[EC01–EC24纸面方案](../../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-paper-checks.md)。这里只追踪问题覆盖，不抄入旧试案参数或标成当前唯一预期。重新启用必须逐项重新设计并冻结输入。

| 来源限定ID | 效果登记 | 当前解释 |
| --- | --- | --- |
| 纸面/EC01 | [FX-010](entries/FX-010.md) | 窗口结束阶段未定；原第9刻数值仅Parked |
| 纸面/EC02 | [FX-010](entries/FX-010.md) | 演出残留不是对象 |
| 纸面/EC03 | [FX-010](entries/FX-010.md) | 名单锁定后失效不补位 |
| 纸面/EC04 | [FX-014](entries/FX-014.md)、[FX-010](entries/FX-010.md) | 元素归零条件待定义，不能直接套状态归零 |
| 纸面/EC05 | [FX-015](entries/FX-015.md)、[FX-011](entries/FX-011.md) | 抵挡量及剩余使用未定义 |
| 纸面/EC06 | [FX-015](entries/FX-015.md)、[FX-011](entries/FX-011.md) | 已结算结果不回滚 |
| 纸面/EC07 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) | 宿主失效时载体是否支付须正式声明 |
| 纸面/EC08 | [FX-001](entries/FX-001.md)、[FX-004](entries/FX-004.md)、[FX-011](entries/FX-011.md) | 冰冻减伤和零伤害载体消耗均Parked |
| 纸面/EC09 | [FX-003](entries/FX-003.md)、[FX-010](entries/FX-010.md)、[FX-027](entries/FX-027.md) | 施加量修正不在周期重复；新镶嵌语义不采纳旧数值 |
| 纸面/EC10 | [FX-003](entries/FX-003.md) | 状态重施骨架可复用，原数量／时长不恢复 |
| 纸面/EC11 | [FX-007](entries/FX-007.md)、[FX-003](entries/FX-003.md) | 仅状态骨架消耗装置，不新增消耗卡 |
| 纸面/EC12 | [FX-005](entries/FX-005.md) | 完全清除取消未执行周期／到期，具体熄灭词义待定 |
| 纸面/EC13 | [FX-003](entries/FX-003.md)、[FX-005](entries/FX-005.md) | 清后重施重建计时；新参数未定 |
| 纸面/EC14 | [FX-003](entries/FX-003.md)、[FX-004](entries/FX-004.md) | 双状态互作须新词义声明，原并存细则Parked |
| 纸面/EC15 | [FX-003](entries/FX-003.md) | 无支持资格不能以增幅变合法；具体石块属性待定 |
| 纸面/EC16 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) | 覆盖不产生本次生成结果 |
| 纸面/EC17 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) | 后续打断不撤销此前独立对象 |
| 纸面/EC18 | [FX-001](entries/FX-001.md)、[FX-011](entries/FX-011.md) | 完整法术后检查终局，不在终局后追加收集 |
| 纸面/EC19 | [FX-020](entries/FX-020.md)、[FX-003](entries/FX-003.md)、[FX-004](entries/FX-004.md) | 不靠状态重置刷掉卡额度；具体额度待定 |
| 纸面/EC20 | [FX-020](entries/FX-020.md)、[FX-010](entries/FX-010.md) | 生成物不能继承无来源的掉卡权限 |
| 纸面/EC21 | [FX-010](entries/FX-010.md) | 每次词出现各占实体卡 |
| 纸面/EC22 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) | 对象当时数值与来源修正快照分开 |
| 纸面/EC23 | [FX-003](entries/FX-003.md)、[FX-004](entries/FX-004.md) | 原冰冻直接减伤版本Parked，不能当周期修正规则 |
| 纸面/EC24 | [FX-003](entries/FX-003.md)、[FX-004](entries/FX-004.md) | 原零层续时属于Parked词条声明，不作为通用默认 |

原火焰／强化／点燃逐刻组合关联FX-010／013／003，原冰冻示范关联FX-004／001，原掉卡领取分支关联FX-020与框架收益。三组均不是现行完整卡牌规格。

## 首批18词与能力方向

来源：[首批分类](../../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md)、[能力B01–B10](../../game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md)。

| 词名 | 登记去向 | 说明 |
| --- | --- | --- |
| 释放 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) | 对不同元素的生成规格分别登记 |
| 点燃 | [FX-003](entries/FX-003.md) | 对不同宿主与火焰载体复用时须明示差异 |
| 冰冻 | [FX-004](entries/FX-004.md) | 动作，不与元素冰霜合并 |
| 伤害 | [FX-001](entries/FX-001.md) | 限定攻防参照与其他载体变体分开 |
| 强化 | [FX-013](entries/FX-013.md)、[FX-022](entries/FX-022.md)、[FX-028](entries/FX-028.md) | 元素、召唤物、属性不默认为同一被改变量 |
| 削弱 | [FX-014](entries/FX-014.md) | 其他状态方向见FX-007，需词义许可 |
| 抵挡 | [FX-015](entries/FX-015.md) | 可操作窗口必需 |
| 熄灭 | [FX-005](entries/FX-005.md) | 清除或减量须明确 |
| 解除 | [FX-006](entries/FX-006.md) | 对应具体状态权限 |
| 收集 | [FX-020](entries/FX-020.md) | 对象掉卡 |
| 火焰 | [FX-010](entries/FX-010.md) | 元素对象；燃烧效果见FX-003 |
| 雷电 | [FX-011](entries/FX-011.md) | 元素对象；伤害见FX-001 |
| 冰霜 | [FX-012](entries/FX-012.md) | 元素对象；冰冻见FX-004 |
| 燃烧 | [FX-003](entries/FX-003.md)、[FX-005](entries/FX-005.md)、[FX-008](entries/FX-008.md)、[FX-009](entries/FX-009.md) | 状态及操作案例 |
| 冰冻状态 | [FX-004](entries/FX-004.md)、[FX-006](entries/FX-006.md) | 状态及清除 |
| 敌人 | 对象与选择规则；被FX-001／003／004等引用 | 一般对象名词，不单独产生效果 |
| 树木 | 对象与选择规则；被FX-003／020等引用 | 没有默认材料或掉落 |
| 石块 | 对象与选择规则；资格反例关联FX-003／020 | 支持能力必须明确，非自动燃烧或可收集 |

| 能力方向 | 登记 |
| --- | --- |
| B01 数量变化 | [FX-001](entries/FX-001.md)、[FX-002](entries/FX-002.md)、[FX-007](entries/FX-007.md)、[FX-013](entries/FX-013.md)、[FX-014](entries/FX-014.md)、[FX-028](entries/FX-028.md) |
| B02 点燃 | [FX-003](entries/FX-003.md) |
| B03 冰冻 | [FX-004](entries/FX-004.md) |
| B04 状态削弱／清除 | [FX-005](entries/FX-005.md)、[FX-006](entries/FX-006.md)、[FX-007](entries/FX-007.md)、[FX-032](entries/FX-032.md) |
| B05 生成元素 | [FX-010](entries/FX-010.md)、[FX-011](entries/FX-011.md)、[FX-012](entries/FX-012.md) |
| B06 抵挡 | [FX-015](entries/FX-015.md) |
| B07 反弹 | [FX-016](entries/FX-016.md) |
| B08 转移 | [FX-017](entries/FX-017.md) |
| B09 改变未完成时间 | [FX-018](entries/FX-018.md)、[FX-019](entries/FX-019.md) |
| B10 掉卡 | [FX-020](entries/FX-020.md) |

额外具名案例“获得、召唤、吞噬、蔓延、加倍、力量”分别进入FX-002／021／023／009／008／028；过程取消范围为FX-031，有限产金为FX-030。

<a id="framework"></a>

## 框架引用与暂不开放的方向

这些项目也有登记去向，不能漏掉后又误当已开放特效。H编号是后置／表现／框架提及的索引，具体效果获准设计时再拆分为FX条目并保留双向关系。

| 边界ID | 内容 | 所属与处理 |
| --- | --- | --- |
| ER-F01 | 疲劳双方扣血、法术禁疗 | [FAT-A／FAT-C](../../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md)；全局规则。FAT-A方向Accepted，细则Candidate；不是可被法术操作的状态卡 |
| ER-F02 | 护甲自动抵伤、生命伤害打断 | 伤害／时序框架；FX-001／002引用，不新建被动物品 |
| ER-F03 | 战后状态清理、死亡、胜负与成功事件 | 生命周期／终局框架；不得额外产卡或复活 |
| ER-F04 | 战后恢复、金币与耗时奖金 | 节点／收益框架；与FX-029战内恢复、FX-030产金分开 |
| ER-F05 | 固定镶嵌身份、施法范围、获取和槽位 | IN-A／IN-C框架；只有实际特殊效果进入FX-026／027等，未具名范围增减不凭空成为物品 |
| ER-H01 | 联想／回忆等词汇操作 | [后置词汇问题](../../game-design-workflow/idea-inbox/2026-09-05-vocabulary-design-questions.md)；Raw／Parked，玩家影响和配置关系Unknown，不允许战中换装 |
| ER-H02 | 爆炸、建筑倒塌、草地形态／恢复 | [战场变化来源](../../game-design-workflow/idea-inbox/2026-09-10-battlefield-physical-transformations.md)；表现例子不产生范围伤害、结构破坏或资源效果；具体机制Parked |
| ER-H03 | 传播、燃料、导电、复杂环境关系 | 简单对象边界之外；传播案例另见FX-009，其余仍为范围排除，不补实现规则 |
| ER-H04 | 移动、方向／端点选择、连接／支撑、空间参照 | 按简单对象交互决定暂不做；不能由反弹或转移登记恢复 |
| ER-H05 | 环境材料份额、容器、供材／收材、配方加工 | 暂不做；FX-020只做到对象掉卡 |
| ER-H06 | 战内生命上限成长、复活、身份重置 | [支撑规则](../../game-design-workflow/idea-materials/M-2026-09-07-supporting-design-rules.md)与FAT-C08边界；当前未开放，未来实际提出时登记独立效果并复审有限终局 |
| ER-H07 | 条件触发额外施法或连锁响应 | 现有GR07是声明要求，不是一张已定义“回响”卡；具体现象未提出时不虚构效果 |
| ER-H08 | 硬控制、特殊防御、永久词卡／局外强化 | 支撑规则的后置范围；名称不授予能力，未来逐效资格确认 |

## 已有测试证据的定位

[攻防Candidate v0.1](../../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md)中的参数/T01–T04配置只依赖FX-001／002；[TH-001 r1报告](../test-reports/TH-2026-09-11-001-r1-run-01.md)和[r2报告](../test-reports/TH-2026-09-11-001-r2-run-01.md)仅证明各自固定输入范围。其余案例没有因被列入本表获得新执行证据。测试交接F／GR／MDT／IN-T编号保持原身份，由[TH-002 r7](../test-handoff.md)关联本登记。
