# Semantic Card Engine Exploration Directions

## Status

This document records technical exploration paths. It is not a GDD, does not change accepted gameplay, and does not make either path production-ready.

Design material: [finite semantic card physics](../game-design-workflow/idea-materials/M-2026-08-30-finite-semantic-card-physics.md).

Effect-region design material: [bounded semantic effect regions](../game-design-workflow/idea-materials/M-2026-08-30-bounded-semantic-effect-regions.md).

Embedding source and technical analysis: [Embedding semantic effect space](../game-design-workflow/idea-inbox/2026-08-30-embedding-semantic-effect-space.md).

## Shared Boundary

- AI may assign candidate properties or propose candidate laws during offline content production or inside a controlled sandbox.
- Published runtime behavior uses frozen, versioned, validated rules and data.
- Runtime generation does not execute model-authored arbitrary code or invent new effect operations.
- Qualitative selection and numerical balance remain separate. Every result must pass a finite effect schema and a conserved value budget.
- A synthesis preview and the committed result must use the same published inputs and engine version.

## Path A: Discrete Semantic Dynamics

Replace recipe-like `requires -> effect` laws with typed state transitions:

```text
concept properties + action operators + core boundary + combat topology
  -> deterministic state-transition simulation
  -> auditable transition trace
  -> combat-state delta
  -> effect IR projection
```

Laws may reference property classes, relationships and conserved channels, but not specific concept combinations or final card effect IDs. `damage`, `shield`, `heal` and control operations are projected once from combat-state changes.

Primary strengths are causal explanations, deterministic replay, conservation checks and Noita-like reuse of local laws. Primary risks are ontology design cost, sparse coverage and the possibility of hiding recipes inside overly specific property rules.

## Path B: Embedding Semantic Effect Field

Use a pinned embedding model to place concept definitions, actions, core descriptions and effect prototypes in a continuous semantic space:

```text
versioned concept definitions
  -> pinned embeddings
  -> role-aware composition
  -> factorized effect-prototype scores
  -> capacity-constrained effect-region assignment
  -> boundary projection and compatibility gate
  -> independent value-budget allocation
  -> effect IR
```

The first baseline may use cosine similarity, but the target experiment must not force every input to the nearest single effect. It should score independent axes such as effect family, target, propagation, timing and semantic channel. Low-confidence or incompatible results are rejected.

Embedding similarity selects qualitative candidates only. It must never directly determine damage, cost, duration or rarity. Vectors, model ID, templates and normalization settings are stored with a version hash so published results do not drift when a provider or model changes.

Primary strengths are zero-shot vocabulary coverage and low per-concept authoring cost. Primary risks are polysemy, symmetric similarity where directional causality is required, unstable decision boundaries, false confidence and weak causal explanations.

### Capacity-Constrained Effect Partition

The recorded direction divides the effect space into a finite cell complex:

- a card assigned to the stable interior of one effect cell receives exactly one effect;
- a card may receive two effects only inside a boundary band shared by two compatible effect cells;
- triple and higher-order junctions never create three-effect cards and must project to the nearest legal single cell or compatible pair boundary;
- every region has a versioned capacity, and pair boundaries also have a global density limit;
- assignment retains the original vector, assigned region, projected point and projection distance.

For an offline candidate batch, region selection can be solved as a minimum-cost assignment under capacity constraints. Cost combines semantic distance, projection distance and an occupancy penalty. Candidate regions are limited by confidence and an explicit effect-pair compatibility matrix. Published assignments remain immutable within one content version so adding later cards cannot silently remap existing recipes.

Capacity is a content-density constraint, not semantic evidence. The allocator must not force a distant card into a region merely to satisfy coverage. A maximum projection distance and an explicit `unmapped` result are required. If all semantically legal regions are full or too distant, the candidate remains `unmapped` for review and is not published as a false match.

## Comparison Contract

Both paths should receive the same structured inputs and emit the same validated card IR so the evaluation compares semantic mechanisms rather than output formats.

| Dimension | Path A: discrete dynamics | Path B: embedding field |
| --- | --- | --- |
| Unseen vocabulary | Requires property grounding | Strong zero-shot potential |
| Unseen combinations | Emerges from state laws | Interpolates in vector space |
| Causal explanation | Strong transition trace | Similarity evidence only |
| Deterministic release | Natural | Requires frozen/cached vectors |
| Player predictability | Potentially learnable laws | Unknown semantic boundaries |
| Authoring pressure | Ontology and laws | Prototypes, templates and calibration |
| True runtime emergence | Stronger | Closer to continuous classification |
| Main failure | Disguised recipes | Plausible but mechanically wrong mapping |

## Shared MVP Evaluation

- Inputs: 8 concepts, 3 actions and 2 core cards, producing 48 combinations.
- Outputs: one shared finite effect schema and one independent value-budget implementation.
- No combination-specific rule or labeled combination table is available to either generator.
- Evaluation: deterministic replay, paraphrase stability, action-swap sensitivity, held-out semantic coherence, result diversity, invalid-result rejection, single/dual-effect density, capacity occupancy, projection distance, budget conservation and human prediction.
- Evidence: retain every input, engine/model version, intermediate trace or similarity scores, source and assigned regions, projection distance, capacity state, rejection reason and final IR.

Path B should compare three composition baselines: weighted vector average, role-aware transforms and a fixed structured-sentence embedding. Direct nearest-effect mapping is a baseline, not the recommended architecture.

## Recorded Direction

The effect-count policy is now explicit:

- stable cell interiors produce one effect;
- compatible pair-boundary bands may produce two effects under one shared budget;
- higher-order intersections project to a legal single or pair region;
- versioned regional capacity limits the number of cards in each region;
- a candidate remains `unmapped` when no legal region is within the projection threshold or every legal region is full;
- capacity never overrides semantic validity, and published assignments do not change inside one content version.

The remaining work is empirical rather than a policy decision: implement the 48-combination comparison and measure semantic agreement, rejection rate, distribution, stability and player predictability for both exploration paths.
