# 设计流程与资格规范

状态：现行操作规范 / 2026-09-30。由原根AGENTS的流程收束而来，资格与采纳门槛不变。先按目标项目AGENTS选择W/P和允许材料；以下言咒路径不适用于独立肉鸽。

## 原始输入与素材资格

主系统使用[原始想法模板](../game-design-workflow/templates/idea-template.md)，写入`yanzhou/sources/inbox/YYYY-MM-DD-short-name.md`。探索直接写所属DIR的README，不预建流程目录。保留原话、触发来源、状态Raw Idea / Unqualified和Unknown。

主动使用grill-with-docs，先查允许材料，再一次确认一个关键问题。全部满足以下条件才能晋级：

1. 原始表达和触发来源可追溯。
2. 设计对象或目标GDD章节明确。
3. 玩家情境，或非玩法内容承担的设计功能明确。
4. 玩家行为、可见影响或约束明确。
5. 预期反馈、体验或设计价值明确。
6. 与已有核心、系统、素材的关系明确。
7. 主要未知、下一步验证/决策方法明确。

完整数值和全部制作边界不是入库前提；情绪词、功能名和泛泛愿景不能替代上述字段。信息不足继续Raw；用户选择一个模糊候选也不能跳过资格。通过后按[合格素材模板](../game-design-workflow/templates/qualified-gdd-material-template.md)生成`M-日期-主题.md`并与原始记录双向追踪。主系统放sources/materials，探索放同一DIR。

## 正式GDD

使用[GDD写作要求与模板](../game-design-workflow/templates/gdd-writing-requirements-and-template.md)，明确GDD-0/GDD-1/GDD-2。按本轮阅读授权审查当前规则、决策、问题、已有GDD，以及目标项目正式素材和相关inbox。

- 写到相应章节时给出最相关的素材与Include/Omit/Park建议，不一次倾倒库存。
- 用户采用inbox候选时，先资格确认并晋级，再写正文；模型自行补全的猜测不得写为结论。
- 素材审查表与使用记录双向链接。未读材料明确列缺口，不宣称全量审查。
- 新草案放`yanzhou/sources/gdd-drafts/GDD-日期-主题.md`；Accepted规格在design唯一维护。
- 不使用自由散文替代模板，不创建客户端/代码GDD；引擎、类、函数、脚本、API、编程数据结构、CI、Bug与代码进度不入GDD。
- 代码已实现不使Hypothesis自动变Confirmed；GDD写入不自动修改正式采纳范围。

## 提案、评估与采纳

| 阶段 | 前提与输出 |
| --- | --- |
| Proposal | 来源必须是合格素材；使用提案模板写玩家行为、核心反馈、玩法假设、最小验证、参照与未知；不过早展开全套数值 |
| Evaluation | 有合格来源/提案，使用评估模板判断推荐推进、修改后重评、搁置或不推进；说明动作、反馈、核心取舍、最小原型及可验证风险 |
| Draft Change | 以合格来源和提案/评估为据，列拟增删替换文本、影响、理由及来源；未经明确采纳不修改现行核心 |
| Accepted | 用户确认或既有明确采纳授权后，更新design对应权威页、核心摘要（受影响时）与decision-log；同轮提交推送 |

主系统对应sources/proposals、evaluations、draft-changes；探索正式文件直接放所属DIR。跨探索回写须目标项目复审，目标Draft Change在主系统sources/draft-changes。历史已完成的P/E/D可在history/accepted-design-records保留来源，不因归档新增采纳范围。

## 参考产品与理论

顺手提及产品先保存参照；正式拆解写产品案例，横向比较写比较记录。至少说明核心循环、相关机制、玩家价值、可借鉴结构、雷同风险和可验证假设；不因成功产品就复制系统。项目案例写目标工作区research，通用方法写共享知识。来源可能变化或用户要求最新时联网核实并标注。

理论/文章先登记来源，再用自己的话整理，并回答“它如何改变本项目设计判断”；无法回答时保留学习材料，不直接推进提案。研究不能只堆链接。

## 实现与验证

先确认明确设计来源和规则ID，按目标开发索引进入代码仓库；实现、测试、构建与发布细节留代码仓库。本仓库记录里程碑、范围、证据、阻塞和下一步。偏差、临时替代物单列；试玩观察转研究记录，再决定是否产生设计变更。

没有设计依据先回设计流程；没有执行授权不启动实验。模拟、局部检查与真人体验分别报告，不以历史测试外推新版本，不修改原实验结果。

## 命名与交付

日期用实际YYYY-MM-DD；主题用英文小写、数字和连字符。原始输入无前缀，正式类型用M、GDD、P、E、D、H；共享模板只用[登记清单](../game-design-workflow/templates/README.md)。

每次说明保存位置、Raw/Qualified/GDD/Proposal/Evaluation/Draft Change/Accepted/Parked/Rejected状态及最自然的下一步。保护文件变更必须按[Git规范](github-collaboration.md)提交推送，报告分支和哈希。
