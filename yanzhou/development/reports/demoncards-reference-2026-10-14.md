# Demoncards 第一表现参照：证据与制作映射

2026-10-14 · game-002 · ImplementationIndex。用户授权读取本机游戏并制作真实牌桌；设计仍由既有「言咒设计对接」负责，总控负责画面、接线和交付。材料范围CUSTOM，仅限本次交接白名单及相关实现。

## 固定来源

[原件清单](E:/Game/Demoncards/verified-2026-10-14/source-manifest-v01.json)固定启动器、主程序、pak、两篇用户已有报告、两个OBJ与两份数据。主程序SHA-256 `cb2581db83f4af6c6f8de2138049720df7ad52a5f8a8bdc71aabcdde71ecb2fc`；pak `c61d079f5a853f51b52b81d1799f8c3595b8a2d079a1d449329af4597075ebd4`。原件就地保存，原报告作为待核线索，不作为已证实机制。

REA 6.4.0 inspect-pe-resources返回真实Evidence ID `ev_62295047dc200d899daf69bb3a1b6196be15d607561848e1bdf752f31dc0788b`，保存在[原返回](E:/Game/Demoncards/verified-2026-10-14/rea-main-pe-v01.json)。本机未注册REA MCP；没有改配置。后续pak／UE属性解析是普通离线静态取证，不能冒充REA记录或实际运行。

## 已观察与静态结论

[真实菜单／教程截图](E:/Game/Demoncards/verified-2026-10-14/runtime-v01/02-table-intro.png)与同目录录屏展示暖暗木质房间、酒红桌布／黄铜边、宽木桌沿、薄纸牌、厚技能盘和局部烛光。真实选牌出现小幅抬起／转角和黄描边；没有取得成功部署、完整物品使用或详情打开的可可靠测时样本。教程录屏01／02存在掉帧或PTS警告，03／04按CFR15保存，也未观察成功部署；不得据此填写精确曲线、运行节点或帧时长。

[B完整类型证据](E:/Game/Demoncards/verified-2026-10-14/static-b-v01/typed-evidence-v01.json)SHA-256 `1eb267f32f31c0b00718eb01f176eefc2d4b3fdb01ac4346e0045311ff0d6aa2`：31项导出由4个CurveVector、14个CurveFloat、13个TimelineTemplate组成，按属性类型和serial size完整消费。Common长度0.7、Weak 0.5；RotFlip长度0.5，关联曲线键值0／180@0.2／180@0.3／360@0.5；brightness关联曲线长度0.15。实际调用、轴映射、播放倍率和场景用途仍Unknown。

悬停Alpha实际关联外部Curve_CardScale（0→0、0.06→0.288、0.18→1，weightedBoth cubic）；旧报告把内部CurveFloat6误作Alpha，该导出属于RotAlpha。返回Alpha对应CurveFloat8／RotAlpha7。[外部曲线证据](E:/Game/Demoncards/verified-2026-10-14/static-b-v01/external-curve-v01.json)单独保存关联与原字节指纹。

Card_fixed.obj为192 split顶点／64焊接点／124面，186焊接边均为两面使用，闭合无退化；原Card.obj有53退化面和非流形边。固定OBJ与原Card.uexp 192顶点最大误差小于5.1e-5、372个uint16索引完全相同。局部600×10.0002×800，仅证明3:4比例和宽1/60的厚度，世界scale Unknown；圆角rx47.9277／rz63.9036，为完整宽高各7.988%，不是旧报告所写27cm半径。

## 在言咒中的制作采用

[DC-v01设计](../../visual/demoncards-reference-2026-10-14/design-v01.md)采用相似纸感、桌布、旧木、黄铜、暖主光及短促过渡。言咒正式卡比例沿9:13，不照抄参考OBJ尺寸；材质和线绘是自制重建。没有导入参考游戏的像素、模型、文本、音频或pak内容到运行包。

完工来源先亮再原位显牌；使用卡与真实目标同起；新公开r→T及真实预计拍改变可转位；暂停详情立即静态，关闭仍停。参考抬牌仅列观察，不覆盖言咒无悬停缩放／暂停不补动画的合同。[来源与采纳](../../sources/draft-changes/D-2026-10-14-demoncards-presentation.md)只改变必要只读文字容器与合法展示动作，Q、结算、公开资格、消费锁沿EX-002。

实际运行包、源／包检查、失败修正和未验范围集中在[第九批集成](E:/Project/yanzhou-godot/docs/reviews/2026-10-14-demoncards-integration.md)。参考运行缺口不写成完成，技术检查不替代用户对相似度和最终画面的接受。
