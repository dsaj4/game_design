# Semantic Card Engine Architecture

## Scope

This document records the technical architecture of the isolated engine experiment. It does not define accepted gameplay and does not replace the GDD.

## Requirements

### Functional

- Run the same 8 concepts, 3 actions and 2 cores through both semantic routes.
- Produce exactly one result per input: a single-effect card, a compatible dual-effect card, or `unmapped`.
- Enforce versioned region capacities across the complete offline batch.
- Preserve input, intermediate evidence, assignment evidence, final IR and content digests.

### Non-functional

- Deterministic: identical versions and inputs produce byte-equivalent report data.
- Auditable: every mapped result retains scores, source vector, projected point and distance.
- Bounded: only whitelisted effect operations can enter `card-ir-v0`.
- Offline: no model call or arbitrary generated code is executed during comparison or runtime.
- Replaceable substrate: a later pinned embedding model can replace frozen vectors without changing the assignment or IR contracts.

## Implemented Pipeline

```text
data/experiment.json
  -> canonical 48-input matrix
  -> discrete state dynamics ---------+
  -> role-aware frozen-vector field --+-> semantic candidates
                                      -> legal single/pair regions
                                      -> global capacity assignment
                                      -> card-ir-v0 or unmapped
                                      -> deterministic comparison report
```

Both routes stop at `SemanticCandidate`. They do not allocate card effects directly. The shared publisher owns compatibility, capacity, projection thresholds, value-budget allocation and final IR validation.

## ADR-EXP-001: Shared Candidate Contract and Batch Allocator

| Field | Decision |
| --- | --- |
| Status | `Accepted for EXP-002` |
| Date | `2026-08-30` |
| Source | Qualified semantic-physics and bounded-effect-region materials |

### Context

Route-specific final-card generators would make the comparison invalid because each route could silently apply different effect-count, compatibility or capacity rules. Per-card greedy assignment would also make results depend on input order and could waste scarce regions.

### Decision

Each route emits a common candidate containing a semantic vector, factorized effect scores, an independent value budget and an audit trace. A deterministic minimum-cost bipartite assignment then allocates the complete batch to versioned single/pair region slots or explicit `unmapped` slots. Illegal and over-distance regions are excluded before optimization, so capacity cannot make a semantically invalid assignment legal.

### Alternatives

- Route-specific card IR: simpler locally, rejected because it confounds route quality with different publishing rules.
- Greedy nearest-region assignment: smaller implementation, rejected because early candidates can consume capacity and make results order-sensitive.
- External optimization library: mature algorithms, deferred because the current 48-row experiment is small and a standard-library Hungarian assignment keeps the prototype dependency-free.

### Consequences

- The two routes are comparable at the candidate boundary and share every publishing constraint.
- Batch results are deterministic for a fixed catalog and canonical input order.
- Adding a new route requires only candidate generation plus a region prototype space.
- This allocator validates one fixed offline batch. It does not yet implement persistent content-version migration when later cards are appended.

## Current Technology Choice

The Embedding route currently reads six-dimensional frozen vectors from the versioned experiment catalog and applies role-specific diagonal transforms. This proves the continuous-space composition, boundary and capacity machinery without network access or model drift. It does not validate natural-language zero-shot understanding. A learned embedding model must be pinned, cached and evaluated against human judgments before that claim can be tested.

## Failure Modes

| Failure | Current control | Remaining risk |
| --- | --- | --- |
| Popular regions fill early | Global minimum-cost assignment | Capacity values are still hand-tuned experiment parameters |
| A distant candidate is forced into a slot | Maximum distance and explicit `unmapped` slots | Human semantic distance may disagree with the configured space |
| Three effects leak into a card | Only single and compatible pair regions exist | Compatibility policy still requires player testing |
| Numbers drift with semantic similarity | Value budget is independent of region distance | Budget values are placeholders, not balanced content |
| Results change between runs | Canonical ordering, frozen data and SHA-256 digests | Cross-version migration is not implemented |
| Frozen vectors appear more capable than they are | README and reports label them as a substrate | A real pinned model and blind review are still required |
