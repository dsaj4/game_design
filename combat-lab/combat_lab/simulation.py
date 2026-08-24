from __future__ import annotations

import math
import random
from collections import Counter
from dataclasses import dataclass

from .actions import CombatAction, ComboAction, StandaloneAction
from .catalog import Catalog
from .engine import (
    PlayerState,
    release_prepared,
    resolve_action_exchange,
    tick_owner_turn_start,
)
from .policies import HeuristicPolicy


@dataclass(frozen=True)
class GameConfig:
    starting_health: int = 30
    opening_hand: int = 4
    hand_limit: int = 7
    max_full_rounds: int = 12
    energy_capacity: int = 4


@dataclass(frozen=True)
class GameResult:
    winner: int | None
    reason: str
    full_rounds: int
    turns: int
    turns_by_player: tuple[int, int]
    remaining_health: tuple[int, int]
    remaining_shield: tuple[int, int]
    combo_usage: tuple[tuple[tuple[str, int], ...], tuple[tuple[str, int], ...]]
    standalone_usage: tuple[tuple[tuple[str, int], ...], tuple[tuple[str, int], ...]]
    standalone_offense_actions: tuple[int, int]
    standalone_defense_actions: tuple[int, int]
    no_offense_turns: tuple[int, int]
    offense_energy_spent: tuple[int, int]
    defense_energy_spent: tuple[int, int]
    reserved_energy_after_offense: tuple[int, int]
    starting_player: int


@dataclass(frozen=True)
class MatchupReport:
    deck_a: str
    deck_b: str
    games: int
    deck_a_wins: int
    deck_b_wins: int
    draws: int
    deck_a_score_rate: float
    deck_a_score_ci95: tuple[float, float]
    average_full_rounds: float
    knockout_rate: float
    starts_a: int
    starts_b: int
    starting_player_wins: int
    starting_player_score_rate: float
    deck_a_score_when_starting: float
    deck_a_score_when_second: float
    combo_usage_a: dict[str, int]
    combo_usage_b: dict[str, int]
    standalone_usage_a: dict[str, int]
    standalone_usage_b: dict[str, int]
    standalone_offense_rate_a: float
    standalone_offense_rate_b: float
    standalone_defense_rate_a: float
    standalone_defense_rate_b: float
    no_offense_rate_a: float
    no_offense_rate_b: float
    average_offense_energy_spent_a: float
    average_offense_energy_spent_b: float
    average_defense_energy_spent_a: float
    average_defense_energy_spent_b: float
    average_reserved_energy_a: float
    average_reserved_energy_b: float


@dataclass
class _Combatant:
    deck_id: str
    core_id: str
    state: PlayerState
    policy: HeuristicPolicy


