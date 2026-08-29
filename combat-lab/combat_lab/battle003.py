from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from itertools import combinations
import json
import math
from pathlib import Path
import random

from .errors import CatalogError, IllegalAction


ALLOWED_CARD_TYPES = {"glyph", "action"}
ALLOWED_EFFECTS = {"damage", "shield", "heal", "cancel_intent"}
ALLOWED_CONTEXT_TIERS = {"high", "general", "floor"}
POLICY003_PROFILES = ("balanced", "aggressive", "defensive")


@dataclass(frozen=True)
class Effect003:
    kind: str
    value: int


@dataclass(frozen=True)
class Card003:
    id: str
    name: str
    card_type: str
    energy_cost: int
    effects: tuple[Effect003, ...]


@dataclass(frozen=True)
class Recipe003:
    id: str
    name: str
    core_id: str | None
    glyph_materials: tuple[str, ...]
    action_materials: tuple[str, ...]
    product: str


@dataclass(frozen=True)
class Core003:
    id: str
    name: str


@dataclass(frozen=True)
class EnemyIntent003:
    id: str
    name: str
    damage: int
    hits: int
    status: str | None = None
    status_value: int = 0

    @property
    def total_damage(self) -> int:
        return self.damage * self.hits


@dataclass(frozen=True)
class Enemy003:
    id: str
    name: str
    health: int
    intents: tuple[EnemyIntent003, ...]


@dataclass(frozen=True)
class ContextOutcome003:
    card_id: str
    required_state: str
    tier: str
    reward_card_id: str
    next_state: str


@dataclass(frozen=True)
class Context003:
    id: str
    name: str
    outcomes: tuple[ContextOutcome003, ...]


@dataclass(frozen=True)
class Battle003Catalog:
    cards: dict[str, Card003]
    recipes: dict[str, Recipe003]
    cores: dict[str, Core003]
    starter_deck: dict[str, int]
    enemy: Enemy003
    contexts: dict[str, Context003]


@dataclass
class Battle003State:
    health: int = 30
    max_health: int = 30
    shield: int = 0
    energy: int = 0
    max_energy: int = 4
    weakened: int = 0
    draw_pile: list[str] = field(default_factory=list)
    hand: list[str] = field(default_factory=list)
    discard: list[str] = field(default_factory=list)
    discovered_recipes: set[str] = field(default_factory=set)


@dataclass(frozen=True, order=True)
class SynthesisChoice003:
    recipe_id: str
    glyph_indexes: tuple[int, ...]
    action_indexes: tuple[int, ...]


@dataclass(frozen=True)
class Battle003Config:
    starting_health: int = 30
    energy_capacity: int = 4
    draw_count: int = 5
    max_turns: int = 30
    capture_trace: bool = False

    def __post_init__(self) -> None:
        if self.starting_health < 1:
            raise ValueError("battle003 starting health must be positive")
        if self.energy_capacity < 0:
            raise ValueError("battle003 energy capacity cannot be negative")
        if self.draw_count < 1:
            raise ValueError("battle003 draw count must be positive")
        if self.max_turns < 1:
            raise ValueError("battle003 max turns must be positive")


@dataclass(frozen=True)
class Battle003GameResult:
    result: str
    turns: int
    remaining_player_health: int
    remaining_enemy_health: int
    final_deck_counts: tuple[tuple[str, int], ...]
    discovered_recipes: tuple[str, ...]
    synthesis_count: int
    recipe_usage: tuple[tuple[str, int], ...]
    card_usage: tuple[tuple[str, int], ...]
    action_catalyst_usage: tuple[tuple[str, int], ...]
    intent_cancels: int
    empty_hand_turns: int
    no_glyph_play_turns: int
    action_cards_drawn: int
    total_cards_drawn: int
    energy_spent: int
    trace: tuple[str, ...]


