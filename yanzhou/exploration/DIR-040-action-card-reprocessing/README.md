# DIR-040 行动卡结算机制修改和重新定位

日期：2026-10-18。状态：Raw Idea / Unqualified。体验假设：Hypothesis / NotRun。负责人：本方向探索总控（当前会话）。

## 用户目标与原话

以下为2026-10-18用户本轮输入，原文保留：

```text
启动《言咒》的新探索方向：行动卡结算机制修改和重新定位
你担任本方向的探索总控。

目标：
评估完善下列想法，检查目前行动卡相关机制，汇报可能的矛盾点，并推测可能的玩家体验变化

请先读取：
E:/Project/game/yanzhou/exploration/start.md
E:/Project/game/yanzhou/exploration/AGENTS.md

按现有登记分配下一未占用方向编号，在所属方向README中
保留我的原话、阅读范围、探索结论和未决问题。

阅读模式：
采用完整GDD模式，按阅读合同完整读取56份现行GDD文件。
另外纳入以下材料：
- yanzhou/design/core-design.md
- yanzhou/CONTEXT.md
- yanzhou/governance/questions.md
- yanzhou/governance/development-review-2026-10-18.md
- yanzhou/sources/inbox/2026-10-17-standard-card-face.md
- yanzhou/sources/inbox/2026-10-17-minimal-battle-ui.md
- yanzhou/sources/inbox/2026-10-18-development-system-review.md

固定启动时的版本，分批记录实际阅读情况。
其他inbox、探索方向和历史默认不读；需要增补时，
集中说明建议材料及用途。不要通过链接递归扩读。

我的思路：
1.行动卡结算后不消失，可反复进入法器中再生产，实现和资源一样的升级效果
2.新定位：行动卡象征”能释放“，资源卡象征”能生产“，其余不变
3.预期体验：玩家可以不断将王牌法术逐渐增强威力，用同一张卡作为载体，体验更明确
4.设计初衷：行动卡目前结算后就消失，时间轴结算后的左侧部分没有对应价值；我想将重点的UI展示体验回到法器像工厂、流水线一样自动运行，不断加工，因此将行动卡也加入加工体系丰富体验，贴近自走棋（如背包乱斗）的玩家体验；
```

## 本轮阅读范围

- 日期／轮次：2026-10-18 / R1。
- 模式：GDD（完整固定包56份）＋明确增补7份，共63份；逐项版本及实际进度见[阅读记录](reading-log.md)。
- 来源版本：启动时已提交HEAD `2fe5d8f09762f4759df4fc1e8e570ecef21d16ae`；起点工作树干净。本轮后续提交不自动进入来源。
- 增补：用户上列core-design、CONTEXT、questions、development-review及3份inbox，仅这7份。
- 排除与扩读：其他inbox、其他方向正文、历史、外部代码／网页／图片均未授权；禁止递归沿链接扩读。缺口集中列出建议及用途后再由用户决定。
- 操作规则：根AGENTS（用户注入）、yanzhou/AGENTS、exploration/start与AGENTS、探索入口编号／标题、docs/design-workflow、docs/github-collaboration、game-design-workflow/templates/README。仅作路由与流程。
- 方法：game-design-reality-check与grill-with-docs；批量澄清遵守仓库流程，原始想法不转成正式Evaluation。
- 已有范围外背景：编号提取时误带其他3个活动方向的状态摘要，未读正文、不用作证据；详见阅读记录。
- 范围变更：无。
- 原轮覆盖：按同目录阅读记录，63/63份已读；本轮整理仅核对记录一致性，不宣称重新阅读原轮材料。

## 构思与资格初检

用户要保留行动卡结算后的同一载体，使其能再次进入法器加工，以强化王牌法术连续成长与自动流水线的可见体验。行动卡拟表达“能释放”，资源卡拟表达“能生产”。

来源、设计对象、预期价值已明确；卡牌状态、回流方式、升级代价、场内／跨场持久范围、与现行结算和资源边界的关系尚为Unknown。先完成允许材料核对，再提出成组澄清。

## 探索结论与未决问题

原轮阅读记录已完成，探索结论与资格确认尚未完成。本方向仍为Raw / Unqualified；2026-11-01仅补齐登记和覆盖说明。后续主系统CORE-067已采用统一卡牌及回收，但本方向未完成的再加工／成长构思不随之晋级；续作须明确核对原固定基线与新规则的关系。没有修改主系统、创建正式提案或启动玩法实验。

