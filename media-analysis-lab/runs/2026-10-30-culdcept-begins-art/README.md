# Culdcept BEGINS 卡面与美术资源

2026-10-30 · **Research / StaticArtifactEvidence** · AS-SH-005@CULDCEPT-ART-2026-10-30-v01。

用户指定使用本机 `E:/Game/Demoncards/rea` 分析 `E:/Game/Culdcept BEGINS`，重点提取卡面和美术图像，并把结果交给“设计法器与卡面风格”对话完成一轮卡面设计。本轮只处理发布文件与图像，不加载《言咒》玩法材料；视觉研究不代表正式设计采纳。

**打开[本机资源图册](<E:/Game/Culdcept BEGINS-analysis/2026-10-30/index.html>)。** 默认展示407张普通卡面，可按原资源名搜索、切换类别与Texture2D／Sprite，并点击查看源尺寸PNG。

![24张风格样本](<E:/Game/Culdcept BEGINS-analysis/2026-10-30/previews/style-overview-01.jpg>)

## 提取范围与数量

120个本机Unity资源包及13个顶层`.assets`全部完成清点。序列化版本均为Unity `6000.0.61f1`；游戏发行版本Unknown，以源文件SHA-256固定本次安装。共识别9,935个Texture2D／Sprite对象，导出**9,913个PNG，2,927,355,437字节，约2.73 GiB**。另外22个对象是0×0的空字体图集，不含可导出的图像。纹理和Sprite可能呈现同一作品，不能把文件数当作独立插画数。

| 资源 | 文件与规格 | 本机图册类别 |
| --- | --- | --- |
| 普通完整卡面 | **407张Sprite，均248×451**；对应432张Texture2D，包含256×512卡纹理及包内附属图像 | `01-card-images` |
| 遮蔽版本 | 407张Sprite＋407张Texture2D | `02-card-blind` |
| 独立主体图 | **409张Sprite**；对应409张1024×1024Texture2D，Sprite按原有效区域输出、尺寸不一 | `03-card-3d-sprites` |
| 卡牌材质纹理 | 434张：402张512×64名称纹理，23张2048²与9张1024²底材／法线／材质／贴花纹理 | `04-card-material-textures` |
| 牌包及相关资源 | 143个PNG | `05-card-pack-and-models` |
| UI、书本 | 1,088个PNG | `06-ui-and-books` |
| 角色相关 | 987个PNG | `07-characters` |
| 特效纹理 | 385个PNG | `08-effects` |
| 其他美术纹理 | 4,405个PNG | `09-other-art` |

分类用于查找，依据资源包名，不宣称已识别每张图的实际游戏用途。导出图保持原解码尺寸及透明信息，没有AI修图、锐化或放大；Sprite依据Unity原矩形／图集信息解包。22张JPEG接触表属于缩略预览，不能替代PNG原件。网格、材质、Shader、字体和文本已清点，但本轮没有导出模型几何、字体文件、音视频或游戏代码，也没有还原运行时合成／动画。

[407张卡牌对应表](<E:/Game/Culdcept BEGINS-analysis/2026-10-30/card-catalog.csv>)把普通卡面与高清主体按原资源名配对：406项精确匹配，`SPR_Card_C_ALGA`没有同名高清主体，保留Unknown，不凭画面猜配。409个主体也不表示409个独立卡种。

## 目视观察：三种图像语言共用纸张与牌式

下列判断来自实际查看24卡风格板、42主体预览、8盾牌专题、单张HEALR卡面及一张2048²底材，不等于逐张艺术审阅全部资源。

- **生物／人物**：大块轮廓与硬边棱面组织形体，细节有所省略，暗部常呈深色块；少量有力的色彩落在纸张底上。GLAD、SAMRAI、HEALR、GOLEM可作比对。不是所有资源都遵循同一种棱面画法。
- **器物／盾牌**：有更明确的体积、金属高光、边缘与装饰细节。KSHLD、CounterShield、E_SHLD等以完整实体盾作为主角；不能把它们概括为极简木刻图标。
- **法术**：MBOLT、ACID、WaterShift等使用颗粒印刷、蚀刻式线条和局部小场景，并常配几何围合。该路线与生物的大色块不同。
- **共同牌式**：暖粉褐旧纸、窄边与磨损、顶部小符号、底部短字形带；主体四周留有空间。装饰与纸纹统一家族感。提取的短字形带不能当作已解读文本或《言咒》可用文字体系。

