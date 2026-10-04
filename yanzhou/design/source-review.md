# TL-1 + INS-1 素材使用审查

Project ID：game-002。文档角色：SourceReview。2026-10-04。当前GDD-0 / 2.1；原RC1审查见[固定版本](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/source-review.md)。

## TL-1当时正式使用（2026-10-01）

以下至第9轮保留原使用记录；当前INS-1覆盖范围见末节，旧材料句法和直接资源输出不再作为现行入口。

| 来源 | 资格／采纳 | 用途与限制 |
| --- | --- | --- |
| [DIR-028核心素材](../sources/materials/M-2026-10-01-timeline-production-core.md) | Qualified；确认结构Accepted | 自动产线、有限队列、敌牌倒计时、自动维护恢复、保存与本轮INT边界 |
| [DIR-028新卡表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/M-2026-10-01-resource-card-pool.md) | Qualified；通用边界局部Accepted，具体内容Proposed | 材料句法等仅按用户答复采纳；13词／4资源／4行动及全部数字没有整包采纳 |
| [P](../sources/proposals/P-2026-10-01-timeline-production-system.md)／[E](../sources/evaluations/E-2026-10-01-timeline-production-system.md)／[D](../sources/draft-changes/D-2026-10-01-timeline-production-core.md) | 正式过程记录 | 结构替代关系、风险、用户授权；不是实验结果 |
| DIR-028第7轮UI与HTML | Raw / Unqualified | 仅展示候选；发布网站不等于采纳页面布局 |

## 旧来源逐类处置

原68份素材与47份inbox的资格、形成过程及原采纳结论保留；本轮不从未读旧inbox抽取新规则。其现行适用性以本表与[逐文件清单](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/reading-log.md)为准，而非文件里的历史“当前”。

| 旧规则来源族 | TL-1处置 | 原因 |
| --- | --- | --- |
| 实体词卡分配、完整法术、同名与实例、词义明确权限 | 有限保留；内容接口重设计 | 仍支持程序配置，不继承旧卡池或副本额度 |
| 目标名单、合法性、已付成本不复制、已成结果不回滚 | 保留原则；己方选目标改为生效时 | 制造成本不能套旧无目标免付；空放已明确 |
| 普通伤害先甲后生命、完整事件终局 | 保留明确基础 | 掉血全杖打断已替代；普通伤害与疲劳分开 |
| 冷却、释放、复诵、开始槽、名义续排 | 由生产／交付／排队／实际顺延替代 | 旧法术过程与新批次不等价 |
| 格子、锚点、宿主距离、邻近脉冲、环境形态 | 退出默认规则，内容重设计 | 用户选择卡牌主战场 |
| 元素本体、火冰层数、镶嵌及53实体 | 保留原设计记录；不列入新版发行池 | 用户要求重新设计卡表 |
| 19节点、三款杖、12场、旧开局与PG值 | 保留历史；新结构下重新评估 | 不能凭旧完整度填充新规格 |
| 路线、休整、商店、单局库存 | TL-32–36补齐路线、库存、节点选择、交易及保存；新参数和可达性重审 | 部分资源跨战引入新的经济关系 |
| 疲劳 | 递增方向再次确认，参数与上界重定 | 不再宣称80／120刻上界适用 |
| 同场开头锁定重播、只读战斗 | 已替代 | 需要保存信息与已提交的战中决策 |
| TH／CAL／Demo及视觉评审 | 原版本证据 | 不证明新机制、卡表或UI成立 |

## 审查深度与尚缺项

已逐页核对现行系统、内容接口、参数与验收；卡表按53实体结构字段审查，历史来源与证据按索引、角色和全文关键词筛查，未把222份全部声称为全文语义复审。每文件的实际覆盖、固定blob与修改／保留理由见reading-log。完整同拍顺序、具体发行池、跨战边界及参数仍Unknown。独立付费干涉能力按用户要求延期。

## 第9轮兼容复用审查

以TL-1提交`ed013948f6c5379fc984413ffd08ae8e7ce0f0c9`继续复核旧Qualified材料的相关规范化章节。[21份直接复用来源表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)逐项列出TL-26–37的当前落点和禁止迁入部分；另两份数值／遭遇素材只作边界对照。旧材料页添加当前适用范围，原文保留。没有把68份素材或47份inbox声称为本轮全文重审。

采用用户明确授权合并的兼容条款，通过既有[P/E第9轮](../sources/proposals/P-2026-10-01-timeline-production-system.md)及[新D](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)记录CORE-048。改变的是当前使用范围，不重写原资格或补造原确认。具体阅读覆盖和固定blob见[reading-log第9轮](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/reading-log.md)。

由此补回构句／绑定／修饰、护甲／支付、真实配置、路线／库存／节点经济及保存约束。旧“施法开始”“执行者”“无目标免付”“整包收益”均按新阶段限定，不覆盖材料句法、空放制造损失、资源携带和战中恢复。没有新的发行卡、效果身份、玩法实测或UI采纳。

## INS-1法器铭刻局部复审（2026-10-04）

[DIR-036局部M](../sources/materials/M-2026-10-04-artifact-inscription-core.md) Qualified、[P](../sources/proposals/P-2026-10-04-artifact-inscription-core.md)／[E](../sources/evaluations/E-2026-10-04-artifact-inscription-core.md)与[D／CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)记录限定采纳。比较输入`a4a7aea8500970ef3504a62e576fc99f08c566db`，逐文件blob与全文／局部覆盖在E；本轮不声称全读历史、其他方向或所有旧候选卡表。

上表及第9轮记录保留当时使用情况；当前适用按以下覆盖：TL-20入口与CORE-041材料—动作—目标已替代；实体占用、耗材分账和卡效绑定继续适用；修饰目的地改为法器辅槽预设；法器直接资源输出退出，高阶材料来源／加工Unknown，资源维护与携带只在内容明确提供时成立。TL-38–45以用户确认结构为来源，不纳入模型推荐或发行例子。

原Qualified卡表保持原资格与历史含义，但完整程序、材料／目标角色与直接资源生产内容须按INS-1复审后才能发行。未更改其原文或声称整池重新合格。原CORE背景不刷新，没有新FX、实验或实现证据。


## 2026-10-04探索退役后的来源状态

用户明确审查后决定删除全部现有方向，测试、UI等信息可后续重做。DIR-001–036的未采纳候选不再进入当前待审清单；上述表格保留原轮次资格与使用事实。DIR-028、036的六份已采纳M/P/E已迁入sources，其原始答复、兼容审查和覆盖记录通过固定Git链接取证。CORE-037–049与现行规则未因清理撤销，未知内容不由旧试点补齐。详情见[清理记录](../governance/cleanup-report.md#2026-10-04探索方向退役)。
