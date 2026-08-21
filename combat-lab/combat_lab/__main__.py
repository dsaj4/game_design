from __future__ import annotations

import argparse
from pathlib import Path

from .analysis import analyze_availability
from .catalog import load_catalog


DATA_DIR = Path(__file__).parents[1] / "data"


def main() -> None:
    parser = argparse.ArgumentParser(description="成语组合战斗独立测试工具")
    parser.add_argument(
        "command",
        choices=("validate", "show", "analyze"),
        nargs="?",
        default="validate",
    )
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