@dataclass(frozen=True)
class Battle003MatchupReport:
    core_id: str
    policy: str
    games: int
    wins: int
    losses: int
    draws: int
    win_rate: float
    win_rate_ci95: tuple[float, float]
    average_turns: float
    average_remaining_health: float
    average_enemy_health: float
    average_syntheses: float
    average_intent_cancels: float
    average_final_deck_size: float
    average_energy_spent_per_turn: float
    action_draw_share: float
    empty_hand_turn_rate: float
    no_glyph_play_turn_rate: float
    recipe_usage: dict[str, int]
    card_usage: dict[str, int]
    action_catalyst_usage: dict[str, int]


@dataclass(frozen=True)
class _PolicyWeights003:
    damage: float
    prevention: float
    healing: float
    synthesis_threshold: float


@dataclass(frozen=True)
class _PlayPlan003:
    indexes: tuple[int, ...]
    score: float
    damage: int
    shield: int
    healing: int
    cancels_intent: bool
    energy_cost: int


POLICY_WEIGHTS003 = {
    "balanced": _PolicyWeights003(1.0, 1.1, 1.0, 0.5),
    "aggressive": _PolicyWeights003(1.4, 0.65, 0.55, 0.25),
    "defensive": _PolicyWeights003(0.8, 1.5, 1.2, 0.5),
}


def load_battle003_catalog(data_dir: Path | str) -> Battle003Catalog:
    path = Path(data_dir) / "battle003.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    raw_cards = _unique_items_by_id(data["cards"], "battle003 card")
    raw_recipes = _unique_items_by_id(data["recipes"], "battle003 recipe")
    raw_cores = _unique_items_by_id(data["cores"], "battle003 core")
    raw_contexts = _unique_items_by_id(data.get("contexts", []), "battle003 context")
    cards = {
        item["id"]: Card003(
            id=item["id"],
            name=item["name"],
            card_type=item["type"],
            energy_cost=int(item["energy_cost"]),
            effects=tuple(
                Effect003(kind=effect["kind"], value=int(effect["value"]))
                for effect in item.get("effects", [])
            ),
        )
        for item in raw_cards
    }
    recipes = {
        item["id"]: Recipe003(
            id=item["id"],
            name=item["name"],
            core_id=item.get("core_id"),
            glyph_materials=tuple(item["glyph_materials"]),
            action_materials=tuple(item.get("action_materials", [])),
            product=item["product"],
        )
        for item in raw_recipes
    }
    cores = {
        item["id"]: Core003(id=item["id"], name=item["name"])
        for item in raw_cores
    }
    enemy_data = data["enemy"]
    enemy = Enemy003(
        id=enemy_data["id"],
        name=enemy_data["name"],
        health=int(enemy_data["health"]),
        intents=tuple(
            EnemyIntent003(
                id=item["id"],
                name=item["name"],
                damage=int(item["damage"]),
                hits=int(item["hits"]),
                status=item.get("status"),
                status_value=int(item.get("status_value", 0)),
            )
            for item in enemy_data["intents"]
        ),
    )
    contexts = {
        item["id"]: Context003(
            id=item["id"],
            name=item["name"],
            outcomes=tuple(
                ContextOutcome003(
                    card_id=outcome["card_id"],
                    required_state=outcome["required_state"],
                    tier=outcome["tier"],
                    reward_card_id=outcome["reward_card_id"],
                    next_state=outcome["next_state"],
                )
                for outcome in item["outcomes"]
            ),
        )
        for item in raw_contexts
    }
    catalog = Battle003Catalog(
        cards=cards,
        recipes=recipes,
        cores=cores,
        starter_deck={card_id: int(count) for card_id, count in data["starter_deck"].items()},
        enemy=enemy,
        contexts=contexts,
    )
    validate_battle003_catalog(catalog)
    return catalog


