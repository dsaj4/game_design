# 言咒项目操作

2026-10-31。game-002，工作区`yanzhou/`；继承根AGENTS的资格、Git及设计／代码边界。输入、来源与验收按[轻量记录](../docs/design-workflow.md#言咒轻量记录)：摘要代替原话，共用固定版本，准确引用，已有信息不重复抄录。

## 开始阅读

- **开发接手或主系统完善**：先读[development/README](development/README.md)，按其5文件启动包读取唯一核心与任务入口。记CUSTOM及启动时完整提交；已注入的AGENTS计一次，术语、基准和问题只查需要的条目。用户指定更窄材料时以用户为准。
- **具体实现／规则修改**：沿[任务设计包](development/task-pack.md)选行为，再按触发条件补细则、内容和验收。不要每次读全GDD或来源沿革。改公共机制须覆盖所有受影响接口；明确的材料白名单继续有效。
- **探索方向**：先读[阅读合同](exploration/start.md)和[探索AGENTS](exploration/AGENTS.md)，沿其模式；不套用开发启动包，不自动读取主系统或其他方向。
- **局部管理**：只读目标及必要操作规则；不自动读核心设计、来源或GDD。

当前准备同一游戏的新2D开发，按[开工交接](development/README.md#新2d开工交接)限定首轮范围和必要输入。CORE-068已采纳战前背包布局／固定用途、专属待料与默认自动补料，保留CORE-067统一卡牌、手动布牌与立即回收；四个任务包已同步，新增机制未实现、未测试；CORE-063仅约束原旧3D演示。CORE-066的EX-004战斗内容已按067／068迁移手动路线与战前用途，但无背包尺寸和材料形状输入，两组持牌与列间窗口的2D展示合同仍待闭合；既有独立行为可按已定范围拆任务；不要求先完成全游戏。

## 各写一处

| 内容 | 位置 |
| --- | --- |
| 现行玩法与参数 | `design/GDD.md`为唯一核心正文，系统rules为细则；具体裁决由规则索引定位，`baseline.md`管版本 |
| 领域语言 | `CONTEXT.md` |
| 意图摘要、资格、提案、评估、待采纳变更 | `sources/inbox/`、`materials/`、`proposals/`、`evaluations/`、`draft-changes/` |
| GDD草案 | `sources/gdd-drafts/`；正式模板用根`game-design-workflow/templates/README.md` |
| 当前问题／已采纳决策与编号 | `governance/questions.md`／`decision-log.md`；不另建问题数据库或编号沿革副本 |
| 当前能力／单轮方法 | `development/README.md`／`iteration-spec.md` |
| 任务设计输入／场景审阅 | `development/task-pack.md`及`task-packs/`／`design-review.md`；派生读取，不独立改规则 |
| 视觉原件与资产身份 | `visual/`及统一AS／DM目录，原件就地 |
| 实现、构建、技术证据 | 外部代码仓库；当前3D为`E:/Project/yanzhou-godot/` |
| 查看与执行合同 | `E:/Project/yanzhou-workspace/`，不复制GDD或另一套进度 |

写入职责有疑问再查[文档合同](governance/document-contract.md)，查旧决定时按相关ID取`decision-log`章节；不把整份历史作为默认背景。旧资料中的“当前”只指原日期，历史TH/CAL和Demo局部结果不能外推完整RC1或真人体验。

## 开发遇到设计取舍

按[开发规范第8节](development/development-standard.md#8-设计裁决闸门)暂停当前批次，保全现有改动，交专门设计对接agent集中处理；总控确认阻塞及必要采纳落地后恢复。已确认事项不重问，规则已有唯一答案的纯工程缺口不冒充设计未决。小修改可复用已确认产物，只补变化与对照；新重点交互仍走文字→HTML→效果→实现。

新方向、设计资格、玩法采纳和实验授权分别处理。历史恢复不扩大材料范围，不重建兼容树，不覆盖原有未提交内容。
