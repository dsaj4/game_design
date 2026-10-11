# v04：3D界面轮廓占位

2026-10-11。用户补充：“该示意图只用于模拟UI形态和位置，真实UI会是3d的；只进行轮廓描位”。本版替代v03作为当前结构评审入口，收敛为整张牌桌的轮廓图。

- [打开HTML](C:/Users/Administrator/.codex/visualizations/2026/10/11/01a12b3f-545d-7672-8512-7579183a1c80/battle-ui-html-v04/index.html) · [本轮本机预览](http://127.0.0.1:8784/)。
- [预览图](C:/Users/Administrator/.codex/visualizations/2026/10/11/01a12b3f-545d-7672-8512-7579183a1c80/battle-ui-html-v04/preview-1920.png) · [使用与检查说明](C:/Users/Administrator/.codex/visualizations/2026/10/11/01a12b3f-545d-7672-8512-7579183a1c80/battle-ui-html-v04/README.md)。
- [固定版本清单](C:/Users/Administrator/.codex/visualizations/2026/10/11/01a12b3f-545d-7672-8512-7579183a1c80/battle-ui-html-v04/manifest.json) · [浏览器检查记录](C:/Users/Administrator/.codex/visualizations/2026/10/11/01a12b3f-545d-7672-8512-7579183a1c80/battle-ui-html-v04/verification.json)。

保留牌桌透视轮廓、上方敌方主体、下方己方主体、上下行动牌列、右上状态牌、左下法器托盘、右下主操作区。实线描物件，虚线表示空位和对齐辅助线；上下同列代表同一刻，空位不挤掉。七个刻位、两件法器仅用于描位，不限定最终可见数量。移除v03的数值、案例、详情、规则解释及所有交互；固定构图等比缩放。

DM-G002-010 / BATTLE-UI-HTML-04，game-002 / main；ReadyForScope（轮廓位置评审）/ PresentLocal。自制HTML内联矢量线框，无第三方库或嵌入图像。uses: AS-G002-005@v02（对齐结构）、AS-G002-006（构图参照，原图未导入）；同一DM迭代，无外部代码派生。可在本项目改作，对外分发许可未另定。仍是第一步视觉候选，未进入美术设计、建模或玩法验证，规则输入未扩读或修改。

2026-10-11实际用Edge检查1920、1366、736宽度、两排同刻中心对齐、六个空位、HTTP及离线显示，无交互控件、脚本错误或页面横向溢出；目视检查1920、1366预览。代码与证据保存在上述本机持久目录，未公开发布。[v03原交付与检查](v03-html.md)保持原版本含义，原件与manifest未覆盖。
