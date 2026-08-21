from pathlib import Path

from combat_lab.catalog import load_catalog
from combat_lab.simulation import GameConfig, simulate_game, simulate_matchup


DATA_DIR = Path(__file__).parents[1] / "data"


def test_game_is_reproducible_and_bounded_to_twelve_rounds() -> None:
    catalog = load_catalog(DATA_DIR)
    config = GameConfig(max_full_rounds=12)

    first = simulate_game(
        catalog,
        "sheep_starter_v0",
        "boat_starter_v0",
        seed=20260821,
        config=config,
    )
    second = simulate_game(
        catalog,
        "sheep_starter_v0",
        "boat_starter_v0",
        seed=20260821,
        config=config,
    )

    assert first == second
    assert 1 <= first.full_rounds <= 12
    assert first.winner in {0, 1, None}


def test_matchup_report_accounts_for_every_game() -> None:
    catalog = load_catalog(DATA_DIR)

    report = simulate_matchup(
        catalog,
        "sheep_starter_v0",
        "boat_starter_v0",
        games=40,
        seed=7,
    )

    assert report.deck_a_wins + report.deck_b_wins + report.draws == 40
    assert 0.0 <= report.deck_a_score_rate <= 1.0
    assert report.deck_a_score_ci95[0] <= report.deck_a_score_rate
    assert report.deck_a_score_ci95[1] >= report.deck_a_score_rate
    assert 0.0 <= report.starting_player_score_rate <= 1.0
    assert 0.0 <= report.deck_a_score_when_starting <= 1.0
    assert 0.0 <= report.deck_a_score_when_second <= 1.0
    assert sum(report.combo_usage_a.values()) > 0
    assert sum(report.combo_usage_b.values()) > 0


def test_alternating_starting_player_is_balanced_in_even_sample() -> None:
    catalog = load_catalog(DATA_DIR)

    report = simulate_matchup(
        catalog,
        "sheep_starter_v0",
        "boat_starter_v0",
        games=20,
        seed=11,
    )

    assert report.starts_a == 10
    assert report.starts_b == 10
