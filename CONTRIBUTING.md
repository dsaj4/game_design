# 贡献指南

感谢你参与这个游戏构思系统。这个仓库重视“判断过程”胜过一次性写出完美结论，因此请尽量保留想法来源、评估理由和决策记录。

## GitHub 协作底线

请先阅读 [GitHub 协作规范](docs/github-collaboration.md)。

- 不要直接在 `main` 或 `master` 上修改核心文档。
- 开始工作后先创建自己的分支，例如 `agent/codex/2026-05-25-topic` 或 `user/name/2026-05-25-topic`。
- 修改核心文档、流程文档或正式提案后，必须提交并推送。
- 如果你不会 GitHub，可以让 agent 自动完成分支、提交和推送。
- `research/raw-sources/` 中的第三方资料快照不要提交到公开仓库。

## 贡献类型

你可以贡献：

- 新游戏想法。
- 核心玩法提案。
- 提案评估。
- 同类产品分析。
- 游戏设计理论摘要。
- 可验证设计假设。
- 原型测试或纸面推演后的观察。
- 文档结构和模板改进。

## 提交新想法

1. 复制 `game-design-workflow/templates/idea-template.md`。
2. 在 `game-design-workflow/idea-inbox/` 创建新文件。
3. 文件名使用 `YYYY-MM-DD-short-name.md`。
4. 写清楚原始想法、触发来源和可能带来的玩家体验。

不要一开始就直接修改 `core-concept.md`。

## 提交提案

1. 复制 `game-design-workflow/templates/proposal-template.md`。
2. 在 `game-design-workflow/idea-proposals/` 创建新文件。
3. 文件名使用 `P-YYYY-MM-DD-short-name.md`。
4. 至少说明核心玩法假设、玩家行为、为什么可能好玩、最小可验证原型。

提案应尽量小，能被评估和验证。

## 提交评估

1. 复制 `game-design-workflow/templates/evaluation-template.md`。
2. 在 `game-design-workflow/evaluations/` 创建新文件。
3. 文件名使用 `E-YYYY-MM-DD-short-name.md`。
4. 给出快速结论、主要风险和最终建议。

评分只是辅助讨论，最终要写清楚理由。

## 修改核心构思

`game-design-workflow/core-concept.md` 是正式主干，只接收已经确认的内容。

修改前请先：

1. 确认当前在自己的工作分支，不在 `main` 或 `master`。
2. 在 `draft-changes/` 写出拟修改文本。
3. 标明来源提案和评估。
4. 确认采纳后再修改 `core-concept.md`。
5. 同步更新 `game-design-workflow/decision-log.md`。
6. 提交并推送当前分支。

## 提交研究材料

研究材料应服务于当前问题，而不是单纯收藏链接。

推荐路径：

1. 从 `research/00-index-and-roadmap/current-questions.md` 选择问题。
2. 把资料登记到 `research/01-theory-library/` 或对应案例目录。
3. 写成理论摘要、产品案例或横向比较。
4. 最后沉淀为 `research/05-design-hypotheses/` 中的设计假设。

## 文档风格

- 使用清晰、直接的中文。
- 优先写玩家行为、判断依据和验证方式。
- 避免过早展开完整数值、商业化或技术实现。
- 引用同类产品时，说明可借鉴的结构和应避免的雷同。
- 可以保留不确定性，但要明确下一步怎么验证。

## 发布前检查

提交前请确认：

- 新文档放在正确目录。
- 文件名符合当前命名规则。
- 相关来源和上下文已经写清楚。
- 如果修改了核心构思，已经同步更新决策记录。
- Markdown 链接能指向实际存在的文件。
