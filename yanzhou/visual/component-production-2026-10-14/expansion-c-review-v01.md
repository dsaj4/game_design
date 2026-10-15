# C 桌面组件独立复核 · v01

2026-10-15（America/New_York）· D / component_detail_design。

**TABLE-01、MAT-01、DRAWER-01 的 Q1/Q2 通过，可交限定接入；SLOT-01 的空态与压位结构已核，但三张状态图裁切，完整状态复核待补图。** 不因该补图阻塞其他三件，也不把 C 独立装配图通过外推为当前游戏相机/拾取通过。

固定包：`E:/Project/yanzhou-battle-3d/component-detail-2026-10-14/expansion-c-v01/`，AS-G002-020 / COMPONENT-EXPANSION-C-01。manifest SHA `3792ae0bf401b418723181917125c81d6df14f8bf0fb64f7a7fe2fe0d529f61a`；源 SHA `9f4670d8fac82c489fb75873b0081ed634bf065d70ab3403e70566283194e163`。总控已独立核152/152文件bytes+SHA，D采用该结果；D另实际解析6个GLB及解码内部MR图。没有改写源、GLB或原manifest。

## 实际查看与证据归属

D 实际 `view_image` 查看18张：最终GLB实回导 `FINAL-GLB-roundtrip-assembly-neutral`、`FINAL-GLB-roundtrip-contact-detail`；Q1阶段 `Q1-runtime-edge-profile-clay`、`Q1-mat-hem-detail-clay`、`Q1-slot-depression-detail-clay`、`Q1-drawer-join-detail-clay`；最终几何 `Q1-final-rail-installation-cutaway-clay`、`Q1-final-drawer-mounts-clay`；材质/状态 `MAT-01-runtime-fit-weave-hem-detail`、`MAT-01-runtime-fit-raking`、`FINAL-MAT-felt-underside`、`FINAL-SLOT-cloth-pressure-neutral`、`SLOT-01-reserved`、`SLOT-01-history`、`SLOT-01-focus`、`FINAL-DRAWER-neutral`、`DRAWER-01-handle-detail`、`TABLE-01-runtime-fit-raking`，均为renders目录PNG。

只有前两张是最终GLB实际回导图。其他图的源版本按包内 `reports/render-provenance.json` 区分：首轮Q1图来自511db…源；多数单件材质图来自f3128…源；FINAL非回导与Q1-final来自fc3c63…源，即最终安装几何、粗糙度直连导出修复之前。D未把早期图误记成最终GLB渲染。最终回导图与D直接MR解码用来确认最终派生保持材质层次。

## 分件结果

| 组件 | Q1 | Q2 | 具体结论 |
| --- | --- | --- | --- |
| TABLE-01 | Pass | Pass | 65mm包沿与桌板、裙板分件清楚，45度拼口、上下圆弧与中腰直壁、浅凹榫塞能在黏土及近图辨认。runtime-fit只重建平面，板厚/包沿未按不同轴拉伸。最终GLB图保留木长纹/转向端纹及较亮接触沿、较暗凹位；不是靠新增噪点替代结构 |
| MAT-01 | Pass | Pass | 薄体、底毡、双层折边、两道缝线及暗金织带独立可辨，缝线已露出表面；贴桌接触成立，无角部翘起或掩盖空隙的整体抬升。近图经纬细节低对比，掠射没有金属镜面；全景中纹理不抢纸牌区域 |
| DRAWER-01 | Pass | Pass | 两级前板、真实梯形燕尾、两隔片三空格、双支座拉环和侧轨可辨。固定轨/安装块与移动箱分开；最终局部图显示实际桌底安装。木/皮衬/暗铁轨/铜环材质区分成立，不靠材质名代替目视 |
| SLOT-01 | 局部已核，完整状态待补 | 空态/材质方向已核，完整状态待补 | 窄卡比例、短角线和0.3mm压位QA成立，未生成假牌。reserved/history/focus三张现图上下裁切，不能据此声称完整四角/全长状态均已审。仅需独立补完整构图图，不要求修改几何或材质 |

## D 独立检查与作者执行证据

只读脚本 `audit-mesh-c-v01.py`，输出 `expansion-c-independent-check-v01.json`：D独立解析六个GLB的glTF2.0结构、根/状态/移动节点与材质，解码内部MR图。实际runtime桌的有效roughness均值为接触沿0.5280446、长木0.6680341、凹槽0.7880412，木材有效metallic均为0，确认粗糙度差异已进入最终GLB，不只是Blender节点记录。材质并未换成统一光亮塑料。

源重开、修改参数后四项另导探针、六件回导AABB/UV/法线/退化面检查由C作者实际执行；D读取报告并核固定源指纹，不冒称自己再跑Blender。报告六GLB尺寸回导差0，缺图/UV/非法法线/退化面0；四项编辑探针不同于正式派生且未覆盖原件。D没有做物理仿真。

runtime-fit实际桌749.411762×497.823536mm，顶Z=0、含裙高108mm；垫642.352939×347.941190mm，底Z=0，织体2.2mm、折边3.5mm，独立细丝使总包围高约3.61084mm。垫搭入齐平包沿11.4706mm，桌/垫基面间隙为0。此平面派生有总控明确授权；原1100×760桌及720×500垫仍保留，SLOT/CARD比例不变。

抽屉面144.9×40.95mm、木箱深113.4mm，含轨总宽155.4mm；安装口157mm。作者安装端位检查显示固定轨与木吊块接合，移动内轨与块横向约0.25mm净隙，关闭与78mm展开端位均不相交。12mm拉环净空与94.4mm展开前方包络列入接入约束。这不是全行程物理仿真结论。

## 接入边界与补图

1. TABLE/MAT共同比例仍为0.34/0.091；顶/底接触为0。不能通过各轴拉伸让桌垫去迁就旧布局，也不能把槽与纸牌一起拉宽。
2. **C源抽屉开口在桌前中央，原运行入口在左前。** 当前相机底裁切、玩家前景遮挡、真实拾取位置、0.4左右运行单位的桌/裙厚度要在两档Q3实际看；独立组合图没有证明这些运行关系可用。先不返修改源几何，按实际集成证据校准相机/布局。
3. SLOT的负Z槽底放入未处理的不透明垫下，不会自动产生压痕。运行必须将 `slot-pressure-mask.png` 绑定到局部垫材质/几何，并分别控制EMPTY/RESERVED/HISTORY/FOCUS。QA布片的真实0.3mm布尔压位不是生产游戏宿主，不能导入后宣称规则或全部槽效果已验证。
4. 三张槽状态补图应完整含全宽全长与四角、至少5%外边距，使用最终GLB或固定源并明确来源。原152文件及manifest冻结；新图放独立 `review-supplement` 目录并附自身manifest。总控已同意，只补证据，不返工源。

Q3、OS输入、性能、完整战斗与用户美术接受均未在本轮执行。三件通过允许限定接入，SLOT在补图后另给完整离线状态结论。
