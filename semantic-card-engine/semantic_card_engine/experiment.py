from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
from typing import Callable


class ExperimentError(ValueError):
    pass


@dataclass(frozen=True)
class ExperimentEntity:
    id: str
    name: str
    potency: int
    state: dict[str, float]
    state_scale: dict[str, float]
    state_delta: dict[str, float]
    embedding: tuple[float, ...]


@dataclass(frozen=True)
class RegionPolicy:
    minimum_score: float
    single_margin: float
    pair_margin: float
    maximum_projection_distance: float
    unmapped_penalty: float
    single_capacities: dict[str, int]
    pair_capacities: dict[tuple[str, str], int]


@dataclass(frozen=True)
class ExperimentConfig:
    version: str
    effect_ops: tuple[str, ...]
    state_dimensions: tuple[str, ...]
    embedding_dimensions: tuple[str, ...]
    embedding_role_weights: dict[str, float]
    embedding_role_scales: dict[str, tuple[float, ...]]
    effect_prototypes: dict[str, tuple[float, ...]]
    dynamics_projection: dict[str, dict[str, float]]
    concepts: dict[str, ExperimentEntity]
    actions: dict[str, ExperimentEntity]
    cores: dict[str, ExperimentEntity]
    region_policy: RegionPolicy


@dataclass(frozen=True, order=True)
class ExperimentInput:
    concept_id: str
    action_id: str
    core_id: str


@dataclass(frozen=True)
class SemanticCandidate:
    route: str
    input: ExperimentInput
    name: str
    budget: int
    vector: tuple[float, ...]
    effect_scores: dict[str, float]
    trace: dict[str, object]


@dataclass(frozen=True)
class EffectRegion:
    id: str
    effect_ops: tuple[str, ...]
    capacity: int
    prototype: tuple[float, ...]


@dataclass(frozen=True)
class RegionAssignment:
    region: EffectRegion | None
    projection_distance: float | None
    legal_region_ids: tuple[str, ...]
    rejection_reason: str | None


def load_experiment_config(path: Path | str) -> ExperimentConfig:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    effect_ops = tuple(str(value) for value in data.get("effect_ops", []))
    state_dimensions = tuple(
        str(value) for value in data.get("state_dimensions", [])
    )
    embedding_dimensions = tuple(
        str(value) for value in data.get("embedding_dimensions", [])
    )
    concept_items = data.get("concepts", [])
    action_items = data.get("actions", [])
    core_items = data.get("cores", [])
    concepts = _load_entities(concept_items, "concept")
    actions = _load_entities(action_items, "action")
    cores = _load_entities(core_items, "core")

    raw_policy = data.get("region_policy", {})
    op_order = {effect_op: index for index, effect_op in enumerate(effect_ops)}
    pair_capacities: dict[tuple[str, str], int] = {}
    for pair_name, capacity in raw_policy.get("pair_capacities", {}).items():
        parts = tuple(str(pair_name).split("+"))
        if len(parts) != 2 or len(set(parts)) != 2:
            raise ExperimentError(f"invalid pair region: {pair_name}")
        if any(part not in op_order for part in parts):
            raise ExperimentError(f"pair region references unknown effect: {pair_name}")
        pair = tuple(sorted(parts, key=op_order.__getitem__))
        pair_capacities[pair] = int(capacity)

    config = ExperimentConfig(
        version=str(data.get("version", "")),
        effect_ops=effect_ops,
        state_dimensions=state_dimensions,
        embedding_dimensions=embedding_dimensions,
        embedding_role_weights={
            str(key): float(value)
            for key, value in data.get("embedding_role_weights", {}).items()
        },
        embedding_role_scales={
            str(key): tuple(float(value) for value in values)
            for key, values in data.get("embedding_role_scales", {}).items()
        },
        effect_prototypes={
            str(key): tuple(float(value) for value in values)
            for key, values in data.get("effect_prototypes", {}).items()
        },
        dynamics_projection={
            str(effect_op): {
                str(dimension): float(weight)
                for dimension, weight in weights.items()
            }
            for effect_op, weights in data.get("dynamics_projection", {}).items()
        },
        concepts=concepts,
        actions=actions,
        cores=cores,
        region_policy=RegionPolicy(
            minimum_score=float(raw_policy.get("minimum_score", 0)),
            single_margin=float(raw_policy.get("single_margin", 0)),
            pair_margin=float(raw_policy.get("pair_margin", 0)),
            maximum_projection_distance=float(
                raw_policy.get("maximum_projection_distance", 0)
            ),
            unmapped_penalty=float(raw_policy.get("unmapped_penalty", 0)),
            single_capacities={
                str(key): int(value)
                for key, value in raw_policy.get("single_capacities", {}).items()
            },
            pair_capacities=pair_capacities,
        ),
    )
    validate_experiment_config(config)
    return config


