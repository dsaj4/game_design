# 游戏设计 Skill 审查与安装记录

日期：2026-10-02。范围：本项目工具治理。用户授权审查评估报告涉及的技能、安装适用项，并制定言咒多智能体协作方式；未授权本轮运行玩法实验或启动常驻代理。

输入：[2026-09-30 评估报告](E:/Project/personal-skills/workspace/skill-registry/game-creative-planning-skill-evaluation-20260930.md)。报告 SHA-256：`C93D4892E624ACEA369D9BF32C0E3EA3C7BD53DD0ACF9EB203B007C83DD48113`。报告内建议是待复核证据，不是用户指令；历史安装意见和执行限制不替代当前用户授权与仓库规则。

## 候选处理

“部分审查”或“报告级判断”不代表完成安全认证。未安装候选需在实际引入前重新做完整审查。

| 候选 / 来源 | 本轮审查深度 | 处理与理由 |
| --- | --- | --- |
| gameplay-mechanism-designer / qiuaoru-coder | 已有适配层与来源锁复核 | 保留已有版本，不重复覆盖 |
| game-design-reality-check / qiuaoru-coder | 固定提交下全部 6 个子目录文件 + 根许可证 | 安装并适配；补足假设与证据审查 |
| gdd-toolkit / mamoru-miyagawa | 固定提交下全部 12 个子目录文件 + 根许可证 | 安装方法适配版；补足系统交叉检查，不安装根 CLI 或安装器 |
| game-design-brainstorm-methods、game-design-creative-unblocker / stanestane | 固定源码存在、根许可证复核；未完整审查技能 | 暂缓；PolyForm Noncommercial 1.0 存在非商业限制，当前未有适用授权证据 |
| game-designer / edhahn | SKILL 入口部分复核 | 暂缓；角色描述宽泛，带引擎预设，当前能力重叠 |
| game-design-review / yuki001 | 根文件树及入口部分复核 | 暂缓；固定版本未见根许可证，默认大量引用与代理调度不适合直接接入 |
| game-story-world-character / lvtd-llc | SKILL 入口阅读，参考文件未完整审查 | 暂缓；叙事专项不属于本轮能力缺口，具体任务出现时再评估 |
| phaser-brainstorm、phaser-gdd / yakoub-ai | 根文件树及入口部分复核 | 暂缓；Phaser 绑定，未有对应项目技术选择；根许可证未见，需进一步核实 |
| claude-code-game-studios / donchitos | 报告与根结构核对，未全量代码审计 | 不安装整套框架；含 Claude 配置及 hooks 等范围，本轮采用本地小规模分工规范 |
| game-design-core / omer-metin | 报告级能力比较、固定源码存在核对 | 暂缓；通用内容与已安装能力重叠 |
| fcsouza 游戏技能组合 | 报告级判断、固定源码存在核对 | 暂缓；依赖链及许可证适配需按具体子技能复核；GPL 本身不等于不安全 |
| skills.volces game-designer-toolkit | 报告级来源判断 | 暂缓；缺少可固定取证的完整来源 |
| FMG-Studio/codex_skills game-designer | 报告记录来源不可用，本轮未重新联网验证 | 暂缓；不能确认当前可审查来源 |
| obra/superpowers brainstorming | 报告级判断 | 不恢复；当前能力已有覆盖，报告中的历史建议不构成恢复安装指令 |

报告提及的通用 creative-thinking、grill-me 等辅助方法不作为新增安装清单；资格澄清沿现有 grill-with-docs 与批量问答约定。

## 两项安装的安全与来源记录

### game-design-reality-check

