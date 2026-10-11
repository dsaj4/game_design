# 言咒测试交接

Project ID：game-002。文档角色：EvidenceIndex。2026-10-11。当前输入GDD 2.2 / CORE-059 / EX-001；[阶段计划](production-plan.md)定义P0引擎评估、P1规则及后续分阶段验收。117项规则预期仍NotRun，本轮仅静态资料／资产检查；早期局部试点及下列报告沿原版本。

| 批次 | 输入与结果 | 范围 |
| --- | --- | --- |
| CORE-059正式开发批次 | Planned / NotRun；TL-11总序及EX-001短情境已明确；完整内容／疲劳仍待补 | [新版预期](../design/validation.md)与[分阶段范围](production-plan.md)；不以范围外缺项否定可执行的局部检查 |
| DEMO05-001 | cf7b98d；16项局部检查；seed42在C5L第76刻失败 | [实现验证](E:/Project/yanzhou-dark-demo/docs/verification.md)；旧版本Implementation Slice Checked，不能改称TL-1 |
| TH-003/r1 | 29,404场限定实验 | [原报告](reports/TH-2026-09-13-003-r1-run-01.md)；旧临时规则，非完整RC1／TL-1 |
| CAL-001/r1–r3 | 975,659场合计，r3 CalibratedCandidate | [r3报告](reports/CAL-2026-09-13-001-r3-run-01.md)；不代表TL-1参数或玩法通过 |
| RC1正式计划 | 720单场、36边界、20整局及U01–08未完成 | [原验收输入](https://github.com/dsaj4/game_design/blob/d6e54af395518401fb4d8466b2302a1271da557a/yanzhou/design/validation.md)，不重贴新版本 |

新批次先限定所验范围，闭合该范围必要的[设计问题](../governance/questions.md)，固定设计／代码提交与对应输入；未涉及的材料、维护、携带等标范围外，不为短情境强行补全整局。完整战斗必须补疲劳等必要参数，实际玩法实验另按具体任务执行。效果只按[目录](../effects/catalog.md)当前适用范围选择；FX-135原直接资源路径已替代、FX-137具体候选已退役，不能整组当作就绪输入。过去输入错误、失败、未到达和NotRun保持原记录。
