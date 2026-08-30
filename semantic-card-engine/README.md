# Semantic Card Engine

独立的语义卡牌生成引擎实验。它把概念、动作和核心卡语义镜片编译成确定性的卡牌 IR，用于验证“少量共享规律能否产生可解释的组合结果”。

## 状态与边界

- 当前状态：`Verified MVP / EXP-002 V1 Human Review Pack Ready`
- 设计来源：[概念合成世界模型原始想法](../game-design-workflow/idea-inbox/2026-08-29-semantic-composition-world-model.md)
- 正式素材：[有限、确定且可学习的卡牌语义物理](../game-design-workflow/idea-materials/M-2026-08-30-finite-semantic-card-physics.md)
- 效果约束素材：[有限效果区域与可拒绝合成](../game-design-workflow/idea-materials/M-2026-08-30-bounded-semantic-effect-regions.md)
- 并列技术方向：[离散语义动力学与 Embedding 语义效果场](EXPLORATION-DIRECTIONS.md)
- 技术架构与实验 ADR：[ARCHITECTURE.md](ARCHITECTURE.md)
- 本目录不是 GDD，也不表示该想法已经成为正式玩法或核心构思。
- 默认比较和运行时不调用模型，不生成或执行任意代码，不直接接入 Godot。
- 只有显式执行 `build-embeddings` 时才下载固定修订版模型并重建缓存；发布比较只读取缓存。
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
data/experiment.json + data/embedding-cache.json
  -> 8 概念 × 3 行动 × 2 核心卡
  -> 离散动力学 / 人工向量 / 真实向量三种组合基线
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
- `EXP-002 V1` 对五条路线使用相同的 48 个输入和发布约束，共输出 240 条可审计结果。
- 区域分配保留原始向量、候选分数、投影点、投影距离、合法区域和拒绝原因。
- 效果区域总容量小于候选数，因此测试会真实覆盖 `capacity_exhausted -> unmapped`，而不是只测试理论分支。
- 真实 Embedding 缓存固定到 `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` 的提交 `e8f8c211...`，许可证为 Apache-2.0，共保存 78 条、384 维规范化向量。
- 缓存记录每段输入文本、文本哈希、构建库版本和整体摘要；定义变化、内容篡改或缓存缺失都会拒绝运行，不会静默退回人工向量。
- 固定种子可从 V1 报告生成三阶段盲态评审包：48 条事前预测、240 条匿名语义评分和 80 组动作对照；路线身份只保存在独立解盲密钥中。
- 公开评审表使用带 BOM 的 UTF-8 CSV，默认拒绝覆盖已存在文件，避免误删评审者已经填写的数据。

## V1 初步结果

| 路线 | 映射 | `Unmapped` | 双效果 | 当前解释 |
| --- | ---: | ---: | ---: | --- |
| 离散语义动力学 | 39 | 9 | 4 | 通用状态变换对照 |
| 人工角色向量 | 41 | 7 | 5 | V0 连续空间对照，不代表真实模型 |
| 真实向量加权平均 | 0 | 48 | 0 | 全部低于合法距离/分数门槛，基线失败 |
| 真实向量角色提示 | 32 | 16 | 4 | 角色文本显著恢复映射能力 |
| 真实向量结构化句子 | 38 | 10 | 2 | 当前覆盖最好，仍需人工判断语义是否合理 |

没有为了让加权平均“看起来可用”而降低合法性阈值；失败结果作为基线证据保留。

## 运行

在本目录执行：

```powershell
py -3 -m semantic_card_engine validate
py -3 -m semantic_card_engine generate --concept water --action compress --core neutral
py -3 -m semantic_card_engine generate --concept water --action compress --core crown
uv run --python 3.12 --extra embedding-build python -m semantic_card_engine build-embeddings
py -3 -m semantic_card_engine compare --output reports/semantic-physics-exp-002-v1.json
py -3 -m semantic_card_engine compare --manual-only
py -3 -m semantic_card_engine build-review-pack
py -3 -m pytest -q
```

`build-embeddings` 是可选的内容生产命令；缓存已存在时，`compare` 和测试不需要安装 PyTorch 或 SentenceTransformers。

`build-review-pack` 默认读取 V1 报告并生成到 `reports/semantic-physics-exp-002-v1-human-review/`。评审者必须按 `README.md` 顺序填写；完成全部评审前不得查看 `private-blind-key.json`。只有确认尚未写入人工结果时，才可显式使用 `--overwrite` 重建。

`generate` 输出的 JSON 是候选卡牌 IR。未来可由批量模拟器校验后编译为 Godot 可加载的内容目录。

## 目录

```text
semantic-card-engine/
├── ARCHITECTURE.md
├── EXPLORATION-DIRECTIONS.md
├── data/catalog.json
├── data/embedding-cache.json
├── data/experiment.json
├── reports/semantic-physics-exp-002.json
├── reports/semantic-physics-exp-002-v1.json
├── reports/semantic-physics-exp-002-v1-human-review/
│   ├── 01-prediction.csv
│   ├── 02-semantic-fit.csv
│   ├── 03-action-contrast.csv
│   ├── private-blind-key.json
│   └── README.md
├── semantic_card_engine/
│   ├── __init__.py
│   ├── __main__.py
│   ├── embedding_cache.py
│   ├── engine.py
│   ├── experiment.py
│   └── human_review.py
├── uv.lock
└── tests/
    ├── test_engine.py
    ├── test_experiment.py
    └── test_human_review.py
```

## 下一阶段候选

1. 让至少 3 名评审者按盲态协议填写评审包，再解盲计算各路线的预测命中率、语义评分、拒绝准确性和评审者一致性。
2. 加入同义改写和反义/动作替换输入，检查真实模型是否只会按表面词汇聚类。
3. 比较另一种固定中文/多语 Embedding，判断当前结果是模型特性还是方法特性。
4. 将通过人工评审的路线接入共享 IR 和批量战斗预算验证。
