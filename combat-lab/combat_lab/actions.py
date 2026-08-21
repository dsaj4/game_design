from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .catalog import Catalog
from .matcher import matches_requirements


@dataclass(frozen=True, order=True)
class ComboAction:
    combo_id: str
    card_ids: tuple[str, ...]


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

