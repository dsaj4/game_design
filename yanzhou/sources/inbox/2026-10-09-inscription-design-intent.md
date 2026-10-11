# 铭文及辅槽：设计初衷与探索体验

Project ID：game-002。日期：2026-10-09（America/New_York）。文档角色：SourceRecord。初始状态 Raw Idea / Unqualified；用户直接说明及 INS-I1—5 答复已完成局部资格，进入 [合格素材](../materials/M-2026-10-09-inscription-design-intent.md)。新增设计意图与候选机制未采纳为 CurrentSpec，体验 Hypothesis / NotRun。

## 原始想法

以下保留本会话用户原话：

> 系统职责：应该承担“配方核心“、“探索组合”、“调整搭配”的职责。“配方核心“：暗句含义是决定配方的重要要素，概括了配方所做的行动，在设计上也和相关行动卡效果密切相关，是玩家认识理解配方的核心要素。“探索组合”：暗句使每个配方遵守一定规律，但又不完全公开，玩家因此需要探索尝试可行的铭文组合以构成有效配方；“调整搭配”：共享相同铭文的配方存在共性，是玩家思考搭配联动的重要要素之一，一个核心铭文对应的配方可能成为一个流派的核心。同时玩家如果要小幅度调整变化自身的能力，修改铭文最为直接。我的设计初衷：模拟炼金、施法中的炼金配方或法术秘籍，铭文系统的暗句构成就像是破解配方和秘籍的语言，铭文像是法术的真正含义，探索组合体验像是学习测试不同的炼金或魔法组合。我的理想效果：1.铭文需要简单清晰、有神秘感，最好符号化，让其可以使玩家直观理解作用；2.辅槽铭文主要带来有侧重的数值提升，不动由主铭文构成的逻辑，玩家不断取舍主铭文形成组合搭配的突破，不断（升级）换副铭文提升效果的量值

## 触发来源与任务边界

来自“阅读言咒主系统文档”会话的用户授权交接，要求在规则之上解释系统为何存在、不同选择与希望获得的体验；本会话随后收到上述直接说明和五项答复。交接文件为 `C:/Users/Administrator/AppData/Local/Temp/yanzhou-inscription-design-handoff-2026-10-09-54ad759.md`，SHA-256：`35f1f1f61eeebfa9611433c8c83079465dffc1b6736dea7f19f37426d82145b0`。交接仅为导航，不作玩法来源；未启动其他 agent 或跨会话发消息。

用户初衷是破解配方／秘籍的语言、学习魔法组合。先前文档中的“有限兼容降低理解负担”只覆盖理解的一面，不能继续作为全部目的；公开完整候选清单的默认想象也不能替代本轮明确的组合发现目标。

本轮只处理通用职责、选择、学习负担与体验。具体流派、铭文池、配方、符号资产、数值、取得机制及玩法测试留后续。现行 rules、其他系统、共享索引与治理记录只读；本人只写本页、对应 M 及铭文／辅槽的 design、experience 四页。

## 可能带来的玩家体验

用户希望玩家能由少量清楚的铭文含义理解法术，从未知组合中发现配方，把已学到的共性用于新搭配；以核心组合的突破和副铭文效果的增强，感到对炼金或魔法语言越来越熟悉。该期望来自用户，不是已观察结果。

暂定标签：System / Constraint / Presentation；探索理解、知识积累、组合突破、专门化成长。风险：穷举代替推理、符号只剩记忆、同词义不能迁移、共性没有实际联动、纯数字替换掩盖取舍、知识发现耗尽后重复劳动。

## 与既有页面的差距

| 既有覆盖 | 本轮补充 | 处理边界 |
| --- | --- | --- |
| 有限装配、实体分配、兼容理解 | 暗句是理解配方及相关行动的核心语义；有限规律同时承载探索 | 不把暗句设为可以自行推导任意卡效的语言引擎 |
| 主辅槽结构、可选修饰和占用成本 | 主铭文取舍形成组合变化；副铭文提供有侧重的量值／节奏成长 | 不把“主”解释为永不调整，也不把“副”解释为收益必须很小 |
| 信息可读和原因可查 | 已知语义可读、未知组合未列全、试配成立后结果公开 | 新的揭示规则为 Qualified 候选，未修改 TL-31 等现行文本 |
| 情境取舍与理解假设 | 从推断、试配到发现，再用知识组织配方搭配 | “探索存在”不能证明玩家在推理，需要保留穷举与查表的失败路径 |
| 辅槽稀有度及标记协同 | 明确“升级”本轮指替换成长；保留时间与简单标记条件／支付 | 不自动新开实体强化、合成或槽位升级 |

