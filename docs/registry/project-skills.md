# 项目 Skill 清单

2026-10-14。本项目安装仍为 **4 项**，均位于 `.codex/skills/`；全局技能、插件及外部Mr. Mak工作台不计入此数。管理流程见 [SK-1](../skill-management.md)，原安装证据见[审查记录](../skills/2026-10-02-game-design-skill-review.md)。

| 项目安装 | 职责与启动条件 | 来源及状态 |
| --- | --- | --- |
| [game-analysis-orchestra](../../.codex/skills/game-analysis-orchestra/SKILL.md) | 对已提供的游戏媒体材料做证据化拆解；输出到 media-analysis-lab，再由目标项目判断资格 | 原有项目技能，保留现状；本轮只复核入口与职责，未重新全量安全审计；上游来源锁 Unknown |
| [gameplay-mechanism-designer](../../.codex/skills/gameplay-mechanism-designer/SKILL.md) | 扩展机制、玩法循环及不同方向；先读项目适配层 | 原有适配版；qiuaoru-coder/game-design-agent-skills，固定 `29e8c759ca26c6bd4f337744b647dc728bf322b6`，以 source-lock 为准 |
| [game-design-reality-check](../../.codex/skills/game-design-reality-check/SKILL.md) | 质疑假设、区分证据、找失败条件和最小验证方式 | 本轮新增并适配；同上游及提交；完整子目录审查，MIT；无自动实验 |
| [gdd-toolkit](../../.codex/skills/gdd-toolkit/SKILL.md) | 指定系统的接口、交叉影响、MDA 与 GDD 一致性审查 | 本轮新增方法适配版；mamoru-miyagawa/gdd_toolkit，固定 `33f2d88677da8f9ab6ac2659c8ed72a951dbbff0`；MIT；不含上游 CLI |

新增两项的安装、来源和格式已检查；人工边界演练不等于独立模型效果评估，更不等于真人玩法验证。新装技能下一轮生效。

## 全局辅助能力

`skill-registry-control` 负责注册，`skill-installer` 负责安装，`skill-creator` 负责适配，使用已有全局能力，不复制到项目。原记录提及的全局 `skill-vetter` 已于2026-10-03卸载，本次未重装；保留协议仅作审查参考，不声称仍为可调用全局技能。

`grill-with-docs` 用于资格和关键决策澄清，遵守本项目批量问答约定；`windows-cn-agent-ops` 用于 Windows 文件操作。实现和测试技能按实际代码仓库任务选择，不据此授予代码访问或实验权限。

## 外部 Mr. Mak 工作台

2026-10-14按用户全量接入授权，在独立 `E:/Project/yanzhou-workspace` 固定上游 v0.5.1 / `59477702e1f86187d1ac8a84905505e2dfe53c73`。其20项受控方法入口在 `.agents/skills/`，`.claude/skills/`为同文分发副本；不加入本仓库4项计数，也不覆盖全局技能。入口先读言咒合同，原始方法与工具资源保留为固定来源库，391个文件逐个SHA-256；未全量审查的执行库不写成安全通过，具体任务执行前继续核查。

范围覆盖：制作路线、角色设定、图像参考、程序几何、材质、Blender动画、动作参考、引擎动画、UI、特效、关卡、音频、视觉审查、fal、Higgsfield、视频按帧观察、语音输入设置、规划、交接和工作台报告。完整对应表见[接收审查](../../../yanzhou-workspace/docs/yanzhou-skill-review.md)，本项目使用入口见[开发工作台](../../yanzhou/development/workspace.md)。

全局扫描器将此自定义 `.agents/.claude`位置保守分类为source-only；工作台自身ContextLibrary发现20项的运行证据单列。不能据目录存在声称本次game会话已加载20项。注册初扫 `20261014-215647`、最终复扫 `20261014-220936` 的运行时可见重复名均为0，来源、范围与结果已记全局变更日志。

## 推荐调用

- 新构思：`使用 $gameplay-mechanism-designer，按本方向登记的阅读范围提出三个结构不同的方案；保留 Raw/Unknown，不进入正式 GDD。`
- 假设审查：`使用 $game-design-reality-check，只审查我指定的方案和证据，指出最可能失败的条件，给最低成本验证计划，本轮不执行实验。`
- 系统一致性：`使用 $gdd-toolkit，按 CUSTOM 白名单审查指定系统之间的输入、输出、时序与冲突；记录无法判断之处，不自动修改现行规则。`
- 持续协作：按[多智能体分工](../../yanzhou/governance/agent-collaboration.md)给出本轮目标、材料范围与完成条件，再启动有界任务。
