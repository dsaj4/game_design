from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .catalog import Catalog
from .matcher import matches_requirements
from .models import AuxiliaryCard, ComboRule


@dataclass(frozen=True)
class AvailabilityReport:
    deck_id: str
    hand_size: int
    total_hands: int
    combo_hits: dict[str, int]
    any_attack_hits: int
    any_defense_hits: int
    any_combo_hits: int

    def probability(self, hits: int) -> float:
        return hits / self.total_hands if self.total_hands else 0.0


def analyze_availability(
    catalog: Catalog,
    deck_id: str,
    hand_size: int,
) -> AvailabilityReport:
    deck = catalog.decks[deck_id]
    core = catalog.core_cards[deck.core_id]
    cards = [
        catalog.auxiliary_cards[card_id]
        for card_id, count in deck.cards.items()
        for _ in range(count)
    ]
    if hand_size < 1 or hand_size > len(cards):
        raise ValueError("hand size must be between 1 and deck size")

    combo_hits = {combo.id: 0 for combo in core.combos}
    attack_hits = 0
    defense_hits = 0
    any_hits = 0
    total = 0
    for hand in combinations(cards, hand_size):
        total += 1
        available = {
            combo.id: _hand_can_form(hand, combo)
            for combo in core.combos
        }
        for combo_id, can_form in available.items():
            combo_hits[combo_id] += int(can_form)
        has_attack = any(
            available[combo.id] for combo in core.combos if combo.nature == "attack"
        )
        has_defense = any(
            available[combo.id] for combo in core.combos if combo.nature == "defense"
        )
        attack_hits += int(has_attack)
        defense_hits += int(has_defense)
        any_hits += int(has_attack or has_defense)

    return AvailabilityReport(
        deck_id=deck_id,
        hand_size=hand_size,
        total_hands=total,
        combo_hits=combo_hits,
        any_attack_hits=attack_hits,
        any_defense_hits=defense_hits,
        any_combo_hits=any_hits,
    )


def _hand_can_form(hand: tuple[AuxiliaryCard, ...], combo: ComboRule) -> bool:
    if len(hand) < combo.required_card_count:
        return False
    return any(
        matches_requirements(selected, combo.requirements)
        for selected in combinations(hand, combo.required_card_count)
    )