## 资格确认记录

使用 grill-with-docs，依项目批量约定一次提出以下五项。提问用于补本轮设计意图与通用候选边界，不是现行规则采纳请求。

| 编号 | 已展示的推荐与影响 | 用户答复原文 |
| --- | --- | --- |
| INS-I1 | 单枚铭文基本含义、槽位规则可读；未知合法组合不预先列全；试配后反馈是否成立，成立后可查看行动与制造要求。保留破解感，并区分不成立与缺料 | “按推荐：隐藏未知组合，成立后公开结果” |
| INS-I2 | 在允许的战前编辑中试配，不成立时不消耗铭文或制造材料；实际施放按配方支付。代价主要来自取得、分配铭文和选择带入方案 | “按推荐：试配免费，施放付费” |
| INS-I3 | 发现后可长期查阅，不每局重猜；知识保留不赠铭文、材料或永久属性，后续探索来自新铭文、法器与组合 | “按推荐：知识可长期查阅” |
| INS-I4 | 保留已有生成时间修饰和简单标记条件／支付，仅服务本法器时间或既有行动量值；不新增主行动逻辑、目标、事件或直接跨法器加成 | “按推荐：保留时间与标记条件／支付” |
| INS-I5 | 本轮按替换更适配或更高稀有度副铭文理解成长，继续取舍为主、成长并存；实体强化、合成及槽位升级分别待设计 | “按推荐：以替换获得成长” |

五项均已答复，不重复询问。INS-I3只确认配方知识可长期查阅，不建立完整局外成长系统、图鉴奖励或永久解锁实体；INS-I2没有授权战中换铭、免费获得候选或无成本施放；INS-I4没有将“标记”变成新的核心逻辑入口。

| 资格问题 | 当前答案 | 状态 |
| --- | --- | --- |
| 来源及设计对象 | 本页用户原话与五项答复；铭文及辅槽 design／experience | Clear |
| 情境及功能 | 允许的战前配置、配方探索、取得新铭文后的搭配判断，战中按配方兑现 | Clear；战中重铭仍未开放 |
| 行为及可见影响 | 阅读基本语义、试配、发现并查阅、围绕共性组合、替换副铭文 | Clear |
| 价值及体验 | 理解配方语言、发现组合、形成流派联系与有侧重成长 | Clear；Hypothesis / NotRun |
| 与已有设计关系 | 继承有限核心／实体／队列，新增发现与知识边界；辅槽权限继续引用 AUG-Q1—5 | Clear；新增候选未采纳 |
| 未知及下一步 | 探索内容如何免于穷举、知识记录范围、反馈粒度、实际搭配价值；内容设计后再做授权验证 | Clear；具体答案延期 |

资格结论：**Promoted / 局部 Qualified**。合格范围是用户明确的职责、风格、主辅差异及 INS-I1—5，不包含本文分析建议与未来实现默认。未新建 P／E／D，未改变 Accepted 规则。

## 阅读范围与版本

CUSTOM 继承上轮铭文范围，显式增补资源三份成果。实际基准 `51257ba5e00b0cae155940c11251134dffd6db69`；沿原任务工作树和分支。必要路由与治理文件在该提交相对上轮读取版本无变化，已按 Git 差异核对；不在根工作区切分支或改文件。

本轮完整重读铭文／辅槽四份 design、experience 和两份 rules，以及核心结构 M；沿本会话前轮读取复用 CORE-049 D、辅槽 M、辅槽确认原话段和上轮来源记录。相邻接口沿上轮已登记的法器、行动、标记、资源与交互条款，未扩读全 GDD。来源链接不递归读取。