![8张盾牌参考](<E:/Game/Culdcept BEGINS-analysis/2026-10-30/previews/shields-01.jpg>)

## 交给卡面设计对话的一轮任务

这是用户授权的**视觉探索制作**，不更改《言咒》现行规则、卡种或信息合同。目标对话保留其已确认设计约束，先实际查看上方风格板、盾牌专题与相应PNG，使用本次资源理解媒介和牌式，再生成原创卡面。旧A1负形＋B1刀刻属于前轮路线，本轮以Culdcept参考另做一版，避免自动混成旧朱墨盾牌。

建议以**护盾单卡为必交主件**：完整盾身、盾缘与中脊清晰可见，主体直接表达护盾，延续用户已经明确的“手抓球不行”。可围绕目标对话已有主题补两张同套样张，比较家族一致性，不擅自发行新卡或新规则。

本轮优先比较暖旧纸上的器物体积、克制装饰、可辨的主体轮廓与色彩关系；若延用该对话的卡面无字约束，去掉参考中的题签和角标，并重新安排留白。角色色块、器物细绘、法术蚀刻三条语言需明确选择，不能只写笼统的“低多边形风格”。产物标为Raw视觉候选并登记固定文件／提示词／引用关系，用户接受PendingReview；未授权把第三方原图直接作为运行卡面或公开分发。

## 固定版本、检查与复用登记

| 字段 | 内容 |
| --- | --- |
| 归属／维护位置 | shared-reference / media-analysis-lab；本页唯一维护；AS-SH-005 |
| 用途 | 卡面、独立主体、纸张底材及装饰的本机视觉研究；标签：Culdcept、卡牌、盾牌、纸张、Unity |
| 固定包 | [package-manifest.json](<E:/Game/Culdcept BEGINS-analysis/2026-10-30/package-manifest.json>)；SHA-256 `97e936ad27055530b9dcd32e9f4832c498a1d6fa1332f2193c84c48394597684` |
| 源／导出范围 | 包内inventory.json固定133个源资产文件的SHA与对象索引；补充可执行文件、IL2CPP元数据等身份；exports.json固定每个PNG的源包、CAB、path ID、原资源名、容器路径、尺寸及SHA |
| 工具／证据 | REA 6.4.0，提交`58300885207133422af235e0f2b10658cf958b03`；UnityPy 1.25.4，依赖锁与提取脚本保留本机包；[UnityPy上游说明](https://github.com/K0lb3/UnityPy) |
| 状态 | ReadyForScope / PresentLocal，2026-10-30，仅静态图像提取、文件验证与上述抽样目视 |
| 检查 | 9,913个PNG的SHA、尺寸与完整性全通过；9,935对象全部由导出或22空图集覆盖；133源文件重算SHA无变化；无未解决导出错误 |
| 来源／条件 | 用户指定本机第三方游戏；原作者与资源再分发许可Unknown，仅本机内部研究与风格参考。原游戏文件、PNG、网页图册及技术原始输出不入Git，不扩大公开分发／直接接入游戏授权 |
| 关系 | uses: None；derived-from: 用户指定安装文件的静态解码；目标使用者：“设计法器与卡面风格”对话，限本轮原创视觉探索，实际生成产物由目标对话登记 |

REA实际运行了`inspect-artifact`（指定EXE）、`inspect-pe-resources`和`inspect-managed-artifact`（GameAssembly.dll），证据分别保存在包内rea-executable.json、rea-pe-resources.json、rea-gameassembly.json。REA确认PE文件身份与GameAssembly不含CLI元数据；**Unity图像清点／解码由UnityPy完成，不冒称REA原生提取功能。** IL2CPP判断另有安装中的GameAssembly与global-metadata.dat相互佐证，没有反编译完整程序或启动游戏。

初次读取资源目录的REA路由不接受普通目录，随后改为EXE；初版脚本的PPtr API适配及跨包Sprite依赖缺失已修正，十个跨包UI Sprite重试成功。失败原件与恢复经过保留本机。未验证游戏内展示、交互、动态合成、全部视觉用途或玩家可读性；这些未知不影响本次固定图像包的交付。
