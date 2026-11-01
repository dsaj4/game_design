# 历史与来源取证

Project ID：game-002。文档角色：HistoricalNavigation。2026-11-01更新；各历史批次按自己的固定版本解释。

原文档清理基准提交：`d44ecd04840b434b171d26f601bafbd87c311c92`。历史的“当前”、未决项、操作口令与资格仅按其原日期有效。现行规则读[design](../design/README.md)，不要恢复整套旧目录来开展新工作。

<a id="legacy-implementations-2026-11-01"></a>

## 2026-11-01 旧3D与早期Demo统一恢复

用户明确授权删除旧3D及其他分散旧言咒。共同设计取证提交为`5b6b0072d39a3752957e5ec8147cbf7ee7ce3ba1`。删除范围仅为原`E:/Project/`下的`yanzhou-godot`、`yanzhou-godot-baselines`、`yanzhou-pixel-lab`、`yanzhou-tl1-demo`、`yanzhou-alchemy-atlas`、`yanzhou-battle-3d`和`game-002-godogen-lab`；当前二维工程、设计仓库、现用美术、UI原型、公共研究与工作台继续保留。此管理决定不改玩法或历史验收结论。

唯一恢复位置：[恢复说明](E:/Project/game-retired-2026-11-01/README.md)，归档`legacy-yanzhou.tar.gz`与`manifest.json`同目录保管。完整保存本地Git、原包、失败证据、ignored／未跟踪文件及Godogen未提交的`art/e1/e1-r2-master.blend`；每个普通文件经归档字节与删除前源文件SHA-256一致性核对，目录链接仅保留链接本身、不跟随读取或删除外部目标。总量、归档SHA及各仓库完整HEAD以该manifest为准，不另建逐项去向表。恢复包只在本机，不提交或上传。

固定恢复包：36,923个普通文件、源字节21,912,529,822；归档16,893,803,824字节，SHA-256 `96501c86e273a33891fd8e9b8c777715bdecef8c8a1f65d086258d12abce5eed`。16个历史目录链接仅作为链接保存，原目标不纳入递归删除。

旧3D工程HEAD为`c7d861c3b88b887eb638e3797be2dbf7a9245886`；原接手与失败总结位于归档内`yanzhou-godot/docs/development-handoff.md`，更早合并依据为其Git提交`cc8c229fe89d85a51e739efc0111a54d139fff1a`。原0.4运行`9c50458a56a38f0c6ebd001d9e6a3ef34382adaa`、B07组合`e0077ffa10d22ad1c9dd91e8037aa2c021409098`、B13运行`e975de8bdbbe70591d4099c34b799e76c4bff1d7`及其manifest、报告和技术ADR均随原Git与文件保留；旧登记的原路径须先恢复再访问。

继续有效的独有经验：B07正式600秒测量出现113.127ms尖峰Fail，507.172秒与116.001秒中断不能拼成通过；30秒或预加载诊断不能代替长测。B13只证明限定资产适配／检视，不证明OS实体输入、完整新单战、听感或视觉接受；原UE Shader／Blueprint／Niagara未完整移植，FuncCardBack用途及第三方再分发条件仍Unknown。源几何、材质可编辑性和引擎呈现须分开检查；运行过曝、透明排序、中文行高及真实点击几何先在发生层修复。更具体的恢复游标、资产生命周期、PCM与工具误判经验保留于归档接手正文，不外推为新2D已验证。共通制作规范仍在[开发规范](../development/development-standard.md#制作与验证经验)。

当前二维需要的两字体／OFL已独立保留，Godot工具迁出到二维工程ignored目录；工作台连接同步二维路径。仅做字节、依赖、文档和路径核对，未启动旧Demo或新玩法实验。

## 治理历史

2026-10-23精简前的[完整治理目录](https://github.com/dsaj4/game_design/tree/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance)保留旧决策、编号、审查复盘、清理报告与输入附件，包含原来源及仓库外恢复线索。按原文件名／章节取证，不再复制历史目录或维护清理映射。当前职责见[治理入口](../governance/README.md)。

旧报告的Open、停点、数量、测试命令和“下一步”只代表原日期；当前未决查questions，采纳与替代查decision-log，执行状态查开发入口。现用制作经验已归开发规范，旧失败与NotRun不因精简改成通过。

## 本地保留

- [已完成的P/E/D记录](accepted-design-records/README.md)：六组已采纳设计的18份过程资料；原始输入和正式素材继续在sources。
- [探索原始构思](exploration-2026-09-24/idea-inbox/)、[局部合格素材](exploration-2026-09-24/idea-materials/)、[研究](exploration-2026-09-24/insights/)、[运行记录](exploration-2026-09-24/runs/)与[旧问题](exploration-2026-09-24/questions/)。保留独有内容，不重新解释为当前待办。
- [冻结背景包](exploration-2026-09-24/context/baseline-2026-09-09-001/context-pack.md)及manifest原字节不改。历史包的相对路径按原提交解释；本地旧路径已移除时用该提交读取，不自行改写SHA或扩展材料范围。

## 已退出工作树的快照

| 资料 | 固定版本入口 |
| --- | --- |
| 整理前GDD、核心和FX全文 | [原快照](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/pre-organization) |
| 旧审查 | [审查记录](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/audits) |
| 重复方向页与旧登记 | [方向快照](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/history/exploration-2026-09-24/directions) |
| layout.1与layout.2迁移映射 | [第一次映射](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/path-map.json) · [第二次映射](https://github.com/dsaj4/game_design/blob/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/exploration-path-map.json) |
| 时间轴详细定位、哈希和覆盖快照 | [原审查附件](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/yanzhou/governance/time-axis-review) |
| 旧兼容目录 | [workspaces](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/workspaces) · [optimization](https://github.com/dsaj4/game_design/tree/d44ecd04840b434b171d26f601bafbd87c311c92/exploration/game-002-optimization) |

无需联网或恢复文件也可用`git show <提交>:<原路径>`读取；目录用`git ls-tree -r <提交> -- <目录>`查找。用户仍需授权相应历史范围，Git取证不绕过READ-1。

保留的旧探索历史正文按上述清理基准提交或文件自身更早来源解释。其本地副本字节冻结，相对链接可能指向已退役快照；沿固定提交查看即可保留完整引用语境。活动文档的链接已经改到现用位置或固定版本，不以失效本地兼容页作为入口。

[本轮处理清单](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/cleanup-map.json) · [清理报告](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/cleanup-report.md)


## 2026-10-04退役探索

DIR-001至DIR-036已退出活动工作树，未新增一套本地历史正文。已提交方向、比较表、独有失败记录与原确认按固定提交`e6f3dab4c2d7947d842f4f120cbb8c61ceef86a9`及原路径取证；DIR-035与其他未提交内容按[清理报告](https://github.com/dsaj4/game_design/blob/ccf3544c1d93372f05b726610a0a3a637efb0ae0/yanzhou/governance/cleanup-report.md#2026-10-04探索方向退役)的仓库外恢复位置取证。原资格和版本范围保持原义，读取历史仍须纳入当轮材料范围。
