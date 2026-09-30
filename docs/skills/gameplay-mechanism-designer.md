# 玩法机制设计器：项目安装与推荐用法

日期：2026-09-30。状态：Installed / Project-local；适配修订 game-project-1。这是机制构思工具的安装与流程适配，不是玩法采纳或测试结论。

已安装到 [项目 skill](../../.codex/skills/gameplay-mechanism-designer/SKILL.md)，固定使用[用户指定的上游版本](https://github.com/qiuaoru-coder/game-design-agent-skills/tree/29e8c759ca26c6bd4f337744b647dc728bf322b6/gameplay-mechanism-designer)，提交 `29e8c759ca26c6bd4f337744b647dc728bf322b6`。在本项目下一轮对话中可用 `$gameplay-mechanism-designer` 调用；没有安装全局副本。

## 它适合承担什么

把一个种子展开为玩家会做什么、什么状态发生变化、如何连成机制链、如何形成循环、系统之间传递什么，以及如何用最小验证判断是否值得继续。内置方法包括 10 类状态域、25 个机制元素、7 个落点、283 条机制链、13 类循环和18类系统关系；它们提供构思语言，不是好玩的证明。

推荐顺序：**Spark → 选一个候选 → Loop Builder / System Network → grill-with-docs 资格确认 → 必要时正式 GDD 或 Proposal → Prototype Pack 验证计划**。简单任务可以停在 Spark；不要求把所有模式跑一遍。

| 需要 | 推荐模式 | 产物 |
| --- | --- | --- |
| 一条灵感，想找几个真正不同的玩法 | Spark | 三个候选及取舍、一个推荐 |
| 同一机制还能放在哪里、换哪一环 | Placement Variants / Mechanism Variants | 玩家决策发生变化的变体 |
| 动作有了，但玩一轮之后怎么办 | Loop Builder | 下一轮继承什么、如何重置/退出 |
| 两个系统看似有关，实际没有相互影响 | System Network | 有载体和后果的系统关系 |
| 检查已有方案的断点 | Audit | 按已读范围列问题、缺失与修订建议 |
| 想验证一个明确假设 | Prototype Pack | 最小设计验证计划，默认未执行 |
| 已有较完整思路，想组织整体方案 | Full Design | 构思草案；正式文档另走资格与模板流程 |

## 直接复制使用

### 1. 推荐起步：核心设计 + 三个候选

```text
使用 $gameplay-mechanism-designer，启动言咒新探索：〈主题〉。
阅读模式 CORE，只读核心设计，不自动扩读。
种子：〈我的想法〉。用 Spark 给三个结构不同的候选，比较玩家决策、反馈、代价和最大未知，推荐一个。
三个候选先放同一个方向 README，记录实际阅读版本；保持 Raw，不回写主系统。
```

适合早期发散。无需完整 GDD，不预建流程目录。若上一轮已经读过大量背景，严格控制输入时由你新开一个项目对话再使用此话术；同一对话无法真正清除已读内容。

### 2. 只研究一个系统

```text
使用 $gameplay-mechanism-designer，启动言咒新探索：〈主题〉。
阅读模式 CUSTOM，只读 yanzhou/design/core-design.md 和 yanzhou/design/systems/04-elements-environment.md。
用 Mechanism Variants 对〈指定机制〉提出三个变体，保留〈约束〉。
不要读其他系统、历史或其他方向；缺少接口就记 Unknown。保留方法链出处与改编说明。
```

CUSTOM 不隐含 CORE；这里因为明确列出了 core-design 才读取它。范围内文件的链接也不会自动扩读。

### 3. 继续已有方向，补循环

```text
使用 $gameplay-mechanism-designer，继续 yanzhou/exploration/〈已有DIR目录〉。
沿该方向已登记来源和版本，不换基线，不读其他方向。
用 Loop Builder 补出每轮玩家选择、消耗、反馈、下一轮保留状态、失败和退出条件。
新建议与已确认内容分开，直接更新本方向 README，不自动运行测试。
```

### 4. 以完整 GDD 为基准审查新方向

```text
使用 $gameplay-mechanism-designer，启动言咒新探索：〈主题〉。
阅读模式 GDD，按 start.md 的固定包完整读取并记录版本。
用 Audit 检查〈机制设想〉与现行规则的冲突、循环断点和缺失接口，给最小修改候选。
不读历史或其他探索方向，不直接修改现行设计。
```

想连同主系统来源和开发记录核对时，可把模式换为 FULL（全量主系统文本），但成本更高；它仍不包含历史、其他方向和外部代码。只要框架帮助、不借用游戏背景时用 NONE。已有方向改用上述 GDD/FULL，须在话术中明确“本轮切换阅读模式并保留旧基线记录”。

## 如何接入当前文档系统

| 项目约束 | 适配行为 |
| --- | --- |
| 阅读由用户控制 | 先应用 READ-1，再读正文；CORE/GDD/FULL/CUSTOM/NONE 不因 skill 模式改变 |
| 探索按方向简化 | 一个 DIR 一个 README；Spark 的三个候选不会自动变成三套目录 |
| 主系统与探索隔离 | 主系统新点子入 `yanzhou/sources/inbox/`；探索入所属 DIR；调用 skill 不等于选定探索 |
| 原始想法不能直接晋级 | 自动推演只形成 Raw 假设，正式资格由 grill-with-docs 确认 |
| 统一正式文档 | 使用根登记 GDD/Proposal 等模板；上游 Full Design 大纲不能替代 |
| 设计与代码分开 | Prototype Pack 默认写计划；技术实现进对应代码仓库，开发状态进索引 |
| 固定来源可追踪 | 游戏背景记录提交/哈希；方法资料另记上游版本、实际引用链号与原创改编 |
| 多项目隔离 | 独立肉鸽遵循自身路由，不套用言咒背景；不读取旧归档来补 Unknown |

详细执行规则在[项目适配层](../../.codex/skills/gameplay-mechanism-designer/references/project-integration.md)。通用机制资料与“游戏背景材料”分开：阅读 CORE 仍可按需用方法图谱；若连图谱也不想读，明确说“只使用我提供的材料，不检索内置方法资料”。

它与现有工具各司其职：`game-analysis-orchestra` 处理参考产品拆解；本 skill 组织机制候选；`grill-with-docs` 负责资格澄清和文档一致性。无需为了使用本 skill 再安装配套技能。

## 来源审查与维护

本轮按 skill-vetter 完整审查固定提交下的11份 skill 文件及仓库 MIT LICENSE。内容为 Markdown、YAML、TSV，无执行脚本、依赖安装、凭据读取、上传逻辑或后台任务。判定 **LOW：可按本项目文档范围安装**。GitHub API 审查时为0 stars / 0 forks；下载量、外部审查记录未知，不据此声称可信度已经被社区验证。

保留仓库 MIT 通知及 TSV 对“六边形老闪（张鹏）”原图谱的署名。安装时11份文件与固定 Git blob 逐字节一致；之后仅修改 SKILL.md 的前置项目规则和 agents/openai.yaml 的启动话术，新增 project-integration.md 与 source-lock.json，并从仓库根补入 LICENSE。九份上游方法参考文件保持原字节。

[source-lock.json](../../.codex/skills/gameplay-mechanism-designer/source-lock.json)记录上游文件 SHA-256、提交与本地修改清单。更新时先登记计划、审查新版本差异，再重新合并适配层；不要用上游覆盖安装抹掉本地规则，也不要把这里登记的来源版本冒充游戏文档版本。审计临时副本与脚本不属于运行 skill。

验证记录：skill 结构校验通过；283 条链 ID 唯一、表列完整；本次新增/修改的18处本地链接有效；九份上游方法参考文件哈希保持；人工核对了 CORE / CUSTOM / NONE、旧方向续作、Raw Full Design、正式 GDD 与 Prototype Pack 的路由。后者是规则审阅，未运行模型端到端玩法评测或真实原型测试。

登记扫描 `20260930-072312` 已识别本项目唯一安装项，分类为 `project-runtime-conditional`，`runtimeVisible=null` 表示随活动工作区决定可见性，不是全局启用或实际触发测试结果。计划、审查与结果已写入本机 skill registry；未修改评估隔离区。

[探索启动规范](../../yanzhou/exploration/start.md) · [共享模板](../../game-design-workflow/templates/README.md) · [返回仓库入口](../../README.md)
