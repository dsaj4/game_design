# Demo 与素材统一目录

版本：DA-1 / 2026-10-01。维护身份、入口及复用边界；完整约定见[规范](../demo-asset-standard.md)，补录用[模板](../../game-design-workflow/templates/demo-asset-record-template.md)。检索本页的ID、Project/DIR、用途和标签，再按授权打开原件。

本轮是**初始登记**：来自当前开发索引、视觉入口、DIR-029演示交付和已跟踪参考包；不是全历史资产审计。未打开旧归档、未读取未跟踪新方向、未运行Demo或重新验证玩法。登记基线：`25ec81ea9f9cef3496922068bc63622b36aba5c5`。下文“基线提交”均指该完整提交，不自动追随HEAD。本仓库原件用该提交+路径固定；外部资源另外注明。

## <a id="as-g002-030"></a>AS-G002-030 二维桌面参考截图

- 归属：game-002-optimization / DIR-039；[完整登记与使用边界](../../yanzhou/exploration/DIR-039-2d-first-battle/README.md#as-g002-030-用户二维桌面参考截图)。用户2026-10-18附件，仅作空间分区、桌面氛围与卡牌层次参照；设计Raw / Unqualified。
- v01，JPEG 1919×1079；SHA-256 `191934888cfd853dc312e87ae1e5de602e821aa392e2af404a95a133e9bc4dee`。原件 `C:/Users/ADMINI~1/AppData/Local/Temp/codex-clipboard-d4ed62f5-d98f-4d07-b496-8d205713eaca.jpg`，未复制二进制入Git。
- Catalogued / PresentLocal，2026-10-18已目视及核SHA；临时路径长期可访问性不保证。原作者／作品身份／原URL／再分发许可Unknown；仅本轮内部参照，未导入、未公开上传。uses／derived-from：None；使用者DIR-039/R1。

## Demo

| ID / 名称 / 标签 | 归属 / 权威说明 | 固定版本与入口 | 状态 / 可复用范围 |
| --- | --- | --- | --- |
| <a id="dm-g002-001"></a>DM-G002-001 暗面Demo；可玩流程、旧RC1 | game-002 / main；[开发索引](../../yanzhou/development/README.md) | 原登记v0.1、分支codex/dark-demo、短提交cf7b98d；完整实现提交待补。外部README（原路径`E:/Project/yanzhou-dark-demo/README.md`，2026-10-18本机缺失） | Catalogued / PresentLocal（2026-10-01仅确认README存在）；可参考旧流程和视觉，不是TL-1实现 |
| <a id="dm-g002-002"></a>DM-G002-002 时间轴翻牌；动效、交互 | game-002-optimization / DIR-029；[方向第19轮](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-029-timeline-card-battle/README.md#第19轮四刻翻牌动效演示)、[开发证据](../../yanzhou/development/README.md) | v0.1 / 2026-09-30；[本机预览文件](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-preview.html)、[技术说明](C:/Users/Administrator/.codex/visualizations/2026/09/24/01a0d1f2-4d90-7db2-8527-684c3085e2ee/timeline-flip-demo-notes.txt)；文件指纹见下 | Archived / PresentLocal（外部原件保留；2026-10-04退出当前候选）；原Catalogued / PresentLocal记录；可参考共同翻牌、移动与播放反馈，未包含战斗结算；本轮未运行 |
| <a id="dm-g002-003"></a>DM-G002-003 Godogen E1 R2；Godot材质与场景小样 | game-002 / main；[开发索引](../../yanzhou/development/README.md)、[原E1报告](E:/Project/game-002-godogen-lab/docs/e1-r2-report.md) | 外部提交`1dd488c507a73933e5f16e9d3829e451b5e37937`；[仓库与启动说明](E:/Project/game-002-godogen-lab/README.md)、[Godot工程入口](E:/Project/game-002-godogen-lab/game/project.godot) | Catalogued / PresentLocal（2026-10-01恢复后检查）；原记录为E1 R2小样，不含完整装配/选路/战斗；本轮未运行 |

### <a id="dm-g002-011"></a>DM-G002-011 Godot EX-001首版（2026-10-11新增）

- 归属：game-002 / main；[当前开发入口](../../yanzhou/development/README.md)、[交付范围](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/godot-start-2026-10-11.md)。标签：Godot、真实结算、GLB接入、Windows、拍末恢复。
- 类型／用途：唯一正式工程的首个局部可运行版本；验证EX-001 0—14拍、中文详情、用途改变、队列／支付／打断、存取及资产重导入。完整游戏未实现。
- 固定版本：GODOT-EX001-0.1，外部完整代码提交`e71dcb78e81324b10eb8be08f5a5fce68facd937`；[源码与运行](E:/Project/yanzhou-godot/README.md)、[Windows包](E:/Project/yanzhou-godot/build/windows/Yanzhou.exe)、[manifest与文件哈希](E:/Project/yanzhou-godot/manifest.json)、[原始检查入口](E:/Project/yanzhou-godot/evidence/verification.md)。本地Git保存，无远端发布。
- 生命周期：ReadyForScope（EX-001局部技术检查）/ PresentLocal，2026-10-11实际运行；28项规则检查、两档各12项输入检查、独立包跨进程拍末恢复和组件重导入通过。实际断网、独立人员接手、完整117项验收、完整单战与真人体验NotRun。
- 来源／复用：本轮原创代码与占位卡面；uses: AS-G002-010@BATTLE-3D-02（实际复制导入原GLB）；derived-from: None（新工程，不复用旧Demo代码）。暂时放宽器具的Blender／GLB副本只是本Demo故障／重导入夹具，未成为新正式资产，交付包已恢复源版本。
- 工具／资产条件：Godot与.NET许可随包提供；调用系统中文字体，不打包字体文件。源模型沿AS-G002-010内部改作授权，公开分发权Unknown；原资产原件就地保留，未上传二进制、第三方缓存或原始美术。
- 设计边界：原型操作不补TL-Q08决定，示例数值不扩为默认；仅拍末保存，无中间步骤恢复。完整实现范围及保留差异以代码报告为准。
- 2026-10-11后续版本：**GODOT-EX001-0.2**，固定运行代码`c81fec17a39249dc733405ef842881d3bbb44c3f`；[新包](E:/Project/yanzhou-godot/build/development-batch-02/windows/Yanzhou.exe)、[193项包指纹](E:/Project/yanzhou-godot/evidence/development-batch-02/build/package-manifest.json)、[集成报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-11-batch-02-integration.md")、[四状态对照板](E:/Project/yanzhou-godot/evidence/development-batch-02/captures/index.html)。内容完整性／真实反馈／故障输入保护／参数化恢复的局部续作，仍EX-001；主工程133项、两档各13项输入、跨进程拍末恢复和10张原生尺寸截图通过。原0.1包、原证据和453文件保全未变；ReadyForScope仅限本批技术范围。CORE-060正式交互、EX-002完整单战、正式美术及独立人员接手仍未验收，不等于117项全通过。uses仍为AS-G002-010@BATTLE-3D-02，无资产改版、无新DM或公开发布。

- 2026-10-12第五批源码增量：GODOT-EX002-BATCH05-SOURCE，固定7a5b55daadfe0ffdf4ff81cb209d7beec43d7759，[实际报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-batch-05-integration.md")、[固定证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-05-evidence.json)。完整单战、事件恢复、正式操作、固定字体、摘要与基础音画／设置，340项主工程、两档各32＋22项技术检查及胜败／跨进程恢复通过。uses新增AS-G002-011@FONT-ASSETS-01、AS-G002-012@SYNTH-AUDIO-01；AS-G002-010原固定GLB不变。没有导出新包，正式音画／真人体验未验，第04轮边界按现行规则解释后恢复开发；旧包及证据原样保留。

- 2026-10-12后续包：**GODOT-EX002-0.3**，固定运行源码9cf9b64b34f689a71c3a0362db25917b93259ddf、设计输入5518fde；[Windows包](E:/Project/yanzhou-godot/build/development-batch-05/windows/Yanzhou.exe)、[固定包证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-05-release-evidence.json)。增加非暂停新揭示提示并完成本批包验收：主工程340项；独立复制包旧案例7次、完整界面10次运行，两档各32项键鼠及31项音画检查、胜败／跨进程恢复通过。包与复制目录各195文件、232,308,612字节且逐文件指纹一致，两份字体OFL原字节随包。uses为AS-G002-010@BATTLE-3D-02、AS-G002-011@FONT-ASSETS-01、AS-G002-012@SYNTH-AUDIO-01；ReadyForScope仅限本批技术范围，正式美术／音色、真人体验和独立机器重建未验。原包与失败证据保留，无新DM或公开发布；第六批曾因失焦政策R7暂停，后续用户选择及CORE-062集成已闭合，设计确认不改变此固定包的运行范围。

- 2026-10-12后续包：**GODOT-EX002-0.4**，固定运行源码9c50458a56a38f0c6ebd001d9e6a3ef34382adaa、设计abe8869；[当前Windows包](E:/Project/yanzhou-godot/build/development-batch-06/windows-02/Yanzhou.exe)、[固定证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-06-release-evidence.json)、[实际范围（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-batch-06-integration.md")。新增失焦暂停、公开插图卡面和运行材质样板，修复读数遮挡；346项核心、独立复制包旧案例7次／完整界面12次／失焦2次运行通过，两档各32项UI／31项表现／19项卡面／53项失焦检查。包与副本各195文件／238,983,705字节，指纹、原OFL及来源说明一致；uses新增AS-G002-009三张原图，其余AS-G002-010／011／012固定版本保持。ReadyForScope仅限本批技术范围；正式音画、真人体验、完整性能、实际断网及独立机器未验，原包／失败与453文件保全保持。仅本地内部交付，无新DM或公开发布。

- 2026-10-12第七批测量复用：沿GODOT-EX002-0.4固定源码9c50458叠加工程仪器，保存于实现57e95441fa497f30d5f857419724fd02dae98fd5；[限定性能报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-batch-07-performance.md")、[固定证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-07-performance-evidence.json)。193文件测量包指纹复核一致，复用原GLB／卡图／字体／声音，无素材改版。1080p连续600秒因一次113.127ms尖峰判Fail；768p 120秒仅为通过预算的诊断。不是新玩家版本、最终最重场景验收或公开发布，原0.4包及证据保留。

- 2026-10-12第七批组合候选保全：实现e0077ffa10d22ad1c9dd91e8037aa2c021409098，沿相同AS-G002-009卡图、AS-G002-010原GLB、字体及声音，增加卡图准备/复用及木纹/皮革代码组件SURFACE-DETAIL-CANDIDATE-02；不改源素材、不新分配AS。候选包和副本各195文件/239,109,709字节，指纹一致；[保全索引](E:/Project/yanzhou-godot/docs/coordination/development-batch-07-preserved-evidence.json)。组合包限定检查未全部完成，600秒测量因系统前台变化中断，不登记0.5正式交付。用户随后明确要求主交互依赖3D模型及真实桌面翻牌，当前暂停待第07轮设计对接；材质样板与旧HUD技术结果不构成新主交互或美术采纳。原包/素材/失败记录及复用权利保持。
- 2026-10-13第八批首批预览：**GODOT-PHYSICAL-B08-PREVIEW-01**，运行源码`ed982ec2b7122310bc415c0a868d87089246618e`，设计计划`c646447762b7c712b58da7bd998e28bfad816398`；[Windows本机预览](E:/Project/yanzhou-godot/build/development-batch-08/preview-01/windows/Yanzhou.exe)、[限定集成报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-13-batch-08-integration.md")、[固定证据与包哈希](E:/Project/yanzhou-godot/docs/coordination/development-batch-08-evidence.json)。首个真实桌面／稳定卡片身份、G02守护链、精确筹码与消费锁、已绘无底板近观；核心352项、两档各38项限定引擎检查。输入采用引擎注入，OS失焦、完整新单战、正式材质和性能未验；ReadyForScope仅限本批本机技术审查，不登记0.5正式成品。uses沿AS-G002-009原三图、AS-G002-010@3D-02、AS-G002-011字体、AS-G002-012程序声；AS-G002-013确认图仅制作对照，不作为全屏贴图；结构参照DM-G002-012@HTML-05。新增程序筹码／卡片／局部光效随本DM登记；源GLB／PNG不改字节，原件、0.4包、0.5候选及失败证据保留，无新AS、无公开发布。

### <a id="dm-g002-004"></a>DM-G002-004 炼咒试验台（2026-10-02新增）

- 归属：game-002-optimization / DIR-032；[探索与机制规格](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-032-playable-mechanism-loop/README.md)、[开发索引](../../yanzhou/development/README.md)。
- 类型／用途：两战最小可玩Demo；TL-1生产、卡牌试点、队列、维护／增幅、临时路由、跨战奖励与携带。
- 固定版本：DIR032-0.1，外部Git提交`afc6e4e0454bb3e306a49899022c340faabb5941`；[单文件Demo](E:/Project/yanzhou-tl1-demo/demo.html)、[操作／构建说明](E:/Project/yanzhou-tl1-demo/README.md)、[逐文件SHA-256](E:/Project/yanzhou-tl1-demo/manifest.json)。本机预览`http://127.0.0.1:8765`仅为本次会话入口，不替代固定版本。
- Archived / PresentLocal（外部原件保留；2026-10-04退出当前候选）；原ReadyForScope记录；2026-10-02已实际运行22项规则检查、6组固定输入两战试跑，并通过浏览器操作完成基础→增幅与辉核→辉核；[证据及限制](E:/Project/yanzhou-tl1-demo/evidence/verification.md)。真人体验、完整路线及平衡未验证。
- 来源／复用：本任务自制代码、CSS占位图形及验证附件；uses: None，derived-from: None，不引用其他方向资产或旧代码。可在本项目继续改作，未另授公开分发许可证；系统字体不随包分发。代码已本地Git保存，尚无远端仓库，不等于已公开发布。
- 设计边界：Q1–Q16只确认DIR-032试点，未回写主系统。未含付费干涉能力、完整路线／商店、复杂修饰或完整发行池。单文件构建无网络依赖；浏览器保存按来源隔离，下载事件未核验，可复制JSON导出已核对。

### <a id="dm-g002-005"></a>DM-G002-005 效果语言与卡面展示稿（2026-10-02新增）

- 归属：game-002-optimization / DIR-032；[用途、来源与资格边界](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-032-playable-mechanism-loop/README.md)、[EL-01设计候选](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-032-playable-mechanism-loop/UI-2026-10-02-effect-language.md)。
- 类型／用途：可操作UI展示稿，评审八配方、战前／战中词卡显示、关键词释义、时间／费用与资源状态；不运行战斗。
- 固定版本：EL-01，外部Git 22950acae3bbe805432a7bd4449364c9c33bc016，文件范围ui-language/；[单文件入口](E:/Project/yanzhou-tl1-demo/ui-language/index.html)、[操作与检查记录](E:/Project/yanzhou-tl1-demo/ui-language/README.md)。本机预览http://127.0.0.1:8766/仅为当前入口。
- Archived / PresentLocal（外部原件保留；2026-10-04退出当前候选）；原ReadyForScope记录；2026-10-02实际浏览器核对四页签、八配方和主要呈现交互，查看两张截图；真人可读性与窄屏实测未做。设计仍Raw候选，Q17只确认词卡展开方式。
- 来源／复用：本任务原创HTML、CSS图形、脚本及截图，无第三方美术；官方参考只使用链接和方法归纳。允许本项目继续改作，公开分发许可未另定；本地Git保存，无远端发布。
- 关系：uses: None；derived-from: None。概念／参数参照DM-G002-004@afc6e4e0454bb3e306a49899022c340faabb5941，未导入其运行代码或存档；既有可玩Demo文件未改变。

### <a id="dm-g002-006"></a>DM-G002-006 卡牌与法杖设计卡册（2026-10-02新增）

- 归属：game-002-optimization / DIR-032；[方向与来源边界](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-032-playable-mechanism-loop/README.md)、[开发索引](../../yanzhou/development/README.md)。
- 类型／用途：独立可编辑HTML卡册；46条基准内容涵盖卡牌、通用法杖、词条／状态与基础规则，支持形象、效果、属性编辑、基准对照和候选草稿备份。
- 固定版本：ATLAS-01；外部Git 24f191946f9acd3413aae26dce0d67fed73c0574，文件范围atlas/；[单文件入口](E:/Project/yanzhou-tl1-demo/atlas/index.html)、[操作与检查](E:/Project/yanzhou-tl1-demo/atlas/README.md)。本机预览http://127.0.0.1:8767/为当前入口。
- Archived / PresentLocal（外部原件保留；2026-10-04退出当前候选）；原ReadyForScope记录（设计工具）；2026-10-02通过6项数据检查、实际浏览器保存刷新／对照／复制／导入拒绝与恢复／撤销／词条跳转，两张截图已查看。真人可读性、窄屏与跨浏览器未验；HTML下载完成事件超时，未核验导出文件落盘；JSON可见文本备份与导入已验证。
- 来源／关系：本方向P、EL-01及用户直接制作授权；DM-G002-004@afc6e4e0454bb3e306a49899022c340faabb5941与DM-G002-005@22950acae3bbe805432a7bd4449364c9c33bc016仅作概念／参数／表达参照。uses: None；derived-from: None；未导入引擎、存档或资源文件。
- 复用／边界：原创HTML、CSS、SVG、脚本和截图，无第三方美术；可在本项目改作，公开分发许可未另定。本地Git保存，无远端发布。草稿保持候选，不自动改写战斗或主系统；既有Demo与EL-01未变。

### <a id="dm-g002-007"></a>DM-G002-007 炼金系统构筑展示册（2026-10-02新增）

- 归属：game-002-optimization / DIR-033；[方向、设计与资格边界](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-033-alchemy-system-redesign/README.md)、[开发索引](../../yanzhou/development/README.md)。标签：炼金系统、真实实体、自由装拆、类型连线、效果协同。
- 类型／用途：可操作机制与卡牌展示册；30种卡、3套系统，战前有限库存装配／拆解／连接、配方成本预览、草稿保存恢复和冻结局部账本。不执行任意草稿或完整战斗。
- 固定版本：ALC-ATLAS-01.1，独立外部Git提交`887bfebaad384d2276e8b51fb742caec8e475c0e`；[私有远端固定目录](https://github.com/dsaj4/yanzhou-alchemy-atlas/tree/887bfebaad384d2276e8b51fb742caec8e475c0e)，文件范围为该提交全部18文件，含源码、数据、单文件与检查／截图证据。[单文件入口](E:/Project/yanzhou-alchemy-atlas/alchemy-atlas.html)、[运行依赖与操作](E:/Project/yanzhou-alchemy-atlas/README.md)、[数据指纹](E:/Project/yanzhou-alchemy-atlas/manifest.json)。本机预览http://127.0.0.1:8770/只为当前入口。
- Archived / PresentLocal（外部原件保留；2026-10-04退出当前候选）；原ReadyForScope记录；2026-10-02已实际浏览器核对HTTP模块入口，12组程序检查通过，数据与DIR-033镜像SHA-256一致；[浏览器证据](E:/Project/yanzhou-alchemy-atlas/evidence/browser-review.md)、[程序报告](E:/Project/yanzhou-alchemy-atlas/check-report.json)。私有远端已同轮推送成功；需仓库权限，不等于公开网站发布。
- 未验／限制：单文件同数据与脚本语法检查通过，内置浏览器安全策略拒绝file://，直接双击运行未验；下载落盘、窄屏、跨浏览器、存储故障、完整战斗与真人体验／平衡未验。三账无敌伤与环境补给，不能推断持续供料或有效策略平衡。
- 来源／关系：本轮自制HTML、CSS、SVG、脚本与截图，无第三方图片／字体导入。概念输入固定为主系统＋DIR-031／032文本@`0702a146ccd079b28d7fb939b7297e47f8d5a27e`；uses: None；derived-from: None。未导入DM-G002-004／005／006的引擎、存档、代码或图片。
- 复用／设计身份：可在本项目继续改作，公开分发许可未另定；系统字体不随包分发。新增卡义／端口Raw候选，Q1–Q3只确认术语、战前构筑和有成本协同。展示完成不等于正式素材资格、主系统采纳或体验成立；[下一轮交接](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-033-alchemy-system-redesign/handoff.md)。

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

### <a id="dm-g002-009"></a>DM-G002-009 藏器与咒式（2026-10-06新增）

- 归属：game-002-optimization / DIR-037；[方向与权威登记](../../yanzhou/exploration/DIR-037-effect-framework/README.md#dm-g002-009-藏器与咒式)。
- 类型／用途：仅5件示例法器与5张行动卡的展示册；铭刻与生产信息、词条解释、产出／来源跳转及固定条件读法。
- 固定版本：EFFECT-ATLAS-01；外部本地Git df2af4310a27afc23f433323902c7a0ed5596795；离线入口（原路径`E:/Project/yanzhou-effect-atlas/index.html`，2026-10-18本机缺失）、操作／技术说明（原路径`E:/Project/yanzhou-effect-atlas/README.md`，2026-10-18本机缺失）、文件清单与SHA-256（原路径`E:/Project/yanzhou-effect-atlas/manifest.json`，2026-10-18本机缺失）。[本机预览](http://127.0.0.1:8771/)仅为会话入口，未公网发布。
- ReadyForScope（本机交互展示）／PresentLocal；2026-10-06实际浏览器检查页签、详情、词条、双向跳转、蓄言／承句／封缄情境、键盘和桌面／窄屏布局。检查与截图（原路径`E:/Project/yanzhou-effect-atlas/evidence/verification.md`，2026-10-18本机缺失）。真人理解、跨浏览器及玩法平衡未验证。
- 来源／关系：本方向R1@0457eeeb9177c0faafdf9c360e156797832baef0和用户明确制作授权；原创页面与内嵌矢量图，无第三方资源或外部依赖。uses: None；derived-from: None；未导入退役Demo。
- 复用／边界：可在本项目改作，公开分发许可证未另定；外部实现仅本地Git保存。本册没有战斗模拟或其他卡册；名称、配方与数值为Illustrative，设计Raw / Unqualified、玩法NotRun，不因交付成为主系统规则。

### <a id="dm-g002-010"></a>DM-G002-010 战斗HTML结构示意（2026-10-11新增）

- 归属：game-002 / main；[当前交付与本机入口](../../yanzhou/visual/battle-ui-2026-10-11/v10-outline.md)，BATTLE-UI-HTML-10，抽屉向桌内展开、两主体与时间轴中点居中，保留前沿四件法器本体；固定文件及SHA-256见交付页所链manifest。[v09及其检查](../../yanzhou/visual/battle-ui-2026-10-11/v09-outline.md)和原件保持原版本，不覆盖。
- ReadyForScope（3D界面轮廓位置评审）/ PresentLocal；2026-10-11实际Edge检查抽屉在桌内、主体与轴中点居中、刻位对称、四法器、面板删除、桌上物件、空位、三档宽度及HTTP／离线入口，1366预览目视检查完成。当前仅描位，无交互、战斗数据或模型；整体UI仍待评审，玩法NotRun。
- 来源：用户要求HTML并明确仅轮廓描位；uses: AS-G002-005@v02（对齐结构）、AS-G002-006（既有构图）、AS-G002-007（桌面与桌沿关系），derived-from: None（外部代码）。自制单文件HTML内联SVG，无外部依赖，不嵌入第三方图像或字体。可在本项目改作，对外分发许可未另定。原件位于本机持久演示目录，未公开发布。
- 后续使用：[AS-G002-008](../../yanzhou/visual/battle-ui-2026-10-11/art-v01.md)以HTML v10为构图骨架生成独立效果图；HTML原件与固定版本未改。

### <a id="dm-g002-012"></a>DM-G002-012 战斗卡片交互HTML（2026-10-12新增）

- 当前修订：PHYSICAL-CARD-HTML-05；[HTML](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v05.html)、[动作修订说明](../../yanzhou/visual/physical-table-2026-10-12/card-flow-html-v05.md)、[固定清单](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v05-manifest.json)、[限定复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/physical-table-2026-10-12/card-flow-html-verification-v05.md)。derived-from：本资源@HTML-04及用户两点简化要求；法器完工一次亮光后原刻位浮现，使用牌原位亮起且真实目标同步局部特效。21情境不变，Catalogued / PresentLocal，浏览器未验；对应AS-G002-013@ART-02；HTML制作时阶段4未开始，2026-10-13首批真实接入见DM-G002-011本轮记录，HTML浏览器结论不变。

- 旧版保留：PHYSICAL-CARD-HTML-04，game-002 / main；[HTML](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v04.html)、[说明](../../yanzhou/visual/physical-table-2026-10-12/card-flow-html-v04.md)、[manifest](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v04-manifest.json)、[检查](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/physical-table-2026-10-12/card-flow-html-verification-v04.md)。derived-from：本资源@PHYSICAL-CARD-HTML-03，固定输入`20b92ec65fa66219ec8b2a4f7dd5c1a6d63d9ba8`及用户同步悬浮批注；只补齐双方棋子状态近观。Catalogued / PresentLocal，浏览器未验；原回放与消费锁沿v03，HTML交付时阶段3／4未开始，复用条件沿v01。后续阶段3已生成[AS-G002-013首批效果图](../../yanzhou/visual/physical-table-2026-10-12/art-v01/README.md)，仅作结构参照使用，不改本HTML固定版或浏览器结论。

- 旧版保留：PHYSICAL-CARD-HTML-03，game-002 / main；[HTML v03](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v03.html)、[文字增补与来源](../../yanzhou/visual/physical-table-2026-10-12/card-flow-html-v03.md)、[固定清单](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v03-manifest.json)、[本轮检查](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/physical-table-2026-10-12/card-flow-html-verification-v03.md)。derived-from：本资源@PHYSICAL-CARD-HTML-02，固定输入`1d6b151f4634383d7ea7f5ec80873171e89cb447`及用户四条批注／消费锁答复。右正向／左负面筹码，悬停／焦点精确读数，卡牌与空抽屉无底板；消费锁在独立示意中可操作，原20回放保持只读。Catalogued / PresentLocal，浏览器未验；阶段3／4未开始，自制及项目内复用条件沿v01。

- 旧版保留：PHYSICAL-CARD-HTML-02，game-002 / main；[HTML v02](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v02.html)、[说明与用户原话](../../yanzhou/visual/physical-table-2026-10-12/card-flow-html-v02.md)、[固定清单](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v02-manifest.json)、[本轮检查](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/physical-table-2026-10-12/card-flow-html-verification-v02.md)。derived-from：本资源@PHYSICAL-CARD-HTML-01；固定输入`9be040292d64f3b15f24bb746c42951cb1c7ba36`及本轮两条直接浏览器批注。筹码分居双方棋子左右、法器与材料／预计产物悬浮近观、静态拍数圆环。Catalogued / PresentLocal：已制作，浏览器视觉／手势待实测；v01浏览器结论不外推到v02。阶段3／4未开始，自制与项目内复用条件沿v01。
- 归属：game-002 / main；PHYSICAL-CARD-HTML-01；[可操作单文件](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v01.html)、[制作说明](../../yanzhou/visual/physical-table-2026-10-12/card-flow-html-v01.md)、[固定文件及SHA-256](../../yanzhou/visual/physical-table-2026-10-12/card-flow-v01-manifest.json)。DOC-025首条卡片链阶段2，20情境／47个预设帧，包含公开／暗牌、暂停近观、回看、错误和终局。
- ReadyForScope（限定HTML空间与点击路径评审）/ PresentLocal；两档各20情境的实际浏览器布局扫描、关键点击／键盘、暂停、单步、错误重试和结果路径通过，见[总控证据](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/physical-table-2026-10-12/card-flow-html-verification-v01.md)。真实OS失焦、直接file入口、Godot、音频、实际存取及真人体验未验；阶段3／4未完成。
- 来源：用户明确开始制作战斗卡片交互示意；固定设计输入`6d98641eaed3a4c3e063cca2f3484175474408d5`与首条文字结构。uses：DM-G002-010@BATTLE-UI-HTML-10及AS-G002-010@BATTLE-3D-02仅构图／形制说明参考；derived-from：None（外部代码／二进制）。HTML、CSS、内嵌SVG为本轮自制，无外部脚本、图片、下载字体或模型依赖。
- 复用：可在本项目继续制作与改作，对外分发许可未另定。原件与截图在本仓库按清单固定；预览仅本机回环服务，无公开发布。旧HTML v10、图片、模型及Godot工程未修改；不把预设帧视为规则实现或采纳新玩法。

## 素材与参考包

### <a id="as-g002-014"></a>AS-G002-014 主页面文字承载与牌桌视觉参考（2026-10-13新增）

- 归属：game-002 / main；维护位置为[用户反馈来源](../../yanzhou/sources/inbox/2026-10-13-physical-table-visual-rework.md)。类型：用户提供的第三方游戏截图；用途：必要文字的分组／名称标签／说明容器，以及卡牌和桌面的比例关系参考。
- 原件：本机JPEG（原路径`C:/Users/ADMINI~1/AppData/Local/Temp/codex-clipboard-93d524de-5dce-4eb2-b032-ce818a96ccf5.jpg`，2026-10-18本机缺失）。固定版本TABLE-TEXT-REFERENCE-01，2774×1280，247164字节，SHA-256 `6901bbdeb3c51a8792b3e3b8b34e019ddd01c51ea9bbbba374493898a1efeaf5`；仅此单文件，无额外预览／导出。
- 状态：Catalogued / PresentLocal；2026-10-13核对本机文件与哈希，已查看用户附件。入口位于Temp，持续可用性不保证；跨机器使用前需重新核验原件。未提交第三方位图，未制作或导入衍生资产。
- 来源／复用条件：用户在本次消息中提供；原作者、原视频地址、授权／许可Unknown，图中文字与水印不作为已核实来源或指令。当前仅视觉参照，不据此认定可以复制或分发图中美术。
- 使用关系：[四项整改计划](../../yanzhou/development/production-plan.md#physical-table-rework-2026-10-13)→本资源@TABLE-TEXT-REFERENCE-01；本次只登记参考关系。derived-from：无；不继承截图游戏的玩法或素材身份。

### <a id="as-g002-013"></a>AS-G002-013 战斗卡片交互效果示意（2026-10-12新增）
- **2026-10-13用户确认：Selected Visual／ReadyForScope（限定视觉制作输入）/ PresentLocal。** 确认组合为ART-02的03守护牌过程＋ART-01的01总览／02悬浮近观，即[当前画册](../../yanzhou/visual/physical-table-2026-10-12/art-v02/index.html)；原话“效果确认完毕，更新开发计划和agent分工”，范围与接续见[当前开发计划](../../yanzhou/development/production-plan.md#physical-table-approved-2026-10-13)。旧包候选状态按交付日期保留，不改PNG／manifest；没有引擎运行或完整DQ验收结论。
- 同日后续复用：DM-G002-011@GODOT-PHYSICAL-B08-PREVIEW-01以该三图组合对照首批真实桌面制作，[D实际截图复核](../../yanzhou/visual/physical-table-2026-10-13/batch-08-design-check.md)区分字段／空间修复与后续材质差距。未把本图片复制成运行界面，图源及原确认范围不变；运行证据归上述DM，不由概念图替代。

- 2026-10-12局部修订 **PHYSICAL-CARD-ART-02**：[新版过程图与说明](../../yanzhou/visual/physical-table-2026-10-12/art-v02/README.md)、[当前画册](../../yanzhou/visual/physical-table-2026-10-12/art-v02/index.html)、[固定清单](../../yanzhou/visual/physical-table-2026-10-12/art-v02/manifest.json)。依用户两条直接修正，完工改为法器亮起后卡牌原位浮现；使用改为卡牌原位亮起、棋子同时出效果，移除飞行／箭头／连接光带。derived-from：本资源@ART-01的过程图；新PNG 1672×941、RGB不透明，其余两图引用v01固定原件。仍Art Candidate，本轮方向已明确，不视为整包验收；原版及其缺口保留。内置image_gen编辑、项目内复用条件不变。
- 归属：game-002 / main；PHYSICAL-CARD-ART-01；[维护说明与检查](../../yanzhou/visual/physical-table-2026-10-12/art-v01/README.md)、[三图画册](../../yanzhou/visual/physical-table-2026-10-12/art-v01/index.html)、[实际提示词](../../yanzhou/visual/physical-table-2026-10-12/art-v01/prompts.md)。类型：静态效果示意／事件分镜；DOC-025阶段3首批候选。
- 固定输入：设计提交9ef30c702d81fa2b38d7db28018796a32c8db07b；三张PNG均1672×941、RGB不透明；原图、说明、画册及提示词六文件的版本／SHA-256见[manifest](../../yanzhou/visual/physical-table-2026-10-12/art-v01/manifest.json)。工具原始生成输出保留，选定三图复制入本项目。
- Catalogued / PresentLocal / Art Candidate；2026-10-12已逐图目视、图像解码、哈希与来源检查。覆盖第0拍桌面、四类悬浮近观及G02守护牌过程；遗漏字段、道具一致性与未覆盖情境见维护说明。未认定完整阶段3通过、用户接受或引擎实现。
- derived-from：AS-G002-008@BATTLE-UI-ART-01（材质／道具／光照改作）；uses：DM-G002-012@PHYSICAL-CARD-HTML-04（结构与状态）、AS-G002-010@BATTLE-3D-02（仅窄牌透视说明）。内置image_gen生成，未使用CLI；旧PNG、HTML、模型未改，本轮未复制模型或第三方原件。
- 用户授权本项目效果示意生成和继续评审改作；对外分发许可未另定，上游参考权利保持。本轮只是静态图片包，未公开部署或导入Godot，浏览器／运行／体验状态不提升。

### <a id="as-g002-011"></a>AS-G002-011 Noto 简体中文与符号字体来源（2026-10-12新增）

- 归属：game-002 / main；FONT-ASSETS-01；维护于[实现报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-bundled-font.md")，固定来源与完整SHA-256见[字体清单](E:/Project/yanzhou-godot/docs/coordination/font-assets-v01.json)。类型：第三方字体原件／许可证；已用于DM-G002-011@GODOT-EX002-0.3的中文及类别符号，Windows包与独立复制目录均已运行检查。
- 固定范围：Noto Sans CJK SC Regular 2.004（官方提交523d033d6cb47f4a80c58a35753646f5c3608a78，OTF 16,437,364字节）与Noto Sans Symbols 2 Regular 2.008（官方提交25b00f0d3f40873a005287514ba2a48558655314，TTF 671,568字节）。原始下载及两份OFL保留在实现仓库evidence/development-batch-05/fonts/source/，清单给精确文件路径；未修改、子集化或转换，原ZIP亦保留。
- ReadyForScope（固定来源恢复、源码接入与随包技术检查）/ PresentLocal。2026-10-12完成两种PowerShell各17项恢复检查，480个检查汉字及▲■⊘✱组合无缺字；两档实际Godot及独立复制包禁系统回退检查与截图通过。原字体共约16.32 MiB，0.3整包约221.55 MiB；字体增量内存和真人小字号可读性未验。
- 来源：官方notofonts/noto-cjk与notofonts/symbols，OFL-1.1；按许可证保留版权／许可、字体不可单独售卖，具体声明见实现清单。未取用系统雅黑文件，未公开发布二进制。此字体许可不改变模型等其他资产的权利边界。
- uses: None；derived-from: None（未经修改第三方原件）；使用者DM-G002-011@GODOT-EX002-0.3，固定运行源码9cf9b64b34f689a71c3a0362db25917b93259ddf，复制到godot/assets/fonts；两份原字节OFL也随EXE提供，实际哈希核对通过。来源及早期7a5b55d检查保留；本条登记局部技术范围，不证明成品或玩法成立。

### <a id="as-g002-012"></a>AS-G002-012 程序合成声音样板（2026-10-12新增）

- 归属：game-002 / main；SYNTH-AUDIO-01；维护于[第五批实现报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-batch-05-integration.md")，[来源与14组PCM指纹](E:/Project/yanzhou-godot/docs/coordination/synth-audio-v01.json)。类型：原创程序合成效果／环境声音技术样板，非正式音色。
- 固定版本：实现提交7a5b55daadfe0ffdf4ff81cb209d7beec43d7759，godot/EncounterAudio.cs，SHA-256 77cb7499590fe6e8e9f5d65d9247a761d3f03594cea8ff855bd730c6a84baa3b。由正弦谐波和包络在启动时生成22050Hz单声道PCM16，不下载录音、不访问用户音频、不导入旧游戏资产；14组包括尚未派发的胜败预备波形。
- Catalogued / PresentLocal，2026-10-12实际引擎混音有信号／静音零及声音暂停／恢复生命周期通过；9cf9b64／0.3独立复制包已接通非暂停新揭示并留实际音频信号与图像证据，原7a5b55d停点尚未接通的记录保留。胜败音在EX-002依CORE-061无可听运行触发，不把资源存在当运行通过；听感、音色和正式DQ-31未验。
- 来源／使用：本次项目原创实现，无外部录音或第三方音频依赖；不新增通用公开许可。uses: None；derived-from: None；使用者DM-G002-011@GODOT-EX002-0.3，固定运行源码9cf9b64。后续增加诊断／接线未改变14组PCM字节，当前源文件与PCM核对见清单；同项目后续复用按固定版本与合同核对。Windows包仅本机保管，无公开发布。

### <a id="as-g002-010"></a>AS-G002-010 战斗桌面 Blender 建模首版（2026-10-11新增）

- 归属：game-002 / main；当前BATTLE-3D-02；[v02交付、预览及证据](../../yanzhou/visual/battle-ui-2026-10-11/model-v02.md)。按用户要求调整透视与窄卡型；原生 `.blend`、20份组件集合库、含主相机的 `.glb`、四张卡面纹理及四张检查渲染另存 `E:/Project/yanzhou-battle-3d/v02/`。固定范围和逐文件 SHA-256 见交付页链接的 manifest。[v01及其十张原检查图](../../yanzhou/visual/battle-ui-2026-10-11/model-v01.md)保持原文件与原哈希。
- ReadyForScope（静态三维结构与视觉评审）/ PresentLocal；2026-10-11检查源工程重开、纹理打包、GLB回导与几何尺寸、主视角及近景。真实几何已建立，雕饰为首版简化；原生约61.4万三角面，米制，Blender Z-up／GLB Y-up，无骨骼动画，实时预算 Unknown。
- derived-from（视觉改作）：AS-G002-008@BATTLE-UI-ART-01、AS-G002-009@BATTLE-COMPONENTS-01；uses：DM-G002-010@BATTLE-UI-HTML-10（构图），AS-G002-009的11–14卡面PNG（直接纹理）。其余物件效果图仅参照，模型/程序材质本轮自制。程序纹理与体积雾在GLB中简化，未宣称等效材质或目标引擎通过。
- 用户授权真实建模与本项目评审改作；上游对外分发许可 Unknown。二进制和制作脚本就地保管，未公开上传；登记不等于美术采纳、战斗实现或玩法验证。
- 2026-10-11复用：DM-G002-011@GODOT-EX001-0.1实际复制BATTLE-3D-02 GLB到Godot工程；源SHA-256与原件一致。临时组件变体只用于重导入夹具，交付包恢复源版本；[代码与实际范围](E:/Project/yanzhou-godot/evidence/verification.md)。此复用不升级原美术采纳或公开分发条件。
- 同日0.2续作沿用相同GLB字节，新增[固定依赖清单](E:/Project/yanzhou-godot/docs/coordination/runtime-assets-v01.json)与[参数化恢复检查（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-11-runtime-assets.md")，两种PowerShell环境各22项通过；新目录恢复副本仅为运行依赖／技术夹具，源原件和资产版本不变。中文字体、正式卡面、音频／动画与实时材质仍有缺口，权利条件沿原登记。
- 2026-10-12第六批复用：DM-G002-011完整单战在相同BATTLE-3D-02原GLB上挂接运行材质／灯光代码小样RUNTIME-ART-SAMPLE-01，固定实现9c50458a56a38f0c6ebd001d9e6a3ef34382adaa；[限定报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-12-batch-06-art.md")。18项资源隔离／恢复检查及两档四张实际前后对照通过，14种材质／540个surface，原几何、贴图和源件不变；木纹、皮革细节及晶球体积未还原。不形成独立模型分支，代码组件随DM登记，不新分配AS；原美术／分发资格不变。

### <a id="as-g002-009"></a>AS-G002-009 战斗组件隔离设计 v01（2026-10-11新增）

- 归属：game-002 / main；BATTLE-COMPONENTS-01；[独立图片、提示词、总览与检查](../../yanzhou/visual/battle-ui-2026-10-11/components-v01/README.md)。固定文件范围、规格及SHA-256见该页所链manifest。
- ReadyForScope（组件外观评审）/ PresentLocal；19张PNG，其中18张RGBA透明组件、1张RGB环境图；2026-10-11检查文件解码、alpha、哈希及浏览器合成显示。
- 用户授权内置image_gen逐项生成；derived-from / uses: AS-G002-008@BATTLE-UI-ART-01。源图已由用户选定为效果示意图初版；独立组件为本轮重绘设计参考，源图与HTML未改。用于后续外观评审与建模参考，不是三维资产或玩法采纳。
- 本项目可继续改作；对外分发许可未另定，上游参考权利沿源登记保留。原始生成输出保留，19张最终图片入库，无公开部署；本机总览源在交付页指定的持久目录。
- 2026-10-12第六批直接复用：DM-G002-011完整单战复制11牌背、12火焰、13护盾三张原PNG作运行卡面插图，字节不改；[固定文件清单](E:/Project/yanzhou-godot/docs/coordination/card-art-v01.json)，使用实现9c50458a56a38f0c6ebd001d9e6a3ef34382adaa。状态／名称／数值由真实公开内容另绘，图片不新增元素规则；两档公开信息、长名／两位数、同拍双牌和按住检查通过。未复制水浪独立插图或重绘新图，原19图版本／权限不变。

### <a id="as-g002-008"></a>AS-G002-008 战斗效果图 v01（2026-10-11新增）

- 归属：game-002 / main；BATTLE-UI-ART-01；[原件、提示词与交付说明](../../yanzhou/visual/battle-ui-2026-10-11/art-v01.md)。PNG 1672×941，RGB不透明，固定文件和SHA-256见交付页所链manifest。
- ReadyForScope（概念图评审）/ PresentLocal；2026-10-11实际核对解码、规格、哈希及构图。用户授权内置image_gen独立生成；uses: DM-G002-010@BATTLE-UI-HTML-10（布局）、AS-G002-006（风格）；原参考图和HTML未修改。
- 2026-10-12后续视觉改作：[AS-G002-013@PHYSICAL-CARD-ART-01](../../yanzhou/visual/physical-table-2026-10-12/art-v01/README.md)将本PNG作为材质／道具／光照图像输入，结构沿HTML v04；本源件字节不变。
- 用户2026-10-11已选定为效果示意图初版；后续使用者为[AS-G002-009组件隔离设计](../../yanzhou/visual/battle-ui-2026-10-11/components-v01/README.md)，尚未建模或验证玩法。本项目可继续评审改作，对外分发许可未另定。最终新图已复制入本工作区，原始生成输出保留，未公开部署。

### <a id="as-g002-007"></a>AS-G002-007 桌面承载与边沿布局参考（2026-10-11新增）

- 归属：game-002 / main；[原件、规格与使用记录](../../yanzhou/visual/battle-ui-2026-10-11/v08-outline.md#as-g002-007-桌面承载与边沿布局参考)。用户附件PNG 890×786；SHA-256 `ebe3396be8554bfab425c73514a1bf9a92e5e072ea513fec8c087451cd522db6`。
- Catalogued / PresentLocal；2026-10-11已目视及核对尺寸、哈希。原件在用户临时目录，未复制／推送原图，长期访问未知；作者、原游戏及对外分发权Unknown。
- 用户授权本轮布局参照；使用者DM-G002-010@v08、v09及v10。只参考物件在桌上、操作对象在桌沿的关系，不导入图片、美术或玩法；uses: None；derived-from: None。

### <a id="as-g002-005"></a>AS-G002-005 战斗界面结构线稿包（2026-10-11新增）

- 归属：game-002 / main；[维护说明与三张图入口](../../yanzhou/visual/battle-ui-2026-10-11/README.md)。用途：第一步评审战斗UI位置、信息层级和功能；Raw UI Candidate / Unqualified，未采纳布局，玩法与体验NotRun。
- 当前版本：UI-WF-01 / v02；[六文件范围与SHA-256](../../yanzhou/visual/battle-ui-2026-10-11/manifest-v02.json)，[修订说明](../../yanzhou/visual/battle-ui-2026-10-11/v02-notes.md)。三份可编辑SVG及同名PNG，各1920×1200，不透明白底，无图集关系；[v01固定清单](../../yanzhou/visual/battle-ui-2026-10-11/manifest.json)及图源保留。
- ReadyForScope（仅静态结构评审）/ PresentLocal；2026-10-11核对图像解析、文字边界、三张PNG目视及EX-001指定快照。无交互实现／模型；小屏、真人理解及完整战斗未验证。
- 来源／关系：用户本轮授权，Codex自制线条与文字；游戏文本输入固定提交`19ed8760c6a925914eb7770a38d2ac551e316f7f`，完整读取范围见维护页。v01 uses: None；v02 uses: AS-G002-006@固定SHA-256（仅布局参照）；derived-from: None（外部资产）。SVG使用本机系统字体但不嵌入字体文件；可在本项目改作，对外分发许可未另定。
- 后续使用：DM-G002-010@BATTLE-UI-HTML-03参照v02结构，以HTML重绘，v04／v05／v06／v07／v08继续沿用同刻对齐结构；未导入PNG／SVG文件。

### <a id="as-g002-006"></a>AS-G002-006 用户提供的牌桌布局参考（2026-10-11新增）

- 归属：game-002 / main；[原件位置、来源、规格与使用记录](../../yanzhou/visual/battle-ui-2026-10-11/v02-notes.md#as-g002-006-用户提供的牌桌布局参考)。PNG 1672×941；固定SHA-256 `5b402a3b35d3b1d44d79c316f1fe09251fc440a2f5a8598f3c41603893a5b63f`。
- Catalogued / PresentLocal；2026-10-11目视、尺寸与哈希核对。原件位于用户附件临时目录，未复制／推送原图，长期访问未知；作者、生成来源与对外分发权Unknown。
- 用户授权UI布局参照；使用者AS-G002-005@v02、[DM-G002-010@v04](../../yanzhou/visual/battle-ui-2026-10-11/v04-outline.md)及[v08](../../yanzhou/visual/battle-ui-2026-10-11/v08-outline.md)。原结构稿仅参考空间构图；用户2026-10-11另授权[AS-G002-008](../../yanzhou/visual/battle-ui-2026-10-11/art-v01.md)参考材质、配色与光照生成新图。原图未修改或复制入交付，不继承卡义或玩法；uses: None；derived-from: None。

| ID / 名称 / 标签 | 归属 / 原件入口 | 版本 / 来源条件 | 状态 / 使用边界 |
| --- | --- | --- | --- |
| <a id="as-g002-001"></a>AS-G002-001 05紧凑暗面视觉包；UI、风格 | game-002 / main；[风格说明](../../yanzhou/visual/reviews/2026-09-19/style-guide.md)、[文件清单](../../yanzhou/visual/reviews/2026-09-19/source-manifest.json) | v0.2 / 2026-09-19；基线提交下`yanzhou/visual/reviews/2026-09-19/`的已跟踪文件；生成来源/提示词沿原包，分发条件未审 | Catalogued / PresentLocal；旧RC1 Selected Visual；不能当成TL-1最终布局 |
| <a id="as-g002-002"></a>AS-G002-002 DIR-029完整牌桌v9；概念图 | game-002-optimization / DIR-029；[PNG原件](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-029-timeline-card-battle/ui-concept-v9-full-tabletop.png)、[提示词](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-029-timeline-card-battle/ui-concept-v9-full-tabletop-prompt.txt) | 基线提交下上述两个文件；生成资料，具体生成模型/分发条件本轮未审 | Archived / GitSnapshot（2026-10-04本地原件随方向删除）；原Catalogued / PresentLocal记录；Scene Concept / Awaiting Visual Review，尚非最终生产素材；尺寸等在实际复用前补录 |
| <a id="as-g002-003"></a>AS-G002-003 Godot/Blender实验集合；模型、渲染、概念图 | game-002 / main；[恢复后的仓库入口](E:/Project/game-002-godogen-lab/README.md)、[登记来源](../../yanzhou/development/README.md) | 外部提交`1dd488c507a73933e5f16e9d3829e451b5e37937`；范围与入口见下方恢复记录；依赖见外部工具链锁，逐项分发条件待核实 | Catalogued / **PresentLocal**（2026-10-01用户通知恢复后复查）；旧RC1资产与视觉探索，未认定TL-1兼容或完成美术验收 |
| <a id="as-g002-004"></a>AS-G002-004 DIR-031视觉案例参考包；官方截图、牌桌、炼金工作台 | game-002-optimization / DIR-031；[图文与登记](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-031-visual-form-style/README.md#第4轮五个相邻案例的真实游戏截图)、[来源清单](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-031-visual-form-style/reference-screenshots-v01-sources.json) | v0.1 / 2026-10-02；固定提交`46f8a0ff7813f022e8e4c9b13516f5ba68c2ce98`下`yanzhou/exploration/DIR-031-visual-form-style/`，文件范围仅限清单所列7张图；5张官方Steam截图＋2张既有用户参考图，逐项规格、来源、SHA-256见清单；具体许可Unknown | Archived / GitSnapshot（2026-10-04本地原件随方向删除）；原Catalogued / PresentLocal记录；2026-10-02核对7图哈希及解码，目视核对5张新增官方截图；DIR-031仅作视觉参照，保持Raw / Unqualified，未运行游戏、不授予资产复制改作或商业分发权 |
| <a id="as-sh-001"></a>AS-SH-001 拆解写法参考包；结构、DOCX范例 | shared-reference / media-analysis-lab；[包入口](../../media-analysis-lab/references/writing-examples/README.md) | 基线提交下`media-analysis-lab/references/writing-examples/`的已跟踪文件；结构MD与两份DOCX各自来源/转载条件待核实 | Catalogued / PresentLocal；按原入口只作结构和写法参考；本轮未读DOCX正文或检查版式，不授予复制正文/重发权限 |

素材PresentLocal仅指列出入口/原件存在及已跟踪，不代表已目视审图或核验全部清单。包范围以固定提交内已跟踪文件为限，未跟踪资源不纳入。文件规格、作者和许可缺口保留Unknown；实际复用时按所需范围补齐，不把目录登记当作授权或Qualified素材。

AS-G002-004为2026-10-02的后续登记，使用该行独立固定提交，不适用页首初始登记基线。其来源清单SHA-256为`db79a49078d3a48f95a28b0d45239c662bea0bfc161385847e6bbed1c05c6019`；目视核对范围以该行和方向页记录为准。

2026-10-02使用范围调整：用户决定排除Tainted Grail: Conquest，原话“该案例可以排除，基本没有可借鉴点”。DIR-031当时只使用包内其余6张图（4张官方截图＋2张用户参考图）；被排除截图及v0.1来源清单保留作历史追溯，不再作为当前风格参考。包的固定版本、文件哈希和原采集证据不变。

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
| [DIR-031第4轮](https://github.com/dsaj4/game_design/blob/e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9/yanzhou/exploration/DIR-031-visual-form-style/README.md#第4轮五个相邻案例的真实游戏截图) | AS-G002-004@v0.1 / `46f8a0ff7813f022e8e4c9b13516f5ba68c2ce98` | 当前使用其中6张图；Tainted Grail: Conquest已按用户决定排除，截图仅作历史保存；其余4张官方截图与2张既有用户参考图作视觉参照，不导入实现、不回写现行视觉规范 |

新使用关系写在目标维护文档；此表保留跨资源发现入口，不复制项目参数或验证结论。正式系统与探索方向互相参考后仍保留各自设计版本。

### <a id="dm-g002-008"></a>DM-G002-008 炼金构句重设计展示册退役记录

- 归属：game-002-optimization / DIR-035；2026-10-04按用户决定退役，ID不复用。
- 状态：Archived / PresentLocal（仓库外恢复副本）；原条目与三个未提交文件逐字节保存在 `E:/Project/game-exploration-cleanup-20261004/recovery/`，SHA-256见该目录的上级 `recovery-manifest.json`。
- 原文件范围：DIR-035的README.md、handoff.md、alchemy-showcase.html；未发布这些未提交字节，也未将其登记为已采纳内容。恢复与原来源说明见[清理记录](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/cleanup-report.md#2026-10-04探索方向退役)。


## 待补与维护

- DM-G002-001：完整实现提交、可运行入口与环境、代码/依赖复用条件。
- DM-G002-002：如需跨机器交付，明确持久交付位置、依赖和使用条件；原局部检查保留，不自动重跑。
- AS-G002-001/002及AS-SH-001：按实际使用任务补规格、来源与许可；不为本次登记发布或移动原件。
- AS-G002-003 / DM-G002-003：入口已恢复；实际选用时核对具体子包规格、分发条件及未提交Blender修改，目标环境运行能力尚未重新检查。
- new-roguelike：其[开发索引](../../new-roguelike/development/README.md)当前无登记产物，保持空白，不继承言咒条目。
- 其他方向、历史Demo、已发布布局站点和未跟踪资产未逐项盘点；遇到实际复用需求再登记，不宣称此次收录全部资源。稳定ID归档后保留记录，不重新分配。

## 2026-10-04探索资源退役

用户决定删除现有方向并允许后续重做测试与UI。DM-G002-002、004–008及AS-G002-002、004停止维护，ID与原版本不复用；本仓库原件随方向删除，已提交内容以固定Git取证，未提交内容只保存在仓库外恢复目录。外部实现原件未删除，访问状态未重新验证。历史检查保持原覆盖，不外推到INS-1；详情见[清理记录](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/cleanup-report.md#2026-10-04探索方向退役)。

## 2026-10-11正式开发接入复核

用户已完成界面设计并进入正式开发准备。当前使用DM-G002-010@HTML-10、AS-G002-008@ART-01、AS-G002-009@COMPONENTS-01、AS-G002-010@3D-02；AS-G002-005@v02仅补充同刻对齐语义。用途与实际核验集中见[开发资产接入](../../yanzhou/development/asset-readiness.md)。

本轮逐文件复核5包75文件与原manifest哈希一致，GLB元数据解析及v02主渲染目视完成；未重跑Blender、浏览器、引擎或玩法。接入尚为计划关系，没有把资源复制到运行工程。旧记录中的“未建模／待评审”保留其原日期范围，当前建模入口为3D-02；原件、旧版本及来源／分发条件不变，不新增AS／DM身份。
## 2026-10-14 Demoncards 第一表现参照与真实制作

### <a id="as-sh-002"></a>AS-SH-002 Demoncards 本机游戏与有界取证包

- 2026-10-15追加盘点：[候选与接入优先级（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/coordination/2026-10-15-existing-assets.md")、[固定审计数据](E:/Project/yanzhou-godot/docs/coordination/existing-assets-audit-2026-10-15.json)。主pak哈希未变，旧索引7,811包全部可定位；定向45对象核类型，17纹理内存解码、13模型缓冲候选，无新运行导出。沿本条登记参考，不新分配AS，不把Catalogued升级为整体ReadyForScope；B12已接部分另沿AS-G002-025及下文2026-10-15记录。后续复用默认见[开发规范](../../yanzhou/development/development-standard.md#5-资产接入)。以下2026-10-14边界保留原轮次含义。

- 归属：shared-reference；原件在[E:/Game/Demoncards](E:/Game/Demoncards/verified-2026-10-14/source-manifest-v01.json)，维护说明为[言咒本次限定取证](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-reference-2026-10-14.md)。类型：用户提供第三方游戏、两篇分析报告、OBJ、静态解析、截图／录屏；标签：纸牌、牌桌、UE曲线、材质。
- 固定版本：DEMONCARDS-REFERENCE-2026-10-14-v01，源清单所列10件原物与SHA-256；主pak指纹`c61d079f5a853f51b52b81d1799f8c3595b8a2d079a1d449329af4597075ebd4`。类型化证据指纹`1eb267f32f31c0b00718eb01f176eefc2d4b3fdb01ac4346e0045311ff0d6aa2`；运行帧／媒体位于同包verified-2026-10-14。固定范围为清单和本轮报告明确文件，不把整个可变目录当固定版。
- Catalogued / PresentLocal，2026-10-14核查原件哈希、局部卡网格和31项UE导出；菜单／教程／选牌实际观察，物品成功使用、详情、完整移动触发及精确测时未取得。局部网格600×10.0002×800不等于世界单位，原Card.obj失败拓扑保留，Card_fixed闭合版另列。
- 使用者：DM-G002-013／AS-G002-015／AS-G002-016／DM-G002-011第九批，均为视觉／几何关系参照。uses: None；derived-from: None。原游戏再分发／改作权Unknown；本轮只在用户授权范围本机内部取证，不上传原exe、pak、提取缓存，不向言咒包导入其原始像素／网格／音频／文本。跨项目引用不继承言咒资格、规则或验证。

### <a id="dm-g002-013"></a>DM-G002-013 Demoncards 风格言咒设计交接HTML

- 归属：game-002 / main；维护者既有「言咒设计对接」，[文字结构](../../yanzhou/visual/demoncards-reference-2026-10-14/design-v01.md)、[可操作HTML](../../yanzhou/visual/demoncards-reference-2026-10-14/design-v01.html)、[前三阶段复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/demoncards-reference-2026-10-14/design-review-v01.md)。类型：独立设计原型；标签：牌桌、必要文本、薄纸牌、触发、移动、近观。
- 固定DC-v01，设计包清单SHA-256 `d0154eabed4351613c001cf7ac329a9652807522d5cf879fd9957b16f8ae8212`，[完整范围／逐文件哈希](../../yanzhou/visual/demoncards-reference-2026-10-14/design-manifest-v01.json)。ReadyForScope（两档HTML列明路径）/ PresentLocal，2026-10-14由D实际浏览器核查，记录在清单；非真实规则Demo，真实包单列DM-G002-011。
- uses: AS-SH-002@REFERENCE-v01（视觉参照）、AS-G002-015@DC-ART-01（制作对照）；derived-from: None。沿CORE-063／EX-002的公开／受理／停点，html动作快照不是后端状态依据。原创HTML/CSS/脚本、系统字体不嵌入，可在本项目改作；公共分发许可未另定。来源材料资格与展示衔接见physical-table.2，浏览器通过不等于用户视觉接受或玩法成立。

### <a id="as-g002-015"></a>AS-G002-015 DC-v01 牌桌与动作美术示意包

- 归属：game-002 / main；[原件画册／说明](../../yanzhou/visual/demoncards-reference-2026-10-14/art-v01/README.md)、[预览](../../yanzhou/visual/demoncards-reference-2026-10-14/art-v01/index.html)、[实际提示词](../../yanzhou/visual/demoncards-reference-2026-10-14/art-v01/prompts.md)。固定DC-ART-01，范围由上方DC-v01清单固定。
- 4张选用PNG，1672×940／941，另保留2张失败PNG、布局输入与HTML浏览器证据；不把失败帧替换成成功。02-actions第三帧错误■攻击角标明确排除，正确Move采用04-card-move；图片Q4省略不能改变真实Q5。
- ReadyForScope（D设计制作对照）/ PresentLocal，D已目视候选与列明缺口；内置image_gen生成，用户已授权后续真实制作。uses: DM-G002-013@DC-v01布局、AS-SH-002@REFERENCE-v01仅风格参照；derived-from: None（独立新图）。使用者DM-G002-011／AS-G002-016作为制作参照，未整图贴进游戏。允许本项目继续改作，公开分发许可未另定；不宣称3D资产或真实运行已验。

### <a id="as-g002-016"></a>AS-G002-016 DC 真实牌桌重制几何与自制材质

- 归属：game-002 / main；[B制作报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-14-demoncards-b.md")、[几何源](E:/Project/yanzhou-godot/godot/DemoncardsTableGeometry.cs)、[实际材质源](E:/Project/yanzhou-godot/godot/DemoncardsSurfaceMaterials.cs)。代码在唯一实现仓库；图片原件在godot/assets/demoncards-v01，固定清单为[DC-ASSETS-01](E:/Project/yanzhou-godot/docs/coordination/demoncards-assets-v01.json)／[DC-MATERIAL-TUNE-02](E:/Project/yanzhou-godot/docs/coordination/demoncards-materials-v02.json)，指纹分别`98d8738724ea4ff34cb9ed9bc3f29ef567c4d3e68a9a2846e9b51263f419c843`／`cf92697a73b981fff56b217d501b46849148103e72c63f4c0322386fcd5ab791`。
- 7张v01与8张修订v02 PNG，512×512；PBR RGB木／布／纸、RGBA独立墨绘／完整背纹。薄卡、窄槽、木桌／刺绣布、车制棋子、切面晶体、书页／旧铜器与筹码由代码生成；Godot坐标Y向上，网格／材质依赖随实现说明，不是参考游戏世界单位复制。生成器及重建／指纹校验留实现仓库；旧v01与失败截图完整保留。
- Catalogued / PresentLocal，2026-10-14生成与15图哈希校验；最终两档／包验／D复核按[集成报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-14-demoncards-integration.md")实际范围登记。uses: DM-G002-013@DC-v01、AS-G002-015@DC-ART-01、AS-SH-002@REFERENCE-v01（只参照结构／材质语言）；derived-from: None（独立代码／像素重建）。运行依附AS-G002-010原GLB宿主，原GLB、原卡图字节不改。本项目自制允许内部复用；原游戏像素／网格未导入，公开发布未授权。

使用关系：DM-G002-011第九批真实Godot预览→AS-G002-016实际运行导入；DM-G002-013／AS-G002-015制作对照不作为全屏贴图。旧DM-G002-012、AS-G002-013／014及旧包保留原版本，不以新图覆盖其历史结论。

## 2026-10-14 组件细节重新设计

### <a id="dm-g002-014"></a>DM-G002-014 言咒组件细节HTML

- 归属：game-002 / main；独立维护的组件细化结构稿，derived-from: DM-G002-013@DC-v01（视觉与公开信息结构参照）。[HTML入口](../../yanzhou/visual/component-detail-2026-10-14/design-v01.html)、[19组件规格与操作说明](../../yanzhou/visual/component-detail-2026-10-14/brief-v01.md)、[限定检查](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-detail-2026-10-14/design-review-v01.md)、[交接范围](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-detail-2026-10-14/handoff-readiness-v01.md)。
- 固定YANZHOU-COMPONENT-DETAIL-V01，文件范围与逐项SHA-256见[manifest](../../yanzhou/visual/component-detail-2026-10-14/manifest-v01.json)。Catalogued / PresentLocal，19组件、109状态选择入口（包含共用图形，实际覆盖见state-coverage）；HTML/CSS/SVG/JS内嵌数据，无运行后端。2026-10-14静态结构/脚本检查已做；浏览器file协议策略拒绝，真实打开、布局与输入NotRun。两档布局选择不代表两档浏览器通过。
- uses: AS-G002-017（美术目标）；Demoncards与旧B09仅作造型/材质和问题对照。原创结构稿及确定性几何更正图可在本项目改作；系统字体不嵌入，公开分发许可未另定。非玩法验证、非真实3D、非已接受最终造型；后续工具评估/独立资产/运行绑定按交接范围分别推进。

### <a id="as-g002-017"></a>AS-G002-017 组件细节效果板与提示词

- 归属：game-002 / main；[原件说明](../../yanzhou/visual/component-detail-2026-10-14/art-v01/README.md)、[可放大画册](../../yanzhou/visual/component-detail-2026-10-14/art-v01/index.html)。固定COMPONENT-ART-01，三张v02修订及三张保留v01，6个实际提示词、原生成来源、逐文件SHA-256见[图像manifest](../../yanzhou/visual/component-detail-2026-10-14/art-v01/manifest-v01.json)。
- PNG实际1586×992、非透明底；提示请求2560×1600但工具未返回该尺寸。内置image_gen生成和定向编辑，未上传原游戏资产。覆盖文字/纸牌、法器/棋子/筹码、桌面/控制/装饰三组；只是外观与装配参考，不是模型、PBR图集、动态状态全套或游戏截图。
- Catalogued / PresentLocal。2026-10-14总控与D目视并修正内容/形状/符号；仍有环开口、币局部等生成不一致，排除项及确定性更正见DM-G002-014复核。不将旧稿错误用于运行内容，不整板贴入游戏。uses: DM-G002-014文字与HTML；derived-from: None（新生成包，内部v02分别基于对应v01）；允许本轮言咒制作继续改作，公共分发许可未另定。

## 2026-10-15 四组件生产样件

### <a id="as-g002-018"></a>AS-G002-018 文本框、薄纸牌、环杖与雕木棋子首样

- 归属：game-002 / main。原件就地维护在`E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/sample-v01/`；[制作说明](E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/sample-v01/README.md)、[四样件图册](E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/sample-v01/renders/four-samples-neutral-contact-sheet.png)、[独立复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/sample-review-v02.md)。仅TXT-01、CARD-01、WAND-01、PAWN-01，其他15件不在此版本中。
- 固定COMPONENT-SAMPLES-01，[manifest](E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/sample-v01/manifest.json) SHA-256 `e81b4175ed0d9b0f4ba7a4656ae6a14a87a5e6a5a2832848ed1e765feb3cbd3c`，119文件112614894字节；源Blender SHA `2ba59d4a572d7593faef6f6a25902314a8c9ace1bb3dede7388ee36091f7abb7`。四GLB、可编辑blend、独立PBR/原生SVG、RGBA皮肤与切片、检查报告、失败图和提示词均在清单范围。
- 单位米，C=.063；源Z上，GLB Y上；牌正面+Y/牌顶-Z，棋子正面+Z，无骨骼动画。TXT生产层640×192 RGBA，端夹固定、中央重复，无中文数字；盾墨绘1086×1448 RGBA原图保留，合成牌面属于派生；材质色彩空间、UV/节点/枢轴与独立通道见原件说明和asset-bindings。不是扫描PBR或完整卡种图集。
- ReadyForScope / PresentLocal（仅首批四件限定范围）。2026-10-15总控复核119项字节/哈希全匹配，源重开/GLB回导及D独立Q1/Q2通过；[限定Q3](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/q3-source-04-review.md)通过，源码与Release两档各61/61，48张PNG逐字节相同。[运行交付记录（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-15-component-samples-integration.md")、预览目录`E:/Project/yanzhou-godot/build/development-batch-10/samples-01/windows/`。OS输入、性能与用户最终美术接受未验，其他15件及其他卡种新墨绘不在本限定范围。
- uses: DM-G002-014@YANZHOU-COMPONENT-DETAIL-V01、AS-G002-017@COMPONENT-ART-01（仅设计/外观参照）；derived-from: None（本轮原创网格、程序表面与图形，未复制参考游戏网格或像素）。盾墨绘由内置image_gen新生成，原始提示词和源图保留于同轮illustration-v01且副本纳入本包；允许本项目内部继续改作，公开分发条件Unknown。供DM-G002-011后续限定接入使用，当前不覆盖旧AS-G002-010/016资产。

## 2026-10-15 组件扩量制作登记

以下均归属game-002 / main，用于DM-G002-011后续表现接入；原件根为`E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/`。各包按下列实际状态登记；未固定包的manifest与SHA-256仍为Unknown。目录存在不代表Q1/Q2/Q3通过。

| ID与入口 | 制作版本 | 范围 | 生命周期 / 可访问性 |
| --- | --- | --- | --- |
| <a id="as-g002-019"></a>AS-G002-019 · `expansion-a-v01/` | COMPONENT-EXPANSION-A-01 | PAWN-02、CHIP-01/02/03、CONTROL-01 | ReadyForScope（源件Q1/Q2及限定运行Q3） / PresentLocal |
| <a id="as-g002-020"></a>AS-G002-020 · `expansion-c-v01/` | COMPONENT-EXPANSION-C-01 | TABLE-01、MAT-01、SLOT-01、DRAWER-01，含独立runtime-fit桌/垫 | ReadyForScope（源件Q1/Q2及限定运行Q3） / PresentLocal |
| <a id="as-g002-021"></a>AS-G002-021 · `expansion-b-v01/` | COMPONENT-EXPANSION-B-01 | WAND-02 | ReadyForScope（源件Q1/Q2及限定运行Q3） / PresentLocal |
| <a id="as-g002-022"></a>AS-G002-022 · `expansion-d-v01/` | COMPONENT-EXPANSION-D-01 | DECOR-01/02/03 | ReadyForScope（源件Q1/Q2及限定运行Q3） / PresentLocal |
| <a id="as-g002-023"></a>AS-G002-023 · `expansion-e-v01/` | COMPONENT-EXPANSION-E-01 | TXT-02、TXT-03分层皮肤及布局说明 | ReadyForScope（源件Q1/Q2及限定运行Q3） / PresentLocal |

共同uses：DM-G002-014@YANZHOU-COMPONENT-DETAIL-V01、AS-G002-017@COMPONENT-ART-01；工具选择依据[固定调研结论](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/component-detail-higgsfield-assessment-2026-10-14.md)。实际采用本项目原创网格、程序表面及可编辑SVG；允许复用AS-G002-018@COMPONENT-SAMPLES-01的自制生成函数/表面，具体derived-from文件和指纹以各包最终manifest为准，不改冻结样件。未复制参考游戏原始网格或像素。

A/B/C/D按米制可编辑源、独立GLB/PBR、枢轴/轴向/尺寸及源重开/回导证据交接；E按分层RGBA/原生SVG、切片/内容区/锚点和18/24px实际字体审查图交接。进度登记在Mr. Mak Workspace对应组件页；完成后分别做独立质量复核和Godot限定运行检查。玻璃排序/成本、真实文本避让及用户最终美术接受不能由首批四件结论继承。内部制作复用已获本轮授权，公开分发条件Unknown；原件就地保存，Git仅登记来源与证据，不提交生产二进制。

2026-10-15固定补记：

- AS-G002-019：`expansion-a-v01/manifest.json` SHA `3144406c979f28266c39cb521ef26465b6a5228f3368a1149e6348268f474507`；124文件108911850字节全部复核，源SHA `596ef556a1f24a601c3a752a704d1650ac13135e97dc546bb1779f76d5654a24`。15GLB含三托盘与锁箍、七控制变体；[总控独立Q1/Q2](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/expansion-a-root-review-v02.md)实际15图及GLB结构检查通过，源重开与回导证据已固定。源自制表面/函数复用来自AS-G002-018，具体文件指纹见texture-provenance；运行标量粗糙度与动态节点边界已明记，最终Godot限定Q3见下方整合补记。
- AS-G002-020：`expansion-c-v01/manifest.json` SHA `3792ae0bf401b418723181917125c81d6df14f8bf0fb64f7a7fe2fe0d529f61a`；152文件245287889字节总控逐项核对。可编辑源SHA `9f4670d8fac82c489fb75873b0081ed634bf065d70ab3403e70566283194e163`，六GLB含桌/垫runtime-fit派生、独立PBR/掩罩、84渲染、实际源重开/四编辑探针与回导。GLB粗糙度导出丢失已修并保留失败记录；[D复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/expansion-c-review-v01.md)及[总控槽位补图复核](../../yanzhou/visual/component-production-2026-10-14/expansion-c-root-supplement-v02.md)收口，四件源Q1/Q2通过；Godot已接入，最终限定Q3见下方整合补记。
- AS-G002-021：`expansion-b-v01/manifest.json` SHA `319574140761207617a703e3967e1724471a8cf3a0f95d60cdc776dbd1804e3b`；71文件49745301字节，源SHA `f6ae050f4d9479779ae1bc2c4b1c7e6c9309cd318531131f1b4cf88bd0f98305`。[D独立复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/expansion-b-review-v01.md)核实际落桌姿态、晶体与镶爪接触、用途环间隙、源编辑与回导；Q1/Q2通过。Godot已接入，真实用途环、玻璃排序与接触的最终限定Q3见下方整合补记。
- AS-G002-022：`expansion-d-v01/manifest.json` SHA `881820f6f40a372f9607ea255cb9cb0eb456c81fc06f3ba28f45c4bb83249f3a`；109文件114299813字节，源SHA `42c50434bdc15ff1403b28d57232e0268a0ad5b46f8ac0a0f2d882a1512e3138`。[D独立复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/expansion-d-review-v01.md)核书分帖/书脊、1.8mm晶球壳、沙漏连续玻璃与三组互斥砂位、逐件编辑/回导；Q1/Q2通过。Godot接入采用记录过的透明外壳近似，不宣称原源材质光学传输已完整保留，最终运行限定Q3见下方整合补记。
- AS-G002-023：`expansion-e-v01/manifest.json` SHA `c1fe336bf9ca2e96d0eb35f148ac65fbb4d5f75c876dae648b55bf13b0f1242c`；607文件5876261字节总控逐项核对，145SVG/441PNG/6审查图。[D独立Q1/Q2](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/expansion-e-review-v01.md)通过，实际项目字体18/24px、28布局、102字形界及编辑重导已核；最终Godot限定Q3见下方整合补记。运行选28份准确逻辑尺寸的2倍合成无字皮肤及layouts，原分层源完整保留，禁止整体拉伸合成图。这里只覆盖二维文本载体，不宣称包含真实木条3D网格。

2026-10-15整合补记：AS-G002-018—023共同进入全19件预览。[D独立限定Q3](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/component-production-2026-10-14/q3-expansion-source-06-review.md)通过；[实际运行与包交付（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-15-component-expansion-integration.md")记录源码和Release两档各72/72、68PNG逐字节一致。运行v05选74项，SHA `a597788ee7e0366489400bec22ecfcf82ad02d375df117c76cee468d5cf209f1`；代码 `399d933ca191e5811232d3e8862749ba0e2c8c5e`；新包`E:/Project/yanzhou-godot/build/development-batch-10/components-01/windows/`，旧四样件包保留。原源件SHA不变。透明壳与压痕为运行近似，只有护盾新墨绘；1366少量标点/辅助页码换行保留。HTML浏览器、OS输入、正式性能及用户最终美术接受未验，不推为完整美术或玩法验收。


## DM-G002-015 真实UI文字／截图交互审阅首版

- 归属：game-002 / main；DM / UI审阅。主入口 `E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/index.html`；[逐组件审阅与范围](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/ui-review-2026-10-15/review-v01.md)。本机临时预览 `http://127.0.0.1:5191`，恢复说明在原代码目录README。
- 固定 UI-REVIEW-01；代码提交 `d8a94ed303923a067826450a024e7be6751cce86`；原目录manifest SHA-256 `89438025b4ab87720a7233c81fd10c1c6aaaae6d3bf52195c30fc7c15fa46742`，8个发布源文件另加manifest与技术检查报告。ReadyForScope / PresentLocal，2026-10-15浏览器实际操作及179项本机资源／HTTP完整性通过；不是完整战斗模拟、全状态验收或用户接受。
- 68真实截图状态、112去重捕获文案、11条入口；候选文字／字体／偏移和审阅草稿可操作。开始／设置全页及未捕获历史未实现，待受理和后续页为源码派生HTML。Godot替换、截图局部美术图与像素差分尚未执行。全部组件待审，设计资格与采纳不变。
- uses: AS-G002-011@FONT-ASSETS-01（现行字体）、AS-G002-018@COMPONENT-SAMPLES-01（TXT01原载体切片）、AS-G002-023@expansion-e-v01（原生纸页／签）、AS-G002-024@FONT-CANDIDATES-01；截图复用DM-G002-011的package-components-01固定证据。derived-from: None（新审阅工具；旧109状态HTML仅作历史参考）。原图片、字体及许可就地保管，未复制原始二进制入本仓库。

## AS-G002-024 中文字体候选比较包

- 归属：game-002 / main；字体比较；维护[字体调查](../../yanzhou/visual/ui-review-2026-10-15/fonts-v01.md)，供DM-G002-015内部审阅使用。FONT-CANDIDATES-01，原件 `E:/Project/yanzhou-godot/evidence/development-batch-11/ui-review-v01/fonts/`；固定文件清单、下载URL、大小／SHA及许可SHA见DM015代码提交中的data.json。ReadyForScope / PresentLocal，仅本轮503字技术覆盖及浏览器同尺寸对照。
- Noto Serif CJK SC Regular 2.003，官方源提交 `9b0f1436e455d902de067a2501422e5dc71ad16b`，文件SHA `2a2eae2628df83556c54018c41e20fa532c1b862c5256ae8b3f23feb918d12ca`；LXGW WenKai Regular 1.522，官方发布tag v1.522，文件SHA `39ad71264b588165b469e35e6afb162a378dacd1f95348160240ba9038ac3009`。均原始未修改文件、原OFL1.1逐份保留；软件嵌入／捆绑按原文保留版权许可、不得单售字体、修改版本遵守保留名称条件。未安装字体、未付费授权或公开发布。
- 每个主字体503测试字，本体缺✱，配AS-G002-011的Symbols2后无缺字；其他字重与罕见字、Godot基线／fallback和成本未验。不由此认定全中文字库或全游戏选型。来源官方URL和权利原文见维护页；字体最终选择待用户逐组件审阅。

## AS-G002-025 恶魔牌原资源本机适配包

- 归属：game-002 / main；原桌、桌布、卡牌网格与纹理。源文件沿AS-SH-002本机固定pak；[接入清单（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/coordination/2026-10-15-demoncards-asset-integration.md")与[原资源固定清单](E:/Project/yanzhou-godot/docs/coordination/demoncards-original-assets-v01.json)。
- 版本 DEMONCARDS-ORIGINAL-01；具体源/导出SHA、顶点/UV/纹理尺寸、轴向与运行缩放见清单。原件在E:/Game/Demoncards，派生在唯一代码仓库ignored的godot/assets/demoncards-original-v01，原第三方二进制不提交。
- ReadyForScope / PresentLocal（本机接入限定范围）。原3模型+5纹理已导出，实际运行为3模型+3纹理，另两图保留来源；源码修正轮两档各72项通过，独立包/设计复核见[本轮记录](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-assets-2026-10-15.md)。uses: AS-SH-002、DM-G002-013及当前组件合同；derived-from: AS-SH-002@DEMONCARDS-REFERENCE-2026-10-14-v01。使用者DM-G002-011第十二批；原游戏资源再分发条件Unknown，本次没有公开上传。

## AS-G002-026 恶魔牌字体对应作者原版包

- 归属：game-002 / main；全濑体1.11和狮尾B2宋朝简中Regular/Bold，直接从原作者渠道取得；[固定下载与字形清单](E:/Project/yanzhou-godot/docs/coordination/demoncards-fonts-v01.json)、[字体接入报告（Git原文）](E:/Project/yanzhou-godot/docs/development-handoff.md#追溯与日常记录 "git show cc8c229fe89d85a51e739efc0111a54d139fff1a:docs/reviews/2026-10-15-demoncards-fonts-a.md")。
- 版本 demoncards-fonts-v01；作者下载URL、Swei固定commit、原文件/原OFL SHA与实际字形覆盖在清单。三份TTF放代码仓库ignored字体目录，原许可证跟随代码和本机包；没有全局安装字体。游戏清单只证明家族/字重存在，不证明每个页面原字重或作者文件与游戏内文件字节一致。
- ReadyForScope / PresentLocal（本机接入限定范围）。2026-10-15原件指纹及348字符合并覆盖通过；全濑体短标题、Swei Regular正文、真实Bold常驻精确值，修正轮两档各72项通过。字体字节和两份原OFL随包核对；完整检查见[本轮记录](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-assets-2026-10-15.md)。uses: AS-G002-011符号/中文覆盖回退；derived-from: None（作者原版未修改）；使用者DM-G002-011第十二批。沿两份原OFL保留版权/许可证，具体条款按原文，不由参考游戏的资源许可代替字体授权。

DM-G002-011第十二批使用补记：GODOT-DEMONCARDS-ASSETS-B12-01，本机独立预览；固定代码 `8d22262dfa4a3cf9cdc96cae5f9994f27608cafe`，使用AS-G002-025/026，保留AS-G002-018—023其他组件及既有动作。原桌/布/牌只替换对应外观，旧源件和包不覆盖。[范围与证据入口](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-assets-2026-10-15.md)记录实际源码、包、D限定复核；OS、性能、用户最终美术接受不由此升级。

## AS-G002-027 恶魔牌追加视觉与曲线适配包

- 归属：game-002 / main；模型、纹理、表面／局部特效、曲线。维护[本批开发记录](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-candidates-2026-10-15.md)；派生原件保存在代码仓库ignored的 `E:/Project/yanzhou-godot/godot/assets/demoncards-candidates-v01/` 与 `demoncards-motion-v01/`，原pak沿AS-SH-002就地保管。
- 固定版本 DEMONCARDS-CANDIDATES-01：[51文件清单](E:/Project/yanzhou-godot/docs/coordination/demoncards-candidates-v01.json)，SHA `12e731f41ed0fa10593f940bef750dbe6226e0c9ec4e06e74b4b27dbf4bc270b`；13GLB＋17指定PNG＋21材质依赖PNG，源包、规格、轴向／单位／UV、材质绑定及导出哈希逐件记录。DEMONCARDS-MOTION-01：[曲线清单](E:/Project/yanzhou-godot/docs/coordination/demoncards-motion-v01.json)，SHA `6b84f7a923338eac4b9e3ebd5235f30d4121b57bd2272c14d5a52460a7f3313c`；19曲线＋13时间轴保存在一份固定JSON，并非32段独立动作。
- ReadyForScope / PresentLocal（2026-10-15本机有限适配）。全部模型／纹理可检视，6模型用于主桌；17纹理中书页随主桌使用，其他用于检视与载体／局部效果样例。书表面、烛组合、NS样例为Godot重建，原材质图／Blueprint／Niagara未完整执行；5处默认WorldGrid槽明确使用项目补材质，源无效次UV只在派生中省略，原件保留。源／包两档检视87/87，逐项结果见[接入记录](E:/Project/yanzhou-godot/docs/coordination/demoncards-candidates-integration-v01.json)，D复核限指定16张静态图，最终美术接受NotRun。
- uses: AS-SH-002、DM-G002-013及现十九组件宿主；derived-from: AS-SH-002@DEMONCARDS-REFERENCE-2026-10-14-v01，原pak SHA `c61d079f5a853f51b52b81d1799f8c3595b8a2d079a1d449329af4597075ebd4`；使用者DM-G002-011@B13。第三方原作者／公开再分发条件沿源记录，Unknown不改为开放许可；仅用户授权本机预览，无原始二进制入Git或公开上传。

## AS-G002-028 恶魔牌十二音效适配包

- 归属：game-002 / main；短音效。维护[本批开发记录](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-candidates-2026-10-15.md)，派生原件在ignored的 `E:/Project/yanzhou-godot/godot/assets/demoncards-audio-v01/`；原包沿AS-SH-002。
- 固定版本 demoncards-audio-v01：[25文件清单](E:/Project/yanzhou-godot/docs/coordination/demoncards-audio-v01.json)，SHA `ed2ee4d53969d099bc05ff2d77a573ffee70769de625b64c914d0ef548a94be0`。12完整48kHz双声道PCM16 WAV＋12逐字节相同PCM sidecar＋1catalog；单个0.042—1.106秒、非循环，具体采样数／增益／源与派生哈希见清单。CloseHandbook防饱和整体衰减约0.404dB，其余不裁剪、不归一化。
- ReadyForScope / PresentLocal（2026-10-15本机技术范围）。12音效可试听，9个用于主桌既有事件／UI，3个瓶／饮用音仅试听。源／独立包两档均完成12份真实混音、静音、切换停止及完整PCM匹配；[实际交付证据](E:/Project/yanzhou-godot/docs/coordination/development-batch-13-evidence.json)记录后续总控验证，清单中A交回时的NotRun保持原快照。主观音色／平衡NotRun。
- uses: AS-SH-002；derived-from: AS-SH-002@DEMONCARDS-REFERENCE-2026-10-14-v01；使用者DM-G002-011@B13。原游戏音效的作者／再分发条件Unknown；本次仅用户授权本机适配。既有AS-G002-012程序声作为回退保留；不提交原第三方声音或构建二进制，不公开上传。

DM-G002-011第十三批使用补记：GODOT-DEMONCARDS-CANDIDATES-B13-01，固定运行代码 `e975de8bdbbe70591d4099c34b799e76c4bff1d7`；uses AS-G002-027/028及既有AS-G002-025/026、十九组件的固定版本。45候选均有检视适配，6模型／9音效用于主桌，有限UE对象重建不声称原脚本移植完成。[本机Windows包](E:/Project/yanzhou-godot/build/development-batch-13/candidates-01/windows/Yanzhou.exe)、[使用／验证与限制](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/development/reports/demoncards-candidates-2026-10-15.md)、[D限定复核](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/demoncards-candidates-2026-10-15/design-review-v02.md)各自定位。源码及复制包两档主桌80/80、检视87/87，202包文件指纹一致；ReadyForScope / PresentLocal。源件、B12和阶段失败全部保留；非OS输入、性能、主观听感、用户接受或玩法成立证明。

## DM-G002-015 第十三批资产同步审阅稿（v02）

- 同一Demo续版 UI-REVIEW-02；维护入口[逐组件审阅v02](https://github.com/dsaj4/game_design/blob/f21058a54b096e0d6ad2b3b559e352b67596c239/yanzhou/visual/ui-review-2026-10-15/review-v02.md)，本机仍为 `http://127.0.0.1:5191`。外部代码 `E:/Project/yanzhou-godot/tools/ui-review-2026-10-15/`，固定提交 `f5c702907cfa157565764435e759611dd471d0cf`；9份发布源文件，manifest SHA `1e8a394be46c874c7ed72b3cfcfaee2e37751feb73f2df36efdbff0e466cf2a8`。
- ReadyForScope / PresentLocal（2026-10-15本机审阅工具）。70主桌截图、136条去重取证文字、118资源检视图和12种声音的两档引擎混音；新字体分工、逐组件意见、视口隔离草稿与JSON导出已接入。335项资源／HTTP检查及两档70状态浏览器入口检查通过；用户接受、引擎像素对照、动态资源检视未由网页检查推定。
- uses: DM-G002-011@GODOT-DEMONCARDS-CANDIDATES-B13-01固定包证据，AS-G002-025/026/027/028；继续复用AS-G002-011/018/023/024。原第三方资源和混音证据仍在本机ignored路径，只通过localhost白名单读取；许可／再分发条件沿原条目，未公开上传。首版UI-REVIEW-01及其固定输入保留Git取证，当前预览由v02承接。

## <a id="dm-g002-016"></a>DM-G002-016 主桌少文字交互示意

- 归属：game-002 / main；[候选与完整登记](../../yanzhou/sources/inbox/2026-10-17-minimal-battle-ui.md#dm-g002-016-主桌少文字交互示意)。用于讲解空间时间刻度、分段加工环、容量四态及当前／未来用途，设计保持Raw Idea / Unqualified。
- MINIMAL-BATTLE-UI-01；[本机会话源片段](C:/Users/Administrator/.codex/visualizations/2026/10/15/01a141f1-a6fd-7cc1-ad44-eab0824be2ca/minimal-battle-ui.html)，单文件SHA-256 `6253e6b9fdb5c211d857da18c0afd857b8013911c12bafd14e1e6453ee03a249`。源文件就地保管，依赖Codex可视化宿主；两组固定快照、对象说明及响应布局，无战斗推进。
- ReadyForScope / PresentLocal（2026-10-17，仅方案讲解）。实际检查736／320px预览、情境切换、法器／容量说明及Enter入口；浏览器无报错，窄屏相关容器无横向溢出。完整图形近观、动效、引擎对照、完整键盘验收及玩家理解未验证。
- 原创示意，本项目内部讨论可复用；图标依宿主Lucide支持，许可沿宿主依赖。uses: None；derived-from: None；B13只作既有视觉参照。登记不改变现行规则或授权引擎开发，暂无登记使用者。

## <a id="as-g002-029"></a>AS-G002-029 主桌少文字截图效果图

- 归属：game-002 / main；[制作记录与完整提示词](../../yanzhou/visual/minimal-battle-ui-2026-10-17/art-v01.md)，设计来源为[少文字候选](../../yanzhou/sources/inbox/2026-10-17-minimal-battle-ui.md)，状态Raw Idea / Unqualified。用途为当前真实主桌基础上的视觉审阅，非运行截图或新资产实装。
- MINIMAL-BATTLE-UI-ART-01；本机原件／交付图 `E:/Project/yanzhou-godot/evidence/ui-concepts/2026-10-17-minimal/minimal-battle-ui-art-v01.png`，1672×941 PNG；SHA-256 `d478521339be289d3a5f404a171cfd0ebc95993e1a9de4bc1ad5f660bbab54d5`。模型生成原件、首版及修订提示词沿制作记录定位。图像保持本机，不随本次文档提交上传。
- ReadyForScope / PresentLocal（2026-10-17，仅本机效果稿审阅）。设计agent使用内置image_gen编辑，协调者独立目视二版：卡片刻位3／6、暗牌揭示刻位4、容量1实牌＋1预留＋3空位、三格加工环2/3、原生命与标记数值及窗外类别可辨。存在生图细部重绘与尺寸变化，未做引擎像素对照或用户美术接受，不作为动态进度或玩法验证。
- 底图为DM-G002-011@GODOT-DEMONCARDS-CANDIDATES-B13-01的 `package-main-01/1920x1080/09-completion-paused.png`，SHA `d974b54753390760fc862ebdcce50d2d5ae0291939a854e60d104f098b444a2b`。derived-from: 该固定取证截图；uses: 本轮少文字候选。底图所含Demoncards资源沿AS-G002-025/027原本机制作与审阅边界，公开再分发条件Unknown；本条不新增图像公开分发授权。