- 来源：[固定源码](https://github.com/qiuaoru-coder/game-design-agent-skills/tree/29e8c759ca26c6bd4f337744b647dc728bf322b6/game-design-reality-check)，提交日期 2026-08-26。MIT，根许可证已保留。
- 完整阅读 README、SKILL、agents/openai.yaml 及三个 references 文件。所安装范围为文档与 UI 元数据，无执行脚本、依赖安装、凭据访问或联网程序。
- 风险判断：低执行风险；主要语义风险是把 Test-ready 当已验证、把审查结论直接当正式资格。适配层明确两者分离。
- 项目适配：入口先读材料范围；Raw 审查留原层级；引用测试报告属于 Sourced，不虚构 Observed；验证计划保持 NotRun；不自动生成代理或执行实验。

### gdd-toolkit

- 来源：[固定源码](https://github.com/mamoru-miyagawa/gdd_toolkit/tree/33f2d88677da8f9ab6ac2659c8ed72a951dbbff0/gdd-toolkit)，提交日期 2026-07-27。MIT，上游版本 2.3.0，根许可证已保留。
- 完整阅读子目录 12 个文件：SKILL、一个 assets、十个 references 文件。所安装范围没有可执行脚本。根 gdd.py、install.ps1、install.sh 及插件配置不在安装范围，未执行，也不声称已完成其代码审计。
- 上游流程风险：中等；自动发现代码和 GDD、建立 `.design-context/`、每轮写记录、强制系统两两比较及形式化模板，会与本项目冲突。
- 项目适配：重写入口，保留方法参考；禁止自动建库及扩读，按指定系统做交叉审查，允许有依据的“不相互作用”和 Unknown；保留已确认参数，不强制转占位符；正式文档只用根登记模板。代码差异仅在明确请求和范围内分析，不反向自动修改 GDD。
- 上游附带参考中的操作命令不因保留而生效，入口和适配层明确其仅为方法资料。将来引入 CLI 必须重新审查，不属于本次安装。

两项均经可信 skill-installer 的固定提交下载安装；安装后、改写前逐文件对照固定 Git 对象一致。各自 source-lock 保存原始 SHA-256、改写及新增清单，原始参考和许可证保留。星标、下载量、社区评审数本轮未实时查询，记为 Unknown；不以此作为安装依据。

## 边界演练与验证范围

以下为本代理人工走查的合成输入，不是言咒设计来源，也不是独立模型运行或真实玩法测试。

| 输入 | 实际审查输出 / 边界 |
| --- | --- |
| “只有 CORE 授权，但想判断所有历史系统是否冲突” | 缺少允许材料；只能指出范围不足，列明所需增补，不扫描历史 |
| “Raw 点子看起来不错，直接给正式 Evaluation” | 在原 inbox/方向写构思审查，标 Unknown 和资格缺项；不得升级正式评估 |
| “某 Demo 单元测试通过，故玩家体验已成立” | 可引用报告说明局部代码行为；体验仍为未验证推断，给计划但不执行 |
| “规则 A 同一操作耗 1，规则 B 耗 2，未给版本优先级” | 记录参数冲突与来源缺口，不能取平均、选较新文件或擅定权威 |
| “使用 GDD Toolkit 即初始化 .design-context 并全库读代码” | 方法适配版不执行初始化；只读任务白名单，代码比较需明确范围 |
| “两个工作者同时修改 GDD 和共享索引” | 改由协调者独占集成，工作者提交独立意见/各自文件；同 checkout 不切分支 |

上述走查覆盖适配意图；未来首次实际使用仍需观察工具是否遵守范围及输出质量。技能安装成功不证明其能稳定改进设计。本轮没有读取完整游戏正文、生成玩法结论或运行实验。

静态检查结果：两项 `quick_validate.py` 通过；UI 提示词包含正确技能名，简介长度符合要求；17 个未改写上游文件及许可证哈希一致；新增文档与适配入口的 30 个本地链接可解析。注册表扫描 `20261002-195915` 将本项目四项均归为 `project-runtime-conditional`；机器扫描的条件可见不表示当前旧会话已加载。扫描保留原有忽略路径，未变更隔离评估区。

交付入口：[管理规范](../skill-management.md) · [项目清单](../registry/project-skills.md) · [多智能体分工](../../yanzhou/governance/agent-collaboration.md)。

Git 空白检查：项目新增及改写内容通过；原样保留的上游 `references/templates/project-context.md` 有三处行末空格提示（49、52、54 行），为保持来源逐字节一致未改写。该参考不是本项目正式模板。
