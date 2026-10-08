# 系统目录

Project ID：game-002。文档角色：Navigation。修订：2026-10-08 / system-docs.2。依据 G002-DOC-013／014。

## 六个主系统

```text
systems/
├─ artifact-system/                  法器系统
├─ inscription-system/               铭文系统
│  └─ augment-system/                辅槽系统
├─ action-card-system/               行动卡系统
│  └─ mark-system/                   标记系统
├─ enemy-system/                     敌人系统
├─ resource-system/                  资源系统
└─ meta-progression-system/          局外成长系统（尚未开发）
```

每个系统与子系统均使用五个文件：`README.md` 导航与状态、`rules.md` 规则、`experience.md` 玩家体验、`design.md` 设计定位与待定方案、`examples.md` 独立示例。文件名不改变确认、采纳或证据状态。

| 系统 | 职责 | 当前状态 |
| --- | --- | --- |
| [法器系统](artifact-system/README.md) | 法器本体、处理流程、供料编排、容量预留、打断返工与契合接口 | 既有规则与待定内容分别保留 |
| [铭文系统](inscription-system/README.md) | 铭文实体、核心装配、兼容与挂接，包含辅槽子系统 | 既有规则；辅槽新增通用框架仍为 Qualified |
| [行动卡系统](action-card-system/README.md) | 卡牌类别、行动效果、战斗行与共同结算，包含标记子系统 | 既有条款 Accepted；行动／标记新增通用结构 Qualified，体验 NotRun |
| [敌人系统](enemy-system/README.md) | 敌人程序、遭遇输入、敌方行动与应对窗口 | 既有规则与设计目标分别保留 |
| [资源系统](resource-system/README.md) | 材料、供给、托管、维护、转化与数量合同 | 既有规则与待定内容分别保留 |
| [局外成长系统](meta-progression-system/README.md) | 预留独立系统入口；范围、机制与持续性均待设计 | 尚未开发；仅占位 |

## 公共流程与相邻内容

[公共流程与合同](../common/README.md)保留局内路线、局内奖励与经济、交互与保存，不列为第七个主系统。本局战斗之外的获取和跨战携带不自动等于局外成长。

具体法器、卡牌与敌人内容仍在 [内容目录入口](../README.md) 维护；本次目录调整不另发卡表、不重写阶段成果。既有 SYS-001—007 保留为来源和规格域标识，不把它们重新编号成六个系统；现行条款位置见 [规则索引](../../governance/rule-index.md)。

## 空白通用框架

使用 [系统通用框架模板](../../../game-design-workflow/templates/system-framework/README.md)，整目录复制五个文件。模板只提供待填写结构，不带入言咒或其他项目规则。

[现行设计入口](../README.md) · [文档职责](../../governance/document-contract.md#系统文件夹与分文件职责) · [目录调整记录](../../governance/decision-log.md#g002-doc-013)
