# 言咒桌面：背包空间与信息层级输入

2026-10-31建立，2026-11-01更新 · game-002 / main · **Promoted：限定的非规则呈现素材已通过资格，体验验证NotRun**。

**当前唯一审阅入口：[桌面、信息与交互设计](interaction-contract.md)。** [资格来源](../../sources/materials/M-2026-11-01-tabletop-backpack-information.md)保留限定确认与固定原文。 本页只保留意图、确认摘要与实际阅读范围，不再平行维护布局正文。

## 输入意图与确认摘要

用户要求沿已选Ways画风调整桌面空间与信息层级，将法器生产区转为背包空间。先做设计、批量确认后形成可审阅方案，不改玩法或主工程，不启动玩法实验。

2026-11-01已确认：

- Q1—Q3：上方五列牌局、中下背包、底部两组持牌，右侧计数；各阶段区域固定，仅调整突出程度；背包采用桌上展开的收纳垫，边界清楚、格位柔和。
- Q4—Q5的原则：主页面文字尽量少，常驻信息以图形UI体现，细节逐步披露；取消短纸签，优先通过鼠标和快捷键主动查看。
- Q6：1920×1080设计基准，后续核对1366×768可读性，底部持牌方向沿用。尺寸目标已确认，实际检查尚未执行。
- Q8—Q9：左键选择／规则允许的操作、拖动移动；右键或详情快捷键查看，Escape返回；拖动中右键优先取消。关键准确数字常驻；法器进度图形化，精确剩余拍主动查看。
- Q7：获准补读下列两份变更中的空间、装配、待料／补料及阶段权限相关段落，不沿链接扩读。已完成授权范围阅读。

尚未选定：进度具体形状、关系显隐方式、详情窗口形态、快捷键具体字母。用户的轮廓倒计时只是示例，`I`也仅为候选。缺少实际背包尺寸、对象占形、接口及压力状态输入；不从图像或旧实现反推这些规则。

资格确认使用grill-with-docs，按本项目批量澄清约定执行。设计对象、玩家情境、可见行为与价值、现行设计关系、未知及下一步已在正式素材中覆盖；资格通过只意味着该呈现素材可引用，不等于整套未定细节被采纳，也不改变规则状态。资格前候选与提问可按固定提交[5b6b007原页](https://github.com/dsaj4/game_design/blob/5b6b0072d39a3752957e5ec8147cbf7ee7ce3ba1/yanzhou/sources/inbox/2026-10-31-tabletop-backpack-information.md)取证。

## 实际阅读范围

模式CUSTOM，共同游戏背景版本 **d4daf2d35a549fce4916aae38aa28aa28110a21b**。实际使用的受控背景材料与该版本无差异；后续提交不自动扩大阅读范围。2026-11-01的两项增补读取时亦与该共同版本一致。

已读游戏材料：

- `yanzhou/visual/README.md`：全文。
- `yanzhou/visual/baseline-2026-10-26/README.md`：全文。
- `yanzhou/exploration/DIR-042-herbal-engraving-style/README.md`：§2026-10-28底部持牌与语言细节更新（含其阅读记录）、§本轮采用什么、§与现行规则的边界。
- `yanzhou/development/README.md`：开头当前状态、§新2D开工交接、§当前事实。
- `yanzhou/development/card-motion-2026-10-29.md`：全文。
- `yanzhou/visual/first-battle-handflow-2026-10-28/README.md`：全文。
- `yanzhou/visual/card-frame-2026-10-31/complete-v02/README.md`：全文。
- `yanzhou/visual/alchemy-apparatus-2026-10-31/ways-v10/README.md`：全文。
- `yanzhou/development/development-standard.md`：仅§9。
- 本次增补`yanzhou/sources/draft-changes/D-2026-10-31-backpack-production.md`：§新增规则、§替换／合并／淘汰中空间、待料／补料与阶段权限相关内容，§保留疑问与证据边界。
- 本次增补`yanzhou/sources/draft-changes/D-2026-10-31-spatial-auxiliaries.md`：§新增与替换中占格、接口、核心装配、批次及身份保存相关内容，§采纳理由与边界。

必要操作规则：根及项目AGENTS、探索start／AGENTS、设计流程、共享模板入口、原始想法与合格素材模板、Git协作规范及全局grill-with-docs。两份增补是采纳差异摘要；未沿链接读取现行细则，不声称完整规则审查。

外部输入：

- 临时交接：`C:/Users/Administrator/AppData/Local/Temp/codex-handoffs/2026-10-31-yanzhou-tabletop-information-handoff.md`，只作导航与边界入口。
- 用户指定[背包乱斗分析参考](<E:/Game/Backpack Battles-analysis/2026-10-31/inventory-ui-v01/index.html>)，已按文本完整读取；BACKPACK-UI-01／AS-SH-007，SHA-256 `161ab327aa56cf43fbc8ac27ff8bb3d9f3000cfd236b8fa4cea9b54b468d89df`。只取位置状态、容量边界、作用关系与短反馈的职责分离，不套用格数、容量或运行行为。

本轮没有读取参考图像、其他方向、历史、完整GDD或外部实现代码，没有执行HTML脚本。既有未提交修改不作为本轮输入，不清理或覆盖。

## 本次交付边界

正式素材包含已确认方向、具体信息宿主建议、关键情境预期、来源与未决项。只形成文字审阅稿；HTML、美术效果、主工程、浏览器／引擎／真人验证均未开展。后续依文字→HTML→美术效果→真实实现顺序推进，不能把本次文字审阅当成后续阶段通过。
