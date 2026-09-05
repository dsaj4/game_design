# 来源索引：课程、逐字稿、证据卡与覆盖状态

Page ID：`W-SOURCE-001`

状态：`Published / Phase 1 pilot`

版本：`0.1.1`

Owner：`游戏设计知识系统维护者`

更新时间：`2026-09-05`

Review date：`2026-10-05`

来源范围：`飞书批次 manifest / failed-items / 覆盖报告；SJ-002 / SJ-003 / SJ-004 Evidence Cards`

证据状态：`E0 覆盖事实 + E1 Source Claim + E2 Inference；当前项目转化为 Hypothesis`

变更摘要：`0.1.1 修正记录/视频口径，补齐治理元数据和可证伪项目假设。`

适用阶段：`S0-S7`

## 一句话结论

来源索引是唯一的追溯入口：先看课程记录和逐 P 覆盖，再看 Evidence Card 和主题页；`Complete` 只表示逐分集覆盖满足预期，不表示课程观点或项目设计已经被证明。

## 初学者解释

把来源索引当作“知识材料的目录卡”，而不是课程结论本身。它告诉你某门课有多少视频、哪些分集可用、哪些内容失败，以及哪张证据卡负责解释。需要核对原话时按 `Source ID -> BV -> P` 回到逐分集文件；看到 `Partial` 或 `Failed` 就停止补全，保留 `Unknown`。

## 来源总览

| Source ID | 课程 | BV | 预期记录/视频 | 预期 P | 成功 P | 失败 P | Material 状态 | Evidence Card |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `S-SJ002` | 从创意到发布：游戏设计实战全流程 | `BV1hMNu64E55` | 1/1 | 20 | 20 | 无 | `Reviewed` | [SJ-002](../evidence-cards/SJ-002.md) |
| `S-SJ003` | 游戏测试：游戏设计的核心 | `BV1ZqN365ERZ` | 1/1 | 30 | 30 | 无 | `Reviewed` | [SJ-003](../evidence-cards/SJ-003.md) |
| `S-SJ004` | 专业 GDD 写作全攻略 | `BV1pgNZ6JERH` | 1/1 | 45 | 44 | `P005` | `Partial` | [SJ-004](../evidence-cards/SJ-004.md) |
| `S-SJ009` | 你的游戏为什么不好玩？（下）构建游戏设计体系 | `BV1cagy6xEmp` | 1/1 | 77 | 74 | `P007/P033/P040` | `Partial / Repair queue` | 暂无 |

`S-SJ009` 的课程标题、BV 和 77 个分集以资料包 `manifest.json` 为准；本页只把 P007/P033/P040 的内容结论保留为 `Unknown`，不凭标题或相邻课程补写。当前飞书批次共 237 条记录、235 个唯一视频、753 个预期分集、749 个成功转写、233 个完整视频；完整性详情见 [覆盖报告](../../../../../../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/coverage-report.md)。

## 唯一事实源与路径

| 信息 | 唯一事实源 | 下游使用 |
| --- | --- | --- |
| 飞书记录、BV、分集、转写状态 | [`manifest.json`](../../../../../../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/manifest.json) | 覆盖报告、证据卡、来源索引 |
| 失败与修复尝试 | [`failed-items.md`](../../../../../../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/failed-items.md) 与修复状态 | `Failed/Unknown`、补证队列 |
| 单材料证据 | [Evidence Cards](../../../../../../../research/02-theory-digests/game-design-development-wiki/evidence-cards) | Wiki、规则候选、项目假设 |
| 批次综合 | [首批课程材料摘要与试跑](../00-sources-and-pilot.md) | 主题页和优先级 |
| 外部流程对照 | [Phase 0 外部框架对照](../../../01-theory-library/phase-0-framework-comparison.md) | 阶段基线、MDA 边界 |

下游页面不得复制 manifest 的完整记录；需要状态时引用 Source ID 和本页表格，详细字段回到唯一事实源。

## 覆盖状态解释

| 状态 | 含义 | 允许的知识加工 |
| --- | --- | --- |
| `Captured` | 已登记来源，尚未核对全部分集 | 只能写元数据和队列 |
| `Reviewed` | 预期 P 全部有可定位转写并完成证据审阅 | 可写 Source Claim、Inference 和候选 |
| `Partial` | 至少一个 P 失败、为空或定位不可靠 | 相关结论列缺口，缺失部分 `Unknown` |
| `Failed` | 当前尝试无法取得可靠材料 | 记录失败证据和下一步，不补写 |
| `Blocked` | 需要外部权限、来源替换或用户决定 | 保留阻塞原因，不标完成 |

