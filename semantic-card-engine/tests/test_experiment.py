import json
from pathlib import Path
import subprocess
import sys

import pytest

from semantic_card_engine.experiment import (
    build_experiment_inputs,
    load_experiment_config,
    run_comparison,
)


EXPERIMENT_PATH = Path(__file__).parents[1] / "data" / "experiment.json"


@pytest.fixture(scope="module")
def config():
    return load_experiment_config(EXPERIMENT_PATH)


@pytest.fixture(scope="module")
def report(config):
    return run_comparison(config)


def test_experiment_builds_the_shared_48_input_set(config):
    inputs = build_experiment_inputs(config)

    assert len(inputs) == 48
    assert len(set(inputs)) == 48
    assert inputs == tuple(sorted(inputs))


def test_experiment_catalog_contains_no_combination_answers():
    payload = json.loads(EXPERIMENT_PATH.read_text(encoding="utf-8"))

    assert "recipes" not in payload
    assert "combinations" not in payload
    assert all("effect" not in item for item in payload["concepts"])
    assert all("effect" not in item for item in payload["actions"])
    assert all("effect" not in item for item in payload["cores"])


def test_comparison_is_deterministic(config):
    first = run_comparison(config)
    second = run_comparison(config)

    assert first == second
    assert first["digest"] == second["digest"]
    assert (
        first["routes"]["discrete_dynamics"]["result_digest"]
        != first["routes"]["embedding_role_aware"]["result_digest"]
    )
    discrete_inputs = [
        result["input"]
        for result in first["routes"]["discrete_dynamics"]["results"]
    ]
    embedding_inputs = [
        result["input"]
        for result in first["routes"]["embedding_role_aware"]["results"]
    ]
    assert discrete_inputs == embedding_inputs


@pytest.mark.parametrize(
    "route",
    ["discrete_dynamics", "embedding_role_aware"],
)
def test_every_route_returns_one_result_per_input(report, route):
    route_report = report["routes"][route]
    results = route_report["results"]
    summary = route_report["summary"]

    assert len(results) == report["input_count"] == 48
    assert summary["mapped"] + summary["unmapped"] == 48
    assert summary["unmapped"] > 0
    assert summary["rejection_reasons"]["capacity_exhausted"] > 0


@pytest.mark.parametrize(
    "route",
    ["discrete_dynamics", "embedding_role_aware"],
)
def test_mapped_cards_obey_effect_and_budget_constraints(config, report, route):
    compatible_pairs = {
        frozenset(pair) for pair in config.region_policy.pair_capacities
    }
    mapped = [
        result
        for result in report["routes"][route]["results"]
        if result["status"] == "mapped"
    ]

    assert mapped
    assert any(len(result["card"]["effects"]) == 2 for result in mapped)
    for result in mapped:
        effects = result["card"]["effects"]
        budget = result["card"]["provenance"]["budget"]
        assert 1 <= len(effects) <= 2
        assert sum(effect["value"] for effect in effects) == budget
        if len(effects) == 2:
            assert frozenset(effect["op"] for effect in effects) in compatible_pairs


@pytest.mark.parametrize(
    "route",
    ["discrete_dynamics", "embedding_role_aware"],
)
def test_region_capacity_and_projection_evidence_are_preserved(config, report, route):
    summary = report["routes"][route]["summary"]
    for region_id, occupancy in summary["region_occupancy"].items():
        assert occupancy <= summary["region_capacities"][region_id]

    for result in report["routes"][route]["results"]:
        assert result["candidate"]["vector"]
        assert result["candidate"]["effect_scores"]
        if result["status"] == "unmapped":
            assert result["assignment"]["rejection_reason"] in {
                "capacity_exhausted",
                "no_legal_region",
            }
            continue
        assert result["assignment"]["projected_point"]
        assert (
            result["assignment"]["projection_distance"]
            <= config.region_policy.maximum_projection_distance
        )


def test_compare_cli_writes_the_full_utf8_report(tmp_path):
    output_path = tmp_path / "comparison.json"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "semantic_card_engine",
            "compare",
            "--output",
            str(output_path),
        ],
        cwd=EXPERIMENT_PATH.parents[1],
        capture_output=True,
        check=True,
        encoding="utf-8",
    )

    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert "OK version=semantic-physics-exp-002-v0 inputs=48" in result.stdout
    assert payload["schema_version"] == "semantic-physics-comparison-v0"
    assert len(payload["routes"]["discrete_dynamics"]["results"]) == 48
    assert len(payload["routes"]["embedding_role_aware"]["results"]) == 48
