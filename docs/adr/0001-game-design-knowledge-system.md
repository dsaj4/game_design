# ADR-0001: 采用分层游戏设计知识加工系统

## Status

Proposed

## Context

飞书“游戏设计系统课程”已经整理为 BiliSum 逐字稿资料包，但原始转写、课程观点、项目设计判断和 agent 行为约束的职责不同。资料包还包含多分集视频，单个合并文本文件不能证明所有分集都已完成；当前有 `753` 个预期分集、`749` 个成功分集，`SJ-004 P005` 与 `SJ-009 P007/P033/P040` 仍缺失。

仓库已经有：

- `research/` 的理论来源、摘要、假设和原型观察流程。
- `game-design-workflow/` 的双层想法库、GDD-0/1/2 模板、提案、评估和核心构思保护流程。
- `docs/code-development-index.md` 的代码与设计边界。
- `game-analysis-orchestra` 的产品拆解 Phase 1 流程。

如果直接把课程总结写进 GDD 或 `AGENTS.md`，会产生无来源结论、阶段状态混用、重复模板和核心文档越权修改风险。

## Decision

采用以下分层架构，并以 [游戏设计知识与构思辅助系统升级 Spec](../game-design-knowledge-system-spec.md) 作为跨目录的方案入口：

1. 原始逐字稿继续保留为 `Research Input / Transcript Archive`。
2. 所有课程分析先经过逐 P 完整性校验，再生成带 `BV + P + 时间戳/行号` 的证据卡和单材料摘要。
3. 单材料摘要经过交叉综合后，分别输出：
   - 面向初学者的生命周期 Wiki；
   - 面向 agent 的 `HARD / SHOULD / EXPERIMENT` 规则候选。
4. Wiki、agent 规范、GDD 成熟度、设计工作流状态、生产阶段和代码状态分别维护，不能互相代替。
5. Agent 规范先在规则草案中评审，之后再分批增量集成到 `AGENTS.md`、现有 GDD 模板、`docs/control-center.md` 或技能 references；不复制同一规则形成多个权威版本。
6. 课程内容对当前项目的影响默认写成 `Hypothesis`，继续通过 `Proposal -> Evaluation -> Draft Change -> Accepted` 流程，不能直接改 `core-concept.md`。

## Consequences

### Positive

- 课程原文、证据、Wiki 教学和 agent 约束可以分别维护并互相追踪。
- 多分集缺失会在输入阶段暴露，不能因为存在 P1 或合并稿而误报完成。
- 同一套 S0-S7 阶段、证据等级和验收标准可同时服务人类学习和 agent 执行。
- 保留未知、冲突、失败和历史版本，降低后续复盘时的误读风险。
- 现有 GDD、想法资格闸门和代码开发边界可以增量复用。

### Negative

- 首轮整理需要维护证据卡、状态轴和来源索引，工作量高于直接写一篇总结。
- Wiki 和 agent 规范需要不同写法，不能简单复制同一段正文。
- 课程观点只有在多来源或项目测试支持后才能升级，短期内会保留较多 `Hypothesis` 和 `Unknown`。

### Neutral

- 新 Wiki 需要与已有 `gdd-writing-knowledge-wiki-2026-08-18.md` 建立复用和去重关系。
- 规则长期维护需要 owner、版本、复审日期和废弃记录。

## Alternatives Considered

### 直接把课程整理成一篇长 Wiki

不采用：容易按课程目录堆资料，无法为 agent 提供可判定规则，也难以显示缺失分集和证据边界。

### 直接把课程观点写入 `AGENTS.md` 或 GDD 模板

不采用：会把来源观点误当仓库政策，绕过审阅和版本迁移，并增加与现有 GDD/核心流程冲突的风险。

### 只保留摘要，不建立证据卡

不采用：无法定位具体分集和时间位置，难以处理转写错误、重复 BV 和课程观点冲突。

### 为新知识系统创建一套全新的 GDD 模板

不采用：现有模板已经覆盖 GDD-0/1/2、素材审查、规则/体验验收和代码边界；新系统只应提出增量改进。

## References

- [游戏设计知识与构思辅助系统升级 Spec](../game-design-knowledge-system-spec.md)
- [飞书游戏设计系统课程逐字稿资料包](../../research/01-theory-library/feishu-game-design-system-transcripts-2026-08-30/README.md)
- [GDD 写作要求与模板](../../game-design-workflow/templates/gdd-writing-requirements-and-template.md)
- [GDD 写作知识 Wiki](../../research/02-theory-digests/gdd-writing-knowledge-wiki-2026-08-18.md)
- [GitHub 协作规范](../github-collaboration.md)
