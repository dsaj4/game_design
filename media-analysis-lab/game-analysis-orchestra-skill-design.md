# game-analysis-orchestra Skill 设计稿

状态：Skill Design / Phase 1

本文档从 PaperOrchestra 与 AutoSurvey 中提取可迁移设计，定义一个面向 Codex 的 `game-analysis-orchestra` skill。第一阶段目标只覆盖：

```text
素材包 -> 大纲 -> 分模块拆解稿
```

暂不覆盖真实视频接入、联网调研、多模型评审、迭代重写和 BiliSum 集成。

## 参考项目

### PaperOrchestra

- 论文：[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://arxiv.org/abs/2604.05018)
- 官方仓库：[google-research/paper-orchestra](https://github.com/google-research/paper-orchestra)
- 社区 skill-pack：[Ar9av/PaperOrchestra](https://github.com/Ar9av/PaperOrchestra)

可迁移要点：

- 把非结构化 pre-writing materials 转成正式长文。
- 用专门阶段处理 Outline、Literature Review、Section Writing、Plotting、Content Refinement。
- 先生成结构化 outline，再分章节写作，避免一个大 prompt 直接产出全文。
- 把图示当作一级产物，而不是装饰。
- 用 deterministic helpers 做 schema、覆盖率、引用、格式检查。
- 社区 skill-pack 版本证明：复杂写作流水线可以先做成 skill + references + scripts，而不必先做完整产品。

### AutoSurvey

- 论文：[AutoSurvey: Large Language Models Can Automatically Write Surveys](https://arxiv.org/abs/2406.10252)
- 仓库：[AutoSurveys/AutoSurvey](https://github.com/AutoSurveys/AutoSurvey)

可迁移要点：

- 面向综合性 survey，而不是单篇短摘要。
- 使用“初始检索与 outline 生成 -> subsection drafting -> integration and refinement -> evaluation and iteration”的系统化方法。
- 把长文长度、章节数量、每节长度、参考材料数量做成显式参数。
- 先用大量候选资料支撑 outline，再让每个小节围绕局部材料写作。
- 评估不是附属步骤，而是判断生成结果是否可用的必要环节。

## 为什么做成 skill

`game-analysis-orchestra` 的核心价值是流程知识，而不是独立运行时：

- 它需要 Codex 阅读素材、判断证据、组织大纲、撰写长文。
- 它依赖模板、schema、rubric 和少量确定性脚本。
- 它未来可以被 BiliSum 调用，但现在不应绑定 BiliSum 的 UI、任务库、模型配置和截图策略。

因此第一阶段适合做成 Codex skill：

```text
用户请求
  -> 触发 game-analysis-orchestra
  -> 读取素材包
  -> 产出 outline
  -> 按模块写拆解稿
```

## Skill 定位

建议名称：

```text
game-analysis-orchestra
```

建议触发语义：

- 用图片和文本素材生成游戏拆解稿。
- 把 BiliSum 图文笔记 / 视频转写整理成游戏分析。
- 为某款游戏生成拆解大纲。
- 按八模块写游戏策划拆解案。
- 把素材包转成游戏玩法、系统、经济、内容、叙事分析。

第一阶段不处理：

- 自动下载视频。
- 自动抽帧。
- 自动 ASR。
- 联网补商业数据。
- 多模型 peer review。
- 自动写入 `research/03-product-case-studies/`。
- 修改 `core-concept.md`。

## 推荐 Skill 目录结构

```text
game-analysis-orchestra/
  SKILL.md
  references/
    workflow.md
    material-pack.md
    outline-standard.md
    module-writing.md
    source-inspirations.md
  scripts/
    validate_material_pack.py
    scaffold_outline.py
    scaffold_dossier.py
    check_phase1_outputs.py
  assets/
    materialpack.schema.json
    outline-template.md
    dossier-template.md
```

### SKILL.md

只放最短可执行说明：

- 何时使用。
- 第一阶段流程。
- 需要读取哪些 reference。
- 运行哪些脚本。
- 输出哪些文件。

不要在 `SKILL.md` 里放完整八模块解释，避免 context 过重。

### references/workflow.md

描述从 PaperOrchestra / AutoSurvey 抽象出的阶段式流程：

```text
1. Validate material pack
2. Build evidence map
3. Generate analysis outline
4. Write module drafts
5. Integrate dossier
6. Run phase-1 checks
```

第一阶段只执行前 5 步加轻量检查，不执行外部调研和重写循环。

### references/material-pack.md

定义素材包字段和使用原则：

- `project`：游戏名、slug、范围、目标问题。
- `text_sources`：文本材料、转写、图文笔记、人工观察。
- `images`：截图、关键帧、画面观察、证据标签。
- `analysis_constraints`：是否完整八模块、是否允许推断、是否需要项目转化。
- `draft_seed`：可选人工结构化笔记。

关键规则：

- 素材包是事实入口，不是最终结论。
- 所有关键判断要能回指到文本、图片或明确的推断。
- 未确认信息必须单列。

### references/outline-standard.md

定义大纲生成标准。借鉴 PaperOrchestra 的 Outline Agent，但改成游戏拆解语境。

输出建议为 `outline.json` 和 `outline.md` 两份：

```json
{
  "game_name": "...",
  "scope": "...",
  "target_questions": [],
  "thesis": "...",
  "modules": [
    {
      "id": "module-3",
      "title": "核心玩法循环",
      "claim": "...",
      "evidence": ["text:materials.md#L10", "image:battle-layout"],
      "open_questions": [],
      "write_priority": "high"
    }
  ],
  "diagrams": [
    {
      "type": "core_loop",
      "module": "module-3",
      "purpose": "解释玩家输入、行动、产出、消耗、反馈和回流"
    }
  ]
}
```

大纲必须先回答：

- 本次拆解要证明什么。
- 哪些模块有材料支撑。
- 哪些模块只能保守写。
- 哪些图示必须生成。

### references/module-writing.md

定义分模块写作规则。借鉴 AutoSurvey 的 subsection drafting：

- 每个模块只读取与自己相关的 evidence。
- 每个模块先写核心结论，再写证据。
- 每个模块都要写“对本项目的启示”。
- 没有证据时写“材料不足”，不能硬编。
- 模块 3 和模块 4 优先级最高，因为它们决定是否像游戏拆解而不是普通介绍。

第一阶段模块映射：

| 模块 | 写作重点 | Phase 1 要求 |
| --- | --- | --- |
| 1. 定位与基础信息 | 游戏是什么、拆解范围是什么 | 可保守，不编商业数据 |
| 2. 玩家体验 | 玩家进入、游玩、反馈链路 | 必须来自文本或截图观察 |
| 3. 核心循环 | 输入、行动、产出、消耗、反馈、回流 | 必须有流程图 |
| 4. 系统架构 | 系统如何联动 | 必须有系统关系图 |
| 5. 内容关卡 | 内容如何填充时间 | 材料不足可简写 |
| 6. 数值经济 | 资源、费用、成长、消耗 | 只写材料中可见部分 |
| 7. 叙事包装 | 角色、世界观、视觉、音频 | 没有证据则保守 |
| 8. 优劣与方案 | 亮点、短板、改进 | 必须落到玩家行为和系统位置 |

### references/source-inspirations.md

记录借鉴来源，不在执行时默认全文加载。内容包括：

- PaperOrchestra 阶段与 game-analysis-orchestra 阶段对照。
- AutoSurvey 阶段与 game-analysis-orchestra 阶段对照。
- 哪些能力第一阶段暂不迁移。
- 后续 Phase 2/3 的扩展建议。

### scripts/validate_material_pack.py

确定性检查：

- JSON 可读。
- 必填字段存在。
- 文本文件存在。
- 图片文件存在。
- 至少 1 个目标问题。
- 至少 1 个文本或图片证据。

### scripts/scaffold_outline.py

生成大纲骨架，不替代 LLM 判断。

输入：

```text
materialpack.json
```

输出：

```text
workspace/outline/outline.md
workspace/outline/outline.json
```

作用：

- 把八模块先铺开。
- 把素材证据按标签分配到候选模块。
- 标记缺材料模块。

### scripts/scaffold_dossier.py

根据 outline 生成拆解稿骨架。

输入：

```text
outline.json
materialpack.json
```

输出：

```text
workspace/drafts/<slug>-dossier.md
```

作用：

- 固定八模块顺序。
- 插入 evidence map。
- 插入核心循环图和系统关系图占位。
- 留出每个模块的写作槽位。

### scripts/check_phase1_outputs.py

轻量质量检查：

- 是否有大纲。
- 是否有拆解稿。
- 是否包含八模块。
- 是否包含证据地图。
- 是否包含核心循环图。
- 是否包含系统关系图。
- 是否包含项目转化。
- 是否列出未确认信息。

## Phase 1 工作流

### Step 1：读取与检查素材包

输入：

```text
materialpack.json
```

Codex 应先运行：

```powershell
py -3 game-analysis-orchestra/scripts/validate_material_pack.py --pack <materialpack.json>
```

如果失败，先修素材包或向用户报告缺口。

### Step 2：建立证据地图

Codex 读取素材包和相关文本材料，整理：

```text
证据 ID -> 类型 -> 观察点 -> 支撑模块 -> 可信度
```

这里借鉴 AutoSurvey 的 retrieval 思路，但第一阶段不联网；“检索库”就是素材包里的文本与图片。

### Step 3：生成拆解大纲

Codex 先运行 scaffold，再基于证据补全大纲：

```powershell
py -3 game-analysis-orchestra/scripts/scaffold_outline.py --pack <materialpack.json> --out <workspace>
```

大纲必须包括：

- 总论点。
- 八模块每模块的核心 claim。
- 每模块证据列表。
- 图示计划。
- 未确认问题。
- 写作优先级。

这是从 PaperOrchestra Outline Agent 迁移来的关键步骤。

### Step 4：分模块写作

Codex 按模块顺序写作，但写作策略不是平均用力：

1. 先写模块 3 核心循环。
2. 再写模块 4 系统架构。
3. 再写模块 2 玩家体验。
4. 再补模块 1、5、6、7、8。

原因：游戏拆解案的质量首先取决于是否还原了玩家循环和系统联动。

这是从 AutoSurvey subsection drafting 迁移来的关键步骤：每个模块围绕局部材料写，最后再整合。

### Step 5：整合拆解稿

Codex 运行：

```powershell
py -3 game-analysis-orchestra/scripts/scaffold_dossier.py --outline <outline.json> --pack <materialpack.json> --out <workspace>
```

然后把模块正文写入统一 Markdown。

输出文件：

```text
workspace/drafts/<slug>-dossier.md
```

### Step 6：Phase 1 检查

Codex 运行：

```powershell
py -3 game-analysis-orchestra/scripts/check_phase1_outputs.py --workspace <workspace>
```

检查通过后，本阶段完成。

## 输出目录约定

一次运行建议生成：

```text
workspace/
  inputs/
    materialpack.json
  outline/
    outline.md
    outline.json
  drafts/
    <slug>-dossier.md
  checks/
    phase1-check.md
```

如果在本仓库 `media-analysis-lab` 内试跑，可使用：

```text
media-analysis-lab/runs/<slug>/
```

## 与当前 media-analysis-lab 的关系

当前 `media-analysis-lab` 已经有：

- 素材包 schema。
- 拆解稿模板。
- 生成任务包与初稿脚本。
- 示例素材与质量检查。

`game-analysis-orchestra` skill 应从中抽取，而不是复制所有说明文档：

| 当前文件 | 迁移方式 |
| --- | --- |
| `schemas/material-pack.schema.json` | 放入 skill `assets/` |
| `templates/game-analysis-dossier-template.md` | 放入 skill `assets/` |
| `prompts/game-analysis-dossier.md` | 拆成 `references/module-writing.md` |
| `tools/build_analysis_packet.py` | 拆成 validate / scaffold_outline / scaffold_dossier / check 四个脚本 |
| `acceptance.md` | 拆成 `references/workflow.md` 和检查脚本 |
| `architecture.md` | 精简为 `references/source-inspirations.md` |

## 第一阶段验收

Skill 第一阶段完成后，用一个示例素材包验证：

```text
输入：materialpack.json + 1 个文本材料 + 1 张图片
输出：outline.md + outline.json + dossier.md + phase1-check.md
```

验收标准：

- 大纲包含八模块。
- 大纲区分有证据模块和材料不足模块。
- 拆解稿包含八模块。
- 模块 3 有核心循环图。
- 模块 4 有系统关系图。
- 每个关键结论至少能回指一个证据或标明为推断。
- 包含“对本项目的转化”。
- 包含“未确认信息”。

## 后续阶段预留

Phase 2：加入评审与迭代。

```text
dossier.md -> review.md -> revision-plan.md -> dossier-v2.md
```

借鉴 PaperOrchestra Content Refinement 与 AutoSurvey evaluation。

Phase 3：加入 BiliSum 适配器。

```text
BiliSum visual-note.md + transcript.md + screenshots/
  -> materialpack.json
```

Phase 4：加入外部资料补强。

```text
素材包 -> 同类产品/官方资料/玩家反馈检索 -> 引用证据 -> 拆解稿
```

这一阶段才迁移 PaperOrchestra Literature Review 与 AutoSurvey retrieval 的完整能力。

## 设计决策

1. 第一阶段只做素材内分析，不联网。
2. 第一阶段只做大纲与分模块写作，不做多模型评审。
3. 保留八模块，但允许材料不足模块保守简写。
4. 模块 3、模块 4 权重最高。
5. 图示是必要输出，不是可选装饰。
6. Skill 先项目本地验证，稳定后再考虑全局安装。
