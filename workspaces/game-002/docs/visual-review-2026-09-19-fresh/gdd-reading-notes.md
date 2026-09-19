# GDD 阅读对照与评审范围

2026-09-19。当前使用RC1主文档和其10篇规格正文、Wiki目录；根GDD索引用于判断版本优先级。仅阅读文字，未打开任何仓库已有图片。独立输出目录避免覆盖工作树中的其他视觉稿。输入文件的SHA-256见[来源清单](source-manifest.json)。

## 全部正文对视觉工作的约束

| 文字来源 | 读取内容 | 本包对应处理 |
| --- | --- | --- |
| [主GDD 0–18章](../../game-design-workflow/gdd/GDD-2026-09-14-yanzhou-full-game.md) | 产品合同、单局循环、53实体、7系统、平台和交付边界 | 风格服务战前编排与自动观察；图像不等于已开发或体验验证 |
| [01 七系统](../../game-design-workflow/gdd/yanzhou-rc1/01-systems.md) | 输入／代价／失败／验收及依赖 | 配置、战斗、获取三个主状态清晰分开 |
| [02 构句与配置](../../game-design-workflow/gdd/yanzhou-rc1/02-grammar-and-configuration.md) | 阵营、三杖、12词起点、角色白名单、装配、效果组 | 02、04、05共用同一默认实体配置；固定芯与可换两槽分开 |
| [03 战斗与状态](../../game-design-workflow/gdd/yanzhou-rc1/03-combat-and-status.md) | RC01–12、BR、ST、GR、四阶段、开始槽与打断 | 竖向共同刻轴、名义计划、只读配置和独立失败原因 |
| [04 元素与环境](../../game-design-workflow/gdd/yanzhou-rc1/04-elements-and-environment.md) | 十格、邻近、宿主资格、原地新身份、当前层与历史痕迹 | 元素本体／宿主状态／地面分层；火冰形态不暗示新能力 |
| [05 全53实体](../../game-design-workflow/gdd/yanzhou-rc1/05-card-catalog.md) | 9名词、14动词、11形容词、19镶嵌的卡面、角色、参数、正反例与组合 | 图中文字仅取实际卡；06的印记／标记／空心的均属首期合格名称 |
| [06 参数与经济](../../game-design-workflow/gdd/yanzhou-rc1/06-parameters-and-economy.md) | τ、C/L、取整、支付、全部价格与取得时点 | 起点与首次释放分开；卡面时间不画成法力费用；商店无刷新 |
| [07 路线与遭遇](../../game-design-workflow/gdd/yanzhou-rc1/07-route-and-encounters.md) | 19节点全部连边、12布场、8敌人、疲劳和跨战账本 | 01采用C1原始布场；03显示纸地图与19节点结构候选 |
| [08 旅程/UI/资产](../../game-design-workflow/gdd/yanzhou-rc1/08-journey-ui-and-assets.md) | 三步编排、默认9卡、播放／保存、无障碍、逐类资产 | 页面功能、法杖袋文字入口、字体缩放、低动效目标 |
| [09 验收与风险](../../game-design-workflow/gdd/yanzhou-rc1/09-validation-and-risks.md) | I0–I3、K01–09、720单场、36边界、20整局、V01–20、U任务及证据限制 | 当前只查视觉文件和规则表述；不执行、不宣称通过这些玩法计划 |
| [10 素材审查](../../game-design-workflow/gdd/yanzhou-rc1/10-source-review.md) | 68正式素材和47原始记录的Include/Park边界 | 不恢复草法术、召唤、旧卡池、旧参数和旧图设定 |

## 版本解释

- 根GDD索引开头明确RC1 Accepted并优先，其结尾仍有“当前尚无已采纳GDD”的旧句。本次按新日期、RC1主文档及工作区AGENTS的明确优先级理解；未为视觉任务重写该历史段。
- Wiki中保留的一些“参数待补／尚未写GDD”沿袭段，用同包具体CG/PG/EG/RG/UX表解释，不能用旧段落回退已定参数。
- 旧 `GDD-2026-09-12-first-person-grid-battlefield.md` 在索引标为历史单项草案，本次不把其候选作为当前设计。
- 预期的 `research/00-index-and-roadmap/current-questions.md` 在当前工作树不存在，已核实；当前问题入口采用工作区AGENTS指定的 `docs/design-decisions-needed.md`，不从其他项目补读。

## 参考观察的具体范围

| 游戏 | 本次官方页面可见证据 | 改编方式 |
| --- | --- | --- |
| Inscryption | 桌面对战画面：低视点、暖光、刻线卡格、实体卡纸、暗背景 | 用更亮的纸面与本作四杖构句替换原卡牌对战；不借入献祭等规则 |
| Noita | 官方页的像素洞窟、法术色光及玩法说明；本次未取得库存面板的精确截图 | 05仅为法杖槽位组织的概念借鉴，不称为截图复刻；不用法力、乱序、背包容量替换本作规则 |
| Slay the Spire | 官方页视频中的Choose a Card：上方横幅、居中三卡、下方Skip、压暗背景 | 改为本作休整拿词流程，保持只能选一或拒收的节点约束 |

官方页面只作视觉参考，未导入任何原游戏图标、卡图或角色资源。题材氛围、色彩、造型和布局是本轮agent提出的**视觉候选**；游戏规则仍以RC1为准。

## 对图片的使用边界

这批图用于选择材质、布局与信息密度。它们没有提供完整可交互控件、真实动画、存档或测试证据。生成文字、地图连线及个别图标必须按[质量记录](qa-notes.md)校正后才能作为制作布局依据；不能从图中多画的装饰推导新物品和能力。

Demo开发待用户确认本包后启动。阅读RC1和制作视觉稿不自动接受新的核心玩法、参数或正式美术规范。
