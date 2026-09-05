# 游戏设计与开发 Wiki

> 跨游戏共享方法库。2026-09-05 已移除历史游戏的专属假设、原型与设定示例。项目转化只写入所选工作区；通用卡牌或桌游教学不规定新游戏类型。入口见[共享知识](../../../docs/shared-knowledge.md)。

Page ID：`W-README-001`

状态：`Published / Phase 1 pilot`

版本：`0.1.2`

Owner：`游戏设计知识系统维护者`

更新时间：`2026-09-05`

Review date：`2026-10-05`

来源范围：`SJ-002 / SJ-003 / SJ-004 Evidence Cards；Phase 0 外部框架对照；知识系统升级 Spec；逐字稿覆盖报告`

证据状态：`E0/E1 Source Claim + E2 Inference；无新增项目 Decision/Accepted`

变更摘要：`0.1.2 移除历史游戏专属转化与示例，保留通用方法和课程证据。`

适用阶段：`S0-S7`

## 这套 Wiki 解决什么问题？

它把“我想做一个游戏”拆成一条可执行的学习和开发路径：先理解玩家问题，再形成概念，做最小原型，逐步扩大制作范围，最后准备发布和复盘。

Wiki 给初学者看的内容与课程逐字稿、证据卡和 agent 规则分开维护：

```text
逐字稿 -> Evidence Card -> 材料摘要 -> Wiki 解释
                                  -> Agent 规则候选
                                  -> 独立工作区中的 Hypothesis
```

课程观点默认是 `Source Claim`，跨来源的总结是 `Inference`，具体项目转化应在独立工作区标为 `Hypothesis`。只有项目决策记录明确采纳的内容才是 `Decision/Accepted`。

## 最短学习路径

1. 先读 [术语、状态与使用方法](00-glossary-and-how-to-use.md)，理解 `Unknown`、`Hypothesis` 和阶段门。
2. 再读 [S0-S7 生命周期总览](01-process/overview.md)，知道当前问题属于哪个阶段。
3. 从 [S0 研究与 S1 概念](01-process/s0-research-and-concept.md) 开始，把灵感写成可检验的概念。
4. 读 [S2 原型与试玩](01-process/s2-prototype-and-playtest.md)，学会一次只验证一个主要未知。
5. 原型值得扩大后，读 [S3-S7：从垂直切片到发布后复盘](01-process/s3-to-s7-production-and-release.md)，区分代表性体验、稳定生产、功能完整、发布候选和发布后学习。
6. 需要系统设计时，读 [体验与 MDA](02-player-and-design/player-experience-and-mda.md) 和 [卡牌、组合与平衡](03-systems-and-rules/cards-combos-and-balance.md)。
7. 需要写文档或推进制作时，读 [文档、范围与阶段门](04-production-and-quality/documentation-scope-and-gates.md)。
8. 最后用 [试玩与证据](04-production-and-quality/playtesting-and-evidence.md) 记录实际观察，再回到对应阶段门。

## 页面目录

| 页面 ID | 页面 | 适用阶段 | 状态 | 目的 |
| --- | --- | --- | --- | --- |
| `W-README-001` | 本页 | S0-S7 | `Published / Phase 1 pilot` | 入口、边界和阅读路径 |
| `W-TERM-001` | [术语、状态与使用方法](00-glossary-and-how-to-use.md) | S0-S7 | `Published / Phase 1 pilot` | 不混淆材料、证据、设计和代码状态 |
| `W-PROC-001` | [S0-S7 生命周期总览](01-process/overview.md) | S0-S7 | `Published / Proposed baseline` | 阶段目标、产出和 Go/Iterate/Park/Stop |
| `W-PROC-002` | [S0 研究与 S1 概念](01-process/s0-research-and-concept.md) | S0-S1 | `Published / Phase 1` | 从问题到可复述概念 |
| `W-PROC-003` | [S2 原型与试玩](01-process/s2-prototype-and-playtest.md) | S2 | `Published / Phase 1` | 设计最小验证并观察玩家行为 |
| `W-PROC-004` | [S3-S7：从垂直切片到发布后复盘](01-process/s3-to-s7-production-and-release.md) | S3-S7 | `Published / Proposed baseline` | 区分代表性质量、稳定生产、质量收敛、发布与复盘 |
| `W-EXP-001` | [玩家体验与 MDA](02-player-and-design/player-experience-and-mda.md) | S0-S4 | `Published / Phase 1 pilot` | 把机制、行为和体验连起来 |
| `W-CARD-001` | [卡牌、组合与平衡](03-systems-and-rules/cards-combos-and-balance.md) | S1-S5 | `Published / Phase 1 pilot` | 记录卡牌规则、时序、代价和回归 |
| `W-DOC-001` | [文档、范围与阶段门](04-production-and-quality/documentation-scope-and-gates.md) | S1-S7 | `Published / Phase 1 pilot` | 选择 GDD 深度，控制范围和交接 |
| `W-TEST-001` | [试玩与证据](04-production-and-quality/playtesting-and-evidence.md) | S2-S7 | `Published / Phase 1 pilot` | 把反馈转成可追踪的设计证据 |
| `W-SOURCE-001` | [来源索引](05-sources/source-index.md) | S0-S7 | `Published / Phase 1 pilot` | 追溯课程、外部来源和缺失分集 |

## 每页如何阅读

每页固定回答九个问题：

1. 这页的结论是什么？
2. 初学者需要先理解什么？
3. 它降低哪一种风险？
4. 按什么步骤执行？
5. 什么是正例，什么是反例？
6. 如何自行检查完成？
7. 哪些内容来自来源，哪些是本 Wiki 的推断？
8. 方法适用于哪些情境，哪些结论需要项目独立验证？
9. 还有哪些 `Unknown` 和下一步？

## 本 Wiki 不做什么

- 不把 235 个视频的标题或合并稿当作完整课程证据；缺失的 `SJ-004 P005`、`SJ-009 P007/P033/P040` 在取得可靠转写、官方字幕或人工核验前保持 `Failed/Unknown`，不能补写。
- 不把讲师经验、竞品做法或 MDA 分析直接写成当前项目 `Accepted` 规则。
- 不替代 `game-design-workflow/` 的想法资格闸门、Proposal、Evaluation、Draft Change 和 Decision Log。
- 不记录类、函数、API、构建命令或代码完成度；这些内容留在 [代码开发进度索引](../../../docs/code-development-index.md)。

## 来源与版本

### 来源主张（Source Claim）

- [首批课程材料摘要与试跑](00-sources-and-pilot.md)
- [Phase 0 外部框架对照](../../01-theory-library/phase-0-framework-comparison.md)
- [逐字稿覆盖报告](../../01-theory-library/feishu-game-design-system-transcripts-2026-08-30/coverage-report.md)
- [来源索引](05-sources/source-index.md)
- [知识系统升级 Spec](../../../docs/game-design-knowledge-system-spec.md)

这些来源分别提供课程观点、外部框架、覆盖事实和治理要求；它们不直接证明 S0-S7 或当前项目示例已经成立。

### Wiki 推断（Inference）

本 Wiki 将上述来源组织成同一条学习路径，并用 S0-S7 连接知识页；该结构仍是 `Proposed baseline`，需要通过实际设计任务和阶段回顾检验。

### 版本记录

- `0.1.0`：建立首批入口、页面导航和 Phase 1 pilot 主题页。
- `0.1.1`：补入 `W-PROC-004`、统一 `W-PROC-001` 状态，并把失败分集边界改为“取得可靠证据前”。
