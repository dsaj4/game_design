# 《言咒》核心构思入口

Project ID：game-002。文档角色：Navigation。Core Concept v0.16；基准GDD 2.1 / TL-1 + INS-1 / processing.2 + timing.2 + enemy.1 + commitment.1 + time-formula.1 + resource.1；2026-10-09。

玩家战前在法器上补齐名词／动词暗句的核心铭文，选择辅槽修饰与基础供料；战中开工预留有限容量，仅经历处理耗时、完成即入行，经普通队列兑现，面对揭示后的倒计时威胁作有限调整。

[核心设计浓缩](core-design.md) · [GDD](GDD.md) · [版本与来源](baseline.md) · [当前问题](../governance/questions.md)

已采纳结构与主辅槽铭刻，证据仍Hypothesis / NotRun；具体卡效、材料映射、打造成本及契合形式尚未定。详见[CORE-049](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md)。

[CORE-051](../sources/draft-changes/D-2026-10-05-single-processing-time.md)简化生产时间：D≥1整数拍，取消J／R／独立周期／冷却／S；无位在开工前等待。[CORE-052](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md)补齐容量预留不排牌序、按有效供料优先级开工、中断回收下拍可用、入行最早下拍翻开及单份临时供料到期恢复；该轮完整总序未定，现见CORE-057。

[CORE-053](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md)确认拍末一次开工、a+D完工、正常空位当拍复用、揭示后观察提交及基础补给下拍可用。阶段一文档完成；复杂效果、真实内容与体验仍待后续阶段。

[CORE-054](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md)确定敌程序固定时间表与翻开表公开、打断锁定剩余最长施法、单一来源敌人死亡即胜、敌我共用四类卡面种类；首批敌人仍为候选。

当前局部采纳：[CORE-055 / commitment.1](../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md)，开工冻结D与应付标记、完工扣除、打断释放下拍可用；消费前预警和玩家指定数量锁定。其他Qualified框架不整包升级，通用总序后由CORE-057补齐，具体生命周期仍待补齐，NotRun。

[CORE-056 / time-formula.1](../sources/draft-changes/D-2026-10-08-processing-time-formula.md)已补齐D的固定增减、有效倍率连乘、最终向上取整和最低1拍；取整无进一步缩短不自动免除已声明费用。通用总序后由CORE-057补齐，具体内容与剩余生命周期仍待定，GDD-0／NotRun不变。

[CORE-057 / timing.2](../sources/draft-changes/D-2026-10-08-settlement-order-reference.md)已确认同拍总序、复合步骤、定时与维护、逐事件终局及恢复合同；通用顺序已定，具体内容／生命周期缺口仍按当前问题处理，GDD-0／NotRun不变。

[CORE-058 / resource.1](../sources/draft-changes/D-2026-10-09-resource-system-design.md)采纳资源职责与通用边界：材料性质／阶级、无铭文基础加工、转化／兑现、背包投入与统一选留，以及公开取材和常态自动运行目标。具体流派与参数延期，体验仍NotRun。
