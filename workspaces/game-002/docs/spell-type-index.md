# 法术类型与分类讨论入口

日期：2026-09-11。状态：Accepted / G002-CORE-012；证据Hypothesis。当前任务为类型区分、首批词名归类和按类型组织讨论。

[正式类型素材](../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md)是分类依据，含18词逐项表和26项例句；本页按四类交叉索引，不重复维护另一套词义。具体效果能否执行须另外检查。

| 类型 | 特征 | 代表归类 |
| --- | --- | --- |
| 简易法术 | 省略显式主语 | 获得护甲＝简易＋状态；释放火焰＝简易＋元素 |
| 状态法术 | 名词中出现状态 | 燃烧加倍＝状态；火焰吞噬护甲＝状态＋元素 |
| 元素法术 | 名词中出现火焰、雷电、冰霜等元素 | 释放火焰＝简易＋元素；恶魔释放火焰＝元素＋召唤 |
| 召唤法术 | 名词中出现召唤物 | 召唤恶魔＝简易＋召唤；恶魔释放火焰＝召唤＋元素 |

所有命中类型同时保留。“点燃敌人／冰冻敌人”只有动词表达状态施加、没有状态名词，因此只命中简易；效果结果不反推类型。护甲是已有状态，所以不能把“获得护甲”只归入简易。

## 简易法术

判定只看省略主语，不能按词少、冷却短或伤害低判断，也没有专属的“简易名词”清单。

- 首批省略句：伤害敌人、点燃敌人、冰冻敌人、收集树木（只命中简易）。
- 与状态交叉：熄灭燃烧、解除冰冻状态；用户例句获得护甲。
- 与元素交叉：释放火焰／雷电／冰霜、强化火焰、削弱雷电、抵挡冰霜。
- 与召唤交叉：用户例句召唤恶魔；首批18词本身没有召唤物名词。

后续在本入口讨论省略句的具体操作与可接受名词，实际效果和词卡时间另行设计。显式“我”不算省略；默认语义补全“我”仍保留简易特征。

## 状态法术

首批提供状态特征的名词为燃烧、冰冻状态；已有素材中的护甲同样是状态名词。

- 用户例句：燃烧蔓延、燃烧加倍；两句有显式燃烧主语，类型是状态。
- 首批交叉句：熄灭燃烧、解除冰冻状态，均为简易＋状态。
- 与元素交叉：火焰吞噬护甲，类型是元素＋状态；本次不决定消耗归属或作用结果。
- 与召唤交叉：解除恶魔的燃烧，类型是简易＋状态＋召唤；复合名词需要实际对应词卡。

后续讨论状态名词允许承担的角色、操作和组合。燃烧蔓延／燃烧加倍的名词＋动词简写可作类型示例，完整句法和作用规则尚需在该类内明确；没有因此放开任意语序、传播或其他复杂环境机制。

## 元素法术

首批元素名词为火焰、雷电、冰霜。生成物、宿主状态、已结算效果与演出继续按现行对象范围区分。

- 简易＋元素：释放火焰／雷电／冰霜、强化火焰、削弱雷电、抵挡冰霜。
- 只命中元素的首批表达：火焰点燃敌人、雷电伤害敌人、冰霜冰冻敌人；其中点燃、伤害、冰冻均为动词。
- 元素＋状态：火焰吞噬护甲。
- 元素＋召唤：恶魔释放火焰。

当前采纳这些表达的类型识别；元素如何生成、是否需要后续使用、怎样影响对象及何时结束，按元素类后续具体词义讨论。此前6刻存续、一次使用及强度数字已Parked，不能作为本类的共同规则。

## 召唤法术

首批18词没有召唤物名词；恶魔作为用户明确给出的召唤物例子纳入分类参照，不自动加入正式起始词表。

- 简易＋召唤：召唤恶魔、强化恶魔。
- 召唤＋元素：恶魔释放火焰。
- 简易＋召唤＋状态：解除恶魔的燃烧。

召唤类型不要求实际生成新单位，单独出现召唤动词也不能代替召唤物名词。完整召唤、单位占位、出生位置、容量与指挥继续后置，类型目录不等于恢复该系统制作。

## 通用词与后续讨论方式

首批10个动词：释放、点燃、冰冻、伤害、强化、削弱、抵挡、熄灭、解除、收集。它们结合主语省略及实际名词才形成法术类型，不能分别锁成互斥的类型专属卡。

首批一般对象名词：敌人、树木、石块；它们自身不提供状态、元素、召唤物特征。首批8个名词的分类合计为元素3、状态2、一般对象3。

每次后续讨论依次记录：本次关注类型、完整句子、全部命中类型和理由、涉及词义、已有依据、尚未明确的效果。多类型内容在相关入口共同引用同一条规则，既不复制实体卡成本，也不重复计事件。未指定类型时先从简易类的省略句和可组合词义整理开始。

