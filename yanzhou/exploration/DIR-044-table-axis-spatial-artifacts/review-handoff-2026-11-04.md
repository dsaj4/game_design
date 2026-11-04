# CORE-075 采纳后审查交接

2026-11-04 · 交给负责审查与完善的下一个 agent。状态：用户已明确回复「直接采纳」，CORE-075（GDD 3.8，table-axis.1）已回写。玩法与体验 NotRun，操作量只有纸面推演，真人未测。

- 分支：`codex/2026-11-02-tabletop-html`；共同基准提交 `d92851e951a3a8ad67e26962c4a9924ac5cd532b`。
- 采纳提交：`58ccd5e`（32 个文件）。**推送未成功**：GitHub Git Operations 事故期间连续三次 Internal Server Error，远端停在 `b0cb167`，本地领先 1 个提交。事故解除后在 `E:\Project\game` 执行 `git push origin HEAD`；不要强推。
- 来源链：[DIR-044 方向页](README.md) → [M](M-2026-11-04-table-axis-spatial-artifacts.md) → [E](E-2026-11-04-table-axis-spatial-artifacts.md) → [D（已采纳）](../../sources/draft-changes/D-2026-11-04-table-axis-spatial-artifacts.md)。

## 1. 采纳了什么

- 一桌一轴：横向 X=5 个时间列，纵向战斗行加每台法器一条工序行；唯一动词是排；一根光标，左侧冻结、右侧可改；D 以列计，第 c 列开工、第 c+D 列的列间窗口入手、下一列起可用；最终整理与列间窗口合并为布置窗口。
- 空间：炉心必选（小炉 1×1、长炉 1×2）；圈号＝max(0, 曼哈顿距离−1)；圈下限＝1＋圈号（示意值）；实际 D＝max(圈下限, 公式结果)；法器组合（首批只做硫链）；入料口尺寸 P；辅助改为覆盖圈（首版距辅助格曼哈顿距离不超过 2）。
- 取消：生产拍、累计拍、第 0 拍、观察窗、待料、托管、吸收拍、供料资格拍、材料锁定、自动补料、法器序、接收范围、一格接触、唯一链接、辅助朝向与单器连接。
- 不做打断介入生产；封印牌另行采纳，首战不引入。
- 首战：先配 1 枚小炉，加 1 个序幕回合；补给解封改为列序号。
- 内容：滚烫蒸汽 r04、轻盈雾团 r05、草药汁液 r06 由 D2 改 D3；合计工时 生命灵药 9→10、水银飞弹 18→19、炼金爆弹 20→21、万灵药 53→54。
- 保留：八法器本体占形、CORE-067 统一卡牌与三权限、CORE-069 核心可逆装配、CORE-070 共用背包、TL-21 空放、疲劳与终局。

## 2. 改动文件

- 核心与规则：`design/GDD.md`；各系统 `rules.md`（artifact、resource、action-card、backpack、enemy、inscription、augment）；`common/interaction-save/rules.md`；`common/run-economy/rules.md`。artifact 与 resource 两份是整页重写，其余是定点替换。
- 参数与验收：`design/parameters.md`、`design/validation.md`（新增 CORE-075 一节，旧 CORE-074／068 节只改标题标注替换，未逐项重写）。
- 内容：`content-library/catalog.json`（仅 r04、r05、r06 的 duration 与四个成品的合计工时），并用外部生成器重建 `alchemy.md`、`recipes.md`、`index.html`，`build.py --check` 通过；`design/content/wands.md` 少量替换。
- 登记与导航：`governance/decision-log.md`（CORE 下一编号 076）、`design/baseline.md`、`governance/rule-index.md`、`governance/questions.md`、`CONTEXT.md`、`development/README.md`、探索入口与 DIR-044 方向页。
- 派生：四个任务包（round-hand、future-purpose、shared-backpack、interruption-restart）仅在开头加「待同步」；EX-005 仅在开头标「待重算」；`system-design/effects/catalog.md` 改了一处锚点文字。

## 3. 已知缺口，请优先审查

1. **首战规格未改。** `content-library/first-battle.md` 及 catalog 中的 encounters 仍是旧版：未改为 1 枚小炉、无序幕、布局锚点与待料 9 格仍是旧值。须改 catalog 再用 `E:/Project/yanzhou-ui-prototypes/content-library-2026-11-01/` 的 `build.py` 重建。
2. **内容库残留废止字段。** `artifact-geometry.md` 的接收范围字段、`alchemy.md` 各法器的「供料范围」行、`recipes.md` 各条的「局部装载」段、catalog 中 `fit` 里的 `feedArea` 等；这些已被 CORE-075 废止，也要经 catalog 改。成品的「冷启动首份下界」按旧时间线推出，需重算。
3. **EX-005 未重算。** 时间表、两条获胜路线、胜利重装段仍是旧推导。可参考方向页「TA-Q10 纸面推演」：1 枚小炉下萃炼器被拖慢，草本灵液 D3 变 4。
4. **链接与锚点没做全库核对。** 我只检索替换过 `卡牌的战斗与供料可用时点`（已改为 `…排料可用时点`）。GDD 的 `TL-12` 标题改为「伤害与封印」，原锚点 `#tl-12-伤害与法器中断` 可能被其他页引用；`TL-07` 打断条款保留了标题但内容退役。请全库搜 `tl-12`、`tl-07`、`tl-09`、`tl-06`、`tl-15` 的引用。
4. **旧词残留。** 建议在 `yanzhou/` 下搜：待料、生产拍、吸收、接收范围、供料、托管、自动补料、观察窗、最终整理、法器序、材料锁定、打断。`GDD.md` 第 3 行版本头还夹着 3.7 的旧说明，可精简；`TL-11` 与 `TL-30` 的措辞需通读。
5. **未读未改的文件。** `development/task-packs/first-battle-alchemy.md`、各系统 `design.md`／`experience.md`、`system-design/presentation/`、`system-design/backpack/shared-backpack-design.md`、`examples.md` 系列、`standards/`。它们可能含旧机制描述。
6. **validation 只做了标注。** TL-V 系列里涉及生产拍、待料、打断的旧条目没有逐条标退役，需要按适用域逐项处理。
7. **未登记项。** 没有新增 G002-DOC 决定；`id-registry` 在当前树里不存在，未处理。

## 4. 数值与证据边界

- 圈下限曲线、覆盖圈半径、炉心配置均为示意值，待标定。
- 空间下限结论来自 8×5 空包枚举，脚本是临时文件，未入库；首战 1 枚小炉的**全部**最优摆法没有穷举，只验证了一个摆法。
- TA-Q10 纸面推演是固定策略计数：有序幕版每轮峰值 9 次拖放、合计 38 次，约三分之二为固定操作；无序幕首轮 11 次。真人操作量与可预测性未测。
- 原型 `spatial-artifact-v2.html` 的网格渲染未目视检查。
- 新增待办 TA-Q13：回收牌回手后是否默认待命于下一未开始列，暂不做。

## 5. 建议的审查顺序

1. 先确认推送成功；2. 补完内容库首战与废止字段并重建；3. 重算 EX-005；4. 全库搜旧词与锚点；5. 通读 GDD 第 2 至 5 节与 TL-11 的一致性；6. 处理 validation 旧条目与各 design／experience 文档。审查中发现需要改规则的地方，回对应权威页，不要直接改任务包。
