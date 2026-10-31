# 炼金法器 · 古朴器形重设计

2026-10-31 · game-002 / main · **AS-G002-036 / ALCHEMY-APPARATUS-07**。

**[查看新器形及四版切换](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/archaic-form-v07/preview.html)**。D为本轮候选；[A·粗线简洁](../README.md)、[B·精线古朴](../antique-v05/README.md)、[C·Culdcept器物画法](../culdcept-v06/README.md)继续保留。

用户本轮要求器形也重新设计，更加古朴、减少拟真感；因此解除06版的旧轮廓约束，重新从文字生成两件完整器物。沿用简洁、低细节量与中央安静表面的要求，古朴感来自厚重比例、手制边缘与土色，不依赖附加装饰。

| 原件 | 器形与画法变化 | 实际规格 |
| --- | --- | --- |
| [平炼釜](refining-kettle-archaic-v01.png) | 无足、宽肩略方腹，厚陶口沿与小片状双耳；去掉金属光泽，改用深褐哑光色面 | 1536×1024 RGBA透明PNG |
| [白化曲颈瓶](albedo-retort-archaic-v01.png) | 饱满圆腹、短折颈，去掉颈部套环；米白与灰绿大块明暗 | 1225×1284 RGBA透明PNG |

两件均不加铭文、雕刻、裂纹、附属器件或特效。前表面保留低干扰区域，供后续独立铭文表现；这两张是完整静态主体，本轮不制作分体、发光动画或绑定。

## 生成与保存

内置image_gen两次全新文字生图，**本轮没有图像参考输入**，避免继续锁定旧器形。提示词仍沿上一版的Culdcept BEGINS手绘器物方向，强调不透明色块、经济的轮廓线、少量明暗层次与非拟真表现；不重新输入第三方图像。[平炼釜提示词](prompts/refining-kettle.txt)、[曲颈瓶提示词](prompts/albedo-retort.txt)及[generation](generation.json)保存准确调用文字与原生成路径。

PNG从工具输出逐字节复制；无程序图像编辑、裁切、抠图、改色或缩放。预览只对完整源图作运行时缩放定位。[manifest](manifest.json)固定原图SHA、尺寸、alpha、预览文件和检查证据。图片与独立预览本机保管，说明、提示词和清单入Git。

## 检查与边界

A／B／C前三版61个登记文件按原SHA校验，保持原字节。实际浏览器460×871视口已核四版切换、四版对照、浅纸／深色／暖灰木色透明合成、剪影及224／64／96／160px显示，无横向溢出。新釜宽扁与瓶颈转折在小图仍可辨；64px釜耳孔较小。[检查记录](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/archaic-form-v07/browser-qa.json)与[当前画面](E:/Project/yanzhou-ui-prototypes/alchemy-apparatus-2026-10-31/archaic-form-v07/evidence/05-current-d.png)保存于独立预览目录。

ReadyForScope / PresentLocal仅限本机美术、文件和预览检查；D造型与风格接受为PendingReview。CUSTOM输入为`9e7762168610ca7a1731de32ab2238a8bda07522`的既有三版与用户本轮要求，不扩读玩法，不改配方、占格、供料接口或核心兼容；未进行背包场景、引擎或玩法测试。复用仅限项目内部审阅；后续工程集成另定范围。
