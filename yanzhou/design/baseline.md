# 当前设计基准

规则基准：2026-10-14 · documentation.3 / first-example.1 / battle-demo.1 / battle-presentation.1 / battle-focus.1 / physical-table.2。导航与状态核对：2026-10-18；本次整理不提升GDD成熟度或玩法证据。

| 项目 | 当前值 |
| --- | --- |
| GDD | 2.6 / GDD-0 |
| 核心摘要 | v0.21 / CORE-SUM-16 |
| 规则 | TL-1 + INS-1，CORE-037—063；44个现行TL身份（TL-20退役） |
| 最近规则增量 | CORE-063 physical-table.2：保留真实3D操作宿主，允许绑定宿主的只读必要文本与公开短提示，合法公开投影动作不改结算；CORE-060—062和案例数值不变 |
| 结构 | 六主系统、两子系统、三公共流程，各保留五文件 |
| 内容 | EX-001保留原回归；EX-002为独立完整单战；具体值仅适用各自固定配置 |
| 证据 | 已实现规则、界面及CORE-061基础音画有局部技术证据，见开发入口；正式音画质量、玩家体验及平衡NotRun；设计采纳不代替验收 |
| 开发状态 | 当前能力、最新包与未验范围只在[开发入口](../development/README.md)汇总；DOC-026确认先完善首场核心玩法，再开同一游戏的2D表现。此安排不直接替代CORE-063，见[当前问题](../governance/questions.md) |
| 视觉输入 | 按任务选择[固定资产](../development/asset-readiness.md)和对应视觉稿；B13运行预览与10月17新UI候选分开，不再把旧v10／v02列为所有新任务的默认输入 |

## 状态只在这里统一解释

- **Accepted**：已采纳规则与明确决定。各 rules 页TL条款及CORE-055—063的限定接口按此执行。
- **Qualified**：已确认且可用于设计的素材。辅槽／行动／标记尚未整包采纳的通用框架，以及ART-I1—4、INS-I1—5、行动设计意图仍保留此状态；其已被具体CORE采纳的部分按Accepted执行。
- **EX-001**：用户要求加入的首批案例，三项后续推荐已确认；完整参数在案例内固定，用于展示与开发对照。未晋为全局发行池或平衡结果。
- **EX-002**：用户确认R3后的独立完整单战；疲劳与静态胜败只适用于本场，原EX-001回归不变。
- **Hypothesis / NotRun**：体验、平衡与执行证据未完成。文档版本更新不提升证据等级。

## 来源与追溯

| 内容 | 依据 |
| --- | --- |
| 原核心与兼容复用 | [CORE-037—048来源审查](source-review.md) |
| 铭刻结构 | [CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md) |
| 供料调整 | [CORE-050](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md) |
| 单一D、预留和拍序 | [CORE-051](../sources/draft-changes/D-2026-10-05-single-processing-time.md) · [CORE-052](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md) · [CORE-053](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md) |
| 敌情 | [CORE-054](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md) |
| 冻结与锁定 | [CORE-055](../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md) |
| D公式 | [CORE-056](../sources/draft-changes/D-2026-10-08-processing-time-formula.md) |
| 总序与恢复 | [CORE-057](../sources/draft-changes/D-2026-10-08-settlement-order-reference.md) |
| 资源与跨战 | [CORE-058](../sources/draft-changes/D-2026-10-09-resource-system-design.md) |
| 首批设计与新增明确接口 | [CORE-059](../sources/draft-changes/D-2026-10-11-simple-spell-example.md) |
| 首场操作合同与完整单战 | [CORE-060](../sources/draft-changes/D-2026-10-11-development-design-round-01.md) |
| 首场表现与声音 | [CORE-061](../sources/draft-changes/D-2026-10-12-development-design-round-03.md) |
| 首场失焦与返回 | [CORE-062](../sources/draft-changes/D-2026-10-12-development-design-round-05.md) |
| 桌面3D主交互 | [CORE-063](../sources/draft-changes/D-2026-10-12-development-design-round-07.md) |
| 必要文本与公开投影动作 | [CORE-063 physical-table.2](../sources/draft-changes/D-2026-10-14-demoncards-presentation.md) |
| 通用设计与体验意图 | [2026-10-11集成记录](../governance/main-system-review-2026-10-11.md) |

整理输入固定提交：`a9a7be3a48356379d9fb3eed86c17cfe3ada7325`。此前的基准沿革、各轮来源及独有设计解释保留在[整理前版本](https://github.com/dsaj4/game_design/blob/a9a7be3a48356379d9fb3eed86c17cfe3ada7325/yanzhou/design/baseline.md)及[决策记录](../governance/decision-log.md)。当前问题只查[集中登记](../governance/questions.md)，不从旧轮次的Unknown倒推待办。

<!-- 旧章节链接保留；历史正文见 baseline 固定版本。 -->
<a id="2026-10-08系统框架重建与审查"></a>
<a id="commitment1批次冻结与消费锁定2026-10-08"></a>
<a id="enemy1敌情合同与卡面种类2026-10-05"></a>
<a id="guidance-alignment1设计与体验集成2026-10-11"></a>
<a id="ins-1局部替代2026-10-04"></a>
<a id="processing1局部替代2026-10-05"></a>
<a id="processing2接口补全2026-10-05"></a>
<a id="resource1资源设计与通用边界2026-10-09"></a>
<a id="routing1局部澄清2026-10-04"></a>
<a id="time-formula1耗时公式2026-10-08"></a>
<a id="timing1共同拍序与阶段一完成2026-10-05"></a>
<a id="timing2同拍结算2026-10-08"></a>
<a id="来源与替代"></a>
<a id="现行版本清单"></a>
