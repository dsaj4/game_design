# 晶杖近观局部修订实看

2026-10-15，设计 D 实际使用 view_image 查看 `E:/Project/yanzhou-godot/evidence/development-batch-10/expansion-component-01/1920x1080/failure.png`。

限定 1080 近观方向可接受，建议保留：晶头由近黑恢复青蓝，主面、左尖端和下缘有可辨明暗差，铜爪与暗衬分离；计时签与用途签上下对齐且明显留空，不再相交，文字未裁切。因此 Q3-B05-01 与 Q3-E05-01 的本档视觉问题已修，等待 1366 与真实纸框坐标取证再收双档结论。alpha 近似仍不称真实折射。

本图是失败时捕获图，不是整轮通过证据。总控报告失败来自测试查找了 PanelContainer，而此处实际宿主为 Label3D+Quad；总控正在改为实际 Label3D.paper_rect 取证。D 本次仅目视图像，没有执行该断言或复跑测试。源模型与其他运行状态不在此轮重审范围。

图像 SHA-256：`a6c412c359c9cd7f4b53f01229fbec1d04bbfec8a8879e78b6735f738344f3f3`。

## component-02 的 1080 局部闭合补记

同日 D 实际使用 view_image 查看 `E:/Project/yanzhou-godot/evidence/development-batch-10/expansion-component-02/1920x1080/` 的 component07/08/09/10，并读取 `physical-result.json`。执行方 11 条结果全部 Pass；D 没有重跑引擎。

- **晶杖近观**：07 与上次已看的修订图 SHA 相同，本次也再次目视。青蓝切面、铜爪和暗衬保持分离。真实 worldCaptions 记录两框分别为 `(559.65344,786.5241),(216,60)` 和 `(559.65344,856.5241),(216,60)`，垂直净距 **10px**；字号18、投影字高约18.012px，纸框原生尺寸保持。Q3-B05-01 / Q3-E05-01 在本档闭合。
- **15拍近时**：08 为玩家近观附属沙漏，上腔少砂、下腔较多可见，正文明确下一次疲劳第16拍；仍不将小物件画面称为独立玻璃近观验收。
- **16拍结清**：09 主桌上腔无黄色砂团、下砂可见，疲劳签更新为“20拍·双方10”，阶段为16拍完工。执行方 `components-hourglass-paid-from-live-fatigue-result` Pass，解决此前停在观察阶段的取证问题。
- **终局**：10 的1/2文字页、分页/关闭及下方两组操作区可读，无叠框或出屏；关闭与分页目标实际44×44。执行方 `components-hourglass-terminal-holds-last-presentation` Pass，画面保留末态沙漏。本次没操作第二页，不据单帧宣称动态冻结或全内容交互已由D执行。

此四图不新增外观返修。总控另报1366在第5项发现一行TXT02残留两行容器高度，由E修复；本补记没有把1080通过扩为双档或完整回归通过。玻璃仍按alpha近似范围，不声称真实折射或性能验收。

| component-02 文件 | SHA-256 |
| --- | --- |
| `component-07-caster-future.png` | `a6c412c359c9cd7f4b53f01229fbec1d04bbfec8a8879e78b6735f738344f3f3` |
| `component-08-hourglass-near.png` | `60ad56f8d4d394e8231adf775cbd91816b24595d625daded7cb1fdc490d45bd6` |
| `component-09-hourglass-paid.png` | `0b3db055ebd85dd0d4c46a8e315ef62718c4c28d80914f4250ff005019740bc3` |
| `component-10-terminal.png` | `8bfc1e4f10cf91afd4de19143700043ba2dd8d057cd6be786c97f7a4df68f7fa` |
| `physical-result.json` | `51016df58f0b3c78ca8a7410c8ac5c17bfb2885f5bee109ae09fb645ea503c17` |

## component-03 的 1366 局部闭合补记

D实际看1366的component04/05/06/07/08/09/10七图。单行hover恢复原生196×60，protectedOverlap=0；详情原生360×392、关闭/分页44×44且在屏内。caster两签为 `(377.10916,559.306),(196,60)` 与 `(377.1092,629.3061),(196,60)`，净距10.0001px，投影字高约18.012px。青蓝切面及夹爪保持，近时/结清/终局状态在此档均可读。这些局部问题可关闭。

两档结果JSON各11/11 Pass（D读取，非D重跑）；1366 stderr为空，1080 stderr实际2339字节，内容为NotifyMouseEntered重复通知WARNING，不能写成两档stderr空。退出0由总控报告。完整72项回归另以source06检查，不由此11项代替。

1366结果SHA：`a45cc79a3e76f8098069bf4e5b23a3873788a48c445819765c33ef21fd4a9129`；1080结果SHA：`ba510e2bbc88311e8b3e2a8e981ec638d703931c0eced0a159853be0af28b7ef`。本次主桌/玻璃继续按有色alpha近似评价，不声称光学折射或性能达标。