def validate_experiment_config(config: ExperimentConfig) -> None:
    if not config.version:
        raise ExperimentError("experiment version is required")
    if len(config.concepts) != 8 or len(config.actions) != 3 or len(config.cores) != 2:
        raise ExperimentError("EXP-002 requires 8 concepts, 3 actions, and 2 cores")
    if not config.effect_ops or len(set(config.effect_ops)) != len(config.effect_ops):
        raise ExperimentError("effect operations must be unique and non-empty")
    if not config.state_dimensions or not config.embedding_dimensions:
        raise ExperimentError("state and embedding dimensions are required")
    if set(config.effect_prototypes) != set(config.effect_ops):
        raise ExperimentError("every effect operation requires one embedding prototype")
    if set(config.dynamics_projection) != set(config.effect_ops):
        raise ExperimentError("every effect operation requires one dynamics projection")

    state_dimensions = set(config.state_dimensions)
    embedding_size = len(config.embedding_dimensions)
    for label, entities in (
        ("concept", config.concepts),
        ("action", config.actions),
        ("core", config.cores),
    ):
        for entity in entities.values():
            if len(entity.embedding) != embedding_size or not any(entity.embedding):
                raise ExperimentError(f"{label} {entity.id} has an invalid embedding")
            if set(entity.state) - state_dimensions:
                raise ExperimentError(f"{label} {entity.id} has an unknown state")
            if set(entity.state_scale) - state_dimensions:
                raise ExperimentError(f"{label} {entity.id} has an unknown state scale")
            if set(entity.state_delta) - state_dimensions:
                raise ExperimentError(f"{label} {entity.id} has an unknown state delta")
            if label == "concept" and set(entity.state) != state_dimensions:
                raise ExperimentError(f"concept {entity.id} requires every state dimension")
            if label != "core" and entity.potency < 1:
                raise ExperimentError(f"{label} {entity.id} requires positive potency")

    roles = {"concept", "action", "core"}
    if set(config.embedding_role_weights) != roles:
        raise ExperimentError("embedding weights require concept, action, and core roles")
    if set(config.embedding_role_scales) != roles:
        raise ExperimentError("embedding scales require concept, action, and core roles")
    if not math.isclose(sum(config.embedding_role_weights.values()), 1.0):
        raise ExperimentError("embedding role weights must sum to one")
    if any(len(values) != embedding_size for values in config.embedding_role_scales.values()):
        raise ExperimentError("embedding role scales have inconsistent dimensions")
    if any(len(values) != embedding_size for values in config.effect_prototypes.values()):
        raise ExperimentError("effect prototype dimensions are inconsistent")

    for effect_op, weights in config.dynamics_projection.items():
        if not weights or set(weights) - state_dimensions or sum(weights.values()) <= 0:
            raise ExperimentError(f"effect {effect_op} has an invalid dynamics projection")

    policy = config.region_policy
    if set(policy.single_capacities) != set(config.effect_ops):
        raise ExperimentError("single-region capacities must cover every effect operation")
    if any(capacity < 1 for capacity in policy.single_capacities.values()):
        raise ExperimentError("single-region capacities must be positive")
    if any(capacity < 1 for capacity in policy.pair_capacities.values()):
        raise ExperimentError("pair-region capacities must be positive")
    if not 0 <= policy.minimum_score <= 1:
        raise ExperimentError("minimum score must be between zero and one")
    if policy.unmapped_penalty <= policy.maximum_projection_distance:
        raise ExperimentError("unmapped penalty must exceed maximum projection distance")


