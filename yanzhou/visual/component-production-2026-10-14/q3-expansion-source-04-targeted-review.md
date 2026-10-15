# 合并运行 source-04 定点复核

日期：2026-10-15（America/New_York）。复核者：设计 D / component_detail_design。

结论：此次 1920×1080 图示中的 caster 签压账目、抽屉底规则亮点、晶球奶白实心感已关闭；晶杖主桌方向可保留进入下一轮验证。源 Q1/Q2 不变。这里不作完整 Q3、双档运行、性能、光学折射或用户美术接受结论。

## 实际证据与判断

D 使用 view_image 实际查看下列三张完整图。证据目录为 `E:/Project/yanzhou-godot/evidence/development-batch-10/expansion-source-04/1920x1080/`。

| 证据 | 本次观察 | 结论 |
| --- | --- | --- |
| `01-tabletop.png`、`11-shield-use.png` | caster 小签落在施法账目右下，未覆盖精确量；生命与护盾签保持币面上方 | Q3-E03-01 在此次 1080 示例关闭；完整状态与 768 待测 |
| `05-resource-closeup.png` | 三格木底原规则亮点消失，隔板、底板和木纹仍清楚 | Q3-C02-01 在此近观关闭；不要求返修冻结源模型 |
| `01-tabletop.png`、`11-shield-use.png` | 晶球成为低对比青绿薄壳，铜托与内层可见，原奶白实心亮球感消除 | 主镜头方向可接受；透明排序、近观及双档仍待实际检查 |
| `01-tabletop.png`、`11-shield-use.png` | 晶杖主面偏灰蓝，边面青蓝和面差异可辨，奶白已降低 | 不再盲调首屏；下一轮 caster 近观核六面、夹爪与内衬，不能由首屏直接推全材质通过 |

执行方 `physical-result.json` 记录共 39 个已执行结果，38 Pass、1 Fail；计划为 72 项。失败仍是双位揭示拍字宽，因此本轮没有完整运行通过。总控随后报告 ASCII `2/r12` 的两档窄项已 Pass；D 接受其表示“程序 2 / 揭示 r12”，完整解释仍由 hover 保留。该窄项由总控执行，D 本轮没有复跑；source-04 三图也不是 ASCII 修后图。此前建议的 `2·r12` 被真实 Noto CJK 字宽证据否定，以 `2/r12` 取代。

`renderCosts` 记录的是有色 alpha 壳近似：WAND-02 alpha 0.26、roughness 0.24、specular 0.16；DECOR-02 alpha 0.19、roughness 0.26、specular 0.14；DECOR-03 alpha 0.12、roughness 0.22、specular 0.12。它们均不声明光学透射或折射。这些材料值由执行方采集，D 读取核对；截图符合此次近似方向。捕获计数也不等于帧耗时或性能验收。

## 固定 SHA-256

| 文件 | SHA-256 |
| --- | --- |
| `01-tabletop.png` | `346a1d11f8883b7b39a16ecc08029e7427e4de57180567d70affbfbde2948182` |
| `05-resource-closeup.png` | `8aaf7f3f2e537ff9d5d477d2d32ea2a0685065def59b442a7f0d4ac955c71222` |
| `11-shield-use.png` | `5a4ed2bb3d38f2ecefdf73e8c3b5a4f752a95f1129538120d6594ee94b69ede4` |
| `physical-result.json` | `03c309cf83baee5dd727f64d8ea6ee3916d8abe6aabc1be5b736506a4f64108b` |

下一关使用新的完整双分辨率证据；保留 source-02/03 的失败与修订记录，不覆盖历史，也不改任何资产源或运行文件。
