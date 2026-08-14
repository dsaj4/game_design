# 游戏视频拆解实验室

状态：Prototype Lab

这个目录是一个隔离开发区，用来验证“游戏视频 / 图片 / 文本材料 -> 高质量游戏拆解案”的新工作流。它暂时不并入 `research/` 的正式案例系统，也不修改现有核心构思文档。

## 当前目标

第一阶段先不接入真实视频分析，也不依赖 BiliSum 任务库。验收目标是：

- 输入一组图片和文本材料。
- 输出一份结构完整、证据可追溯、面向策划讨论的游戏拆解稿。
- 同时输出一个可交给多模态模型继续润色或重生成的分析任务包。
- 用质量检查清单验证报告是否覆盖核心定位、玩家体验、核心循环、系统架构、内容节奏、经济闭环、叙事包装和项目转化。

## 为什么先做隔离目录

BiliSum 已经具备视频转写、截图理解、VLM 图文笔记和 Markdown 导出能力。这个实验室只验证“游戏拆解总结模式”的信息结构和输出质量，不直接改 BiliSum 代码。

等效果过关后，可以把这里的素材包协议和提示词迁移为 BiliSum 的一种总结模式：

```text
BiliSum 视频任务
  -> 转写文本
  -> 关键帧 / 截图
  -> VLM 图文笔记
  -> 游戏拆解素材包
  -> 游戏拆解稿
```

## 目录结构

```text
media-analysis-lab/
  README.md
  architecture.md
  acceptance.md
  schemas/
    material-pack.schema.json
  templates/
    game-analysis-dossier-template.md
  prompts/
    game-analysis-dossier.md
  tools/
    build_analysis_packet.py
  examples/
    core-card-duel/
      materialpack.json
      materials.md
      images/
        battle-layout.svg
```

## 快速运行

在仓库根目录执行：

```powershell
py -3 media-analysis-lab/tools/build_analysis_packet.py `
  --pack media-analysis-lab/examples/core-card-duel/materialpack.json `
  --out media-analysis-lab/examples/core-card-duel/dist `
  --check
```

运行后会生成：

- `core-card-duel-analysis-packet.md`：可交给 LLM / VLM 的完整任务包。
- `core-card-duel-draft.md`：基于素材包生成的拆解稿初稿。
- `core-card-duel-quality-check.md`：覆盖度与质量门槛检查。

## 当前边界

- 不下载视频。
- 不调用真实 VLM / LLM。
- 不读取 BiliSum 数据库。
- 不把结论写入 `core-concept.md`。
- 输出状态仍是 Research / Prototype Lab，不是 Accepted。

## 下一步

1. 用真实游戏截图和游玩记录替换示例素材。
2. 对比人工拆解稿，调整素材字段和提示词。
3. 增加 BiliSum 导出适配器：把 `visual-note.md`、转写和截图目录转换为 `materialpack.json`。
4. 再考虑接入模型调用，生成最终长文。
