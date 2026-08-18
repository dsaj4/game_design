# 正式想法素材库

本目录只保存 `Qualified GDD Material`（合格 GDD 素材）。这里的内容可以被 GDD 或 Proposal 正式引用，但仍不等于已经采纳的核心设定。

## 与 idea-inbox 的区别

| 目录 | 内容状态 | 可以模糊吗 | 可直接写入 GDD/Proposal 吗 |
| --- | --- | --- | --- |
| `idea-inbox/` | `Raw Idea / Unqualified` | 可以 | 不可以 |
| `idea-materials/` | `Qualified GDD Material` | 不可以 | 可以作为候选引用 |

`idea-inbox/` 是隔离区，负责不丢灵感；本目录是正式素材库，负责不让模糊内容污染设计判断。

## 晋级门槛

agent 必须使用 [`grill-with-docs`](C:/Users/Administrator/.codex/skills/grill-with-docs/SKILL.md) 逐项澄清。问题能通过仓库文档回答时先查文档；不能回答时一次只问用户一个问题，并给出推荐答案。

只有以下项目全部清楚，才能晋级：

- 可追溯的原始表达和触发来源。
- 明确的设计对象或目标 GDD 章节。
- 玩家处境，或该素材在设计中的明确功能。
- 玩家会做什么、看到什么或受到什么影响。
- 希望产生的反馈、体验或设计价值。
- 与当前核心构思、现有系统和相关素材的关系。
- 主要未知项、风险和下一步验证/决策方式。

不要求在此阶段完成详细数值、全部边界或制作规格；这些属于 GDD-1/GDD-2 或 Proposal/Evaluation 的工作。

## 晋级操作

1. 保留 `idea-inbox/` 原文件，不删除、不覆盖原始表达。
2. 复制 `game-design-workflow/templates/qualified-gdd-material-template.md`。
3. 创建 `M-YYYY-MM-DD-short-name.md`。
4. 链接来源 inbox 文件和资格确认结论。
5. 标记为 `Qualified GDD Material`，并写明仍属于 `Hypothesis` 或 `Unknown` 的部分。

现有 inbox 内容不会自动晋级；只有实际需要时才逐份复审。

## 在 GDD 写作中的使用

agent 开始或续写 GDD 时必须：

1. 检索本目录中与当前章节相关的素材，并主动向用户提出纳入、排除或暂缓选项。
2. 同时检索相关 inbox 内容，但单独标成“未确认候选”。
3. 未确认候选必须先通过资格闸门并进入本目录，之后才能写入 GDD 正文。
4. 在素材文件中回填它被哪个 GDD、版本和章节使用。
