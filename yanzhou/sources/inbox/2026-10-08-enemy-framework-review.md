# 敌人系统框架：来源审查与归位

Project ID：game-002。文档角色：SourceRecord。日期：2026-10-08（America/New_York）。修订：enemy-framework.1。状态：Documentation；继承的玩法保持原 Accepted／Qualified 状态，未确认扩展保持 Raw / Unqualified。证据：Hypothesis / NotRun。

## 用户请求与阅读范围

本轮用户原话：“阅读此交接文档，整理敌人系统相关内容”。交接文件为 `C:/Users/Administrator/AppData/Local/Temp/yanzhou-framework-handoff-2026-10-08-475adb87.md`。它用于定位材料及既有约定；其中建议分工、阶段续作、创作或执行步骤不视为本轮新增授权。本轮由单个 agent 整理现有敌人框架，没有启动其他 agent。

模式 CUSTOM。固定基准为 `a23c75d74187f45f04b50376658be0274049f3f8`，进入时分支 `codex/2026-10-08-artifact-framework`，任务分支 `codex/2026-10-08-enemy-framework`。交接列的 `71e7a0a` 已有后续法器整理提交；本轮采用实际 HEAD，不回退文件。

允许范围为敌人五文件、敌人与遭遇内容、必要的行动／标记／法器／资源／路线／信息保存接口及其已登记来源。`yanzhou/inbox/` 中只检索和选读敌人相关片段；未提交原件单列哈希，不将其整体当作已确认设计。治理、导航与模板只作路由和维护。未读取完整 GDD 包、其他探索、历史正文、上一款游戏、外部实现或视觉资源；未联网、未执行原型或玩法实验。

操作依据：根 README／AGENTS、workspace-map、github-collaboration，言咒 AGENTS，探索 start／AGENTS，document-contract，design-workflow；使用项目 gdd-toolkit 及适配层，沿已登记五文件模板。没有新增玩法资格确认，故不生成新的 M／P／E／D，也不重新采访阶二 Q01—24。

## 已提交输入与实际覆盖

下表路径相对 `yanzhou/`；blob 固定本轮输入版本。局部阅读不会被记为全文。

| 已提交材料 | Git blob | 实际覆盖 |
| --- | --- | --- |
| `design/systems/enemy-system/README.md` | `28d3cefcfba27f8afb1e3c0d2b87832a76fbbbe5` | 全文；原五文件基准 |
| `design/systems/enemy-system/rules.md` | `b846b9d4736cdaf69ee4e3e5d6de0a871675e405` | 全文；原五文件基准 |
| `design/systems/enemy-system/experience.md` | `67c1774a520863df1b5e174a85be73f19551c85f` | 全文；原五文件基准 |
| `design/systems/enemy-system/design.md` | `d069e56455dcd945d299e15727573a70da225f21` | 全文；原五文件基准 |
| `design/systems/enemy-system/examples.md` | `0932b8c1df9bde6ee1e900266433a44261a7c089` | 全文；原五文件基准 |
| `design/content/enemies-encounters.md` | `f2f3d3bfbbf24df8eaa00d4edbde7797c36728a8` | 全文；字段、限制、表现与候选状态 |
| `design/systems/action-card-system/rules.md` | `4fbe97b9205facd2ea3db1c422c3c4a39003551f` | 全文；生产与敌牌流程边界 |
| `design/systems/action-card-system/mark-system/rules.md` | `f29a74f7cc1116c05257ff94d8bccbea3c2f78b8` | 全文；Qualified 宿主、定时与权限 |
| `design/systems/artifact-system/rules.md` | `f04adf4ef13473c688a8b5aeadf9ea555eb25ec1` | TL-05／06／07；其余仅标题与接口定位 |
| `design/systems/resource-system/rules.md` | `ba5c96ebbe05a724f03b3cdbb3c1b9719fa74013` | 开头至 TL-37（1—41 行）；TL-22 仅定位，其余正文未读 |
| `design/common/interaction-save/rules.md` | `b032283cf4df1be99a896e248d37d8d502e19f6b` | 全文；信息、暂停、恢复与可达性 |
| `design/common/run-route/rules.md` | `6336b1f6a92a3c9ecd463a6d704a05a2362c2fb2` | 全文；出发前摘要与敌人接口 |
| `design/validation.md` | `06d5fce634aaff47bac486563f8fd905eb251733` | enemy.1 节 TL-V61—68；其他仅标题定位 |
| `sources/inbox/2026-10-05-stage-two-enemy-pressure.md` | `34a0fe8646b0bccde1909183d8302b5588629ca6` | 1—152、258—359、393 行至结尾；候选逐拍正文与旧阅读表未读 |
| `sources/materials/M-2026-10-05-stage-two-enemy-pressure.md` | `4b92e2fc0bc713b11b8b0f499120967925b06d38` | 全文；既有资格及设计假设 |
| `sources/evaluations/E-2026-10-05-stage-two-enemy-pressure.md` | `0dcd389dbb89e218f524199249dd6686e3d96358` | 全文；仅引用原文档推演的证据范围 |
| `sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md` | `357739f17418b9decabe4dba3429f6b70f4b9312` | 全文；CORE-054 采纳边界 |
| `sources/materials/M-2026-10-08-action-card-framework.md` | `49682c23b1ffb8f8f93d448567d8b71bde16dee6` | 全文；仅引用已确认通用接口 |
| `sources/inbox/2026-10-08-action-card-framework-review.md` | `cfeb9d21f85cd12a199f9e3fce8365dd283880fc` | 全文；已有答复与 Raw 排除范围 |
| `design/systems/README.md` | `f47d45e494cd6d821ea30d85029fc4c5a740cba4` | 全文；导航状态 |
| `design/source-review.md` | `c7984c836ac847d7a0812c96763a493d978f908c` | enemy.1 及之后三节；其余仅相关来源定位 |
| `governance/decision-log.md` | `75300d00c51e5a1c937c024e69f5482a39a52ef6` | CORE-050—054、DOC-014／015；其余仅标题与敌人相关索引定位 |
| `governance/questions.md` | `46bae14893f17e1329ab63517c4f0d54e2fa45cc` | 敌人相关摘要、TL-Q02／05、routing.1；其他未作正文审查 |
| `governance/rule-index.md` | `4955dc98df721e8d2cafa522d9a0d7fb7da085ff` | TL-16 与相邻规则定位；元数据 |

