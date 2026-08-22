from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass

from .actions import (
    CombatAction,
    ComboAction,
    enumerate_combat_actions,
    enumerate_combo_actions,
)
from .catalog import Catalog
from .engine import PlayerState, release_prepared, resolve_action_exchange
from .errors import IllegalAction
from .models import Effect


@dataclass(frozen=True)
class PolicyWeights:
    own_health: float
    opponent_health: float
    shield: float
    cards: float
    status: float
    preparation_card_cost: float
    lost_attack_option_cost: float
    future_defense: float


PROFILES = {
    "balanced": PolicyWeights(4.0, 4.0, 1.2, 0.8, 1.0, 0.8, 0.35, 0.4),
    "aggressive": PolicyWeights(2.8, 5.5, 0.7, 0.6, 0.7, 1.0, 0.55, 0.2),
    "defensive": PolicyWeights(5.5, 3.0, 1.8, 0.8, 1.4, 0.55, 0.2, 0.65),
}


class HeuristicPolicy:
    """Two-ply deterministic policy over public state and the player's hand."""

    def __init__(self, profile: str = "balanced") -> None:
        if profile not in PROFILES:
            raise ValueError(f"unknown policy profile: {profile}")
        self.profile = profile
        self.weights = PROFILES[profile]

    def choose_attack(
        self,
        catalog: Catalog,
        core_id: str,
        player: PlayerState,
        opponent_core_id: str,
        opponent: PlayerState,
    ) -> CombatAction | None:
        actions = enumerate_combat_actions(
            catalog,
            core_id,
            player.hand,
            "attack",
            energy=player.energy,
        )
        if not actions:
            return None

        pass_player = deepcopy(player)
        pass_opponent = deepcopy(opponent)
        release_prepared(pass_opponent)
        best_score = self._score(pass_player, pass_opponent) + (
            self._future_defense_value(catalog, core_id, pass_player)
            * self.weights.future_defense
        )
        best_action: CombatAction | None = None

        for action in actions:
            outcome = self._anticipated_outcome(
                catalog,
                core_id,
                action,
                player,
                opponent_core_id,
                opponent,
            )
            if outcome is None:
                continue
            score = self._score(*outcome) + (
                self._future_defense_value(catalog, core_id, outcome[0])
                * self.weights.future_defense
            )
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    def choose_defense(
        self,
        catalog: Catalog,
        attack_core_id: str,
        attack_action: CombatAction,
        attacker: PlayerState,
        defense_core_id: str,
        defender: PlayerState,
    ) -> CombatAction | None:
        return self._best_defense(
            catalog,
            attack_core_id,
            attack_action,
            attacker,
            defense_core_id,
            defender,
        )

    def prepare_defense(
        self,
        catalog: Catalog,
        core_id: str,
        player: PlayerState,
    ) -> CombatAction | None:
        if player.prepared:
            return None
        actions = enumerate_combat_actions(
            catalog,
            core_id,
            player.hand,
            "defense",
            energy=player.energy,
        )
        if not actions:
            return None

        attack_options_before = len(
            enumerate_combo_actions(catalog, core_id, player.hand, "attack")
        )
        best_action: CombatAction | None = None
        best_score = 0.0
        for action in actions:
            remaining_hand = list(player.hand)
            for card_id in action.card_ids:
                remaining_hand.remove(card_id)
            attack_options_after = len(
                enumerate_combo_actions(catalog, core_id, remaining_hand, "attack")
            )
            score = self._static_defense_value(catalog, core_id, action)
            score -= len(action.card_ids) * self.weights.preparation_card_cost
            score -= (
                attack_options_before - attack_options_after
            ) * self.weights.lost_attack_option_cost
            if score > best_score:
                best_score = score
                best_action = action

        if best_action is None:
            return None
        for card_id in best_action.card_ids:
            player.hand.remove(card_id)
            player.prepared.append(card_id)
        return best_action

    def trim_hand(
        self,
        catalog: Catalog,
        core_id: str,
        player: PlayerState,
        hand_limit: int,
    ) -> None:
        while len(player.hand) > hand_limit:
            best_index = 0
            best_remaining_options = -1
            for index in range(len(player.hand)):
                remaining = player.hand[:index] + player.hand[index + 1 :]
                option_count = len(
                    enumerate_combo_actions(catalog, core_id, remaining, "attack")
                ) + len(enumerate_combo_actions(catalog, core_id, remaining, "defense"))
                if option_count > best_remaining_options:
                    best_remaining_options = option_count
                    best_index = index
            player.discard.append(player.hand.pop(best_index))

    def _anticipated_outcome(
        self,
        catalog: Catalog,
        attack_core_id: str,
        attack_action: CombatAction,
        attacker: PlayerState,
        defense_core_id: str,
        defender: PlayerState,
    ) -> tuple[PlayerState, PlayerState] | None:
        defense = self._best_defense(
            catalog,
            attack_core_id,
            attack_action,
            attacker,
            defense_core_id,
            defender,
        )
        attacker_copy = deepcopy(attacker)
        defender_copy = deepcopy(defender)
        try:
            _resolve_action_pair(
                catalog,
                attacker_copy,
                defender_copy,
                attack_core_id,
                attack_action,
                defense_core_id,
                defense,
            )
        except IllegalAction:
            return None
        return attacker_copy, defender_copy

    def _best_defense(
        self,
        catalog: Catalog,
        attack_core_id: str,
        attack_action: CombatAction,
        attacker: PlayerState,
        defense_core_id: str,
        defender: PlayerState,
    ) -> CombatAction | None:
        actions: list[CombatAction | None] = [None]
        actions.extend(
            enumerate_combat_actions(
                catalog,
                defense_core_id,
                defender.prepared,
                "defense",
                energy=defender.energy,
            )
        )
        best_action: CombatAction | None = None
        best_score = float("-inf")
        for defense_action in actions:
            attacker_copy = deepcopy(attacker)
            defender_copy = deepcopy(defender)
            try:
                _resolve_action_pair(
                    catalog,
                    attacker_copy,
                    defender_copy,
                    attack_core_id,
                    attack_action,
                    defense_core_id,
                    defense_action,
                )
            except IllegalAction:
                continue
            score = self._score(defender_copy, attacker_copy)
            if score > best_score:
                best_score = score
                best_action = defense_action
        return best_action

    def _score(self, player: PlayerState, opponent: PlayerState) -> float:
        return (
            player.health * self.weights.own_health
            - opponent.health * self.weights.opponent_health
            + (player.shield - opponent.shield) * self.weights.shield
            + (
                len(player.hand)
                + len(player.prepared)
                - len(opponent.hand)
                - len(opponent.prepared)
            )
            * self.weights.cards
            + (
                _future_status_value(player.statuses)
                - _future_status_value(opponent.statuses)
            )
            * self.weights.status
        )

    def _static_defense_value(
        self,
        catalog: Catalog,
        core_id: str,
        action: CombatAction,
    ) -> float:
        effects = [catalog.auxiliary_cards[card_id].base_effect for card_id in action.card_ids]
        score = sum(self._effect_value(effect) for effect in effects)
        if isinstance(action, ComboAction):
            rule = catalog.combo(core_id, action.combo_id)
            score += sum(self._effect_value(effect) for effect in rule.effects)
            if rule.persistent:
                score += rule.persistent.triggers * sum(
                    self._effect_value(effect) for effect in rule.persistent.effects
                )
        return score

    def _future_defense_value(
        self,
        catalog: Catalog,
        core_id: str,
        player: PlayerState,
    ) -> float:
        actions = enumerate_combat_actions(
            catalog,
            core_id,
            player.hand,
            "defense",
            energy=player.energy,
        )
        return max(
            (
                self._static_defense_value(catalog, core_id, action)
                - len(action.card_ids) * self.weights.preparation_card_cost
                for action in actions
            ),
            default=0.0,
        )

    def _effect_value(self, effect: Effect) -> float:
        if effect.kind in {"block", "heal"}:
            return effect.value * self.weights.own_health
        if effect.kind == "gain_shield":
            return effect.value * self.weights.shield
        if effect.kind == "damage":
            return effect.value * self.weights.opponent_health
        if effect.kind in {"draw", "discard"}:
            return effect.value * self.weights.cards
        if effect.kind == "pay_health":
            return -effect.value * self.weights.own_health
        return 0.0


def _future_status_value(statuses) -> float:
    total = 0.0
    for status in statuses:
        for effect in status.effects:
            total += effect.value * status.remaining_triggers
    return total


def _resolve_action_pair(
    catalog: Catalog,
    attacker: PlayerState,
    defender: PlayerState,
    attack_core_id: str,
    attack_action: CombatAction,
    defense_core_id: str,
    defense_action: CombatAction | None,
) -> None:
    resolve_action_exchange(
        catalog,
        attacker,
        defender,
        attack_core_id=attack_core_id,
        attack_action=attack_action,
        defense_core_id=defense_core_id,
        defense_action=defense_action,
    )
