from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Iterable


class CatalogError(ValueError):
    pass


class GenerationError(ValueError):
    pass


@dataclass(frozen=True)
class SemanticSource:
    id: str
    name: str
    traits: frozenset[str]
    potency: int


@dataclass(frozen=True)
class SemanticLaw:
    id: str
    name: str
    requires: frozenset[str]
    derives: frozenset[str]
    effect_op: str
    effect_weight: int


@dataclass(frozen=True)
class CoreLens:
    id: str
    requires: frozenset[str]
    from_op: str
    to_op: str


@dataclass(frozen=True)
class CoreDefinition:
    id: str
    name: str
    lenses: tuple[CoreLens, ...]


@dataclass(frozen=True)
class Catalog:
    version: str
    allowed_effect_ops: frozenset[str]
    concepts: dict[str, SemanticSource]
    actions: dict[str, SemanticSource]
    laws: tuple[SemanticLaw, ...]
    cores: dict[str, CoreDefinition]


def load_catalog(path: Path | str) -> Catalog:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    concepts = _load_sources(data.get("concepts", []), "concept")
    actions = _load_sources(data.get("actions", []), "action")
    laws = tuple(
        SemanticLaw(
            id=str(item.get("id", "")),
            name=str(item.get("name", "")),
            requires=frozenset(str(value) for value in item.get("requires", [])),
            derives=frozenset(str(value) for value in item.get("derives", [])),
            effect_op=str(item.get("effect", {}).get("op", "")),
            effect_weight=int(item.get("effect", {}).get("weight", 0)),
        )
        for item in _unique_items(data.get("laws", []), "law")
    )
    cores = {
        str(item["id"]): CoreDefinition(
            id=str(item["id"]),
            name=str(item.get("name", item["id"])),
            lenses=tuple(
                CoreLens(
                    id=str(lens.get("id", "")),
                    requires=frozenset(
                        str(value) for value in lens.get("requires", [])
                    ),
                    from_op=str(lens.get("from_op", "")),
                    to_op=str(lens.get("to_op", "")),
                )
                for lens in _unique_items(item.get("lenses", []), "core lens")
            ),
        )
        for item in _unique_items(data.get("cores", []), "core")
    }
    catalog = Catalog(
        version=str(data.get("version", "")),
        allowed_effect_ops=frozenset(
            str(value) for value in data.get("allowed_effect_ops", [])
        ),
        concepts=concepts,
        actions=actions,
        laws=laws,
        cores=cores,
    )
    validate_catalog(catalog)
    return catalog


def validate_catalog(catalog: Catalog) -> None:
    if not catalog.version:
        raise CatalogError("catalog version is required")
    if not catalog.allowed_effect_ops:
        raise CatalogError("at least one effect operation is required")
    if "neutral" not in catalog.cores:
        raise CatalogError("catalog requires a neutral core")
    if not catalog.concepts or not catalog.laws:
        raise CatalogError("catalog requires concepts and laws")

    for label, sources in (("concept", catalog.concepts), ("action", catalog.actions)):
        for source in sources.values():
            if not source.traits:
                raise CatalogError(f"{label} {source.id} requires semantic traits")
            if source.potency < (1 if label == "concept" else 0):
                raise CatalogError(f"{label} {source.id} has invalid potency")

    for law in catalog.laws:
        if not law.id or not law.name or not law.requires or not law.derives:
            raise CatalogError("each law requires id, name, requirements, and derivations")
        if law.effect_op not in catalog.allowed_effect_ops or law.effect_weight < 1:
            raise CatalogError(f"law {law.id} has an invalid effect")

    for core in catalog.cores.values():
        for lens in core.lenses:
            if not lens.id or not lens.requires:
                raise CatalogError(f"core {core.id} has an incomplete lens")
            if {
                lens.from_op,
                lens.to_op,
            } - catalog.allowed_effect_ops:
                raise CatalogError(f"lens {lens.id} references an unknown effect operation")


