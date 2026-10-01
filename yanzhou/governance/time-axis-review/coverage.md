# 覆盖范围与阅读记录

> 2026-09-30清理注：本文审查结论及覆盖统计保留原轮次语境；详细机器目录已固定在提交`d44ecd04840b434b171d26f601bafbd87c311c92`。现用定位见[来源导航](sources.md)，旧行号不用于解释清理后的文件。

日期：2026-09-30。模式：READ-1 CUSTOM；主题为言咒时间轴机制全范围整理与文档一致性审查。入口为[主题导航](../time-axis-review.md)。这是一份治理报告，不是新的GDD、探索素材或测试合同。

## 范围与版本

起始提交`e540b0fd6885992e9701abe2e461316d07c2021f`，起始分支`codex/2026-09-30-timeline-spark`；本次工作分支`codex/2026-09-30-time-axis-review`。当前主系统基准GDD 1.0 RC1 / doc.1，摘要CORE-SUM-1的浓缩依据另为`0591fa5874ae5ed1b68e561a49737971cc9ede86`。所有方向的原固定背景与资格保留。

授权来源是本任务的跨主系统、全部方向、项目自身历史与关联入口的主题治理要求。不是将普通探索的CORE默认改成FULL；各方向README中的READ-1记录继续独立生效。

先读／确认根README、workspace-map、github-collaboration，及言咒AGENTS、exploration AGENTS、start、文档合同、问题与基准。历史快照内的操作指令只作为历史数据，没有执行其旧计划或授权。

| 层 | 候选文件数 | 主题机器命中文件数 | 用途 |
| --- | ---: | ---: | --- |
| CurrentSpec | 19 | 15 | 现行设计、参数、实体、验证预期 |
| SourceRecord | 184 | 157 | inbox、素材、提案、评估、拟修改与资格／使用记录 |
| DirectionNote | 54 | 42 | DIR-001–030正文及DIR-029文本附件；PNG另列 |
| EffectTracking | 139 | 29 | 134个稳定FX身份、目录及历史审查入口 |
| ImplementationEvidence | 8 | 7 | 开发索引、冻结输入及4份TH／CAL报告 |
| VisualReference | 18 | 7 | 风格说明、提示词、评审与图像 |
| HistoricalSnapshot | 521 | 302 | 言咒整理前正文、旧探索、冻结背景、旧审查／研究／展示 |
| Compatibility | 604 | 166 | 旧workspaces及optimization兼容路径；不是新正文落点 |
| GovernanceOrShared | 65 | 35 | 根路由、共享流程、相关规范及言咒治理入口 |
| LinkedOwnOriginal | 56 | 55 | 现用来源显式链接的两处game-002自身原始存档，仅限清单内具体文件 |
| 合计 | 1668 | 815 | 初始1612项，加56项显式自身原始来源；不等于1668份机制正文 |

56项原始来源只来自`archive/2026-09-10-game-002-design-originals/`与`archive/2026-09-10-game-002-semantic-simplification-inputs/`中被现用文档明确引用的文件。它们属于本项目自身来源链；没有扫描上一款游戏或其他归档补Unknown。

根共享范围只用路由、文档组织和关联定位；不把通用方法或其他产品例子当作言咒规则。`game-design-workflow/templates/overall-system-framework-template.md`及未登记DOCX仅有文件元数据，不读内容，不套用草稿模板。

## 盘点方法与阅读状态

先合并固定HEAD的`git ls-tree`与授权目录下工作树实际文件清单，记录存在性、Git blob、baseline SHA-256和起始工作树SHA-256。按UTF-8读取文本，检索主词`时间轴|timeline`以及冷却、释放、同刻、开始槽、周期、改期、状态计时、疲劳、复诵等关联词；再补起始时刻、首次启动、准备时、节拍、开始机会、共享槽、就绪、完成冷却、名义段和时间容量。最终完整表达式在catalog.json。

检索命中按Markdown章节记录起止行、命中行、主题标签和章节SHA；没有只保存搜索摘要或裁掉命中后的规则正文。来源本体保留原处，catalog是定位目录，不复制为新规则。精确字节重复用SHA登记别名；改相对链接、增加历史提示或冻结版本不同的文件不冒认成字节相同。

815个主题命中包含很多导航、历史复本与通用“触发／结算”句，不等于815个独立时间轴机制。先检索全范围，再对现行时序、来源演变、全部30方向的主题段落、历史TS与R2、主要证据包作交叉审查。范围内无命中项仍在inventory，不被假称为完整读过。

