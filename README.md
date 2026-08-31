# Exact Interaction Geometry

**Interaction-first reconstruction of interfaces, objects, and compositional structure.**

Exact Interaction Geometry (EIG) is an emerging mathematical research programme built around a deliberately basic question:

> **How much mathematical structure can be reconstructed from interaction itself — from what composes, what future contexts distinguish, and what witness data must survive exact gluing — rather than being supplied in advance as objects, states, types, or interfaces?**

The strongest version of that question is open. This repository is a dated foundational disclosure, not a declaration that a new foundation of mathematics has been completed.

**Jump:** [core idea](#the-core-idea) · [Boolean Tucker case study](#a-small-external-case-study-boolean-tucker-junction-failure) · [exact calibrations](#two-exact-calibrations) · [open foundation](#what-is-conjectural) · [prior art](#what-is-not-being-claimed) · [status](#current-epistemic-status)

## The core idea

For an interaction fragment `a`, do not begin by assigning it a primitive source object, target object, state type, or semantic label. Instead ask which left and right continuations remain possible and what closed experiments return.

```text
interaction execution + closed continuation response
                        ↓
coarsest response-exact contextual quotient
                        ↓
interfaces / objecthood / witness fibres
                        ↓
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

## A small external case study: Boolean Tucker junction failure

A useful test of EIG is whether its internal questions lead to ordinary mathematics that can be checked without accepting EIG terminology.

One recurring EIG question is:

> **If each boundary admits an independently minimal exact interface, must those minima glue through one common junction witness?**

This leads naturally to exact Boolean Tucker decomposition. For a Boolean tensor `T`, minimize each mode unfolding separately using Boolean matrix rank, then ask whether those minima can be realized simultaneously by one Boolean Tucker core.

They need not be.

There is an explicit `2 x 4 x 4` Boolean tensor with

```text
mode Boolean ranks = (2,3,3)
```

but no exact Boolean Tucker decomposition of profile `(2,3,3)`. Its exact feasible profile region is

```text
Tuck_B(T) = Up(2,3,4) union Up(2,4,3)
```

where `Up(p,q,r)` denotes the componentwise upward closure. Thus the exact Boolean Tucker profile poset has two incomparable Pareto minima and no componentwise least element for this tensor.

The obstruction is tiny: one positive tensor entry has only four possible lifts through the two minimum latent interfaces, and four explicitly displayed zeros block all four lifts.

```text
EIG question: independently minimal interfaces — do they jointly descend?
                                ↓
Boolean Tucker translation: minimize each unfolding separately
                                ↓
counterexample: (2,3,3) local minima cannot share one exact core
                                ↓
small obstruction: every candidate latent lift of one positive is blocked
```

This is the role external examples are meant to play here: EIG suggests the structural question and failure mechanism; the resulting mathematical statement is then verified independently in standard language.

**Read the counterexample:** [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md)  
**Run the solver-free checker:** `python3 verification/verify_boolean_tucker_junction_counterexample.py`

A follow-up analysis in the private research ledger identifies two minimal rank-three separator types (`F` and `T`), classifies their reduced fiber/tensor holes, and finds a common three-zero hook obstruction. It also connects the safe side of the phenomenon to classical distributive/flat semilattices. The proof/checker for that follow-up is not imported into this public repository, so it is treated here as **ledger-audited provenance**, not as a public independently reproducible theorem. None of it is needed for the Boolean Tucker counterexample above.

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

## Other external-search evidence

The repository keeps external-search results separate from foundational claims.

### Binary-Kronecker calibration

The EIG parallel-composition heuristic independently led to a correct `5 x 5` binary matrix with

```text
rank_bin(A) = 5,
rank_bin(A tensor A) <= 24 < 25.
```

This is **not** a novelty claim: Yaroslav Shitov had publicly posted a different `5 x 5` `5 -> 24` counterexample on 2026-07-25. The EIG-found example is retained only as an independent rediscovery / calibration of the search methodology. See [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md).

The earlier source-pair augmentation dossier is also retained as secondary evidence because the wording of its motivating 2018 question admits a scope ambiguity. See [`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md).

Current private search lanes target unresolved finite-certificate problems such as Parnas--Ron--Shraibman `U_{3,20}` and the exceptional crown self-products. Search programs do not become public mathematical claims unless they return a short independently checked certificate.

## What is conjectural

The main foundational target is **WEIR — Witness-Enriched Interaction Reconstruction**. Roughly, it asks for natural classes of interaction laboratories in which exact contextual reduction, interface/object selection, map selection, witness reconstruction, composition, doctrine change, and local-to-global descent are all derived from interaction data, up to unavoidable Cauchy/Morita/doctrine moduli.

WEIR is **not proved**. It is stated as a falsifiable programme with explicit acceptance gates in [`theory/03-weir.md`](theory/03-weir.md).

## What is not being claimed

EIG does **not** claim that objectless category theory, syntactic monoids, Myhill--Nerode minimization, idempotent splitting, relations-as-primary, allegories, ludics, Geometry of Interaction, Interaction Graphs, or Isbell nuclei are new. Nor does it claim that every mathematical object has been reconstructed from interaction, that one doctrine-free notion of objecthood has been identified, or that scalar response suffices to recover witness multiplicity and higher coherence.

Boolean Tucker decomposition is established prior work; constrained Tucker decompositions are also known to exhibit non-field-like rank phenomena in other cones, including nonnegative Tucker models. The EIG case study here is deliberately narrower: it records one explicit exact Boolean junction failure and the interaction-first question that exposed it. See [`PRIOR_ART.md`](PRIOR_ART.md).

## Current epistemic status

| Layer | Status |
| --- | --- |
| finite exact residual quotient and elementary factor-rank laws | proved / publicly documented; much of the algebra is classical |
| exact category reconstruction from untyped consolidation + one-bit continuation success | publicly documented theorem with end-to-end finite regression; classical ingredients |
| explicit Boolean Tucker `(2,3,3)` junction counterexample and displayed rank region for that tensor | finite exact statement with solver-free exhaustive checker; no historical `first` claim |
| rank-three `F/T` reduced separator classification and three-zero hook | ledger-audited; public proof/checker not imported; broader universal converse remains reduced |
| binary-Kronecker `5 -> 24` example | correct independent rediscovery; no theorem-priority claim |
| source-pair and current search targets | secondary / candidate evidence; scope or novelty review pending |
| general witness-enriched, doctrine-relative, cross-domain reconstruction | conjectural / open |

The detailed boundary is in [`STATUS.md`](STATUS.md).

## Read in this order

1. [`FOUNDATIONS.md`](FOUNDATIONS.md) — the minimal interaction-first setup and design constraints.
2. [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md) — the clearest current example of the EIG-to-external-mathematics workflow.
3. [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md) — the smallest exact calculus.
4. [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) — a full object/typing/Hom reconstruction theorem in the category sector.
5. [`theory/03-weir.md`](theory/03-weir.md) — the open foundational theorem.
6. [`PRIOR_ART.md`](PRIOR_ART.md) — where EIG overlaps established mathematics.
7. [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md) — a correct rediscovery retained as calibration.
8. [`ROADMAP.md`](ROADMAP.md) — the main open gates.
9. [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md) — source/audit provenance.

## Verification

```bash
make verify-all
```

The Boolean Tucker case study alone can be checked with

```bash
python3 verification/verify_boolean_tucker_junction_counterexample.py
```

The checker uses no external solver, floating point, randomness, normalization lemma, or discovery code; it exhausts all nonzero support masks on each mode.

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
**Historical novelty:** not claimed for classical ingredients; external examples are presented at the narrowest independently supported scope.
