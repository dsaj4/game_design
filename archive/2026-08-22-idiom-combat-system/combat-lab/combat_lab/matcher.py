from __future__ import annotations

from collections.abc import Sequence

from .models import AuxiliaryCard, FieldRequirement


def matches_requirements(
    cards: Sequence[AuxiliaryCard],
    requirements: Sequence[FieldRequirement],
) -> bool:
    """Return whether distinct cards can fill every required field slot.

    A multi-field card may fill one slot only. This is a small bipartite
    matching problem; card order has no effect on the result.
    """
    slots = tuple(
        requirement.field
        for requirement in requirements
        for _ in range(requirement.count)
    )
    if len(cards) != len(slots):
        return False

    ordered_cards = sorted(cards, key=lambda card: sum(field in slots for field in card.fields))

    def assign(card_index: int, remaining_slots: tuple[str, ...]) -> bool:
        if card_index == len(ordered_cards):
            return not remaining_slots

        card = ordered_cards[card_index]
        tried_fields: set[str] = set()
        for slot_index, field in enumerate(remaining_slots):
            if field in tried_fields or field not in card.fields:
                continue
            tried_fields.add(field)
            next_slots = remaining_slots[:slot_index] + remaining_slots[slot_index + 1 :]
            if assign(card_index + 1, next_slots):
                return True
        return False

    return assign(0, slots)

