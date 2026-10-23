# 按行为查规则

2026-10-23 · Navigation / G002-DOC-028。先读[核心](../design/GDD.md)，再按任务选下表。具体规则只在所指正文维护；来源、历史及不适用细则不随链接自动加载。

## 按行为选细则

| 本次行为／触发 | 必要输入 | 什么时候再展开 |
| --- | --- | --- |
| 改未来用途 | [用途包](../development/task-packs/future-purpose.md) | 新材料、消费阶段或操作宿主时，补对应资源／标记／交互合同 |
| 打断与重开 | [打断包](../development/task-packs/interruption-restart.md) | 改共同排程、维护或周期登记时，补全部受影响接口 |
| 战前装配／新增铭文 | 铭文TL-02／26—28／39—42＋交互TL-31＋实际兼容、库存与获取内容 | 新辅槽效果补辅槽rules；涉及打造补INS-Q05，不猜费用 |
| 改生产耗时／容量 | 法器TL-03／05／07＋核心TL-04／08＋行动TL-11＋参数及具体用途 | 使用标记费补冻结与失效；涉及维护补资源次序 |
| 新行动／支付 | 行动TL-44／11／30、核心TL-08／13／21、内容字段与实际案例 | 有标记或定时再补相应生命周期；无此能力不读全部分支 |
| 改敌牌／遭遇 | 敌人TL-16、行动TL-09／11、核心TL-10／12／13、实际敌表 | 跨循环、锁定、首版限制及恢复都须核对 |
| 改资源取得／维护 | 资源TL-14／15／22／23／37／43、实际配方与初态 | 跨战携带补经济TL-25；基础加工补法器TL-38 |
| 改路线／休整／商店 | 路线TL-32、经济TL-25／33—35、实际库存与节点内容 | 提交与恢复补交互TL-36，不用EX战后片段代替完整路线 |
| 改交互／音画／保存 | 对应行为包或条款＋交互TL-17／19／36及适用CORE-060—063 | 读取实际涉及的合同章节；新2D先处理PRE2D-Q01 |
| 改公共总序／生命周期 | 行动TL-11全文及全部受影响系统、内容、恢复与验收 | 必要时扩大为全GDD；不能把公共变更伪装为局部任务 |

选定后只记录本任务需要的文件／章节。某系统出现新依赖就补读，不能仅靠关键词匹配或固定页数保证输入完整。验收按[行为分组](../design/validation.md)取相关ID；实际执行还需完整内容与具体授权。

## 稳定规则定位

| 规则 | 唯一正文 |
| --- | --- |
| TL-04 实际顺延；TL-08／21队列与空放；TL-10取消；TL-12伤害与中断；TL-13／24终局与疲劳 | [核心GDD](../design/GDD.md)；原系统页保留定位链接 |
| TL-01／44类别与卡效；TL-09揭示；TL-11总序；TL-29状态；TL-30支付 | [行动规则](../design/systems/action-card-system/rules.md) |
| TL-02／26—28／39—42装配、实体、绑定、辅槽与打造 | [铭文规则](../design/systems/inscription-system/rules.md) |
| TL-03／05—07／38／45加工、预留、用途、中断、统一输出与契合 | [法器规则](../design/systems/artifact-system/rules.md) |
| TL-14／15／22／23／37／43资源、维护、量值与配方 | [资源规则](../design/systems/resource-system/rules.md) |
| TL-16固定敌程序 | [敌人规则](../design/systems/enemy-system/rules.md) |
| TL-32单向路线 | [路线规则](../design/common/run-route/rules.md) |
| TL-25／33—35携带、库存、收益、休整与商店 | [经济规则](../design/common/run-economy/rules.md) |
| TL-17—19／31／36交互、战前、暂停、保存与可达性；CORE-060—063首场合同 | [交互规则](../design/common/interaction-save/rules.md) |

TL-20退役，不复用；其余44个TL身份保持。TL-V01—110去除02／20，加INS-V01—09共117项既有预期；另有CORE-060—063合同与EX-002情境，不能把117当作完整覆盖证明。

[辅槽](../design/systems/inscription-system/augment-system/rules.md)与[标记](../design/systems/action-card-system/mark-system/rules.md)的通用框架保留Qualified；已由CORE-055—059等采纳的局部按其范围执行，不整包提升。局外成长尚未设计。历史SYS／R／CG／PG／EG／RG等按[迁移前索引](https://github.com/dsaj4/game_design/blob/2e967f5e71cc387238131bd18feec47e6b546598/yanzhou/governance/rule-index.md)追溯；当前采纳来源查[来源索引](../design/source-review.md)。
