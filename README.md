# Exact Interaction Geometry

**Interaction-first reconstruction of interfaces, objects, and compositional structure.**

Exact Interaction Geometry (EIG) is an emerging mathematical research programme built around a deliberately basic question:

> **How much of mathematical structure can be reconstructed from interaction itself — from what can be composed, what future contexts can distinguish, and what witness data must survive exact gluing — rather than being supplied in advance as objects, states, types, or interfaces?**

The strongest version of that question is open. This repository is a dated foundational disclosure, not a declaration that a new foundation of mathematics has been completed.

**Jump:** [core idea](#the-core-idea) · [exact calibrations](#two-exact-calibrations) · [concrete discoveries](#concrete-discoveries-from-the-interaction-viewpoint) · [open foundation](#what-is-conjectural) · [prior art](#what-is-not-being-claimed) · [status](#current-epistemic-status)

## The core idea

For an interaction fragment `a`, do not begin by assigning it a primitive source object, target object, state type, or semantic label. Instead ask which left and right continuations remain possible and what closed experiments return.

The basic reduction is contextual:

```text
interaction execution
        +
closed continuation response
        |
        v
coarsest response-exact contextual quotient
        |
        v
interfaces / objecthood / witness fibres
        |
        v
composition + descent + reconstructed structure
```

The working EIG architecture is:

```text
CONTEXT
  -> REDUCE
  -> WITNESS
  -> COMPOSE
  -> GLUE / CODESCEND
  -> PROJECT
  -> STRUCTURE
  -> REFLECT
  -> RECONSTRUCT
```

Here **exact** means that a reduction is allowed only when every admitted future continuation has the same response. **Witness** means that multiplicity, provenance, cocycles, or higher comparison data are retained when later interaction can distinguish them. **Geometry** refers to the resulting factorization, descent, obstruction, and localization structure; it is not a claim that every EIG invariant is a metric or curvature.

## Two exact calibrations

### 1. Finite response tables

For a finite response table `M : X x Y -> K`, two left states are contextually equivalent exactly when they have identical response rows. The quotient by this equivalence is the **unique coarsest surjective deterministic exact interface**. If interfaces are instead allowed to carry latent witnesses, exact mediation becomes semiring factorization; serial composition satisfies a data-processing inequality and parallel composition is submultiplicative.

See [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md).

### 2. Categories from untyped interaction

Let `C` be any small category. Erase its objects and every source/target label. Keep only the raw arrows, add an absorbing failure `0`, compose two arrows when they are composable and return `0` otherwise, and observe just one bit:

```text
success = composite is nonzero.
```

Then two-sided continuation success recovers the ordered source/target pair of every arrow. The resulting contextual quotient has one nonzero idempotent for every original object. If the raw arrows are retained as witness fibres over the recovered endpoint classes, the original Hom sets, identities, and composition are recovered exactly.

In this precise category-sector sense,

```text
untyped interaction execution + one-bit success/failure
    -> objects + typing + Hom witnesses + identities + composition.
```

The construction uses classical category consolidation / semigroup ideas; those ingredients are not claimed novel. The point is the operational recognition theorem and its role as a calibration of the broader EIG question.

See [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md).

## Concrete discoveries from the interaction viewpoint

A foundational programme should be judged not only by whether it reorganizes known mathematics, but by whether its viewpoint generates **externally checkable mathematical consequences**.

One such test arose from Parnas--Shraibman's 2018 work on Boolean and binary matrix rank. Their Section 6 asks whether a rank increase caused by jointly augmenting with two source bases must already be witnessed by just one vector chosen from each source.

The factorization-atlas viewpoint suggested the opposite mechanism: incompatibility can be genuinely collective, with every small selection extending through some source even though the whole family does not. Exact search then produced the following candidate discoveries:

1. **4-row Boolean counterexample.** `A={3,7,15}`, with source bases `U={3,5,8}` and `V={3,5,12}`. The full augmentation raises Boolean rank from 3 to 4, while every cross pair `u in U, v in V` leaves rank 3.
2. **5-row binary counterexample.** `A={10,31,27,18}`, `U={4,9,10,18}`, `V={9,10,18,21}`. The full augmentation raises binary rank from 4 to 5, while every cross pair leaves rank 4.
3. **Unbounded Boolean obstruction family.** For every `r>=2`, an explicit rank-`r` matrix has two source bases whose incompatibility requires an augmentation core of exactly `r` vectors. Thus no constant-size local witness principle of this form can hold in Boolean rank.

The structural explanation is a source-incidence Helly/set-cover duality: if `Sigma_A(x)` is the set of source bases that span an admissible added vector `x`, then

```text
rank(A | X) stays r
    iff
intersection_{x in X} Sigma_A(x) is nonempty.
```

So augmentation failure is exactly a collective cover obstruction on the factorization atlas.

**Status before public release:** the checked-in exact integer verifiers pass; these external-discovery claims are intentionally marked **pending an independent mathematical/program recheck and a fresh historical-novelty audit**. They do not depend on WEIR being true, and they do not by themselves prove EIG.

Full statement, proof skeleton, exact instances, verifier instructions, and immutable research provenance: **[`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md)**.

## What is conjectural

The main foundational target is **WEIR — Witness-Enriched Interaction Reconstruction**. Roughly, it asks for natural classes of interaction laboratories in which exact contextual reduction, interface/object selection, map selection, witness reconstruction, composition, doctrine change, and local-to-global descent are all derived from interaction data, up to unavoidable Cauchy/Morita/doctrine moduli.

WEIR is **not proved**. It is stated as a falsifiable programme with explicit acceptance gates in [`theory/03-weir.md`](theory/03-weir.md).

## What is not being claimed

EIG does **not** claim that:

- objectless category theory is new;
- syntactic monoids or Myhill--Nerode minimization are new;
- idempotent splitting / Karoubi completion is new;
- relations-as-primary, allegories, ludics, Geometry of Interaction, Interaction Graphs, or Isbell nuclei are new;
- every mathematical object has already been reconstructed from interaction;
- one doctrine-free notion of objecthood has been identified;
- scalar response is sufficient to recover witness multiplicity or higher coherence;
- category reconstruction automatically gives ULF/Conduche factorization or descent.

The closest prior art is load-bearing. In particular, 2026 work of Gastaldi--Jarvis--Seiller--Terilla derives types from execution and measurement through Isbell nuclei, so **“types emerge from interaction” is not an EIG novelty claim**. See [`PRIOR_ART.md`](PRIOR_ART.md).

## Current epistemic status

This repository deliberately separates four layers:

| Layer | Status |
| --- | --- |
| finite exact residual quotient and elementary factor-rank laws | proved / audited; much of the algebra is classical |
| exact category reconstruction from untyped consolidation + one-bit continuation success | main-audited recognition theorem; classical ingredients |
| external source-pair augmentation discoveries | exact programs pass; independent recheck + novelty audit pending |
| general witness-enriched, doctrine-relative, cross-domain reconstruction | conjectural / open |

The detailed boundary is in [`STATUS.md`](STATUS.md).

## Read in this order

1. [`FOUNDATIONS.md`](FOUNDATIONS.md) — the minimal interaction-first setup and design constraints.
2. [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md) — the smallest exact calculus.
3. [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) — a full object/typing/Hom reconstruction theorem in the category sector.
4. [`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md) — an externally checkable counterexample harvest generated by the viewpoint.
5. [`theory/03-weir.md`](theory/03-weir.md) — the open foundational theorem.
6. [`PRIOR_ART.md`](PRIOR_ART.md) — where EIG overlaps established mathematics.
7. [`ROADMAP.md`](ROADMAP.md) — only the load-bearing open gates.
8. [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md) — source/audit provenance.

## Verification

The foundational category regression is:

```bash
make verify
```

The exact external-discovery checks are:

```bash
make verify-discoveries
```

and CI runs the combined suite with `make verify-all`.

The finite source-pair verifier exhaustively enumerates the displayed Boolean and binary examples. The unbounded-family verifier checks the closed-form formulas through `r=30` and exhausts the base `r=3` case. Regression evidence is not substituted for the infinite mathematical proof or for novelty review.

See [`verification/README.md`](verification/README.md).

## Research process and provenance

The programme was developed through extended AI-assisted mathematical research, with theorem-generation, counterexample-search, repair, and independent adversarial audit lanes. Model-generated claims are not promoted merely because they were generated or computationally checked. Failed and superseded formulations remain in Git history and in the original research ledger; this repository keeps only the current public mathematical surface.

See [`provenance/RESEARCH_PROCESS.md`](provenance/RESEARCH_PROCESS.md) and [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md).

---

**Author:** Keigo Oka  
**Initial EIG public-foundation snapshot:** 2026-08-31  
**Historical novelty:** not claimed for classical ingredients; the novelty and scope of the unified EIG programme and of the external discovery candidates remain subject to independent literature review.
