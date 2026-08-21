from pathlib import Path

import pytest

from combat_lab.catalog import load_catalog, validate_catalog
from combat_lab.errors import CatalogError


DATA_DIR = Path(__file__).parents[1] / "data"


def test_first_catalog_is_valid() -> None:
    catalog = load_catalog(DATA_DIR)

    validate_catalog(catalog)

    assert len(catalog.core_cards) == 2
    assert all(len(core.combos) == 4 for core in catalog.core_cards.values())
    assert all(sum(deck.cards.values()) == 20 for deck in catalog.decks.values())


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

