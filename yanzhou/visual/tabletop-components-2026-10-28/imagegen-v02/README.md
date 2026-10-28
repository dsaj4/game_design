# 基础组件逐件imagegen生成

2026-10-28 · game-002 / main · AS-G002-034 / TABLETOP-COMPONENTS-02。10个完整组件已全部逐件使用内置image_gen重新生成，PNG／来源／透明与预览局部检查通过，美术接受和引擎接入待验。旧版30个控件导出分片不作为新版组件来源。法器、卡牌仍后置；不扩展玩法或修改首轮HTML。

**[组件总览](preview-components.png)** · [下载本机PNG包](tabletop-imagegen-v02.zip) · [透明底检查](preview-alpha.png) · [接入说明](IMPORT.md)

![十件逐件imagegen组件](preview-components.png)

## 逐件输出

每行都是一次独立image_gen调用产生的一张完整PNG。exports/中的10个文件均与各自生成原件字节一致，没有裁切、拼接、改alpha、重采样或补画；整幅原生画布及透明留白一并保留。预览代码只做并排显示和底色检查，不生产组件。

| 组件 | 独立原图 | 原生画布 | 提示词 |
| --- | --- | --- | --- |
| 木桌背景 | [wood-background.png](exports/wood-background.png) | 1672×941 RGB | [准确提示词](prompts/wood-background.txt) |
| 桌垫 | [felt-mat.png](exports/felt-mat.png) | 2018×779 RGBA | [准确提示词](prompts/felt-mat.txt) |
| 空工作台 | [workbench-base.png](exports/workbench-base.png) | 2172×724 RGBA | [准确提示词](prompts/workbench-base.txt) |
| 无字确认按钮 | [confirm.png](exports/confirm.png) | 2055×765 RGBA | [准确提示词](prompts/confirm.txt) |
| 无字选中题签 | [tab-active.png](exports/tab-active.png) | 2098×749 RGBA | [准确提示词](prompts/tab-active.txt) |
| 无字未选中题签 | [tab-idle.png](exports/tab-idle.png) | 2098×749 RGBA | [准确提示词](prompts/tab-idle.txt) |
| 无字顶部纸带 | [header.png](exports/header.png) | 2172×724 RGBA | [准确提示词](prompts/header.txt) |
| 生命筹码短叠 | [chip-heart.png](exports/chip-heart.png) | 1312×1199 RGBA | [准确提示词](prompts/chip-heart.txt) |
| 护甲筹码短叠 | [chip-armor.png](exports/chip-armor.png) | 1263×1246 RGBA | [准确提示词](prompts/chip-armor.txt) |
| 施法次数筹码短叠 | [chip-spell.png](exports/chip-spell.png) | 1261×1247 RGBA | [准确提示词](prompts/chip-spell.txt) |

文字、数值和牌位仍独立排版。筹码绘制短叠层数不表示实有总数或容量；四角小装饰、纸纹及拟铭纹不发行新规则或库存。

CUSTOM局部资产范围：父目录README／manifest／IMPORT、v06图像、既有UI／筹码仅作形制参考，以及项目AGENTS、imagegen技能、DA-1和必要登记／协作规则。共同输入提交`69d45a6f16572709c1d0b8907a8b502f7492bafb`。新版一组件对应一次独立内置image_gen生成调用，全部保留生成原件、准确提示词和来源，检查后再交付。旧版文件及ZIP不覆盖。

## AS-G002-034 本版登记与检查

| 字段 | 内容 |
| --- | --- |
| 归属／用途 | game-002 / main；本页为全imagegen版维护入口，供后续2D美术接入与用户审阅 |
| 固定版本 | TABLETOP-COMPONENTS-02；[manifest](manifest.json)固定10个文件的尺寸、alpha、SHA、生成原件、参考及提示词；[checks](checks.json)记录本版实际检查 |
| ZIP固定交付 | tabletop-imagegen-v02.zip，17,679,367字节；SHA-256 `5f4265b42f131fc46c42b7d701751a6721b58f78749dedc08bcc3b0e2676d709`。25项：10个原PNG、10份提示词、接入说明、manifest、checks及2张预览 |
| 来源关系 | v06：AS-G002-032@HERBAL-ENGRAVING-06为风格参考；v01完整UI／筹码：AS-G002-034@TABLETOP-COMPONENTS-01仅作形制参考。本版没有直接发布旧图像素或旧拼接件；AS-G002-033、法器／卡牌均未取用 |
| 原件保管 | 工具生成原件仍在Codex原位置；逐件相同副本、生成对应表及检查工具保存在 `E:/Project/yanzhou-art-assets/tabletop-components-2026-10-28/imagegen-v02/`，准确路径与工具哈希见manifest |
| 状态／访问 | ReadyForScope / PresentLocal，2026-10-28，限原PNG、生成来源、透明和三种底色预览检查；用户接受PendingReview，正式引擎／触区／压缩预算NotRun |
| 复用条件 | 本项目内部审阅／使用；公开分发未另授权，原参考边界保持。PNG／预览／ZIP本机保管，只提交说明、提示词与固定清单 |

已核对10个独立生成原件、10份提示词、10个导出哈希、9张真正透明PNG及1张不透明背景；透明图四角alpha均为0。已目视检查完整边界、单一指定物件、无文字／数值底板及心形／盾形／星芒主体，并在浅纸、深色、木色底检查9个透明件。原图v06、v01包和DM-G002-020保持原字节。

独立生成会改变轮廓、比例和金边强度，本版不声称与v01同形，未继承旧版九片边距或命中区。完整画布包含透明留白；manifest的contentBoundsAlpha16只供定位，未据此裁图。引擎布局、状态同形、完整悬停／按下／禁用图、书本／手部／陈设及真人体验仍未验。法器与卡牌继续后置，PRE2D-Q01不因此关闭。

## v01保留

[父目录历史v01](../README.md)及其40文件导出、原manifest、检查和ZIP不覆盖；原记录固定在提交`69d45a6f16572709c1d0b8907a8b502f7492bafb`。本版交付只取当前exports/的10个imagegen原图，不混入旧30分片。