def validate_battle003_catalog(catalog: Battle003Catalog) -> None:
    if len(catalog.cards) != len(set(catalog.cards)):
        raise CatalogError("battle003 card ids must be unique")
    for card in catalog.cards.values():
        if card.card_type not in ALLOWED_CARD_TYPES:
            raise CatalogError(f"{card.id}: unknown card type {card.card_type}")
        if card.card_type == "action":
            if card.energy_cost != 0 or card.effects:
                raise CatalogError(f"{card.id}: action cards must be free and have no direct effects")
        elif card.energy_cost < 1:
            raise CatalogError(f"{card.id}: glyph cards must have a positive play cost")
        for effect in card.effects:
            if effect.kind not in ALLOWED_EFFECTS or effect.value < 1:
                raise CatalogError(f"{card.id}: invalid effect {effect.kind} {effect.value}")

    signatures: dict[str, set[tuple[tuple[str, ...], tuple[str, ...]]]] = {
        core_id: set() for core_id in catalog.cores
    }
    for recipe in catalog.recipes.values():
        if recipe.core_id is not None and recipe.core_id not in catalog.cores:
            raise CatalogError(f"{recipe.id}: unknown core {recipe.core_id}")
        if not recipe.glyph_materials:
            raise CatalogError(f"{recipe.id}: at least one glyph material is required")
        if recipe.product not in catalog.cards:
            raise CatalogError(f"{recipe.id}: unknown product {recipe.product}")
        if catalog.cards[recipe.product].card_type != "glyph":
            raise CatalogError(f"{recipe.id}: first-test products must be glyph cards")
        for card_id in recipe.glyph_materials:
            _require_card_type(catalog, recipe.id, card_id, "glyph")
        for card_id in recipe.action_materials:
            _require_card_type(catalog, recipe.id, card_id, "action")
        signature = (
            tuple(sorted(recipe.glyph_materials)),
            tuple(sorted(recipe.action_materials)),
        )
        applicable_cores = (
            catalog.cores.keys() if recipe.core_id is None else (recipe.core_id,)
        )
        for core_id in applicable_cores:
            if signature in signatures[core_id]:
                raise CatalogError(f"{core_id}: ambiguous recipe materials for {recipe.id}")
            signatures[core_id].add(signature)

    for core_id in catalog.cores:
        if not any(recipe.core_id == core_id for recipe in catalog.recipes.values()):
            raise CatalogError(f"{core_id}: first test needs core-specific recipes")
        _validate_recipe_graph(catalog, core_id)

    if not catalog.starter_deck or any(count < 1 for count in catalog.starter_deck.values()):
        raise CatalogError("battle003 starter deck counts must be positive")
    unknown_deck_cards = set(catalog.starter_deck) - set(catalog.cards)
    if unknown_deck_cards:
        raise CatalogError(f"battle003 starter deck has unknown cards: {sorted(unknown_deck_cards)}")
    glyph_types = {
        card_id
        for card_id in catalog.starter_deck
        if catalog.cards[card_id].card_type == "glyph"
    }
    action_types = {
        card_id
        for card_id in catalog.starter_deck
        if catalog.cards[card_id].card_type == "action"
    }
    if len(glyph_types) < 5 or len(action_types) != 3:
        raise CatalogError("battle003 first test needs at least five glyphs and exactly three actions")

    if catalog.enemy.health < 1 or not catalog.enemy.intents:
        raise CatalogError("battle003 enemy must have health and intents")
    for intent in catalog.enemy.intents:
        if intent.damage < 0 or intent.hits < 1:
            raise CatalogError(f"{intent.id}: invalid damage or hit count")
        if intent.status not in {None, "weaken"}:
            raise CatalogError(f"{intent.id}: unsupported status {intent.status}")
        if intent.status is None and intent.status_value != 0:
            raise CatalogError(f"{intent.id}: status value requires a status")

    for context in catalog.contexts.values():
        seen: set[tuple[str, str]] = set()
        for outcome in context.outcomes:
            key = (outcome.card_id, outcome.required_state)
            if key in seen:
                raise CatalogError(f"{context.id}: duplicate deterministic outcome {key}")
            seen.add(key)
            if outcome.card_id not in catalog.cards or outcome.reward_card_id not in catalog.cards:
                raise CatalogError(f"{context.id}: context references an unknown card")
            if outcome.tier not in ALLOWED_CONTEXT_TIERS:
                raise CatalogError(f"{context.id}: invalid tier {outcome.tier}")


