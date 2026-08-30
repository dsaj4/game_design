import json
from pathlib import Path
import subprocess
import sys

import pytest

from semantic_card_engine.embedding_cache import (
    DEFAULT_MODEL_ID,
    DEFAULT_MODEL_REVISION,
    EmbeddingCacheError,
    build_embedding_texts,
    load_embedding_cache,
)
from semantic_card_engine.experiment import (
    build_experiment_inputs,
    load_experiment_config,
    run_comparison,
)


EXPERIMENT_PATH = Path(__file__).parents[1] / "data" / "experiment.json"
CACHE_PATH = EXPERIMENT_PATH.with_name("embedding-cache.json")
ALL_ROUTES = [
    "discrete_dynamics",
    "manual_vector_role_aware",
    "embedding_weighted",
    "embedding_role_aware",
    "embedding_structured",
]
MAPPED_ROUTES = [route for route in ALL_ROUTES if route != "embedding_weighted"]


@pytest.fixture(scope="module")
def config():
    return load_experiment_config(EXPERIMENT_PATH)


@pytest.fixture(scope="module")
def embedding_cache(config):
    return load_embedding_cache(CACHE_PATH, config)


@pytest.fixture(scope="module")
def report(config, embedding_cache):
    return run_comparison(config, embedding_cache)


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


def test_structured_embedding_texts_do_not_contain_effect_answers(config):
    texts = build_embedding_texts(config)
    structured_texts = [
        text for entry_id, text in texts.items() if entry_id.startswith("structured:")
    ]

    assert len(texts) == 78
    assert len(structured_texts) == 48
    assert all(
        effect_op not in text
        for text in structured_texts
        for effect_op in config.effect_ops
    )


def test_embedding_cache_is_pinned_and_complete(embedding_cache):
    assert embedding_cache.model_id == DEFAULT_MODEL_ID
    assert embedding_cache.model_revision == DEFAULT_MODEL_REVISION
    assert embedding_cache.model_license == "apache-2.0"
    assert embedding_cache.dimension == 384
    assert len(embedding_cache.entries) == 78
    assert embedding_cache.digest == (
        "22251a4cd31e9d4eb186fe2b36013fed02bcec4464bad5946d311345dd49070c"
    )


def test_tampered_embedding_cache_is_rejected(config, tmp_path):
    payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    payload["entries"]["effect:damage"]["vector"][0] += 0.1
    tampered_path = tmp_path / "embedding-cache.json"
    tampered_path.write_text(
        json.dumps(payload, ensure_ascii=False),
        encoding="utf-8",
        newline="\n",
    )

    with pytest.raises(EmbeddingCacheError, match="digest"):
        load_embedding_cache(tampered_path, config)


def test_comparison_is_deterministic(config, embedding_cache):
    first = run_comparison(config, embedding_cache)
    second = run_comparison(config, embedding_cache)

    assert first == second
    assert first["digest"] == second["digest"]
    assert (
        first["routes"]["discrete_dynamics"]["result_digest"]
        != first["routes"]["manual_vector_role_aware"]["result_digest"]
    )
    discrete_inputs = [
        result["input"]
        for result in first["routes"]["discrete_dynamics"]["results"]
    ]
    embedding_inputs = [
        result["input"]
        for result in first["routes"]["embedding_structured"]["results"]
    ]
    assert discrete_inputs == embedding_inputs
    assert first["embedding_cache"]["digest"] == embedding_cache.digest


def test_learned_route_outcomes_are_frozen(report):
    summaries = {
        route: payload["summary"] for route, payload in report["routes"].items()
    }

    assert summaries["embedding_weighted"]["mapped"] == 0
    assert summaries["embedding_weighted"]["rejection_reasons"] == {
        "no_legal_region": 48
    }
    assert summaries["embedding_role_aware"]["mapped"] == 32
    assert summaries["embedding_structured"]["mapped"] == 38


@pytest.mark.parametrize(
    "route",
    ALL_ROUTES,
)
def test_every_route_returns_one_result_per_input(report, route):
    route_report = report["routes"][route]
    results = route_report["results"]
    summary = route_report["summary"]

    assert len(results) == report["input_count"] == 48
    assert summary["mapped"] + summary["unmapped"] == 48
    assert summary["unmapped"] > 0
    assert sum(summary["rejection_reasons"].values()) == summary["unmapped"]


@pytest.mark.parametrize(
    "route",
    MAPPED_ROUTES,
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
    ALL_ROUTES,
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
    assert "OK version=semantic-physics-exp-002-v1 inputs=48" in result.stdout
    assert payload["schema_version"] == "semantic-physics-comparison-v1"
    assert set(payload["routes"]) == set(ALL_ROUTES)
    assert all(len(route["results"]) == 48 for route in payload["routes"].values())


def test_compare_cli_requires_cache_unless_manual_only(tmp_path):
    missing_cache = tmp_path / "missing-cache.json"
    failed = subprocess.run(
        [
            sys.executable,
            "-m",
            "semantic_card_engine",
            "compare",
            "--embedding-cache",
            str(missing_cache),
        ],
        cwd=EXPERIMENT_PATH.parents[1],
        capture_output=True,
        check=False,
        encoding="utf-8",
    )
    manual = subprocess.run(
        [
            sys.executable,
            "-m",
            "semantic_card_engine",
            "compare",
            "--embedding-cache",
            str(missing_cache),
            "--manual-only",
            "--output",
            str(tmp_path / "manual.json"),
        ],
        cwd=EXPERIMENT_PATH.parents[1],
        capture_output=True,
        check=True,
        encoding="utf-8",
    )

    assert failed.returncode == 2
    assert "No such file" in failed.stderr
    assert "OK version=semantic-physics-exp-002-v1 inputs=48" in manual.stdout
