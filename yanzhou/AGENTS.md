# 言咒项目操作

2026-11-01。game-002，工作区`yanzhou/`；继承根AGENTS的资格、Git及设计／代码边界。输入、来源与验收按[轻量记录](../docs/design-workflow.md#言咒轻量记录)：摘要代替原话，共用固定版本，准确引用，已有信息不重复抄录。

## 开始阅读

- **系统设计与设计师接手**：从[系统设计手册](system-design/handbook.md)定位目标、预期体验、核心取舍及具体工作稿。`system-design/`与规则层`design/`平级；工作方法集中在[standards](standards/README.md)。未决和候选保持原资格，不因整理视为规则采纳。
- **世界观与叙事**：从[worldbuilding](worldbuilding/README.md)进入，世界、文明因果与人物故事独立维护；新方向仍先按READ-1选择范围。虚构历史不进入项目`history/`，叙事不改写精确玩法或内容库规格。

- **开发接手或主系统完善**：先读[development/README](development/README.md)，按其5文件启动包读取唯一核心与任务入口。记CUSTOM及启动时完整提交；已注入的AGENTS计一次，术语、基准和问题只查需要的条目。用户指定更窄材料时以用户为准。
- **具体实现／规则修改**：沿[任务设计包](development/task-pack.md)选行为，再按触发条件补细则、内容和验收。不要每次读全GDD或来源沿革。改公共机制须覆盖所有受影响接口；明确的材料白名单继续有效。
- **探索方向**：先读[阅读合同](exploration/start.md)和[探索AGENTS](exploration/AGENTS.md)，沿其模式；不套用开发启动包，不自动读取主系统或其他方向。
- **局部管理**：只读目标及必要操作规则；不自动读核心设计、来源或GDD。

当前同一游戏的新2D开发按[开工交接](development/README.md#新2d开工交接)限定材料。CORE-071已明确淘汰38项非alchemy内容，包括原EX-004首战套组、敌表、案例与完整首战包；CORE-072已限定采纳35配方制作参数、43卡权限／11成品卡效与新的炼金咒定义，现有62项alchemy及3构筑；核心组合、几何、携带、具体供给与初态未闭合，不能作为已采纳完整首战。替代完整内容与合法几何待设计。CORE-070共用背包、069辅助／核心装配、068固定用途／待料及067统一卡牌／手动使用继续生效；四个通用任务包可按合法输入拆任务。旧实现只保留固定证据，不能恢复退役设计；新增机制实现与测试NotRun。

## 各写一处

| 内容 | 位置 |
| --- | --- |
| 现行玩法与参数 | `design/GDD.md`为唯一核心正文，系统rules为细则；具体裁决由规则索引定位，`baseline.md`管版本 |
| 具体物件、配方、文案与占形 | [content-library](content-library/README.md)的catalog为单一数据源，Markdown分册与HTML展板均派生；资格逐项保留，规则仍归design |
| 系统目标、理由、体验及设计方法 | `system-design/handbook.md`为设计师入口；各系统说明、炼金方法、背包工作稿与表现设计在`system-design/`维护；具体物件查询内容库 |
| 世界、虚构历史、人物与背景故事、线索揭示 | [worldbuilding](worldbuilding/README.md)；确认、候选、角色信念与Unknown分开，正式物件文案仍归内容库 |
| 与游戏规则无关的设计／开发工作规范 | `standards/`：文档职责、开发规范、迭代、审阅、协作、工作台与阶段方法 |
| 领域语言 | `CONTEXT.md` |
| 意图摘要、资格、提案、评估、待采纳变更 | `sources/inbox/`、`materials/`、`proposals/`、`evaluations/`、`draft-changes/` |
| GDD草案 | `sources/gdd-drafts/`；正式模板用根`game-design-workflow/templates/README.md` |
| 当前问题／已采纳决策与编号 | `governance/questions.md`／`decision-log.md`；不另建问题数据库或编号沿革副本 |
| 当前能力／单轮方法 | `development/README.md`／`standards/iteration-spec.md` |
| 任务设计输入／场景审阅 | `development/task-pack.md`及`task-packs/`／`standards/design-review.md`；派生读取，不独立改规则 |
| 视觉原件与资产身份 | `visual/`及统一AS／DM目录，原件就地 |
| 实现、构建、技术证据 | 当前二维工程`E:/Project/yanzhou-2d/`；旧3D及早期Demo已退役，恢复入口见`history/README.md` |
| 查看与执行合同 | `E:/Project/yanzhou-workspace/`，不复制GDD或另一套进度 |

写入职责有疑问再查[文档合同](standards/document-contract.md)，查旧决定时按相关ID取`decision-log`章节；不把整份历史作为默认背景。旧资料中的“当前”只指原日期，历史TH/CAL和Demo局部结果不能外推完整RC1或真人体验。

## 开发遇到设计取舍

按[开发规范第8节](standards/development-standard.md#8-设计裁决闸门)暂停当前批次，保全现有改动，交专门设计对接agent集中处理；总控确认阻塞及必要采纳落地后恢复。已确认事项不重问，规则已有唯一答案的纯工程缺口不冒充设计未决。小修改可复用已确认产物，只补变化与对照；新重点交互仍走文字→HTML→效果→实现。

新方向、设计资格、玩法采纳和实验授权分别处理。历史恢复不扩大材料范围，不重建兼容树，不覆盖原有未提交内容。