def enumerate_syntheses(
    catalog: Battle003Catalog,
    core_id: str,
    hand: list[str],
) -> list[SynthesisChoice003]:
    if core_id not in catalog.cores:
        raise CatalogError(f"unknown battle003 core: {core_id}")
    choices: list[SynthesisChoice003] = []
    for recipe in sorted(catalog.recipes.values(), key=lambda item: item.id):
        if recipe.core_id not in {None, core_id}:
            continue
        glyph_sets = _matching_index_sets(hand, recipe.glyph_materials)
        action_sets = _matching_index_sets(hand, recipe.action_materials)
        for glyph_indexes in glyph_sets:
            for action_indexes in action_sets:
                if set(glyph_indexes).isdisjoint(action_indexes):
                    choices.append(
                        SynthesisChoice003(
                            recipe_id=recipe.id,
                            glyph_indexes=glyph_indexes,
                            action_indexes=action_indexes,
                        )
                    )
    return sorted(set(choices))


def commit_synthesis(
    catalog: Battle003Catalog,
    state: Battle003State,
    choice: SynthesisChoice003,
) -> None:
    try:
        recipe = catalog.recipes[choice.recipe_id]
    except KeyError as exc:
        raise IllegalAction(f"unknown battle003 recipe: {choice.recipe_id}") from exc
    if choice not in enumerate_syntheses(
        catalog,
        recipe.core_id or _only_compatible_core(catalog, recipe, state.hand),
        state.hand,
    ):
        raise IllegalAction("synthesis materials are no longer available")
    for index in sorted(choice.glyph_indexes, reverse=True):
        state.hand.pop(index)
    state.hand.append(recipe.product)
    state.discovered_recipes.add(recipe.id)


def end_player_turn(state: Battle003State) -> None:
    state.discard.extend(state.hand)
    state.hand.clear()
    state.energy = 0


def resolve_context(
    catalog: Battle003Catalog,
    context_id: str,
    card_id: str,
    target_state: str,
) -> ContextOutcome003:
    try:
        context = catalog.contexts[context_id]
    except KeyError as exc:
        raise IllegalAction(f"unknown context: {context_id}") from exc
    for outcome in context.outcomes:
        if outcome.card_id == card_id and outcome.required_state == target_state:
            return outcome
    raise IllegalAction(f"{card_id} is not relevant to {context_id} in state {target_state}")