def build_experiment_inputs(config: ExperimentConfig) -> tuple[ExperimentInput, ...]:
    return tuple(
        ExperimentInput(concept_id, action_id, core_id)
        for concept_id in sorted(config.concepts)
        for action_id in sorted(config.actions)
        for core_id in sorted(config.cores)
    )


def run_comparison(config: ExperimentConfig) -> dict[str, object]:
    inputs = build_experiment_inputs(config)
    routes: tuple[tuple[str, Callable[[ExperimentConfig, ExperimentInput], SemanticCandidate]], ...] = (
        ("discrete_dynamics", _build_dynamics_candidate),
        ("embedding_role_aware", _build_embedding_candidate),
    )
    route_reports: dict[str, object] = {}
    for route, builder in routes:
        candidates = tuple(builder(config, item) for item in inputs)
        assignments = assign_effect_regions(config, route, candidates)
        results = [
            _project_result(config, candidate, assignment)
            for candidate, assignment in zip(candidates, assignments, strict=True)
        ]
        route_reports[route] = _build_route_report(config, route, results)

    report: dict[str, object] = {
        "schema_version": "semantic-physics-comparison-v0",
        "experiment_version": config.version,
        "input_count": len(inputs),
        "routes": route_reports,
    }
    report["digest"] = hashlib.sha256(_canonical_json(report)).hexdigest()
    return report


def assign_effect_regions(
    config: ExperimentConfig,
    route: str,
    candidates: tuple[SemanticCandidate, ...],
) -> tuple[RegionAssignment, ...]:
    ordered_candidates = tuple(sorted(candidates, key=lambda item: item.input))
    if ordered_candidates != candidates:
        raise ExperimentError("candidates must use canonical input order")
    regions = _build_regions(config, route)
    region_slots = [region for region in regions for _ in range(region.capacity)]
    slots: list[EffectRegion | None] = region_slots + [None] * len(candidates)
    legal_maps = [_legal_regions(config, candidate, regions) for candidate in candidates]
    cost_scale = 1_000_000
    impossible_cost = 1_000_000_000
    unmapped_cost = round(config.region_policy.unmapped_penalty * cost_scale)
    costs = [
        [
            unmapped_cost
            if region is None
            else round(legal.get(region.id, impossible_cost) * cost_scale)
            if region.id in legal
            else impossible_cost
            for region in slots
        ]
        for legal in legal_maps
    ]
    slot_assignments = _minimum_cost_assignment(costs)

    assignments: list[RegionAssignment] = []
    for legal, slot_index in zip(legal_maps, slot_assignments, strict=True):
        region = slots[slot_index]
        legal_ids = tuple(
            region_id for region_id, _ in sorted(legal.items(), key=lambda item: (item[1], item[0]))
        )
        if region is None:
            reason = "capacity_exhausted" if legal_ids else "no_legal_region"
            assignments.append(RegionAssignment(None, None, legal_ids, reason))
            continue
        assignments.append(
            RegionAssignment(region, legal[region.id], legal_ids, None)
        )
    return tuple(assignments)


