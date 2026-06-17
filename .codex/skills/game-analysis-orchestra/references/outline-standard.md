# Outline Standard

The outline is the control artifact. Write it before drafting the dossier.

## Required Outputs

Generate both:

- `outline/outline.md`
- `outline/outline.json`

## JSON Shape

Use this shape:

```json
{
  "game_name": "",
  "slug": "",
  "scope": "",
  "target_questions": [],
  "thesis": "",
  "evidence_map": [],
  "modules": [
    {
      "id": "module-3",
      "title": "核心玩法循环",
      "claim": "",
      "evidence": [],
      "open_questions": [],
      "write_priority": "high"
    }
  ],
  "diagrams": [
    {
      "type": "core_loop",
      "module": "module-3",
      "purpose": ""
    }
  ]
}
```

## Outline Requirements

- Include all eight modules, even if some are marked material-insufficient.
- State one overall thesis.
- State each module claim in one or two sentences.
- Assign evidence to modules.
- Mark module 3 and module 4 as `high` priority.
- Include at least two diagram plans:
  - `core_loop` for module 3.
  - `system_relation` for module 4.

## Eight Modules

1. 游戏核心定位、基础信息、商业大盘复盘。
2. 全局玩家体验与底层设计目标。
3. 核心玩法循环。
4. 全链路游戏架构拆解。
5. 内容与关卡体系。
6. 数值体系与经济资源闭环。
7. 叙事体系、角色 IP 与视听包装。
8. 优劣复盘与可落地优化方案。
