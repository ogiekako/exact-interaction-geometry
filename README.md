# Exact Interaction Geometry

**Interaction-first reconstruction of interfaces, objects, and compositional structure.**

Exact Interaction Geometry (EIG) is an emerging mathematical research programme built around a deliberately basic question:

> **How much mathematical structure can be reconstructed from interaction itself — from what composes, what future contexts distinguish, and what witness data must survive exact gluing — rather than being supplied in advance as objects, states, types, or interfaces?**

The strongest version of that question is open. This repository is a dated foundational disclosure, not a declaration that a new foundation of mathematics has been completed.

**Jump:** [core idea](#the-core-idea) · [exact calibrations](#two-exact-calibrations) · [external-search evidence](#external-search-evidence) · [open foundation](#what-is-conjectural) · [prior art](#what-is-not-being-claimed) · [status](#current-epistemic-status)

## The core idea

For an interaction fragment `a`, do not begin by assigning it a primitive source object, target object, state type, or semantic label. Instead ask which left and right continuations remain possible and what closed experiments return.

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

Here **exact** means that a reduction is allowed only when every admitted future continuation has the same response. **Witness** means that multiplicity, provenance, cocycles, or higher comparison data are retained when later interaction can distinguish them. **Geometry** refers to the resulting factorization, descent, obstruction, and localization structure; it is not a claim that every EIG invariant is metric geometry.

## Two exact calibrations

### 1. Finite response tables

For a finite response table `M : X x Y -> K`, two left states are contextually equivalent exactly when they have identical response rows. The quotient is the **unique coarsest surjective deterministic exact interface**. If interfaces instead carry latent witnesses, exact mediation becomes semiring factorization; serial composition satisfies a data-processing inequality and parallel composition is submultiplicative.

See [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md).

### 2. Categories from untyped interaction

Let `C` be any small category. Erase its objects and every source/target label. Keep only the raw arrows, add an absorbing failure `0`, compose two arrows when composable and return `0` otherwise, and observe one bit: success iff the composite is nonzero.

Two-sided continuation success recovers the ordered source/target pair of every arrow. The contextual quotient has one nonzero idempotent for every original object. Retaining the raw arrows as witness fibres over the recovered endpoint classes then reconstructs the original Hom sets, identities, and composition exactly.

```text
untyped interaction execution + one-bit success/failure
    -> objects + typing + Hom witnesses + identities + composition.
```

The construction uses classical category consolidation / semigroup ideas; those ingredients are not claimed novel. The point is the operational recognition theorem and its role as a calibration of the broader EIG question.

See [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md).

## External-search evidence

A foundational programme should eventually generate externally checkable mathematics rather than only reorganize known mathematics. EIG therefore maintains a separate certificate-first external-search lane.

### Binary-Kronecker calibration: correct rediscovery, not a novelty claim

The EIG parallel-composition / witness-sharing heuristic independently led to a `5 x 5` binary matrix `A` with

```text
rank_bin(A) = 5,
rank_bin(A tensor A) <= 24 < 25.
```

The proof and 24-rectangle certificate are correct and independently checkable. However, **this is not the first refutation of binary-rank Kronecker multiplicativity**: Yaroslav Shitov publicly posted a different `5 x 5` `5 -> 24` counterexample on **2026-07-25** in *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*.

Accordingly, the EIG-found example is retained only as an independent rediscovery / calibration of the factorization-atlas search methodology. No historical priority is claimed for the nonmultiplicativity theorem.

See [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md).

### Current unresolved targets

The external-search lane is now aimed at targets for which a positive finite certificate would still resolve an explicitly open case:

- **Parnas--Ron--Shraibman `U_{3,20}`.** Their 2019 conjecture predicts Boolean rank `9`; an explicit cover by `8` all-one rectangles would refute it.
- **Exceptional crown Kronecker cases.** The 2026 Parnas survey records `C_5 tensor C_5` and `C_6 tensor C_6` as the exceptional self-product cases not covered by the known crown-family theorem. Since `rank_B(C_5)=rank_B(C_6)=4`, a `15`-rectangle cover would prove strict submultiplicativity.

The earlier source-pair augmentation dossier remains secondary because the wording of its motivating 2018 question admits a scope ambiguity. See [`discoveries/boolean-four-row-one-page.md`](discoveries/boolean-four-row-one-page.md) and [`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md).

The discovery rule is deliberately strict: **search programs may suggest certificates, but only short standalone proofs or finite positive certificates belong on the public mathematical surface.** Historical novelty is audited separately.

## What is conjectural

The main foundational target is **WEIR — Witness-Enriched Interaction Reconstruction**. Roughly, it asks for natural classes of interaction laboratories in which exact contextual reduction, interface/object selection, map selection, witness reconstruction, composition, doctrine change, and local-to-global descent are all derived from interaction data, up to unavoidable Cauchy/Morita/doctrine moduli.

WEIR is **not proved**. It is stated as a falsifiable programme with explicit acceptance gates in [`theory/03-weir.md`](theory/03-weir.md).

## What is not being claimed

EIG does **not** claim that objectless category theory, syntactic monoids, Myhill--Nerode minimization, idempotent splitting, relations-as-primary, allegories, ludics, Geometry of Interaction, Interaction Graphs, or Isbell nuclei are new. Nor does it claim that every mathematical object has been reconstructed from interaction, that one doctrine-free notion of objecthood has been identified, or that scalar response suffices to recover witness multiplicity and higher coherence.

Several established lines of work are directly relevant and sharply constrain what can reasonably be claimed as new here. In particular, 2026 work of Gastaldi--Jarvis--Seiller--Terilla derives types from execution and measurement through Isbell nuclei, so **“types emerge from interaction” is not an EIG novelty claim**. The binary-rank Kronecker nonmultiplicativity theorem is also explicitly not claimed as an EIG first discovery after locating Shitov's 2026-07-25 preprint. See [`PRIOR_ART.md`](PRIOR_ART.md).

## Current epistemic status

| Layer | Status |
| --- | --- |
| finite exact residual quotient and elementary factor-rank laws | proved / audited; much of the algebra is classical |
| exact category reconstruction from untyped consolidation + one-bit continuation success | main-audited recognition theorem; classical ingredients |
| binary-Kronecker `5 -> 24` example | correct independent rediscovery; theorem priority belongs at least to Shitov's 2026-07-25 preprint |
| source-pair and other external candidates | exact checks/proofs as stated; independent scope/novelty review pending |
| general witness-enriched, doctrine-relative, cross-domain reconstruction | conjectural / open |

The detailed boundary is in [`STATUS.md`](STATUS.md).

## Read in this order

1. [`FOUNDATIONS.md`](FOUNDATIONS.md) — the minimal interaction-first setup and design constraints.
2. [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md) — the smallest exact calculus.
3. [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) — a full object/typing/Hom reconstruction theorem in the category sector.
4. [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md) — a correct independent rediscovery retained as a calibration, not a novelty claim.
5. [`discoveries/boolean-four-row-one-page.md`](discoveries/boolean-four-row-one-page.md) — the minimal handwritten source-pair candidate.
6. [`theory/03-weir.md`](theory/03-weir.md) — the open foundational theorem.
7. [`PRIOR_ART.md`](PRIOR_ART.md) — where EIG overlaps established mathematics.
8. [`ROADMAP.md`](ROADMAP.md) — the main open gates.
9. [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md) — source/audit provenance.

## Verification

```bash
make verify-all
```

The binary-Kronecker certificate alone can be checked with:

```bash
python3 verification/verify_binary_kronecker_counterexample.py
```

The checker is intentionally small and does not import the search code. A passing certificate establishes the displayed finite statement, not historical novelty.

See [`verification/README.md`](verification/README.md).

## License

Mathematical notes, theorem/proof text, README files, and other human-readable documentation are licensed under **CC BY 4.0** unless otherwise noted. Source code, scripts, build/workflow files, and machine-readable verification certificates are licensed under the **Apache License 2.0** unless otherwise noted.

See [`LICENSE.md`](LICENSE.md) for the exact scope and license references.

## Research process and provenance

The programme was developed through extended AI-assisted mathematical research, with theorem generation, counterexample search, repair, and independent adversarial audit lanes. Model-generated claims are not promoted merely because they were generated or computationally checked. Failed and superseded formulations remain in Git history and in the original research ledger; this repository keeps only the current public mathematical surface.

See [`provenance/RESEARCH_PROCESS.md`](provenance/RESEARCH_PROCESS.md) and [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md).

---

**Author:** Keigo Oka  
**Initial EIG public-foundation snapshot:** 2026-08-31  
**Historical novelty:** not claimed for classical ingredients; external candidates are promoted only after independent literature review.