| 本轮基准下的文件（相对 yanzhou） | Git blob |
| --- | --- |
| `design/systems/inscription-system/design.md` | `239b1c403dc3ebef256975862a7cb4a3fbab7315` |
| `design/systems/inscription-system/experience.md` | `504adb2a8954639b97c28747d90453e9a842927a` |
| `design/systems/inscription-system/augment-system/design.md` | `8a89a8c0dcdc3f1a62db036a535677cf2294a0f8` |
| `design/systems/inscription-system/augment-system/experience.md` | `efb3b50604d9a1a9227a56f38e0b3458545cc466` |
| `design/systems/inscription-system/rules.md` | `ab595a0bd063d17be5f3db9315d822874f80deb2` |
| `design/systems/inscription-system/augment-system/rules.md` | `93524f23ce61c8d11d2afb19246a2bcf8f6f35cb` |
| `sources/materials/M-2026-10-04-artifact-inscription-core.md` | `60839e0e589b0e4e6cb6ce798924b860bd8c333c` |
| `sources/draft-changes/D-2026-10-04-artifact-inscription-core.md` | `2ac8ff40f9f8f4c1d25d16d9c5999cbf8ccb6725` |
| `sources/materials/M-2026-10-08-augment-framework.md` | `dab538784a5e1d716ea80a785f7ed0e84da4e060` |
| `sources/inbox/2026-10-08-augment-framework-review.md` | `593b8326b27a331423855a8d5407b57c6b557c83` |
| `sources/inbox/2026-10-08-inscription-framework-review.md` | `03a3d47b08623aebfefa7505ece5313a5beab267` |

资源三份文件全文从共享 Git 对象中的固定提交 `54ad7597145127922759be7840c5d4d30ea786e1` 读取，未合并其分支或引用根工作区未提交材料：

