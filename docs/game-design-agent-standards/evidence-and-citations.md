# 证据与引用规范

文档 ID：`AGS-EVID-001`

状态：`Proposed / Phase 4 draft`

版本：`0.1.0`

更新时间：`2026-09-04`

复审日期：`2026-10-04`

## 1. 目的

本规范要求 agent 把“从哪里知道”与“因此建议什么”分开。转写、截图、外部页面、试玩记录和正式决策可以互相引用，但不能互相冒充。证据强度描述支持范围，不代表结论一定正确。

## 2. 证据等级与结论类型

| 等级 | 典型内容 | 可支持什么 | 不能推出什么 |
| --- | --- | --- | --- |
| `E0` | 可定位的逐字稿、画面观察、原型日志 | 某来源在某位置说了什么/发生了什么 | 来源主张普遍正确 |
| `E1` | 讲师明确的方法建议、案例或规则性主张 | 记录为 `Source Claim`，作为候选方法 | 行业共识或本项目决策 |
| `E2` | 多来源方向一致的综合 | `Inference`，说明推理链和边界 | 适用于所有类型、玩家或平台 |
| `E3` | 本项目原型、试玩、回归或发布观察 | 项目范围内的 `Observed Fact`，链接版本和样本 | 一次测试证明长期或商业结果 |
| `E4` | 核心文档与 Decision Log 中明确记录的已采纳决定 | 项目 `Decision/Accepted`，链接完整决策链 | Proposal、Evaluation、Draft Change、课程或代码自动变成 Accepted |

证据等级不是项目工作流状态。一个课程主张可以是 `E1 + Source Claim`，一个试玩观察可以是 `E3 + Observed Fact`，一个已采纳设计可以同时链接 `E2/E3 + E4/Decision`。Proposal、Evaluation 和 Draft Change 只是决策链中的可追溯材料；在用户确认、核心文档和 Decision Log 完成前，它们不能提供 `E4` 或 `Accepted` 状态。

## 3. 引用最小格式

每条影响设计判断的结论至少包含：

```text
Evidence ID: E-<SOURCE>-<PART>-<NNN>
Locator: BV + P / URL + 页面锚点 / Test ID + 版本 + 时间或行号
Claim: 来源实际支持的句子
Type: Observed Fact / Source Claim / Inference / Hypothesis / Decision / Unknown
Scope: 适用对象、阶段、玩家和平台
Confidence: High / Medium / Low
Limit: 不能据此推出什么
```

没有稳定定位时写 `Unknown`，并记录补证责任人。不要用合并逐字稿、文件存在或标题相似替代逐分集定位。

## 4. 规则条目

### ADRULE-EVIDENCE-001：重要结论必须可追溯

Strength：`SHOULD`

Status：`Proposed`

Trigger：写入 Wiki、材料摘要、规则候选、Proposal、GDD 或阶段报告中的事实性/规范性结论。

Preconditions：已有来源或已明确记录当前没有来源。

Input：待写结论、原始来源/观察、稳定定位信息和项目适用范围。

MUST：为结论添加 Evidence ID、定位、类型、范围和限制；项目假设同时写验证方式。

MUST NOT：把没有定位的讲师观点、个人体感、代码存在或单条评论写成 `Confirmed`。

Procedure：`定位来源 -> 选择结论类型 -> 标记适用边界 -> 写限制 -> 链接下游文档`。

Output：带引用的结论表、材料摘要或未知项记录。

Pass criteria：审阅者能在合理时间内从结论回到具体来源或明确的未知记录。

Failure handling：来源不可定位或转写覆盖不完整时标 `Unknown/Partial`，降低结论强度并进入补证队列。

Evidence：知识系统 Spec 第 3、4、8 节；Evidence Cards `SJ-002/SJ-003/SJ-004`。

Owner/version/review date：研究维护者 / `0.1.0` / `2026-10-04`。

Review trigger：引用格式、资料包结构或证据状态轴变化。

