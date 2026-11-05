# 首战器物可用资产

2026-11-04 · game-002 / main · **AS-G002-042 / FIRST-BATTLE-ART-02**。统一目录由总控登记，本对话不占用新编号。

**[打开四件器物审阅板](E:/Project/yanzhou-ui-prototypes/first-battle-art-2026-11-04/index.html)**

按用户授权制作三件修订透明法器与小炉候选；共同输入固定 `e67e8c1748079abbf6f08d06be91fd0740422e86`，CUSTOM，CORE-076 / GDD3.9 / CONTENT-LIBRARY-08。画法沿 WAYS-ART-BASELINE-02，三法器保留 AS-G002-042@FIRST-BATTLE-ART-01 的身份；小炉只参考其画法。2026-11-05（Asia/Shanghai）用户明确通过review并授权正式列入可用资产；四件图稿用户接受均为 **Accepted / AvailableForUse**，不改玩法或内容资格。

| 器物 | 内容ID | 本轮源画布 | 实际占形 |
| --- | --- | --- | --- |
| 黄铜显咒灯 | alchemy.artifact-lamp | 724×2172 RGBA | 1×3，3格 |
| 盘管萃炼器 | alchemy.artifact-extractor | 1024×1536 RGBA | 2×3完整矩形，6格 |
| 白瓷曲颈瓶 | alchemy.artifact-retort | 1024×1536 RGBA | 四格L：[[0,0],[0,1],[0,2],[1,2]] |
| 小炉 | alchemy.hearth-small | 1254×1254 RGBA | 1×1，1格 |

占形来自固定版本 catalog 与 artifact-geometry；透明画布、留白和 alpha 不定义点击几何。源件按逻辑包围框中心锚点等比装入；这是本审阅板定位方式，尚未宣称主工程宿主适配。核心、状态、名称、数值和激活反馈由宿主独立绘制。小炉的炭盆外观已通过用户审阅，不授予生产或核心装配能力。

内置 image_gen 共4次，每件独立生成；准确提示词、参考角色与SHA、原输出路径、持久源件、尺寸、alpha及可视包围框见 [manifest](manifest.json)。三法器重新构图，未非等比拉伸旧图；四源件均逐字节复制生成原件，未抠色、裁切或修改alpha。旧包和参考原件保持原字节。原件保存在 `E:/Project/yanzhou-art-assets/first-battle-2026-11-04/sources/`，派生审阅、脚本与证据在独立审阅目录。

![深浅紫底及224／64px静态检查](E:/Project/yanzhou-ui-prototypes/first-battle-art-2026-11-04/evidence/alpha-small-review.png)

已检查4件解码、SHA与原字节一致、画布／格形比例、各占用格有主体、曲颈瓶空格、三底色224／64px等比预览及0／90／180／270度格形合成。静态目视未见明显底色板、白边或轮廓裁切；四主体在64px下仍可区分，细部不承担文字信息。萃炼器和曲颈瓶最大alpha为254而非255；曲颈瓶两处空格最大alpha为1/255、alpha≥32像素数为0。低alpha残留未处理，不称为严格全0遮罩。萃炼器底部源件安全边距仅6px，后续宿主须按完整画布contain，不能裁紧。

检查为 Pillow 静态合成与目视，不是独立用户辨识证据。HTML图片路径检查通过；浏览器、引擎、真人辨识、玩法与平衡检查均NotRun。素材可访问性PresentLocal，ReadyForScope覆盖本轮已接受图稿及静态审阅，可供项目资产接入使用；无发布或分发验收。使用Windows本机字体绘制审阅图，未打包字体或第三方原图。

本轮仅新增本目录README、manifest和4份prompts；外部新增4份源PNG、审阅index.html、jobs.json、build.py、finalize.py及2张evidence PNG，准确路径及指纹由manifest列明。需总控完成AS-G002-042续版与使用关系登记、按需同步内容库美术关联；四件图稿已由用户明确接受；共享目录与内容库关联仍由总控集成，非用户审批待办。共享分支 `codex/2026-11-02-tabletop-html`，本对话不提交、不推送、不改共享索引；总控统一集成。
