# 言咒现行设计

Project ID：game-002。文档角色：Navigation。更新：2026-10-05。当前GDD 2.1 / TL-1 + INS-1 / processing.2 + timing.1，GDD-0；已采纳核心结构，内容与完整参数尚未闭合。

[核心设计](core-design.md) · [GDD总览](GDD.md) · [版本与旧版取证](baseline.md) · [当前问题](../governance/questions.md)

| 文档 | 维护内容 |
| --- | --- |
| [SYS-001](systems/01-grammar.md) | 法器暗句、核心／辅槽铭刻、兼容与卡牌类别 |
| [SYS-002](systems/02-wands.md) | 统一行动输出、处理与容量预留、路由与返工 |
| [SYS-003](systems/03-combat.md) | 战斗行、敌方倒计时、时序、伤害和胜负 |
| [SYS-004](systems/04-elements-environment.md) | 环境资源、转化、维护与产物；旧文件名保留定位 |
| [SYS-005](systems/05-route-encounters.md) | 遭遇程序与路线接口 |
| [SYS-006](systems/06-rewards-growth.md) | 战中与战外资源、获取、辅槽打造和成长边界 |
| [SYS-007](systems/07-interaction-save.md) | 可操作信息、暂停、保存与干涉系统边界 |
| [卡表](content/cards.md) | 新卡表设计合同与候选入口 |
| [法器](content/wands.md) | 法器暗句、槽位、契合与内容合同 |
| [敌人与遭遇](content/enemies-encounters.md) | 敌牌内容字段与迁移状态 |
| [参数](parameters.md) | 单位、已定约束与未定数值 |
| [验收](validation.md) | 新版规则、体验任务与停止条件，全部NotRun |
| [素材审查](source-review.md) | 纳入、替代、重设计与原始来源边界 |

旧RC1数字、空间规则与验收用例不再从本目录的“当前”身份继承；需要追溯时读固定旧提交。

兼容材料已按[CORE-048](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)补入TL-26–37（文档修订reuse.1）：构句／对象／支付、单向路线、库存与节点选择、保存及数量合同。使用旧材料时先核对[逐来源适用表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)，不从历史正文补入未定新参数。

INS-1按[CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)采纳TL-38–45；替代完整自由构句、TL-20入口与法器直接资源交付，明确主辅槽和行动输出。未决卡效、打造费用与契合形式不因本次回写变成已定规则。

2026-10-04局部修订routing.1按[CORE-050](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md)明确全敌牌正延迟、未承诺批次的临时供料优先级及供料调时；成品争入行仍用战前法器序。GDD版本与成熟度不变。

局部修订processing.1按[CORE-051](../sources/draft-changes/D-2026-10-05-single-processing-time.md)采用唯一处理耗时D≥1整数拍，取消J／R／周期／冷却／S；开工预留容量、无位不开工、完成即入行。旧完工等位已替代。

processing.2按[CORE-052](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)补齐五项接口：预留不排牌序、按有效供料优先级联合检查开工条件、中断回收下拍可用、入行最早下拍翻开、单份临时供料在指定结束拍恢复基础方案。完整同拍时序、多牌批次和实际内容仍待补齐，GDD仍2.1／GDD-0。

timing.1按[CORE-053](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md)补齐拍末开工、a+D、正常空位复用、揭示后输入窗口及补给可用拍。阶段一文档完成，见[收束包](../sources/inbox/2026-10-05-stage-one-closure.md)；复杂总序及真实内容继续按阶段二至四处理，GDD-0／NotRun不变。
