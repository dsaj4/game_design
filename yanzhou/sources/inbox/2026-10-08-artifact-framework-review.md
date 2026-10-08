# 法器系统框架整理：来源、归类与边界

Project ID：game-002。文档角色：SourceRecord。日期：2026-10-08（America/New_York）。修订：1.0。状态：Documentation / 既有来源复用；不是新增 Qualified 素材、Proposal、Evaluation 或玩法采纳。证据：继承规则推导；体验 Hypothesis / NotRun。

## 请求与阅读范围

用户原话：“阅读此交接文档，整理法器系统相关内容”。附件为本地 `yanzhou-framework-handoff-2026-10-08-475adb87.md`，SHA-256：`f24a0eb1dec7dc8f516585493872ea64f3aca588dd9e75fd74555cef43a9d54c`。附件提供前序工作背景及建议流程；本轮范围以用户指定法器系统为准，不将其中可选分工、后续任务或测试建议视为新的执行授权。

阅读模式 CUSTOM。固定已提交基准：`71e7a0a18709e19e85ea171feb10b2ba2b432097`。范围为法器五文件、法器内容合同、相关铭文／辅槽／行动／标记／资源接口、已登记框架素材及局部原输入；来源与治理索引只作必要的状态和使用记录维护。已提交输入在开始时无本轮范围内的工作树差异；本地未提交原输入另记哈希，不代为提交。

沿既有记录中“阶段 1—4 已完成”与“仅系统通用框架”的前提，不重做阶段或发新卡池。未读上一款游戏、其他探索方向、外部实现和历史链接正文；没有联网、原型、Demo、玩法实验或实现核验。

操作依据：根 README／AGENTS、workspace-map、github-collaboration、言咒 AGENTS、探索 start／AGENTS、document-contract、design-workflow、已登记模板入口及 system-framework/README。方法使用 gdd-toolkit 及其项目适配层，仅作分类与必要接口核对；没有发起新的资格确认或重复采访 AUG／ACT 答复。

## 已提交游戏输入与实际覆盖

下表均来自上述固定提交。哈希为 Git blob；没有把链接中的历史材料算作已读。

| 文件（相对 `yanzhou/`） | blob | 实际覆盖 |
| --- | --- | --- |
| `design/systems/artifact-system/README.md` | `604cd712049da1b99d7a4ecf9d838736aa3bcd12` | 全文，原导航 |
| `design/systems/artifact-system/rules.md` | `77a1cc0b62bd0e8811e83aa13bd8b0a126f78338` | 全文，七个既有 TL 条款及 Unknown |
| `design/systems/artifact-system/design.md` | `846c09bee75996b094e3b0f45d0718a78448a198` | 全文，定位、未知与契合种子 |
| `design/systems/artifact-system/experience.md` | `a0148b49a5f08073ce60973dd73835e29b361dbb` | 全文，原假设与观察线索 |
| `design/systems/artifact-system/examples.md` | `0ebeced83269e035f08964dd45c9fa0b19666ef8` | 全文，六条短例 |
| `design/content/wands.md` | `c09149d5f180cb34bcafa08e972da23303fc974d` | 全文，内容字段与未发行边界 |
| `design/systems/inscription-system/rules.md` | `2a9d602adb517c6cfdd8d8cf31770c3a140eba7d` | 全文，合法配置、实体、主辅槽及契合分工 |
| `design/systems/inscription-system/augment-system/rules.md` | `dac5316b3abb22883843684c857453a46351fd66` | 全文，权限、支付与未知接口 |
| `design/systems/action-card-system/rules.md` | `4fbe97b9205facd2ea3db1c422c3c4a39003551f` | 全文，完工后的队列、目标、支付与终局 |
| `design/systems/action-card-system/mark-system/rules.md` | `f29a74f7cc1116c05257ff94d8bccbea3c2f78b8` | 全文，实有状态、支付与未来登记 |
| `design/systems/resource-system/rules.md` | `ba5c96ebbe05a724f03b3cdbb3c1b9719fa74013` | 全文，材料可用、维护与数量合同 |
| `sources/materials/M-2026-10-08-augment-framework.md` | `8b940e555c1ef8eebf8b08a4289b6910033ded55` | 全文，复用 AUG-Q1—5 的局部资格 |
| `sources/materials/M-2026-10-08-action-card-framework.md` | `8fb94ae2efbc2b5188965c121907e0ec4a96b626` | 全文，复用行动／标记接口资格 |
| `sources/inbox/2026-10-08-action-card-framework-review.md` | `cfeb9d21f85cd12a199f9e3fce8365dd283880fc` | 全文，已有确认、差异与原件哈希 |
| `sources/inbox/2026-10-08-augment-framework-review.md` | `593b8326b27a331423855a8d5407b57c6b557c83` | 局部：原始想法与 AUG-Q1—5 原话；已显示的诊断及框架前段只作对照，不称全文重审 |

此外读系统目录、source-review 相关使用记录及 decision-log 的 CORE-054／DOC-012—014；决定标题、规则 ID、阅读包与本地链接仅检查元数据。没有阅读整个 GDD 包，也未沿来源递归审查所有 M／P／E／D。未提交的 conflict-register 和其他删除／新增文件未修改或纳入本轮。

## 未提交输入

