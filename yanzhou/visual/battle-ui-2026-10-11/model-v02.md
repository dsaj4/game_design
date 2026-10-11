# AS-G002-010 战斗桌面 Blender v02

2026-10-11 · game-002 / main · BATTLE-3D-02 · ReadyForScope（透视/卡型评审）/ PresentLocal。

用户要求：“1.适当增加一点摄像机角度，做到近大远小的效果;2.卡牌适量做窄一点，类似扑克牌”。按此修改[建模v01](model-v01.md)，保持CUSTOM视觉建模材料范围。

- 主相机改为50毫米透视，俯视约49度，前沿物件更突出；同尺寸近排卡牌投影宽度比远排约大6.5%。GLB也保存主透视相机。
- 卡牌高度和中心不变，宽度统一收窄约11%–18%，牌型更修长；对应空位框同步收窄。上、下排仍共用世界坐标刻位，透视投影下自然形成纵深。
- [Blender v02](E:/Project/yanzhou-battle-3d/v02/yanzhou-battle-v02.blend) · [GLB](E:/Project/yanzhou-battle-3d/v02/yanzhou-battle-v02.glb) · [主图](E:/Project/yanzhou-battle-3d/v02/renders/main.png) · [灰模](E:/Project/yanzhou-battle-3d/v02/renders/clay.png) · [斜侧图](E:/Project/yanzhou-battle-3d/v02/renders/oblique.png)。
- [制作说明及20份组件库](E:/Project/yanzhou-battle-3d/v02/README.md) · [修改数据](E:/Project/yanzhou-battle-3d/v02/revision.json) · [实际检查](E:/Project/yanzhou-battle-3d/v02/verification.json) · [文件与SHA-256清单](E:/Project/yanzhou-battle-3d/v02/manifest.json)。

实际检查：八张卡牌尺寸、十四个空位框、主场景物件完整入镜；原生重开与打包纹理、组件库加载及GLB回导。文件另存v02，v01的45项交付文件按原清单逐个核对保持原哈希。牌面插画随牌宽缩放，原PNG和UV取图范围未改。详细尺寸属于本轮制作假设，不写入玩法规则。

固定交付共38个文件；manifest SHA-256：`a3bb4a3bd60562b0605e1dc3c476384b4e68b749d646f76cebf135b4632c4ddd`。20份组件库实际加载通过，GLB JSON内主相机类型确认为perspective。

沿用v01的材质导出限制与未完成项；本轮只调整相机和卡型，没有新增玩法或性能验证。原件保存在本机独立制作目录，未公开上传；本项目改作授权及上游分发权Unknown沿源包记录。
