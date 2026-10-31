# Backpack Battles 物品美术与交互取证

2026-10-31 / BACKPACK-ITEMS-01。状态：Research / LimitedEvidence；AS-SH-007，shared-reference。本轮按用户要求分析本机 RAR，使用指定的 REA，并以已有 GDRE 补充其不支持的 Godot PCK 读取。没有打开源游戏，没有修改其他项目设计。

**入口：[物品图册](E:/Game/Backpack%20Battles-analysis/2026-10-31/catalog/index.html)。** 可直接双击该本机 HTML；内嵌索引，图片依赖分析包内 `recovered/`，不能只复制一个 HTML。技术报告、CSV/JSON、原图与证据均从图册或[本机完整报告](E:/Game/Backpack%20Battles-analysis/2026-10-31/REPORT.md)进入。

## 结果与覆盖

| 对象 | 结果 |
| --- | --- |
| 输入身份 | 用户提供 `E:/Game/Backpack Battles.rar`，RAR5；EXE＋Godot 3.6.0 PCK |
| 图片 | 1,791 张恢复 PNG；Items 下 453 张，含主体、变体、特效、遮罩与格子 UI，不等于 453 种物品 |
| 物品 | ItemData.csv 382 条；334 条匹配场景、333 个不同主 Icon 路径 |
| 缺失关系 | 48 条未匹配，均为表内 version=1.0.0；保留为未确认内容，不声称本包可获得 |
| 配方 | 131 条原始声明，保留 + 与 *；包括未匹配对象，不等于全部可执行 |
| 脚本 | 586 个加密 .gde，0 个成功反编译；完整交互算法仍 Unknown |
| 产物 | 可搜索图册、图片尺寸/alpha/SHA、物品与配方 CSV、场景继承/纹理/格子 JSON、七张接触表、交互报告、固定 manifest |

重点结论：物品主体、占格、点击轮廓、物理轮廓分别定义；基础格为 80×80。皮包覆盖自己的 TileSet，不能全局套用 tile_id。生命魔药分瓶身、液体遮罩、前景覆盖层；彩虹剑分轮廓、玻璃层并带两个宝石槽。图册可直接定位附加纹理。物品到场景的 334 条关系按场景根名／文件名匹配推导，匹配依据保留；尚未恢复加密 ItemBook 中的运行 ID 绑定。

交互已确认的是输入与场景声明、作者提示文本、配方字段和动画内回调：右键/R/E/滚轮存在旋转映射，另有保留、合成锁定；放入背包有 0.3 秒短高亮/缩放，合成就绪有两秒循环高亮，Sell 动画在 0.5 秒末调用 discard。购买结算、合法放置、上下文分派、配方竞争、动态说明替换和战斗结算顺序均未得到完整源码或实机证据。

## 工具与证据限制

REA 6.4.0 来自 `E:/Game/Demoncards/rea`，提交 `58300885207133422af235e0f2b10658cf958b03`。inspect-pe-resources 返回成功证据，覆盖 21 个资源目录项、9 个资源；inspect-artifact 对 PCK 返回 unsupported_target，失败原件保留。物品图片、场景与数据表来自 GDRE Tools 2.6.0 的静态恢复，明确区别于 REA Evidence。

GDRE 报告 2,064 个导入资源转换成功、0 失败，Lossy=1、metadata rewrite=10；那 1 个 Lossy 的具体对象未定位，不承诺原作者源文件无损还原。脚本加密与三个插件配置恢复不完整，恢复目录不是可运行工程交付。翻译表原始 key 大量未恢复，仅精确匹配英文名称到中文，不猜测物品与描述的行序关系。

检查通过：6,420 个 PCK 条目的内嵌 MD5 全部核对；1,791 张 PNG 解码与导出 SHA；382 条物品原始字段保留与 ID 唯一；334 条匹配场景/纹理路径。浏览器检查覆盖物品搜索、详情与占格、附加纹理、18 条 Bag 筛选、遮罩搜索、配方搜索和交互页，采样日志无警告/错误。只目视接触表第 1 页与局部图册界面，没有逐图美术验收、游戏运行或玩法验证。

## AS-SH-007 登记

- 归属／用途：shared-reference / media-analysis-lab，本机第三方物品美术、装配及交互证据研究；无目标项目采纳。
- 固定版：BACKPACK-ITEMS-01；源身份、工具、导出清单和本机 manifest SHA 在[身份元数据](source-and-output.json)。本机原件不迁移；资源／证据文件范围由 manifest 固定。
- 生命周期／访问：ReadyForScope / PresentLocal，2026-10-31，限上述静态核对与图册检查；不是完整交互源码或可运行工程。
- 来源／复用：用户提供的第三方包；作者及公开改作、分发许可 Unknown，仅本机内部研究。原 EXE/PCK、恢复图像、游戏文本与脚本不入 Git。后续复用仍需记录目标和具体版本。
- uses: None；derived-from: 用户指定 RAR 的静态提取；暂无登记使用者。AS 登记不替代 M 资格，不改变任何项目玩法规则。

下一证据缺口为 Item/Inventory/CraftingManager/ItemTooltip/BottleOfBooze 加密脚本的真实实现，以及有授权的实机行为观察；本轮没有启动玩法测试。
