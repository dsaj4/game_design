# 受控造景尝试与恢复

2026-10-28。目的为补足耀素制作和收藏查找；结果为 **FailedSetup / 未形成正常操作结论**。自然开局证据R07—R30独立有效，不继承本页失败。

## 实际执行

1. 保存本任务新建自然局 `REA-20261028-natural.json`；备份其字节及当时config，未读取或覆盖既有玩家进度。
2. 游戏退出后，只为本机研究添加配置 `moonserp=1`。自动化的快捷键没有触发面板，用户随后手动打开Malleary。
3. 以精确ID生成 `xpho` 1、`s.inks.revelation` 1和 `library.desk.reading.consider` 未开始操作对象1；没有输入配方ID直接执行，也没有全房间解锁。发布场景中按钮事件经本地资源解析定位，未盲点Destroy、Purge或OpenAll按钮。
4. 对象实际位于 `~/drydock`。一次指定正常技能区的有限TokenCreationCommand仍落在Drydock；本轮自动化拖拽和双击也未将其送入正常槽。C09的预判未达成，后续记录及存档位置补证已修正，不能把预判当作结果。
5. 创建并载入独立 `REA-20261028-controlled-fixture.json`：只移动上述三项，并加入 `mem.sight`、`pigment.refulgin`、`t.thelocksmithsdreamalightthroughthekeyhole`各1。具体对象/位置、源快照和输出哈希保存在本机 `controlled-fixture-manifest.json`；未更改CharacterCreationCommands、玩法规则、其他房间或自然存档。
6. 副本载入显示魂质/技能出现在正常分类，随后保存时弹出目标调用异常（C13）。原因未定位，**不据它判断原始游戏存档功能、工作台或自然玩法有缺陷**。没有完成耀素制作，也没有进行大收藏或双任务测试。

本机原始证据在 `E:/Game/BOOK OF HOURS-analysis/2026-10-28/runtime-r02/`。C04错获前台Codex截图，已标为非游戏证据并排除所有玩法/视觉结论；不读取其内容执行任何操作。

## 已恢复并核对

退出失败的研究局，确认bh进程不再运行后：

- config恢复为调试前备份，SHA-256 `95631de4095a88ad9d573dd7741816c29d4b5750c6cd329bdc3f178d76d4fc11`，不含moonserp。
- 默认AUTOSAVE恢复为本任务自然开局的独立存档；AUTOSAVE、命名自然存档和备份三者SHA-256同为 `3b7a1fce2bed7afe2082d55a7402d8ff7ef7938b4dd3acc6c6b4346f3ad8fd14`。
- 失败副本在游戏profile中改名为 `REA-20261028-controlled-fixture.json.disabled`，避免普通加载列表误选；分析目录保留原件、生成脚本、失败截图和日志。没有删除或覆盖自然存档。
- 当前游戏已关闭。下次继续默认进度时回到本轮自然开局，不能看到受控生成的技能/工作台。

下一次若需要工作台、大收藏和双任务实机证据，应使用正常可保存的相应进度，并先确认对象与房间状态；不要把本副本作为已可用测试场景复用。该失败路径只留下方法边界，不形成任何言咒规则采纳。