基础句式、词卡分配、两种绑定、单次名单、共享槽、四阶段和成功/收益规则作为各类共同依据。类型加成、触发或专属数值需要独立设计，不由标签自动产生。

## 当前搁置与后续内容

| 内容 | 当前状态 |
| --- | --- |
| 四类特征、多类型、首批词名与例句分类 | Accepted；26项例句覆盖全部用户示例 |
| 首批具体词效、元素载体、冰冻减伤、有限掉卡 | Parked；仅保留原稿 |
| 首批时间、强度、持续、产出参数及逐刻记录 | Parked；不是默认值或当前验证依据 |
| 普通攻击抵挡、反弹、自动转移细则 | 暂停推进；若后续讨论再按具体句子的类型归档 |
| 完整召唤、复杂传播、镶嵌 | 依既有范围后置 |
| 后续工作 | 按类型逐项形成具体词义；本轮未采纳额外效果与数值 |

首批[词效原稿](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-wording.md)与[纸面记录](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-paper-checks.md)保留追溯。已确认的对象范围和基础执行规则继续有效。

## 来源与交付

[用户原话](../game-design-workflow/idea-inbox/2026-09-11-spell-type-system.md) → [合格素材](../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md) → [提案](../game-design-workflow/idea-proposals/P-2026-09-11-spell-type-system.md) → [评估](../game-design-workflow/evaluations/E-2026-09-11-spell-type-system.md) → [采纳](../game-design-workflow/draft-changes/D-2026-09-11-spell-type-system.md)与[核心](../game-design-workflow/core-concept.md)、[决策记录](../game-design-workflow/decision-log.md)。

正式素材46份，inbox21份。已检查首批18词与原表逐项对应，26项例句分类一致，核心/素材/Draft Change采用一致类型规则，搁置状态与当前入口同步。30份文件严格UTF-8读取通过，检查中未发现坏链接或表格列数问题；没有进行游戏运行、玩家测试或平衡验证。

<details>
<summary>本次同步的30份文件</summary>

- [README.md](../../../README.md)
- [workspaces/game-002/README.md](../README.md)
- [workspaces/game-002/AGENTS.md](../AGENTS.md)
- [workspaces/game-002/CONTEXT.md](../CONTEXT.md)
- [workspaces/game-002/game-design-workflow/core-concept.md](../game-design-workflow/core-concept.md)
- [workspaces/game-002/game-design-workflow/decision-log.md](../game-design-workflow/decision-log.md)
- [workspaces/game-002/game-design-workflow/README.md](../game-design-workflow/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md](../game-design-workflow/idea-materials/M-2026-09-06-spell-types-and-effect-conditions.md)
- [workspaces/game-002/game-design-workflow/idea-materials/README.md](../game-design-workflow/idea-materials/README.md)
- [workspaces/game-002/docs/semantic-world-content-index.md](semantic-world-content-index.md)
- [workspaces/game-002/docs/design-decisions-needed.md](design-decisions-needed.md)
- [workspaces/game-002/docs/numerical-redesign.md](numerical-redesign.md)
- [workspaces/game-002/docs/control-center.md](control-center.md)
- [workspaces/game-002/docs/README.md](README.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/README.md](../game-design-workflow/idea-inbox/README.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-object-catalog.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-ability-word-catalog.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md](../game-design-workflow/idea-inbox/2026-09-10-semantic-sentence-cases.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-element-state-drop-wording.md](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-wording.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-10-element-state-drop-paper-checks.md](../game-design-workflow/idea-inbox/2026-09-10-element-state-drop-paper-checks.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/README.md](../game-design-workflow/idea-proposals/README.md)
- [workspaces/game-002/game-design-workflow/evaluations/README.md](../game-design-workflow/evaluations/README.md)
- [workspaces/game-002/game-design-workflow/draft-changes/README.md](../game-design-workflow/draft-changes/README.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md](../game-design-workflow/idea-materials/M-2026-09-05-battle-state-persistence.md)
- [workspaces/game-002/game-design-workflow/idea-inbox/2026-09-11-spell-type-system.md](../game-design-workflow/idea-inbox/2026-09-11-spell-type-system.md)
- [workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md](../game-design-workflow/idea-materials/M-2026-09-11-spell-type-system.md)
- [workspaces/game-002/game-design-workflow/idea-proposals/P-2026-09-11-spell-type-system.md](../game-design-workflow/idea-proposals/P-2026-09-11-spell-type-system.md)
- [workspaces/game-002/game-design-workflow/evaluations/E-2026-09-11-spell-type-system.md](../game-design-workflow/evaluations/E-2026-09-11-spell-type-system.md)
- [workspaces/game-002/game-design-workflow/draft-changes/D-2026-09-11-spell-type-system.md](../game-design-workflow/draft-changes/D-2026-09-11-spell-type-system.md)
- 本页

</details>

本轮进入前已有两份语法与显式主语素材的本地修改，保留原样且不纳入本次提交；本次未回填它们移除的具体词效表述。