def simulate_battle003_game(
    catalog: Battle003Catalog,
    *,
    core_id: str,
    policy: str,
    seed: int,
    config: Battle003Config | None = None,
) -> Battle003GameResult:
    if core_id not in catalog.cores:
        raise ValueError(f"unknown battle003 core: {core_id}")
    if policy not in POLICY_WEIGHTS003:
        raise ValueError(f"unknown battle003 policy: {policy}")
    config = config or Battle003Config()
    rng = random.Random(seed)
    draw_pile = [
        card_id
        for card_id, count in sorted(catalog.starter_deck.items())
        for _ in range(count)
    ]
    rng.shuffle(draw_pile)
    state = Battle003State(
        health=config.starting_health,
        max_health=config.starting_health,
        energy=0,
        max_energy=config.energy_capacity,
        draw_pile=draw_pile,
    )
    enemy_health = catalog.enemy.health
    recipe_usage: Counter[str] = Counter()
    card_usage: Counter[str] = Counter()
    action_catalyst_usage: Counter[str] = Counter()
    intent_cancels = 0
    empty_hand_turns = 0
    no_glyph_play_turns = 0
    action_cards_drawn = 0
    total_cards_drawn = 0
    energy_spent = 0
    trace: list[str] = []

    for turn in range(1, config.max_turns + 1):
        intent = catalog.enemy.intents[(turn - 1) % len(catalog.enemy.intents)]
        _start_player_turn(state, config.draw_count, rng)
        total_cards_drawn += len(state.hand)
        action_cards_drawn += sum(
            catalog.cards[card_id].card_type == "action" for card_id in state.hand
        )
        if not state.hand:
            empty_hand_turns += 1
        _trace(
            trace,
            config,
            f"turn:{turn}:intent:{intent.id}:{intent.damage}x{intent.hits}:hand:{','.join(state.hand)}",
        )

        synthesis_steps = 0
        while True:
            choice = _choose_synthesis(catalog, core_id, state, enemy_health, intent, policy)
            if choice is None:
                break
            recipe = catalog.recipes[choice.recipe_id]
            action_materials = [state.hand[index] for index in choice.action_indexes]
            commit_synthesis(catalog, state, choice)
            recipe_usage[recipe.id] += 1
            action_catalyst_usage.update(action_materials)
            synthesis_steps += 1
            _trace(trace, config, f"synthesis:{recipe.id}:{recipe.product}")
            if synthesis_steps > 32:
                raise RuntimeError("battle003 synthesis failed to terminate")

        plan = _choose_play_plan(catalog, state, enemy_health, intent, policy)
        if not plan.indexes:
            no_glyph_play_turns += 1
        intent_cancelled = False
        for index in sorted(plan.indexes, reverse=True):
            card_id = state.hand.pop(index)
            card = catalog.cards[card_id]
            state.energy -= card.energy_cost
            energy_spent += card.energy_cost
            state.discard.append(card_id)
            card_usage[card_id] += 1
            for effect in card.effects:
                if effect.kind == "damage":
                    damage = max(0, effect.value - state.weakened)
                    enemy_health -= damage
                    _trace(trace, config, f"play:{card_id}:damage:{damage}")
                elif effect.kind == "shield":
                    state.shield += effect.value
                    _trace(trace, config, f"play:{card_id}:shield:{effect.value}")
                elif effect.kind == "heal":
                    healed = min(effect.value, state.max_health - state.health)
                    state.health += healed
                    _trace(trace, config, f"play:{card_id}:heal:{healed}")
                elif effect.kind == "cancel_intent":
                    intent_cancelled = True
                    _trace(trace, config, f"play:{card_id}:cancel:{intent.id}")

        if enemy_health <= 0:
            return _battle003_result(
                state,
                "win",
                turn,
                enemy_health,
                recipe_usage,
                card_usage,
                action_catalyst_usage,
                intent_cancels,
                empty_hand_turns,
                no_glyph_play_turns,
                action_cards_drawn,
                total_cards_drawn,
                energy_spent,
                trace,
            )

        state.weakened = 0
        end_player_turn(state)
        if intent_cancelled:
            intent_cancels += 1
        else:
            for _ in range(intent.hits):
                absorbed = min(state.shield, intent.damage)
                state.shield -= absorbed
                state.health -= intent.damage - absorbed
            if intent.status == "weaken":
                state.weakened = intent.status_value
            _trace(
                trace,
                config,
                f"enemy:{intent.id}:health:{state.health}:shield:{state.shield}",
            )
        if state.health <= 0:
            return _battle003_result(
                state,
                "loss",
                turn,
                enemy_health,
                recipe_usage,
                card_usage,
                action_catalyst_usage,
                intent_cancels,
                empty_hand_turns,
                no_glyph_play_turns,
                action_cards_drawn,
                total_cards_drawn,
                energy_spent,
                trace,
            )

    return _battle003_result(
        state,
        "draw",
        config.max_turns,
        enemy_health,
        recipe_usage,
        card_usage,
        action_catalyst_usage,
        intent_cancels,
        empty_hand_turns,
        no_glyph_play_turns,
        action_cards_drawn,
        total_cards_drawn,
        energy_spent,
        trace,
    )


