# 四样件最终独立复核

2026-10-15（America/New_York）· 设计 D / component_detail_design · COMPONENT-SAMPLES-QA-01

**结论：TXT-01、CARD-01、WAND-01、PAWN-01 的 Q1 / Q2 均通过，可交 Godot 限定接入（ReadyForScopedIntegration）。这不是用户最终美术接受，也不是 Q3 / 完整战斗验收。** 本结论只针对下面固定包，不扩展到另外十五组件。

## 固定包与实际核验

资产包：`E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/sample-v01/`，AS-G002-018 / COMPONENT-SAMPLES-01。

| 固定输入/输出 | SHA-256 |
| --- | --- |
| 设计包 manifest-v01.json | `28568ce85aa3680cdd6298f4803d4059d1a48edf268fea9677fd0686d59c7e97` |
| 资产包 manifest.json | `e81b4175ed0d9b0f4ba7a4656ae6a14a87a5e6a5a2832848ed1e765feb3cbd3c` |
| models/four-samples-source.blend | `2ba59d4a572d7593faef6f6a25902314a8c9ace1bb3dede7388ee36091f7abb7` |
| TXT-01.glb | `dcdb4370149d156b35263f8870a9d9d2582de4d2b83229eb2fd8a7a7c962a290` |
| CARD-01.glb | `4080ca8ace7ced14cb5c3e6a067e0f731d4be33fe3cc17ec799a6f2f2a3c861f` |
| WAND-01.glb | `c74c223c2941e08bba62dfb2e4d8a8e6d672fe8176b3798c342e8074d4f76976` |
| PAWN-01.glb | `c5db71cbd5744cdea2a4e8fc43e06be27aca2fd579111b74ac066d80d2a36011` |

固定规格取自设计 brief / components / 几何更正 SVG；效果板的局部排除继续有效。质量门槛沿 `component-detail-higgsfield-assessment-2026-10-14.md` §5/6，没有新增玩法或装饰要求。

D 实际使用 `view_image` 分轮查看四向黏土、中性材质、细节、掠射图；最终额外查看四张 `*-glb-roundtrip.png` 和环杖背垫两张近景。独立只读核对资产 manifest **119 / 119** 个文件的 SHA-256 与 bytes，全部匹配；读取四个 GLB 的 JSON 验证 glTF 2.0、稳定根和材质分件；源 / GLB / 回导图与报告哈希均一致。详见 [source-verification-d-v01.json](source-verification-d-v01.json)。

Blender 源重开、修改尾帽倒角 0.6→0.5mm 的独立重导探针、GLB 回导几何检查由专门资产 agent 实际执行，D 阅读 `reports/verification.json` 与 `reports/roundtrip-render-evidence.json` 并核对其对应文件；D 没有冒充独立执行 Blender。四件源与回导 AABB delta=0，无缺 UV / 图、退化三角、非有限顶点或无效法线。源可编辑保留方式不完全相同：CARD 为可编辑顶点/材质节点及重建参数源码，其他件另有曲线/修改器；不把 custom property 描述当成实时驱动器。

## 逐件 Q1 / Q2

证据路径以资产包为根；所有结论仅覆盖静态样件。

| 组件 | Q1 | Q2 | 通过依据 | 接入后的残差 |
| --- | --- | --- | --- | --- |
| TXT-01 | Pass | Pass | 削角皮底、端夹、缝线、凹纸实际分件；皮框顶1.20mm、纸面0.85mm、凹深0.35mm，夹片底1.20mm。`TXT-01-detail.png` / `TXT-01-raking-material.png` 无共面黑纸，纸/皮/铜反射不同。`txt01-scaling-test.png` 的72/220/300px×20/18px六种离线读数清楚，端夹不拉长、针脚不被拉成线 | 真实引擎排版、字体、锚点、遮挡仍需 Q3。GLB是物理样件，不应整体拉伸；屏幕文字皮肤取 `ui/` 的固定端区+中段重复层，文字继续由运行层生成 |
| CARD-01 | Pass | Pass | 63×91×0.45mm、R3mm和0.15mm微倒角；四向薄体、`paper-edge-detail` / `corner-edge-detail` 暖灰三层纸芯连续，无粗塑料/金属边。正背在同灯架可读。新原创盾墨以30×40mm接独立alpha源层，负形露纸、不占标题/核心值安全区；最终回导保留身份 | 目前只完成代表防护面，另外四类卡图未声称完成。真实牌尺寸下的墨纹/字重、未揭示信息边界、合法翻面与原位显现/使用留 Q3；本次无动画闪烁测试 |
| WAND-01 | Pass | Pass | 长201.6mm、外环61.74mm、环壁3mm、气隙2mm、柄径11.97mm；连续外环/顶开内环、两耳夹与三贯穿铆钉、六组浅刻、斜缝皮握柄、三分带、尾帽搭接均可见。`clamp-side-detail` / `raking-material` 显示真实接合与铜皮区分。两张 `back-pad-*-detail` 显示实际外露毡垫；报告二垫最高源Y同为9.150000289mm，分别与耳夹/尾帽有实际相交 | 放入桌面后仍须按后背共平面确定姿态，未做物理仿真。计时圈显隐/枢轴和加工反馈由运行层控制；GLB不继承Blender隐藏状态，接入时须显式管理 |
| PAWN-01 | Pass | Pass | 真罩腔与暗槽、封闭非对称斜肩、三道连续V宽褶、窄腰/下摆切面、三级底/铜嵌线/毡脚清楚；四向一致，不再是球头旋转体或套环围脖。中性/detail/raking图保持墨绿哑光木、铜和毡的差异。高141.7556mm、底径56.7mm；与141.75mm规格差0.0056mm按建模/倒角容差接收 | 真实主视角缩小可辨性、敌我对照和受击/防护局部反馈留 Q3。不得把整个棋子换成发光球；本样件没有骨骼或动态布料 |

### 补充墨绘来源

`E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/illustration-v01/shield-ink-v01.png`，1086×1448 RGBA，SHA `0156e2d4f967179d911e2bff9cf918afc8d38000fc7ede1c14f340d2eda9be51`。总控用内置 image_gen 生成，原字节保留；D 实际目视确认深墨面、双边线、纸色负形十字、方向排线/断墨符合固定A板，无新增图案含义。源材质独立层叠，GLB使用UV对齐派生合成，不烘入运行文字。未修改冻结设计包或直接复用参考游戏像素。

## 可交接范围

1. 四个固定 GLB、米制尺度、真实分件/材质/枢轴、TXT 静态分层底图可交 Godot 做**限定接入**。读取 `reports/asset-bindings.json` 的稳定根、轴、材料和动态字段安全区，不凭截图重猜绑定。
2. Q3 应检查两档布局的字体和常驻量、真实3D宿主拾取/焦点/近观、卡牌公开边界、物件接触、计时圈、源亮后原位显牌、卡亮与目标局部效果同起。暂停/单步/载入静态与消费锁语义继续沿既定实现。
3. 本次 Browser NotRun；离线六种排版图不冒充浏览器。Godot加载、OS输入、双分辨率实时表现、性能、完整战斗与用户视觉接受均 NotRun。
4. 另外十五组件可依据通过的类别样件继续排期，但不能从这四件直接推为全部资产或真实场景通过。后续扩量仍沿类别Q3门槛和总控调度。

旧失败与返修过程留在 [sample-review-v01.md](sample-review-v01.md)，制作包 `renders/q1-review-01/` 与 `renders/q2-review-01/` 保留实际失败图；没有删去失败路径。此轮 D 没有改源模型、运行工程、冻结设计包、分支或提交。
