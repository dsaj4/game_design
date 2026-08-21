from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field

from .catalog import Catalog
from .errors import IllegalAction
from .matcher import matches_requirements
from .models import AuxiliaryCard, ComboRule, Effect, PersistentSpec


MAX_STATUS_SLOTS = 3


@dataclass
class ActiveStatus:
    id: str
    name: str
    remaining_triggers: int
    effects: tuple[Effect, ...]


@dataclass
class PlayerState:
    health: int = 30
    max_health: int = 30
    shield: int = 0
    hand: list[str] = field(default_factory=list)
    prepared: list[str] = field(default_factory=list)
    deck: list[str] = field(default_factory=list)
    discard: list[str] = field(default_factory=list)
    statuses: list[ActiveStatus] = field(default_factory=list)


@dataclass
class ResolutionResult:
    attack_damage: int = 0
    blocked_damage: int = 0
    shield_absorbed: int = 0
    health_damage: int = 0
    log: list[str] = field(default_factory=list)


@dataclass
class _ResolutionContext:
    phase: str
    result: ResolutionResult
    pending_damage: int = 0


def resolve_exchange(
    catalog: Catalog,
    attacker: PlayerState,
    defender: PlayerState,
    *,
    core_id: str,
    attack_combo_id: str,
    attack_card_ids: list[str],
    defense_core_id: str | None = None,
    defense_combo_id: str | None = None,
    defense_card_ids: list[str] | None = None,
) -> ResolutionResult:
    """Resolve one attack and the defender's optional single defense combo atomically."""
    attack_rule = catalog.combo(core_id, attack_combo_id)
    if attack_rule.nature != "attack":
        raise IllegalAction(f"{attack_rule.name} is not an attack combo")

    attacker_copy = deepcopy(attacker)
    defender_copy = deepcopy(defender)
    result = ResolutionResult()
    attack_context = _ResolutionContext(phase="attack", result=result)

    attack_cards = _take_cards(
        catalog,
        attacker_copy.hand,
        attacker_copy.discard,
        attack_card_ids,
        zone_name="hand",
    )
    _assert_matches(attack_rule, attack_cards)
    _resolve_cards_and_combo(
        attacker_copy,
        defender_copy,
        attack_rule,
        attack_cards,
        attack_context,
    )
    result.attack_damage = attack_context.pending_damage

    has_defense = defense_combo_id is not None or defense_card_ids is not None
    if has_defense:
        if not defense_core_id or not defense_combo_id or defense_card_ids is None:
            raise IllegalAction("defense core, combo, and cards must be declared together")
        defense_rule = catalog.combo(defense_core_id, defense_combo_id)
        if defense_rule.nature != "defense":
            raise IllegalAction(f"{defense_rule.name} is not a defense combo")
        defense_cards = _take_cards(
            catalog,
            defender_copy.prepared,
            defender_copy.discard,
            defense_card_ids,
            zone_name="prepared zone",
        )
        _assert_matches(defense_rule, defense_cards)
        defense_context = _ResolutionContext(
            phase="defense",
            result=result,
            pending_damage=attack_context.pending_damage,
        )
        _resolve_cards_and_combo(
            defender_copy,
            attacker_copy,
            defense_rule,
            defense_cards,
            defense_context,
        )
        attack_context.pending_damage = defense_context.pending_damage

    defender_copy.hand.extend(defender_copy.prepared)
    defender_copy.prepared.clear()
    result.shield_absorbed, result.health_damage = _deal_damage(
        defender_copy,
        attack_context.pending_damage,
    )

    _commit(attacker, attacker_copy)
    _commit(defender, defender_copy)
    return result


def tick_owner_turn_start(catalog: Catalog, player: PlayerState) -> None:
    del catalog  # Reserved for future status lookup and dynamic balance tables.
    remaining: list[ActiveStatus] = []
    for status in player.statuses:
        for effect in status.effects:
            _apply_self_effect(player, effect)
        status.remaining_triggers -= 1
        if status.remaining_triggers > 0:
            remaining.append(status)
    player.statuses = remaining


