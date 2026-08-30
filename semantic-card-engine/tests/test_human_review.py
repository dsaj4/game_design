import csv
from copy import deepcopy
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

import pytest

from semantic_card_engine.experiment import load_experiment_config
from semantic_card_engine.human_review import (
    ACTION_CONTRAST_FILE,
    BLIND_KEY_FILE,
    GUIDE_FILE,
    PREDICTION_FILE,
    SEMANTIC_FIT_FILE,
    HumanReviewError,
    build_review_pack,
)


ROOT = Path(__file__).parents[1]
EXPERIMENT_PATH = ROOT / "data" / "experiment.json"
REPORT_PATH = ROOT / "reports" / "semantic-physics-exp-002-v1.json"
PUBLIC_FILES = [
    PREDICTION_FILE,
    SEMANTIC_FIT_FILE,
    ACTION_CONTRAST_FILE,
    GUIDE_FILE,
]


def _csv_rows(content):
    return list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))


def test_review_pack_is_deterministic_and_has_expected_sizes():
    config = load_experiment_config(EXPERIMENT_PATH)
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    first = build_review_pack(report, config, seed=20260830)
    second = build_review_pack(report, config, seed=20260830)

    assert first == second
    assert len(_csv_rows(first[PREDICTION_FILE])) == 48
    assert len(_csv_rows(first[SEMANTIC_FIT_FILE])) == 240
    assert len(_csv_rows(first[ACTION_CONTRAST_FILE])) == 80
    assert first[PREDICTION_FILE].startswith(b"\xef\xbb\xbf")


def test_public_review_files_do_not_leak_route_names():
    config = load_experiment_config(EXPERIMENT_PATH)
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    files = build_review_pack(report, config, seed=20260830)

    public_text = b"\n".join(files[name] for name in PUBLIC_FILES).decode(
        "utf-8-sig"
    )
    assert all(route not in public_text for route in report["routes"])
    assert "effect_scores" not in public_text
    assert "projection_distance" not in public_text
    assert "model_id" not in public_text


def test_review_pack_rejects_a_tampered_source_report():
    config = load_experiment_config(EXPERIMENT_PATH)
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    tampered = deepcopy(report)
    tampered["routes"]["discrete_dynamics"]["results"][0]["status"] = "unmapped"

    with pytest.raises(HumanReviewError, match="digest"):
        build_review_pack(tampered, config, seed=20260830)


def test_blind_key_is_bijective_and_authenticates_public_files():
    config = load_experiment_config(EXPERIMENT_PATH)
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    files = build_review_pack(report, config, seed=20260830)
    key = json.loads(files[BLIND_KEY_FILE].decode("utf-8"))

    semantic_pairs = {
        (
            item["route"],
            item["input"]["concept_id"],
            item["input"]["action_id"],
            item["input"]["core_id"],
        )
        for item in key["semantic_samples"]
    }
    action_groups = {
        (item["route"], item["concept_id"], item["core_id"])
        for item in key["action_groups"]
    }

    assert len(semantic_pairs) == 240
    assert len(action_groups) == 80
    assert len(key["prediction_samples"]) == 48
    for name in PUBLIC_FILES:
        assert key["public_file_sha256"][name] == hashlib.sha256(
            files[name]
        ).hexdigest()


def test_review_pack_cli_writes_files_and_refuses_accidental_overwrite(tmp_path):
    output_dir = tmp_path / "review"
    command = [
        sys.executable,
        "-m",
        "semantic_card_engine",
        "build-review-pack",
        "--output-dir",
        str(output_dir),
    ]

    created = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        check=True,
        encoding="utf-8",
    )
    repeated = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        check=False,
        encoding="utf-8",
    )

    assert "files=5 seed=20260830" in created.stdout
    assert set(path.name for path in output_dir.iterdir()) == {
        *PUBLIC_FILES,
        BLIND_KEY_FILE,
    }
    assert repeated.returncode == 2
    assert "review files already exist" in repeated.stderr
