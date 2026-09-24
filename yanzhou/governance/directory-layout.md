# 目录结构与文件放置规范

修订：layout.1 / 2026-09-23。依据用户明确要求新建yanzhou并重新设计文件结构。Project ID保持game-002，优化Project ID保持game-002-optimization。

```text
yanzhou/
├── README.md                    阅读入口
├── AGENTS.md                    实际路径映射及权限
├── CONTEXT.md                   术语
├── design/                      唯一现行规格
│   ├── GDD.md / core-concept.md / baseline.md
│   ├── systems/                 七个系统，各自维护规则
│   ├── content/                 词卡、法杖、敌人与遭遇
│   └── parameters.md / validation.md / source-review.md
├── sources/                     设计形成过程
│   ├── inbox/ / materials/ / proposals/ / evaluations/
│   ├── draft-changes/ / gdd-drafts/
│   └── supporting/              其他原设计流程记录
├── effects/entries/              FX身份及追踪
├── exploration/optimization/    独立候选、比较、固定背景和运行
├── development/                 外部实现索引与实际证据
│   ├── reports/ / inputs/
│   └── test-handoff.md / calibration-method.md
├── visual/reviews/              视觉评审、图像与来源
├── governance/                  问题、决策、规范、编号、迁移清单
└── history/                     历史，不覆盖现行规则
    ├── pre-organization/        整理前全文，保留原目录层级追溯
    ├── audits/                  旧日期审查与记录
    └── reorganizations/         以往整理报告及原始清单
```

## 放在哪里

| 内容 | 放置方式 |
| --- | --- |
| 修改当前机制细则 | 经采纳后更新design对应唯一正文；原因记决策与Draft Change |
| 一个尚未明确的新想法 | 主系统sources/inbox或明确选定的探索项目本地idea-inbox |
| 提出替代主循环 | exploration/optimization；独立方向及比较，不写进现行GDD |
| 设计预期和验收条件 | design/validation.md及对应规则页 |
| 测试已经运行的事实 | development/reports，附版本、输入、失败和覆盖边界 |
| 实现进度、技术资产 | development索引；具体代码留在外部仓库 |
| 视觉方案与图片 | visual/reviews/日期，附方案状态和来源；不是规则权限 |
| 旧规则、旧审查、旧来源哈希 | history或原来源记录；标明原日期和适用范围 |

## 命名与路径

现行职责页使用稳定名称；历史/来源用日期和既有M/P/E/D/FX/DIR ID。新GDD草案使用日期命名，不在design中增建第二套“最新版本”。中文标题用于阅读，路径沿英文小写与连字符。相对链接按真实目录解析；固定提交里的旧路径按原提交解释，不能全局替换历史manifest字段。

共享模板、通用知识、独立肉鸽及旧游戏仍在仓库根各自目录。本目录是言咒项目组织入口，不声称是包含所有共享依赖和实现代码的独立仓库。

旧路径兼容页只导航；冻结包、机器来源记录、媒体以及已有未提交修改作为明确例外保留旧地址，具体见迁移报告。新写入统一使用本目录；两个遗留未提交素材由原修改任务决定如何同步，不在迁移中替用户采纳。
