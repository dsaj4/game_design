# Agent 规则索引

文档 ID：`AGS-INDEX-001`

状态：`Proposed / Phase 4 pilot`

版本：`0.1.0`

更新时间：`2026-09-04`

复审日期：`2026-10-04`

## 1. 使用说明

这是规则的导航和评审清单，不是规则正文的复制品。`Status=Inherited` 表示来自现有 `AGENTS.md` 或仓库协议；`Proposed` 表示本轮形成、尚未集成；`Accepted` 只能在完成反例演练、冲突检查和版本记录后使用。

规则强度：`HARD` 违反时必须停止越界动作；`SHOULD` 偏离时记录理由和影响；`EXPERIMENT` 只用于明确试验，不阻塞无关工作。

## 2. 规则总表

| Rule ID | 类别 | Strength | Status | 触发摘要 | 正文 |
| --- | --- | --- | --- | --- | --- |
| `ADRULE-ROUTE-001` | Routing | SHOULD | Proposed | 任何会产生文件或判断的输入 | [routing](routing.md) |
| `ADRULE-ROUTE-002` | Routing | HARD | Inherited | 原始想法/未完整机制 | [routing](routing.md) |
| `ADRULE-ROUTE-003` | Routing | SHOULD | Proposed | 理论、课程、外部资料 | [routing](routing.md) |
| `ADRULE-ROUTE-004` | Routing | SHOULD | Proposed | 产品案例/竞品 | [routing](routing.md) |
| `ADRULE-ROUTE-005` | Routing | HARD | Inherited | 代码实现、Bug、进度 | [routing](routing.md) |
| `ADRULE-STAGE-001` | Stage Gate | SHOULD | Proposed | 阶段报告和过门 | [stage-gates](stage-gates.md) |
| `ADRULE-STAGE-002` | Stage Gate | SHOULD | Proposed | 阶段门判断 | [stage-gates](stage-gates.md) |
| `ADRULE-STAGE-003` | Stage Gate | SHOULD | Proposed | 试图跳阶段/伪造完成 | [stage-gates](stage-gates.md) |
| `ADRULE-STAGE-004` | Stage Gate | SHOULD | Proposed | 平台发布检查 | [stage-gates](stage-gates.md) |
| `ADRULE-STAGE-005` | Stage Gate | SHOULD | Proposed | Iterate/Park/Stop | [stage-gates](stage-gates.md) |
| `ADRULE-EVIDENCE-001` | Evidence | SHOULD | Proposed | 写入重要结论 | [evidence](evidence-and-citations.md) |
| `ADRULE-EVIDENCE-002` | Evidence | SHOULD | Proposed | 缺失或失败分集 | [evidence](evidence-and-citations.md) |
| `ADRULE-EVIDENCE-003` | Evidence | SHOULD | Proposed | 来源/测试结果冲突 | [evidence](evidence-and-citations.md) |
| `ADRULE-GDD-001` | GDD | HARD | Inherited | 创建或更新 GDD | [gdd](gdd-rules.md) |
| `ADRULE-GDD-002` | GDD | HARD | Inherited | 新增或修改系统 | [gdd](gdd-rules.md) |
| `ADRULE-GDD-003` | GDD | HARD | Inherited | GDD 验收/验证 | [gdd](gdd-rules.md) |
| `ADRULE-GDD-004` | GDD | HARD | Inherited | 设计与代码混写 | [gdd](gdd-rules.md) |
| `ADRULE-DESIGN-001` | Design Reasoning | SHOULD | Proposed | 新增设计原则 | [design](design-principles.md) |
| `ADRULE-DESIGN-002` | Design Reasoning | SHOULD | Proposed | 新机制/卡牌/资源方案 | [design](design-principles.md) |
| `ADRULE-DESIGN-003` | Design Reasoning | SHOULD | Proposed | 理论/竞品迁移 | [design](design-principles.md) |
| `ADRULE-DESIGN-004` | Design Reasoning | SHOULD | Proposed | 否决、失败、范围缩减 | [design](design-principles.md) |
| `ADRULE-PLAYTEST-001` | Prototype / Playtest | SHOULD | Proposed | 创建原型或试玩 | [prototype](prototype-and-playtest.md) |
| `ADRULE-PLAYTEST-002` | Prototype / Playtest | SHOULD | Proposed | 处理玩家反馈 | [prototype](prototype-and-playtest.md) |
| `ADRULE-PLAYTEST-003` | Prototype / Playtest | SHOULD | Proposed | 整理测试结果 | [prototype](prototype-and-playtest.md) |
| `ADRULE-PLAYTEST-004` | Prototype / Playtest | SHOULD | Proposed | 规则/费用/时序改动 | [prototype](prototype-and-playtest.md) |
| `ADRULE-BALANCE-001` | Prototype / Playtest | SHOULD | Proposed | 平衡/对称/先手讨论 | [prototype](prototype-and-playtest.md) |
| `ADRULE-COLLAB-001` | Collaboration / Safety | HARD | Inherited | 修改文件前 | [collaboration](collaboration-and-safety.md) |
| `ADRULE-COLLAB-002` | Collaboration / Safety | HARD | Inherited | 修改核心构思 | [collaboration](collaboration-and-safety.md) |
| `ADRULE-COLLAB-003` | Collaboration / Safety | HARD | Inherited | 多意图/多目录请求 | [collaboration](collaboration-and-safety.md) |
| `ADRULE-COLLAB-004` | Collaboration / Safety | HARD | Inherited | 正式文档交付 | [collaboration](collaboration-and-safety.md) |
| `ADRULE-COLLAB-005` | Collaboration / Safety | SHOULD | Proposed | 外部资料/不可逆操作 | [collaboration](collaboration-and-safety.md) |
| `ADRULE-COLLAB-006` | Collaboration / Safety | SHOULD | Proposed | 正式文档提交前检查 | [collaboration](collaboration-and-safety.md) |

