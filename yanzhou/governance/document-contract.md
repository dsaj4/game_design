# 文档职责与统一规范

Project ID：game-002。治理状态：Accepted / Documentation；依据用户授权全量整理。更新：2026-09-24。

## 权威来源

| 信息 | 唯一维护处 | 其他页面的职责 |
| --- | --- | --- |
| 产品范围、体验目标与不变量 | GDD主文档 | core-design为唯一成篇浓缩；core-concept保留版本入口 |
| 探索阅读权限与材料预设 | exploration/start.md | AGENTS负责路由；每DIR记录当轮清单及实际覆盖 |
| 实体语法、类型、条件 | SYS-001 | 内容条目声明具体合法角色 |
| 法杖范围、装配、相位 | SYS-002 | 法杖目录提供索引 |
| 公共执行时序、来源、支付、状态与疲劳执行 | SYS-003 | 元素与卡牌只能声明明确局部例外 |
| 元素／环境身份、宿主能力、生成转化 | SYS-004 | 遭遇表提供初态，不重定义机制 |
| 路线与整局结构 | SYS-005 | 图和交互引用连接规则 |
| 奖励、获取与跨战资源 | SYS-006 | 商品参数引用统一参数表 |
| 交互与恢复合同 | SYS-007 | 实现偏差进入开发索引 |
| 53实体专属角色、短卡面与效果 | content/cards.md | S2／E3为同一实体的分类视图 |
| 词卡时间、量值、取整和商品参数（PG） | parameters.md | 卡牌详情引用对应行；示例明确非独立默认值 |
| 环境形态阈值（EG） | SYS-004 | PG不重复环境阈值 |
| 疲劳参数（RG06） | SYS-003 | 参数总入口链接该节 |
| 敌人能力、初态与布场 | content/enemies-encounters.md | 系统页不复制敌人表 |
| 术语 | CONTEXT.md | 规则页引用定义，不另改词义 |
| 效果登记、应用、历史修订 | effects/ | 关联规则和内容，不复制整套通用规则与价格 |
| 规则验收预期 | GDD validation.md | 测试交接指定冻结输入，报告保留实际结果 |
| 设计原因与替代范围 | decision-log及Draft Change | 当前正文直接陈述规则并链接来源 |
| 探索候选 | exploration/各DIR方向文件夹 | 只经明确回写流程进入主系统 |

## 规则写法

按“规则ID／对象／前置条件 → 时点与名单 → 支付 → 结果与单位 → 零值和失败 → 有限触发与终止 → 正例和反例 → 决策与验收来源”陈述。

具体条款覆盖通用规则时必须明示规则ID、适用对象和覆盖范围，不能只靠更晚日期或更具体的卡名自动取得例外。找不到裁决时登记Open，不根据代码行为反向采纳。

参数至少包含：ID、单位、数值／公式、合法域、零值许可、适用角色及来源。C是冷却，L是释放段，τ是词卡时间；历史c／r在当前文稿分别按C／L理解。明确区分开始槽仲裁、完整事件、过程子事件和派生响应。

每份现用文档标明Project ID、文档角色、设计基准、文档修订、设计／证据状态及来源。Navigation、CoreDesignSummary、ExplorationReadingContract、CurrentSpec、SourceRecord、DecisionRecord、HistoricalSnapshot、ResearchComparison、ValidationSpec、ImplementationIndex不得混用。

## 状态与变更

- 设计：Raw／Qualified／Proposed／Accepted／Parked／Rejected，资格和采纳分别记录。
- 证据：Hypothesis／NotRun／LimitedEvidence／ValidatedForScope，必须附版本与覆盖范围。
- 实现：NotStarted／Partial／ImplementedForScope，与设计状态独立。
- Closed只关闭指定问题；不得推出全系统无歧义。GDD-2是文档成熟度。
- 当前入口只有一个“当前”；日期型旧结论放history或有明确HistoricalSnapshot标识的原报告。
- 概览和卡面允许简写，但不构成第二处可独立修改的规则／参数。修改权威来源时核对所有示例与派生摘要。
- 新玩法先资格确认；文档整理不扩大采纳范围。当前机制变更继续P／E／D与决策记录，保护文件同轮提交推送。
- 不修改原实验结果，不借新规则重命名旧输入。原始背景包与外部资料快照不得原地刷新。

## 迁移与链接

旧GDD及主题入口保留兼容页；整理前文本在history，原提交记录于baseline。旧研究应按其提交／哈希取证，不能把兼容页跳转后的正文视为原研究输入。归档、源文件、未提交用户修改不纳入自动替换。

## 系统间接口

构句输出合法法术与引用条件；法杖输出锁定配置和空间／时间参数；战斗按阶段执行；元素系统提供对象变化结果；收益系统只在规定节点提交资源；交互提供查看和授权动作。图像、演出和代码的默认行为均不能新增规则。


## 探索构思的轻量存储

每个方向以README保存必要构思、问题、来源和阶段，comparison集中保留跨方向判断与吸收范围。正文摘录属于DirectionNote，不等于CurrentSpec。旧流程记录在history/exploration-2026-09-24；不在活动探索区恢复同名流程树。需要正式设计输出时才建立带类型ID的独立材料，资格与回写规则按exploration/AGENTS执行。


## 核心摘要与阅读合同

core-design.md沿GDD核心事实浓缩，不拥有独立规则裁决权；更新GDD循环、范围、系统关系或不变量时必须复核摘要，更新来源基准或显式标待同步。core-concept.md只保留版本与兼容导航，避免两套长摘要竞争。

探索输入按start.md，用户选择的窄范围不会因文内链接或本文件提及其他来源自动扩大。全量阅读中，CurrentSpec定义现行规则，SourceRecord保留原资格，HistoricalSnapshot仅按原轮次，ImplementationIndex不反向覆盖设计；治理清单中的其他方向名称只作元数据，不作为候选设计来源。缺少详细GDD输入时，不对规则相容性作完整结论。
