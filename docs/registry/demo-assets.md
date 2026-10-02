# Demo 与素材统一目录

版本：DA-1 / 2026-10-01。维护身份、入口及复用边界；完整约定见[规范](../demo-asset-standard.md)，补录用[模板](../../game-design-workflow/templates/demo-asset-record-template.md)。检索本页的ID、Project/DIR、用途和标签，再按授权打开原件。

本轮是**初始登记**：来自当前开发索引、视觉入口、DIR-029演示交付和已跟踪参考包；不是全历史资产审计。未打开旧归档、未读取未跟踪新方向、未运行Demo或重新验证玩法。登记基线：`25ec81ea9f9cef3496922068bc63622b36aba5c5`。下文“基线提交”均指该完整提交，不自动追随HEAD。本仓库原件用该提交+路径固定；外部资源另外注明。

## Demo

| ID / 名称 / 标签 | 归属 / 权威说明 | 固定版本与入口 | 状态 / 可复用范围 |
| --- | --- | --- | --- |
| <a id="dm-g002-001"></a>DM-G002-001 暗面Demo；可玩流程、旧RC1 | game-002 / main；[开发索引](../../yanzhou/development/README.md) | 原登记v0.1、分支codex/dark-demo、短提交cf7b98d；完整实现提交待补。[外部README](E:/Project/yanzhou-dark-demo/README.md) | Catalogued / PresentLocal（2026-10-01仅确认README存在）；可参考旧流程和视觉，不是TL-1实现 |
| <a id="dm-g002-002"></a>DM-G002-002 时间轴翻牌；动效、交互 | game-002-optimization / DIR-029；[方向第19轮](../../yanzhou/exploration/DIR-029-timeline-card-battle/README.md#第19轮四刻翻牌动效演示)、[开发证据](../../yanzhou/development/README.md) | v0.1 / 2026-09-30；[本机预览文件](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-preview.html)、[技术说明](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-notes.txt)；文件指纹见下 | Catalogued / PresentLocal；可参考共同翻牌、移动与播放反馈，未包含战斗结算；本轮未运行 |
| <a id="dm-g002-003"></a>DM-G002-003 Godogen E1 R2；Godot材质与场景小样 | game-002 / main；[开发索引](../../yanzhou/development/README.md)、[原E1报告](E:/Project/game-002-godogen-lab/docs/e1-r2-report.md) | 外部提交`1dd488c507a73933e5f16e9d3829e451b5e37937`；[仓库与启动说明](E:/Project/game-002-godogen-lab/README.md)、[Godot工程入口](E:/Project/game-002-godogen-lab/game/project.godot) | Catalogued / PresentLocal（2026-10-01恢复后检查）；原记录为E1 R2小样，不含完整装配/选路/战斗；本轮未运行 |

### <a id="dm-g002-004"></a>DM-G002-004 炼咒试验台（2026-10-02新增）

- 归属：game-002-optimization / DIR-032；[探索与机制规格](../../yanzhou/exploration/DIR-032-playable-mechanism-loop/README.md)、[开发索引](../../yanzhou/development/README.md)。
- 类型／用途：两战最小可玩Demo；TL-1生产、卡牌试点、队列、维护／增幅、临时路由、跨战奖励与携带。
- 固定版本：DIR032-0.1，外部Git提交`afc6e4e0454bb3e306a49899022c340faabb5941`；[单文件Demo](E:/Project/yanzhou-tl1-demo/demo.html)、[操作／构建说明](E:/Project/yanzhou-tl1-demo/README.md)、[逐文件SHA-256](E:/Project/yanzhou-tl1-demo/manifest.json)。本机预览`http://127.0.0.1:8765`仅为本次会话入口，不替代固定版本。
- ReadyForScope / PresentLocal；2026-10-02已实际运行22项规则检查、6组固定输入两战试跑，并通过浏览器操作完成基础→增幅与辉核→辉核；[证据及限制](E:/Project/yanzhou-tl1-demo/evidence/verification.md)。真人体验、完整路线及平衡未验证。
- 来源／复用：本任务自制代码、CSS占位图形及验证附件；uses: None，derived-from: None，不引用其他方向资产或旧代码。可在本项目继续改作，未另授公开分发许可证；系统字体不随包分发。代码已本地Git保存，尚无远端仓库，不等于已公开发布。
- 设计边界：Q1–Q16只确认DIR-032试点，未回写主系统。未含付费干涉能力、完整路线／商店、复杂修饰或完整发行池。单文件构建无网络依赖；浏览器保存按来源隔离，下载事件未核验，可复制JSON导出已核对。

以下为原DM-G002-001–003登记记录，保留各自日期、来源与未验范围。

DM-G002-001的打开、安装与操作按外部README核查；原登记轮未审查代码许可、完整依赖或构建，不声称已具备复制改作条件。设计源为旧RC1及旧视觉，原实现缺口、局部检查和失败记录仍以开发索引为准。

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
| <a id="as-g002-003"></a>AS-G002-003 Godot/Blender实验集合；模型、渲染、概念图 | game-002 / main；[恢复后的仓库入口](E:/Project/game-002-godogen-lab/README.md)、[登记来源](../../yanzhou/development/README.md) | 外部提交`1dd488c507a73933e5f16e9d3829e451b5e37937`；范围与入口见下方恢复记录；依赖见外部工具链锁，逐项分发条件待核实 | Catalogued / **PresentLocal**（2026-10-01用户通知恢复后复查）；旧RC1资产与视觉探索，未认定TL-1兼容或完成美术验收 |
| <a id="as-g002-004"></a>AS-G002-004 DIR-031视觉案例参考包；官方截图、牌桌、炼金工作台 | game-002-optimization / DIR-031；[图文与登记](../../yanzhou/exploration/DIR-031-visual-form-style/README.md#第4轮五个相邻案例的真实游戏截图)、[来源清单](../../yanzhou/exploration/DIR-031-visual-form-style/reference-screenshots-v01-sources.json) | v0.1 / 2026-10-02；固定提交`46f8a0ff7813f022e8e4c9b13516f5ba68c2ce98`下`yanzhou/exploration/DIR-031-visual-form-style/`，文件范围仅限清单所列7张图；5张官方Steam截图＋2张既有用户参考图，逐项规格、来源、SHA-256见清单；具体许可Unknown | Catalogued / PresentLocal；2026-10-02核对7图哈希及解码，目视核对5张新增官方截图；DIR-031仅作视觉参照，保持Raw / Unqualified，未运行游戏、不授予资产复制改作或商业分发权 |
| <a id="as-sh-001"></a>AS-SH-001 拆解写法参考包；结构、DOCX范例 | shared-reference / media-analysis-lab；[包入口](../../media-analysis-lab/references/writing-examples/README.md) | 基线提交下`media-analysis-lab/references/writing-examples/`的已跟踪文件；结构MD与两份DOCX各自来源/转载条件待核实 | Catalogued / PresentLocal；按原入口只作结构和写法参考；本轮未读DOCX正文或检查版式，不授予复制正文/重发权限 |

素材PresentLocal仅指列出入口/原件存在及已跟踪，不代表已目视审图或核验全部清单。包范围以固定提交内已跟踪文件为限，未跟踪资源不纳入。文件规格、作者和许可缺口保留Unknown；实际复用时按所需范围补齐，不把目录登记当作授权或Qualified素材。

AS-G002-004为2026-10-02的后续登记，使用该行独立固定提交，不适用页首初始登记基线。其来源清单SHA-256为`db79a49078d3a48f95a28b0d45239c662bea0bfc161385847e6bbed1c05c6019`；目视核对范围以该行和方向页记录为准。

2026-10-02使用范围调整：用户决定排除Tainted Grail: Conquest，原话“该案例可以排除，基本没有可借鉴点”。DIR-031当前只使用包内其余6张图（4张官方截图＋2张用户参考图）；被排除截图及v0.1来源清单保留作历史追溯，不再作为当前风格参考。包的固定版本、文件哈希和原采集证据不变。

### Godogen恢复登记（2026-10-01）

用户通知“game-002-godogen-lab已恢复，加入登记”。保留此前Missing检查作为历史，本轮已复查README及下列入口存在，更新AS-G002-003为PresentLocal，另登记DM-G002-003；恢复不等于重新执行历史验证。

- 外部固定提交：`1dd488c507a73933e5f16e9d3829e451b5e37937`，分支`codex/setup-godogen-demo`。集合范围为该提交内`art/`、`concepts/`、`references/`及对应说明的已跟踪文件；可独立复用子包后续按需拆ID。
- [法杖管理原生资产v03](E:/Project/game-002-godogen-lab/art/wand-management-v03/README.md)、[长袋与桌面组合v02](E:/Project/game-002-godogen-lab/art/map-desk-v02/README.md)：README记载为原生Blender美术，仍待美术评议，不包含完整管理交互。
- [工具链锁](E:/Project/game-002-godogen-lab/toolchain.lock.json)、[原设计快照清单](E:/Project/game-002-godogen-lab/references/design/2026-09-14-wand-management-rc1/manifest.json)保留依赖和旧RC1来源；本轮只核对入口存在，未运行安装/启动脚本、逐文件验收资产或复核报告结果。
- 实际工作树有未提交修改`art/e1/e1-r2-master.blend`，未改动、未提交，也不计入上述固定提交版本。使用该本机文件前须另记其SHA-256和工作树身份，不能用HEAD冒充实际文件版本。
- 本轮已读README的SHA-256：`25B0A3EF469D85BE50D9EEA50B2B5A1A5E9D82DF6E9F2F03CAC508F8E39A1762`。生成素材、用户参考与原生资产依原来源分别解释；复制改作、分发条件及目标项目适配仍需按实际选用子包核对。

## 已知使用关系

| 使用者 | 来源 | 关系及证据 |
| --- | --- | --- |
| DM-G002-001 | AS-G002-001@v0.2（基线提交） | 视觉选择/参考关系来自原风格说明与开发索引；本轮未核对代码中实际导入文件 |
| DM-G002-002 | AS-G002-002@v9（基线提交） | 原方向与开发索引说明采用v9候选作视觉参照；演示使用文字/装饰占位，不代表导入这张PNG |
| DM-G002-003 | AS-G002-003中的E1子集@外部固定提交 | 外部README记载`art/e1`与`game/assets/e1`的源/运行资产关系；本轮未执行构建，工作树Blender修改不纳入固定版结论 |
| [DIR-031第4轮](../../yanzhou/exploration/DIR-031-visual-form-style/README.md#第4轮五个相邻案例的真实游戏截图) | AS-G002-004@v0.1 / `46f8a0ff7813f022e8e4c9b13516f5ba68c2ce98` | 当前使用其中6张图；Tainted Grail: Conquest已按用户决定排除，截图仅作历史保存；其余4张官方截图与2张既有用户参考图作视觉参照，不导入实现、不回写现行视觉规范 |

新使用关系写在目标维护文档；此表保留跨资源发现入口，不复制项目参数或验证结论。正式系统与探索方向互相参考后仍保留各自设计版本。

## 待补与维护

- DM-G002-001：完整实现提交、可运行入口与环境、代码/依赖复用条件。
- DM-G002-002：如需跨机器交付，明确持久交付位置、依赖和使用条件；原局部检查保留，不自动重跑。
- AS-G002-001/002及AS-SH-001：按实际使用任务补规格、来源与许可；不为本次登记发布或移动原件。
- AS-G002-003 / DM-G002-003：入口已恢复；实际选用时核对具体子包规格、分发条件及未提交Blender修改，目标环境运行能力尚未重新检查。
- new-roguelike：其[开发索引](../../new-roguelike/development/README.md)当前无登记产物，保持空白，不继承言咒条目。
- 其他方向、历史Demo、已发布布局站点和未跟踪资产未逐项盘点；遇到实际复用需求再登记，不宣称此次收录全部资源。稳定ID归档后保留记录，不重新分配。