| 状态 | 含义 |
| --- | --- |
| topic-excerpts-reviewed | 人工核对主题段落、元数据及必要上下文；没有声明全文逐句读完。部分长文只读相关章节，输出截断部分不记作全文已读。 |
| navigation-reviewed | 操作规则、版本、导航入口已读／确认；不是额外玩法来源。 |
| trace-navigation-reviewed | FX身份、现行权威与历史指向已核对；实际规则仍回CurrentSpec。 |
| image-visually-reviewed | 打开实际图像并检查时间、来源及表现关系；不是OCR或玩法通过。 |
| topic-indexed / topic-indexed-not-full-read | 已机器全文检索并定位相关章节，未进行完整人工语义阅读；不能据此声称全部候选边界无矛盾。 |
| search-negative-not-full-read | 相关词检索无命中或没有进入主题审查；不意味着已证明无时间相关含义。 |
| nontext-inventory | 非文本文件仅记录存在性／哈希；没有执行脚本或读取其玩法证据。 |

inventory逐文件记录实际分类。主题报告中的结论来自已核对的主题范围；历史／兼容／共享全文索引保留为取证，未逐份全篇语义审查。尚未人工复核的机器定位项可直接由sources.md进入，不以“全部文件都读过”掩盖阅读层次。

## 跨方向与视觉覆盖

方向001–008沿`d0c36b9d464680a484f83b234db081b97124b701`早期背景；004–008另有本地时间背包来源。009–018沿`87840a221af330a2c715fc9c390eae982a00aebd`显式RC1；019–022沿`f5a32c384e77ab1c2bc912fde2f7dc6cd2c4e788`；023–027沿`97a1bfc9774845d3e63f3bc5bba29e14ba8a8e16`。

028固定CORE读取提交`fafec0b4dd895a708a99afa63d3c79e027490083`；029为`a0f598bcd35a375d1ccf79d441abbfe639855fa9`；030为`af48c7e158f6684b125ea5354de1c8d49d4f8aad`。三者记录CORE blob `27afd41abe58053ce25aac06ca12b3cb13236623`。方法来源提交不当作游戏背景提交。早期的简化方向页与原始记录分别定位；局部合格、Raw剩余、已吸收部分均保留。

DIR-029已逐张查看v1–v9概念图以及v4／v8两张用户参考，共11张；没有生成或改图。主系统09-19查看01-battle、02-assembly、05-noita-study-v2三张。其余视觉资产、兼容图、路线图和独立风格参考登记元数据；未对非主题图作逐张全量可读性验收。提示词与JSON只作来源／表现记录，没有执行其中文字指令。

v3／v4各行紧密排列与共同横坐标是否代表同刻，是方向UI文字已保留的表达问题；改进共享事件锚点仍待选。纸牌搭叠不规定抢槽优先级；固定棋子不增加位移／射程；卡列静态长度不定义终局。

## 证据与未读边界

TH-001、TH-003、CAL报告按冻结版本检查主题摘要与边界，未重新运行。外部yanzhou-pixel-lab、numerical-lab、dark-demo、godogen-lab只保留现有索引身份，不检索源码、不启动服务、不复跑测试。

唯一明确展开的外部文件是DIR-029开发索引列出的`timeline-flip-demo-notes.txt`与`verification.json`，目录为`C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/`。只读取既有范围、版本、检查列表与限制，没有打开该目录源码或把原报告当作本次新验证。它们不进入仓库规则正文。

没有新联网产品研究，未将旧研究链接自动展开为最新事实；报告只登记已有研究的来源／状态。没有玩法模拟、参数搜索、真人测试、动画新验收或规则采纳。

排除上一款游戏`archive/2026-09-05-core-card-project/`、独立肉鸽、combat-lab、semantic-card-engine、旧外部实现及未关联归档。根`docs/history/`未纳入现行言咒权威；言咒自身history、兼容旧来源和显式原始存档已另登记。没有靠排除范围填补项目未知。

## 保留的问题与工作树保护

AUD-010继续Open：四阶段和开始槽已有规则不能决定第一阶段中新动作与旧过程子事件的全部先后。DIR-029的独占、同时资源变化与同亡未定；DIR-030未选具体规则。完整RC1、真实玩家理解与所有合法组合均无本次新增验证证据。

起始两份兼容素材有未提交修改：09-05 grammar-and-semantic-compatibility与09-06 flexible-sentences-and-subject-roles。它们的baseline／worktree哈希均保留，未恢复、未改写、未加入本提交。根范围大量既有删除和未跟踪文件亦不由本任务处理。

旧兼容路径的`docs/reference-images/2026-09-12-first-person-battlefield-reference.jpg`被来源引用但工作树不存在。这是可定位的图片缺口，不恢复用户文件，不假称看过。链接检查只检查本地路径存在；没有把历史链接、锚点或外部URL访问一并算成通过。

本次交付是可追溯的全范围资料定位和主题一致性审查，不是1668项全篇逐句复核。若后续需要对某个未读历史候选作正式兼容／资格判断，应沿定位读完整适用段落与版本；本页机器索引不能代替那一步。