## 3. 评审队列

下一次评审逐条检查：

1. 是否能用一个真实请求触发并完成，而不依赖“感觉”或上下文猜测。
2. 是否与 `AGENTS.md`、现有 GDD 模板、双层想法库和代码开发索引冲突。
3. 是否有反例：信息不足、多个意图、缺失分集、相反测试结果、技术约束改变玩法。
4. 是否能明确输出文件、状态轴、失败状态、责任人和回退位置。
5. 是否有来源 Evidence ID、适用边界、版本和复审触发。

## 4. 四类最小回归请求

| 场景 | 预期检查 | 不应发生 |
| --- | --- | --- |
| 零散卡牌想法 | 路由到 inbox，保留 Raw Idea，逐项资格确认 | 直接进入 GDD/核心构思 |
| “帮我写 GDD” | 选择 GDD-0/1/2，检索两层素材，分离代码边界 | 静默跳过素材或写技术实现 |
| “像某游戏，借鉴一下” | 建立产品案例，事实/分析/假设分层 | 复制系统或商业结论 |
| “功能做到哪/修 Bug” | 更新代码进度索引，链接 GDD 和偏差 | 把代码状态写进 GDD 或改玩法结论 |

## 5. 集成状态

本索引和新增正文目前是 `Proposed / Pilot`。Phase 5 集成前，不得把 `Status: Proposed` 条目宣传为已经自动执行的系统政策；`Status: Inherited` 条目仍由其上游 `AGENTS.md`、现有 GDD 模板或 GitHub 协作规范持续生效。集成时应一次更新唯一承载文件，完成回归后再把新增条目标为 `Accepted` 或继续保留 `Proposed`。

来源：

- [知识系统升级 Spec](../game-design-knowledge-system-spec.md)
- [Agent 操作手册](../../AGENTS.md)
- [游戏设计与开发 Wiki](../../research/02-theory-digests/game-design-development-wiki/README.md)
- [GitHub 协作规范](../github-collaboration.md)
