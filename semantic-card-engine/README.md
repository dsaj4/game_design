# Semantic Card Engine

独立的语义卡牌生成引擎实验。它把概念、动作和核心卡语义镜片编译成确定性的卡牌 IR，用于验证“少量共享规律能否产生可解释的组合结果”。

## 状态与边界

- 当前状态：`Verified MVP / EXP-002 V0 Implemented`
- 设计来源：[概念合成世界模型原始想法](../game-design-workflow/idea-inbox/2026-08-29-semantic-composition-world-model.md)
- 正式素材：[有限、确定且可学习的卡牌语义物理](../game-design-workflow/idea-materials/M-2026-08-30-finite-semantic-card-physics.md)
- 效果约束素材：[有限效果区域与可拒绝合成](../game-design-workflow/idea-materials/M-2026-08-30-bounded-semantic-effect-regions.md)
- 并列技术方向：[离散语义动力学与 Embedding 语义效果场](EXPLORATION-DIRECTIONS.md)
- 技术架构与实验 ADR：[ARCHITECTURE.md](ARCHITECTURE.md)
- 本目录不是 GDD，也不表示该想法已经成为正式玩法或核心构思。
- 当前不调用 AI，不生成或执行任意代码，不直接接入 Godot。
- 临时概念、规律、预算和核心镜片只用于验证技术闭环。

## 最小架构

```text
data/catalog.json
  -> 目录校验
  -> 单调前向语义推演
  -> 核心卡镜片重定向
  -> 固定预算分配
  -> 规范化卡牌 IR + 内容哈希
```

AI 后续只能在这个闭环之前生成候选概念事实、规律或 IR；运行时执行层仍只接受白名单操作。真正新增效果操作码需要显式扩展引擎和测试。

并列实验采用另一条隔离管线：

```text
data/experiment.json
  -> 8 概念 × 3 行动 × 2 核心卡
  -> 离散语义动力学 / 角色感知冻结向量
  -> 共享语义候选
  -> 容量约束的全局最小代价分配
  -> 单效果 / 兼容双效果 / unmapped
  -> card-ir-v0 + 完整比较报告
```

## 当前能力

- 概念和动作提供初始语义特征与固定预算。
- 规律通过 `requires -> derives + effect` 单调推演，不删除事实，因此必然终止。
- 核心镜片可以按语义条件重定向效果类型，但不能增加总预算。
- 相同输入、目录版本和核心镜片生成完全相同的卡牌与 SHA-256 内容哈希。
- 材料顺序不影响结果，重复材料保留并提高预算。
- 未知输入、纯行动输入、没有规律命中的组合都会明确失败。
- `EXP-002 V0` 对两条路线使用相同的 48 个输入和发布约束，共输出 96 条可审计结果。
- 区域分配保留原始向量、候选分数、投影点、投影距离、合法区域和拒绝原因。
- 效果区域总容量小于候选数，因此测试会真实覆盖 `capacity_exhausted -> unmapped`，而不是只测试理论分支。
- Embedding 路线当前使用版本化人工冻结向量，只验证连续空间与分配机制，不代表真实模型已经具备零样本语义理解。

## 运行

在本目录执行：

```powershell
py -3 -m semantic_card_engine validate
py -3 -m semantic_card_engine generate --concept water --action compress --core neutral
py -3 -m semantic_card_engine generate --concept water --action compress --core crown
py -3 -m semantic_card_engine compare --output reports/semantic-physics-exp-002.json
py -3 -m pytest -q
```

`generate` 输出的 JSON 是候选卡牌 IR。未来可由批量模拟器校验后编译为 Godot 可加载的内容目录。

## 目录

```text
semantic-card-engine/
├── ARCHITECTURE.md
├── EXPLORATION-DIRECTIONS.md
├── data/catalog.json
├── data/experiment.json
├── reports/semantic-physics-exp-002.json
├── semantic_card_engine/
│   ├── __init__.py
│   ├── __main__.py
│   ├── engine.py
│   └── experiment.py
└── tests/
    ├── test_engine.py
    └── test_experiment.py
```

## 下一阶段候选

1. 用固定的真实 Embedding 模型替换人工冻结向量，并缓存模型 ID、定义模板和输出向量。
2. 加入加权平均基线与结构化句向量基线，和当前角色感知路线做盲测。
3. 让评审者对 96 条结果标注语义合理性与可预测性，区分算法通过和玩家认可。
4. 将 Godot 和 `combat-lab` 的卡牌效果统一为同一版 IR，再进行批量战斗预算验证。
