from math import comb
from pathlib import Path

from combat_lab.analysis import analyze_availability
from combat_lab.catalog import load_catalog


DATA_DIR = Path(__file__).parents[1] / "data"


def test_analyzer_enumerates_every_four_card_opening_hand() -> None:
    catalog = load_catalog(DATA_DIR)

    report = analyze_availability(catalog, "sheep_starter_v0", 4)

    assert report.total_hands == comb(20, 4)
    assert 0 < report.any_attack_hits < report.total_hands
    assert 0 < report.any_defense_hits < report.total_hands


def test_one_card_persistent_combo_is_more_available_than_two_card_combo() -> None:
    catalog = load_catalog(DATA_DIR)

    report = analyze_availability(catalog, "boat_starter_v0", 4)

    assert report.combo_hits["same_boat_aid"] > report.combo_hits["row_against_current"]

