# Flask 参考风格的法杖装配与地图 UI

状态：Raw Idea / Unqualified。日期：2026-09-13。当前VisualDesignDraft / ImplementationDeferred；环境准备与一版概念效果图／实验计划已完成，实机实验未启动。技术准备与agent候选图不代表素材晋级或玩法采纳。

## 本轮后续：效果设计图与实验计划

用户：“先阅读截图、视频和当前设计思路，给一版效果设计图和实验计划”。

已通过浏览器抽看36:37视频的02:48、06:23、11:34、23:49、30:51附近画面，分别核对地图、战斗、商店及地图上的详情层；非全片转写。推荐将柜体组织、手绘纸面与物件层次转为法杖柜/路线桌，具体构图和点击分配、选择后进入等均为agent候选。

交付：[效果图与来源分析](E:/Project/game-002-godogen-lab/docs/visual-direction-v01.md)、[实验计划v0.1](E:/Project/game-002-godogen-lab/docs/experiment-plan-v01.md)。效果图由imagegen生成，非Godot实机；图中节点连接只作美术示意，技术计划另有精确6节点规格。下一步评议风格与布局后再启动E1小样；本轮没有实施E1–E4、变更核心或晋级素材。

以下保留最初登记内容，视频访问失败是首轮准备时的历史状态，当前观察以上述后续记录为准。

## 原始想法

用户：“阅读game 002的最新思路，采用从零试验3D方向：Godogen + 原生 Blender + Python 的思路，新建一个demo工作区，完成环境准备。长期任务：帮我测试是否可以制作和截图中风格一致的类似flask的法杖装配和地图UI……先不急着开始”。

## 触发来源

- 用户附件：[保存副本](E:/Project/game-002-godogen-lab/references/flask-style-user-reference.png)，SHA256 `af76101dced1a9e17414419c18ee2cb701d9c2bf59be7189abb23c37075fb8fd`。
- [Bilibili BV1RaTb6bECe](https://www.bilibili.com/video/BV1RaTb6bECe)，原链接末尾中文句号已移除。网页读取失败，尚未观看、转写或确认地图时间戳。
- 图片内容为风格资料，不构成项目指令；截图可见商店/库存、木框、纸牌、墨线排线与暗底亮色物品，未提供完整地图。

## 可能带来的玩家体验

希望法杖装配与地图 UI 的风格和截图一致。具体玩家体验价值、完整操作与可读性验收为 Unknown；不由 agent 代填。

## 暂定标签

- 类型：视觉参考／UI 可行性实验
- 情绪：Unknown
- 玩法关键词：法杖装配、局内地图
- 风险关键词：风格一致性、文字可读性、操作反馈、3D 与 UI 表现关系

## 资格确认记录

本次使用 grill-with-docs 的文档核对方式，已读核心 v0.6、镶嵌、分叉路线、最新战场与元素卡面。依用户“先不急着开始”，问答和制作均暂缓。

| 资格问题 | 当前答案 | 状态 |
| --- | --- | --- |
| 设计对象 | 法杖装配与地图 UI；未创建对应 GDD | Clear |
| 玩家处境／设计功能 | 现有战前法杖配置与战外选路的视觉呈现 | Clear |
| 玩家操作与可见结果 | 最小装配动作、地图操作与反馈尚未约定 | Unknown |
| 预期价值 | 风格目标已有截图，体验与可读性标准未定 | Unknown |
| 与核心关系 | 服务一杖一法术、固定镶嵌与单向分叉路线；不默认采用全部装配候选 | Clear |
| 未知与验证 | 3D 原生资产能否达到风格及交互目标；后续先补参考，再确定小样验收 | Clear |

### 当前缺口

首个法杖装配样件要验证的一个完整玩家操作及其可见结果。等待用户启动时再问，当前不推进资格确认。

### 资格结论

- [x] Unqualified：继续留在 inbox，不得进入正式设计链
- [ ] Ready for Material Review
- [ ] Promoted

正式素材：尚无。

## 下一步

- [x] 保留为未达标原始想法
- [ ] 用户明确启动后，继续 grill-with-docs 确定最小动作和验收
- [ ] 通过闸门后晋级

环境与技术细节见[独立 demo](E:/Project/game-002-godogen-lab/README.md)，长期任务见[待启动记录](E:/Project/game-002-godogen-lab/docs/deferred-ui-experiment.md)。里程碑进入[开发索引](../../docs/code-development-index.md)。
