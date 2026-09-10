# SW01语义世界对象范围采纳交付

日期：2026-09-10。状态：Accepted / Scope。决策：G002-SCOPE-002。证据：Hypothesis。基础执行基线为Core Concept v0.6。

## 已确认内容

法术对象设计范围覆盖实体、部件、材料、属性状态、空间关系，以及飞行物、敌方攻击、法术冷却等过程；各类按明确能力开放操作。胜负判定、全局结算顺序等世界基础规则保持固定。

用户已针对SW01回答“确认”。此次只晋级并采纳范围，SW02–SW07的具体交互机制保持未确认，数值继续重新设计。

## 追溯入口

- [原始表达、问题及用户确认](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)。
- [正式范围素材](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)。
- [提案](../game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md)与[评估](../game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md)。
- [采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md)、[核心](../game-design-workflow/core-concept.md)及[决策记录](../game-design-workflow/decision-log.md)。

## 当前待决

SW02推荐具体实例绑定与条件绑定并存：前者持续指向同一对象；后者战前确定选择条件、释放时自动匹配当前对象，使符合条件的新生对象可以参与。方案比较和边界推演已保存到inbox；并存模型、名单时点、顺序及具体表达尚未采纳。

SW03–SW07继续依对象设计逐项展开。[决定清单](design-decisions-needed.md)作为当前问题入口。文档统一阶段C01–C08的完成结论保留，本记录不把新增设计分支算作已处理。

## 文件清单

本次新建范围素材、提案、评估、Draft Change和本记录；同步核心、词汇、决策、来源与相关入口。以下清单仅含本次任务文件：

- [README.md](../../../README.md)
- [docs/control-center.md](../../../docs/control-center.md)
- [workspaces/game-002/CONTEXT.md](../../../workspaces/game-002/CONTEXT.md)
- [workspaces/game-002/README.md](../../../workspaces/game-002/README.md)
- [workspaces/game-002/docs/control-center.md](../../../workspaces/game-002/docs/control-center.md)
- [workspaces/game-002/docs/design-decisions-needed.md](../../../workspaces/game-002/docs/design-decisions-needed.md)
- [workspaces/game-002/game-design-workflow/README.md](../../../workspaces/game-002/game-design-workflow/README.md)
- [workspaces/game-002/game-design-workflow/core-concept.md](../../../workspaces/game-002/game-design-workflow/core-concept.md)
- [workspaces/game-002/game-design-workflow/decision-log.md](../../../workspaces/game-002/game-design-workflow/decision-log.md)
- [workspaces/game-002/game-design-workflow/draft-changes/README.md](../../../workspaces/game-002/game-design-workflow/draft-changes/README.md)
- [workspaces/game-002/game-design-workflow/evaluations/README.md](../../../workspaces/game-002/game-design-workflow/evaluations/README.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/README.md](../../../workspaces/game-002/game-design-workflow/idea-inbox/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-casting-time-and-interruption.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-basic-sentence-targeting-and-locking.md)
- [workspaces/game-002/game-design-workflow/idea-materials/README.md](../../../workspaces/game-002/game-design-workflow/idea-materials/README.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/README.md](../../../workspaces/game-002/game-design-workflow/idea-proposals/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/evaluations/E-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md](../../../workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md)
- [workspaces/game-002/docs/semantic-world-scope-adoption.md](../../../workspaces/game-002/docs/semantic-world-scope-adoption.md)

## 验收范围

已检查所列22份文档：UTF-8有效，295处相对链接均可解析，补丁空白检查通过，正式素材实数与索引均为42。核心、范围素材与Draft Change包含完全一致的范围正文；当前问题入口统一指向SW02。

逻辑审查区分已采纳范围和具体机制候选。本次没有运行原型、数值模拟或玩家测试，证据继续为Hypothesis。
