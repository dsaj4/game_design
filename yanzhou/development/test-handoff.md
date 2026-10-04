# 言咒测试交接

Project ID：game-002。文档角色：EvidenceIndex。2026-10-04。当前设计输入为TL-1 + INS-1，尚无对应完整实现或运行证据；早期TL-1局部试点已退役，见开发索引。本轮仅静态文档检查。

| 批次 | 输入与结果 | 范围 |
| --- | --- | --- |
| TL-1 + INS-1未来批次 | Draft / NotRun；卡池、参数与总时序未冻结 | [新版预期](../design/validation.md)，不是Ready；不启动实验 |
| DEMO05-001 | cf7b98d；16项局部检查；seed42在C5L第76刻失败 | [实现验证](E:/Project/yanzhou-dark-demo/docs/verification.md)；旧版本Implementation Slice Checked，不能改称TL-1 |
| TH-003/r1 | 29,404场限定实验 | [原报告](reports/TH-2026-09-13-003-r1-run-01.md)；旧临时规则，非完整RC1／TL-1 |
| CAL-001/r1–r3 | 975,659场合计，r3 CalibratedCandidate | [r3报告](reports/CAL-2026-09-13-001-r3-run-01.md)；不代表TL-1参数或玩法通过 |
| RC1正式计划 | 720单场、36边界、20整局及U01–08未完成 | [原验收输入](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/validation.md)，不重贴新版本 |

新批次须先闭合[设计问题](../governance/questions.md)，固定设计／代码提交、卡池、法器、材料、维护、队列、敌牌程序、携带、疲劳与参数，再获得实际实验任务授权。效果只按[目录](../effects/catalog.md)当前适用范围选择；FX-135原直接资源路径已替代、FX-137具体候选已退役，不能整组当作就绪输入。过去输入错误、失败、未到达和NotRun保持原记录。
