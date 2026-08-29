from collections import Counter
from pathlib import Path
import random

from combat_lab.battle003 import (
    Battle003Config,
    Battle003State,
    commit_synthesis,
    end_player_turn,
    enumerate_syntheses,
    load_battle003_catalog,
    resolve_context,
    simulate_battle003_game,
    simulate_battle003_matchup,
)
from combat_lab.errors import CatalogError


DATA_DIR = Path(__file__).parents[1] / "data"


def _all_cards(state: Battle003State) -> Counter[str]:
    return Counter([*state.draw_pile, *state.hand, *state.discard])


def test_first_battle003_catalog_is_valid_and_bounded() -> None:
    catalog = load_battle003_catalog(DATA_DIR)

    assert set(catalog.cores) == {"edge_core", "bastion_core"}
    general_recipes = [
        recipe for recipe in catalog.recipes.values() if recipe.core_id is None
    ]
    recipe_products = {recipe.product for recipe in catalog.recipes.values()}
    assert len([card for card in catalog.cards.values() if card.card_type == "glyph"]) >= 5
    assert len([card for card in catalog.cards.values() if card.card_type == "action"]) == 3
    assert len(general_recipes) >= 4
    assert any(
        material in recipe_products
        for recipe in catalog.recipes.values()
        for material in recipe.glyph_materials
    )
    assert all(
        recipe.glyph_materials
        for recipe in catalog.recipes.values()
    )
    assert all(
        not catalog.cards[card_id].effects
        for card_id in ("compress", "stack", "gather")
    )


def test_core_specific_recipe_only_appears_for_own_core() -> None:
    catalog = load_battle003_catalog(DATA_DIR)
    hand = ["water", "compress", "earth", "stack"]

    edge = {choice.recipe_id for choice in enumerate_syntheses(catalog, "edge_core", hand)}
    bastion = {
        choice.recipe_id
        for choice in enumerate_syntheses(catalog, "bastion_core", hand)
    }

    assert "edge_water_blade" in edge
    assert "edge_water_blade" not in bastion
    assert "bastion_stone_wall" in bastion
    assert "bastion_stone_wall" not in edge


def test_synthesis_permanently_replaces_glyph_and_keeps_action_card() -> None:
    catalog = load_battle003_catalog(DATA_DIR)
    state = Battle003State(hand=["water", "compress", "fire"])
    before = _all_cards(state)
    choice = next(
        choice
        for choice in enumerate_syntheses(catalog, "edge_core", state.hand)
        if choice.recipe_id == "edge_water_blade"
    )

    commit_synthesis(catalog, state, choice)

    assert state.hand == ["compress", "fire", "water_blade"]
    assert _all_cards(state) == before - Counter({"water": 1}) + Counter({"water_blade": 1})
    assert state.discovered_recipes == {"edge_water_blade"}


def test_two_glyph_synthesis_reduces_permanent_deck_by_one_card() -> None:
    catalog = load_battle003_catalog(DATA_DIR)
    state = Battle003State(hand=["fire", "air", "gather"])
    before_size = sum(_all_cards(state).values())
    choice = next(
        choice
        for choice in enumerate_syntheses(catalog, "edge_core", state.hand)
        if choice.recipe_id == "general_steam_burst"
    )

    commit_synthesis(catalog, state, choice)

    assert sum(_all_cards(state).values()) == before_size - 1
    assert state.hand == ["gather", "steam_burst"]


def test_end_turn_discards_entire_hand_and_clears_energy() -> None:
    state = Battle003State(
        energy=2,
        hand=["water", "compress", "earth"],
        discard=["fire"],
    )

    end_player_turn(state)

    assert state.hand == []
    assert state.discard == ["fire", "water", "compress", "earth"]
    assert state.energy == 0


def test_context_resolution_is_deterministic_for_same_card_target_and_state() -> None:
    catalog = load_battle003_catalog(DATA_DIR)

    first = resolve_context(catalog, "coal_outcrop", "gather", "fresh")
    second = resolve_context(catalog, "coal_outcrop", "gather", "fresh")

    assert first == second
    assert first.tier == "high"
    assert first.reward_card_id == "earth"
    assert first.next_state == "depleted"


def test_game_replays_identically_with_same_seed_and_trace() -> None:
    catalog = load_battle003_catalog(DATA_DIR)
    config = Battle003Config(capture_trace=True)

    first = simulate_battle003_game(
        catalog,
        core_id="edge_core",
        policy="balanced",
        seed=20260829,
        config=config,
    )
    second = simulate_battle003_game(
        catalog,
        core_id="edge_core",
        policy="balanced",
        seed=20260829,
        config=config,
    )

    assert first == second
    assert first.trace
    assert first.turns <= config.max_turns
    assert first.result in {"win", "loss", "draw"}


def test_matchup_report_is_reproducible_and_accounts_for_every_game() -> None:
    catalog = load_battle003_catalog(DATA_DIR)

    first = simulate_battle003_matchup(
        catalog,
        core_id="bastion_core",
        policy="balanced",
        games=50,
        seed=17,
    )
    second = simulate_battle003_matchup(
        catalog,
        core_id="bastion_core",
        policy="balanced",
        games=50,
        seed=17,
    )

    assert first == second
    assert first.wins + first.losses + first.draws == 50
    assert first.win_rate_ci95[0] <= first.win_rate <= first.win_rate_ci95[1]
    assert sum(first.recipe_usage.values()) > 0
    assert sum(first.card_usage.values()) > 0
    assert sum(first.action_catalyst_usage.values()) > 0
    assert 0.0 < first.action_draw_share < 1.0
    assert first.average_final_deck_size <= sum(catalog.starter_deck.values())
    assert 0.0 <= first.no_glyph_play_turn_rate <= 1.0


def test_simulation_safety_cap_must_be_positive() -> None:
    try:
        Battle003Config(max_turns=0)
    except ValueError as exc:
        assert "max turns must be positive" in str(exc)
    else:
        raise AssertionError("a non-positive simulation cap must be rejected")


def test_duplicate_catalog_ids_are_rejected_before_mapping(tmp_path: Path) -> None:
    source = (DATA_DIR / "battle003.json").read_text(encoding="utf-8")
    duplicate = source.replace(
        '"cards": [',
        '"cards": [{"id":"water","name":"重复","type":"glyph",'
        '"energy_cost":1,"effects":[]} ,',
        1,
    )
    (tmp_path / "battle003.json").write_text(duplicate, encoding="utf-8")

    try:
        load_battle003_catalog(tmp_path)
    except CatalogError as exc:
        assert "duplicate battle003 card id: water" in str(exc)
    else:
        raise AssertionError("duplicate ids must fail catalog loading")
