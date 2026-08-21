from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .actions import enumerate_combo_actions
from .analysis import analyze_availability
from .catalog import load_catalog
from .policies import PROFILES
from .simulation import simulate_matchup


DATA_DIR = Path(__file__).parents[1] / "data"


def main() -> None:
    parser = argparse.ArgumentParser(description="成语组合战斗独立测试工具")
    parser.add_argument(
        "command",
        choices=("validate", "show", "analyze", "enumerate", "simulate"),
        nargs="?",
        default="validate",
    )
    parser.add_argument("--games", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260821)
    parser.add_argument("--deck-a", default="sheep_starter_v0")
    parser.add_argument("--deck-b", default="boat_starter_v0")
    parser.add_argument("--policy-a", choices=tuple(PROFILES), default="balanced")
    parser.add_argument("--policy-b", choices=tuple(PROFILES), default="balanced")
    parser.add_argument("--core", default="sheep_core")
    parser.add_argument("--nature", choices=("attack", "defense"), default="attack")
    parser.add_argument(
        "--cards",
        default="lamb_charge,tiger_pounce,wool_guard,guiding_hand",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    catalog = load_catalog(DATA_DIR)

    if args.command == "validate":
        combo_count = sum(len(core.combos) for core in catalog.core_cards.values())
        print(
            "OK: "
            f"{len(catalog.auxiliary_cards)} 张辅助卡模板，"
            f"{len(catalog.core_cards)} 张核心卡，"
            f"{combo_count} 个组合，"
            f"{len(catalog.decks)} 套 20 卡测试卡组"
        )
        return

    if args.command == "analyze":
        for deck in catalog.decks.values():
            core = catalog.core_cards[deck.core_id]
            print(f"[{deck.name}]")
            for hand_size in (4, 5):
                report = analyze_availability(catalog, deck.id, hand_size)
                print(
                    f"可见 {hand_size} 张: 任意组合 "
                    f"{report.probability(report.any_combo_hits):.1%}; "
                    f"攻击 {report.probability(report.any_attack_hits):.1%}; "
                    f"防御 {report.probability(report.any_defense_hits):.1%}"
                )
                for combo in core.combos:
                    print(
                        f"  - {combo.name}: "
                        f"{report.probability(report.combo_hits[combo.id]):.1%}"
                    )
        return

    if args.command == "enumerate":
        card_ids = [card_id.strip() for card_id in args.cards.split(",") if card_id.strip()]
        actions = enumerate_combo_actions(
            catalog,
            args.core,
            card_ids,
            args.nature,
        )
        print(f"{args.core} / {args.nature}: {len(actions)} 个合法组合动作")
        for action in actions:
            combo = catalog.combo(args.core, action.combo_id)
            card_names = " + ".join(
                catalog.auxiliary_cards[card_id].name for card_id in action.card_ids
            )
            print(f"- {combo.name}: {card_names}")
        return

    if args.command == "simulate":
        report = simulate_matchup(
            catalog,
            args.deck_a,
            args.deck_b,
            games=args.games,
            seed=args.seed,
            policy_a=args.policy_a,
            policy_b=args.policy_b,
        )
        if args.json:
            print(json.dumps(asdict(report), ensure_ascii=False, indent=2))
            return
        low, high = report.deck_a_score_ci95
        print(f"{report.deck_a} vs {report.deck_b} ({report.games} 局)")
        print(
            f"A胜 {report.deck_a_wins} / B胜 {report.deck_b_wins} / "
            f"平局 {report.draws}"
        )
        print(
            f"A对局得分率 {report.deck_a_score_rate:.1%} "
            f"(95% CI {low:.1%}-{high:.1%})"
        )
        print(
            f"平均 {report.average_full_rounds:.2f} 完整回合；"
            f"击倒率 {report.knockout_rate:.1%}；"
            f"先手得分率 {report.starting_player_score_rate:.1%}"
        )
        print(
            f"A先手得分率 {report.deck_a_score_when_starting:.1%}；"
            f"A后手得分率 {report.deck_a_score_when_second:.1%}"
        )
        print(
            f"无攻击组合回合率: A {report.no_attack_rate_a:.1%}; "
            f"B {report.no_attack_rate_b:.1%}"
        )
        print(f"A组合使用: {report.combo_usage_a}")
        print(f"B组合使用: {report.combo_usage_b}")
        return

    for core in catalog.core_cards.values():
        print(f"[{core.name}]")
        for combo in core.combos:
            requirements = " + ".join(
                f"{requirement.field} x{requirement.count}"
                for requirement in combo.requirements
            )
            effects = " + ".join(
                f"{effect.kind} {effect.value}" for effect in combo.effects
            ) or "无瞬时组合效果"
            print(
                f"- {combo.name}: {combo.nature}/{combo.duration}; "
                f"{requirements}; {effects}"
            )


if __name__ == "__main__":
    main()
