# 世界观技能组完整安装

2026-11-01 · 工具治理。用户明确要求全量安装`skills/creative/fiction/worldbuilding/`下各技能，用于重新开展言咒世界观写作，特别关注语言演变、文字设定，以及不同叙述视角和物品描述中的名人与世界知识。

## 来源与安装范围

来源：[jwynia/agent-skills世界观目录](https://github.com/jwynia/agent-skills/tree/e02ec7e226a6e4f8419fd3b88a1d8e472d421b32/skills/creative/fiction/worldbuilding)，固定提交`e02ec7e226a6e4f8419fd3b88a1d8e472d421b32`。目录完整包含11项技能、24个原始文件，本轮全部安装到本项目`.codex/skills/`，包括7个TypeScript脚本、5个JSON数据文件和1个模板；没有安装相邻目录的技能、Deno、运行依赖、插件或hooks。

| 技能 | 写作用途 |
| --- | --- |
| belief-systems | 信仰、仪式、学说与内部异议 |
| conlang | 语言声音、词形、命名与一致性 |
| economic-systems | 资源、劳动、交换与社会关系 |
| governance-systems | 势力、权力来源及不同历史解释 |
| language-evolution | 古今语言、借词、方言、失传、误读与书写演变 |
| metabolic-cultures | 闭环生存条件下的文化；保留方法，不预设言咒存在该环境 |
| oblique-worldbuilding | 书信、碑铭、物品描述、名人引述等有限视角 |
| settlement-design | 聚落功能、空间关系与历史层次 |
| systemic-worldbuilding | 从明确虚构前提推演跨领域后果 |
| world-fates | 长期命运、势力消长的候选推演；不默认导入随机剧情机制 |
| worldbuilding | 世界、制度、经济与文化的一致性诊断 |

## 审查与适配

使用system skill-installer固定提交下载到运行时目录外审查，再安装。手工沿已退役skill-vetter的存档协议审阅全部24个文件；该旧技能没有重装，也不声称它当前可调用。每个源文件按Git blob身份与SHA-256核对，原始入口另保留在各技能`references/upstream-skill.md`，source-lock记录上游文件、改写及新增文件。

**许可核查：**11个原始SKILL.md均明确声明MIT及作者jwynia；该提交没有独立根LICENSE／COPYING文件，README也未提供完整许可证正文。本次保留原始逐项声明，并用UPSTREAM-LICENSE.md如实记录其来源，不伪造上游许可证或版权年份。项目清单不将其描述为“已保留上游根LICENSE”。

**静态执行范围：**未发现凭据读取、外传请求、混淆执行、子进程或系统配置修改。conlang的两个脚本、world-fates的fate-choice和propose-shift引用`deno.land/std@0.208.0/path/mod.ts`，首次运行可能取得远程依赖；未审查或下载该依赖。propose-shift可向调用方指定的`--output`写文件，未限制路径或防止覆盖，其余脚本主要读本地数据／输入并输出文本。故附带脚本按中等文件操作／依赖范围保留，安装不等于执行许可或运行验证。

**上游功能限制：**world-fates原文宣传的`--bible`读取／自动更新合同没有在实际CLI中完整实现；fate-pressure脚本的状态阈值与SKILL／数据表不一致，随机推演不是事实依据。conlang数据自称跨语言频率简化输入，未经本轮独立研究核实；参数、词形与语言真实性不作运行保证。原件不静默修复，后续确需脚本时先闭合实际任务边界。

各技能入口加入相同项目适配：READ-1与用户材料范围优先；世界正文归worldbuilding，物件文案归内容库；不自动建立context配置、world-bible或平行模板树；不自动派生代理、执行实验、增加玩法或更新现行规则。上游方法完整保留，仅对冲突的默认流程明确项目优先关系。

worldbuilding入口的原`compatibility`字段移至`metadata.upstream_compatibility`，以满足本机结构校验器；值和原始入口完整保留，source-lock登记此改写。

## 检查及使用

检查完整子目录、源哈希、UTF-8／JSON、技能入口格式、适配链接与来源锁；按人工边界演练核对“写语言不自动取得铭文权限”“叙述者信念不等于真相”“随机命运不自动回写历史”“既有目录不再询问落点”。未执行上游脚本，未进行独立模型创作评估或玩家测试。新装技能从下一轮会话开始使用，列表未刷新时重开会话。

项目清单及扫描结果见[项目技能入口](../registry/project-skills.md)，机器注册记录沿全局skill-change-log。重新设计任务从[世界观入口](../../yanzhou/worldbuilding/README.md)接手；上一轮具体设计已撤回，不作为此次技能演练的素材。

最终检查：11项结构校验通过，24个上游文件可按原哈希恢复，适配入口／新增文件哈希、JSON及44个技能链接通过；既有世界确认未变，137个相关文档链接通过。注册复扫`20261101-035916`保留原扫描根和排除项，11个新增入口均为project-runtime-conditional，运行时可见重名0；机器扫描不宣称旧会话已加载新技能。
