# game-002 代码开发进度

## 2026-09-13 最新设计变更尚未实现

[G002-CORE-018 / ST01–04](../game-design-workflow/idea-materials/M-2026-09-13-end-tick-status-rulings.md)已采纳每刻末状态、固定排序、自然衰减累计小数和允许空心＋自噬储层。现有TH-003／CAL引擎与候选仍对应旧周期／取整输入；本轮只改设计文档，没有修改代码或demo，新规则实现与测试NotRun。下一步按[交接](test-handoff.md)冻结新输入后再登记实现版本。

日期：2026-09-13。设计依据：[Core Concept v0.6](../game-design-workflow/core-concept.md)。

| 里程碑 | 设计来源 | 状态与证据 | 阻塞与下一步 |
| --- | --- | --- | --- |
| 战前配置与完整自动战斗 | 当前核心及[正式素材](../game-design-workflow/idea-materials/README.md) | Planned；尚无符合当前全流程的实现验收证据 | [接口范围](design-decisions-needed.md)已确认；先建立当前规则所需参数，再登记实现与验证 |
| 时间、覆盖、打断与终止验证 | 当前核心及[攻防候选v0.1](../game-design-workflow/idea-materials/M-2026-09-11-simple-spell-parameter-candidates.md) | Limited Verified：TH-2026-09-11-001/r2的726组逐事件差分与10项规则边界通过；[报告](test-reports/TH-2026-09-11-001-r2-run-01.md) | 仅两句攻防、固定单敌；其他词义和完整流程未验收 |
| 超时疲劳 | [G002-CORE-014与FAT-C候选](../game-design-workflow/idea-materials/M-2026-09-11-overtime-fatigue.md) | Limited Experimental Evidence：TH-003/r1独立模型验证无恢复条件的有限终局与归因；[报告](test-reports/TH-2026-09-13-003-r1-run-01.md) | demo尚未接入；加入治疗、复活或生命上限变化须重新检查，不外推完整玩法 |
| 词义、数值与路线验证 | 当前合格素材及[数值重设计任务](numerical-redesign.md) | Planned；候选参数不等于已平衡 | 重新建立输入并完成资格确认，再验证完整规则关系 |

可用实现资源目录为 E:/Project/game-002-glyph-timeline；本次未检查或修改该目录，不能据目录存在推定当前设计已实现。[实现记录快照](../../../archive/2026-09-10-game-002-design-originals/workspaces/game-002/docs/code-development-index.md)保留已登记的提交、测试范围及原始证据。

## 关联demo数值测试注册

按用户2026-09-11指定的「时序施法原型」任务，另登记`E:/Project/yanzhou-pixel-lab`为本轮可玩数值测试实现；不替换上述资源身份，不视为完整v0.6实现。

