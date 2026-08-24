from __future__ import annotations

import json
from dataclasses import dataclass, replace
from pathlib import Path

from .errors import CatalogError
from .matcher import matches_requirements
from .models import (
    AuxiliaryCard,
    ComboRule,
    CoreCard,
    Deck,
    Effect,
    FieldRequirement,
    PersistentSpec,
)


ATTRIBUTE_EFFECTS = {
    "attack": "damage",
    "defense": "gain_shield",
    "dispatch": "draw",
    "disrupt": "discard",
}
ALLOWED_EFFECTS = {
    "damage",
    "gain_shield",
    "draw",
    "discard",
    "block",
    "heal",
    "pay_health",
}


@dataclass
class Catalog:
    auxiliary_cards: dict[str, AuxiliaryCard]
    core_cards: dict[str, CoreCard]
    decks: dict[str, Deck]

    def combo(self, core_id: str, combo_id: str) -> ComboRule:
        try:
            core = self.core_cards[core_id]
        except KeyError as exc:
            raise CatalogError(f"unknown core card: {core_id}") from exc
        for combo in core.combos:
            if combo.id == combo_id:
                return combo
        raise CatalogError(f"unknown combo {combo_id} for core {core_id}")


def with_combo_costs(catalog: Catalog, overrides: dict[str, int]) -> Catalog:
    """Return a validated catalog with uniquely identified combo costs replaced."""
    locations: dict[str, list[str]] = {}
    for core_id, core in catalog.core_cards.items():
        for combo in core.combos:
            locations.setdefault(combo.id, []).append(core_id)

    for combo_id, cost in overrides.items():
        core_ids = locations.get(combo_id, [])
        if not core_ids:
            raise CatalogError(f"unknown combo cost override: {combo_id}")
        if len(core_ids) > 1:
            raise CatalogError(f"ambiguous combo cost override: {combo_id}")
        if cost < 1 or cost > 4:
            raise CatalogError(f"{combo_id}: energy cost must be between 1 and 4")

    core_cards = {}
    for core_id, core in catalog.core_cards.items():
        combos = tuple(
            replace(combo, energy_cost=overrides.get(combo.id, combo.energy_cost))
            for combo in core.combos
        )
        core_cards[core_id] = replace(core, combos=combos)

    updated = Catalog(catalog.auxiliary_cards, core_cards, catalog.decks)
    validate_catalog(updated)
    return updated


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _effect(data: dict) -> Effect:
    return Effect(kind=data["kind"], value=int(data["value"]))


def _combo(data: dict) -> ComboRule:
    persistent_data = data.get("persistent")
    persistent = None
    if persistent_data:
        persistent = PersistentSpec(
            id=persistent_data["id"],
            name=persistent_data["name"],
            trigger=persistent_data["trigger"],
            triggers=int(persistent_data["triggers"]),
            stacking=persistent_data["stacking"],
            effects=tuple(_effect(item) for item in persistent_data["effects"]),
        )
    return ComboRule(
        id=data["id"],
        name=data["name"],
        nature=data["nature"],
        duration=data["duration"],
        energy_cost=int(data["energy_cost"]),
        requirements=tuple(
            FieldRequirement(field=field, count=int(count))
            for field, count in data["requirements"].items()
        ),
        effects=tuple(_effect(item) for item in data.get("effects", [])),
        persistent=persistent,
    )


def load_catalog(data_dir: Path | str) -> Catalog:
    data_dir = Path(data_dir)
    auxiliary_data = _read_json(data_dir / "auxiliary_cards.json")
    core_data = _read_json(data_dir / "core_cards.json")
    deck_data = _read_json(data_dir / "decks.json")

    auxiliary_cards = {
        item["id"]: AuxiliaryCard(
            id=item["id"],
            name=item["name"],
            attribute=item["attribute"],
            fields=tuple(item["fields"]),
            energy_cost=int(item["energy_cost"]),
            base_effect=_effect(item["base_effect"]),
        )
        for item in auxiliary_data["cards"]
    }
    core_cards = {
        item["id"]: CoreCard(
            id=item["id"],
            name=item["name"],
            combos=tuple(_combo(combo) for combo in item["combos"]),
        )
        for item in core_data["core_cards"]
    }
    decks = {
        item["id"]: Deck(
            id=item["id"],
            name=item["name"],
            core_id=item["core_id"],
            cards={card_id: int(count) for card_id, count in item["cards"].items()},
        )
        for item in deck_data["decks"]
    }
    catalog = Catalog(auxiliary_cards, core_cards, decks)
    validate_catalog(catalog)
    return catalog