def simulate_battle003_matchup(
    catalog: Battle003Catalog,
    *,
    core_id: str,
    policy: str,
    games: int,
    seed: int,
    config: Battle003Config | None = None,
) -> Battle003MatchupReport:
    if games < 1:
        raise ValueError("games must be positive")
    rng = random.Random(seed)
    wins = 0
    losses = 0
    draws = 0
    turns = 0
    remaining_health = 0
    enemy_health = 0
    syntheses = 0
    intent_cancels = 0
    empty_hand_turns = 0
    no_glyph_play_turns = 0
    final_deck_size = 0
    action_cards_drawn = 0
    total_cards_drawn = 0
    energy_spent = 0
    recipe_usage: Counter[str] = Counter()
    card_usage: Counter[str] = Counter()
    action_catalyst_usage: Counter[str] = Counter()

    for _ in range(games):
        result = simulate_battle003_game(
            catalog,
            core_id=core_id,
            policy=policy,
            seed=rng.randrange(0, 2**63),
            config=config,
        )
        wins += int(result.result == "win")
        losses += int(result.result == "loss")
        draws += int(result.result == "draw")
        turns += result.turns
        remaining_health += result.remaining_player_health
        enemy_health += max(0, result.remaining_enemy_health)
        syntheses += result.synthesis_count
        intent_cancels += result.intent_cancels
        empty_hand_turns += result.empty_hand_turns
        no_glyph_play_turns += result.no_glyph_play_turns
        final_deck_size += sum(count for _, count in result.final_deck_counts)
        action_cards_drawn += result.action_cards_drawn
        total_cards_drawn += result.total_cards_drawn
        energy_spent += result.energy_spent
        recipe_usage.update(dict(result.recipe_usage))
        card_usage.update(dict(result.card_usage))
        action_catalyst_usage.update(dict(result.action_catalyst_usage))

    win_rate = wins / games
    total_turns = turns or 1
    return Battle003MatchupReport(
        core_id=core_id,
        policy=policy,
        games=games,
        wins=wins,
        losses=losses,
        draws=draws,
        win_rate=win_rate,
        win_rate_ci95=_proportion_ci95(win_rate, games),
        average_turns=turns / games,
        average_remaining_health=remaining_health / games,
        average_enemy_health=enemy_health / games,
        average_syntheses=syntheses / games,
        average_intent_cancels=intent_cancels / games,
        average_final_deck_size=final_deck_size / games,
        average_energy_spent_per_turn=energy_spent / total_turns,
        action_draw_share=action_cards_drawn / (total_cards_drawn or 1),
        empty_hand_turn_rate=empty_hand_turns / total_turns,
        no_glyph_play_turn_rate=no_glyph_play_turns / total_turns,
        recipe_usage=dict(sorted(recipe_usage.items())),
        card_usage=dict(sorted(card_usage.items())),
        action_catalyst_usage=dict(sorted(action_catalyst_usage.items())),
    )


def _start_player_turn(state: Battle003State, draw_count: int, rng: random.Random) -> None:
    state.energy = state.max_energy
    if len(state.draw_pile) < draw_count and state.discard:
        recycled = list(state.discard)
        state.discard.clear()
        rng.shuffle(recycled)
        state.draw_pile.extend(recycled)
    amount = min(draw_count, len(state.draw_pile))
    state.hand.extend(state.draw_pile[:amount])
    del state.draw_pile[:amount]


