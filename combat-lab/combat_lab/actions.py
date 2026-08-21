from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import TypeAlias

from .catalog import Catalog
from .matcher import matches_requirements


@dataclass(frozen=True, order=True)
class ComboAction:
    combo_id: str
    card_ids: tuple[str, ...]


@dataclass(frozen=True, order=True)
class StandaloneAction:
    card_id: str

    @property
    def card_ids(self) -> tuple[str, ...]:
        return (self.card_id,)


CombatAction: TypeAlias = ComboAction | StandaloneAction


def enumerate_combo_actions(
    catalog: Catalog,
    core_id: str,
    card_ids: list[str],
    nature: str,
) -> list[ComboAction]:
    """Enumerate unique legal combo/material choices for a card zone."""
    core = catalog.core_cards[core_id]
    cards = [catalog.auxiliary_cards[card_id] for card_id in card_ids]
    actions: set[ComboAction] = set()
    for combo in core.combos:
        if combo.nature != nature or len(cards) < combo.required_card_count:
            continue
        for indexes in combinations(range(len(cards)), combo.required_card_count):
            selected = [cards[index] for index in indexes]
            if matches_requirements(selected, combo.requirements):
                actions.add(
                    ComboAction(
                        combo_id=combo.id,
                        card_ids=tuple(sorted(card.id for card in selected)),
                    )
                )
    return sorted(actions)


def enumerate_combat_actions(
    catalog: Catalog,
    core_id: str,
    card_ids: list[str],
    nature: str,
    *,
    energy: int,
) -> list[CombatAction]:
    """Enumerate affordable combos plus unique one-card fallback actions."""
    combos = [
        action
        for action in enumerate_combo_actions(catalog, core_id, card_ids, nature)
        if catalog.combo(core_id, action.combo_id).energy_cost <= energy
    ]
    standalone = [
        StandaloneAction(card_id)
        for card_id in sorted(set(card_ids))
        if catalog.auxiliary_cards[card_id].energy_cost <= energy
    ]
    return [*combos, *standalone]


def action_energy_cost(
    catalog: Catalog,
    core_id: str,
    action: CombatAction,
) -> int:
    if isinstance(action, ComboAction):
        return catalog.combo(core_id, action.combo_id).energy_cost
    return catalog.auxiliary_cards[action.card_id].energy_cost
