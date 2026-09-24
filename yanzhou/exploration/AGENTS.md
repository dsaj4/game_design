# 言咒探索：按方向保存

Project ID：game-002-optimization；P = yanzhou/exploration/。layout.2 / 2026-09-24。用户明确要求简化内部结构；本文件的存储映射优先于根手册及共享探索规则的旧流程目录映射。资格门槛、来源隔离、Git保护仍适用。

## 默认操作

先读P/README.md，选择一个方向文件夹，再读其README和明确需要的来源。这里不采用父级主系统默认读取清单，不自动读取其他方向、主系统全文、独立肉鸽或旧游戏。用户指定当轮RC1背景时登记固定提交和来源范围；没有指定时沿该方向已有基准，新方向使用登记的旧固定包，不凭最新日期自行换背景。

## 最小存储

- 一个独立方向使用`DIR-NNN-short-name/README.md`；同方向补充直接更新，不为一次聊天重复建方向。
- README保存构思、玩家行为与取舍、与主系统的关系、未知与下一步、来源/日期/状态。有不同互斥思路时明确列出，尚未选择就保留未选择。
- 原始输入、澄清和轻量研究记录先留在方向页；默认Raw Idea / Unqualified。新增方向分配不复用的编号，并在P/README增加一行。只有确需比较时才更新comparison.md。
- 图片或长篇支撑材料按实际需要直接放同一方向文件夹；不预建inbox、materials、proposals、evaluations、questions、runs、gdd等流程树，也不维护第二份机器方向注册表。
- 正式资格确认仍使用grill-with-docs和根登记模板。若确实形成合格素材、Proposal、Evaluation或GDD，将带类型/日期/ID的独立文件直接放所属方向内，由README链接；Raw正文不可直接冒充正式材料。日常构思不要求先生成这些文件。
- 原有27方向的摘录是DirectionNote；DIR-003、008只保留既有局部资格与采纳差异，其余保持Raw。研究建议、规划测试与真实结果分开，未指定实验任务不自动运行测试。

## 历史与回写

[整理前档案](../history/exploration-2026-09-24/README.md)承接旧流程记录。[固定背景包](../history/exploration-2026-09-24/context/baseline-2026-09-09-001/context-pack.md)及manifest原样保留；旧脚本、预算、待办、AGENTS与“当前”不构成现用命令。未来生成背景包须另有明确任务与完整来源配置，不能直接执行历史脚本更新当前目录。

普通任务只写所选方向及必要索引。回写主系统必须有合格来源、提案/评估、差异及目标项目复审，目标Draft Change放yanzhou/sources/draft-changes；明确采纳后才改design并登记决策和比较表中的吸收范围。物理同属yanzhou不扩大权限。

暂停方向标Parked并保留，不删除失败路径。保护文档改动同轮提交推送，只暂存本任务文件。