def validate_catalog(catalog: Catalog) -> None:
    for card_id, card in catalog.auxiliary_cards.items():
        expected = ATTRIBUTE_EFFECTS.get(card.attribute)
        if expected is None:
            raise CatalogError(f"{card_id}: unknown attribute {card.attribute}")
        if card.base_effect.kind != expected:
            raise CatalogError(
                f"{card_id}: attribute {card.attribute} requires {expected}, "
                f"got {card.base_effect.kind}"
            )
        if card.base_effect.value != 1:
            raise CatalogError(f"{card_id}: first-test base effects must have value 1")
        if card.energy_cost != 1:
            raise CatalogError(f"{card_id}: standalone auxiliary actions must cost 1 energy")
        if not card.fields or len(card.fields) != len(set(card.fields)):
            raise CatalogError(f"{card_id}: fields must be non-empty and unique")

    for core_id, core in catalog.core_cards.items():
        if len(core.combos) != 4:
            raise CatalogError(f"{core_id}: a first-test core must define exactly 4 combos")
        if len({combo.id for combo in core.combos}) != 4:
            raise CatalogError(f"{core_id}: combo ids must be unique")
        natures = {combo.nature for combo in core.combos}
        if not {"attack", "defense"} <= natures:
            raise CatalogError(f"{core_id}: must define at least one attack and defense combo")
        for combo in core.combos:
            _validate_combo(core_id, combo)

    for deck_id, deck in catalog.decks.items():
        if deck.core_id not in catalog.core_cards:
            raise CatalogError(f"{deck_id}: unknown core card {deck.core_id}")
        if sum(deck.cards.values()) != 20:
            raise CatalogError(f"{deck_id}: first-test decks must contain exactly 20 cards")
        unknown = set(deck.cards) - set(catalog.auxiliary_cards)
        if unknown:
            raise CatalogError(f"{deck_id}: unknown auxiliary cards: {sorted(unknown)}")
        expanded = [
            catalog.auxiliary_cards[card_id]
            for card_id, count in deck.cards.items()
            for _ in range(count)
        ]
        for combo in catalog.core_cards[deck.core_id].combos:
            if not _deck_can_match(expanded, combo):
                raise CatalogError(f"{deck_id}: cannot form combo {combo.id}")


def _validate_combo(core_id: str, combo: ComboRule) -> None:
    if combo.nature not in {"attack", "defense"}:
        raise CatalogError(f"{core_id}/{combo.id}: invalid nature {combo.nature}")
    if combo.duration not in {"instant", "persistent"}:
        raise CatalogError(f"{core_id}/{combo.id}: invalid duration {combo.duration}")
    if combo.energy_cost < 1 or combo.energy_cost > 4:
        raise CatalogError(f"{core_id}/{combo.id}: energy cost must be between 1 and 4")
    if combo.required_card_count < 1 or combo.required_card_count > 3:
        raise CatalogError(f"{core_id}/{combo.id}: requires between 1 and 3 cards")
    if any(requirement.count < 1 for requirement in combo.requirements):
        raise CatalogError(f"{core_id}/{combo.id}: field counts must be positive")
    for effect in combo.effects:
        _validate_effect(core_id, combo.id, effect)
    if combo.duration == "persistent" and combo.persistent is None:
        raise CatalogError(f"{core_id}/{combo.id}: persistent combo needs a status")
    if combo.duration == "instant" and combo.persistent is not None:
        raise CatalogError(f"{core_id}/{combo.id}: instant combo cannot create a status")
    if combo.persistent:
        if combo.persistent.trigger != "owner_turn_start":
            raise CatalogError(f"{core_id}/{combo.id}: unsupported persistent trigger")
        if combo.persistent.triggers < 1:
            raise CatalogError(f"{core_id}/{combo.id}: status needs at least one trigger")
        if combo.persistent.stacking != "refresh":
            raise CatalogError(f"{core_id}/{combo.id}: first test only supports refresh stacking")
        for effect in combo.persistent.effects:
            _validate_effect(core_id, combo.id, effect)
            if effect.kind not in {"gain_shield", "heal"}:
                raise CatalogError(f"{core_id}/{combo.id}: unsupported persistent effect")


def _validate_effect(core_id: str, combo_id: str, effect: Effect) -> None:
    if effect.kind not in ALLOWED_EFFECTS:
        raise CatalogError(f"{core_id}/{combo_id}: unknown effect {effect.kind}")
    if effect.value < 1:
        raise CatalogError(f"{core_id}/{combo_id}: effect values must be positive")


def _deck_can_match(cards: list[AuxiliaryCard], combo: ComboRule) -> bool:
    from itertools import combinations

    return any(
        matches_requirements(selected, combo.requirements)
        for selected in combinations(cards, combo.required_card_count)
    )
