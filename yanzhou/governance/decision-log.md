# 决策与编号

2026-10-23 · DecisionRecord。这里只记决定摘要及替代关系；现行行为查[核心与细则](rule-index.md)，版本查[baseline](../design/baseline.md)，实现查[开发入口](../development/README.md)。设计采纳不等于实现或体验通过。

## 编号与别名

新增前查本表及所属登记，不复用退役ID；日期／主题型来源沿原路径识别，不另造同义编号。

| 身份 | 使用范围／下一编号 |
| --- | --- |
| G002-CORE | 001—064已用；下一065。001—036按原版本保留，仅由048等明确条款限定继承 |
| G002-DOC | 001—030已用；下一031。下表含本轮030 |
| EX | 001／002已用，下一003；案例身份不等于发行实体或FX |
| TL／验收 | TL-01—19、21—45共44个现行身份，20退役；TL-V01—110去除02／20，加INS-V01—09共117项既有预期，另有CORE合同情境 |
| FX／SYS | FX-001—137沿effects登记；SYS-001—007保留原规格域身份，不按六系统重新分号 |
| DIR／AS／DM | DIR按[探索入口](../exploration/README.md)分配，001—036退役；资产和Demo沿[统一目录](../../docs/registry/demo-assets.md)，这里不重复维护计数 |
| 其他旧身份 | ADMIN-001、SCOPE-001—004、BF-001、AUD-001—040及R／GR／RC／BR／ST／CG／HG／WG／SG／PG／EG／RG／UX、V／AC／U／TH／CAL／DEMO05保留原范围；旧卡W／EN／B／C与退役TC／TR／TS／TA／TE不作为当前发行池 |

别名只修当前引用，原来源不改：2026-09-13 BR12的DOC-002＝DOC-004，2026-09-12效果登记仍为DOC-002；2026-10-08铭文／辅槽分支（固定提交`51257ba5e00b0cae155940c11251134dffd6db69`）的DOC-016＝DOC-018，敌人整理仍为DOC-016。RC1的55个流派ID对应53实体，其中护甲S2-N02＝E3-N05，引爆S2-V04＝E3-V06。

## 核心决定

