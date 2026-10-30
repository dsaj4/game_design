# 护盾卡正式资产 · 首版

2026-10-30 · game-002 / main · **AS-G002-038 / SHIELD-CARD-PRODUCTION-01**。用户已确认[阻挡与庇护](../card-face-exploration-2026-10-29/shield-scene-2026-10-30/README.md)作为制作模板，本包完成首张可导入美术资产。模板构图确认与新分层成品验收分开：本包ReadyForScope限独立Godot导入／显示检查，新分层成品仍待用户审阅，尚未替换首场工程占位。

![原生引擎多尺寸检查](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/evidence/size-review.png)

**[取得完整交付包](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30.zip)** · [直接查看成品PNG](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/cards/shield-guard/shield-front-1024.png) · [包内装载说明](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/README.md)。本页是唯一制作入口；文件、SHA与原生成路径见[manifest](manifest.json)。

## 分几层，怎样用

| 对象 | 文件／规格 | 职责 |
| --- | --- | --- |
| 共用纸底与细框 | [生成源](sources/paper-frame-v01.png)，1024×1536 RGBA | 共用皮肤；纸底与细边一体，不把本来不变的边饰再拆散 |
| 整幅透明插画 | [生成源](sources/shield-illustration-v01.png)，同画布RGBA | 盾、受护者、箭、撞击、金弧与地形一组，保持遮挡关系；无自动tight trim |
| 默认运行成品 | 交付包cards/shield-guard/shield-front-1024.png，同画布RGBA | Godot原生两层合成烘焙；普通卡实例只加载这一张 |
| 显示与装载适配 | 交付包cards/card_face.tscn及card_texture_library.gd | 逻辑ID为shield.guard；相对res路径，资源复用、等比容纳；只负责美术显示 |

两份生成源由内置image_gen根据已确认模板独立重绘／隔离，原字节保管；[纸底提示词](prompts/paper-frame-v01.txt)与[插画提示词](prompts/shield-illustration-v01.txt)完整保存。构图关系保留，局部笔触与细节有重绘差异；这是两层PNG源件，不是原图无损PSD拆层。

画布原点左上(0,0)，中心pivot_uv=(0.5,0.5)，不裁边、不非等比拉伸。生成纸底原alpha约0.97，包内paper_surface.gdshader仅在制作／Layered显示时使纸内不透明并统一30px圆角；源PNG没有程序修图。最终成品中心alpha=1、四角=0。插画straight alpha，深／浅／紫三底已查看，无矩形纸底或明显纸色晕边。

## 装载决策与参考

[三款游戏的专门调研与采用理由](../../../media-analysis-lab/runs/2026-10-30-card-production/README.md)已经收齐。借鉴“共用牌式／整幅主画／动态状态分工”和完整画布注册，运行采用静态成品，制作保留两层。暂不引入图集、双档、三维法线或多层PBR，也不强拆盾／人物／箭。

手牌和放大共用1024×1536资源，开启mipmap、无损导入、线性mipmap过滤、非预乘alpha及alpha边缘修正。库按ID请求并通过ResourceLoader.CACHE_MODE_REUSE与路径缓存复用；不在逐帧逻辑读盘。缓存清理只移除本库引用，不保证其他持有者或GPU立即释放。

宿主现有手牌盒155×229来自yanzhou-2d脚本，只读版本见manifest。源画布2:3在其中等比显示为152.667×229，左右各约1.167留空；不为适配而拉宽盾牌。包内TextureRect忽略鼠标，原宿主继续拥有命中、悬停、拿起、选择描边、卡名／效果查看与状态。没有因为本包无字而删除必要信息或修改现行C1—C3合同。

## 检查与交付状态

- Godot 4.7.2实际图形渲染通过：155×229手牌盒、110×165小尺寸、310×465检视和420×630放大；已目视盾、人物与来袭方向。小尺寸细箭和磨损不再逐笔可读，主体保护关系仍可辨；没有将其等同真人辨识实验。
- [深浅紫底透明检查](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/evidence/alpha-review.png)、[像素与alpha](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/evidence/bake-checks.json)、[装配与缓存](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/evidence/runtime-checks.json)：分层重新渲染与成品字节相等；100次请求同一Texture2D；普通Flat首次只请求一张成品。
- [干净目录检查](E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30/evidence/clean-import.json)：不带.godot缓存重新导入，两张检查图SHA与原工程一致。ZIP内31个锁定文件逐一重算SHA通过；导入缓存不随包封装。

所有证据是独立资产校验工程，不是当前战斗实机截图、OS输入、全牌库性能或玩法测试。首轮独立校验视口未强制更新导致一致性断言失败，已修正校验宿主后复核通过；最终日志及结果沿交付锁定。本轮未写yanzhou-2d、未移除占位文字、未改玩法。

## 来源与保管

本包的纸底、纸面Shader、装载约定与显示组件已用于[AS-G002-039炼金材料卡首批](../alchemy-material-cards-2026-10-30/README.md)；目标记录原字节复用和适配，当前包／ZIP／锁定清单保持原版。

CUSTOM，设计固定game提交f3101a6489686877f802e0e60983062e4d6971da；用户本轮明确确认构图模板并授权正式制作及三项专门调研。阅读限模板、视觉与资产操作资料、研究报告和现工程卡面宿主必要片段。规则全GDD未扩读。

本包从AS-G002-037@05独立维护；uses AS-SH-006技术研究。工程／装载代码和截图留E:/Project/yanzhou-art-assets/shield-card-production-2026-10-30，生成原件继续保留.codex/generated_images并在本包sources备份；PNG与ZIP本机ignored，文档／提示词／清单入Git。原创运行包无第三方图像、代码、材质或字体。仅本项目本机制作与审阅；本轮不进行公开发布。后续可直接交开发方导入这一个代表件，再沿既有信息合同审阅真实卡牌宿主。
