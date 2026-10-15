# 首批四样件 Q3 限定收口 · source-04

2026-10-15（America/New_York）· D / component_detail_design。

**首批 TXT-01、CARD-01、WAND-01、PAWN-01 的本轮限定 Q3 通过。** TXT/CARD/PAWN 沿 `q3-source-02-review.md` 的具体范围；WAND 的近观照明问题在 source-04 收口。这里没有把四样件通过扩成 19 个组件完成、发布包通过或用户整体美术接受。

## WAND-01 局部复核

D 实际 `view_image` 查看 source-03 与 source-04 的 1920×1080、1366×768 `06-guard-closeup.png`，共四张。source-03 已消除 source-02 的整环黄白过曝，但环面接近背景黑，768 档尤其难辨，故未通过。source-04 由总控仅调整 guard 近观克隆的独立离轴光，未修改冻结源材质或主桌灯光。

source-04 两档环面恢复为铜金中间调，正面与暗边、浅刻槽、内环开口有区分；夹片铆钉及皮握柄仍可辨。高光仍较集中，但不再整面黄白或近黑，静止铜面不再与来源亮整杖反馈混同。近观的转正斜置、物件包围计时圈和投入/产物空间保持。此处可以通过，不再提出无新增证据的换材质或装饰返工。

## 运行身份与回归

source-04 `execution-manifest.json` 固定 Debug 程序集 SHA `6a1259b1e5e3e403944ff738aae93eb30aa0ec3d15cd12700849028273578412`；程序集写入 `2026-10-15T04:42:48.8629024Z`，运行记录 `2026-10-15T04:42:49.1625221Z`。源码快照在同一 manifest；仓库基点 `979b1e6a16f9a9951634361ccb8299b87ba5860c` 不等于所有未提交改动已入提交。

D 解析两份结果 JSON，均为 61/61 Pass；runs 记录两档 exit 0，stderr 均 0 字节。测试边界仍为 Viewport 模拟鼠标/键盘、手动动效时点和直接焦点处理器，不是 OS 输入/焦点、性能或完整战斗验收。未自行启动这一轮 Godot，只核对总控执行证据。

另逐文件 SHA 核对两档 `01-tabletop`、`02-player-closeup`、`07-completion-source`、`08-completion-appear`、`10-card-closeup`、`11-shield-use` 共 12 张 PNG，**全部与 D 已实际查看并记录的 source-02 对应图字节一致**。因此沿用三件已通过结果以及主桌源亮/显牌/目标反馈结论；没有把未再打开的相同文件冒称重新目视。指纹见 `q3-source-04-png-regression.json`。

## 分类准入

| 组件 | 限定 Q3 结果 | 保留边界 |
| --- | --- | --- |
| TXT-01 | Pass | 本次两档常驻读数与实拍字段；不是任意长数值、全屏幕或 TXT-02/03 家族验收 |
| CARD-01 | Pass | 薄纸主卡的护盾代表图、近观及已测显牌/Use；其他卡面需另验 |
| WAND-01 | Pass | 主桌形体/来源亮、近观真实物件/计时圈/当前投入与产物空间及静止铜面；WAND-02 不能继承本件验收 |
| PAWN-01 | Pass | 主桌与近观同形、罩腔/宽褶/局部目标反馈；PAWN-02 另验 |

四件已具备源 Q1/Q2 与限定运行 Q3 的分别记录，可以作为总控后续类别扩量/拼装的输入。A/C 扩量件仍各自停留在实际制作或待复核阶段，不自动通过。源件固定 manifest `e81b4175ed0d9b0f4ba7a4656ae6a14a87a5e6a5a2832848ed1e765feb3cbd3c` 及此前 Q1/Q2 复核 manifest 均未修改。
