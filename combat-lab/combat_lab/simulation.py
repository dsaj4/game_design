from __future__ import annotations

import math
import random
from collections import Counter
from dataclasses import dataclass

from .catalog import Catalog
from .engine import PlayerState, release_prepared, resolve_exchange, tick_owner_turn_start
from .policies import HeuristicPolicy


@dataclass(frozen=True)
class GameConfig:
    starting_health: int = 30
    opening_hand: int = 4
    hand_limit: int = 7
    max_full_rounds: int = 12


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
    no_attack_turns: tuple[int, int]
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
    no_attack_rate_a: float
    no_attack_rate_b: float


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
    no_attack_turns = [0, 0]
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

            attack = active.policy.choose_attack(
                catalog,
                active.core_id,
                active.state,
                defending.core_id,
                defending.state,
            )
            if attack is None:
                no_attack_turns[active_index] += 1
                release_prepared(defending.state)
            else:
                defense = defending.policy.choose_defense(
                    catalog,
                    active.core_id,
                    attack,
                    active.state,
                    defending.core_id,
                    defending.state,
                )
                kwargs = {}
                if defense is not None:
                    kwargs = {
                        "defense_core_id": defending.core_id,
                        "defense_combo_id": defense.combo_id,
                        "defense_card_ids": list(defense.card_ids),
                    }
                    combo_usage[defending_index][defense.combo_id] += 1
                resolve_exchange(
                    catalog,
                    active.state,
                    defending.state,
                    core_id=active.core_id,
                    attack_combo_id=attack.combo_id,
                    attack_card_ids=list(attack.card_ids),
                    **kwargs,
                )
                combo_usage[active_index][attack.combo_id] += 1

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
                    no_attack_turns,
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
        no_attack_turns,
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
    no_attacks = [0, 0]
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
        no_attacks[0] += result.no_attack_turns[0]
        no_attacks[1] += result.no_attack_turns[1]
        turns[0] += result.turns_by_player[0]
        turns[1] += result.turns_by_player[1]
        combo_usage[0].update(dict(result.combo_usage[0]))
        combo_usage[1].update(dict(result.combo_usage[1]))
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
        no_attack_rate_a=no_attacks[0] / turns[0] if turns[0] else 0.0,
        no_attack_rate_b=no_attacks[1] / turns[1] if turns[1] else 0.0,
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
    no_attack_turns: list[int],
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
        no_attack_turns=(no_attack_turns[0], no_attack_turns[1]),
        starting_player=starting_player,
    )


def _mean_ci95(values: list[float]) -> tuple[float, float]:
    mean = sum(values) / len(values)
    if len(values) == 1:
        return mean, mean
    variance = sum((value - mean) ** 2 for value in values) / (len(values) - 1)
    margin = 1.96 * math.sqrt(variance / len(values))
    return max(0.0, mean - margin), min(1.0, mean + margin)
