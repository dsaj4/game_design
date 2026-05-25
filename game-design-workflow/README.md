# 游戏创意整理工作流

这个文件夹用于维护游戏策划/可行性探索阶段的核心构思。工作方式类似轻量 git：任何想法先进入提案，再经过细化、评估、拟修改，最后才正式写入核心构思文档。

## 文件结构

- `core-concept.md`：正式核心构思文档，只记录已经确认的精华内容。
- `idea-inbox/`：零散想法入口，未经筛选。
- `idea-proposals/`：已整理成可讨论提案的想法。
- `evaluations/`：对提案的可行性、可玩性、市场参照等评估。
- `draft-changes/`：拟写入 `core-concept.md` 的修改草案。
- `decision-log.md`：正式采纳、搁置、否决的决策记录。
- `market-reference.md`：同类产品、相近玩法、市场观察记录。
- `templates/`：想法、提案、评估、拟修改模板。

## 状态流转

1. `Idea`：记录零散想法，不要求完整。
2. `Proposal`：把想法整理成一个可讨论的核心玩法假设。
3. `Evaluation`：从实现可能性、可玩性、市场同类产品、风险等维度评估。
4. `Draft Change`：提出对核心文档的具体修改文本。
5. `Accepted / Parked / Rejected`：正式采纳、暂存、否决，并记录理由。

## 工作规则

- 核心文档只写“已经确认值得保留”的内容。
- 评估阶段不做详细数值设计，不展开完整系统树，只判断核心玩法是否值得继续。
- 每次正式修改 `core-concept.md` 时，都要同步更新 `decision-log.md`。
- 一个提案可以被拆分、合并、重写；保留过程比一次写对更重要。
- 市场参照只用于判断玩法空间和差异化，不直接复制竞品系统。

## 建议文件命名

- 想法：`YYYY-MM-DD-short-name.md`
- 提案：`P-YYYY-MM-DD-short-name.md`
- 评估：`E-YYYY-MM-DD-short-name.md`
- 拟修改：`D-YYYY-MM-DD-short-name.md`

示例：`P-2026-05-13-memory-maze.md`

