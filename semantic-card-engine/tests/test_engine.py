from pathlib import Path
import subprocess
import sys

import pytest

from semantic_card_engine.engine import (
    GenerationError,
    generate_card,
    load_catalog,
)


CATALOG_PATH = Path(__file__).parents[1] / "data" / "catalog.json"


@pytest.fixture(scope="module")
def catalog():
    return load_catalog(CATALOG_PATH)


def test_same_input_is_reproducible(catalog):
    first = generate_card(catalog, ["water"], ["compress"], "neutral")
    second = generate_card(catalog, ["water"], ["compress"], "neutral")

    assert first == second
    assert first["effects"] == [{"op": "damage", "target": "enemy", "value": 6}]
    assert first["cost"] == 2


def test_material_order_does_not_change_the_card(catalog):
    first = generate_card(catalog, ["fire", "air"], [], "neutral")
    second = generate_card(catalog, ["air", "fire"], [], "neutral")

    assert first == second


def test_core_lens_redirects_effect_without_changing_budget(catalog):
    neutral = generate_card(catalog, ["water"], ["compress"], "neutral")
    crown = generate_card(catalog, ["water"], ["compress"], "crown")

    assert neutral["effects"][0]["op"] == "damage"
    assert crown["effects"][0]["op"] == "shield"
    assert sum(effect["value"] for effect in neutral["effects"]) == 6
    assert sum(effect["value"] for effect in crown["effects"]) == 6
    assert crown["provenance"]["applied_lenses"] == ["crown_pressure_guard"]


def test_repeated_materials_increase_budget_but_keep_semantics(catalog):
    one_water = generate_card(catalog, ["water"], ["compress"], "neutral")
    two_waters = generate_card(
        catalog,
        ["water", "water"],
        ["compress"],
        "neutral",
    )

    assert one_water["traits"] == two_waters["traits"]
    assert two_waters["provenance"]["budget"] == 10
    assert two_waters["effects"][0]["value"] == 10


def test_multiple_effects_conserve_the_budget(catalog):
    card = generate_card(
        catalog,
        ["water", "light"],
        ["disperse"],
        "neutral",
    )

    assert card["effects"] == [
        {"op": "heal", "target": "self", "value": 5},
        {"op": "shield", "target": "self", "value": 4},
    ]
    assert sum(effect["value"] for effect in card["effects"]) == 9


def test_cli_emits_utf8_json():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "semantic_card_engine",
            "generate",
            "--concept",
            "water",
            "--action",
            "compress",
        ],
        cwd=CATALOG_PATH.parents[1],
        capture_output=True,
        check=True,
        encoding="utf-8",
    )

    assert '"name": "高压流"' in result.stdout


@pytest.mark.parametrize(
    ("concepts", "actions", "error"),
    [
        (["unknown"], [], "unknown concept"),
        ([], ["compress"], "at least one concept"),
        (["sand"], ["disperse"], "no semantic law"),
    ],
)
def test_invalid_generation_requests_are_rejected(catalog, concepts, actions, error):
    with pytest.raises(GenerationError, match=error):
        generate_card(catalog, concepts, actions, "neutral")
