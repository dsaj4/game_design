# 方法与适配器注册表

更新日期：2026-09-09。区分既有工作流入口与尚未实现的统一适配器，不承接旧测试的 Verified 状态。

| ID | 现有来源 | 登记状态 | 本轮边界 |
| --- | --- | --- | --- |
| media-analysis-guide-v1 | [轻量媒体分析说明](../shared/media-analysis/README.md) | Ready / Document Workflow | 默认可按单文件流程执行；借鉴实验室方法，不依赖其脚本或已安装技能，不代表已完成媒体分析实测 |
| game-analysis-orchestra | [已安装技能](../../.codex/skills/game-analysis-orchestra/SKILL.md) | Existing Workflow / Explicit Invocation | 用户明确调用时按该技能流程处理；轻量说明文档不依赖此技能 |
| media-analysis-packet | [媒体分析原型](../../media-analysis-lab/README.md) | Reference Only / Not Integrated | 复用素材包、证据、分析稿与质检分层思路；不搬迁历史 runs |
| legacy-combat | combat-lab/（冻结旧项目） | Parked / Not Integrated | 仅登记方法来源；没有跨项目移植源码、数据或测试 |
| legacy-semantic-generation | semantic-card-engine/（冻结旧项目） | Parked / Not Integrated | 同上；不能把 embedding 数据当一般缓存清理 |

未来接入必须先说明目标项目、设计来源、输入/输出契约、版本、代码位置、验证结果和不兼容项，再登记为可用。统一模拟运行器、可执行 Schema 和 context pack 生成器本轮均未实现。
