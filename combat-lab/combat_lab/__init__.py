"""Deterministic prototype rules for idiom-based core-card combat."""

from .catalog import load_catalog, validate_catalog
from .engine import PlayerState, resolve_exchange, tick_owner_turn_start
from .simulation import GameConfig, simulate_game, simulate_matchup

__all__ = [
    "PlayerState",
    "GameConfig",
    "load_catalog",
    "resolve_exchange",
    "simulate_game",
    "simulate_matchup",
    "tick_owner_turn_start",
    "validate_catalog",
]
