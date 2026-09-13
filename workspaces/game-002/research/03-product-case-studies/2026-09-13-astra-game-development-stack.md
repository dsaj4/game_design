# Astra 游戏开发案例与技术栈调研

日期：2026-09-13。状态：Research / Technology Recommendation；未采纳为项目技术决策。

后续补充：[Godogen、GodotMaker与Blender MCP比较及推荐组合](2026-09-13-godot-blender-workflow-comparison.md)。

用户原始请求：“调研一下网络上使用astra开发游戏的实例，推荐一个最好的技术栈”。随后明确目标：“持续开发可发布的独立游戏”。本文中的 Astra 指 GPT-6 Astra。

按默认工作区 game-002 保存研究。本文只形成外部案例比较与选型建议，不改变核心构思、素材资格、发行平台或既有实现状态。公开页面与作者报告已查阅；本轮没有下载、运行或独立复现案例。案例不能作为 Astra 与其他模型、或不同引擎之间的受控性能排名。

## 可追溯案例

| 案例 | 实际技术与成果 | 证据与边界 | 借鉴价值 |
| --- | --- | --- | --- |
| [Void Explorer](https://developers.openai.com/blog/how-to-build-games-with-astra) | 作者 Thomas Ricouard 使用 Astra/Codex；TypeScript、Vite、Three.js，渲染从 WebGL2 转向 WebGPU；程序化太空探索 | 2026-09-04官方开发文章，含测试方法和试玩入口；不是商业发行证明 | 将模拟与渲染分开，提供固定复现场景、状态与性能指标；Vitest和Playwright支持反复检查 |
| [Pulsebreak](https://github.com/xindomusic/pulsebreak) | Godot 4.7.2、GDScript、程序化美术与合成音频；Mac上的3D竞技场肉鸽 | 作者公开源码、导出说明和测试记录；报告131项检查，但人类手感与其他构筑平衡仍未充分验证；公开可读不等于授予开源复用许可 | 最值得研究其从玩法到本地打包和质量记录的流程；不把自动通关等同于好玩 |
| [NULLSPACE](https://github.com/marius4lui/NULLSPACE) | Godot 4.7.2、Blender；第一人称生存恐怖游戏 | 作者明确为开发中、Beta Unstable；有源码和发布入口，Windows交叉导出不等于Windows本机验证 | 观察场景、美术、构建、试玩证据如何持续维护；尚不能证明商业完成度 |
| [Jump Run](https://zenn.dev/tkada/articles/d0c31e6533fb62) | Unity 6.3 LTS、Codex/Astra、Kenney素材；3D障碍跑酷 | 2026-09-09作者制作记录，称约20分钟得到可玩版；有演示视频，含命令行验证说明；耗时为个案自述 | 小型规格与UI参考能约束产出，Unity也有可行工作流；不是纯鼠标操作成功率的对照实验 |

本轮检索覆盖官方开发博客、游戏展示目录、GitHub和开发者自述。搜索词包括 Astra game development、GPT-6 Astra Godot/Unity/game/github。排除同名产品、AI游玩现有游戏、二手转载，以及只有场景宣传而缺少制作说明的内容。以上是代表案例，不是穷尽性统计。

## 选型记录：Proposed

### 背景与约束

已确认目标是持续开发可发布的独立游戏。具体发行平台、目标硬件、画面规格、预算和团队既有引擎熟练度未确定。以下推荐以个人或小团队、2D／风格化中小型3D、PC优先为工作假设；它不是用户已确认的平台决定。

### 推荐

首选 **Godot 4稳定版 + 带类型标注的GDScript + Blender + Git + 自动规则检查与实际导出包试玩**。Astra通过Codex参与开发，不默认成为游戏运行时依赖。

| 职责 | 推荐组成 | 原因 |
| --- | --- | --- |
| 场景、渲染、交互、动画与UI | Godot 4稳定版 | 用完整游戏引擎承接制作工具和发行出口；开工时锁定引擎与导出模板版本 |
| 玩法与数据 | 带类型标注的GDScript、Godot Resource | 保持一套主要玩法语言，利用类型检查提前暴露连接错误；核心规则与视觉表现分开 |
| 3D资产 | Blender，交换资源优先glTF/GLB | 保留可修改源文件和明确导出资产；像素／纯2D项目按需使用，不强制加入3D管线 |
| 协作与恢复 | Git；大体积二进制资产按需Git LFS | 可审阅、可回退、固定可交付版本 |
| 验证与交付 | Godot命令行／headless检查 + 实际目标平台导出包试玩 | 自动检查规则、存档和流程；显示、输入、音频、性能与手感需要有画面和真实设备验证 |

Godot的[TSCN文本场景](https://docs.godotengine.org/en/stable/engine_details/file_formats/tscn.html)利于版本审阅，[命令行](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html)支持导入、运行和导出。由此推断：Astra能用文件编辑与可重复执行形成开发闭环，MCP可以增强体验，但不应成为基础可构建性的唯一入口。

[GDScript类型标注](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html)提供提前发现类型问题的工具。Blender可接入Godot的[glTF导入管线](https://docs.godotengine.org/en/stable/classes/class_editorsceneformatimporterblend.html)。Godot允许商业游戏，发行时仍需保留引擎和第三方声明，见[官方许可说明](https://docs.godotengine.org/en/stable/about/complying_with_licenses.html)。

### 备选与取舍

| 方案 | 优势与适用情况 | 本次取舍 |
| --- | --- | --- |
| Godot + GDScript + Blender | 可读场景、完整引擎、本地导出；已有Astra源码案例 | 首选；插件、平台集成与目标设备性能仍需项目验证 |
| TypeScript + Vite + Three.js | 浏览器试玩与链接分享，代码控制程序化表现；Void Explorer证据充分 | 网页优先时可改选；需承担较多游戏工具与系统整合，不作为本次长期开发默认 |
| Unity + C# | 已有Astra制作记录；团队已有Unity代码、资产与操作经验时有价值 | 有既有投入或明确平台SDK依赖时重新比较；本次没有这类约束证据 |

Three.js的[游戏制作说明](https://threejs.org/manual/en/game.html)将其定位为3D库，缺少完整游戏引擎所提供的一些系统。该页本轮可取得搜索索引正文，但直接打开返回404，引用核验有限；关于本次选型的核心判断同时依赖已打开的Void Explorer作者文章和Godot文档，不把单一失效页面作为结论基础。

代价：GDScript与Godot资源存在引擎绑定；未来迁移到其他引擎不能直接复制整套场景。Web也不是原生桌面导出的等价物；[官方Web导出说明](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html)列有渲染与C#限制。若Web成为主要平台，需重新评估。

本次尚未设计完整技术架构；实际代码目录、模块、命令、测试实现和发行流程应进入目标代码仓库。本研究不启动当前暂缓的设计测试。

## 对《言咒》的影响与下一步

当前[核心构思](../../game-design-workflow/core-concept.md)是战前法术编排与自动战斗；[第一人称战场](../../docs/battlefield-and-environment.md)仍需按自身来源状态处理。研究支持的判断是：持续开发时应优先选择能把复杂规则验证、场景和界面一起维护的工具，不因网上演示漂亮就扩张玩法或采用其生成世界系统。

现有代码资源身份见[开发索引](../../docs/code-development-index.md)。本次没有审查对应代码仓库，不估算迁移量，也不建议仅凭这份通用推荐重写现有原型。

最自然的下一步：在用户决定进入实现时，先明确首发平台和最低设备，审查已有代码的可复用部分，再用同一份已确认规则制作小型纵向切片，检查一轮配置—战斗—结算、存档恢复和目标平台导出。选型仍为Recommendation / Proposed，不是Accepted。
