# 当前设计基准

2026-10-12 · documentation.3 / first-example.1 / battle-demo.1 / battle-presentation.1 / battle-focus.1 / physical-table.1。

| 项目 | 当前值 |
| --- | --- |
| GDD | 2.6 / GDD-0 |
| 核心摘要 | v0.21 / CORE-SUM-16 |
| 规则 | TL-1 + INS-1，CORE-037—063；44个现行TL身份（TL-20退役） |
| 本轮增量 | CORE-063：真实3D物件承担全部主页面入口，真实卡片自动呈现已提交事实，近观／系统独立图形页；R9采用用户修正，CORE-060—062停点及案例数值不变 |
| 结构 | 六主系统、两子系统、三公共流程，各保留五文件 |
| 内容 | EX-001保留原回归；EX-002为独立完整单战；具体值仅适用各自固定配置 |
| 证据 | 已实现规则、界面及CORE-061基础音画有局部技术证据，见开发入口；正式音画质量、玩家体验及平衡NotRun；设计采纳不代替验收 |
| 开发状态 | DOC-021—025；0.4保留原限定技术验收，0.5候选未正式交付。第07轮R8／R9完成资格及CORE-063集成；推进每项文字→HTML→美术设计，真实实现须在对应前三阶段复核后记录恢复。见[问题](../governance/questions.md#physical-table-round07)与[开发入口](../development/README.md)。正式美术、性能及真人体验仍未验 |
| 视觉输入 | HTML v10＋效果图v01＋组件v01＋Blender v02；[当前资产及核验](../development/asset-readiness.md)；GLB已接入，正式材质／UI及完整战斗性能仍待验收 |

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