def _build_dynamics_candidate(
    config: ExperimentConfig,
    item: ExperimentInput,
) -> SemanticCandidate:
    concept = config.concepts[item.concept_id]
    action = config.actions[item.action_id]
    core = config.cores[item.core_id]
    initial_state = dict(concept.state)
    after_action = _apply_state_transform(initial_state, action, config.state_dimensions)
    final_state = _apply_state_transform(after_action, core, config.state_dimensions)
    raw_scores = {
        effect_op: sum(
            final_state[dimension] * weight
            for dimension, weight in config.dynamics_projection[effect_op].items()
        )
        / sum(config.dynamics_projection[effect_op].values())
        for effect_op in config.effect_ops
    }
    vector = _normalize(tuple(raw_scores[effect_op] for effect_op in config.effect_ops))
    scores = {
        effect_op: _cosine(vector, prototype)
        for effect_op, prototype in _route_prototypes(config, "discrete_dynamics").items()
    }
    return SemanticCandidate(
        route="discrete_dynamics",
        input=item,
        name=f"{core.name}·{concept.name}·{action.name}",
        budget=concept.potency + action.potency,
        vector=vector,
        effect_scores=scores,
        trace={
            "initial_state": _round_mapping(initial_state),
            "after_action": _round_mapping(after_action),
            "after_core": _round_mapping(final_state),
            "projected_channels": _round_mapping(raw_scores),
        },
    )


def _build_embedding_candidate(
    config: ExperimentConfig,
    item: ExperimentInput,
) -> SemanticCandidate:
    concept = config.concepts[item.concept_id]
    action = config.actions[item.action_id]
    core = config.cores[item.core_id]
    entities = {"concept": concept, "action": action, "core": core}
    contributions: dict[str, tuple[float, ...]] = {}
    for role, entity in entities.items():
        weight = config.embedding_role_weights[role]
        scale = config.embedding_role_scales[role]
        contributions[role] = tuple(
            value * role_scale * weight
            for value, role_scale in zip(entity.embedding, scale, strict=True)
        )
    vector = _normalize(
        tuple(
            sum(contributions[role][index] for role in ("concept", "action", "core"))
            for index in range(len(config.embedding_dimensions))
        )
    )
    prototypes = _route_prototypes(config, "embedding_role_aware")
    scores = {
        effect_op: _cosine(vector, prototype)
        for effect_op, prototype in prototypes.items()
    }
    return SemanticCandidate(
        route="embedding_role_aware",
        input=item,
        name=f"{core.name}·{concept.name}·{action.name}",
        budget=concept.potency + action.potency,
        vector=vector,
        effect_scores=scores,
        trace={
            "embedding_dimensions": list(config.embedding_dimensions),
            "role_contributions": {
                role: _round_vector(values) for role, values in contributions.items()
            },
        },
    )


def _apply_state_transform(
    state: dict[str, float],
    entity: ExperimentEntity,
    dimensions: tuple[str, ...],
) -> dict[str, float]:
    return {
        dimension: min(
            1.5,
            max(
                0.0,
                state[dimension] * entity.state_scale.get(dimension, 1.0)
                + entity.state_delta.get(dimension, 0.0),
            ),
        )
        for dimension in dimensions
    }


def _build_regions(
    config: ExperimentConfig,
    route: str,
) -> tuple[EffectRegion, ...]:
    prototypes = _route_prototypes(config, route)
    regions = [
        EffectRegion(
            id=f"single:{effect_op}",
            effect_ops=(effect_op,),
            capacity=config.region_policy.single_capacities[effect_op],
            prototype=prototypes[effect_op],
        )
        for effect_op in config.effect_ops
    ]
    for pair, capacity in config.region_policy.pair_capacities.items():
        prototype = _normalize(
            tuple(
                prototypes[pair[0]][index] + prototypes[pair[1]][index]
                for index in range(len(prototypes[pair[0]]))
            )
        )
        regions.append(
            EffectRegion(
                id=f"pair:{'+'.join(pair)}",
                effect_ops=pair,
                capacity=capacity,
                prototype=prototype,
            )
        )
    return tuple(regions)


def _route_prototypes(
    config: ExperimentConfig,
    route: str,
) -> dict[str, tuple[float, ...]]:
    if route == "discrete_dynamics":
        return {
            effect_op: tuple(
                1.0 if index == effect_index else 0.0
                for index in range(len(config.effect_ops))
            )
            for effect_index, effect_op in enumerate(config.effect_ops)
        }
    if route == "embedding_role_aware":
        return {
            effect_op: _normalize(vector)
            for effect_op, vector in config.effect_prototypes.items()
        }
    raise ExperimentError(f"unknown experiment route: {route}")


