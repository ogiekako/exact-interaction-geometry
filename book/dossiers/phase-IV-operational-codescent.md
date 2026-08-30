# Dossier IV-A — operational codescent

**Status:** `AUDITED / ACCEPTED` in fixed-ambient complete-state scope.

## Categorical core

Let `D` be the decoration monoid, `LQuiv_D = Quiv/U(BD)`, and `LCat_D = Cat/BD`. The decorated free-category construction

```text
F_D : LQuiv_D -> LCat_D
```

is left adjoint to the underlying labelled-quiver functor. Therefore it preserves colimits:

```text
F_D(colim_j Q_j) ~= colim_j F_D(Q_j).
```

For literal owner covers, the exact global atomic quiver is the colimit of local owned quivers; applying `F_D` reconstructs the exact raw execution category.

## Relation shadow

For two pieces meeting on boundary state set `X_S`, let `R_i` be all decorated `X_S`-to-`X_S` path blocks of child `i`, including identities. After path formation and only then existential black-boxing,

```text
R_union = (R_1 union R_2)^*.
```

This is the mixed-return star: arbitrarily many recrossings of the glued boundary are genuine execution data.

## Boundary fixtures

The maintained verifier checks:

- 256 exhaustive two-piece quiver fixtures through bounded atomic length;
- premature neutralization failure;
- an unsealed macro interleaving that creates an illegal extra behaviour;
- the `B_a*B_b` factor-projection obstruction.

The finite enumeration is regression evidence for the algebraic theorem, not the proof of the free-category adjunction.

## What this does not solve

Complete global state is an exact but potentially vacuous interface. Codescent closes the semantic gluing layer; finding a small natural noncopying separator is a different theorem, supplied next by GPSH in the graph-product storage sector.

## Provenance

`AUDIT_POST_PHASE_III_OPERATIONAL_CODESENT_GRAND_BOOK_REDUCTION_20260830.md`.
