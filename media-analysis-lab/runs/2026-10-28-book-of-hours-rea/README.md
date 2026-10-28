# BOOK OF HOURS：REA深度分析

2026-10-28 · BOH-REA-2026-10-28-v02；v01静态取证保留在提交`feee23195fe277afaaf9aef5e3846a7a69439efe`。

**[阅读分析报告](drafts/2026-10-28-book-of-hours-rea-dossier.md)**

按[DIR-042指定清单](../../../yanzhou/exploration/DIR-042-herbal-engraving-style/book-of-hours-analysis-checklist-2026-10-28.md)分析本机2024.12.m.3。真实REA静态Evidence与资源核对已完成；v02新增自然开局的查看、错误预告、撤回、完整操作及领取去向，9张玩法截图已直接审计。耀素制作、大收藏与双任务仍未覆盖，不能报告全部实机问题已经闭合。

材料、提纲、视觉审计与检查记录保留在本包；图像和完整原始取证保本机。REA入口为用户确认的 `E:/Game/Demoncards/rea/scripts/rea.mjs`，6.4.0。受控造景未通过保存，没有用它补造正常玩法结果；原配置和自然默认进度已恢复并校验，详见[失败与恢复](evidence/controlled-attempt-r02.md)。

## AS-SH-003 Book of Hours 本机分析参考包

| 字段 | 内容 |
| --- | --- |
| 归属 / 维护 | shared-reference / media-analysis-lab；本页唯一包入口 |
| 用途 / 类型 | 符号语义、对象多种表示、槽位与制作表达；参考包，不是可玩Demo或合格设计素材 |
| 主入口 | 上方报告；原件 `E:/Game/BOOK OF HOURS v2024.12.m.3/`；本机取证 `E:/Game/BOOK OF HOURS-analysis/2026-10-28/` |
| 固定版本 | v02继承v01的[发布文件身份](source-manifest.json)、[REA记录](rea-evidence-index.json)和[静态导出](local-output-manifest.json)，新增[实机与恢复清单](runtime-r02-manifest.json) |
| 来源 | 用户指定第三方游戏；Weather Factory；已发行内容、程序集和纹理；分析文字与编排由本轮生成 |
| 生命周期 / 访问 | Catalogued / PresentLocal；2026-10-28核静态样本及自然开局操作链；受控路线FailedSetup，耀素/高收藏/双任务未完成 |
| 规格 | 37张采样RGBA PNG、4张资源分析图、9张已审计玩法截图；本机另保留完整逐步截图/动作、自然存档和失败证据；具体尺寸/哈希见对应清单 |
| 复用条件 | 用户授权本机研究；第三方原图/文本/程序集的公开再分发及改作条件Unknown，不据分析授权复制到游戏或上传原始缓存 |
| 关联 | uses: None；derived-from: None；使用者game-002-optimization / DIR-042，限视觉与信息表达候选参照，未导入游戏资产或采纳规则 |

## 下一步

后续从[自然实机记录](evidence/runtime-observations-r02.md)和报告末尾未覆盖项接续；工作台/高收藏/双任务应使用正常可保存的相应进度，不复用失败副本。原静态、受阻与失败证据保留，不新建平行资料系统。