以下为已采纳范围摘要。旧CORE-001—036及ADMIN／SCOPE／BF的原日期、资格与细节按[历史完整决定](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/decision-log.md#2026-09早期决定历史索引)追溯；BF草案、旧候选和历史实验不因收录晋级。旧RC1未解决的AUD-010只保留历史范围，不冒充现行TL-11缺口或已验证结论。

CORE-037—047共同依据：[时间产线采纳D](../sources/draft-changes/D-2026-10-01-timeline-production-core.md)。

| ID | 决定及当前关系 |
| --- | --- |
| <a id="g002-core-037"></a>CORE-037 | 时间产线、自动运行、有限队列与敌牌倒计时；生产耗时后由051—053替代。 |
| <a id="g002-core-038"></a>CORE-038 | 以卡牌重做战场；仅明确打断中断指定法器，普通伤害不再全杖打断。 |
| <a id="g002-core-039"></a>CORE-039 | 重设计发行卡表；旧53实体不作为新版默认池。 |
| <a id="g002-core-040"></a>CORE-040 | 恢复最近结清状态及已提交操作；正常退出／暂停现按064。 |
| <a id="g002-core-041"></a>CORE-041 | 原材料—动作—目标入口由049铭刻替代；实体铭文与耗材分账保留。 |
| <a id="g002-core-042"></a>CORE-042 | 高阶产物维护不足休眠、保留增幅，补料后恢复。 |
| <a id="g002-core-043"></a>CORE-043 | 无合法目标空放离队，不退制造成本、不补发。 |
| <a id="g002-core-044"></a>CORE-044 | 维护优先、战前序为默认供料／入行序；临时供料与预留后由050—053细化。 |
| <a id="g002-core-045"></a>CORE-045 | 保留递增疲劳；EX-002参数由060限定，跨构筑曲线仍待定。 |
| <a id="g002-core-046"></a>CORE-046 | 部分资源与高阶产物可跨战，拒绝全部清空。 |
| <a id="g002-core-047"></a>CORE-047 | 按携带标签及容量选留，保留数量、重置运行状态；材料身份／阶级由058补齐。 |

| ID | 决定及当前关系 | 依据 |
| --- | --- | --- |
| <a id="g002-core-048"></a>CORE-048 | 兼容复用实体、绑定、支付、路线经济与保存；不恢复旧卡池、格子或冷却。 | [D](../sources/draft-changes/D-2026-10-01-compatible-rules-reuse.md) |
| <a id="g002-core-049"></a>CORE-049 | 核心必填、预设辅槽、法器统一产行动卡；替代041自由构句入口及直接资源交付。 | [D](../sources/draft-changes/D-2026-10-04-artifact-inscription-core.md) |
| <a id="g002-core-050"></a>CORE-050 | 所有敌牌延时；临时供料只影响未来未承诺批次，不开放当前加工暂停／改速。 | [D](../sources/draft-changes/D-2026-10-04-routing-response-clarification.md) |
| <a id="g002-core-051"></a>CORE-051 | 唯一处理D、开工联合检查并预留容量；取消J／R／S、独立冷却及完工等位。 | [D](../sources/draft-changes/D-2026-10-05-single-processing-time.md) |
| <a id="g002-core-052"></a>CORE-052 | 预留不排牌序；回收最早下拍复用、入行最早下拍行动；只保留一份临时方案。 | [D](../sources/draft-changes/D-2026-10-05-production-queue-interfaces.md) |
| <a id="g002-core-053"></a>CORE-053 | 共同拍序、幸存完工及拍末统一开工；独立空位可支持中断后当拍重开。 | [D](../sources/draft-changes/D-2026-10-05-stage-one-common-timing.md) |
| <a id="g002-core-054"></a>CORE-054 | 揭示时锁定最长剩余加工法器；固定敌循环、单一来源敌人、通用类别与公开边界。 | [D](../sources/draft-changes/D-2026-10-05-stage-two-enemy-pressure.md) |
| <a id="g002-core-055"></a>CORE-055 | 冻结本批D及必要标记；资源／标记锁住不自动花，解锁恢复消费资格；不撤回已承诺投入。 | [D](../sources/draft-changes/D-2026-10-08-batch-freeze-consumption-lock.md) |
| <a id="g002-core-056"></a>CORE-056 | D先固定增减、有效倍率连乘，最终向上取整且最低1拍；已启用付费效果不因取整免单。 | [D](../sources/draft-changes/D-2026-10-08-processing-time-formula.md) |
| <a id="g002-core-057"></a>CORE-057 | 五阶段与组内定时→敌→玩家；逐完整事件检查终局；定时、维护、冻结失效及恢复总序闭合。 | [D](../sources/draft-changes/D-2026-10-08-settlement-order-reference.md) |
| <a id="g002-core-058"></a>CORE-058 | 资源身份／性质／阶级、基础加工、背包投入与选留；普通耗材未完工退回、已完工不退。 | [D](../sources/draft-changes/D-2026-10-09-resource-system-design.md) |
| <a id="g002-core-059"></a>CORE-059 | 明示零材料、有限固定未来用途及EX-001首批案例；不新增启停、重铭或全局数值。 | [D](../sources/draft-changes/D-2026-10-11-simple-spell-example.md) |
| <a id="g002-core-060"></a>CORE-060 | EX-002独立完整单战、疲劳与首场操作；内容参数保留，暂停／单步停点由064替代。 | [D](../sources/draft-changes/D-2026-10-11-development-design-round-01.md) |
| <a id="g002-core-061"></a>CORE-061 | 首场音画与恢复基础合同；取消未完动画、静态跳步及第04轮相关解释已由064替代。 | [D](../sources/draft-changes/D-2026-10-12-development-design-round-03.md) |
| <a id="g002-core-062"></a>CORE-062 | OS失焦后返回仍停，保留输入与页面状态；旧事件边界停点由064替代。 | [D](../sources/draft-changes/D-2026-10-12-development-design-round-05.md) |
| <a id="g002-core-063"></a>CORE-063 | 旧首场以真实3D物件操作；physical-table.2允许绑定只读文本和公开投影动作。停点沿064，新2D宿主仍待定。 | [D](../sources/draft-changes/D-2026-10-14-demoncards-presentation.md) |
| <a id="g002-core-064"></a>CORE-064 | 所有暂停完成当前拍及动画后停，单步同样停拍末；终局不补步骤，异常载入不自动补跑。 | [D](../sources/draft-changes/D-2026-10-23-beat-end-pause.md) |

## 文档与开发决定

DOC-001—029的原授权、日期、输入和证据范围见[固定完整记录](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/decision-log.md)，按ID检索；下表保留决定和仍影响工作的替代关系。具体操作规范由所归属正文维护，不在决策中再抄一遍。

| ID | 决定及当前关系 |
| --- | --- |
| <a id="g002-doc-001"></a>DOC-001 | 既有设计文档统一；原快照与采纳边界固定保留。 |
| <a id="g002-doc-002"></a>DOC-002 | 跨系统FX身份及效果追踪；登记不等于采纳具体效果。 |
| <a id="g002-doc-003"></a>DOC-003 | 旧RC1全游戏GDD交接；其GDD-2成熟度不继承给后续TL-1。 |
| <a id="g002-doc-004"></a>DOC-004 | BR12：实际内容与参数先成套再写GDD；修复旧DOC-002重号。 |
| <a id="g002-doc-005"></a>DOC-005 | 主系统与探索文档整理、职责及来源统一。 |
| <a id="g002-doc-006"></a>DOC-006 | 建立yanzhou独立目录；旧兼容树后由009退役。 |
| <a id="g002-doc-007"></a>DOC-007 | 探索按方向README组织，不生成空流程目录。 |
| <a id="g002-doc-008"></a>DOC-008 | 建立核心摘要与READ-1阅读模式；核心正文入口现沿028。 |
| <a id="g002-doc-009"></a>DOC-009 | 清理旧兼容目录与重复快照，固定Git取证；旧docs.py已退役。 |
| <a id="g002-doc-010"></a>DOC-010 | DIR-001—036退役，指定采纳来源迁移；不回收编号或改历史资格。 |
| <a id="g002-doc-011"></a>DOC-011 | 主系统一致性复核、旧效果正文退役；遗留风险归当前questions。 |
| <a id="g002-doc-012"></a>DOC-012 | 规则、理由、体验分职责；不要求机械拆成独立文件，现沿028／029。 |
| <a id="g002-doc-013"></a>DOC-013 | 六主系统、两子系统和三个公共流程的归属。 |
| <a id="g002-doc-014"></a>DOC-014 | 行动框架与独立示例；当时五文件要求已由028改为按需拆分，Qualified不整体升级。 |
| <a id="g002-doc-015"></a>DOC-015 | 法器框架整理，保留规则资格及未采纳边界。 |
| <a id="g002-doc-016"></a>DOC-016 | 敌人框架整理；铭文分支的同号决定映射018。 |
| <a id="g002-doc-017"></a>DOC-017 | 重建后一致性审查；已解决接口与尚待验证风险分开。 |
| <a id="g002-doc-018"></a>DOC-018 | 铭文／辅槽分支DOC-016映射为018，原来源不改号。 |
| <a id="g002-doc-019"></a>DOC-019 | 系统设计指导集成，相关框架仍Qualified，不采纳指导稿所有示例。 |
| <a id="g002-doc-020"></a>DOC-020 | 集中首批案例与开发阅读；现行读取结构由028接续。 |
| <a id="g002-doc-021"></a>DOC-021 | 正式开发规范、阶段与资产准备；双引擎比较排程由022替代。 |
| <a id="g002-doc-022"></a>DOC-022 | 用户确定Godot工程；Unity未实测，不能宣称比较优势；新2D工程关系另定。 |
| <a id="g002-doc-023"></a>DOC-023 | 旧3D成品Demo任务分解；历史DQ状态不复制成新方向完成度。 |
| <a id="g002-doc-024"></a>DOC-024 | 开发遇到设计取舍暂停批次，专人对接，必要采纳落地并复核后恢复。 |
| <a id="g002-doc-025"></a>DOC-025 | 重点交互按文字→HTML→效果→真实实现推进，设计责任连续。 |
| <a id="g002-doc-026"></a>DOC-026 | 先闭合首场核心再做同游戏2D；小修改复用已确认产物，旧3D证据保留。 |
| <a id="g002-doc-027"></a>DOC-027 | 输入记摘要、版本共用、引用准确、验收分预期和实证；不保存逐字原话。 |
| <a id="g002-doc-028"></a>DOC-028 | 唯一核心＋按需细则＋任务设计包＋对话审阅；默认5份启动，按影响人工审校。 |
| <a id="g002-doc-029"></a>DOC-029 | 复杂细则去重、过期纠正、未用扩展按需展开；保留既有锁定／承诺后果。 |

<a id="g002-doc-030"></a>

## DOC-030 治理目录精简

2026-10-23 · Accepted / Documentation。用户确认治理精简方案并要求执行。共同输入版本为`ccf3544c1d93372f05b726610a0a3a637efb0ae0`；本轮仅管理文档，不改GDD 2.7、玩法、案例数值或实验状态。

治理收束为README、文档合同、行为索引、问题、决策与编号、协作六项职责。目录／文件导航合并，编号归本页；问题页只维护未决及体验风险，已闭合项查本页与正式来源。内容检查归内容合同，独有制作失败经验归开发规范；完整旧报告、输入附件、清理记录按[历史版本](../history/README.md#治理历史)取证，不新增清理映射或过程报告。

只保留决定摘要、必要来源和替代关系；原话与逐轮审查统计退出现用治理正文。已提交历史保留原状态与恢复线索，原有未提交探索修改及用户删除不纳入本轮。
