# 文档全量整理与核心摘要化

状态：Accepted / Documentation；不改变CORE-001–036的玩法选择。日期：2026-09-23。

## 来源与授权

用户先要求结构导航、统一版本、系统分隔与规范，再要求纳入探索方向独立整理、索引与比较，最后明确“开始进行全量整理”。现行设计来源为RC1已采纳的[首版补齐提案](../idea-proposals/P-2026-09-14-complete-first-release-design.md)、[评估](../evaluations/E-2026-09-14-complete-first-release-design.md)与[CORE-032–036](D-2026-09-14-complete-first-release-design.md)。本次是已采纳内容组织与订正，不为新机制建立虚构资格。

## 拟替换及实际处理

core-concept.md替换为产品目标、不变量摘要和现行GDD导航；详细规则迁入current七系统、内容与参数，不再在核心重复维护。保留v0.6核心标识，设计基准RC1，doc.1只代表文档整理。旧核心全文在history并保留固定Git来源。

依据现行CORE-021纠正任意空格生成摘要；依据RC1范围去除首版提供副词的歧义；参数待定文字改指已采纳PG。DOC-002重复的BR12记录改为DOC-004并建立别名映射。

## 不新增的设计裁决

AUD-010继续Open；不选定新的过程排序，不改数值，不启动玩法测试，不采纳或合并探索候选。历史实验与原始素材资格保持。

## 同步与验收

同步decision-log的G002-DOC-005，当前入口、AGENTS、术语、效果索引及探索目录；检查来源、链接、53实体和134FX完整性、原始文件保留及已有脏文件未变。实际结果见docs/governance/organization-report.md。