def _resolve_cards_and_combo(
    actor: PlayerState,
    target: PlayerState,
    rule: ComboRule,
    cards: list[AuxiliaryCard],
    context: _ResolutionContext,
) -> None:
    for card in cards:
        _apply_effect(actor, target, card.base_effect, context)
        context.result.log.append(f"base:{card.id}:{card.base_effect.kind}:{card.base_effect.value}")
    for effect in rule.effects:
        _apply_effect(actor, target, effect, context)
        context.result.log.append(f"combo:{rule.id}:{effect.kind}:{effect.value}")
    if rule.persistent:
        _add_status(actor, rule.persistent)
        context.result.log.append(f"status:{rule.persistent.id}")


def _apply_effect(
    actor: PlayerState,
    target: PlayerState,
    effect: Effect,
    context: _ResolutionContext,
) -> None:
    if effect.kind == "damage":
        if context.phase == "attack":
            context.pending_damage += effect.value
        else:
            _deal_damage(target, effect.value)
    elif effect.kind == "gain_shield":
        actor.shield += effect.value
    elif effect.kind == "heal":
        actor.health = min(actor.max_health, actor.health + effect.value)
    elif effect.kind == "pay_health":
        if actor.health - effect.value < 1:
            raise IllegalAction("health payment must retain at least 1 health")
        actor.health -= effect.value
    elif effect.kind == "block":
        if context.phase != "defense":
            raise IllegalAction("block can only resolve during defense")
        blocked = min(context.pending_damage, effect.value)
        context.pending_damage -= blocked
        context.result.blocked_damage += blocked
    elif effect.kind == "draw":
        if actor.deck:
            actor.hand.append(actor.deck.pop(0))
    elif effect.kind == "discard":
        if target.hand:
            target.discard.append(target.hand.pop())
    else:
        raise IllegalAction(f"unsupported effect: {effect.kind}")


def _apply_self_effect(player: PlayerState, effect: Effect) -> None:
    if effect.kind == "gain_shield":
        player.shield += effect.value
    elif effect.kind == "heal":
        player.health = min(player.max_health, player.health + effect.value)
    else:
        raise IllegalAction(f"unsupported persistent effect: {effect.kind}")


def _add_status(player: PlayerState, spec: PersistentSpec) -> None:
    existing = next((status for status in player.statuses if status.id == spec.id), None)
    if existing:
        existing.remaining_triggers = spec.triggers
        existing.effects = spec.effects
        return
    if len(player.statuses) >= MAX_STATUS_SLOTS:
        raise IllegalAction("all 3 persistent status slots are occupied")
    player.statuses.append(
        ActiveStatus(
            id=spec.id,
            name=spec.name,
            remaining_triggers=spec.triggers,
            effects=spec.effects,
        )
    )


def _take_cards(
    catalog: Catalog,
    source: list[str],
    discard: list[str],
    selected_ids: list[str],
    *,
    zone_name: str,
) -> list[AuxiliaryCard]:
    working = list(source)
    selected: list[AuxiliaryCard] = []
    for card_id in selected_ids:
        if card_id not in working:
            raise IllegalAction(f"card {card_id} is not available in {zone_name}")
        try:
            card = catalog.auxiliary_cards[card_id]
        except KeyError as exc:
            raise IllegalAction(f"unknown auxiliary card: {card_id}") from exc
        working.remove(card_id)
        selected.append(card)
    source[:] = working
    discard.extend(selected_ids)
    return selected


def _assert_matches(rule: ComboRule, cards: list[AuxiliaryCard]) -> None:
    if not matches_requirements(cards, rule.requirements):
        raise IllegalAction(f"selected cards do not satisfy {rule.name}")


def _deal_damage(player: PlayerState, amount: int) -> tuple[int, int]:
    shield_absorbed = min(player.shield, amount)
    player.shield -= shield_absorbed
    health_damage = amount - shield_absorbed
    player.health = max(0, player.health - health_damage)
    return shield_absorbed, health_damage


def _commit(destination: PlayerState, source: PlayerState) -> None:
    destination.health = source.health
    destination.max_health = source.max_health
    destination.shield = source.shield
    destination.hand = source.hand
    destination.prepared = source.prepared
    destination.deck = source.deck
    destination.discard = source.discard
    destination.statuses = source.statuses

