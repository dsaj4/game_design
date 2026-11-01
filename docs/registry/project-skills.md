# 项目 Skill 清单

2026-11-01。本项目安装共 **15 项**，均位于 `.codex/skills/`：原4项设计技能及新增11项世界观技能。全局技能、插件及外部Mr. Mak工作台不计入此数。管理流程见 [SK-1](../skill-management.md)，原4项安装证据见[审查记录](../skills/2026-10-02-game-design-skill-review.md)。

| 项目安装 | 职责与启动条件 | 来源及状态 |
| --- | --- | --- |
| [game-analysis-orchestra](../../.codex/skills/game-analysis-orchestra/SKILL.md) | 对已提供的游戏媒体材料做证据化拆解；按目标项目sources／所属方向保存，再独立判断资格 | 原有项目技能；2026-11-01仅更新退役目录路由，未增加能力或重新全量安全审计；上游来源锁 Unknown |
| [gameplay-mechanism-designer](../../.codex/skills/gameplay-mechanism-designer/SKILL.md) | 扩展机制、玩法循环及不同方向；先读项目适配层 | 原有适配版；qiuaoru-coder/game-design-agent-skills，固定 `29e8c759ca26c6bd4f337744b647dc728bf322b6`，以 source-lock 为准 |
| [game-design-reality-check](../../.codex/skills/game-design-reality-check/SKILL.md) | 质疑假设、区分证据、找失败条件和最小验证方式 | 本轮新增并适配；同上游及提交；完整子目录审查，MIT；无自动实验 |
| [gdd-toolkit](../../.codex/skills/gdd-toolkit/SKILL.md) | 指定系统的接口、交叉影响、MDA 与 GDD 一致性审查 | 本轮新增方法适配版；mamoru-miyagawa/gdd_toolkit，固定 `33f2d88677da8f9ab6ac2659c8ed72a951dbbff0`；MIT；不含上游 CLI |

新增两项的安装、来源和格式已检查；人工边界演练不等于独立模型效果评估，更不等于真人玩法验证。新装技能下一轮生效。

<a id="worldbuilding-skills"></a>

## 世界观技能组（完整11项）

2026-11-01按用户全量安装要求引入jwynia/agent-skills的整个`skills/creative/fiction/worldbuilding/`目录，固定提交`e02ec7e226a6e4f8419fd3b88a1d8e472d421b32`。每项先读项目适配层，上游方法及全部子目录资源保留，source-lock逐项记录来源、哈希和改写。审查范围、许可声明、脚本限制及验证见[本轮安装记录](../skills/2026-11-01-worldbuilding-skill-installation.md)。

| 项目安装 | 主要用途 |
| --- | --- |
| [worldbuilding](../../.codex/skills/worldbuilding/SKILL.md) | 世界与社会关系的一致性诊断 |
| [systemic-worldbuilding](../../.codex/skills/systemic-worldbuilding/SKILL.md) | 虚构前提引发的多层因果 |
| [language-evolution](../../.codex/skills/language-evolution/SKILL.md) | 语言历史、方言、借词、失传与书写演变 |
| [conlang](../../.codex/skills/conlang/SKILL.md) | 声音、词形、命名与语言一致性 |
| [oblique-worldbuilding](../../.codex/skills/oblique-worldbuilding/SKILL.md) | 不同叙述者的文献视角、名人引述与物品描述 |
| [belief-systems](../../.codex/skills/belief-systems/SKILL.md) | 信仰、仪式及学说分歧 |
| [economic-systems](../../.codex/skills/economic-systems/SKILL.md) | 资源、劳动、交换与社会关系 |
| [governance-systems](../../.codex/skills/governance-systems/SKILL.md) | 势力、制度、权力与历史叙述 |
| [settlement-design](../../.codex/skills/settlement-design/SKILL.md) | 聚落功能、空间与历史层次 |
| [metabolic-cultures](../../.codex/skills/metabolic-cultures/SKILL.md) | 特定闭环生存条件下的文化推演 |
| [world-fates](../../.codex/skills/world-fates/SKILL.md) | 长期命运与势力消长的候选方法 |

新装技能从下一轮会话开始使用，列表未刷新时重开会话。完整安装不等于每次必须调用全部，也不默认创建world-bible、context配置、自动命运结算或代理；脚本已保留但未执行，远程运行依赖未引入。正式资格、当前规则及材料范围始终沿项目约定。

## 全局辅助能力

`skill-registry-control` 负责注册，`skill-installer` 负责安装，`skill-creator` 负责适配，使用已有全局能力，不复制到项目。原记录提及的全局 `skill-vetter` 已于2026-10-03卸载，本次未重装；保留协议仅作审查参考，不声称仍为可调用全局技能。

`grill-with-docs` 用于资格和关键决策澄清，遵守本项目批量问答约定；`windows-cn-agent-ops` 用于 Windows 文件操作。实现和测试技能按实际代码仓库任务选择，不据此授予代码访问或实验权限。

## 外部 Mr. Mak 工作台

2026-10-14按用户全量接入授权，在独立 `E:/Project/yanzhou-workspace` 固定上游 v0.5.1 / `59477702e1f86187d1ac8a84905505e2dfe53c73`。其20项受控方法入口在 `.agents/skills/`，`.claude/skills/`为同文分发副本；不加入本仓库4项计数，也不覆盖全局技能。入口先读言咒合同，原始方法与工具资源保留为固定来源库，391个文件逐个SHA-256；未全量审查的执行库不写成安全通过，具体任务执行前继续核查。

范围覆盖：制作路线、角色设定、图像参考、程序几何、材质、Blender动画、动作参考、引擎动画、UI、特效、关卡、音频、视觉审查、fal、Higgsfield、视频按帧观察、语音输入设置、规划、交接和工作台报告。完整对应表见[接收审查](../../../yanzhou-workspace/docs/yanzhou-skill-review.md)，本项目使用入口见[开发工作台](../../yanzhou/standards/workspace.md)。

全局扫描器将此自定义 `.agents/.claude`位置保守分类为source-only；工作台自身ContextLibrary发现20项的运行证据单列。不能据目录存在声称本次game会话已加载20项。注册初扫 `20261014-215647`、最终复扫 `20261014-220936` 的运行时可见重复名均为0，来源、范围与结果已记全局变更日志。

## 推荐调用

- 新构思：`使用 $gameplay-mechanism-designer，按本方向登记的阅读范围提出三个结构不同的方案；保留 Raw/Unknown，不进入正式 GDD。`
- 假设审查：`使用 $game-design-reality-check，只审查我指定的方案和证据，指出最可能失败的条件，给最低成本验证计划，本轮不执行实验。`
- 系统一致性：`使用 $gdd-toolkit，按 CUSTOM 白名单审查指定系统之间的输入、输出、时序与冲突；记录无法判断之处，不自动修改现行规则。`
- 持续协作：按[多智能体分工](../../yanzhou/standards/agent-collaboration.md)给出本轮目标、材料范围与完成条件，再启动有界任务。

2026-11-01目录退役联动：仅修正game-analysis-orchestra的Project storage段，未改工作流脚本、自动调用策略或其他技能。UTF-8模式下结构校验通过；注册复扫20261101-022316沿既有扫描根及排除项，目标仍为project-runtime-conditional、运行时可见重名0；未执行完整拆解或效果评估。
