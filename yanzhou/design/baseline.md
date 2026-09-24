# 现行版本清单

更新：2026-09-23。文档角色：BaselineManifest。

| 层 | 身份 | 维护边界 |
| --- | --- | --- |
| 产品设计 | GDD-G002-FULL-001 / 1.0 RC1 | CORE-001–036及原RC1素材采用范围 |
| 文档整理 | doc.1 / 2026-09-23 | 导航、去重、历史分离、探索索引；非新玩法版本 |
| 原始输入提交 | `87ef6d1b7e2ba5812a3d62216a439a9c254393b0` | 本轮开始HEAD；两份已有素材删行及其他工作树变更未纳入 |
| 核心构思标识 | Core Concept v0.6 | 作为既有核心设计标识保留；详细规格以本目录为准 |
| 效果 | FX-001–134 | 每条独立修订与来源；134不是首版可用卡数量 |
| 视觉 | 05紧凑暗面，2026-09-19选定 | 独立Demo视觉方向；不删除GDD功能合同 |
| 实现 | 暗面Demo v0.1 / cf7b98d（索引记录） | 有可玩流程，完整RC1验收未完成 |
| 探索 | baseline-2026-09-09-001与各轮显式RC1来源 | 各方向分别登记，不能整体认作当前RC1 |

## 冻结范围

34词卡（9名词／14动词／11形容词）＋19可换镶嵌＝53实体，55流派ID；三种法杖、起始四根、最多四根出战；19图上节点、12遭遇配置，一条通关路径为6普通＋1首领。无首版可获得副词、草法术、雷电新内容、完整召唤、法术产卡产金及局外数值成长。

## 状态分开记录

设计选择Accepted；原26组选择Closed；新AUD-010仍Open。旧TH／CAL是历史限定输入证据。DEMO05的16项局部检查不代表完整规则、平衡、自然通关或真人理解验证。

## 文件清单与维护顺序

[现行文件导航](README.md)是本版正文清单。每个文件有唯一职责，详见[文档合同](../governance/document-contract.md)。历史基线从固定Git提交读取；旧GDD路径已改为兼容导航，不再作为冻结输入。需要冻结测试时必须记录当前设计提交及文件哈希，不能只写“RC1”。

[本次整理清单](../history/reorganizations/2026-09-23-doc1/organization-report.md)记录实际检查、遗留问题和修改文件。

## 目录修订layout.1

2026-09-23项目迁至yanzhou/，主规则在design/，优化在exploration/optimization/。设计基准仍为RC1 / doc.1；目录移动不冻结新的玩法输入。现行文件位置见[目录规范](../governance/directory-layout.md)，原提交路径按[迁移表](../governance/path-map.json)追溯。


## 核心设计浓缩与探索输入READ-1

2026-09-24新增[核心设计](core-design.md)，角色CoreDesignSummary；保留Core Concept v0.6标识，未改变RC1 / doc.1玩法。core-concept.md只作版本入口。探索根现为yanzhou/exploration/，按[启动规范](../exploration/start.md)选择CORE／GDD／FULL／CUSTOM／NONE；读取版本记录于各方向，不因目录或摘要修订自动升级旧方向背景。
