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
- Rebuildable cache: model identity, exact revision, license, text templates, source hashes and build-library versions are retained.

## Implemented Pipeline

```text
data/experiment.json -> canonical semantic texts
  -> explicit build-embeddings command
  -> pinned SentenceTransformer revision
  -> normalized embedding-cache.json
                                      |
                                      v
data/experiment.json ----------------+
  -> canonical 48-input matrix
  -> discrete state dynamics ---------+
  -> manual frozen-vector field -------+-> semantic candidates
  -> cached weighted/role/sentence ----+
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

The experiment retains the six-dimensional manual vector route as a control and adds a real multilingual SentenceTransformer cache. The model is `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, revision `e8f8c211226b894fcb81acc59f3b34ba3efd5f42`, Apache-2.0. The build environment is optional; normal comparison and tests load only the committed JSON cache.

## ADR-EXP-002: Pinned Offline Embedding Cache

| Field | Decision |
| --- | --- |
| Status | `Accepted for EXP-002` |
| Date | `2026-08-30` |
| Source | User instruction to continue real Embedding integration |

### Context

Calling a hosted model during comparison would make reports depend on credentials, provider drift and network availability. Loading a local model during every game or test run would add a large runtime dependency and blur content production with deterministic execution. Artificial vectors alone cannot test whether language semantics transfer to unseen combinations.

### Decision

An explicit optional command loads one model at an exact repository revision with remote code disabled, encodes the complete versioned text manifest on CPU, and writes normalized vectors plus provenance to a content-addressed cache. Default comparison requires that cache and rejects missing, tampered or stale entries. `--manual-only` is the only explicit fallback.

Three learned-vector compositions share the same cache and region publisher: neutral weighted average, role-qualified weighted average, and one structured combination sentence. None receives labeled combination answers.

### Alternatives

- Hosted embedding API: rejected for the experiment baseline because credentials and provider-side drift weaken reproducibility.
- Runtime model loading: rejected because the released rules should remain lightweight, frozen and deterministic.
- Replace manual vectors entirely: rejected because retaining them exposes how much apparent success came from hand-shaped geometry.

### Consequences

- A normal test run has no PyTorch, Transformers or network requirement.
- Rebuilding needs the optional locked environment and model download; Windows without symlink support uses more cache space.
- The committed cache is about 0.6 MB and the five-route report is larger than V0.
- Model similarity is now real, but semantic correctness still requires blind human labels.

## Failure Modes

| Failure | Current control | Remaining risk |
| --- | --- | --- |
| Popular regions fill early | Global minimum-cost assignment | Capacity values are still hand-tuned experiment parameters |
| A distant candidate is forced into a slot | Maximum distance and explicit `unmapped` slots | Human semantic distance may disagree with the configured space |
| Three effects leak into a card | Only single and compatible pair regions exist | Compatibility policy still requires player testing |
| Numbers drift with semantic similarity | Value budget is independent of region distance | Budget values are placeholders, not balanced content |
| Results change between runs | Canonical ordering, frozen data and SHA-256 digests | Cross-version migration is not implemented |
| Model or prompt silently changes | Exact revision, text hashes, cache digest and template version | Deliberate migrations need a new experiment version |
| Cached model output appears semantically correct | Weighted, role and structured baselines are separated | Blind human review is still required |
| Optional builder executes model repository code | `trust_remote_code=False` and an exact revision | Dependency supply-chain review remains an operational responsibility |
