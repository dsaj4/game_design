# 言咒工作台使用入口

2026-10-18 · game-002。工作台位于`E:/Project/yanzhou-workspace`，连接设计、既有Godot工程和原位资产。双击该目录的`Start Yanzhou Workspace.cmd`启动；本轮不自动重启正在工作的应用。

## 日常只看两个入口

- **言咒项目卡**：当前工作、规范与循环、开发地图、审阅与资产、使用与接手入口。它帮助找产物和解释进度。
- **顶部“言咒 · 开发工作台”面板**：查看真实路径／Git状态、按白名单只读查规范、准备执行合同。会话调度和产物完成是两件事。

当前先做主系统完善准备，旧3D重复组件页已删除，历史原文只按固定Git取证。新的2D工程还没有建立，面板现有代码／资产连接仍指向既有3D探索工程。

## 信息放在哪里

| 信息 | 唯一维护处 | 在工作台怎样查 |
| --- | --- | --- |
| 当前实现与版本 | [开发状态](README.md) | 顶部文档“开发索引” |
| 操作规范与制作循环 | [开发规范](development-standard.md)、[循环规格](iteration-spec.md) | 顶部对应文档；项目卡提供读法 |
| 开放设计问题 | [questions](../governance/questions.md) | 本轮允许后打开指定原文，不复制成工作台待决表 |
| 资产身份与使用条件 | [AS／DM目录](../../docs/registry/demo-assets.md)及原件说明 | 目录定位，再用Files看原件／预览；不复制资产 |
| 每轮产物与审阅结论 | 所属设计页、代码协调记录或治理报告 | 项目卡关联本轮记录；执行合同只负责会话与所有权 |
| 代码、构建与技术报告 | Godot或以后选定的实现仓库 | Files或所属仓库入口 |

操作与开发文档白名单由`projects/yanzhou/project.json`明确列出；新增规范不自动授权读取全部design、sources、历史或其他方向。CORE／GDD／FULL先展开确切文件，再准备CUSTOM合同。

## 读懂状态

`prepared`是准备合同，`active`是会话打开，`closed`是结束合同并释放所有权；不等于制作完成或验收通过。卡片`done`也只关闭工作项。长期结论必须有所属仓库记录、固定版本和检查范围。

工作台现有能力、应展示的字段、手工登记步骤与尚未实现的自动化见[展示规格](workbench-spec.md)。具体安装和本机合同操作见[工作台说明](E:/Project/yanzhou-workspace/docs/yanzhou-integration.md)与[使用与接手](E:/Project/yanzhou-workspace/workspace/2026-10-14_yanzhou/usage.md)。

工作台自身目前只有上游remote，无用户自有remote；本轮文档接入保留本地提交，不向上游发送用户资料。
