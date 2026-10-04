# 铭文、法器与行动内容的审查流程

Project ID：game-002。文档角色：WorkflowGuide。2026-10-04 / TL-1 + INS-1。现行内容接口见[卡表合同](../design/content/cards.md)，资格与采纳沿[统一流程](../../docs/design-workflow.md)。本页不是第二套GDD模板，也不自动授权测试。

## 设计单元

铭文提供已声明词义；法器给出暗句、核心兼容与辅槽预设挂接；合法配置产生独立设计的行动效果。FX只追踪效果身份，不凭名称授予权限。一次可处理少量法器／铭文及代表组合，不要求填满全池。旧自由构句、19镶嵌、GR整包和13词／4资源／4行动候选均不作为现行设计起点。

## 流程与出口

| 阶段 | 工作与出口 |
| --- | --- |
| 原始记录 | 用户原话、设计对象、拟影响的玩家选择与Unknown；主系统进入sources/inbox，使用[原始想法模板](../../game-design-workflow/templates/idea-template.md) |
| 资格确认 | 使用grill-with-docs先查允许材料，再按项目批量澄清；七项资格完整才晋级[合格素材](../../game-design-workflow/templates/qualified-gdd-material-template.md) |
| 提案／评估 | 按[提案](../../game-design-workflow/templates/proposal-template.md)与[评估](../../game-design-workflow/templates/evaluation-template.md)写机制、反馈、代价、反例及最小验证；不把猜测变已定参数 |
| 采纳 | [Draft Change](../../game-design-workflow/templates/draft-change-template.md)列具体增删、理由和影响；明确采纳后同步权威design、必要摘要及decision-log；旧授权只在原范围生效 |
| 验证准备 | 冻结限定输入、同预算对照、正常与失败路径；[交接](../development/test-handoff.md)保持Draft／NotRun直到就绪，执行须有具体实验任务授权 |

设计Accepted与验证通过分别记录，不要求先有测试才能采纳明确的结构。完整GDD仍用[登记模板](../../game-design-workflow/templates/gdd-writing-requirements-and-template.md)。

## 每个组合的必要核对

- 法器暗句、必填核心、合法／非法铭文及器具能力；至少给能说明兼容边界的正反例，有限词池注明覆盖限制。
- 核心行动、可选辅槽与契合分别改变什么；预设挂接、专属替代通用、多修饰次序及实际来源，不用未决附效填满表格。
- 真实铭文实体、法器、获取渠道和机会成本；初始可表达性与沿途取得机会分别核对，未获组件不能当免费拥有。
- 制造映射、整批托管、加工／交付／休歇、批次张数、队列占用与生效截止；法器统一行动输出，资源获取途径须明示。
- 卡效目标及选择优先级、实例／条件、名单与失效、效果支付、零值、完整事件和有限触发；不套旧格子或冷却。
- 实际资源若有维护／增幅／携带，分别声明争料、休眠、生命周期及战终归属；不能由接口倒推生产权限。
- 正常场景、缺组件／缺料、满行、失去目标、来源死亡、终局及保存恢复的结果；设计未决就保留Unknown。

不涉及的字段写“不适用”，不为填表新增机制。流派比较需说明在什么压力下选择不同方案，保留获取失败、无用奖励和队列堵塞的路径；不靠换名或同预算只增加效果宣称深度。

## 效果追踪与回流

效果讨论按既有工作流查重并登记身份、修订、来源和缺项；同时检查引用它的内容及[覆盖](../effects/case-coverage.md)。未选或历史效果不自动进入现行卡池，FX不足以替代资格。当前未决统一进[问题](questions.md)，代码偏差留外部实现及开发索引，实测只更新其实际覆盖范围。

[清理前工作流](https://github.com/dsaj4/game_design/blob/e9b2a8fa7c88e9a34ab6e9a37b4cf05daecf89a4/yanzhou/governance/card-review-workflow.md)保留旧GR、镶嵌与测试批次语境，不以旧阶段建议生成新版待办。
