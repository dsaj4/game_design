# 游戏创意整理工作流

这个文件夹用于维护游戏策划/可行性探索阶段的核心构思。工作方式类似轻量 git：原始想法先进入隔离区，通过资格确认成为正式 GDD 素材后，才能进入 GDD、提案、评估、拟修改和核心构思。

## 文件结构

- `core-concept.md`：正式核心构思文档，只记录已经确认的精华内容。
- `idea-inbox/`：原始想法隔离区，允许模糊内容，但不得直接进入正式设计链。
- `idea-materials/`：正式想法素材库，只保存通过资格闸门的合格 GDD 素材。
- `gdd/`：按统一模板形成的核心玩法设计与设计决策文档，不记录代码规则或开发进度。
- `idea-proposals/`：已整理成可讨论提案的想法。
- `evaluations/`：对提案的可行性、可玩性、市场参照等评估。
- `draft-changes/`：拟写入 `core-concept.md` 的修改草案。
- `decision-log.md`：正式采纳、搁置、否决的决策记录。
- `market-reference.md`：同类产品、相近玩法、市场观察记录。
- `templates/`：想法、提案、评估、拟修改与 GDD 写作模板。

## GDD 写作入口

- [GDD 写作要求与模板](../../../game-design-workflow/templates/gdd-writing-requirements-and-template.md)：先按 `GDD-0 / GDD-1 / GDD-2` 选择完成度，再把已成形构思整理成可讨论、可验证和可追踪的玩法设计合同。
- [GDD 写作知识 Wiki](../shared-knowledge-snapshot/research/02-theory-digests/gdd-writing-knowledge-wiki-2026-08-18.md)：模板背后的理论、重点材料、判断框架与来源索引。
- [合格 GDD 素材模板](../../../game-design-workflow/templates/qualified-gdd-material-template.md)：通过资格闸门后，用于生成可被 GDD/Proposal 引用的正式素材。

用户提出写 GDD、玩法需求、游戏系统规则或玩法设计文档时，agent 必须主动使用模板：

1. 先确认 `GDD-0 / GDD-1 / GDD-2`。
2. 检索 `idea-materials/` 和 `idea-inbox/`。
3. 在对应章节主动提出相关内容：正式素材可供用户选择；inbox 内容必须标为未确认候选。
4. 用户希望采用 inbox 候选时，先使用 `grill-with-docs` 完成资格确认和晋级，不能直接写入 GDD。
5. 引擎、类、函数、脚本、API、编程数据结构、构建、Bug 与开发完成度不得进入 GDD；统一更新到 [`docs/code-development-index.md`](../docs/code-development-index.md) 或对应代码仓库。

## 状态流转

1. `Raw Idea / Unqualified`：保存在 `idea-inbox/`，只代表已捕获。
2. `Qualified GDD Material`：经过 `grill-with-docs`，保存在 `idea-materials/`，可被正式引用但尚未采纳。
3. `GDD / Proposal`：把合格素材组织成设计合同或可讨论玩法假设。
4. `Evaluation`：从实现可能性、可玩性、市场同类产品、风险等维度评估。
5. `Draft Change`：提出对核心文档的具体修改文本。
6. `Accepted / Parked / Rejected`：正式采纳、暂存、否决，并记录理由。

## 工作规则

- 核心文档只写“已经确认值得保留”的内容。
- 模糊想法只能进入 `idea-inbox/`，不能直接进入 `idea-materials/`、GDD、Proposal 或核心构思。
- 资格确认不等于设计采纳；正式素材仍需经过后续判断。
- 评估阶段不做详细数值设计，不展开完整系统树，只判断核心玩法是否值得继续。
- 每次正式修改 `core-concept.md` 时，都要同步更新 `decision-log.md`。
- 一个提案可以被拆分、合并、重写；保留过程比一次写对更重要。
- 市场参照只用于判断玩法空间和差异化，不直接复制竞品系统。

## 建议文件命名

- 想法：`YYYY-MM-DD-short-name.md`
- 合格素材：`M-YYYY-MM-DD-short-name.md`
- GDD：`GDD-YYYY-MM-DD-short-name.md`
- 提案：`P-YYYY-MM-DD-short-name.md`
- 评估：`E-YYYY-MM-DD-short-name.md`
- 拟修改：`D-YYYY-MM-DD-short-name.md`

示例：`P-2026-05-13-memory-maze.md`
