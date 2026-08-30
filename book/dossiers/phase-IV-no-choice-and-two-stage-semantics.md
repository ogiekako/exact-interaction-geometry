# Dossier IV-C — no natural single chart and two-stage semantics

**Status:** `AUDITED / ACCEPTED` in the stated bare finite-process scopes.

## NO-CHOICE

Let `N_4` be a four-state process with no nonidentity dynamics and a constant observer. There are exactly three nontrivial `2 x 2` Cartesian coordinate systems, and `Aut(N_4)=S_4` acts transitively on them. Therefore there is no isomorphism-natural selector of one nontrivial chart on every process groupoid containing `N_4`.

**Consequence:** a canonical exact structural object may be an equivariant atlas/groupoid of admissible charts rather than one distinguished normal form.

## Formal atlas

For any supplied isomorphism-invariant admissibility predicate, admissible exact decompositions form a groupoid `Dec(P)`, pseudofunctorial under process isomorphism. This is a formal classifier relative to admissibility; it does not by itself prove that the admissible charts are small, finite/cofinal, noncopying, or process-natural.

## NO-COLLAPSE

A single representation can be both lossless for exact raw reconstruction and least-information fully abstract for observer family `O` only when contextual equivalence is equality. Hence the universal architecture has two stages:

```text
lossless structure -> exact raw semantics -> Omega_O.
```

## NO-MAX-DOCTRINE

In the fixed two-sided non-c.e. scalar family, every sound c.e. LOW/HIGH doctrine has strict sound c.e. extensions on both sides. Therefore no strongest effective doctrine exists there. This claim is **not** generalized to all complete-port evaluator doctrines.

## Verification

`verification/verify_no_choice.py` checks the four-state symmetry, the full chart orbit, no-collapse fixture, and finite Cartesian-refinement calibrations.

## Provenance

`UNIVERSAL_BOOK_MAXIMALITY_NO_CHOICE_20260830.md` plus `AUDIT_UNIVERSAL_BOOK_MAXIMALITY_MAIN_20260830.md`.
