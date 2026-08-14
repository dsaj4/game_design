# Anode Heart: Layer Null 拆解大纲

## 总论点

待根据素材包补写总论点。

## 目标问题

- Can this BiliSum material support a comprehensive and accurate gameplay analysis dossier?
- What are the core loop, combat resolution, deckbuilding constraints, in-run economy, and growth routes of Anode Heart: Layer Null?
- Which structures can transfer into the current unique-core-card card-battle project?

## 证据地图

| ID | 类型 | 来源 | 说明 | 支撑模块 |
| --- | --- | --- | --- | --- |
| T1 | text | `../source/detailed_record.md` | Full transcript covering rules, match flow, deck adjustment, and conclusions. | module-2, module-3, module-4 |
| T2 | text | `../source/knowledge_note.md` | Structured summary of card types, turn order, counter cards, fragments, energy, evolution, and grass route. | module-2, module-3, module-4 |
| T3 | text | `../source/visual_enhanced_note.md` | Transcript with key visual anchors inserted. | module-2, module-3, module-4 |
| T4 | text | `../source/visual_note.md` | Short captions and paths for 28 keyframes. | module-2, module-3, module-4 |
| I1 | image | `../source/frames/f0001.jpg` | 00:31 游戏界面显示643种卡牌总数 | module-4 |
| I2 | image | `../source/frames/f0002.jpg` | 01:26 属性筛选界面显示六种属性 | module-4 |
| I3 | image | `../source/frames/f0003.jpg` | 02:48 卡牌类型标识：单位、app、patch、病毒 | module-4 |
| I4 | image | `../source/frames/f0004.jpg` | 26:10 牌组界面显示40张卡，其中15张单位卡 | module-3, module-4 |
| I5 | image | `../source/frames/f0005.jpg` | 28:40 败局画面，作者表示无色牌组不行 | module-4, module-5 |
| I6 | image | `../source/frames/f0006.jpg` | 34:00 卡牌效果：回收草系单位、复活所有植物单位 | module-4 |
| I7 | image | `../source/frames/f0007.jpg` | 39:00 使用回收牌后，弃牌堆两个单位出现在场上 | module-4 |
| I8 | image | `../source/frames/f0008.jpg` | 40:00 单位属性显示35/25，对手无法应对 | module-4 |
| I9 | image | `../source/frames/f0009.jpg` | 04:14 区域说明：森林区域获得草系牌，新手区域无色牌 | module-4 |
| I10 | image | `../source/frames/f0010.jpg` | 05:22 对战界面：对手先手出一张牌，后手方行动标记 | module-4 |
| I11 | image | `../source/frames/f0011.jpg` | 07:42 反制牌动画，将对手低血单位移除 | module-4 |
| I12 | image | `../source/frames/f0012.jpg` | 08:00 被动技能图标，显示碎片数量增加 | module-4 |
| I13 | image | `../source/frames/f0013.jpg` | 11:37 商店界面，购买抽三张牌并洗入牌组 | module-4 |
| I14 | image | `../source/frames/f0014.jpg` | 14:57 卡牌右下角显示能量费用：无色能量和绿色能量 | module-4 |
| I15 | image | `../source/frames/f0015.jpg` | 24:30 卡牌说明显示进化条件：需要特定一级单位在场 | module-4 |
| I16 | image | `../source/frames/f0016.jpg` | 28:00 单位卡牌变化，属性大幅提升 | module-4 |
| I17 | image | `../source/frames/f0017.jpg` | 30:30 进化出10-10单位，但对手单位更强 | module-4, module-5 |
| I18 | image | `../source/frames/f0018.jpg` | 36:00 卡牌说明显示进化后属性10-10 | module-4 |
| I19 | image | `../source/frames/f0019.jpg` | 36:40 场地卡说明：任何时候复活草系单位，抽一张牌 | module-4 |
| I20 | image | `../source/frames/f0020.jpg` | 06:05 使用吸血牌，一滴血单位被消灭 | module-4 |
| I21 | image | `../source/frames/f0021.jpg` | 09:04 反制卡生效，对手强力卡被取消 | module-4 |
| I22 | image | `../source/frames/f0022.jpg` | 10:01 使用牛奶牌，给单位+2+2 | module-4 |
| I23 | image | `../source/frames/f0023.jpg` | 12:17 战斗阶段，伤害方块从左到右依次碰撞 | module-4 |
| I24 | image | `../source/frames/f0024.jpg` | 17:00 回合开始只抽一张牌，手牌无单位卡 | module-3, module-4 |
| I25 | image | `../source/frames/f0025.jpg` | 17:35 手牌中有需要4点绿色能量的卡，当前能量不足 | module-4 |
| I26 | image | `../source/frames/f0026.jpg` | 20:20 手牌满，但没有可打出的单位或有效卡 | module-4 |
| I27 | image | `../source/frames/f0027.jpg` | 22:30 反制卡使用后，对手也打出反制卡 | module-4 |
| I28 | image | `../source/frames/f0028.jpg` | 27:30 使用卡牌造成3点伤害并增加火焰能量 | module-4 |
| V1 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0001.jpg` | The collection interface exposes cards as collectible assets with purchase/currency state and individual rule text.; Card identity combines element/type tags, HP/BP stats, bonus growth, and triggered effects.; Card collection/library screen with a grid of locked and owned cards.; Top bar shows Page 9/31, a Bitcrush button, and 488 Bits currency.; Page arrows for browsing card pages.; Close button and Bitcrush action in the library header. | module-1, module-4, module-6 |
| V2 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0002.jpg` | Deck composition is visible as typed counts, making unit/support ratio a deckbuilding constraint.; The deckbuilder separates current deck from the global card pool and supports sorting/import/export.; Deckbuilding screen for a colorless deck: left deck list, right All Cards browser, category counters at the top.; Top counters read Apps: 22, Patch: 3, Tama: 15, Virus: 0; deck area says 40 Cards.; Sort, Import, Export buttons.; Test button is present but appears disabled or inactive. | module-4, module-5 |
| V3 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0003.jpg` | Longer-term growth can unlock starting energy and shard triggers, connecting deck archetype to economy.; The tree layout suggests multiple passive/evolution nodes rather than a single linear upgrade.; Evolution/DNA screen for Saplee with a hex-grid unlock tree.; Header shows Unlock Evo. with a shard-like cost of 1 and Unlocked: 2/26.; Arrow navigation in the unlock panel.; Unlock cost indicator near the top-left button. | module-4, module-5, module-6 |
| V4 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0004.jpg` | Combat is lane/row-like rather than a free board: units line up horizontally and resolve across a central divide.; The player manages hand cards, board slots, HP/BP totals, shop access, and pass timing in one combat screen.; Combat board with opposing units on the upper half, player units on the lower half, and a hand along the bottom.; Left side has a Pass button and stacked icons/counters; bottom center has Shop and resource bars.; Compared with earlier sparse board frames, this frame shows a developed mid-combat board with six player units.; Pass button remains available during the player decision state.; Hand cards are selectable at the bottom. | module-3, module-4, module-8 |
| V5 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0005.jpg` | 28:40 败局画面，作者表示无色牌组不行 | module-5 |
| V6 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0006.jpg` | Card effects can open choice panels during combat rather than only resolving instantly.; Grass/native package visibly includes HP manipulation and high-level units.; A modal/card-selection panel is open over combat, showing multiple selectable card slots on Page 1/1.; Left card detail panel describes a native App named nutrient and a health-draining effect from one Tama.; Cancel button on the selection panel.; Page arrows on the modal. | module-4, module-5 |
| V7 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0007.jpg` | In-run shop uses shards or a similar currency to buy tactical card effects.; Draw/filtering is purchasable mid-run, tying economy directly to draw consistency.; Shop popup with the title Choose a card to buy and three card choices.; Each option has a shard-like cost below it: 3, 4, and 5.; Close button in shop popup.; Card choices are presented as clickable purchase options. | module-4, module-6 |
| V8 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0008.jpg` | The grass/native build can produce very large board stats compared with earlier low-stat frames.; Turn loop returns to player after board development, preserving hand/board/shop decisions.; Player board has five units including a level 3 unit showing 10/10 and a front unit showing 11/4.; Bottom stats show Shop, shard/resource count, HP 25, and BP 3.; Compared with V4, player HP and board stats are much higher, showing progression inside the match.; Pass button and hand cards remain available on the player turn. | module-3, module-4, module-8 |
| V9 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0009.jpg` | 04:14 区域说明：森林区域获得草系牌，新手区域无色牌 | module-4 |
| V10 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0010.jpg` | Summoning a unit can apply a status effect immediately, so unit cards are not only stat bodies.; Card hover/selection exposes rule text before commitment.; Early combat frame with one enemy unit and one player unit on the board.; Hovered hand card Pawee displays tags neutral / mouse / Tama and No Cost.; Pass button on left; hand card tooltip triggered from bottom hand. | module-3, module-4 |
| V11 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0011.jpg` | 07:42 反制牌动画，将对手低血单位移除 | module-4 |
| V12 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0012.jpg` | 08:00 被动技能图标，显示碎片数量增加 | module-4 |
| V13 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0013.jpg` | The central line visually separates sides and likely marks combat resolution lanes/rows.; The six-unit row makes board capacity a tactical limit.; Combat board is divided by a horizontal striped line; enemy units above and player units below.; Player has six units across the bottom row, suggesting the visible board capacity is capped at six units.; Player board is full or near full, unlike sparse early combat frames.; Pass button available during the state.; Hand cards remain visible under the board. | module-3, module-4 |
| V14 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0014.jpg` | Some cards convert HP gain triggers into native energy, connecting health growth to resource generation.; The UI distinguishes generic and native/element-specific resource pools.; Hovered card Munching Saplee shows native / Plant / Tama tags and No Cost.; Card text includes On Trigger, selecting one Tama, HP gain, HP bonus gain, and then gaining native Energy.; Hover panel gives detailed timing text and bonus/stat preview. | module-4, module-6 |
| V15 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0015.jpg` | Evolution or higher-level units coexist with base units on the same combat row.; The frame supports the existence of level states, but not the full evolution prerequisite by itself.; Level 2 player unit is on the board, with two smaller 1/1 units beside it.; Player hand includes two pink unit cards and one 3/2 unit card.; Pass remains available; hand cards can still be played or held. | module-4, module-5 |
| V16 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0016.jpg` | 28:00 单位卡牌变化，属性大幅提升 | module-4 |
| V17 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0017.jpg` | 30:30 进化出10-10单位，但对手单位更强 | module-5 |
| V18 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0018.jpg` | High-level cards with large stats are part of the grass/native package.; Visual feedback indicates an action or effect resolving, but exact cause requires transcript support.; Combat frame with a greyed card moving or targeting on the right side, plus colored hit/feedback marks near a unit.; Bottom hand includes a level 3 card whose large 10/10 stat line is visible.; The right-side ghosted card/arrow suggests targeting, movement, or resolution feedback. | module-4, module-5 |
| V19 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0019.jpg` | Damage/healing feedback is communicated as floating text over units and separate resolution blocks.; Resolution appears stepwise/ordered, with visible damage blocks on the left.; Combat resolution frame shows floating -1 HP text over a top-side unit.; Left side displays blocks of numbered damage or resolution tiles, including 2, 3, 4, 2, 3 and a lower row 2, 1.; Compared with decision frames, this one appears to be an automatic resolution state.; Pass button is dark/disabled during resolution, implying player input is locked while effects resolve. | module-3, module-4 |
| V20 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0020.jpg` | 06:05 使用吸血牌，一滴血单位被消灭 | module-4 |
| V21 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0021.jpg` | 09:04 反制卡生效，对手强力卡被取消 | module-4 |
| V22 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0022.jpg` | 10:01 使用牛奶牌，给单位+2+2 | module-4 |
| V23 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0023.jpg` | 12:17 战斗阶段，伤害方块从左到右依次碰撞 | module-4 |
| V24 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0024.jpg` | Some units refund cards on deletion, making death/removal part of resource flow.; The frame visually supports draw variance concerns: hand composition can be non-unit-heavy while board presence is thin.; Hovered card Porren shows native / Plant / Tama tags and No Cost.; Card text reads On Delete: Draw 1 card.; Hover detail panel and Pass button support inspection before action. | module-3, module-4, module-8 |
| V25 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0025.jpg` | 17:35 手牌中有需要4点绿色能量的卡，当前能量不足 | module-4 |
| V26 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0026.jpg` | 20:20 手牌满，但没有可打出的单位或有效卡 | module-4 |
| V27 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0027.jpg` | 22:30 反制卡使用后，对手也打出反制卡 | module-4 |
| V28 | visual-audit | `../bv1xaxpbhezc-anode-heart/source/frames/f0028.jpg` | Deckbuilder enforces or warns around a 40-card minimum, filling missing slots with blanks.; Card pool filtering by element/type supports archetype-specific rebuilding after failures.; Grass deckbuilding screen with deck counters: Apps 8, Tama 0, Patch 0, Virus 0 in the header.; Warning text says the deck contains less than 40 cards and will be filled out with Blanks in game.; This frame contrasts with V2 by showing grass/native filtering and an incomplete deck warning.; Sort, Import, Export, Test controls; card-pool page arrows and filter label. | module-4, module-5, module-8 |

## 模块规划

| 模块 | 核心判断 | 证据 | 未确认信息 | 优先级 |
| --- | --- | --- | --- | --- |
| 游戏核心定位、基础信息、商业大盘复盘 | 待根据证据补写。 | V1 | 材料不足时补写未确认信息。 | medium |
| 全局玩家体验与底层设计目标 | 待根据证据补写。 | T1, T2, T3, T4 | 材料不足时补写未确认信息。 | high |
| 核心玩法循环 | 待根据证据补写。 | T1, T2, T3, T4, I4, I24, V4, V8, V10, V13, V19, V24 | 材料不足时补写未确认信息。 | high |
| 全链路游戏架构拆解 | 待根据证据补写。 | T1, T2, T3, T4, I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13, I14, I15, I16, I17, I18, I19, I20, I21, I22, I23, I24, I25, I26, I27, I28, V1, V2, V3, V4, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28 | 材料不足时补写未确认信息。 | high |
| 内容与关卡体系 | 待根据证据补写。 | I5, I17, V2, V3, V5, V6, V15, V17, V18, V28 | 材料不足时补写未确认信息。 | medium |
| 数值体系与经济资源闭环 | 待根据证据补写。 | V1, V3, V7, V14 | 材料不足时补写未确认信息。 | medium |
| 叙事体系、角色 IP 与视听包装 | 待根据证据补写。 |  | 材料不足时补写未确认信息。 | low |
| 优劣复盘与可落地优化方案 | 待根据证据补写。 | V4, V8, V24, V28 | 材料不足时补写未确认信息。 | high |

## 图示计划

- 核心循环图：模块3，用于解释输入、行动、产出、消耗、反馈和回流。
- 系统关系图：模块4，用于解释系统联动。