def _choose_synthesis(
    catalog: Battle003Catalog,
    core_id: str,
    state: Battle003State,
    enemy_health: int,
    intent: EnemyIntent003,
    policy: str,
) -> SynthesisChoice003 | None:
    weights = POLICY_WEIGHTS003[policy]
    best_choice: SynthesisChoice003 | None = None
    best_gain = weights.synthesis_threshold
    for choice in enumerate_syntheses(catalog, core_id, state.hand):
        recipe = catalog.recipes[choice.recipe_id]
        product_value = _card_utility(
            catalog.cards[recipe.product], state, enemy_health, intent, weights
        )
        material_value = sum(
            _card_utility(catalog.cards[state.hand[index]], state, enemy_health, intent, weights)
            for index in choice.glyph_indexes
        )
        gain = product_value - material_value * 0.7
        if gain > best_gain or (
            math.isclose(gain, best_gain)
            and best_choice is not None
            and choice < best_choice
        ):
            best_gain = gain
            best_choice = choice
    return best_choice


def _choose_play_plan(
    catalog: Battle003Catalog,
    state: Battle003State,
    enemy_health: int,
    intent: EnemyIntent003,
    policy: str,
) -> _PlayPlan003:
    glyph_indexes = [
        index
        for index, card_id in enumerate(state.hand)
        if catalog.cards[card_id].card_type == "glyph"
    ]
    weights = POLICY_WEIGHTS003[policy]
    best = _PlayPlan003((), 0.0, 0, 0, 0, False, 0)
    best_signature: tuple[str, ...] = ()
    for count in range(1, len(glyph_indexes) + 1):
        for indexes in combinations(glyph_indexes, count):
            cards = [catalog.cards[state.hand[index]] for index in indexes]
            energy_cost = sum(card.energy_cost for card in cards)
            if energy_cost > state.energy:
                continue
            damage = sum(
                max(0, effect.value - state.weakened)
                for card in cards
                for effect in card.effects
                if effect.kind == "damage"
            )
            shield = sum(
                effect.value
                for card in cards
                for effect in card.effects
                if effect.kind == "shield"
            )
            healing = min(
                state.max_health - state.health,
                sum(
                    effect.value
                    for card in cards
                    for effect in card.effects
                    if effect.kind == "heal"
                ),
            )
            cancels = any(
                effect.kind == "cancel_intent"
                for card in cards
                for effect in card.effects
            )
            incoming = 0 if cancels else intent.total_damage
            prevented = min(incoming, state.shield + shield) - min(incoming, state.shield)
            if cancels:
                prevented = max(0, intent.total_damage - state.shield)
            score = (
                min(enemy_health, damage) * weights.damage
                + prevented * weights.prevention
                + healing * weights.healing
                - energy_cost * 0.03
            )
            signature = tuple(sorted(card.id for card in cards))
            if score > best.score or (
                math.isclose(score, best.score) and signature < best_signature
            ):
                best = _PlayPlan003(
                    indexes=tuple(indexes),
                    score=score,
                    damage=damage,
                    shield=shield,
                    healing=healing,
                    cancels_intent=cancels,
                    energy_cost=energy_cost,
                )
                best_signature = signature
    return best


def _card_utility(
    card: Card003,
    state: Battle003State,
    enemy_health: int,
    intent: EnemyIntent003,
    weights: _PolicyWeights003,
) -> float:
    value = 0.0
    for effect in card.effects:
        if effect.kind == "damage":
            value += min(enemy_health, max(0, effect.value - state.weakened)) * weights.damage
        elif effect.kind == "shield":
            prevented = min(effect.value, max(0, intent.total_damage - state.shield))
            value += prevented * weights.prevention + (effect.value - prevented) * 0.15
        elif effect.kind == "heal":
            value += min(effect.value, state.max_health - state.health) * weights.healing
        elif effect.kind == "cancel_intent":
            value += max(0, intent.total_damage - state.shield) * weights.prevention
    return value - card.energy_cost * 0.03


def _matching_index_sets(hand: list[str], required: tuple[str, ...]) -> list[tuple[int, ...]]:
    if not required:
        return [()]
    required_counts = Counter(required)
    return [
        indexes
        for indexes in combinations(range(len(hand)), len(required))
        if Counter(hand[index] for index in indexes) == required_counts
    ]