def simulate_game(
    catalog: Catalog,
    deck_a: str,
    deck_b: str,
    *,
    seed: int,
    config: GameConfig | None = None,
    policy_a: str = "balanced",
    policy_b: str = "balanced",
    starting_player: int = 0,
) -> GameResult:
    config = config or GameConfig()
    rng = random.Random(seed)
    combatants = [
        _create_combatant(catalog, deck_a, policy_a, config, rng),
        _create_combatant(catalog, deck_b, policy_b, config, rng),
    ]
    for combatant in combatants:
        combatant.policy.prepare_defense(catalog, combatant.core_id, combatant.state)

    combo_usage = [Counter(), Counter()]
    standalone_usage = [Counter(), Counter()]
    standalone_offense_actions = [0, 0]
    standalone_defense_actions = [0, 0]
    no_offense_turns = [0, 0]
    offense_energy_spent = [0, 0]
    defense_energy_spent = [0, 0]
    reserved_energy_after_offense = [0, 0]
    turns_by_player = [0, 0]
    turns = 0

    for full_round in range(1, config.max_full_rounds + 1):
        for offset in range(2):
            active_index = (starting_player + offset) % 2
            defending_index = 1 - active_index
            active = combatants[active_index]
            defending = combatants[defending_index]
            turns += 1
            turns_by_player[active_index] += 1

            tick_owner_turn_start(catalog, active.state)
            _draw(active.state, 1)
            active.policy.trim_hand(
                catalog,
                active.core_id,
                active.state,
                config.hand_limit,
            )

            offense = active.policy.choose_attack(
                catalog,
                active.core_id,
                active.state,
                defending.core_id,
                defending.state,
            )
            if offense is None:
                no_offense_turns[active_index] += 1
                release_prepared(defending.state)
            else:
                defense = defending.policy.choose_defense(
                    catalog,
                    active.core_id,
                    offense,
                    active.state,
                    defending.core_id,
                    defending.state,
                )
                result = resolve_action_exchange(
                    catalog,
                    active.state,
                    defending.state,
                    attack_core_id=active.core_id,
                    attack_action=offense,
                    defense_core_id=defending.core_id,
                    defense_action=defense,
                )
                _record_action_usage(
                    offense,
                    active_index,
                    combo_usage,
                    standalone_usage,
                )
                if isinstance(offense, StandaloneAction):
                    standalone_offense_actions[active_index] += 1
                if defense is not None:
                    _record_action_usage(
                        defense,
                        defending_index,
                        combo_usage,
                        standalone_usage,
                    )
                    if isinstance(defense, StandaloneAction):
                        standalone_defense_actions[defending_index] += 1
                offense_energy_spent[active_index] += result.attack_energy_spent
                defense_energy_spent[defending_index] += result.defense_energy_spent

            reserved_energy_after_offense[active_index] += active.state.energy

            winner = _winner(combatants)
            if winner is not _NO_WINNER:
                return _game_result(
                    combatants,
                    winner,
                    "knockout",
                    full_round,
                    turns,
                    turns_by_player,
                    combo_usage,
                    standalone_usage,
                    standalone_offense_actions,
                    standalone_defense_actions,
                    no_offense_turns,
                    offense_energy_spent,
                    defense_energy_spent,
                    reserved_energy_after_offense,
                    starting_player,
                )

            active.policy.trim_hand(
                catalog,
                active.core_id,
                active.state,
                config.hand_limit,
            )
            active.policy.prepare_defense(catalog, active.core_id, active.state)

    health_a = combatants[0].state.health
    health_b = combatants[1].state.health
    winner = 0 if health_a > health_b else 1 if health_b > health_a else None
    return _game_result(
        combatants,
        winner,
        "round_limit",
        config.max_full_rounds,
        turns,
        turns_by_player,
        combo_usage,
        standalone_usage,
        standalone_offense_actions,
        standalone_defense_actions,
        no_offense_turns,
        offense_energy_spent,
        defense_energy_spent,
        reserved_energy_after_offense,
        starting_player,
    )


