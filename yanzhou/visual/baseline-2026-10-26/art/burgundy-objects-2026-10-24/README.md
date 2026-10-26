> 2026-10-26归档附件。以下是原日期的来源／提示词记录；其中布局、当前状态、下一步和美术要求均不约束新基准。原字节及所有未保留文件按附件README的共同Git快照取证。

# 暗酒红独立对象审阅稿

2026-10-24 · game-002 / main · **BURGUNDY-OBJECTS-01**。入口：[打开对象目录](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/index.html)。

用户已确定暗酒红＋古金＋黑褐木的配色方向，并要求逐对象制作HTML与效果图，调整审核后再整体组装。十项均为独立候选；具体造型与美术接受状态仍为 **Raw / Unqualified，待用户审阅**。本批未修改主牌桌HTML、规则或玩法参数。

## 使用

从目录打开任一对象，切换“HTML样稿／效果图”。HTML可调尺寸、边饰强度、光照及该对象的专用参数；效果图保持生成原貌。卡牌和法器可点击打开上层详情；其他陈设只有审阅工具，不增加游戏操作。

批注自动保存于当前浏览器，参数随批注或“保存批注与参数”保存；重置参数保留批注。可导出JSON交回修改。直接用本地文件打开时，浏览器可能限制或按文件隔离本机存储，跨项汇总请通过同一HTTP来源访问；单项导出仍包含当前批注。批注不是正式采纳记录。

整个目录可本地离线打开，无安装或构建依赖。保留相对目录关系：11个HTML入口共享review.css／review.js，图片位于上一级images。没有网站发布。

## 对象清单

| 编号 | 独立HTML | 当前效果图 | 可调重点 |
| --- | --- | --- | --- |
| 01 | [桌面](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/01-table.html) | [PNG](images/01-table-v01.png) | 桌布覆盖、边饰、木面与留白 |
| 02 | [卡牌正面](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/02-card-front.html) | [PNG](images/02-card-front-v01.png) | 护盾卡的比例、边饰、纸色明暗 |
| 03 | [卡背](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/03-card-back.html) | [PNG](images/03-card-back-v01.png) | 统一纹章、正背示例翻转 |
| 04 | [守护法器](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/04-guardian.html) | [PNG](images/04-guardian-v01.png) | 厚重轮廓、珐琅、进度示意 |
| 05 | [施法法器](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/05-caster.html) | [PNG](images/05-caster-v01.png) | 细铜环、水晶、进度示意 |
| 06 | [筹码](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/06-chips.html) | [PNG](images/06-chips-v01.png) | 三类同尺寸、有限堆叠、准确总数 |
| 07 | [铜灯](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/07-lamp.html) | [PNG](images/07-lamp-v01.png) | 灯体比例、可开关微动 |
| 08 | [封蜡试剂瓶](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/08-vial.html) | [PNG v02](images/08-vial-v02.png) | 平放轮廓、液面造型、封蜡 |
| 09 | [札记与笔具](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/09-notes.html) | [PNG](images/09-notes-v01.png) | 封面纹章、摆放角度 |
| 10 | [光影与反馈](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/dist/10-light.html) | [PNG](images/10-light-v01.png) | 光线方向、三段亮纹、短反馈 |

试剂瓶v01视角偏斜，保留原件供追溯，当前页面使用修正后的v02。所有物件先完整呈现；未来铜灯、试剂瓶、札记是否选用、如何裁切摆放，等待用户审核。

## 来源与视觉边界

