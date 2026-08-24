from pathlib import Path

from combat_lab.catalog import load_catalog
from combat_lab.matcher import matches_requirements


DATA_DIR = Path(__file__).parents[1] / "data"


def cards(catalog, *card_ids):
    return [catalog.auxiliary_cards[card_id] for card_id in card_ids]


def test_three_sheep_requires_three_distinct_cards() -> None:
    catalog = load_catalog(DATA_DIR)
    combo = catalog.combo("sheep_core", "three_sheep_blessing")

    assert matches_requirements(
        cards(catalog, "lamb_charge", "wool_guard", "pasture_bell"),
        combo.requirements,
    )
    assert not matches_requirements(
        cards(catalog, "lamb_charge", "wool_guard"),
        combo.requirements,
    )


def test_multifield_card_fills_only_one_requirement_slot() -> None:
    catalog = load_catalog(DATA_DIR)
    combo = catalog.combo("sheep_core", "mend_after_loss")

    assert not matches_requirements(
        cards(catalog, "broken_fence_horn", "wool_guard"),
        combo.requirements,
    )
    assert matches_requirements(
        cards(catalog, "broken_fence_horn", "wool_guard", "pen_post"),
        combo.requirements,
    )


def test_water_and_boat_matches_attack_and_defense_by_phase() -> None:
    catalog = load_catalog(DATA_DIR)
    selected = cards(catalog, "current_surge", "boat_guard")

    assert matches_requirements(
        selected,
        catalog.combo("boat_core", "push_boat_with_current").requirements,
    )
    assert matches_requirements(
        selected,
        catalog.combo("boat_core", "row_against_current").requirements,
    )

