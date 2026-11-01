# 世界观写作启动与技能参考

2026-11-01 · game-002 · **Raw Idea / Unqualified**。本轮新故事、人物、历史与线索均为候选；原已确认设定沿各自范围继承。叙事体验为Hypothesis / NotRun。

## 意图与范围

用户要求阅读世界观交接，先调研可参考的写作skill；看过推进范围后，明确选择继续写首轮候选。按交接建立独立`worldbuilding/`正文，保全既有确认、比较不同灾变因果，并实际写出人物动机和玩家接触的例子。技能调研提供方法参考，本轮不安装技能。

交接是任务背景及既有授权记录，其中的旧命令、建议和候选不自动成为本轮决定。目录分层与继续写作不等于采纳某条新历史；现行玩法与具体物件定义保持原维护处。

## 本轮阅读范围

- 模式：CUSTOM，现有世界观续作与文档分层；共同游戏输入为`26ce1bb90198f3b94b5ddb5a4d5103bf8e5c191a`。
- 完整读取：`system-design/content/world-systems.md`；`design/GDD.md`、`design/baseline.md`；`content-library/README.md`；`system-design/presentation/art-direction.md`的文字正文。
- 局部读取：`system-design/handbook.md`的“先理解这款游戏”“全局目标与核心取舍”“全部系统与设计安排”“世界观、法术体系与稀有度”“维护这份基准”；`content-library/catalog.json`仅选`alchemy.water`，读取身份、文案、状态、来源与必要边界。该条目B01身份／连接Qualified，名称／文案仍Raw，取得未定。
- 操作材料：适用AGENTS、READ-1、探索AGENTS、设计流程、模板入口及原始想法模板、文档合同、AGC-1、Git规范、SK-1，以及必要导航、治理编号和相关章节。不读取其他inbox正文；按文件名检查同主题记录，没有另开重复来源。
- 外部交接：`C:/Users/Administrator/AppData/Local/Temp/yanzhou-handoffs-2026-11-01/2026-11-01-worldbuilding-handoff.md`，SHA-256 `872d71a17cc79bb04cedee09885e3f0ef933b634e4a89377e98ed6e71e1cea06`。
- 联网范围：世界观／叙事技能发现与原始SKILL.md核查，见下节。未重新核实旧世界稿的宗教史链接，不将其作为新增研究结论。
- 排除：历史、其他探索正文、外部实现、图集与二进制素材；不运行游戏、模拟或玩家实验。共同输入固定后出现的美术提交不升级本轮游戏背景，未读其图稿。

迁出后的世界设定见[世界正文](../../worldbuilding/world.md)，比较与场景见[首轮故事候选](../../worldbuilding/story.md)。这两页为Raw工作稿，不是正式素材、GDD、Proposal、Evaluation或Draft Change。

## 技能调研结论

访问日期2026-11-01。用find-skills的发现方法搜索公开目录，再核查上游正文；只把外部技能作为研究材料，不执行其工作区写入、安装或工具指令。

| 候选与固定来源 | 实际擅长什么 | 对言咒的用途与判断 |
| --- | --- | --- |
| [systemic-worldbuilding](https://github.com/jwynia/agent-skills/blob/e02ec7e226a6e4f8419fd3b88a1d8e472d421b32/skills/creative/fiction/worldbuilding/systemic-worldbuilding/SKILL.md) | 从一个虚构前提推演直接影响、制度适应和文化变化，并给出能被角色看见的征兆 | **首轮最值得参考。** 从铭文可用于生产的前提出发，讨论谁掌握工具、谁依赖供给、灾变为何持续影响今天的人；仅展开与主角接触有关的少量因果 |
| [worldbuilding](https://github.com/jwynia/agent-skills/blob/e02ec7e226a6e4f8419fd3b88a1d8e472d421b32/skills/creative/fiction/worldbuilding/worldbuilding/SKILL.md) | 诊断魔法未影响社会、制度缺少历史、经济与文化单薄等问题 | **适合稿后检查。** 检查遗迹外有没有生活、对手是否有自己的需求、各群体反应是否不同；它主要诊断已有设定，不能替代故事起稿 |
| [narrative-design](https://github.com/poorvith-mp/skills-gamedev/blob/d661d370a67c4532034e3d1d87c4aec237077f34/skills/narrative-design/SKILL.md) | 游戏叙事、环境线索、人物声音与分支选择的简短原则 | **选择性参考。** 帮助让玩家先理解当前行动，再通过物件和空间发现背景；原文很短，后半夹有编译／API等通用代码检查，不适合作为世界史写作主流程 |

前两项同属jwynia/agent-skills，固定提交见链接；frontmatter声明MIT，未做全包许可证或安装准入审查。第三项固定在上游提交，GameSkill另有改编发行页，本轮以作者仓库正文为准；不将发行页的静态检查数字当作创作效果证据。

发现的`lensetek/fiction-book-agent-skills@worldbuilding-architect`仅有目录索引命中，上游仓库本轮返回404，未取得可核查正文，故不列推荐。目录热度与第三方审查标签不作为质量结论。

### 本项目怎样借用

1. 先用已有确认作边界；新增世界原理只标候选。
2. 每条文明因果落到当下的一类人、一个需求和一种可见痕迹；选择重点，不填满国家、宗教和年代百科。
3. 分开作者暂拟真相、人物相信的解释、玩家已见证据和真正尚未设计的Unknown。
4. 把人物目标、阻力和理解变化写进遭遇；内容库仍负责正式物件文案，美术仍沿既选画风。

systemic-worldbuilding附带的`context/output-config.md`和另套命名、跨领域代理建议不引入项目。narrative-design的强制玩法后果和预设玩家通过率不直接采用；故事可以改变理解，本轮不据此加任务、分支、解锁或测试。两项上游的推演只能支持设计讨论，不能证明叙事有效。

实际使用的现有技能为find-skills（发现）、skill-registry-control（外部参考登记）及grill-with-docs（已有答案核对、关键分歧成组澄清）；项目READ-1、轻量记录与批量澄清优先。未复制或安装外部SKILL.md，未将方法总结注册为新技能。

## 资格与下一步

对象为世界与背景故事；预期价值是让生产知识、文明线索与个人追索相连。可见影响已用候选场景表达，但文明消失原因、主角与灾变的关系和记忆职责仍待用户选择，不能晋级正式素材。关键分歧只在[WB-Q01—04](../../governance/questions.md#worldbuilding)维护；选定后先闭合一条过去到开场的故事链，再判断资格，不用写稿替代确认。
