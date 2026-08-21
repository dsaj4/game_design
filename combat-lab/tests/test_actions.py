from pathlib import Path

from combat_lab.actions import enumerate_combo_actions
from combat_lab.catalog import load_catalog


DATA_DIR = Path(__file__).parents[1] / "data"


def test_enumerates_all_legal_attack_combos_without_duplicate_material_sets() -> None:
    catalog = load_catalog(DATA_DIR)
    hand = [
        "lamb_charge",
        "wool_guard",
        "tiger_pounce",
        "tiger_bait",
        "guiding_hand",
    ]

    actions = enumerate_combo_actions(catalog, "sheep_core", hand, "attack")

    signatures = {(action.combo_id, action.card_ids) for action in actions}
    assert len(signatures) == len(actions)
    assert ("sheep_enters_tiger_mouth", ("lamb_charge", "tiger_pounce")) in signatures
    assert ("lead_away_sheep", ("guiding_hand", "lamb_charge")) in signatures


def test_duplicate_card_instances_can_form_three_sheep_combo() -> None:
    catalog = load_catalog(DATA_DIR)

    actions = enumerate_combo_actions(
        catalog,
        "sheep_core",
        ["lamb_charge", "lamb_charge", "wool_guard"],
        "defense",
    )

    assert any(
        action.combo_id == "three_sheep_blessing"
        and action.card_ids == ("lamb_charge", "lamb_charge", "wool_guard")
        for action in actions
    )


def test_attack_enumeration_never_returns_defense_combo() -> None:
    catalog = load_catalog(DATA_DIR)

    actions = enumerate_combo_actions(
        catalog,
        "boat_core",
        ["current_surge", "boat_guard"],
        "attack",
    )

    assert {action.combo_id for action in actions} == {"row_against_current"}