def _legal_regions(
    config: ExperimentConfig,
    candidate: SemanticCandidate,
    regions: tuple[EffectRegion, ...],
) -> dict[str, float]:
    policy = config.region_policy
    ranked_ops = sorted(
        config.effect_ops,
        key=lambda effect_op: (
            -candidate.effect_scores[effect_op],
            config.effect_ops.index(effect_op),
        ),
    )
    top_score = candidate.effect_scores[ranked_ops[0]]
    top_pair = frozenset(ranked_ops[:2])
    legal: dict[str, float] = {}
    for region in regions:
        distance = 1.0 - _cosine(candidate.vector, region.prototype)
        if distance > policy.maximum_projection_distance:
            continue
        if len(region.effect_ops) == 1:
            score = candidate.effect_scores[region.effect_ops[0]]
            if score >= policy.minimum_score and top_score - score <= policy.single_margin:
                legal[region.id] = distance
            continue
        first, second = region.effect_ops
        if frozenset(region.effect_ops) != top_pair:
            continue
        if min(candidate.effect_scores[first], candidate.effect_scores[second]) < policy.minimum_score:
            continue
        if abs(candidate.effect_scores[first] - candidate.effect_scores[second]) > policy.pair_margin:
            continue
        legal[region.id] = distance
    return legal


