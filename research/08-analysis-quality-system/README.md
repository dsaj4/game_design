# 深度拆解评审与迭代系统

本目录用于评审和迭代深度游戏拆解报告。它与 `research/03-product-case-studies/deep-analysis-writing-system.md` 分离：

- 写作系统回答“怎么写一份深度拆解案”。
- 评审系统回答“这份拆解案是否接近高质量示例，哪里需要迭代”。

本系统服务于 `research/03-product-case-studies/` 中的深度拆解报告，尤其是使用 `research/templates/deep-product-analysis-template.md` 产出的报告。

## 目录结构

```text
research/08-analysis-quality-system/
├── README.md
├── review-rubric.md
├── iteration-protocol.md
├── templates/
│   └── deep-analysis-review-template.md
├── reviews/
└── iteration-logs/
```

## 使用流程

1. 完成一份深度拆解报告初稿。
2. 复制 `templates/deep-analysis-review-template.md` 到 `reviews/`。
3. 按 `review-rubric.md` 对报告打分。
4. 将总分低于 4 分的维度列为必须迭代项。
5. 按 `iteration-protocol.md` 修改报告或写作系统。
6. 将迭代记录写入 `iteration-logs/`。
7. 如果迭代暴露出模板问题，再修改 `research/templates/deep-product-analysis-template.md` 或写作系统文档。

## 质量目标

一份合格的深度拆解报告应达到：

- 总分不低于 40 / 60。
- 没有任何维度低于 3 分。
- “核心循环”“系统联动”“项目转化”三项都不低于 4 分。
- 至少产出 1 条可验证设计假设，或明确说明暂不形成假设的理由。

一份接近 `assets/` 中 docx 示例质量的报告应达到：

- 总分不低于 50 / 60。
- 没有任何维度低于 4 分。
- 至少 5 个维度达到 5 分。
- 结论、证据、图示、系统联动和项目转化能够闭环。

## 输出状态

评审和迭代记录仍然属于 Research 过程材料，不代表报告结论已经 Accepted。

只有当报告中的观察进入设计假设、提案、评估和拟修改流程，并经用户确认后，才可能影响 `game-design-workflow/core-concept.md`。
