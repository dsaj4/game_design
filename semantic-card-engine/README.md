# Semantic Card Engine

独立的语义卡牌生成引擎实验。它把概念、动作和核心卡语义镜片编译成确定性的卡牌 IR，用于验证“少量共享规律能否产生可解释的组合结果”。

## 状态与边界

- 当前状态：`Experimental MVP / Technical Exploration`
- 设计来源：[概念合成世界模型原始想法](../game-design-workflow/idea-inbox/2026-08-29-semantic-composition-world-model.md)
- 正式素材：[有限、确定且可学习的卡牌语义物理](../game-design-workflow/idea-materials/M-2026-08-30-finite-semantic-card-physics.md)
- 并列技术方向：[离散语义动力学与 Embedding 语义效果场](EXPLORATION-DIRECTIONS.md)
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

## 当前能力

- 概念和动作提供初始语义特征与固定预算。
- 规律通过 `requires -> derives + effect` 单调推演，不删除事实，因此必然终止。
- 核心镜片可以按语义条件重定向效果类型，但不能增加总预算。
- 相同输入、目录版本和核心镜片生成完全相同的卡牌与 SHA-256 内容哈希。
- 材料顺序不影响结果，重复材料保留并提高预算。
- 未知输入、纯行动输入、没有规律命中的组合都会明确失败。

## 运行

在本目录执行：

```powershell
py -3 -m semantic_card_engine validate
py -3 -m semantic_card_engine generate --concept water --action compress --core neutral
py -3 -m semantic_card_engine generate --concept water --action compress --core crown
py -3 -m pytest -q
```

`generate` 输出的 JSON 是候选卡牌 IR。未来可由批量模拟器校验后编译为 Godot 可加载的内容目录。

## 目录

```text
semantic-card-engine/
├── data/catalog.json
├── semantic_card_engine/
│   ├── __init__.py
│   ├── __main__.py
│   └── engine.py
└── tests/test_engine.py
```

## 下一阶段候选

1. 将 Godot 和 `combat-lab` 的卡牌效果统一为同一版 IR。
2. 加入配方图、资源守恒、递归深度和批量胜率验证。
3. 让 AI 只输出结构化候选，再测量自动通过率和人工否决率。
4. 决定生成发生在内容生产期、核心卡诞生时，还是其他非战斗窗口。