| 项目 | 当前记录 |
| --- | --- |
| 设计与参数 | 固定提交1d4bb7faff715f787cba31794829fc8c6527a1c1；Candidate v0.1，未Accepted |
| 实现提交 | 8347088f5e56d46bdc39793cfeb2b59ef01dba33；分支codex/test-agent-candidate-v01，本地已提交，无远端 |
| 测试协作 | [固定交接](test-handoff.md)，TH-2026-09-11-001 / r2，Codex测试agent任务01a08e19-0acb-7cb2-a022-1f54ec6c308d |
| 可玩入口 | [本地demo](http://127.0.0.1:5199/)；根目录已有启动言咒.cmd |
| 已覆盖 | 四种攻防配置、8/10/12刻敌人节奏、六张实体卡、两根法杖、单敌、时间编排、自动战斗、记录导出入口；页面共用引擎726组与独立模型一致，构建与包装检查通过 |
| 实现边界 | 原v0.5视觉资产复用，旧火焰/雷电/回响与金币参数不参与本包；每次重试还原输入生命。范围恒定许可、无跨战成长；浏览器交互和玩家体验未验收 |
| 技术细节与证据 | [代码仓库测试维护说明](E:/Project/yanzhou-pixel-lab/docs/numerical-testing.md)、[实现哈希与事件清单](E:/Project/yanzhou-pixel-lab/docs/test-evidence/TH-2026-09-11-001-r2-run-01/verification.json) |
| 下一步 | 当前先审查数值框架与疲劳候选；后续实现疲劳须登记新设计／实现版本并独立验证。T01/T02玩家可读性测试仍未执行 |

技术细节与测试结果写在对应代码仓库；本索引只记录里程碑、证据、阻塞和下一步。代码完成度不能提升核心或素材的证据状态。

## 2026-09-13 两流派独立数值实验

用户要求自行设初值，明确允许补临时实验规则，并要求本轮无需注册demo。已完成[TH-2026-09-13-003/r1/run-01](test-reports/TH-2026-09-13-003-r1-run-01.md)，状态为Completed / Limited Experimental Evidence；正式规则、S2素材资格与旧demo配置保持原状态。

| 项目 | 当前记录 |
| --- | --- |
| 设计输入 | 16231ee77e389864b10dd4de15d328cccf071d0a；简易方向、EL01–07及选定E3子集；S2新卡仅Raw实验 |
| 实现位置 | [独立实验仓库](E:/Project/game-002-numerical-lab/README.md)，非可玩实现，无demo依赖 |
| 实现与结果 | codex/archetype-tests-2026-09-13；2d783252999f7de703a9e6938d9840c4b408b847，本地已提交、无远端；输入冻结83b3f3c |
| 完成证据 | 17424场主矩阵、6534场数值敏感性、484场临时规则对照、4962场连续生命账本，共29404场；14项规则检查及数据完整性检查通过 |
| 覆盖界限 | 16构筑、9场景、两杖起点0–10；固定单敌与单目标邻近关系，尚非完整2×5环境／全卡池／真实经济／玩家试玩 |
| 主要发现 | 简易复诵较快；元素普通场景可持续，但快攻弱、冰冻结算分支敏感；空心＋自噬与衰减取整需设计裁决 |
| 下一步 | 先决定冰冻增甲及小数衰减接口，再复核脉冲3层候选的压力场景；扩展未测E3组合与空间过滤 |

完整技术输入、实现、复现步骤与逐场证据保留在独立代码仓库。此批不证明当前两流派已能在demo游玩。

## 2026-09-13 自动平衡校准

用户要求先定标准／硬规则、再定任务／临时规则，最后模拟与自动调整。已实现[自动校准流程](automatic-balance-calibration.md)，[CAL-2026-09-13-001/r3报告](test-reports/CAL-2026-09-13-001-r3-run-01.md)为限定任务达标证据，未接入demo。

| 项目 | 当前记录 |
| --- | --- |
| 实现 | [独立数值校准器](E:/Project/game-002-numerical-lab/CALIBRATION.md)；codex/archetype-tests-2026-09-13，9657353e09ed168f9d576617ce8b81ccdaf7d847；本地已提交，无远端 |
| 输入与范围 | 保留TH-003引擎；H01–H08、四代表、四训练场景、允许数值域与临时结算先冻结；机制与标准不进入搜索 |
| 执行 | r1共720点无解，r2共192点无解，r3共60点中18点训练可行；三轮合计975659场，选定候选后一次留出验证 |
| 验证 | r3新敌人1452场、全16配置×9场景×121起点回归17424场、三连战实际5260场；24项检查及三轮版本／选优／统计审计通过 |
| 交付 | [独立候选参数包](E:/Project/game-002-numerical-lab/calibrated-candidate-r3.json)，状态CalibratedCandidate；原TH-003参数和所有失败记录保留 |
| 限制与下一步 | 普通防御损耗中位为0，须为战斗压力和防御机会成本另立任务；全卡池、真实经济、战场与体验未验收 |

修订内自动调参已运行；外层参数域扩大由agent明确制定后重新冻结。当前没有自动改机制、改验收标准或发布参数的权限流程。数值满足本任务不能升级为核心玩法Accepted。

## 2026-09-13 外部技术选型调研

用户要求调研Astra游戏开发案例，并明确目标为持续开发可发布的独立游戏。[案例与选型研究](../research/03-product-case-studies/2026-09-13-astra-game-development-stack.md)推荐Godot、带类型标注的GDScript与Blender，状态为Research / Recommendation / Proposed。尚未确定为本项目技术栈，未审查或迁移既有代码，未运行游戏测试；现有实现里程碑保持原状态。下一步在启动实现时结合首发平台、目标设备与既有代码审查决定是否采用。

同日补充[生成工作流与Blender MCP比较](../research/03-product-case-studies/2026-09-13-godot-blender-workflow-comparison.md)：推荐原生Godot主项目、Blender脚本生产与单一Blender MCP交互桥接；Godogen／GodotMaker用于独立实验或方法参考。状态仍为Research / Recommendation，未安装、运行或采纳工具链。

## 2026-09-13 Godogen 独立 3D demo 环境

用户后续明确选择“从零试验3D：Godogen + 原生 Blender + Python”，并要求先完成新工作区与环境准备。上述调研保留为当时建议；本次选择仅对独立实验生效，不自动迁移正式游戏或已有 demo。

| 项目 | 当前记录 |
| --- | --- |
| 工作区 | [game-002-godogen-lab](E:/Project/game-002-godogen-lab/README.md)，独立本地 Git 仓库 |
| 实现记录 | codex/setup-godogen-demo；0a67711；已本地提交，尚无远端 |
| 来源 | 启动时设计提交305044d6d25783e914ff6d7265ed9d724684a989，12份选定文档快照及哈希；保留Accepted／Qualified／Candidate／Raw状态 |
| 里程碑 | EnvironmentReady；空项目可启动，未制作法杖装配／地图UI或美术样件 |
| 环境证据 | [环境报告](E:/Project/game-002-godogen-lab/docs/environment-report.md)：C#编译、场景生成、Blender保存／GLB导出与Godot读取通过；Vulkan及PNG输出通过 |
| 实验方向 | Godogen本地适配、原生Blender/Python，未启用Blender MCP或上游云端资产技能 |
| 后续任务 | [原始视觉想法](../game-design-workflow/idea-inbox/2026-09-13-flask-style-wand-map-ui.md)，Raw Idea / Unqualified；[详细待办](E:/Project/game-002-godogen-lab/docs/deferred-ui-experiment.md)为Deferred / NotStarted |
| 下一步 | 等用户启动后再补看视频片段、明确最小玩家动作和视觉验收，再制作小样；当前无后台自动开发任务 |

所有代码、工具版本、安装／启动方式、日志与后续技术实验留在独立仓库。环境验收不构成视觉可行性、玩法或发布质量结论。

### 同日后续：视觉方向01与实验计划

用户授权先读截图／视频／设计，再给效果图与实验计划。已交付[两屏概念效果图和来源观察](E:/Project/game-002-godogen-lab/docs/visual-direction-v01.md)、[E0–E4实验计划](E:/Project/game-002-godogen-lab/docs/experiment-plan-v01.md)。E0的参考抽看和概念图完成，状态VisualDesignDraft / AgentCandidate；E1风格小样、E2装配、E3地图、E4合屏维护均NotRun，实机制作仍Deferred。图为imagegen概念输出，不新增引擎验证证据；视频抽看片段和图内未精确呈现的拓扑限制已记录。

独立工作区提交：codex/setup-godogen-demo / 3f76545，本地已提交、无远端；本轮只更新文档、来源状态与概念图，game/运行实现保持环境准备状态。

### 同日后续：E1 首轮实机风格小样

用户明确要求“开始启动E1”。已在独立工作区完成木框、单法杖及固定镶嵌、两纸签、地图纸与单遭遇摆件的原生小样。[E1 实机报告](E:/Project/game-002-godogen-lab/docs/e1-report.md)状态为 Executed / NeedsRevision：资产管线与本样本中文检查通过，风格仍需修订；E2–E4 保持 NotRun。

| 项目 | 当前记录 |
| --- | --- |
| 实现归档 | codex/setup-godogen-demo / d2fa3f0，本地已提交、无远端 |
| 完成证据 | 可编辑 Blender 源、原生生成脚本、基础/墨线同构图资产、Godot 实机 1080p/720p 各两张；[机器检查](E:/Project/game-002-godogen-lab/docs/evidence/E1/verification.json) |
| 结果 | 场景保存完整，实际 GPU 截图尺寸与中文边界通过；墨线版已有纸边和木纹，但木框重复、法杖轮廓简单、塔楼俯视辨识偏弱 |
| 限制 | 未验证装配、选路、战斗、整屏合并、长词条、持续帧率或发行；技术通过不代表达到参考美术完成度 |
| 下一步 | 评议同一 E1 小样，先修轮廓、排线和光照；不据此扩展 E2 或采纳正式美术方向 |

原始视觉想法仍为 Raw Idea / Unqualified；当前实现只提供独立技术实验与美术观察，不改变核心构思或 GDD。

### 同日后续：E1 R2 同页材质与原生模型修订

用户要求继续当前页面，使用图像模型增加参考，并通过电脑插件控制 Blender 细化建模。已完成 [R2 实机修订报告](E:/Project/game-002-godogen-lab/docs/e1-r2-report.md)，状态 Executed / NeedsRevision / user review pending；技术检查通过，E2–E4 仍 NotRun。

| 项目 | 当前记录 |
| --- | --- |
| 实现归档 | codex/setup-godogen-demo / 7b36a90；独立本地仓库已提交，无远端 |
| 图像资产 | 新增法杖／石塔建模参考板、墨线木纹、边缘群山地图纸；原图和提示词留档。木纹／纸图用作模型材质，造型板仅参考 |
| Blender 操作 | 电脑插件实际编辑塔顶轮廓并另存 UI 源；原生 Python 补充瓦片、石砌、法杖木节／根须／铜箍、绳环与内衬；审计确认 UI 修改保留到导出 |
| 完成证据 | [R2 验证记录](E:/Project/game-002-godogen-lab/docs/evidence/E1-r2/verification.json)：基础／墨线同几何与相机、场景保存、GPU 1080p／720p 四图、字形／边界及来源哈希检查通过 |
| 美术观察 | 木纹、地图纸与法杖轮廓较首轮改善；塔楼正面可见。形体与材质层次仍简化，地图下缘说明略受纹理干扰，未认定达到 FLASK 参考完成度 |
| 下一步 | 继续评议和细化当前页面；不扩展装配、选路或战斗，也不改变正式美术／玩法采纳状态 |

### 同日后续：先完善右侧地图整体概念

用户将下一步限定为左右分开、先做右侧地图桌面的整体效果图与设计稿，整体确认后再逐件生成组件图。已交付 [地图桌面视觉设计02](E:/Project/game-002-godogen-lab/docs/map-desk-visual-design-v02.md)和[整体概念图](E:/Project/game-002-godogen-lab/concepts/map-desk-overall-v02.png)，状态 VisualDesignDraft / 整体待确认。四类地图棋子、环境地图与红线、猫／金币宝箱／书已按清单呈现；额外杂物按用户“杂物不用清除”保留。

独立仓库 codex/setup-godogen-demo / 38d0df6，本地已提交、无远端。此次只有概念图片、提示词、来源及设计文稿，运行实现保持 E1 R2 / 7b36a90；没有新 Blender、Godot 或交互验收。下一步由用户确认整体后再启动组件单图，不能把保留杂物视为整体已采纳。

### 同日后续：整体确认与十张 Blender 组件设计稿

用户明确“确认，开始生成，每张图做成blender设计稿”。整体美术方向据此进入 OverallDirectionConfirmed，已交付[十张组件图册](E:/Project/game-002-godogen-lab/concepts/blender-sheets-v01/index.md)与[中文建模说明](E:/Project/game-002-godogen-lab/docs/blender-component-design-v01.md)，组件状态 ComponentDesignDraft。内容涵盖桌面及保留杂物、环境地图、红线、法师木雕、篝火、水晶球、地点建筑、金币宝箱、猫和旧书。

独立仓库 codex/setup-godogen-demo / 78b77d1（内容提交4b98aca，本地已提交、无远端）。10张选用图均1536×1024，地图和红线各修订一次；共12张原图与12份提示词、来源SHA留档。已检查原图复制哈希和66处文稿链接；生成视图的局部透视／方位偏差及尺寸建议记入建模说明。

本轮完成的是建模参考图，不是新.blend模型或运行贴图；实际实现继续为E1 R2 / 7b36a90，无新增引擎、交互或玩法验收。后续制作建议先搭桌面／纸面／红线与相机，再以法师木雕校准风格；本次美术确认不替代原始玩法想法的资格确认。

### 同日后续：九类原生 Blender 资产，猫暂缓

用户明确“开始生成blender资产，猫先不用生成”。已完成[九类资产图册](E:/Project/game-002-godogen-lab/art/map-desk-v01/README.md)、[组合工程](E:/Project/game-002-godogen-lab/art/map-desk-v01/map-desk-master.blend)及[制作／使用说明](E:/Project/game-002-godogen-lab/docs/map-desk-assets-v01.md)，状态 NativeAssetsCreated / NeedsArtReview。MD-01–08与MD-10各有可编辑.blend、GLB和实际渲染：桌面及杂物、环境地图纸面、独立红线、法师木雕、篝火、水晶球、地点建筑、金币宝箱、旧书；MD-09猫按本轮要求未制作。

独立仓库 codex/setup-godogen-demo / 568653496dd70ebbbb8a2f161147d20fe1bda774，本地已提交、无远端。地图贴图另行生成并保存原图／提示词／来源哈希，木纹复用已归档生成素材。电脑插件在原生Blender中实际修改宝箱后铰链开角，后续加工保留；组合与分件均保留可编辑结构和打包图片。

[最终验证](E:/Project/game-002-godogen-lab/art/map-desk-v01/verification.json)通过：组合与九个源文件重新打开，GLB逐件实际回导，三角面数量一致、尺寸误差小于0.002米、无展示地面混入且无猫；组合渲染1536×1280、分件图1100×1100，另检查69处本地文稿链接。当前证据覆盖资产文件和实际Blender渲染，精细雕刻、墨线与透明／火焰效果仍待美术评议。Godot运行实现继续为E1 R2 / 7b36a90，未新增引擎场景、性能、交互或玩法验收；下一步先评议当前分件与组合风格，再决定精修对象。

### 同日后续：法杖袋整体修订，等待确认

用户新增右后侧整皮卷成的破旧法杖袋，露出一至两支杖头，指定后续作为法杖管理入口，并明确先整体、确认后组件图、再Blender资产。已交付[整体效果图03](E:/Project/game-002-godogen-lab/concepts/map-desk-overall-v03.png)与[设计说明](E:/Project/game-002-godogen-lab/docs/map-desk-visual-design-v03.md)，状态OverallRevisionAwaitingConfirmation；独立仓库codex/setup-godogen-demo / 59db26136b46a6ef3185203e57aa3d01fb5a0f17，本地已提交、无远端。

本轮以已确认手绘整体02为底图，用内置imagegen编辑；1254×1254原图、完整提示词与来源SHA已归档，原图复制一致并检查5处设计文稿链接。红线和四类节点可见，保留杂物与原概念中的猫；猫模型仍暂缓。预留MD-11但未生成组件稿、模型或管理交互，原生资产实现仍为5686534、Godot仍为E1 R2 / 7b36a90。下一步等待用户确认新版整体，再按指定顺序制作；本图不是Blender或Godot实机证据。

### 同日后续：删猫、横置与桌宽长法杖

用户认可皮革袋形象，先要求删猫并将加长袋体横向放在后沿原猫位置，随后明确“长法杖可以和桌子差不多长甚至更长”。已完成[整体修订04／05与说明](E:/Project/game-002-godogen-lab/docs/map-desk-visual-design-v05.md)，当前以05为准，状态BagAppearanceConfirmed / OverallRevisionAwaitingConfirmation。独立仓库codex/setup-godogen-demo，04为6b8e229、05为0db4df4588465ca79cb01c1453407ed973e52ad5，本地已提交、无远端。

两张1254×1254图片均由内置imagegen编辑前版，原图、完整提示词及SHA归档；05向左延长袋体，长袋和露头接近后沿可见宽度，猫移除、路线与节点及杂物保留。图像未做透视尺寸标定，提示词比例不作已测量几何。未新增MD-11组件稿、Blender模型或Godot实现；整体确认后再依次做组件图和原生资产。已有九类模型及E1 R2证据保持原范围。

### 同日后续：整体05确认与MD-11设计稿

用户确认“可以开始生产袋子设计图，可替代猫的位置”。已完成[两张MD-11设计板](E:/Project/game-002-godogen-lab/concepts/blender-sheets-v02/index.md)和[中文建模说明](E:/Project/game-002-godogen-lab/docs/blender-wand-roll-design-v01.md)，OverallDirectionConfirmed / ComponentDesignDraft。独立仓库codex/setup-godogen-demo / 0c76b8820c4868c817c938c76950c8e68acdf46e，本地已提交、无远端。

外观稿提供长袋主效果／方向参考／端部与材质细节，拆件稿提供单张皮革包卷、同皮折底、绑带和两支长杖。两张选用图均1448×1086；剖面修订为两个实心木杆，修订前图与全部三份提示词保留，原图复制哈希及17处链接已检查。尺寸、面板缩放与视图方位限制写入建模说明，未把生成图认定为几何验收。MD-09退出当前构图但保留历史设计稿；MD-11模型尚未新建，已有九类资产与Godot E1 R2不变。整体已确认，下一制作阶段为按稿新建长法杖袋原生资产。
