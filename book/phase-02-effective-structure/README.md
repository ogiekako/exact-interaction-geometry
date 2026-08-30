# Phase II — effective structural coastlines

**Status: audited scoped theorems.**

Phase II asks a deliberately narrower question than Phase I:

> On which natural structural interfaces can exact semilinear/Presburger behaviour be characterized and compiled, with an explicit theorem explaining both success and failure?

The word **coastline** is intentional: the point is a falsifiable boundary, not an ever-growing whitelist of compiler cases.

## 1. Finite future legality

For a many-sorted alphabet of deterministic partial Presburger letters, let two states be future-equivalent when they admit exactly the same labelled legal continuations.

### Theorem II.1 — finite future-legality theorem
**AUDITED / ACCEPTED.**

The following are equivalent:

1. future-legality equivalence has finite index;
2. there exists a finite Presburger deterministic stable partition;
3. the least many-sorted Boolean algebra closed under guarded partial-map inverse images is finite.

For a letter `a` with guard `G_a` and partial map `F_a`, the correct preimage operator is

```text
Pre_a(S)=G_a intersect F_a^{-1}(S).
```

The truth-atom refinement algorithm, with an actual stability test rather than a plateau heuristic, halts exactly when the finite-index condition holds.

### Boundary
Positive decrement has infinitely many future classes but a simple Presburger clocked endpoint relation. Hence finite future index is a structural theorem, not an iff criterion for all Presburger recurrence.

## 2. One-counter affine lifting

Consider one-counter-net legality with total integral-affine payload, strictly positive public clock, complete counter endpoint exposure, and the audited observable-minimality hypotheses.

### Theorem II.2 — OCN affine lifting
**AUDITED / ACCEPTED.**

The exact response is Presburger iff

```text
(A) the minimal reachable/future-observable coefficient action is finite;
(B) the initialized signed Z-rational intercept is O(|w|+1)
    on every type-compatible word.
```

The criterion is on the **observable minimal action**, not the raw homogeneous matrix monoid: infinite raw directions may be killed by entry/exit maps.

Necessity uses finite public fibres plus a signed semilinear finite-fibre bound; sufficiency uses a degree-one rational-series representation and exact Parikh compilation through the legality backend.

## 3. LCRP lifting interface

### Theorem II.3 — LCRP coastline
**AUDITED / ACCEPTED.**

Finite-control legality and OCN legality instantiate one reusable base interface:

```text
regular legalizable-word support;
exact boundary/product-transition Parikh compilation after finite regular refinement;
one O(|w|) exposed legalizing boundary pair per word;
positive public grading;
payload independence.
```

Over such a base, the same finite-observable-action + linear-intercept criterion is necessary and sufficient for the declared affine response.

This is non-tautological: none of the base axioms says “the answer is Presburger”.

## 4. Sharp near-misses

### Zero-test OCA
Decorated run relations remain effectively Presburger, but the legalizable word language can cease to be regular. Thus the current LCRP backend no longer applies directly. This is a boundary of the theorem, not a proof of hardness.

### Two ordinary legality counters
An audited Hopcroft--Pansiot-type core yields a nonsemilinear exact run relation while retaining a varying endpoint and positive clock/phase information. Therefore the naive unrestricted two-counter extension of the coastline is false.

### Future quotient alone is insufficient
Termination of future-legality refinement does not magically create the freely-scalable affine chart required by the affine iff theorem.

## 5. Why Phase III is forced

Phase II succeeds in several natural sectors but the proofs use different axes:

```text
future legality
storage/counter resource
observable affine action
Parikh/clock structure
public exposure.
```

Adding one more admission clause cannot explain why these axes belong together. Phase III therefore changes the question from

```text
Which presentations does the compiler accept?
```

to

```text
What is the intrinsic compositional mathematical object being presented?
```

## 6. Sources

- `docs/AUDIT_EFFECTIVE_STRUCTURE_COASTLINE_MAIN_20260830.md`
- `docs/AUDIT_EFFECTIVE_STRUCTURE_COASTLINE_INDEPENDENT_20260830.md`

See [`../../provenance/SOURCE_MAP.md`](../../provenance/SOURCE_MAP.md).
