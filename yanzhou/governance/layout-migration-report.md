# yanzhou目录迁移报告

目录修订：layout.1 / 2026-09-23。管理状态：Accepted / Documentation，G002-DOC-006。玩法基准仍为GDD 1.0 RC1 / doc.1；AUD-010仍Open，未新增玩法采纳或测试结果。

## 实际交付

在仓库根建立[yanzhou/](../README.md)，正式设计、来源链、FX追踪、探索、开发证据、视觉、治理和历史按[目录规范](directory-layout.md)分开。主Project ID仍为game-002；优化Project ID仍为game-002-optimization，物理路径变为exploration/optimization/，资格及回写权限保持。

新目录共728份文件；从原目录迁入718份正文/数据/资产，另将23个重复导航入口归并到对应正文。全部741条旧新路径关系、原始SHA及处理方式见[path-map.json](path-map.json)，可读文件列表见[file-index.md](file-index.md)。迁移起点提交：`97dd791b204be026fc7834985df3cd72495d90c1`。

旧Markdown改为兼容导航并保留原章节锚点。冻结背景包、机器来源记录、媒体保留原地址以兼容历史取证和外部链接；新目录持有相应副本。两份已有未提交素材保留旧正文，见下表。没有递归删除旧目录，也没有把独立肉鸽、旧游戏、外部代码仓库或未跟踪视觉产物打包进来。

## 未提交素材处理

- `workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-05-grammar-and-semantic-compatibility.md` → `yanzhou/sources/materials/M-2026-09-05-grammar-and-semantic-compatibility.md`：旧路径保留未提交字节，新路径从迁移起点提交复制；本轮不提交原修改。
- `workspaces/game-002/game-design-workflow/idea-materials/M-2026-09-06-flexible-sentences-and-subject-roles.md` → `yanzhou/sources/materials/M-2026-09-06-flexible-sentences-and-subject-roles.md`：旧路径保留未提交字节，新路径从迁移起点提交复制；本轮不提交原修改。

这两份新目录来源标注committed-source-pending-edit-excluded；后续由原修改任务对照新目录决定同步，不将工作树修改伪装成已采纳来源。

## 核验结果

| 检查 | 结果 |
| --- | --- |
| 当前导航与迁移链接 | 20337处本地链接；新增错误0 |
| 正式设计完整性 | GDD 0–18章、7系统、53实体/55条目锚点均保留 |
| 效果与探索 | 134个FX入口、27个DIR条目；方向来源路径和新字节SHA已更新，原SHA单独保留 |
| 冻结背景 | 9份包文件逐字节保持；manifest中的6份Git blob源文件SHA逐项一致 |
| 已有媒体 | 8份图像逐字节一致 |
| 原工作树保护 | 942项已有修改/删除的原字节或缺失状态全部保持 |
| 文件格式 | UTF-8读取、Markdown围栏与章节/ID检查通过；Git暂存区空白检查通过；冻结包暂存字节核对通过 |
| 实验 | 本轮仅文件与引用静态核验，无新增玩法模拟或真人测试 |

## 历史与配置例外

旧参考图在本轮前已被删除，共3处历史/原始来源引用仍保留，未替用户恢复。冻结背景的摘录仅含6份来源，原文包含未打包的外链路径；344处不可在包内解析的历史引用保持原字节，按原固定提交理解，不算现行导航。其follow_links=false边界未改变。

原背景生成profile v2仍对应旧提交与活动包。v3仅是新路径配置草稿：4项已映射、2项旧素材当前不存在，明确generation_ready=false。本轮没有替换它们、生成或激活新包；未来明确生成任务须先审查来源并补齐配置。

历史机器清单/来源manifest的路径、提交和SHA原样保留，不能按本次新路径重解释旧取证结果。共享模板、知识与Git协作仍依赖仓库根；本目录是项目目录，不宣称含全部依赖的独立仓库。

## 维护入口

新工作从[项目README](../README.md)及[AGENTS](../AGENTS.md)开始。后续目录变更更新映射、路由与注册；规则变更依旧走Draft Change。当前新分支为codex/2026-09-23-yanzhou-project-layout，按用户要求提交推送本目录及必要的路由兼容改动。