来源／决策索引只核对 enemy.1、action-framework.1、artifact-framework.1、CORE-050—054、DOC-014／015 相关片段；rule-index 和其他系统 TL 声明只用于身份、链接和结构检查，不作为扩展玩法背景。sources 入口及 inbox 入口只作来源导航。53 份阅读包和 11 个五文件目录的核对是文件存在性检查，不代表通读。

## 未提交材料与固定哈希

五份原件先以“敌／遭遇／预警／预告”等相关词检索；命中只能作为定位，不宣称全文件审查。以下是随后实际读取的连续片段，行号对应本轮哈希。

| 本地原件（相对 `yanzhou/inbox/`） | SHA-256 | 实际覆盖 |
| --- | --- | --- |
| `2026-10-08-action-cards-mark-system.md` | `5ed1cc5dbe621963447294cb8fec32b2bc5d1bfe4c2d58d9f2d2f1fe52c9a566` | 1—75、115—143、415—451 行；其余仅相关关键词命中 |
| `2026-10-08-mark-system-rules-detailed.md` | `b1dcfbfbb7432df8e64c664cbd82d8fc795c38605f234227a4eedd40ef5c4c9d` | 1—33、126—146、324—345 行；其余仅相关关键词命中 |
| `2026-10-08-action-cards-stage-delivery.md` | `08cfc166512a620cd444d4ab9ad244df34cb162f12bfd758be5192d413c6ba2b` | 1—12、280—296 行；其余仅相关关键词命中 |
| `2026-10-08-action-cards-pool-design.md` | `4fe43871392a4ec219942881aeead19abfc7dd58912f6141fd9f4f3d1fedaff9` | 442—490 行；其余仅相关关键词命中 |
| `2026-10-08-artifact-augment-effects.md` | `a6ad801015c976969a23f8d1eba653770597d77f0e7da08268f33d1e36468374` | 650 行至结尾；其余仅相关关键词命中 |

交接文件 SHA-256：f24a0eb1dec7dc8f516585493872ea64f3aca588dd9e75fd74555cef43a9d54c。原件不改写、不纳入提交；正式框架的确认依据仍是已提交的阶段二 M／E／D 和行动／标记局部 M，避免依赖本地未提交文件的链接。

## 分类与归位

