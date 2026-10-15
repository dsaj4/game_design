# source-05 新增近观定点复核

日期：2026-10-15（America/New_York）。复核者：设计 D。此轮实际使用 view_image 看 1920×1080 的 `component-06-complete-table.png`、`component-07-caster-future.png`、`component-08-hourglass-near.png`，并读取执行结果；不重复源 Q1/Q2。

**结论：晶杖近观有两项需修；其他本次画面不新增形体返修。暂不收完整 Q3。**

| 项目 | 实际观察 | 定点处理 |
| --- | --- | --- |
| Q3-B05-01 晶杖近观 | 07 晶头主面近黑，蓝色与六面差异不足；铜爪高亮明显，晶体反成黑色块 | 仅近观克隆补离轴中性光/独立光层，恢复灰蓝主面和青蓝窄边，同时保留暗衬。不要改冻结源、主桌或使用发光代替材质 |
| Q3-E05-01 双签间距 | 07 下方 `D3·剩余2` 与 `B·切换未来用途` 的纸框边缘相交 | 两框至少留 8–12px 净距；可将用途签向下移约 12px，保持原生框和 18px，再核 768 安全边界 |
| 整桌 | 06 的木沿/布边/窄槽、玩家与敌棋子、筹码、控制、三装饰形态均可识别；ASCII `2/r4` 已呈现 | 保留此方向，完整状态和双档仍待后续实跑 |
| 近时沙漏 | 08 实际为玩家近观，其中附带疲劳沙漏小物件；15拍下砂更多可见，文字明确下一次第16拍 | 可作此上下文的近时状态证据；不能称独立沙漏玻璃近观全部通过，不要求因此新建交互 |

`physical-result.json` 共 71 条结果，前 70 条 Pass，第71条 `components-hourglass-paid-from-live-fatigue-result` Fail。其错误信息明确 `beat=16; stage=observation`。总控已定位取证停在疲劳结清前，正在仅修测试为等待真实 Fatigue16 事件；D没有复跑此修正，也不将本失败写成源模型或砂位逻辑缺陷。

证据根：`E:/Project/yanzhou-godot/evidence/development-batch-10/expansion-source-05/1920x1080/`。

| 文件 | SHA-256 |
| --- | --- |
| `component-06-complete-table.png` | `085acf4567cb1ecc1a2ffade0b016e74d60d58019388ae95ca244da220ce43ef` |
| `component-07-caster-future.png` | `e857de3aa18e5ab55fede6a50442e9c7265253a60212135c701e76834b658d5b` |
| `component-08-hourglass-near.png` | `60ad56f8d4d394e8231adf775cbd91816b24595d625daded7cb1fdc490d45bd6` |
| `physical-result.json` | `ac41e2e3da72812d163357f2a4bc4d544ce84c291b40b818302ca9a33297afb1` |

结论已发总控，等待局部修订和新的完整双档证据。这里不声称折射、性能、OS输入或用户美术接受。
