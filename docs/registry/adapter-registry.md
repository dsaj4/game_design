# 方法与适配器注册表

更新日期：2026-11-01。区分既有工作流入口与尚未实现的统一适配器，不承接旧测试的 Verified 状态。

| ID | 现有来源 | 登记状态 | 本轮边界 |
| --- | --- | --- | --- |
| media-analysis-guide-v1 | [轻量媒体分析说明](https://github.com/dsaj4/game_design/blob/d47080a1eab3903d37122e8ac0aba00d78c2aceb/media-analysis-lab/methods/project-analysis.md) | Archived / Historical Reference | 2026-11-01退出工作树；原方法仅供固定版本取证，不再作为默认执行入口 |
| game-analysis-orchestra | [已安装技能](../../.codex/skills/game-analysis-orchestra/SKILL.md) | Existing Workflow / Explicit Invocation | 用户明确调用时按该技能流程处理；产物写目标项目或用户指定位置，不重建旧分析区 |
| media-analysis-packet | [媒体分析原型](https://github.com/dsaj4/game_design/blob/d47080a1eab3903d37122e8ac0aba00d78c2aceb/media-analysis-lab/README.md) | Archived / Not Integrated | 原型和历史runs均退出工作树；保留固定版本，不作为可直接运行的本地工具 |
| legacy-combat | [combat-lab固定版本](https://github.com/dsaj4/game_design/tree/d18ea22222c6271405927e369452d04e1c8a6fd0/combat-lab) | Parked / Not Integrated | 仅登记方法来源；没有跨项目移植源码、数据或测试 |
| legacy-semantic-generation | [semantic-card-engine固定版本](https://github.com/dsaj4/game_design/tree/d18ea22222c6271405927e369452d04e1c8a6fd0/semantic-card-engine) | Parked / Not Integrated | 同上；不能把 embedding 数据当一般缓存清理 |

未来接入必须先说明目标项目、设计来源、输入/输出契约、版本、代码位置、验证结果和不兼容项，再登记为可用。统一模拟运行器、可执行 Schema 和 context pack 生成器本轮均未实现。