`Complete` 是分集覆盖字段，不是知识结论状态。`Material`、`Evidence`、`Design`、`Production Stage`、`GDD` 和 `Code` 必须分别报告。

## Evidence ID 约定

课程逐 P 证据使用：`E-<SJ>-P<三位分集>-<三位序号>`，例如 `E-SJ003-P021-001`。Evidence Card 另可使用 `SC-*` 表示外部或跨材料框架，但必须在卡片中说明定位和边界。

| 层级 | 写法 | 例子 |
| --- | --- | --- |
| `E0` | 可定位的逐字稿/观察 | `E-SJ003-P021-001` |
| `E1` | 讲师明确主张或案例 | `Source Claim + E1` |
| `E2` | 多来源综合推断 | `Inference + 证据列表` |
| `E3` | 本项目原型/试玩观察 | `TEST-* + 版本` |
| `E4` | 核心文档与 Decision Log 中明确采纳的决定 | `Decision / Accepted + 决策记录链接` |

证据等级不是 `Confirmed`。课程主张不得自动成为项目决策；试玩观察也要写样本和上下文。Proposal、Evaluation 和 Draft Change 只是可追踪的决策输入，不能单独提供 `E4` 或 `Accepted`。

## 来源主张（Source Claim）

本索引本身不评价课程观点，只记录来源层的可核对主张：

- `E-SJ002-P001-001` 至 `E-SJ002-P020-001` 的定位由 [SJ-002 Evidence Card](../evidence-cards/SJ-002.md) 维护。
- `E-SJ003-P001-001` 至 `E-SJ003-P030-001` 的定位由 [SJ-003 Evidence Card](../evidence-cards/SJ-003.md) 维护。
- `E-SJ004-P001-001` 至 `E-SJ004-P045-001` 的定位由 [SJ-004 Evidence Card](../evidence-cards/SJ-004.md) 维护；其中 P005 为 `Failed / Unknown`，不产生可引用的课程主张。

若来源主张需要成为 Wiki 推断、agent 规则候选或项目假设，必须在下游页面写清适用边界和 Evidence ID；本页的覆盖记录不能代替内容审阅。

## 处理顺序

```text
manifest / 覆盖报告
  -> 逐 P 转写与缺口核对
  -> Evidence Card
  -> 单材料摘要
  -> 主题 Wiki / 规则候选
  -> 项目 Hypothesis
  -> Proposal / GDD / Evaluation / 原型
```

当前优先级：先稳固 `SJ-002`（流程）、`SJ-003`（测试）和 `SJ-004`（GDD，带 P005 缺口）的主题页；随后按主题和当前问题选择材料，不把 235 个视频无差别堆入 Wiki。

## 执行步骤

1. **登记材料元数据：** 为每门课建立唯一 `Source ID`，记录标题、BV、预期分集数、获取日期和材料状态；同一 BV 出现在不同入口时保留课程上下文，并在证据层按 `BV + P` 去重。
2. **逐分集核对覆盖：** 将 manifest 的预期 P 与逐字稿文件逐一对照，分别统计成功、失败、空文件和待复核项。合并稿只作导航，不能替代逐 P 完整性证明。
3. **抽取 Evidence Card：** 每条重要主张绑定 `Evidence ID`，写出分集定位、上下文、可信度、说话者立场和适用边界；课程练习、案例和讲师偏好要与可迁移方法主张分开。
4. **维护状态和缺口：** 材料不完整时保留 `Partial/Failed`，逐 P 列出失败原因、受影响主题和修复任务；没有证据的内容写 `Unknown`，不能从标题、邻集、课程顺序或常识补全。
5. **映射到 Wiki 和项目假设：** 来源观点写 `Source Claim`，跨材料综合写 `Inference`，当前卡牌项目转化写带最小验证的 `Hypothesis`。只有项目正式流程产生的决定才进入 `Decision/Accepted`。
6. **发布前复核：** 检查页面链接、Evidence ID、状态轴、失败清单和版本日期；发现来源修复、外部链接变化或结论冲突时，增加版本记录并保留旧判断，不静默覆盖。

## 正例与反例

### 正例：缺失分集保持可见

> `S-SJ004` 预期 45 P，成功 44 P，`P005` 失败；材料状态为 `Partial`。有关 `P005` 的 3S/3C 定义写为 `Unknown`，主题页只引用成功分集的可核对主张，并列出修复任务。