def simulate_matchup(
    catalog: Catalog,
    deck_a: str,
    deck_b: str,
    *,
    games: int,
    seed: int,
    config: GameConfig | None = None,
    policy_a: str = "balanced",
    policy_b: str = "balanced",
) -> MatchupReport:
    if games < 1:
        raise ValueError("games must be positive")
    rng = random.Random(seed)
    wins = [0, 0]
    draws = 0
    starts = [0, 0]
    starting_wins = 0
    scores: list[float] = []
    scores_by_starter = [[], []]
    starter_scores: list[float] = []
    rounds = 0
    knockouts = 0
    combo_usage = [Counter(), Counter()]
    standalone_usage = [Counter(), Counter()]
    standalone_offense_actions = [0, 0]
    standalone_defense_actions = [0, 0]
    no_offense = [0, 0]
    offense_energy_spent = [0, 0]
    defense_energy_spent = [0, 0]
    reserved_energy = [0, 0]
    turns = [0, 0]

    for game_index in range(games):
        starter = game_index % 2
        starts[starter] += 1
        result = simulate_game(
            catalog,
            deck_a,
            deck_b,
            seed=rng.randrange(0, 2**63),
            config=config,
            policy_a=policy_a,
            policy_b=policy_b,
            starting_player=starter,
        )
        rounds += result.full_rounds
        knockouts += int(result.reason == "knockout")
        no_offense[0] += result.no_offense_turns[0]
        no_offense[1] += result.no_offense_turns[1]
        offense_energy_spent[0] += result.offense_energy_spent[0]
        offense_energy_spent[1] += result.offense_energy_spent[1]
        defense_energy_spent[0] += result.defense_energy_spent[0]
        defense_energy_spent[1] += result.defense_energy_spent[1]
        reserved_energy[0] += result.reserved_energy_after_offense[0]
        reserved_energy[1] += result.reserved_energy_after_offense[1]
        turns[0] += result.turns_by_player[0]
        turns[1] += result.turns_by_player[1]
        combo_usage[0].update(dict(result.combo_usage[0]))
        combo_usage[1].update(dict(result.combo_usage[1]))
        standalone_usage[0].update(dict(result.standalone_usage[0]))
        standalone_usage[1].update(dict(result.standalone_usage[1]))
        standalone_offense_actions[0] += result.standalone_offense_actions[0]
        standalone_offense_actions[1] += result.standalone_offense_actions[1]
        standalone_defense_actions[0] += result.standalone_defense_actions[0]
        standalone_defense_actions[1] += result.standalone_defense_actions[1]
        if result.winner is None:
            draws += 1
            scores.append(0.5)
            scores_by_starter[starter].append(0.5)
            starter_scores.append(0.5)
        else:
            wins[result.winner] += 1
            deck_a_score = 1.0 if result.winner == 0 else 0.0
            scores.append(deck_a_score)
            scores_by_starter[starter].append(deck_a_score)
            starting_wins += int(result.winner == starter)
            starter_scores.append(1.0 if result.winner == starter else 0.0)

    score_rate = sum(scores) / games
    return MatchupReport(
        deck_a=deck_a,
        deck_b=deck_b,
        games=games,
        deck_a_wins=wins[0],
        deck_b_wins=wins[1],
        draws=draws,
        deck_a_score_rate=score_rate,
        deck_a_score_ci95=_mean_ci95(scores),
        average_full_rounds=rounds / games,
        knockout_rate=knockouts / games,
        starts_a=starts[0],
        starts_b=starts[1],
        starting_player_wins=starting_wins,
        starting_player_score_rate=sum(starter_scores) / games,
        deck_a_score_when_starting=sum(scores_by_starter[0]) / len(scores_by_starter[0]),
        deck_a_score_when_second=sum(scores_by_starter[1]) / len(scores_by_starter[1]),
        combo_usage_a=dict(sorted(combo_usage[0].items())),
        combo_usage_b=dict(sorted(combo_usage[1].items())),
        standalone_usage_a=dict(sorted(standalone_usage[0].items())),
        standalone_usage_b=dict(sorted(standalone_usage[1].items())),
        standalone_offense_rate_a=(
            standalone_offense_actions[0] / turns[0] if turns[0] else 0.0
        ),
        standalone_offense_rate_b=(
            standalone_offense_actions[1] / turns[1] if turns[1] else 0.0
        ),
        standalone_defense_rate_a=(
            standalone_defense_actions[0] / turns[0] if turns[0] else 0.0
        ),
        standalone_defense_rate_b=(
            standalone_defense_actions[1] / turns[1] if turns[1] else 0.0
        ),
        no_offense_rate_a=no_offense[0] / turns[0] if turns[0] else 0.0,
        no_offense_rate_b=no_offense[1] / turns[1] if turns[1] else 0.0,
        average_offense_energy_spent_a=(
            offense_energy_spent[0] / turns[0] if turns[0] else 0.0
        ),
        average_offense_energy_spent_b=(
            offense_energy_spent[1] / turns[1] if turns[1] else 0.0
        ),
        average_defense_energy_spent_a=(
            defense_energy_spent[0] / turns[0] if turns[0] else 0.0
        ),
        average_defense_energy_spent_b=(
            defense_energy_spent[1] / turns[1] if turns[1] else 0.0
        ),
        average_reserved_energy_a=reserved_energy[0] / turns[0] if turns[0] else 0.0,
        average_reserved_energy_b=reserved_energy[1] / turns[1] if turns[1] else 0.0,
    )