原件保持原位，全文身份以哈希固定；只对下面明确覆盖作判断。检索命中不算其他段落已经全文审查。

| 本地路径（相对仓库） | SHA-256 | 实际覆盖与用途 |
| --- | --- | --- |
| `yanzhou/inbox/2026-10-08-action-cards-mark-system.md` | `5ed1cc5dbe621963447294cb8fec32b2bc5d1bfe4c2d58d9f2d2f1fe52c9a566` | 1—60、156—235、418—452 行；定位确认方向、法器互动例和 Q-MARK；其余只见标题／关键词命中 |
| `yanzhou/inbox/2026-10-08-artifact-augment-effects.md` | `a6ad801015c976969a23f8d1eba653770597d77f0e7da08268f33d1e36468374` | 1—225、345—437 行；框架、001—008 与 015—020 原例；其他效果及套组只见标题／关键词命中，不称完整复审 |

`action-cards-stage-delivery.md` 仅定位标题，未以其数量、套组或“验证”文字作为本轮依据；`action-cards-pool-design.md` 与 `mark-system-rules-detailed.md` 本轮未读正文。未跟踪的阶段三旧来源、augment-system-archive 与未登记模板未作为现行材料。既有来源记录的阅读覆盖不冒充本轮完整阅读。

## 陈述归类与使用决定

| 材料／陈述 | 处理 | 落点及理由 |
| --- | --- | --- |
| 法器 TL-03—07／38／45 | Include / Inherited / Accepted | 保留规则与原来源；供料防御的情境句移到 examples，不改运行约束 |
| 材料、铭文及队列合同 | Reference | rules 与 README 链接相邻权威，不复制一套可独立修改的规则或参数 |
| AUG-Q1—5 中与法器有关的分工 | Include as Qualified interface | rules 引用生产侧只改生成时间、量值落行动卡、标记协同、足额检查支付；定位／成长解释进入 design，未扩大采纳 |
| ACT-Q1／2 与标记实有状态 | Include as Qualified interface | 只引用已登记接口：先按队列行动，后续定时登记独立；预告不是余额，行动和法器按声明读／付 |
| 自动运行、瓶颈识别与应对 | ExperienceHypothesis | 原目标拆成可能行为、支持／失败信号及后续观察方法；不伪造数值目标或体验证据 |
| 六条短例与边界推导 | ExampleSet / Derived / NotRun | 按用途、前提、时点、结果、未决整理；补入零值、空放、截止、退款与终局边界，无新发行身份 |
| “剑与盾之符＋攻击／防御”及契合形式 | 保留原状态 | design 保留种子；数值改变、改写、附效及“契合附魔”均未选择 |
| 后续临时提速结束后保留“合法增产” | 澄清用语 | 原建议保留且仍未开放操作；增产解释为一段时间内可能增加完成批次数，不恢复辅槽单批增产 |
| 旧输入减料、虚拟材料、增单批张数（含 001／002／004／005／006／008／015／016／017） | Omit from framework | 与后续 AUG-Q3 的权限收窄不一致；保留原输入和原确认，不按新日期静默重释旧名称 |
| 003 开工产资源、018 完工返料、019 少预留同样张数、020 虚拟首批材料 | Omit from framework | 无通用授权，分别涉及生产输出／材料成本／容量承诺；不能以“效率”或“例子”恢复。未将任何一例转为正式卡效 |
| 007 标记改 D 及“D 唯一所以不能改 D”的旧建议 | 分开判断 | 生成时间方向已有 AUG-Q3 确认，但具体名词、每层减一、全耗及最低值算例没有因此整体合格；只保留通用接口 |
| Raw 中“完工附加效果” | 不推定立即生效 | 若描述的是产出行动的字段，仍须经行动兑现；不能在制造完成时直接生成宿主标记或绕队列收益 |
| 支付失败分支、退款、D 快照、同拍标记竞争、契合叠加 | Park / Unknown | 集中至 design；原 AUG-Q4 不决定这些细则。给下一批处理顺序，不把推荐写成答案 |

此处的 Omit 指本轮框架不纳入，并非删除原文、撤销全部历史资格或替用户做新的玩法拒绝决定。Raw 效果没有为填满框架而晋级，亦未新建 M／P／E／D。

## 输出与检查

[法器五文件入口](../../design/systems/artifact-system/README.md)为交付入口；两份既有 Qualified 素材补使用记录，系统目录及 [GDD 来源审查](../../design/source-review.md#artifact-framework1法器系统整理2026-10-08)同步必要增量。文档组织决定见 [DOC-015](../../governance/decision-log.md#g002-doc-015)。

检查限定为：本任务链接与锚点、继承 TL 内容及六例覆盖、五文件结构和固定阅读包文件存在、原输入哈希、提交范围。玩法证据保持 NotRun。未决问题及按依赖分组的推荐见 [设计页](../../design/systems/artifact-system/design.md#未知与依赖)；本轮整理无需将这些问题先裁定为新规则。

结果：321 个本地链接、64 个新增链接及 32 个新增锚点检查通过；44 个 TL 身份未丢失或重复，法器原条款的 63 个句片段及状态表行保留，六条原短例均有对应展开；11 个五文件目录与 53 份阅读文件存在，两个原输入哈希未变。检查辅助仅存本地 `.git/codex-tasks/`，未提交脚本或原始输入。