def _require_card_type(
    catalog: Battle003Catalog,
    recipe_id: str,
    card_id: str,
    expected: str,
) -> None:
    try:
        card = catalog.cards[card_id]
    except KeyError as exc:
        raise CatalogError(f"{recipe_id}: unknown material {card_id}") from exc
    if card.card_type != expected:
        raise CatalogError(f"{recipe_id}: {card_id} must be a {expected} card")


def _unique_items_by_id(items: list[dict[str, object]], label: str) -> list[dict[str, object]]:
    seen: set[str] = set()
    for item in items:
        item_id = str(item.get("id", ""))
        if not item_id:
            raise CatalogError(f"{label} is missing an id")
        if item_id in seen:
            raise CatalogError(f"duplicate {label} id: {item_id}")
        seen.add(item_id)
    return items


def _validate_recipe_graph(catalog: Battle003Catalog, core_id: str) -> None:
    graph: dict[str, set[str]] = {}
    for recipe in catalog.recipes.values():
        if recipe.core_id not in {None, core_id}:
            continue
        for material in recipe.glyph_materials:
            graph.setdefault(material, set()).add(recipe.product)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(card_id: str) -> None:
        if card_id in visiting:
            raise CatalogError(f"{core_id}: synthesis recipe graph contains a cycle at {card_id}")
        if card_id in visited:
            return
        visiting.add(card_id)
        for product in sorted(graph.get(card_id, ())):
            visit(product)
        visiting.remove(card_id)
        visited.add(card_id)

    for card_id in sorted(graph):
        visit(card_id)


def _only_compatible_core(
    catalog: Battle003Catalog,
    recipe: Recipe003,
    hand: list[str],
) -> str:
    compatible = [
        core_id
        for core_id in sorted(catalog.cores)
        if any(
            choice.recipe_id == recipe.id
            for choice in enumerate_syntheses(catalog, core_id, hand)
        )
    ]
    if not compatible:
        raise IllegalAction("synthesis recipe is not compatible with the current hand")
    return compatible[0]


def _battle003_result(
    state: Battle003State,
    result: str,
    turns: int,
    enemy_health: int,
    recipe_usage: Counter[str],
    card_usage: Counter[str],
    action_catalyst_usage: Counter[str],
    intent_cancels: int,
    empty_hand_turns: int,
    no_glyph_play_turns: int,
    action_cards_drawn: int,
    total_cards_drawn: int,
    energy_spent: int,
    trace: list[str],
) -> Battle003GameResult:
    deck_counts = Counter([*state.draw_pile, *state.hand, *state.discard])
    return Battle003GameResult(
        result=result,
        turns=turns,
        remaining_player_health=max(0, state.health),
        remaining_enemy_health=max(0, enemy_health),
        final_deck_counts=tuple(sorted(deck_counts.items())),
        discovered_recipes=tuple(sorted(state.discovered_recipes)),
        synthesis_count=sum(recipe_usage.values()),
        recipe_usage=tuple(sorted(recipe_usage.items())),
        card_usage=tuple(sorted(card_usage.items())),
        action_catalyst_usage=tuple(sorted(action_catalyst_usage.items())),
        intent_cancels=intent_cancels,
        empty_hand_turns=empty_hand_turns,
        no_glyph_play_turns=no_glyph_play_turns,
        action_cards_drawn=action_cards_drawn,
        total_cards_drawn=total_cards_drawn,
        energy_spent=energy_spent,
        trace=tuple(trace),
    )


def _trace(trace: list[str], config: Battle003Config, message: str) -> None:
    if config.capture_trace:
        trace.append(message)


def _proportion_ci95(value: float, samples: int) -> tuple[float, float]:
    z = 1.96
    denominator = 1.0 + z * z / samples
    center = (value + z * z / (2.0 * samples)) / denominator
    margin = (
        z
        * math.sqrt(value * (1.0 - value) / samples + z * z / (4.0 * samples**2))
        / denominator
    )
    return max(0.0, center - margin), min(1.0, center + margin)
