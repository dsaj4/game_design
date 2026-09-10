# 设计决定与后续工作

状态：C01–C08全部已处理；SW01对象范围已采纳，当前推进SW02引用模型。日期：2026-09-10。核心：[Core Concept v0.6](../game-design-workflow/core-concept.md)，证据Hypothesis。

用户确认“均采用推荐决策，数值设计明确重新设计”。[原话与资格记录](../game-design-workflow/idea-inbox/2026-09-10-design-interface-questions.md)、[采纳记录](../game-design-workflow/draft-changes/D-2026-09-10-accept-design-decisions.md)和[确认前建议快照](../../../archive/2026-09-10-game-002-decision-inputs/workspaces/game-002/docs/design-decisions-needed.md)建立完整追溯。

## 已生效处理

| 编号 | 当前决定 | 状态 | 后续工作 |
| --- | --- | --- | --- |
| C01 | 特殊生命变化逐条标注伤害或生命支付；支付不自动算伤害。打断使用独立反馈，取消的释放无正常释放特效；实际发生的无效目标释放仍有特效 | Accepted：分类与反馈边界 | 具体效果及表现出现时填写标注并验证辨识度 |
| C02 | 对象使用战前公开的固定顺序；逐对象检查材料，固定消耗不足只跳过该对象且不部分扣除，其他合法结果保留；完整法术后检查胜负，至少一对象合法结算才计一次成功，合法零值亦可满足 | Accepted：结算规则 | 明确各词义输入，验证多对象结果的可读性 |
| C03 | 保留召唤类型与单位模型；完整召唤指挥流程暂缓。推进时单独设计战前绑定的单位占位和出生位置 | Accepted：暂缓及后续方向 | 具体召唤推进时补齐容量检查、满员行为和公开敌方攻击衔接 |
| C04 | 当前不新增专属引用词卡；若采用C03的战前单位占位，以占位身份记录指向，不自动转向其他单位 | Accepted：当前资源边界与条件方向 | 随C03设计占位生命周期，当前没有完整占位机制 |
| C05 | 法杖起始资源和镶嵌细则后置；公开固定货架、同种候选去重、一层事件响应及每战计数重置仅作届时评议方案 | Accepted：暂缓 | 具体法杖或镶嵌进入设计时明确起点、槽位、持有、获取与触发 |
| C06 | 造卡产出前检查资格、同名额度与效果限制，计数包含已持有及本场待领取卡，仅合法卡进入整体收益包；产金效果明确有限触发或实质成本 | Accepted：产出约束 | 次数、金额、成本与经济循环重新设计并验证 |
| C07 | 继续对象变化的发生、发展与结果描述；BF1–BF3具体环境机制随实际内容重新提出 | Accepted：表现与暂缓范围 | 对象变化描述可继续，机制须局部资格确认 |
| C08 | 实际词卡时间贡献相加用于冷却，释放时长单独设计；数值框架重新建立，所有具体锚点和默认释放长度不作为参数基线 | Accepted：时间含义与数值重设计 | 按[数值任务](numerical-redesign.md)建立目标、参数和逐刻证据 |

## 执行顺序

先依据[已确认的语义世界范围](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)推进引用与具体操作。SW02首先解决新生对象，再逐项明确SW03–SW07；确认结果作为数值重设计输入，随后确定目标节奏、攻防、时间、词表和成长参数，并进行逐刻与跨战验证。具体参数仍须重新建立。

召唤、镶嵌和BF1–BF3按表内触发条件独立推进。暂缓是已经采用的范围决定，具体细则仍为Unknown，不作为当前可执行机制。当前无需再次选择C01–C08；新内容若产生新的冲突，再单独登记。

## 已采纳范围：SW01

用户已确认把实体、部件、材料、属性状态、空间关系与飞行物、敌方攻击、法术冷却等过程纳入可操作对象设计范围；各类按明确能力开放操作，胜负判定、全局结算顺序等基础规则保持固定。状态Accepted / Scope，证据Hypothesis。

来源：[用户确认记录](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)、[正式范围素材](../game-design-workflow/idea-materials/M-2026-09-10-semantic-world-object-scope.md)及[采纳文本](../game-design-workflow/draft-changes/D-2026-09-10-semantic-world-object-scope.md)。决策编号G002-SCOPE-002，范围已写入核心。

范围确认不自动改变当前基础法术的固定目标、位置及循环规则。具体机制仍需回答对象如何被引用、何时能介入、能产生什么变化及付出什么代价。

## 当前资格问题：SW02

推荐保留“点名对象”的固定实例绑定，同时新增“战前固定选择条件、释放时自动匹配当前对象”的条件绑定，让符合条件的新生对象参与法术。两者并存的模型尚待用户确认；本次名单时点、顺序、句式和生命周期的细则也尚未采纳。

[SW02候选](../game-design-workflow/idea-inbox/2026-09-10-semantic-world-object-scope.md)已包含两种方案比较与新生火球、对象同名替换、本次生成及失效等纸面推演。条件绑定会改变当前固定对象集合规则，需用户选择后再局部晋级与采纳。

其余边界继续登记于同一inbox：SW03位置与结构变化、SW04多端点表达、SW05过程与节拍、SW06局部环境机制、SW07配置与资源权限。当前先处理SW02，不要求同时回答全部分支。

## 素材入口

- [接口规则与范围](../game-design-workflow/idea-materials/M-2026-09-10-accepted-design-interfaces.md)。
- [数值重新设计约束](../game-design-workflow/idea-materials/M-2026-09-10-numerical-redesign-constraints.md)。
- [全部正式素材](../game-design-workflow/idea-materials/README.md)。
- [语义世界范围采纳交付](semantic-world-scope-adoption.md)。
