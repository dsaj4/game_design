from pathlib import Path

import pytest

from combat_lab.actions import StandaloneAction
from combat_lab.catalog import load_catalog
from combat_lab.engine import (
    PlayerState,
    resolve_action_exchange,
    resolve_exchange,
    tick_owner_turn_start,
)
from combat_lab.errors import IllegalAction


DATA_DIR = Path(__file__).parents[1] / "data"


@pytest.fixture
def catalog():
    return load_catalog(DATA_DIR)


def player(*card_ids, prepared=(), health=30, shield=0, energy=4):
    return PlayerState(
        health=health,
        max_health=30,
        shield=shield,
        energy=energy,
        max_energy=4,
        hand=list(card_ids),
        prepared=list(prepared),
        deck=[],
    )


def test_sheep_in_tiger_mouth_resolves_base_then_combo_damage(catalog) -> None:
    attacker = player("lamb_charge", "tiger_pounce")
    defender = player()

    result = resolve_exchange(
        catalog,
        attacker,
        defender,
        core_id="sheep_core",
        attack_combo_id="sheep_enters_tiger_mouth",
        attack_card_ids=["lamb_charge", "tiger_pounce"],
    )

    assert result.attack_damage == 6  # two base damage plus four combo damage
    assert defender.health == 24
    assert attacker.energy == 2
    assert attacker.hand == []
    assert attacker.discard == ["lamb_charge", "tiger_pounce"]


def test_insufficient_attack_energy_rolls_back_entire_exchange(catalog) -> None:
    attacker = player("lamb_charge", "tiger_pounce", energy=1)
    defender = player()

    with pytest.raises(IllegalAction, match="not enough energy"):
        resolve_exchange(
            catalog,
            attacker,
            defender,
            core_id="sheep_core",
            attack_combo_id="sheep_enters_tiger_mouth",
            attack_card_ids=["lamb_charge", "tiger_pounce"],
        )

    assert attacker.energy == 1
    assert attacker.hand == ["lamb_charge", "tiger_pounce"]
    assert attacker.discard == []
    assert defender.health == 30


def test_defense_combo_blocks_then_shield_absorbs_remaining_damage(catalog) -> None:
    attacker = player("current_surge", "boat_ram")
    defender = player(prepared=("flowing_water", "boat_guard"))

    result = resolve_exchange(
        catalog,
        attacker,
        defender,
        core_id="boat_core",
        attack_combo_id="row_against_current",
        attack_card_ids=["current_surge", "boat_ram"],
        defense_core_id="boat_core",
        defense_combo_id="push_boat_with_current",
        defense_card_ids=["flowing_water", "boat_guard"],
    )

    assert result.attack_damage == 4
    assert result.blocked_damage == 2
    assert result.shield_absorbed == 1
    assert defender.health == 29
    assert attacker.energy == 2
    assert defender.energy == 2


def test_unaffordable_defense_rolls_back_attack_and_defense(catalog) -> None:
    attacker = player("current_surge", "boat_ram", energy=2)
    defender = player(
        prepared=("flowing_water", "boat_guard"),
        energy=1,
    )

    with pytest.raises(IllegalAction, match="not enough energy"):
        resolve_exchange(
            catalog,
            attacker,
            defender,
            core_id="boat_core",
            attack_combo_id="row_against_current",
            attack_card_ids=["current_surge", "boat_ram"],
            defense_core_id="boat_core",
            defense_combo_id="push_boat_with_current",
            defense_card_ids=["flowing_water", "boat_guard"],
        )

    assert attacker.energy == 2
    assert attacker.hand == ["current_surge", "boat_ram"]
    assert defender.energy == 1
    assert defender.prepared == ["flowing_water", "boat_guard"]
    assert defender.health == 30


def test_standalone_actions_cost_one_and_only_resolve_base_effects(catalog) -> None:
    attacker = player("lamb_charge")
    defender = player(prepared=("wool_guard",), energy=1)

    result = resolve_action_exchange(
        catalog,
        attacker,
        defender,
        attack_core_id="sheep_core",
        attack_action=StandaloneAction("lamb_charge"),
        defense_core_id="sheep_core",
        defense_action=StandaloneAction("wool_guard"),
    )

    assert result.attack_damage == 1
    assert result.shield_absorbed == 1
    assert defender.health == 30
    assert attacker.energy == 3
    assert defender.energy == 0
    assert attacker.discard == ["lamb_charge"]
    assert defender.discard == ["wool_guard"]


def test_health_payment_cannot_reduce_player_to_zero(catalog) -> None:
    attacker = player("iron_pot_strike", "break_pot_resolve", health=3)
    defender = player()

    with pytest.raises(IllegalAction, match="must retain at least 1 health"):
        resolve_exchange(
            catalog,
            attacker,
            defender,
            core_id="boat_core",
            attack_combo_id="break_pot_sink_boat",
            attack_card_ids=["iron_pot_strike", "break_pot_resolve"],
        )

    assert attacker.health == 3
    assert attacker.hand == ["iron_pot_strike", "break_pot_resolve"]
    assert defender.health == 30


def test_persistent_combo_uses_slot_and_ticks_twice(catalog) -> None:
    attacker = player("lamb_charge", "tiger_pounce")
    defender = player(
        prepared=("lamb_charge", "wool_guard", "pasture_bell"),
        energy=1,
    )

    resolve_exchange(
        catalog,
        attacker,
        defender,
        core_id="sheep_core",
        attack_combo_id="sheep_enters_tiger_mouth",
        attack_card_ids=["lamb_charge", "tiger_pounce"],
        defense_core_id="sheep_core",
        defense_combo_id="three_sheep_blessing",
        defense_card_ids=["lamb_charge", "wool_guard", "pasture_bell"],
    )

    assert len(defender.statuses) == 1
    assert defender.statuses[0].remaining_triggers == 2
    assert attacker.health == 29  # attack-attribute material counterattacks in defense
    assert defender.energy == 0
    shield_after_exchange = defender.shield

    tick_owner_turn_start(catalog, defender)
    assert defender.energy == 4
    tick_owner_turn_start(catalog, defender)

    assert defender.shield == shield_after_exchange + 2
    assert defender.energy == 4
    assert defender.statuses == []


def test_attack_combo_cannot_be_used_as_defense(catalog) -> None:
    attacker = player("current_surge", "boat_ram")
    defender = player(prepared=("flowing_water", "boat_guard"))

    with pytest.raises(IllegalAction, match="is not a defense combo"):
        resolve_exchange(
            catalog,
            attacker,
            defender,
            core_id="boat_core",
            attack_combo_id="row_against_current",
            attack_card_ids=["current_surge", "boat_ram"],
            defense_core_id="boat_core",
            defense_combo_id="row_against_current",
            defense_card_ids=["flowing_water", "boat_guard"],
        )
