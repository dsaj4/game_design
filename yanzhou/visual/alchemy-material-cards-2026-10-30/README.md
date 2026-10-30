# 炼金材料卡 · 分批制作与审阅

2026-10-30 · game-002 / main · **AS-G002-039 / ALCHEMY-MATERIAL-CARDS-01**。按用户要求，以护盾首件的正式规格生成炼金配置材料，**每次5张供审阅**。完整材料范围为B01的32种；本轮实际完成首批5张，余27种已入队，未标为已完成。32身份来自[唯一B01材料表](../../sources/materials/M-2026-10-27-alchemy-batch-01.md)§4.1、4.3、4.4，不改配方、卡效或级别。

![首批五张审阅板](E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30/batch-01/evidence/size-review.png)

**本批：[水、火、土、风、草的源件、交付与检查](batch-01/README.md)。** 新成图PendingReview；序号和名称只在审阅板外，实际卡内无字。[全量队列](queue.json)记录32个身份与批次；这是美术生产计划，不建立新的材料规则正文。

| 批次 | 材料 | 进度 |
| --- | --- | --- |
| 01 | 水、火、土、风、草 | 已生成，PendingReview |
| 02 | 铁、光、影、硫、汞 | Queued |
| 03 | 盐、蒸汽、雾气、草汁、铁砂 | Queued |
| 04 | 辉光、影尘、溶剂、灵液、火种 | Queued |
| 05 | 灵火、晶核、封盐、再生液、醒神露 | Queued |
| 06 | 蚀解液、金刚砂、浮空石、封魔晶、太阳火 | Queued |
| 07 | 雷火核、幽冥火 | Queued |

## 共用规格与来源

沿[AS-G002-038 / SHIELD-CARD-PRODUCTION-01](../shield-card-production-2026-10-30/README.md)：1024×1536、2:3、共用纸框＋单幅RGBA插画、中心pivot、不紧裁；运行默认单张合成图，mipmap、线性mipmap过滤、无损与straight alpha，卡效／名称／状态由宿主负责。本批插画统一在四边内收3%以免纸框被水滴或叶尖压住，源PNG不改字节。

首批使用内置image_gen，5次独立调用，每张1个明确材料主题，复用同一纸底而非每张重画。提示词／源原件／尺寸／SHA／装载包由[本批manifest](batch-01/manifest.json)固定；正式包按批冻结，后续不覆盖01版清单。新图像仍需用户审阅；独立Godot检查不能代替主工程接入或真人识别验证。

CUSTOM；设计输入固定game提交42970ee2e02c68d5212da419f4756f678ebf73ae。实际读取B01身份表、炼金配置工作稿的范围／身份引用、视觉生产规格、必要管理文件与现有美术校验代码，未扩读全GDD。11种终末成品是B01另一张表，不计入这32种材料；如需制作可另沿其身份顺序开批。

原件就地：项目sources备份生成原字节，外部交付工程E:/Project/yanzhou-art-assets/alchemy-material-cards-2026-10-30。PNG／ZIP本机ignored，说明、提示词、队列及清单入Git。归属main，derived-from AS-G002-038，ReadyForScope / PresentLocal仅首批限定技术检查；玩法M资格和规则发行状态保持原义。
