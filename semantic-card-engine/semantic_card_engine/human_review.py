from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
import random

from .experiment import ExperimentConfig, ExperimentInput, build_experiment_inputs


REVIEW_SCHEMA_VERSION = "semantic-physics-human-review-v0"
PREDICTION_FILE = "01-prediction.csv"
SEMANTIC_FIT_FILE = "02-semantic-fit.csv"
ACTION_CONTRAST_FILE = "03-action-contrast.csv"
GUIDE_FILE = "README.md"
BLIND_KEY_FILE = "private-blind-key.json"

EFFECT_LABELS = {
    "damage": "伤害",
    "shield": "护盾",
    "heal": "治疗",
    "cancel_intent": "打断意图",
}


class HumanReviewError(ValueError):
    pass


def build_review_pack(
    report: dict[str, object],
    config: ExperimentConfig,
    seed: int,
) -> dict[str, bytes]:
    routes = _validate_report(report, config)
    rng = random.Random(seed)

    prediction_items = list(build_experiment_inputs(config))
    rng.shuffle(prediction_items)
    prediction_rows: list[dict[str, object]] = []
    prediction_key: list[dict[str, object]] = []
    for index, item in enumerate(prediction_items, start=1):
        sample_id = f"P{index:03d}"
        prediction_rows.append(
            {
                "样本ID": sample_id,
                "评审批次": _block(index, 16),
                **_input_labels(config, item),
                "预测效果1": "",
                "预测效果2（可空）": "",
                "是否应拒绝生成（是/否）": "",
                "预测信心（1-5）": "",
                "理由": "",
                "评审者ID": "",
            }
        )
        prediction_key.append({"sample_id": sample_id, "input": _input_dict(item)})

    semantic_items = [
        (route, result)
        for route in routes
        for result in sorted(
            report["routes"][route]["results"],
            key=lambda value: _input_key(value["input"]),
        )
    ]
    rng.shuffle(semantic_items)
    semantic_rows: list[dict[str, object]] = []
    semantic_key: list[dict[str, object]] = []
    for index, (route, result) in enumerate(semantic_items, start=1):
        item = _parse_input(result["input"])
        sample_id = f"S{index:03d}"
        semantic_rows.append(
            {
                "样本ID": sample_id,
                "评审批次": _block(index, 40),
                **_input_labels(config, item),
                "候选结果": _outcome_label(result),
                "语义符合度（1-5）": "",
                "动作贡献度（1-5）": "",
                "核心卡一致性（1-5）": "",
                "无需规则说明可理解（1-5）": "",
                "拒绝是否恰当（是/否/不适用）": "",
                "备注": "",
                "评审者ID": "",
            }
        )
        semantic_key.append(
            {
                "sample_id": sample_id,
                "route": route,
                "input": _input_dict(item),
                "status": result["status"],
            }
        )

    action_items = [
        (route, concept_id, core_id)
        for route in routes
        for concept_id in sorted(config.concepts)
        for core_id in sorted(config.cores)
    ]
    rng.shuffle(action_items)
    route_results = {
        route: {
            _input_key(result["input"]): result
            for result in report["routes"][route]["results"]
        }
        for route in routes
    }
    action_rows: list[dict[str, object]] = []
    action_key: list[dict[str, object]] = []
    ordered_action_ids = sorted(config.actions)
    for index, (route, concept_id, core_id) in enumerate(action_items, start=1):
        group_id = f"A{index:03d}"
        row: dict[str, object] = {
            "组ID": group_id,
            "评审批次": _block(index, 20),
            "概念": config.concepts[concept_id].name,
            "核心卡": config.cores[core_id].name,
        }
        for action_index, action_id in enumerate(ordered_action_ids, start=1):
            key = (concept_id, action_id, core_id)
            row[f"动作{action_index}"] = config.actions[action_id].name
            row[f"动作{action_index}候选结果"] = _outcome_label(
                route_results[route][key]
            )
        row.update(
            {
                "动作区分度（1-5）": "",
                "差异是否可预测（是/否）": "",
                "最符合语义的动作": "",
                "备注": "",
                "评审者ID": "",
            }
        )
        action_rows.append(row)
        action_key.append(
            {
                "group_id": group_id,
                "route": route,
                "concept_id": concept_id,
                "core_id": core_id,
                "action_ids": ordered_action_ids,
            }
        )

    public_files = {
        PREDICTION_FILE: _csv_bytes(prediction_rows),
        SEMANTIC_FIT_FILE: _csv_bytes(semantic_rows),
        ACTION_CONTRAST_FILE: _csv_bytes(action_rows),
        GUIDE_FILE: _guide_bytes(config, report),
    }
    public_text = b"\n".join(public_files.values()).decode("utf-8-sig")
    leaked_routes = [route for route in routes if route in public_text]
    if leaked_routes:
        raise HumanReviewError(
            "public review files expose route identities: "
            + ", ".join(leaked_routes)
        )
    key_payload: dict[str, object] = {
        "schema_version": REVIEW_SCHEMA_VERSION,
        "source_report": {
            "schema_version": report["schema_version"],
            "experiment_version": report["experiment_version"],
            "digest": report["digest"],
        },
        "seed": seed,
        "public_file_sha256": {
            name: hashlib.sha256(content).hexdigest()
            for name, content in sorted(public_files.items())
        },
        "prediction_samples": prediction_key,
        "semantic_samples": semantic_key,
        "action_groups": action_key,
    }
    key_payload["digest"] = hashlib.sha256(_canonical_json(key_payload)).hexdigest()
    return {
        **public_files,
        BLIND_KEY_FILE: (
            json.dumps(key_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8"),
    }


def write_review_pack(
    output_dir: Path | str,
    files: dict[str, bytes],
    *,
    overwrite: bool = False,
) -> None:
    output_path = Path(output_dir)
    existing = [name for name in files if (output_path / name).exists()]
    if existing and not overwrite:
        raise HumanReviewError(
            "review files already exist; use --overwrite only before reviewers add data: "
            + ", ".join(sorted(existing))
        )
    output_path.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (output_path / name).write_bytes(content)


def _validate_report(
    report: dict[str, object], config: ExperimentConfig
) -> tuple[str, ...]:
    if report.get("schema_version") != "semantic-physics-comparison-v1":
        raise HumanReviewError("review generation requires a V1 comparison report")
    if report.get("experiment_version") != config.version:
        raise HumanReviewError("report and experiment versions do not match")
    report_digest = report.get("digest")
    digest_payload = {key: value for key, value in report.items() if key != "digest"}
    if report_digest != hashlib.sha256(_canonical_json(digest_payload)).hexdigest():
        raise HumanReviewError("comparison report digest does not match its content")
    routes_payload = report.get("routes")
    if not isinstance(routes_payload, dict) or not routes_payload:
        raise HumanReviewError("comparison report contains no routes")

    expected_inputs = {
        (item.concept_id, item.action_id, item.core_id)
        for item in build_experiment_inputs(config)
    }
    for route, payload in routes_payload.items():
        results = payload.get("results") if isinstance(payload, dict) else None
        if not isinstance(results, list):
            raise HumanReviewError(f"route {route} contains no result list")
        result_inputs = {_input_key(result.get("input")) for result in results}
        if result_inputs != expected_inputs or len(results) != len(expected_inputs):
            raise HumanReviewError(f"route {route} does not cover every input once")
        for result in results:
            _outcome_label(result)
    return tuple(sorted(str(route) for route in routes_payload))


def _input_labels(
    config: ExperimentConfig, item: ExperimentInput
) -> dict[str, str]:
    return {
        "概念": config.concepts[item.concept_id].name,
        "动作": config.actions[item.action_id].name,
        "核心卡": config.cores[item.core_id].name,
    }


def _outcome_label(result: dict[str, object]) -> str:
    status = result.get("status")
    if status == "unmapped":
        return "拒绝生成"
    if status != "mapped":
        raise HumanReviewError(f"unsupported result status: {status}")
    card = result.get("card")
    effects = card.get("effects") if isinstance(card, dict) else None
    if not isinstance(effects, list) or not 1 <= len(effects) <= 2:
        raise HumanReviewError("mapped result must contain one or two effects")
    labels: list[str] = []
    for effect in effects:
        effect_op = effect.get("op") if isinstance(effect, dict) else None
        if effect_op not in EFFECT_LABELS:
            raise HumanReviewError(f"unsupported effect operation: {effect_op}")
        labels.append(f"{EFFECT_LABELS[effect_op]}（{effect_op}）")
    return " + ".join(labels)


def _parse_input(value: object) -> ExperimentInput:
    if not isinstance(value, dict):
        raise HumanReviewError("result input must be an object")
    return ExperimentInput(
        concept_id=str(value.get("concept_id", "")),
        action_id=str(value.get("action_id", "")),
        core_id=str(value.get("core_id", "")),
    )


def _input_key(value: object) -> tuple[str, str, str]:
    item = _parse_input(value)
    return item.concept_id, item.action_id, item.core_id


def _input_dict(item: ExperimentInput) -> dict[str, str]:
    return {
        "concept_id": item.concept_id,
        "action_id": item.action_id,
        "core_id": item.core_id,
    }


def _block(index: int, size: int) -> int:
    return ((index - 1) // size) + 1


def _csv_bytes(rows: list[dict[str, object]]) -> bytes:
    if not rows:
        raise HumanReviewError("review table cannot be empty")
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8-sig")


def _guide_bytes(config: ExperimentConfig, report: dict[str, object]) -> bytes:
    effect_options = "、".join(
        f"`{effect_op}`（{EFFECT_LABELS[effect_op]}）"
        for effect_op in config.effect_ops
    )
    text = f"""# EXP-002 V1 盲态人工评审

本目录用于判断候选效果是否符合人类语义直觉。公开表已隐藏生成路线、模型、相似度、向量、效果区域和数值预算。

来源报告摘要：`{report['digest']}`。

## 评审顺序

1. 只打开 `01-prediction.csv`。根据“概念 + 动作 + 核心卡”预测最多两个效果，或选择应拒绝生成。可用效果：{effect_options}。
2. 完成预测后再打开 `02-semantic-fit.csv`。不要返回修改预测。对已生成候选填写四项 1-5 分；对“拒绝生成”只填写拒绝是否恰当和备注。
3. 最后打开 `03-action-contrast.csv`。比较相同概念与核心卡在三个动作下的匿名结果，判断动作是否产生清晰、可预测的差异。
4. 全部评审完成前不要打开 `private-blind-key.json`，也不要查看原始 V1 报告。

## 评分锚点

- `1`：明显冲突或无法解释。
- `2`：牵强，需要额外设定才能成立。
- `3`：可以接受，但不是自然联想。
- `4`：大体自然，少量解释即可理解。
- `5`：高度自然，几乎可由输入直接预测。

预测效果请填写英文操作码；第二效果允许留空。每个评审者使用固定的匿名 `评审者ID`。建议每完成一个评审批次就休息，避免后半段疲劳显著影响评分。

## 文件规模

- `01-prediction.csv`：48 条唯一输入。
- `02-semantic-fit.csv`：240 条匿名候选。
- `03-action-contrast.csv`：80 组动作对照。
- `private-blind-key.json`：路线解盲与完整性校验，只由实验负责人保管。
"""
    return text.encode("utf-8")


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