def _project_result(
    config: ExperimentConfig,
    candidate: SemanticCandidate,
    assignment: RegionAssignment,
) -> dict[str, object]:
    input_payload = {
        "concept_id": candidate.input.concept_id,
        "action_id": candidate.input.action_id,
        "core_id": candidate.input.core_id,
    }
    candidate_payload = {
        "vector": _round_vector(candidate.vector),
        "effect_scores": _round_mapping(candidate.effect_scores),
        "trace": candidate.trace,
    }
    assignment_payload: dict[str, object] = {
        "legal_region_ids": list(assignment.legal_region_ids),
    }
    if assignment.region is None:
        assignment_payload["rejection_reason"] = assignment.rejection_reason
        return {
            "status": "unmapped",
            "input": input_payload,
            "candidate": candidate_payload,
            "assignment": assignment_payload,
        }

    region = assignment.region
    effects = _allocate_budget(
        region.effect_ops,
        candidate.effect_scores,
        candidate.budget,
    )
    assignment_payload.update(
        {
            "region_id": region.id,
            "projected_point": _round_vector(region.prototype),
            "projection_distance": round(float(assignment.projection_distance), 6),
        }
    )
    semantic_payload = {
        "experiment_version": config.version,
        "route": candidate.route,
        "input": input_payload,
        "region_id": region.id,
        "effects": effects,
        "budget": candidate.budget,
        "vector": candidate_payload["vector"],
        "projected_point": assignment_payload["projected_point"],
        "projection_distance": assignment_payload["projection_distance"],
    }
    digest = hashlib.sha256(_canonical_json(semantic_payload)).hexdigest()
    card = {
        "schema_version": "card-ir-v0",
        "id": f"experiment_{digest[:12]}",
        "name": candidate.name,
        "card_type": "glyph",
        "cost": min(4, max(1, (candidate.budget + 3) // 4)),
        "traits": sorted(input_payload.values()),
        "effects": effects,
        "provenance": {
            "experiment_version": config.version,
            "route": candidate.route,
            "input": input_payload,
            "region_id": region.id,
            "budget": candidate.budget,
            "digest": digest,
        },
    }
    _validate_experiment_card(config, card)
    return {
        "status": "mapped",
        "input": input_payload,
        "candidate": candidate_payload,
        "assignment": assignment_payload,
        "card": card,
    }


def _allocate_budget(
    effect_ops: tuple[str, ...],
    scores: dict[str, float],
    budget: int,
) -> list[dict[str, object]]:
    if budget < len(effect_ops):
        raise ExperimentError("effect budget is too small for the assigned region")
    base = {effect_op: 1 for effect_op in effect_ops}
    remaining = budget - len(effect_ops)
    total_score = sum(max(scores[effect_op], 0.0) for effect_op in effect_ops)
    if total_score == 0:
        weights = {effect_op: 1.0 for effect_op in effect_ops}
        total_score = float(len(effect_ops))
    else:
        weights = {effect_op: max(scores[effect_op], 0.0) for effect_op in effect_ops}
    raw_shares = {
        effect_op: remaining * weights[effect_op] / total_score
        for effect_op in effect_ops
    }
    for effect_op in effect_ops:
        base[effect_op] += math.floor(raw_shares[effect_op])
    undistributed = budget - sum(base.values())
    remainder_order = sorted(
        effect_ops,
        key=lambda effect_op: (-(raw_shares[effect_op] % 1), effect_op),
    )
    for effect_op in remainder_order[:undistributed]:
        base[effect_op] += 1
    return [
        {
            "op": effect_op,
            "target": "enemy" if effect_op in {"damage", "cancel_intent"} else "self",
            "value": base[effect_op],
        }
        for effect_op in effect_ops
    ]


def _validate_experiment_card(
    config: ExperimentConfig,
    card: dict[str, object],
) -> None:
    effects = card.get("effects", [])
    provenance = card.get("provenance", {})
    if not isinstance(effects, list) or not 1 <= len(effects) <= 2:
        raise ExperimentError("experiment cards require one or two effects")
    if not isinstance(provenance, dict):
        raise ExperimentError("experiment cards require provenance")
    effect_ops = tuple(str(effect["op"]) for effect in effects)
    if any(effect_op not in config.effect_ops for effect_op in effect_ops):
        raise ExperimentError("experiment card contains an unknown effect")
    if len(effect_ops) == 2:
        op_order = {effect_op: index for index, effect_op in enumerate(config.effect_ops)}
        pair = tuple(sorted(effect_ops, key=op_order.__getitem__))
        if pair not in config.region_policy.pair_capacities:
            raise ExperimentError("experiment card contains an incompatible effect pair")
    if sum(int(effect["value"]) for effect in effects) != provenance.get("budget"):
        raise ExperimentError("experiment card effects do not conserve their budget")


def _build_route_report(
    config: ExperimentConfig,
    route: str,
    results: list[dict[str, object]],
) -> dict[str, object]:
    mapped = [result for result in results if result["status"] == "mapped"]
    unmapped = [result for result in results if result["status"] == "unmapped"]
    region_occupancy = Counter(
        str(result["assignment"]["region_id"])
        for result in mapped
    )
    effect_distribution = Counter(
        str(effect["op"])
        for result in mapped
        for effect in result["card"]["effects"]
    )
    rejection_reasons = Counter(
        str(result["assignment"]["rejection_reason"])
        for result in unmapped
    )
    distances = [
        float(result["assignment"]["projection_distance"])
        for result in mapped
    ]
    regions = _build_regions(config, route)
    summary = {
        "mapped": len(mapped),
        "unmapped": len(unmapped),
        "single_effect_cards": sum(len(result["card"]["effects"]) == 1 for result in mapped),
        "dual_effect_cards": sum(len(result["card"]["effects"]) == 2 for result in mapped),
        "effect_distribution": dict(sorted(effect_distribution.items())),
        "rejection_reasons": dict(sorted(rejection_reasons.items())),
        "region_occupancy": {
            region.id: region_occupancy[region.id] for region in regions
        },
        "region_capacities": {region.id: region.capacity for region in regions},
        "mean_projection_distance": round(sum(distances) / len(distances), 6)
        if distances
        else None,
    }
    return {
        "summary": summary,
        "results": results,
        "result_digest": hashlib.sha256(_canonical_json(results)).hexdigest(),
    }


def _minimum_cost_assignment(costs: list[list[int]]) -> list[int]:
    if not costs or not costs[0]:
        raise ExperimentError("assignment requires a non-empty cost matrix")
    row_count = len(costs)
    column_count = len(costs[0])
    if row_count > column_count or any(len(row) != column_count for row in costs):
        raise ExperimentError("assignment requires a rectangular matrix with enough slots")

    infinity = 10**18
    row_potential = [0] * (row_count + 1)
    column_potential = [0] * (column_count + 1)
    matched_row = [0] * (column_count + 1)
    previous_column = [0] * (column_count + 1)
    for row in range(1, row_count + 1):
        matched_row[0] = row
        column = 0
        minimum = [infinity] * (column_count + 1)
        used = [False] * (column_count + 1)
        while True:
            used[column] = True
            current_row = matched_row[column]
            delta = infinity
            next_column = 0
            for candidate_column in range(1, column_count + 1):
                if used[candidate_column]:
                    continue
                reduced_cost = (
                    costs[current_row - 1][candidate_column - 1]
                    - row_potential[current_row]
                    - column_potential[candidate_column]
                )
                if reduced_cost < minimum[candidate_column]:
                    minimum[candidate_column] = reduced_cost
                    previous_column[candidate_column] = column
                if minimum[candidate_column] < delta:
                    delta = minimum[candidate_column]
                    next_column = candidate_column
            for candidate_column in range(column_count + 1):
                if used[candidate_column]:
                    row_potential[matched_row[candidate_column]] += delta
                    column_potential[candidate_column] -= delta
                else:
                    minimum[candidate_column] -= delta
            column = next_column
            if matched_row[column] == 0:
                break
        while True:
            next_column = previous_column[column]
            matched_row[column] = matched_row[next_column]
            column = next_column
            if column == 0:
                break

    assignment = [-1] * row_count
    for column in range(1, column_count + 1):
        if matched_row[column] != 0:
            assignment[matched_row[column] - 1] = column - 1
    if any(column < 0 for column in assignment):
        raise ExperimentError("assignment did not cover every candidate")
    return assignment


def _load_entities(
    items: list[dict[str, object]],
    label: str,
) -> dict[str, ExperimentEntity]:
    entities: dict[str, ExperimentEntity] = {}
    for item in items:
        entity_id = str(item.get("id", ""))
        if not entity_id or entity_id in entities:
            raise ExperimentError(f"{label} ids must be present and unique")
        entities[entity_id] = ExperimentEntity(
            id=entity_id,
            name=str(item.get("name", entity_id)),
            potency=int(item.get("potency", 0)),
            state={str(key): float(value) for key, value in item.get("state", {}).items()},
            state_scale={
                str(key): float(value) for key, value in item.get("state_scale", {}).items()
            },
            state_delta={
                str(key): float(value) for key, value in item.get("state_delta", {}).items()
            },
            embedding=tuple(float(value) for value in item.get("embedding", [])),
        )
    return entities


def _normalize(vector: tuple[float, ...]) -> tuple[float, ...]:
    length = math.sqrt(sum(value * value for value in vector))
    if length == 0:
        raise ExperimentError("semantic vectors cannot be zero")
    return tuple(value / length for value in vector)


def _cosine(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    if len(left) != len(right):
        raise ExperimentError("semantic vectors have inconsistent dimensions")
    left_length = math.sqrt(sum(value * value for value in left))
    right_length = math.sqrt(sum(value * value for value in right))
    if left_length == 0 or right_length == 0:
        raise ExperimentError("semantic vectors cannot be zero")
    return sum(a * b for a, b in zip(left, right, strict=True)) / (
        left_length * right_length
    )


def _round_vector(vector: tuple[float, ...]) -> list[float]:
    return [round(value, 6) for value in vector]


def _round_mapping(values: dict[str, float]) -> dict[str, float]:
    return {key: round(value, 6) for key, value in sorted(values.items())}


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
