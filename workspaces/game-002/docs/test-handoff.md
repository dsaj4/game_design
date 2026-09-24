# 言咒测试交接

文档角色：EvidenceIndex。更新：2026-09-23。本次只做文档静态验收，不运行玩法模拟、平衡或真人研究。

| 批次 | 输入与结果 | 证据范围 |
| --- | --- | --- |
| DEMO05-001 | cf7b98d；16项局部检查；seed42在C5L第76刻失败 | [实现验证](E:/Project/yanzhou-dark-demo/docs/verification.md)；Implementation Slice Checked |
| TH-003/r1 | 29,404场限定实验 | [原报告](test-reports/TH-2026-09-13-003-r1-run-01.md)；旧临时规则，非RC1完整战场 |
| CAL-001/r1–r3 | 975,659场合计，r3 CalibratedCandidate | [r3报告](test-reports/CAL-2026-09-13-001-r3-run-01.md)；不代表参数已采纳或RC1平衡通过 |
| RC1正式批次 | 尚未冻结新的完整执行批次 | [验证规格](../game-design-workflow/gdd/current/validation.md)：720单场、36边界、20整局及U01–08仍未完成 |

后续执行前记录设计提交／文件哈希、代码提交、批次修订、完整输入和范围。先解决会使预期不唯一的AUD-010，再冻结受其影响的用例。原输入错误、失败、未到达和NotRun完整保留。新测试需要实际任务授权；本次整理不是启动令。

[历次完整交接和输入要求](history/pre-organization/docs/test-handoff.md)。