def _create_combatant(
    catalog: Catalog,
    deck_id: str,
    profile: str,
    config: GameConfig,
    rng: random.Random,
) -> _Combatant:
    deck_definition = catalog.decks[deck_id]
    card_ids = [
        card_id
        for card_id, count in deck_definition.cards.items()
        for _ in range(count)
    ]
    rng.shuffle(card_ids)
    state = PlayerState(
        health=config.starting_health,
        max_health=config.starting_health,
        energy=config.energy_capacity,
        max_energy=config.energy_capacity,
        deck=card_ids,
    )
    _draw(state, config.opening_hand)
    return _Combatant(
        deck_id=deck_id,
        core_id=deck_definition.core_id,
        state=state,
        policy=HeuristicPolicy(profile),
    )


def _draw(player: PlayerState, amount: int) -> None:
    for _ in range(amount):
        if not player.deck:
            return
        player.hand.append(player.deck.pop(0))


_NO_WINNER = object()


def _winner(combatants: list[_Combatant]):
    dead = [combatant.state.health <= 0 for combatant in combatants]
    if dead == [False, False]:
        return _NO_WINNER
    if dead == [True, True]:
        return None
    return 0 if dead[1] else 1


def _game_result(
    combatants: list[_Combatant],
    winner: int | None,
    reason: str,
    full_rounds: int,
    turns: int,
    turns_by_player: list[int],
    combo_usage: list[Counter],
    standalone_usage: list[Counter],
    standalone_offense_actions: list[int],
    standalone_defense_actions: list[int],
    no_offense_turns: list[int],
    offense_energy_spent: list[int],
    defense_energy_spent: list[int],
    reserved_energy_after_offense: list[int],
    starting_player: int,
) -> GameResult:
    return GameResult(
        winner=winner,
        reason=reason,
        full_rounds=full_rounds,
        turns=turns,
        turns_by_player=(turns_by_player[0], turns_by_player[1]),
        remaining_health=(combatants[0].state.health, combatants[1].state.health),
        remaining_shield=(combatants[0].state.shield, combatants[1].state.shield),
        combo_usage=(
            tuple(sorted(combo_usage[0].items())),
            tuple(sorted(combo_usage[1].items())),
        ),
        standalone_usage=(
            tuple(sorted(standalone_usage[0].items())),
            tuple(sorted(standalone_usage[1].items())),
        ),
        standalone_offense_actions=(
            standalone_offense_actions[0],
            standalone_offense_actions[1],
        ),
        standalone_defense_actions=(
            standalone_defense_actions[0],
            standalone_defense_actions[1],
        ),
        no_offense_turns=(no_offense_turns[0], no_offense_turns[1]),
        offense_energy_spent=(offense_energy_spent[0], offense_energy_spent[1]),
        defense_energy_spent=(defense_energy_spent[0], defense_energy_spent[1]),
        reserved_energy_after_offense=(
            reserved_energy_after_offense[0],
            reserved_energy_after_offense[1],
        ),
        starting_player=starting_player,
    )


def _record_action_usage(
    action: CombatAction,
    player_index: int,
    combo_usage: list[Counter],
    standalone_usage: list[Counter],
) -> None:
    if isinstance(action, ComboAction):
        combo_usage[player_index][action.combo_id] += 1
    elif isinstance(action, StandaloneAction):
        standalone_usage[player_index][action.card_id] += 1


def _mean_ci95(values: list[float]) -> tuple[float, float]:
    mean = sum(values) / len(values)
    if len(values) == 1:
        return mean, mean
    variance = sum((value - mean) ** 2 for value in values) / (len(values) - 1)
    margin = 1.96 * math.sqrt(variance / len(values))
    return max(0.0, mean - margin), min(1.0, mean + margin)