这条记录同时说明覆盖事实、证据边界和下一步，不会让读者误以为整门课已完整核验。

### 反例：用合并稿伪造完整证据

> “合并逐字稿里出现了 3S/3C，所以 P005 应该是在讲某个常见 GDD 框架；我根据上下文把它补进 Wiki。”

这混淆了材料导航和逐 P 证据，属于未经来源支持的推测。正确做法是保留 `Failed/Unknown`，修复转写或人工回看后再新增 Evidence ID。

## 失败分集与影响

| Source/Part | 当前状态 | 影响 | 处理 |
| --- | --- | --- | --- |
| `SJ-004/P005` | `Failed / Unknown` | 不能确认标题对应的 3S/3C 内容 | 保留失败记录，不从合并稿/邻集推断 |
| `SJ-009/P007` | `Failed / Unknown` | 相关主题需回避该 P 的高强度结论 | 等待重试、官方字幕或替代来源 |
| `SJ-009/P033` | `Failed / Unknown` | 同上 | 同上 |
| `SJ-009/P040` | `Failed / Unknown` | 同上 | 同上 |

重试成功后须更新 manifest、失败清单、覆盖报告、Evidence Card 和本页版本；在此之前，任何主题页都必须保留缺口说明。

## 初学者如何使用来源

1. 先在本页找到 `Source ID` 和覆盖状态。
2. 阅读对应 Evidence Card 的“一句话结论、关键主张、边界和未知”，不要直接把课程标题当结论。
3. 主题 Wiki 只使用稳定 Evidence ID；看到 `Hypothesis` 时，查看其最小验证，不要把它当正式项目规则。
4. 如果需要核对原话，按 `BV + P` 回到逐 P 文件；如果 P 失败，停止推断并记录 `Unknown`。

## 自检清单

- [ ] Source ID、BV、预期 P、成功 P、失败 P 和状态可回到 manifest。
- [ ] 多分集没有用合并稿证明完整；失败 P 明确列出。
- [ ] Evidence Card 和 Wiki 结论使用稳定 Evidence ID。
- [ ] 讲师主张、跨来源推断、项目假设和正式决策分层。
- [ ] 缺失分集未被标题、邻集或 agent 猜测补齐。
- [ ] 覆盖状态与设计状态、阶段状态、GDD 成熟度和代码状态没有混淆。

## Wiki 推断（Inference）

来源索引本身是质量控制工具：它让“已整理”可拆成可复算的覆盖、可定位的证据和明确的缺口，从而阻止合并稿存在、标题相似或单次摘要被误读为完整知识。

## 对当前项目的 Hypothesis

| Hypothesis ID | 项目转化假设 | 最小验证 | 成功信号 | 失败信号 | 不得据此推出 |
| --- | --- | --- | --- | --- | --- |
| `H-SOURCE-001` | 将每条核心卡/组合设计建议链接到 Source ID、Evidence ID、测试 ID 或已采纳决策 ID，可能降低课程经验被误写成正式规则的风险，并缩短 GDD 评审定位未知的时间。 | 在下一份 GDD 和一次原型记录中试用追踪链，由未参与整理者抽查每条关键建议的来源、证据状态和项目状态。 | 所有抽查建议都能定位到有效来源或明确 `Unknown`，且评审者能区分 Source Claim、Hypothesis 与 Accepted。 | 出现孤立结论、失败分集被补写、Proposal/Evaluation/Draft Change 被当作 Accepted，或追踪链无法定位原始范围。 | 任何被引用建议已经正确、已被项目采纳，或增加 ID 本身能提高设计质量。 |

## 未确认信息

- `SJ-009` 的课程标题、BV 和逐 P 主题需要继续以 manifest 和修复结果核对。
- 课程材料对数字卡牌、线上服务、商业数据和发布政策的覆盖不足，不能替代专项研究。
- 本页只整理来源元数据和加工路径，不代表任何课程观点已被项目采纳。

## Evidence ID 来源

- [飞书游戏设计系统课程逐字稿资料包](../../../../../../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/README.md)
- [覆盖报告](../../../../../../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/coverage-report.md)
- [首批课程材料摘要与试跑](../00-sources-and-pilot.md)
- [SJ-002 Evidence Card](../evidence-cards/SJ-002.md)
- [SJ-003 Evidence Card](../evidence-cards/SJ-003.md)
- [SJ-004 Evidence Card](../evidence-cards/SJ-004.md)
- [知识系统升级 Spec](../../../../docs/game-design-knowledge-system-spec.md)
