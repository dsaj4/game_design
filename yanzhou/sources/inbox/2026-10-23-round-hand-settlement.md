# 回合末结算与手牌：输入摘要

2026-10-23。来源：用户本轮对话；只留意图和决定摘要，不保存原话。阅读模式CUSTOM。共同设计输入固定为`b1172f20f24eba5613d63c316256e46e85f8ffc1`；本轮M／P／E／D继承这个版本，不随分支移动更新。

## 用户最初提出的方向

本节保留提出时的意图与未定项；现行决定以下方CORE-065摘要为准。

将连续逐拍出牌改为每X拍一回合，初始候选X=5。敌我相对两行，每行X个位置；敌方回合开始布满暗牌，只显牌背部分信息，玩家由法器在规划期间自动产牌入行。回合末从左到右逐渐结算，再进入下一回合。

玩家超过桌面行的成品进入手牌，初始候选上限3；新增后若超限，最右卡消失，自动入行／入手不收操作费。规划结束前可暂停，付费交换桌面两牌、桌面与手牌互换、向最左空位补一张牌；费用／行动点的来源和额度尚未确定。

敌人分即时和延时行动：即时牌翻开即处理；延时牌结算时生成下一回合才能使用的对应牌，进入敌方手牌。非回合开始时再布敌牌仅列未来空间，不纳入本轮初版。

目标是限制主桌时间信息范围，消除持续移动造成的左侧空区，使玩家看见当前布牌并能调整，集中呈现结算过程。“信息更清楚、决策更多”是体验假设，不是已观察结果。

## 资格范围

意图、对象（时间／队列／敌情／交互）、玩家情境、明确操作、可见结果、价值、现行冲突和下一决策方法均已可定位。按grill-with-docs先查已有规则；不重问用户已经表达的方向。只把上述方向晋级为[合格素材](../materials/M-2026-10-23-round-hand-settlement.md)，不把agent补出的细则晋级为用户决定。

状态：**Promoted，方向Qualified；R01—R13已明确采纳为CORE-065。** 用户在审阅后全部采用推荐，仅将疲劳首次改为第10回合末；每回合一次、双方5×n及其他推荐保留。审阅稿固定提交为`084e529e2c852d2e1a508f74a8766e55763f9933`；这是本次采纳所对照版本，旧设计输入仍为上方共同版本。用户要求大改先复核歧义和冲突，无阻塞则直接同步，仍不实现或测试。最终只记[决定摘要](../draft-changes/D-2026-10-23-round-hand-settlement.md#决定摘要)，不留逐题问答。初始参数不代表平衡通过。

## 实际使用的设计材料

5份启动文件之外，仅展开以下受影响接口；链接是本轮已读定位，不授权继续递归读取。

| 材料 | 用途 |
| --- | --- |
| [术语](../../CONTEXT.md)、[基准](../../design/baseline.md)、[行为索引](../../governance/rule-index.md) | 分清拍、回合、Q、预留、手牌及采纳范围 |
| [决定摘要CORE-037—064](../../governance/decision-log.md#核心决定)、[CORE-064原采纳](../draft-changes/D-2026-10-23-beat-end-pause.md)及其M／E | 查已有生产、敌情、总序、消费锁定和暂停决定；不声称重读所有历史来源 |
| [当前问题](../../governance/questions.md#开发前先看) | FB-Q01／02、TL-Q09、PRE2D-Q01及扩展边界 |
| [行动TL-09／11／29／30](../../design/systems/action-card-system/rules.md)、[法器TL-03—07／38](../../design/systems/artifact-system/rules.md)、[敌人TL-16](../../design/systems/enemy-system/rules.md) | 生产、排序、容量、敌情和终局的公共变更 |
| [资源TL-14／15／22／23／37／43](../../design/systems/resource-system/rules.md)、[标记](../../design/systems/action-card-system/mark-system/rules.md) | 新资源可用、失效、维护、冻结、支付和定时接口 |
| [铭文TL-02／27／28](../../design/systems/inscription-system/rules.md)、[辅槽](../../design/systems/inscription-system/augment-system/rules.md)、[经济TL-25／33](../../design/common/run-economy/rules.md) | 保留批次身份和目标、加速收益、手牌战终清理 |
| [交互TL-17—19／36、CORE-060—064](../../design/common/interaction-save/rules.md) | 调整受理、暂停、保存、暗牌及现有桌面呈现 |
| [卡牌内容](../../design/content/cards.md)、[敌人内容](../../design/content/enemies-encounters.md)、[参数](../../design/parameters.md) | 真实输入、缺失卡池及新字段；不擅造新敌表 |
| [EX-001](../../design/examples/simple-spell.md)、[EX-002](../../design/examples/complete-battle.md)、[验收](../../design/validation.md) | 限定旧例和受影响预期；EX-002的冻结上游不改用最新 |
| [用途包](../../development/task-packs/future-purpose.md)、[打断包](../../development/task-packs/interruption-restart.md)、[场景审阅](../../development/design-review.md) | 正常故事、失败代价及采纳后的派生同步 |

流程使用[设计流程](../../../docs/design-workflow.md)、[模板索引](../../../game-design-workflow/templates/README.md)及对应五类模板、[Git规范](../../../docs/github-collaboration.md)。未读代码、未运行游戏／模拟器／玩法实验；未使用工作区其他人的未提交探索材料。不读取新探索方向，不建立第二套问题数据库。

采纳同步按需补读了受影响的系统design／experience／examples、当前来源索引及开发说明；为登记EX-003，仅检查READ-1固定文件清单和探索操作规则，不读取其他探索方向或修改其未提交内容。
