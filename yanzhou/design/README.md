# 言咒现行设计

Project ID：game-002。文档角色：Navigation。更新：2026-10-08（文档拆分）。当前GDD 2.1 / TL-1 + INS-1 / processing.2 + timing.1 + enemy.1，GDD-0；已采纳核心结构，内容与完整参数尚未闭合。

[核心设计](core-design.md) · [GDD总览](GDD.md) · [版本与旧版取证](baseline.md) · [当前问题](../governance/questions.md)

| 文档 | 维护内容 |
| --- | --- |
| [法器系统](systems/artifact-system/README.md) | 法器本体、处理流程、供料编排、容量预留、打断返工与契合接口；既有规则与待定内容分别保留 |
| [铭文系统](systems/inscription-system/README.md) | 铭文实体、核心装配、兼容与挂接，包含辅槽子系统；既有规则；辅槽新增通用框架仍为 Qualified |
| [行动卡系统](systems/action-card-system/README.md) | 卡牌类别、行动效果、战斗行与共同结算，包含标记子系统；既有规则；标记细则待按阶段成果整理 |
| [敌人系统](systems/enemy-system/README.md) | 敌人程序、遭遇输入、敌方行动与应对窗口；既有规则与设计目标分别保留 |
| [资源系统](systems/resource-system/README.md) | 材料、供给、托管、维护、转化与数量合同；既有规则与待定内容分别保留 |
| [局外成长系统](systems/meta-progression-system/README.md) | 预留独立系统入口；范围、机制与持续性均待设计；尚未开发；仅占位 |
| [公共流程与合同](common/README.md) | 局内路线、局内经济、交互与保存；沿用既有规则 |
| [卡表](content/cards.md) | 新卡表设计合同与候选入口 |
| [法器](content/wands.md) | 法器暗句、槽位、契合与内容合同 |
| [敌人与遭遇](content/enemies-encounters.md) | 敌牌内容字段、首版约束、表现方向与首批候选 |
| [参数](parameters.md) | 单位、已定约束与未定数值 |
| [验收](validation.md) | 新版规则、体验任务与停止条件，全部NotRun |
| [素材审查](source-review.md) | 纳入、替代、重设计与原始来源边界 |

当前按六个主系统组织，辅槽归铭文、标记归行动卡，局外成长仅预留目录。每个目录以 rules、experience、design 分别维护规则、体验假设和设计，README 负责导航；公共流程另存。目录调整不改变原规则采纳和验证状态。

旧RC1数字、空间规则与验收用例不再从本目录的“当前”身份继承；需要追溯时读固定旧提交。

兼容材料已按[CORE-048](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md)补入TL-26–37（文档修订reuse.1）：构句／对象／支付、单向路线、库存与节点选择、保存及数量合同。使用旧材料时先核对[逐来源适用表](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-028-timeline-depth/compatible-rules-reuse.md)，不从历史正文补入未定新参数。

INS-1按[CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)采纳TL-38–45；替代完整自由构句、TL-20入口与法器直接资源交付，明确主辅槽和行动输出。未决卡效、打造费用与契合形式不因本次回写变成已定规则。

2026-10-04局部修订routing.1按[CORE-050](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md)明确全敌牌正延迟、未承诺批次的临时供料优先级及供料调时；成品争入行仍用战前法器序。GDD版本与成熟度不变。

局部修订processing.1按[CORE-051](../sources/draft-changes/D-2026-10-05-single-processing-time.md)采用唯一处理耗时D≥1整数拍，取消J／R／周期／冷却／S；开工预留容量、无位不开工、完成即入行。旧完工等位已替代。

processing.2按[CORE-052](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)补齐五项接口：预留不排牌序、按有效供料优先级联合检查开工条件、中断回收下拍可用、入行最早下拍翻开、单份临时供料在指定结束拍恢复基础方案。完整同拍时序、多牌批次和实际内容仍待补齐，GDD仍2.1／GDD-0。

timing.1按[CORE-053](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md)补齐拍末开工、a+D、正常空位复用、揭示后输入窗口及补给可用拍。阶段一文档完成，见[收束包](../sources/inbox/2026-10-05-stage-one-closure.md)；复杂总序及真实内容继续按阶段二至四处理，GDD-0／NotRun不变。

enemy.1按[CORE-054](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)确定敌程序固定时间表与翻开表公开、打断锁定剩余最长施法、单一来源敌人死亡即胜、同拍敌方到期先于玩家行动及四类通用卡面种类；首批敌人为候选，见[阶段二工作包](../sources/inbox/2026-10-05-stage-two-enemy-pressure.md)。GDD-0／NotRun不变。
