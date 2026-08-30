# Phase III — the intrinsic transactional object

**Status: the intrinsic-object search completed its transition role; the transactional graph-storage relative Book theorem is audited in its declared scope.**

Phase III asks whether the unrestricted Presburger atlas is the mathematics or merely an overexpressive presentation language.

## 1. Intrinsic-object criteria

A candidate object had to be independently motivated before tame/wild classification, invariant under justified process-bijective recodings, naturally compositional, reconstructive rather than merely extensional at the final relation, decomposable with genuine structural obstructions, and compatible with the Phase-I non-r.e. theorem.

The phase explicitly forbids defining the object as “whatever the current compiler accepts”.

## 2. The exposed transactional graph-storage object

A finite graph `Gamma` specifies a graph monoid `M_Gamma`. Unlooped vertices supply bicyclic storage; looped vertices supply group-like integer storage; adjacency specifies commutation.

An exposed transaction records more than its monoid product. Object data include finite typed control, `Gamma` and initial storage `1`, a chosen generator word for every transaction, occurrence identity / additive records / grades, optional storage-blind affine payload action, observer data, and complete residual storage configuration at ports.

The chosen generator word matters because an identity edge and `p_v q_v` have the same total monoid product but different exposed storage footprints.

## 3. Exact composition theorem

### Theorem III.1 — raw-port composition
**AUDITED / ACCEPTED.**

Raw execution semantics with complete storage/payload ports is exact under sequential gluing with matching full ports, shared-port gluing by all legal interleavings in the declared common storage type, finite nondeterministic union, and finite-control star/block feedback before neutral projection.

### Counterexample — neutralize too early
Over `B=<p,q | pq=1>`, the `p` component and the `q` component each have no neutral run from `1`, but

```text
1 --p--> p --q--> 1
```

is a neutral composite. Therefore the neutral/public relations of components cannot be composed first.

## 4. Relative transactional Book theorem

### Theorem III.2
**PROVED AFTER INDEPENDENT ADVERSARIAL AUDIT in the declared relative scope.**

Finite exposed transactional graph-storage processes, with exact residual storage/action ports and process-bijective recodings, support exact raw composition, graph-monoid structural storage theory, recursive tame-storage decomposition, finite induced storage-capacity obstructions, proof-bearing finite-action / degree-one affine charts, exact opaque storage/action atoms, and reconciliation with the scalar effective boundary.

This is a **relative** Book theorem for exposed graph-storage capacity. It does not classify arbitrary Presburger presentations and does not identify final relation equality with process identity.

## 5. Action ports

For an affine path `w`, `F_w(z)=A_w z+b_w`. A suffix-action port `K` carries `K A_w` at entry, `K` at exit, and weight `K b_w`. For consecutive paths `u,v`, exact composition follows from

```text
A_(uv)=A_v A_u,
b_(uv)=A_v b_u+b_v.
```

Thus exact action-port composition exists even when the action set is infinite; finite action is an effective-chart hypothesis, not a raw semantic axiom.

## 6. Why Phase IV is forced

The object retains **complete** residual storage configurations. That is exact but potentially too large to deserve a Graph-Minors-scale structural theorem. The next question is:

> Can complete ambient state be factored through small, natural, noncopying separators without losing future legality or action?

That is Phase IV.

## 7. Sources

- `docs/PHASE_III_INTRINSIC_OBJECT_PROGRAM_20260830.md`
- `docs/PHASE_III_TRANSACTIONAL_GRAPH_STORAGE_BOOK_TERMINAL_20260830.md`
- `docs/PHASE_III_COMPOSITION_FIRST_CONTEXTUAL_OPACITY_BOUNDARY_20260830.md`

See [`../../provenance/SOURCE_MAP.md`](../../provenance/SOURCE_MAP.md).
