# 铭文及辅槽系统框架：来源与整理记录

日期：2026-10-08（America/New_York）。Project ID：game-002。文档角色：SourceRecord。修订：inscription-framework.1 / augment-framework.2。任务为文档整理，未产生新的玩法资格、P／E／D 或 CORE 采纳；体验 Hypothesis / NotRun。

## 用户请求与边界

用户原话：“阅读此交接文档，整理铭文及辅槽系统相关内容”。

所附 `yanzhou-framework-handoff-2026-10-08-475adb87.md` 来自系统临时目录，SHA-256 为 `f24a0eb1dec7dc8f516585493872ea64f3aca588dd9e75fd74555cef43a9d54c`。全文用于理解接续背景及来源导航，其中执行建议不代替本轮用户请求；未据其可选分工启动其他 agent、发送消息或扩大任务。原件未提交。

采用 CUSTOM：铭文目录及辅槽子目录五文件、已登记核心／辅槽来源、必要的法器／行动／标记／资源／交互接口和允许的本地原输入相关段落。共享文件仅增量维护本轮导航、来源使用及文档决定。不读取其他探索方向、上一款游戏、外部实现或未登记框架，不启动玩法实验。

开工时主工作区正有其他任务暂存与未提交改动；读取到已提交法器整理基准后，以固定 HEAD `a23c75d74187f45f04b50376658be0274049f3f8` 创建独立工作树和分支 `codex/2026-10-08-inscription-framework`。没有混入主工作区删除、新增原件或其他暂存内容。交接基准 `71e7a0a` 只作接续信息，本轮实际基准以上述完整提交为准。

方法使用项目版 gdd-toolkit 及其适配层，按已登记系统规格和五文件合同归位；没有新的资格晋级或必须重问的选择，沿用已登记确认。未执行完整 GDD 审查，成熟度仍为 GDD-0 通用框架。

## 已提交输入与实际覆盖

下表路径相对 `yanzhou/`，blob 均来自上述固定提交。全文与局部明确区分；检索命中不等于已全文审查。

