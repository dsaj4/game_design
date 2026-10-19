# 言咒项目操作

2026-10-18。game-002，工作区`yanzhou/`；继承根AGENTS的资格、Git及设计／代码边界。

## 开始阅读

- **开发接手或主系统完善**：先读[development/README](development/README.md)，按其8文件启动包了解构思主系统、术语、版本、问题和工作方式。记CUSTOM及启动时HEAD；只读清单，不递归跟随链接。已注入的AGENTS计一次。用户指定更窄材料时以用户为准。
- **具体实现／规则修改**：启动包只是定位，不足以实现规则。按任务补读对应rules、参数／案例／验收及[开发规范](development/development-standard.md)；补充具体文件和版本后再实现。无授权扩读的明确材料合同继续有效。
- **探索方向**：先读[阅读合同](exploration/start.md)和[探索AGENTS](exploration/AGENTS.md)，沿其模式；不套用开发启动包，不自动读取主系统或其他方向。
- **局部管理**：只读目标及必要操作规则；不自动读核心设计、来源或GDD。

当前顺序已由用户确认：先闭合首场核心玩法，再开始同一游戏的2D表现。旧3D不是新任务排程；2D具体展示条款尚未采纳，不能推断CORE-063已失效。

## 各写一处

| 内容 | 位置 |
| --- | --- |
| 现行玩法与参数 | `design/`；`core-design.md`为摘要，`baseline.md`为版本，具体rules为细则 |
| 领域语言 | `CONTEXT.md` |
| 原话、资格、提案、评估、待采纳变更 | `sources/inbox/`、`materials/`、`proposals/`、`evaluations/`、`draft-changes/` |
| GDD草案 | `sources/gdd-drafts/`；正式模板用根`game-design-workflow/templates/README.md` |
| 当前问题／已采纳决策 | `governance/questions.md`／`decision-log.md`；不另建问题数据库 |
| 当前能力／单轮方法 | `development/README.md`／`iteration-spec.md` |
| 视觉原件与资产身份 | `visual/`及统一AS／DM目录，原件就地 |
| 实现、构建、技术证据 | 外部代码仓库；当前3D为`E:/Project/yanzhou-godot/` |
| 查看与执行合同 | `E:/Project/yanzhou-workspace/`，不复制GDD或另一套进度 |

写入职责有疑问再查[文档合同](governance/document-contract.md)，查旧决定时按相关ID取`decision-log`章节；不把整份历史作为默认背景。旧资料中的“当前”只指原日期，历史TH/CAL和Demo局部结果不能外推完整RC1或真人体验。

## 开发遇到设计取舍

按[开发规范第8节](development/development-standard.md#8-设计裁决闸门)暂停当前批次，保全现有改动，交专门设计对接agent集中处理；总控确认阻塞及必要采纳落地后恢复。已确认事项不重问，规则已有唯一答案的纯工程缺口不冒充设计未决。小修改可复用已确认产物，只补变化与对照；新重点交互仍走文字→HTML→效果→实现。

新方向、设计资格、玩法采纳和实验授权分别处理。历史恢复不扩大材料范围，不重建兼容树，不覆盖原有未提交内容。
