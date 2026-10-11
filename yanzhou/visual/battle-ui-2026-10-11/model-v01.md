# AS-G002-010 战斗桌面 Blender 建模首版

2026-10-11 · game-002 / main · BATTLE-3D-01。ReadyForScope（静态三维结构与视觉评审）/ PresentLocal；尚未完成最终美术验收或实时性能验收。

用户本轮要求：“阅读交接文档，开始进行真实blender建模”。本次交付真实几何、材质、可编辑源工程与标准导出，未新增战斗规则、交互实现或玩法测试。原效果图选择仍仅是视觉初版选择，不把本次建模自动记作采纳。

## 文件入口

- [Blender 总场景](E:/Project/yanzhou-battle-3d/v01/yanzhou-battle-v01.blend) · [GLB 导出](E:/Project/yanzhou-battle-3d/v01/yanzhou-battle-v01.glb)
- [主视角](E:/Project/yanzhou-battle-3d/v01/renders/main.png) · [同相机灰模](E:/Project/yanzhou-battle-3d/v01/renders/clay.png) · [斜侧视角](E:/Project/yanzhou-battle-3d/v01/renders/oblique.png)
- 近景：[短杖](E:/Project/yanzhou-battle-3d/v01/renders/wand.png)、[环首杖](E:/Project/yanzhou-battle-3d/v01/renders/scepter.png)、[法典](E:/Project/yanzhou-battle-3d/v01/renders/book.png)、[晶球](E:/Project/yanzhou-battle-3d/v01/renders/orb.png)、[红冠棋子](E:/Project/yanzhou-battle-3d/v01/renders/enemy.png)、[兜帽棋子](E:/Project/yanzhou-battle-3d/v01/renders/player.png)。
- [制作说明与独立组件入口](E:/Project/yanzhou-battle-3d/README.md) · [固定文件清单](E:/Project/yanzhou-battle-3d/v01/manifest.json) · [验证记录](E:/Project/yanzhou-battle-3d/v01/verification.json) · [输入指纹](E:/Project/yanzhou-battle-3d/v01/source-inputs.json)。

原件保存在独立本机持久目录 `E:/Project/yanzhou-battle-3d/`。设计仓库只登记入口、范围和证据，不提交大型二进制、建模脚本或工具安装包。本机存在不代表其他机器可访问；未公开发布。

固定交付清单包含45个文件，合计111,897,082字节；manifest SHA-256：`de2e6880f800bb767a034dd426eda0411fbe44aaf10ed33e6a2f0f7525390739`。四张纹理按RGBA8展开约24 MiB（不含mipmap/运行时额外占用）。最终原生工程再次重开、20份组件库实际加载均通过；GLB回导场景包围盒最大偏差0米，材质差异另行保留。

## 参照与实际覆盖

CUSTOM / 视觉建模材料。设计来源锁定提交 `59b20e64cbdd492ae28c0b6fa8a73ebadb7cba72`，读取交接、[HTML v10 布局说明](v10-outline.md)及其 HTML 原件、[已选效果图](battle-art-v01.png)、[19 张组件参考及生成记录](components-v01/README.md)。未扩读 CORE/GDD、其他方向或历史游戏。

derived-from（视觉改作）：AS-G002-008@BATTLE-UI-ART-01、AS-G002-009@BATTLE-COMPONENTS-01；uses：DM-G002-010@BATTLE-UI-HTML-10 布局参照。组件包中 11–14 直接作为卡面纹理引用，其余 PNG 只作目视造型参考。模型与程序材质本轮新建，书房为简化几何，未使用背景图片板。

桌体、桌垫、凹槽抽屉、两棋子、可拆筹码、厚度卡牌和四法器都已建立实体。卡牌上下同列、空位、两主体与时间轴中点居中；抽屉三格与右侧内向把手保留；四法器沿前沿分散。组件集合按 01–19 命名，抽屉另拆外壳/移动组。未恢复状态牌、法器托盘或战斗操作面板。

桌宽 2.8 米为首轮制作假设。Blender 原生 Z-up、米制，GLB 按标准 Y-up 导出；原点与复用约定见制作说明。原生场景求值约 61.4 万三角面，含书房与细饰线，尚未按实时预算优化。原生程序木纹/皮革凹凸和晶球体积雾未烘焙进 GLB；导出采用简化 PBR 与晶球透射替代，差异见 [GLB 回导渲染](E:/Project/yanzhou-battle-3d/v01/renders/glb-roundtrip.png)。

## 检查与待评审

检查范围：Blender 原生工程重开、四张纹理打包、GLB 实际回导、尺寸和朝向对照、组件库入口、主图/灰模/斜侧图/六件近景。布局坐标与卡牌空位按参考检查；四法器依据实际求值几何调整桌沿接触，修正了初稿兜帽朝向和法杖悬空。原输入 PNG 与 HTML 保持固定哈希。

本版属于静态建模首版：纹样、背面、抽屉连接及布景做了保守简化，雕刻精度、磨损细节和灯光质感与概念图仍有差距。移动抽屉预留根对象与导轨，不代表完整开合机构已验证；未做 UV 烘焙、LOD、碰撞、动画或目标引擎适配。性能预算和目标引擎 Unknown。玩法与体验验证 NotRun。

本项目评审与改作授权沿本轮用户请求及源包记录；上游参考的对外分发许可 Unknown。没有发布或上传源模型。登记不改变现行玩法或视觉方案的采纳状态。