| 文件 | Git blob | 实际覆盖 |
| --- | --- | --- |
| `design/systems/inscription-system/README.md` | `5346f867b8cb95221425360ec61e947af30ce182` | 全文，原导航 |
| `design/systems/inscription-system/rules.md` | `2a9d602adb517c6cfdd8d8cf31770c3a140eba7d` | 全文，继承 TL 与失败路径 |
| `design/systems/inscription-system/design.md` | `8b16db6b41dae29d9c22030379113f03a10c182b` | 全文，原定位与 Unknown |
| `design/systems/inscription-system/experience.md` | `e6a30e09e4b626eb90584d7e321c9c8317ab3967` | 全文，原理解／情境取舍假设 |
| `design/systems/inscription-system/examples.md` | `96ba590d091e847cce456a53a14750bc464f7fb6` | 全文，原占位 |
| `design/systems/inscription-system/augment-system/README.md` | `9ee382a3a6008266555d4ee7c362bb8b4cdc4512` | 全文，原导航与状态 |
| `design/systems/inscription-system/augment-system/rules.md` | `dac5316b3abb22883843684c857453a46351fd66` | 全文，权限／支付／Unknown |
| `design/systems/inscription-system/augment-system/design.md` | `f8809fe7da3c8b4a74160bbd763988c4340eeb0b` | 全文，定位与建议 |
| `design/systems/inscription-system/augment-system/experience.md` | `26a95379e968166a5a62eea374239d33e6613170` | 全文，四组假设及前提 |
| `design/systems/inscription-system/augment-system/examples.md` | `3d501083928df1dc2775a5d7e730da926eebf4d1` | 全文，协同关系与五条边界例 |
| `sources/materials/M-2026-10-04-artifact-inscription-core.md` | `3b74f54fb61801981da3689756d46393324e043b` | 全文，局部资格、实体分配与理解假设 |
| `sources/draft-changes/D-2026-10-04-artifact-inscription-core.md` | `2ac8ff40f9f8f4c1d25d16d9c5999cbf8ccb6725` | 全文，CORE-049 采纳范围；旧生产阶段按后续当前规则解释 |
| `sources/materials/M-2026-10-08-augment-framework.md` | `4f5b90bb754910adf4e3faeaa10b2d1c65a7cbe5` | 全文，AUG-Q1—5、排除项、未知及使用记录 |
| `sources/inbox/2026-10-08-augment-framework-review.md` | `593b8326b27a331423855a8d5407b57c6b557c83` | 重点完整核对 1—31 行原话；已显示的其他片段只作背景，未以整篇推荐为依据 |
| `design/systems/artifact-system/rules.md` | `f04adf4ef13473c688a8b5aeadf9ea555eb25ec1` | 全文，开工／批次／D／退款及相邻接口 |
| `design/systems/action-card-system/mark-system/rules.md` | `f29a74f7cc1116c05257ff94d8bccbea3c2f78b8` | 全文，宿主／实际层数／支付／未来登记 |
| `design/systems/action-card-system/rules.md` | `4fbe97b9205facd2ea3db1c422c3c4a39003551f` | 35—47、57—67、111—134、142—157 行：行动标记接口、TL-08／21／13／24／29／30／01／44；其余只定位标题 |
| `design/systems/resource-system/rules.md` | `ba5c96ebbe05a724f03b3cdbb3c1b9719fa74013` | 33—43、53—56 行：TL-37／43；其余只定位标题 |
| `design/common/interaction-save/rules.md` | `b032283cf4df1be99a896e248d37d8d502e19f6b` | 11—19、56—81 行：TL-31／36、恢复／携带区分与铭刻打造边界 |
| `design/content/cards.md` | `3a3ab52537667c3ea419d75d2568aa61200565d6` | 全文，内容字段与未发行状态 |
| `governance/questions.md` | `46bae14893f17e1329ab63517c4f0d54e2fa45cc` | 31—49 行：INS-Q01—07 及分组建议 |
| `design/validation.md` | `06d5fce634aaff47bac486563f8fd905eb251733` | 78—96 行：INS-V01—09 与 NotRun |

必要操作规范已读根 README／AGENTS、工作区地图、Git 协作、言咒 AGENTS、exploration/start 与 AGENTS、文档合同、设计流程、模板登记及系统框架模板；GDD 总模板只读系统规格段。systems/README、source-review、decision-log 的相关记录及法器来源审查只用于接续与维护元数据；没有沿其链接扩读其他材料。链接／TL／阅读包检查仅提取路径、锚点和编号，不作为游戏正文阅读。

## 本地未提交输入

原件留在 `E:/Project/game/yanzhou/inbox/`，不复制为新工作树正文，不暂存、不改写。

| 文件 | SHA-256 | 实际覆盖 |
| --- | --- | --- |
| `2026-10-08-artifact-augment-effects.md` | `a6ad801015c976969a23f8d1eba653770597d77f0e7da08268f33d1e36468374` | 1—71、226—239、345—621 行：框架、增幅原则、015—020、配套／套组、打造候选及局部自述“验证”；其他只见标题或关键词命中，未完整复审 001—014 |
| `2026-10-08-action-cards-mark-system.md` | `5ed1cc5dbe621963447294cb8fec32b2bc5d1bfe4c2d58d9f2d2f1fe52c9a566` | 1—90、192—233 行：原确认方向、标记定义与法器互动；其他只见标题或关键词命中 |

`action-cards-stage-delivery.md` 仅定位标题及铭文／辅槽相关命中，不以其数量统计或“兼容性验证”作为证据；`action-cards-pool-design.md`、`mark-system-rules-detailed.md` 未读正文。`augment-system-archive.md`、未登记模板和阶段三旧来源未使用。此前 agent 的全读记录不冒充本轮覆盖。

