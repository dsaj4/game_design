# 炼金材料卡 · 分批制作与审阅

2026-10-30 · game-002 / main · **AS-G002-039 / 当前ALCHEMY-MATERIAL-CARDS-03**。按用户要求，以护盾首件的正式规格生成炼金配置材料，**每次5张供审阅**。首批同五种材料已有01材料版、02法师互动版与当前03极简元素版，当前总量仍为5/32，余27种Queued。32身份来自[唯一B01材料表](../../sources/materials/M-2026-10-27-alchemy-batch-01.md)§4.1、4.3、4.4，不改配方、卡效或级别。

![极简五张审阅板](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01-minimal-v03/evidence/size-review.png)

**当前：[水、火、土、风、草的极简版](batch-01-minimal-v03/README.md)。** 用户认为旧稿过繁，要求不出现法师，以大形、少色与留白重做；[01材料版](batch-01/README.md)与[02法师互动版](batch-01-mage-v02/README.md)保留比较。新稿PendingReview；序号和名称只在审阅板外，实际卡内无字。[全量队列](queue.json)记录32个身份与批次，不新增材料规则正文。

| 批次 | 材料 | 进度 |
| --- | --- | --- |
| 01 | 水、火、土、风、草 | 01材料／02互动／03极简，PendingReview |
| 02 | 铁、光、影、硫、汞 | Queued |
| 03 | 盐、蒸汽、雾气、草汁、铁砂 | Queued |
| 04 | 辉光、影尘、溶剂、灵液、火种 | Queued |
| 05 | 灵火、晶核、封盐、再生液、醒神露 | Queued |
| 06 | 蚀解液、金刚砂、浮空石、封魔晶、太阳火 | Queued |
| 07 | 雷火核、幽冥火 | Queued |

## 共用规格与来源

保留1024×1536、2:3、底材＋单幅RGBA、中心pivot、不紧裁和默认单图装载；mipmap、无损与straight alpha，卡效／名称／状态由宿主负责。03版按最新要求改用原生SVG暖白净底与细边，符号统一65%居中等比显示，源PNG不改字节；旧纸纹／角饰和人物只保留在历史版。

各版元素均用内置image_gen独立调用5次；03版改为新绘极简符号与原生SVG净底。提示词／源原件／尺寸／SHA／装载包分别沿各版manifest固定，当前见[03版清单](batch-01-minimal-v03/manifest.json)；01／02原图和清单不覆盖。新图像仍需用户审阅；独立Godot检查不能代替主工程接入或真人识别验证。

CUSTOM；材料身份与01输入沿原版固定，当前03版输入为game提交a9fea5965150c4fa161aabc84f6c4a28f229f2df，按用户最新极简要求重设视觉，未输入旧人物或场景图。未扩读全GDD或变更材料身份。11种终末成品是B01另一张表，不计入这32种材料。

原件就地：项目sources备份生成原字节，外部交付工程E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30。PNG／ZIP本机ignored，说明、提示词、队列及清单入Git。归属main，derived-from AS-G002-038，ReadyForScope / PresentLocal仅首批限定技术检查；玩法M资格和规则发行状态保持原义。