| 内容 | 状态与处理 | 位置 |
| --- | --- | --- |
| 敌人 TL-16、固定程序、全敌牌正延迟、取消留空档、段尾保留 | Inherited / Accepted；保留 TL 身份与失败路径 | [rules](../../design/systems/enemy-system/rules.md) |
| CORE-054 已采纳的必需字段、首版无护甲／防护、不同拍到期、截击条件 | 从内容合同归位；不重新采纳，不外推为永久限制 | rules；内容页原章节保留导航 |
| 锁定、落空、共同拍序、终局、返工、信息与恢复 | 只整理敌人所需接口与权威链接，不另设通用结算规则 | rules；权威仍在行动卡／法器／交互 |
| 窗口相对式 | Derived；写清空闲、有料、有位和无排队前提 | rules；具体分支进入 examples |
| 压力改变选择、关键威胁节奏、秘仪与炼金及取材边界 | 既有方向保留；图谱页为候选，史实未核实 | [design](../../design/systems/enemy-system/design.md) |
| 机制—行为—体验及观察方式 | 从既有 Qualified 材料的假设和风险展开；无玩家结果 | [experience](../../design/systems/enemy-system/experience.md)，NotRun |
| 揭示、截止、锁定零值／并列／无施法、危险续开、致死、地域符号 | 六组已采纳规则说明，含失败边界；不新增数值与验收身份 | [examples](../../design/systems/enemy-system/examples.md)，Derived / NotRun |
| 绿狮、万溶之液、雷比斯及后续形态 | 保留候选、Illustrative 与 Park／Exclude 状态，具体程序表不改 | [内容目录](../../design/content/enemies-encounters.md) |
| 玩家／敌人均可持正负标记，实有层数与未来预告分开 | 只引用已登记的局部 Qualified 接口；不解除首版限制 | rules 的 Qualified 引用及标记权威页 |

“来源敌人死亡即胜”仍须读完整事件后、玩家存活及同检查点双亡失败的共同条件；本轮在接口和示例中明确这些条件，没有改成敌人先死就跳过玩家失败检查。候选的生命、伤害、Δ、L 与真实法器配套仍未冻结；阶段完成前提不被本次文档检查重判。

## 新材料中的未采纳扩展

以下只是 Raw 差异审查，未进入正式机制、敌牌表或示例；原文件标题中的“Rules / Raw Qualified”“交付完成”“兼容性验证”不提供整份资格或运行证据。

| 原片段与来源 | 与现行框架的关系 | 本轮处理 |
| --- | --- | --- |
| 主材料“迟缓：目标的Δ延长1拍（每层）”；详细规则迟缓行、卡池 AC-023 同类表述 | 固定时间表和既有标记宿主资格不自动授予改延迟能力；阶段二已把改速／改延迟列为新规则类 | Omit from framework；保留 Raw，不改 T／Δ |
| 主材料及详细规则“当敌牌翻开时”获得先兆、灼烧绑定敌牌 T 等片段 | 简单标记条件和指定拍登记不等于新事件触发；取消／来源死亡后的绑定语义及同拍位置未闭合 | Omit；未知由行动／标记接口承接，不靠示例补排序 |
| 卡池 AC-024“辅槽扩展：可取消打断⊘类敌牌” | 不能从未确认具体辅槽例取得目标类别扩展；通用取消权限仍须能力明示 | Omit；不据此发行能力或修改辅槽权限 |
| 卡池 AC-025“提前取消未揭示敌牌”“敌人施法成本增加” | 前者未获得现行取消合同授权；后者假定了未建立的敌方制造成本 | Omit；保留 Raw，不给敌人补造法器或配方 |
| 阶段交付“敌人施加负面标记给玩家”“敌人对自己施加正面标记”“10-15张敌人行动卡” | 两方正负宿主的方向已有局部确认；具体卡数、卡效、BOSS 强化和完整发行池没有随之采纳 | 仅引用宿主接口；张数与具体敌牌继续为未采纳计划 |
| 辅槽原件“敌人行动卡设计……与玩家辅槽形成对抗”，结尾 Content Design / Raw | 后续内容任务，不是本轮整理必须执行的设计或实验 | 保留来源，不启动制作或平衡测试 |

不将本表视为永久拒绝。若以后明确开发这些扩展，应补对象、情境、行为／可见影响、价值、与当前规则关系及验证方式，再沿既有资格与采纳流程处理。

## 双向使用与检查

本次使用的 [阶段二 M](../materials/M-2026-10-05-stage-two-enemy-pressure.md)及 [行动／标记 M](../materials/M-2026-10-08-action-card-framework.md)追加使用记录；[GDD 来源审查](../../design/source-review.md#enemy-framework1敌人系统整理2026-10-08)与 [DOC-016](../../governance/decision-log.md#g002-doc-016)记录文档组织。规则权威、已有 TL 身份及 53 份 GDD 阅读包结构不变。

本轮检查结果见 DOC-016：只做本任务差异、来源状态、迁移保留、链接／锚点、目录和原件哈希静态核对；未运行玩法、原型、代码或真人测试。其他人的修改与本地原件不纳入提交。
