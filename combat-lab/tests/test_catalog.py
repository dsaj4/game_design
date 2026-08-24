from pathlib import Path

import pytest

from combat_lab.catalog import load_catalog, validate_catalog, with_combo_costs
from combat_lab.errors import CatalogError


DATA_DIR = Path(__file__).parents[1] / "data"


def test_first_catalog_is_valid() -> None:
    catalog = load_catalog(DATA_DIR)

    validate_catalog(catalog)

    assert len(catalog.core_cards) == 2
    assert all(len(core.combos) == 4 for core in catalog.core_cards.values())
    assert all(sum(deck.cards.values()) == 20 for deck in catalog.decks.values())
    assert {card.energy_cost for card in catalog.auxiliary_cards.values()} == {1}
    assert {
        combo.id: combo.energy_cost
        for core in catalog.core_cards.values()
        for combo in core.combos
    } == {
        "three_sheep_blessing": 1,
        "mend_after_loss": 2,
        "sheep_enters_tiger_mouth": 2,
        "lead_away_sheep": 2,
        "break_pot_sink_boat": 3,
        "push_boat_with_current": 2,
        "same_boat_aid": 2,
        "row_against_current": 2,
    }


def test_each_core_has_attack_and_defense_combos() -> None:
    catalog = load_catalog(DATA_DIR)

    for core in catalog.core_cards.values():
        natures = {combo.nature for combo in core.combos}
        assert {"attack", "defense"} <= natures


def test_auxiliary_attribute_must_match_its_base_effect() -> None:
    catalog = load_catalog(DATA_DIR)
    card = catalog.auxiliary_cards["lamb_charge"]
    invalid = card.with_base_effect(kind="draw")
    catalog.auxiliary_cards[card.id] = invalid

    with pytest.raises(CatalogError, match="attribute attack requires damage"):
        validate_catalog(catalog)


def test_combo_cost_override_is_validated_without_mutating_source() -> None:
    catalog = load_catalog(DATA_DIR)

    updated = with_combo_costs(catalog, {"break_pot_sink_boat": 4})

    assert catalog.combo("boat_core", "break_pot_sink_boat").energy_cost == 3
    assert updated.combo("boat_core", "break_pot_sink_boat").energy_cost == 4

    with pytest.raises(CatalogError, match="unknown combo cost override"):
        with_combo_costs(catalog, {"missing": 2})