### ADRULE-EVIDENCE-002：缺失分集不得补写

Strength：`SHOULD`

Status：`Proposed`

Trigger：来源是多分集视频，且某一 P 失败、为空、覆盖状态为 `Partial` 或定位不可靠。

Preconditions：能读取分集清单、预期 P 数和每个 P 的状态；来源接口不可用时保持上一份可追溯快照并标日期。

Input：来源清单、`manifest.json`、逐分集文件、失败清单和当前覆盖快照日期。

MUST：引用前检查 `manifest.json` 的预期/成功/失败字段；把缺失 P 保持为 `Failed / Unknown`，在摘要和来源索引中列出。

MUST NOT：用合并稿、标题、邻集、搜索摘要或 agent 推测填补缺失内容；不得把 `successful_parts < expected_parts` 的视频标为完整。

Procedure：`读取 manifest/分集清单 -> 比对 expected/completed/failed -> 验证非空文件与定位 -> 标记缺口 -> 只发布可定位证据`。

Output：覆盖表、失败清单链接和受影响主题的 `Unknown` 说明。

Pass criteria：预期 P 数、成功 P 数和失败 P 数可复算，所有高强度结论避开缺失定位。

Failure handling：重试仍失败则保留失败证据，报告受影响结论和下一次可用来源；不因交付压力降级边界。

Evidence：`feishu-game-design-system-transcripts-2026-08-30/manifest.json`、`coverage-report.md`；`SJ-004 P005` 等失败记录。

Owner/version/review date：资料维护者 / `0.1.0` / `2026-10-04`。

Review trigger：分集修复、来源替换或新的官方字幕可用。

### ADRULE-EVIDENCE-003：冲突和替代解释显式化

Strength：`SHOULD`

Status：`Proposed`

Trigger：不同来源、不同玩家群体或同一测试的结果不一致。

Preconditions：至少保留两条相互冲突的原始主张/观察及其来源、版本或样本上下文。

Input：冲突主张/观察、各自证据等级、来源定位、版本和样本上下文。

MUST：并列记录冲突主张、证据等级、样本/上下文差异、至少一个替代解释和需要什么新证据。

MUST NOT：选择最符合当前偏好的结果并删除其他证据，或把相关性写成因果性。

Procedure：`并列主张 -> 比较来源/样本/版本 -> 标证据等级 -> 列替代解释 -> 设计区分性补证 -> 更新结论状态`。

Output：冲突表、待验证假设和阶段门影响。

Pass criteria：读者能说明当前暂不确定的具体是哪一部分，以及下一次如何区分解释。

Failure handling：无法区分时标 `Unknown`；阶段门尚未决定时记录 `Decision state: Pending`、`Gate: N/A` 和 `Pending reason`，作出决定时只能在 `Iterate/Park` 中选择，不能默认 `Go`。

Evidence：`E-SJ003-P009-001`、`E-SJ003-P010-001`、`E-SJ003-P021-001`；知识系统 Spec 第 8、14 节。

Owner/version/review date：研究/测试负责人 / `0.1.0` / `2026-10-04`。

Review trigger：出现新样本、版本回归或来源覆盖变化。

## 5. 写作与审查示例

**合格：**“在 `E-SJ003-P021-001` 中，讲师主张小规则改动可能改变行动顺序。本项目把它转为 `H-SJ003-002`：改变核心卡费用后比较选择率和回合长度；尚无项目数据，状态为 `Hypothesis`。”

**不合格：**“行业证明费用调整一定会破坏平衡，所以核心卡费用必须固定。”这同时越过了来源范围、项目验证和正式决策三道边界。

## 6. 当前项目提醒

唯一核心卡项目的卡牌效果、费用、组合时机和共享世界收益都应区分：课程/竞品是 `Source Claim` 或 `Inference`，对局观察是 `Observed Fact`，设计判断是 `Hypothesis`；只有核心文档与 Decision Log 同时明确记录已采纳决定后，才可写 `E4 + Decision/Accepted`。
