# Demo 与素材统一目录

版本：DA-1 / 2026-10-01。维护身份、入口及复用边界；完整约定见[规范](../demo-asset-standard.md)，补录用[模板](../../game-design-workflow/templates/demo-asset-record-template.md)。检索本页的ID、Project/DIR、用途和标签，再按授权打开原件。

本轮是**初始登记**：来自当前开发索引、视觉入口、DIR-029演示交付和已跟踪参考包；不是全历史资产审计。未打开旧归档、未读取未跟踪新方向、未运行Demo或重新验证玩法。登记基线：`25ec81ea9f9cef3496922068bc63622b36aba5c5`。下文“基线提交”均指该完整提交，不自动追随HEAD。本仓库原件用该提交+路径固定；外部资源另外注明。

## Demo

| ID / 名称 / 标签 | 归属 / 权威说明 | 固定版本与入口 | 状态 / 可复用范围 |
| --- | --- | --- | --- |
| <a id="dm-g002-001"></a>DM-G002-001 暗面Demo；可玩流程、旧RC1 | game-002 / main；[开发索引](../../yanzhou/development/README.md) | 原登记v0.1、分支codex/dark-demo、短提交cf7b98d；完整实现提交待补。[外部README](E:/Project/yanzhou-dark-demo/README.md) | Catalogued / PresentLocal（2026-10-01仅确认README存在）；可参考旧流程和视觉，不是TL-1实现 |
| <a id="dm-g002-002"></a>DM-G002-002 时间轴翻牌；动效、交互 | game-002-optimization / DIR-029；[方向第19轮](../../yanzhou/exploration/DIR-029-timeline-card-battle/README.md#第19轮四刻翻牌动效演示)、[开发证据](../../yanzhou/development/README.md) | v0.1 / 2026-09-30；[本机预览文件](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-preview.html)、[技术说明](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-notes.txt)；文件指纹见下 | Catalogued / PresentLocal；可参考共同翻牌、移动与播放反馈，未包含战斗结算；本轮未运行 |

DM-G002-001的打开、安装与操作按外部README核查；本轮没有审查代码许可、完整依赖或构建，不声称已具备复制改作条件。设计源为旧RC1及旧视觉，原实现缺口、局部检查和失败记录仍以开发索引为准。

DM-G002-002源文件和预览于2026-10-01仅做存在性与SHA-256检查：

| 文件（同一持久本地目录） | SHA-256 |
| --- | --- |
| timeline-flip-demo.html | `9C36060F5556B6975267CA10A6AC059F053F93653804B1CFD4FEDD67BAE84BB8` |
| timeline-flip-demo-preview.html | `A2AE03ECEB70BB93D63C1122B06D82F6B293C434E0F8D6A259934E8B3D2320A2` |
| timeline-flip-demo-notes.txt | `60F384278BA565F870382856642E96B4303AD46DFACEDB07F7B46DE4337501E9` |
| verification.json | `7468B9FB25A659B2CBFD68461CDC41DB6E6CDBFA511A29E045A2376A9406089A` |

历史报告记载局部浏览器检查通过；本轮未重新执行。四刻静态样例、临时动画节奏和占位美术不升级为正式规则。代码/依赖的复制改作与对外分发条件仍待目标任务核对。跨机器先取得源文件与所需依赖；本机地址不是网站发布或便携构建证明。

## 素材与参考包

| ID / 名称 / 标签 | 归属 / 原件入口 | 版本 / 来源条件 | 状态 / 使用边界 |
| --- | --- | --- | --- |
| <a id="as-g002-001"></a>AS-G002-001 05紧凑暗面视觉包；UI、风格 | game-002 / main；[风格说明](../../yanzhou/visual/reviews/2026-09-19/style-guide.md)、[文件清单](../../yanzhou/visual/reviews/2026-09-19/source-manifest.json) | v0.2 / 2026-09-19；基线提交下`yanzhou/visual/reviews/2026-09-19/`的已跟踪文件；生成来源/提示词沿原包，分发条件未审 | Catalogued / PresentLocal；旧RC1 Selected Visual；不能当成TL-1最终布局 |
| <a id="as-g002-002"></a>AS-G002-002 DIR-029完整牌桌v9；概念图 | game-002-optimization / DIR-029；[PNG原件](../../yanzhou/exploration/DIR-029-timeline-card-battle/ui-concept-v9-full-tabletop.png)、[提示词](../../yanzhou/exploration/DIR-029-timeline-card-battle/ui-concept-v9-full-tabletop-prompt.txt) | 基线提交下上述两个文件；生成资料，具体生成模型/分发条件本轮未审 | Catalogued / PresentLocal；Scene Concept / Awaiting Visual Review，尚非最终生产素材；尺寸等在实际复用前补录 |
| <a id="as-g002-003"></a>AS-G002-003 Godot/Blender实验集合；模型、渲染 | game-002 / main；[登记来源](../../yanzhou/development/README.md) | 原索引入口`E:/Project/game-002-godogen-lab/README.md`；固定版本、包范围、依赖和授权均待补 | Catalogued / **Missing**（2026-10-01本机原入口不存在）；只保留线索，不能宣称可下载或已恢复 |
| <a id="as-sh-001"></a>AS-SH-001 拆解写法参考包；结构、DOCX范例 | shared-reference / media-analysis-lab；[包入口](../../media-analysis-lab/references/writing-examples/README.md) | 基线提交下`media-analysis-lab/references/writing-examples/`的已跟踪文件；结构MD与两份DOCX各自来源/转载条件待核实 | Catalogued / PresentLocal；按原入口只作结构和写法参考；本轮未读DOCX正文或检查版式，不授予复制正文/重发权限 |

素材PresentLocal仅指列出入口/原件存在及已跟踪，不代表已目视审图或核验全部清单。包范围以固定提交内已跟踪文件为限，未跟踪资源不纳入。文件规格、作者和许可缺口保留Unknown；实际复用时按所需范围补齐，不把目录登记当作授权或Qualified素材。

## 已知使用关系

| 使用者 | 来源 | 关系及证据 |
| --- | --- | --- |
| DM-G002-001 | AS-G002-001@v0.2（基线提交） | 视觉选择/参考关系来自原风格说明与开发索引；本轮未核对代码中实际导入文件 |
| DM-G002-002 | AS-G002-002@v9（基线提交） | 原方向与开发索引说明采用v9候选作视觉参照；演示使用文字/装饰占位，不代表导入这张PNG |

新使用关系写在目标维护文档；此表保留跨资源发现入口，不复制项目参数或验证结论。正式系统与探索方向互相参考后仍保留各自设计版本。

## 待补与维护

- DM-G002-001：完整实现提交、可运行入口与环境、代码/依赖复用条件。
- DM-G002-002：如需跨机器交付，明确持久交付位置、依赖和使用条件；原局部检查保留，不自动重跑。
- AS-G002-001/002及AS-SH-001：按实际使用任务补规格、来源与许可；不为本次登记发布或移动原件。
- AS-G002-003：查明新位置或可恢复版本；Missing不等于已经归档。
- new-roguelike：其[开发索引](../../new-roguelike/development/README.md)当前无登记产物，保持空白，不继承言咒条目。
- 其他方向、历史Demo、已发布布局站点和未跟踪资产未逐项盘点；遇到实际复用需求再登记，不宣称此次收录全部资源。稳定ID归档后保留记录，不重新分配。
