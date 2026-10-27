# 当前设计来源索引

2026-10-27 · SourceReview。当前采纳与资格沿[基准](baseline.md)；本页只回答结论来自哪里，不属于日常开发或完整GDD必读包。引用默认取任务共同提交，来源原件按自身固定输入解释。

## 规则来源

| 内容 | 依据 |
| --- | --- |
| 当前统一卡牌与手动使用 | [CORE-067](../sources/draft-changes/D-2026-10-27-unified-card-model.md)，替换049／058中介产物及065自动上桌、H3、点数和整轮编辑限制；直接产卡、列间布牌和回收，旧规则仅未替换部分生效 |
| 当前限定完整首场输入 | [CORE-066 first-round-battle.1](../sources/draft-changes/D-2026-10-23-round-first-battle.md)，冻结EX-004起始套组及完整敌表；CORE-067已迁移手动路线与相应胜败／恢复预期 |
| 当前回合、手牌、整理与敌牌接口 | [CORE-065 round-hand.1](../sources/draft-changes/D-2026-10-23-round-hand-settlement.md)，替换以下旧来源中的连续拍、Q预留、r→T及对应暂停／疲劳条款；未替换部分沿原资格 |
| 原核心与兼容复用 | [CORE-037起点](../sources/draft-changes/D-2026-10-01-timeline-production-core.md) · [CORE-048兼容复用](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md) |
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
| 统一拍末暂停及动画收尾 | [CORE-064 beat-pause.1](../sources/draft-changes/D-2026-10-23-beat-end-pause.md)，替代CORE-060—063相关停点与音画条款 |
| 通用设计与体验意图 | [2026-10-11集成记录](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/main-system-review-2026-10-11.md) |

## Qualified框架与限定使用

| 来源 | 使用范围 |
| --- | --- |
| [辅槽框架](../sources/materials/M-2026-10-08-augment-framework.md) | 时间／量值权限、标记协同；生产不减料、不单批增产、不直接跨法器加成，不默认统一三阶。D冻结、费用与总序已有后续局部采纳 |
| [行动与标记框架](../sources/materials/M-2026-10-08-action-card-framework.md) | 宿主、实有／预告、简单条件与明示支付；未被具体CORE采纳的通用内容仍Qualified |
| [铭文意图](../sources/materials/M-2026-10-09-inscription-design-intent.md) | 职责、主辅差异及INS-I1—5；发现与长期知识尚未取得完整采纳／保存合同 |
| [法器意图](../sources/materials/M-2026-10-09-artifact-design-intent.md) | 程序实现、决策重心及ART-I1—4；不新增战中重铭或启停 |
| [行动意图](../sources/materials/M-2026-10-10-action-card-design-intent.md) | 战斗表现、资源兑现、单卡清晰与标记联系；不是整包卡池发行 |

EX-004是CORE-066采纳的限定完整首场，执行NotRun；EX-003仍是独立局部派生案例，不是完整单战；EX-001／002限定旧连续拍固定范围；不把其数字当全局参数。旧卡表、旧格子／环境形态、退役探索与Raw UI不自动进入现行规则。来源记录中的当轮Unknown可能已被后续CORE覆盖，当前只查questions；反向引用旧稿不能恢复冷却、完工等位或主动撤批；直接产卡、免费撤回未用行牌与列间确认以CORE-067新采纳为据，不从旧稿推导。

## 历史取证

整理输入为2e967f5e71cc387238131bd18feec47e6b546598。原来源资格、独有排除理由、失败路径及各轮实际阅读范围保留在[原审查全文](https://github.com/dsaj4/game_design/blob/2e967f5e71cc387238131bd18feec47e6b546598/yanzhou/design/source-review.md)，早期材料仍沿其固定Git链接取证；本次不重审或提升历史资格。当前规则改变时只更新上表所指采纳依据与受影响正文，不追加长篇过程，不重建双向使用台账。

<!-- 原来源章节定位统一指向上方固定历史全文，不作为当前规则。 -->
<a id="tl-1当时正式使用2026-10-01"></a>
<a id="旧来源逐类处置"></a>
<a id="审查深度与尚缺项"></a>
<a id="第9轮兼容复用审查"></a>
<a id="ins-1法器铭刻局部复审2026-10-04"></a>
<a id="2026-10-04探索退役后的来源状态"></a>
<a id="routing1敌情资源优先级与供料调时澄清"></a>
<a id="processing1单一处理耗时与开工预留2026-10-05"></a>
<a id="processing2生产与队列接口2026-10-05"></a>
<a id="timing1阶段一共同拍序2026-10-05"></a>
<a id="enemy1阶段二敌情合同与卡面种类2026-10-05"></a>
<a id="action-framework1行动卡与标记通用框架2026-10-08"></a>
<a id="artifact-framework1法器系统整理2026-10-08"></a>
<a id="enemy-framework1敌人系统整理2026-10-08"></a>
<a id="augment-framework1与本轮主系统审查2026-10-08"></a>
<a id="commitment1限定采纳2026-10-08"></a>
<a id="time-formula1耗时公式与外部参照2026-10-08"></a>
<a id="timing2同拍结算2026-10-08"></a>
<a id="resource1资源设计与通用边界2026-10-09"></a>
<a id="inscription-framework1铭文与辅槽整理2026-10-08"></a>
<a id="2026-10-11设计指导集成"></a>
<a id="2026-10-11开发阅读整理与首批案例"></a>
<a id="2026-10-11开发设计对接首轮core-060"></a>
<a id="2026-10-12开发设计对接第03轮core-061"></a>
<a id="2026-10-12开发设计对接第05轮core-062"></a>
<a id="2026-10-12开发对接第06轮职责解释"></a>
<a id="2026-10-12开发对接第07轮core-063"></a>