| 文件 | Git blob | 用途 |
| --- | --- | --- |
| [资源原话与 R1—R20](https://github.com/dsaj4/game_design/blob/54ad7597145127922759be7840c5d4d30ea786e1/yanzhou/sources/inbox/2026-10-08-resource-design-intent.md) | `c58908a904562ba130854729f893a7f2753121a7` | 识别已确认候选与用户排除项 |
| [资源 M](https://github.com/dsaj4/game_design/blob/54ad7597145127922759be7840c5d4d30ea786e1/yanzhou/sources/materials/M-2026-10-08-resource-design-intent.md) | `bf338d8e0829ec4f2b1c16a10bd46592b70b475b` | 职责方法与材料／标记接口比较 |
| [资源 E](https://github.com/dsaj4/game_design/blob/54ad7597145127922759be7840c5d4d30ea786e1/yanzhou/sources/evaluations/E-2026-10-08-resource-design-intent.md) | `522bce681597b74259e3362ca7cc5a660872a6db` | 通用框架差异、失败路径及延期内容 |

上述初轮输入中，资源 R1—R20 当时为 Qualified 候选；此历史状态不随之后采纳改写。当前相邻状态已按下文 CORE-058 增补，不能再把资源写作仍未采纳。其具体职责、目标密度和操作取向不自动套用于铭文。排除旧项目、历史、探索方向、未提交原始材料、外部代码、Demo与联网研究。本轮无实验或实现证据。

## 供集成者处理的增量

本轮按文件所有权约定不修改共享文件，以下是集成建议，不是已完成操作：

- `design/source-review.md`：增加本 M 的限定使用记录，区分已有来源复用、新职责和 INS-I1—5 候选；相邻资源状态沿 CORE-058，不将资源采纳扩展成铭文新意图采纳。
- `governance/decision-log.md`：若登记本次文档组织，只记设计／体验补充；新的发现、免费试配及长期知识规则须在未来采纳流程中另记，不分配或占用本轮共享 DOC／CORE 编号。
- `governance/questions.md`：后续需要时接入探索反馈粒度、知识保存等候选接口；本轮五问已答，无需再列待答。
- `CONTEXT.md`、核心摘要与阅读合同：本轮不改术语权威或已采纳摘要。长期知识查阅不能直接把未开发的局外成长系统标为已完成。
- 未来铭文采纳复审：TL-39／40 与交互 TL-31／36 的已知／未知信息、发现记录及保存仍需处理。原建议的辅槽第 3 节范围澄清、资源 R1 无铭文加工及 R10—11 多阶量值／效果差异已由 CORE-058 在资源分支采纳同步；后续集成须保留，不再重复当作待采纳，也不能用本工作树旧规则覆盖。

## 输出与检查

本页与 [M](../materials/M-2026-10-09-inscription-design-intent.md)保存来源和资格；[铭文设计](../../design/systems/inscription-system/design.md)、[体验](../../design/systems/inscription-system/experience.md)、[辅槽设计](../../design/systems/inscription-system/augment-system/design.md)、[体验](../../design/systems/inscription-system/augment-system/experience.md)按局部资格补充解释。规则、示例、旧来源及共享文件保持不变。

检查仅限本轮文件、链接／锚点、资格状态、来源版本及写入范围；不把文档一致性当成玩法或体验验证。本批五项均已答，具体配方、数值和执行合同留后续流派及采纳阶段。

静态结果：六个本任务文件中的 69 个本地链接与 3 个新增锚点可达；4 处资源固定提交链接已用本地 Git 对象核验，11 个主系统输入 blob、3 个资源输入 blob 及交接 SHA-256 匹配。用户原话与五项答复逐字核对通过，规则、示例、旧来源及共享文件未修改，Git 差异空白检查通过。检查辅助仅存本地 `.git/codex-tasks/`，不提交脚本。

## 同日增补：资源 CORE-058 已采纳

来源为原授权交接会话的续接通知，并已读取 [资源采纳 D](https://github.com/dsaj4/game_design/blob/79be780e2ef9c9c8af76d8c1ed1467deb7f242bc/yanzhou/sources/draft-changes/D-2026-10-09-resource-system-design.md)核实其中用户“更新到主系统中”的明确授权与 Accepted 状态。只增补固定提交 `79be780e2ef9c9c8af76d8c1ed1467deb7f242bc` 的必要接口，未合并整个分支或读取根工作区未提交内容。本轮本地起点为 `4ed6c79e9f2fd14476588f2e6bc3c89532be2152`。

| 增补文件（相对 yanzhou） | Git blob | 实际覆盖 |
| --- | --- | --- |
| `sources/draft-changes/D-2026-10-09-resource-system-design.md` | `5cfab479ff17203fd08ea46ccd6f654d9e5fb8d6` | 全文，CORE-058 采纳范围、理由与未决 |
| `design/systems/inscription-system/rules.md` | `347e52a251c7129a55f8579c6f18e47ff956d18f` | TL-02／40：基础用途、完整铭刻与未来批次 |
| `design/systems/artifact-system/rules.md` | `57776dcbca50cbda75ace42eb6232f032e6288dc` | TL-06／38：用途及阶级选择、承诺、独立基础加工入口 |
| `design/systems/inscription-system/augment-system/rules.md` | `905cc8f80e8297f22b95a576e46987ef919668d4` | 第 3 节：限制仅针对辅槽跨法器修饰 |
| `design/systems/resource-system/rules.md` | `13e72d60678e760dd39629665837d881af2345f3` | TL-43 及所属小节：性质／阶级、多阶兑现、基础加工与公开信息 |
| `design/common/interaction-save/rules.md` | `b4918a2316e5ee909d12181ef345511baab934d4` | TL-31：开战铭刻要求与基础可运行性 |

判定：资源三个职责及 R1—R20 已在资源范围成为 Accepted；铭刻仍须完整核心，开战至少一台合法铭刻法器；已有用途／兑现阶级选择不改既有承诺；辅槽标记协同不排除材料流转，基础用途不自动继承修饰。具体流派和数值仍延期，体验 NotRun。本素材的 INS-I1—5 和新增铭文意图仍为已确认的 Qualified 候选，未被此次资源采纳覆盖。

本轮只更新铭文／辅槽 design、本 M 和本记录四文件；experience 的假设未改变，现行规则文件仍只读。原六文件检查结果保留原提交含义，不能当成本次增补已检查的结论。

增补静态检查：四文件范围准确，47 个本地链接可达；8 个固定提交链接（含 4 个本次采纳链接）及 1 个保留锚点已核对 Git 对象，6 个增补来源 blob 匹配。用户原话和五项问答未变化，rules、experience 及共享文件未修改，Git 差异空白检查通过；未运行玩法测试。