共同输入固定于提交 `68b5f3e8b37b54e99dfe3ce7e4717090d8ecbd6e` 的[风格化构思](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/sources/inbox/2026-10-24-top-down-2d-battle-style.md#8-沿用核心要素后的风格化构思)，加本轮用户配色及分项审阅决定。结构参照DM-G002-017／ROUND-TABLE-HTML-02，固定版本 `8641dd583d32d6d3f737b1c1e56efd2bc2052e88`；现行规则输入仍沿主桌原说明，不升级玩法范围。

- 主调为 #4a1724 暗酒红、#ac8c4e 古金、#261a15 黑褐木，辅以 #e7d8b7 旧纸白。灰蓝只用于护甲身份区分。
- HTML是原创CSS／SVG的可调结构稿；PNG由**内置image_gen**生成，表现材质、刻纹与插画方向。二者是同对象的两种审阅材料，尚未逐像素统一；参数不会修改PNG。
- [实际提示词](prompts.json)保存共同描述、各对象描述及试剂瓶修正提示；生成时未上传参考截图，只使用文字描述。修正调用只引用本批生成的瓶子。默认生成原件留在Codex生成目录，项目中保存未改写的副本。
- 图中金属与玻璃高光、磨损密度、笔触平面化程度仍待审阅。此版是效果候选，不能直接视为最终游戏图集或已经验收的2D资产。
- 筹码的最多5层及零值虚线轮廓为可逆展示示意，未采纳为正式细则；数值输入无新增游戏上限。详情与历史仍延期。卡背翻转只是此独立页的正背展示，不代表真实暗牌可翻开。
- 两台法器的进度示意不运行生产；灯光反馈不与战斗结算连接。本批没有新资源、支付、成长、取得方式或状态权限。

## 检查与证据

2026-10-24，本机静态HTTP预览、Codex内置浏览器1280×720：

- 目录十项入口及十张当前图片加载完成，无横向溢出；逐项页面能打开并显示HTML组件。
- 卡牌／法器点击弹窗，关闭或Esc后焦点回到来源；卡背可来回展示。
- HTML／效果图切换正常，原图模式停用HTML参数；尺寸、桌布覆盖、法器进度、瓶液面、札记角度及光向参数可用。
- 筹码示例生命144、护甲9999仍最多5层，准确总数保留；0值无实筹码。没有新增上限或详情／历史。
- 灯火微动可开关，三段亮纹和短反馈可触发；样式包含减少动态效果的系统偏好。
- 批注与参数保存后重载恢复；重置参数保留批注。检查用临时批注已清空。
- JavaScript语法与本地文件引用检查。导出JSON由本地浏览器生成，无远端写入；跨浏览器存储、移动端、屏幕阅读器及真实游戏整合未验。

预览：[对象目录](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/preview/catalog-1280.png)、[卡牌HTML](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/preview/card-html-1280.png)、[卡牌效果图](https://github.com/dsaj4/game_design/blob/56a0ef07f13a647a4383a751977f2dce871bd731/yanzhou/visual/burgundy-objects-2026-10-24/preview/card-image-1280.png)。本检查仅说明此审阅稿可用，不代表美术采纳、玩法测试或真实引擎验收。

## DA-1登记

| 字段 | 记录 |
| --- | --- |
| Demo | **DM-G002-018** 暗酒红独立对象HTML审阅包 |
| 素材 | **AS-G002-031** 暗酒红对象效果图包 |
| 归属／维护 | game-002 / main；本README及此目录 |
| 固定版本 | BURGUNDY-OBJECTS-01；[manifest](manifest.json)列明HTML、样式、脚本、提示词、PNG和截图范围及SHA-256 |
| 状态 | DM ReadyForScope（仅上述浏览器审阅）／PresentLocal；AS Catalogued／PresentLocal；具体美术Raw / Unqualified |
| 规格 | 10个当前PNG＋1个保留瓶子v01；各图尺寸、透明通道及原始生成文件名见manifest；没有裁切图集 |
| 来源／复用 | HTML为本任务自制；PNG为内置image_gen生成。用户授权本项目内部制作与审阅；未声明公共开放许可或第三方原图再分发权 |
| 关系 | DM uses AS-G002-031@BURGUNDY-OBJECTS-01；DM参照DM-G002-017@ROUND-TABLE-HTML-02的核心对象，不改原主桌；AS无第三方像素输入 |
| 下一步 | 用户逐对象批注 → 修改对应源稿／效果图 → 用户审核后才整体组装；具体采纳另外记录 |
