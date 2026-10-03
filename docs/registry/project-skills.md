# 项目 Skill 清单

2026-10-02。本项目安装共 **4 项**，均位于 `.codex/skills/`；全局技能和插件不计入此数。管理流程见 [SK-1](../skill-management.md)，本轮证据见[审查记录](../skills/2026-10-02-game-design-skill-review.md)。

| 项目安装 | 职责与启动条件 | 来源及状态 |
| --- | --- | --- |
| [game-analysis-orchestra](../../.codex/skills/game-analysis-orchestra/SKILL.md) | 对已提供的游戏媒体材料做证据化拆解；输出到 media-analysis-lab，再由目标项目判断资格 | 原有项目技能，保留现状；本轮只复核入口与职责，未重新全量安全审计；上游来源锁 Unknown |
| [gameplay-mechanism-designer](../../.codex/skills/gameplay-mechanism-designer/SKILL.md) | 扩展机制、玩法循环及不同方向；先读项目适配层 | 原有适配版；qiuaoru-coder/game-design-agent-skills，固定 `29e8c759ca26c6bd4f337744b647dc728bf322b6`，以 source-lock 为准 |
| [game-design-reality-check](../../.codex/skills/game-design-reality-check/SKILL.md) | 质疑假设、区分证据、找失败条件和最小验证方式 | 本轮新增并适配；同上游及提交；完整子目录审查，MIT；无自动实验 |
| [gdd-toolkit](../../.codex/skills/gdd-toolkit/SKILL.md) | 指定系统的接口、交叉影响、MDA 与 GDD 一致性审查 | 本轮新增方法适配版；mamoru-miyagawa/gdd_toolkit，固定 `33f2d88677da8f9ab6ac2659c8ed72a951dbbff0`；MIT；不含上游 CLI |

新增两项的安装、来源和格式已检查；人工边界演练不等于独立模型效果评估，更不等于真人玩法验证。新装技能下一轮生效。

## 全局辅助能力

`skill-registry-control` 负责注册，`skill-vetter` 负责安全审查，`skill-installer` 负责安装，`skill-creator` 负责适配。它们继续使用已有全局安装，不复制到项目。

`grill-with-docs` 用于资格和关键决策澄清，遵守本项目批量问答约定；`windows-cn-agent-ops` 用于 Windows 文件操作。实现和测试技能按实际代码仓库任务选择，不据此授予代码访问或实验权限。

## 推荐调用

- 新构思：`使用 $gameplay-mechanism-designer，按本方向登记的阅读范围提出三个结构不同的方案；保留 Raw/Unknown，不进入正式 GDD。`
- 假设审查：`使用 $game-design-reality-check，只审查我指定的方案和证据，指出最可能失败的条件，给最低成本验证计划，本轮不执行实验。`
- 系统一致性：`使用 $gdd-toolkit，按 CUSTOM 白名单审查指定系统之间的输入、输出、时序与冲突；记录无法判断之处，不自动修改现行规则。`
- 持续协作：按[多智能体分工](../../yanzhou/governance/agent-collaboration.md)给出本轮目标、材料范围与完成条件，再启动有界任务。
