---
name: worldbuilding
description: "Diagnose world-level story problems. This skill should be used when settings feel thin, institutions feel designed rather than evolved, economies don't make sense, or non-human species feel like humans in costume. Keywords: worldbuilding, setting, world, institutions, economy, culture, species, consequences."
license: MIT
metadata:
  upstream_compatibility: Works with any fiction genre. Pairs with story-sense for routing.
  author: jwynia
  version: "1.0"
  type: diagnostic
  mode: diagnostic
  domain: worldbuilding
---

## 言咒项目适配（优先于下方上游流程）

本技能安装于game设计仓库。先遵守根及言咒AGENTS、[READ-1](../../../yanzhou/exploration/start.md)、[设计流程](../../../docs/design-workflow.md)和当前任务材料范围，再选择下面真正有用的方法。用于检查世界、制度、经济和文化的内部关系；诊断建议仍是工作意见，不直接晋级正式素材。

- 世界、语言、虚构历史、人物、势力、文献视角与背景故事归[worldbuilding](../../../yanzhou/worldbuilding/README.md)；新输入与研究先留所属sources／方向。具体物件、配方和玩家可见物件文案只在内容库维护，规则仍归design，项目history不存虚构年表。
- 已确认设定、Raw候选、作者暂拟真相、人物信念与Unknown分开；推荐不等于确认，用户已定事项不重问。需要选择时按项目批量澄清约定成组给出推荐及影响。
- 上游的输出发现、自动建库与文件命名为通用参考；已有项目路径直接使用，不创建context/output-config.md、.conlang-output.md、world-bible、第二套问题库或平行模板树，不因上游链接扩读游戏材料。
- 上游关联技能和领域代理列表是方法建议，不自动安装相邻技能、派生会话或启动代理；仅沿当前用户与AGC-1的实际授权分工。安装全组不要求每次调用全组，不为填满参数表补造世界事实。
- 附带脚本和数据完整保留为上游资源；本次安装未执行脚本、安装Deno或下载运行依赖。后续确需执行时按实际任务确定输入、输出和权限，核对远程依赖；不从叙事写作推导测试、游戏运行或自动改规则的授权。
- 静态一致性、人工边界演练、模型输出质量与玩家体验分别记录，未验证保持Hypothesis／NotRun。

原始入口见[上游原文](references/upstream-skill.md)，来源及哈希见source-lock.json；下文保留上游完整方法，冲突时以上述适配与项目约定为准。


# Worldbuilding: Diagnostic Skill

Diagnose world-level problems in fictional settings. Identify what's missing or unconvincing and recommend specific interventions.

## When to Use This Skill

Use this skill when:
- Setting feels like a painted backdrop
- Technology/magic hasn't transformed society
- Institutions feel designed rather than evolved
- Economy doesn't make sense
- Cultures lack depth

Do NOT use this skill when:
- Story problems are character-focused (use character-arc)
- Plot structure issues (use scene-sequencing)
- Need to generate worlds from scratch (use systemic-worldbuilding)

## Core Principle

**Worlds fail when they feel designed rather than evolved.**

Good worldbuilding creates the perception that the setting has history, internal logic, and processes that operate independently of the plot.

## The World States

### W1: Backdrop World
**Symptoms:** Setting exists but has no independent logic
**Interventions:** systemic-worldbuilding (trace consequences)

### W2: World Without Consequences
**Symptoms:** Technology/magic exists but hasn't transformed society
**Interventions:** Consequence Cascade Analysis

### W3: Institutions Without History
**Symptoms:** Organizations feel designed last week
**Interventions:** Organic Institutional Design

### W4: Economy Doesn't Make Sense
**Symptoms:** Trade exists without supply chains; prices arbitrary
**Interventions:** economic-systems

### W5: Belief Systems Are Shallow
**Symptoms:** Religion is flavor without theological depth
**Interventions:** belief-systems

### W6: Culture Without Depth
**Symptoms:** Traditions feel random; surface-level aesthetic
**Interventions:** memetic-depth

### W7: Flat Non-Humans
**Symptoms:** Aliens/species are humans in costume
**Interventions:** conlang, alien-sensory frameworks

### W7.5: Language Feels Generic
**Symptoms:** Names sound like English; no linguistic texture
**Interventions:** conlang, language-evolution

## Consequence Cascade

Apply to any major speculative element:

```
Initial Element
├── 1st Order: Direct practical effects
│   ├── Who gains immediate advantage?
│   ├── What becomes obsolete?
│   └── Technical limitations?
├── 2nd Order: Systemic adaptations
│   ├── How do economic structures adapt?
│   ├── How do power structures respond?
│   └── What resistance movements arise?
└── 3rd Order: Cultural evolution
    ├── What new language emerges?
    ├── What ethical questions arise?
    └── What becomes normalized?
```

## Key Diagnostic Questions

### For Technology/Magic
- What's your initial divergence from our world?
- Who gains power? What becomes obsolete?
- How would the powerful try to control this?

### For Institutions
- When was this organization founded?
- What crises has it survived?
- What are its internal contradictions?

### For Economics
- What's the fundamental scarcity?
- How is value determined?
- What's the underground economy?

### For Belief Systems
- What explains existence?
- How do beliefs affect daily decisions?
- What are the schisms and debates?

## Common Anti-Patterns

### The Monoculture
One unified culture for entire planets/species.
**Fix:** Add regional variation, class differences, schisms.

### The Convenient Technology
Technology exists when plot needs it.
**Fix:** Trace consequence cascade.

### The Static History
World unchanged for centuries.
**Fix:** Add recent disruptions, reforms in progress.

### The Evil Empire
Antagonist nation uniformly evil.
**Fix:** Add internal debates, ordinary people.

### The Rubber Forehead Alien
Non-humans with minor cosmetic differences.
**Fix:** Start with biology, trace to cognition, trace to culture.

## Depth vs Breadth

**Go Deep When:**
- Element is central to plot
- Element will be examined closely
- Element creates ongoing conflict

**Stay Shallow When:**
- Element is background detail
- POV character wouldn't know depth
- Mystery is more interesting

## Related Skills

- **systemic-worldbuilding** - Build worlds from initial divergence
- **belief-systems** - Deep theological design
- **economic-systems** - Economic logic
- **governance-systems** - Political structures
- **conlang** - Language design
- **settlement-design** - Cities and geography