## 陈述归类与处理

| 内容 | 处理与落点 | 状态边界 |
| --- | --- | --- |
| 铭文 TL-02／26—28／39—42 | Inherited：原条款保留，补输入输出及引用导航 | Accepted；未定卡池、词义和数值继续 Unknown |
| 辅槽 AUG-Q1—5 | 沿现有规则／设计分工，补相邻接口引用 | Qualified／已确认，不晋级完整 CurrentSpec |
| 宿主实有层数、未来预告、足额支付及同拍争用缺口 | Reference：标记权威正文，辅槽只写适用边界 | 不另定生命周期、退款或事件排序 |
| 铭文定位、选择与信息表达 | DesignNote：设计目的、已有约束、建议与未决分列 | 不让建议暗改规则，也不要求每种可选配置必然等强 |
| 理解兼容、实体分配、修饰归因及成长 | ExperienceHypothesis：机制、可能行为、观察与反例 | Hypothesis / NotRun；没有理解率、胜率或“已平衡”结论 |
| 铭文六组例；辅槽五原例展开并补零值／退款／终局 | ExampleSet：前提、过程、结果、未决及依据 | Derived / NotRun；无新卡名／效果身份／默认数值 |
| Raw 减料、虚拟材料、单批多产、完工返料、减少预留占用 | Omit from framework，原件保留 | 与已确认权限不一致或没有授权，不以“示例”进入框架 |
| Raw “不能改 D”及处理中动态变化 | 分开判断 | AUG-Q3 已确认生成时间方向；具体读取／叠加及动态变化未定 |
| Raw 标记增幅、名为“契合”的修饰 | 仅提取权限检查问题，不晋级具体效果 | 行动既有量值修改不自动开放新增标记、持续时间、额外事件或法器契合权限 |
| Raw “初版一个辅槽”“解锁一至两个”、金币价格、成就解锁 | Omit from framework | TL-41 要求逐法器声明；TL-42 的成本、时机和保存 Unknown，不填免费默认或局外成长 |
| Raw 闭环／兼容性／数值平衡结论 | 不作为验证证据 | 原阶段进度前提保留，不证明体验或整套规则已验证 |
| D 读取、基础回退／等待、标记退款、同拍总序、契合和打造 | Park / Unknown；设计页分组给已有建议和依赖 | 整理不替用户作出新玩法决定 |

Omit 指本轮不纳入，不删除原件或改写历史资格；本轮没有建立新素材、提案、评估或拟修改。

## 输出与静态核对

交付入口：[铭文系统](../../design/systems/inscription-system/README.md)及 [辅槽子系统](../../design/systems/inscription-system/augment-system/README.md)。两份实际使用的素材补本轮使用记录，[GDD 来源审查](../../design/source-review.md#inscription-framework1铭文与辅槽整理2026-10-08)及 [文档决定](../../governance/decision-log.md#g002-doc-016)同步必要增量。

检查范围：本任务文件和新增锚点、铭文全部继承 TL 正文、辅槽既有规则与原五例覆盖、44 个 TL 身份、11 个五文件目录和 53 份 GDD 阅读文件存在、原输入哈希、Git 差异与提交范围。检查为文档静态检查；未运行玩法、原型或体验实验。

结果：16 个本任务文件中的 397 个本地链接可达，78 个新增链接及其中 42 个锚点有效；铭文 8 个继承 TL 正文块和辅槽 31 个原规则段完整保留，44 个 TL 身份各有唯一声明。铭文六组例与辅槽原五例的覆盖已逐项核对。11 个五文件目录、空白模板及 53 份阅读文件存在；22 个来源 blob 与 3 个原件 SHA-256 匹配，Git 差异空白检查通过。辅助检查脚本仅留本地 `.git/codex-tasks/`，不提交脚本或原始输入。