def generate_card(
    catalog: Catalog,
    concept_ids: Iterable[str],
    action_ids: Iterable[str] = (),
    core_id: str = "neutral",
) -> dict[str, object]:
    concepts = sorted(str(value) for value in concept_ids)
    actions = sorted(str(value) for value in action_ids)
    if not concepts:
        raise GenerationError("at least one concept is required")
    unknown_concepts = sorted(set(concepts) - set(catalog.concepts))
    unknown_actions = sorted(set(actions) - set(catalog.actions))
    if unknown_concepts:
        raise GenerationError(f"unknown concept: {', '.join(unknown_concepts)}")
    if unknown_actions:
        raise GenerationError(f"unknown action: {', '.join(unknown_actions)}")
    if core_id not in catalog.cores:
        raise GenerationError(f"unknown core: {core_id}")

    sources = [catalog.concepts[item] for item in concepts]
    sources.extend(catalog.actions[item] for item in actions)
    traits = set().union(*(source.traits for source in sources))
    budget = sum(source.potency for source in sources)
    _derive_traits(catalog.laws, traits)

    matched_laws = [law for law in catalog.laws if law.requires <= traits]
    if not matched_laws:
        raise GenerationError("no semantic law produces an effect for this input")

    core = catalog.cores[core_id]
    signals: list[tuple[str, int]] = []
    applied_lenses: list[str] = []
    for law in matched_laws:
        effect_op = law.effect_op
        for lens in core.lenses:
            if lens.requires <= traits and effect_op == lens.from_op:
                effect_op = lens.to_op
                applied_lenses.append(lens.id)
        signals.append((effect_op, law.effect_weight))

    effects = _allocate_effects(signals, budget)
    name = "·".join(law.name for law in matched_laws)
    if applied_lenses:
        name = f"{core.name}·{name}"
    cost = min(4, max(1, (budget + 3) // 4))
    semantic_payload = {
        "catalog_version": catalog.version,
        "concepts": concepts,
        "actions": actions,
        "core_id": core_id,
        "matched_laws": [law.id for law in matched_laws],
        "applied_lenses": applied_lenses,
        "traits": sorted(traits),
        "budget": budget,
        "cost": cost,
        "effects": effects,
    }
    digest = hashlib.sha256(_canonical_json(semantic_payload)).hexdigest()
    card = {
        "schema_version": "card-ir-v0",
        "id": f"generated_{digest[:12]}",
        "name": name,
        "card_type": "glyph",
        "cost": cost,
        "traits": sorted(traits),
        "effects": effects,
        "provenance": {
            "catalog_version": catalog.version,
            "concepts": concepts,
            "actions": actions,
            "core_id": core_id,
            "matched_laws": [law.id for law in matched_laws],
            "applied_lenses": applied_lenses,
            "budget": budget,
            "digest": digest,
        },
    }
    _validate_generated_card(catalog, card)
    return card


def _derive_traits(laws: tuple[SemanticLaw, ...], traits: set[str]) -> None:
    changed = True
    while changed:
        changed = False
        for law in laws:
            if law.requires <= traits and not law.derives <= traits:
                traits.update(law.derives)
                changed = True


def _allocate_effects(
    signals: list[tuple[str, int]],
    budget: int,
) -> list[dict[str, object]]:
    weights = Counter[str]()
    for effect_op, weight in signals:
        weights[effect_op] += weight
    effect_ops = sorted(weights)
    if budget < len(effect_ops):
        raise GenerationError("effect budget is too small for the generated operations")

    remaining = budget - len(effect_ops)
    total_weight = sum(weights.values())
    values = {
        effect_op: 1 + (remaining * weights[effect_op]) // total_weight
        for effect_op in effect_ops
    }
    undistributed = budget - sum(values.values())
    remainder_order = sorted(
        effect_ops,
        key=lambda effect_op: (
            -((remaining * weights[effect_op]) % total_weight),
            effect_op,
        ),
    )
    for effect_op in remainder_order[:undistributed]:
        values[effect_op] += 1

    return [
        {
            "op": effect_op,
            "target": _effect_target(effect_op),
            "value": values[effect_op],
        }
        for effect_op in effect_ops
    ]


def _effect_target(effect_op: str) -> str:
    return "enemy" if effect_op in {"damage", "cancel_intent"} else "self"


def _validate_generated_card(catalog: Catalog, card: dict[str, object]) -> None:
    effects = card.get("effects", [])
    provenance = card.get("provenance", {})
    if not isinstance(effects, list) or not effects:
        raise GenerationError("generated card requires effects")
    if not isinstance(provenance, dict):
        raise GenerationError("generated card requires provenance")
    if any(effect.get("op") not in catalog.allowed_effect_ops for effect in effects):
        raise GenerationError("generated card contains an unknown effect operation")
    if sum(int(effect.get("value", 0)) for effect in effects) != provenance.get("budget"):
        raise GenerationError("generated effects do not conserve their budget")


def _load_sources(items: list[dict[str, object]], label: str) -> dict[str, SemanticSource]:
    return {
        str(item["id"]): SemanticSource(
            id=str(item["id"]),
            name=str(item.get("name", item["id"])),
            traits=frozenset(str(value) for value in item.get("traits", [])),
            potency=int(item.get("potency", 0)),
        )
        for item in _unique_items(items, label)
    }


def _unique_items(
    items: list[dict[str, object]],
    label: str,
) -> list[dict[str, object]]:
    seen: set[str] = set()
    for item in items:
        item_id = str(item.get("id", ""))
        if not item_id:
            raise CatalogError(f"{label} is missing an id")
        if item_id in seen:
            raise CatalogError(f"duplicate {label} id: {item_id}")
        seen.add(item_id)
    return items


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
