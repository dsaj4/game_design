from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Effect:
    kind: str
    value: int


@dataclass(frozen=True)
class AuxiliaryCard:
    id: str
    name: str
    attribute: str
    fields: tuple[str, ...]
    base_effect: Effect

    def with_base_effect(self, *, kind: str, value: int | None = None) -> AuxiliaryCard:
        return replace(
            self,
            base_effect=Effect(kind=kind, value=value or self.base_effect.value),
        )


@dataclass(frozen=True)
class FieldRequirement:
    field: str
    count: int


@dataclass(frozen=True)
class PersistentSpec:
    id: str
    name: str
    trigger: str
    triggers: int
    stacking: str
    effects: tuple[Effect, ...]


@dataclass(frozen=True)
class ComboRule:
    id: str
    name: str
    nature: str
    duration: str
    requirements: tuple[FieldRequirement, ...]
    effects: tuple[Effect, ...]
    persistent: PersistentSpec | None = None

    @property
    def required_card_count(self) -> int:
        return sum(requirement.count for requirement in self.requirements)


@dataclass(frozen=True)
class CoreCard:
    id: str
    name: str
    combos: tuple[ComboRule, ...]


@dataclass(frozen=True)
class Deck:
    id: str
    name: str
    core_id: str
    cards: dict[str, int]

