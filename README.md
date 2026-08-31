# Exact Interaction Geometry

**Interaction-first reconstruction of interfaces, objects, and compositional structure.**

Exact Interaction Geometry (EIG) is an emerging mathematical research programme built around a deliberately basic question:

> **How much mathematical structure can be reconstructed from interaction itself — from what composes, what future contexts distinguish, and what witness data must survive exact gluing — rather than being supplied in advance as objects, states, types, or interfaces?**

The strongest version of that question is open. This repository is a dated foundational disclosure, not a declaration that a new foundation of mathematics has been completed.

**Jump:** [core idea](#the-core-idea) · [headline discovery](#headline-external-discovery) · [exact calibrations](#two-exact-calibrations) · [open foundation](#what-is-conjectural) · [prior art](#what-is-not-being-claimed) · [status](#current-epistemic-status)

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

## Headline external discovery

### Binary rank is not multiplicative under Kronecker product

A useful test of a foundational viewpoint is whether it generates externally checkable mathematics rather than only new vocabulary. The strongest current example in this programme is a finite counterexample to Kronecker multiplicativity of the binary rank.

The counterexample is the following `5 x 5` binary matrix, written explicitly as five rows:

```text
A = [
  [0, 1, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1],
]
```

A short handwritten argument proves **`rank_bin(A) = 5`**. An explicit 24-biclique partition of `A ⊗ A` proves the strict inequality

> **`rank_bin(A ⊗ A) ≤ 24 < 25 = rank_bin(A)^2`.**

The lower bound uses only two displayed integer null vectors and one unimodular `4 x 4` minor. The upper bound is a finite list of 24 rectangles partitioning all 196 one-entries of the tensor product exactly once. The search program that found the list is **not** part of the proof.

**Typeset PDF (recommended for reading):** [`discoveries/binary-kronecker-counterexample.pdf`](discoveries/binary-kronecker-counterexample.pdf)  
**Markdown certificate:** [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md)  
**TeX source:** [`discoveries/binary-kronecker-counterexample.tex`](discoveries/binary-kronecker-counterexample.tex)  
**Machine-readable certificate:** [`discoveries/certificates/binary-kronecker-seed5-self-k24.json`](discoveries/certificates/binary-kronecker-seed5-self-k24.json)  
**Independent checker:** [`verification/verify_binary_kronecker_counterexample.py`](verification/verify_binary_kronecker_counterexample.py)

The target was selected from the EIG factorization/parallel-composition heuristic: the product of two individually minimal witness atlases need not remain globally minimal after composition because cross-factor witness sharing can appear only after the product is formed. This motivation is provenance, not a logical dependency of the counterexample.

A targeted literature check on 2026-08-31 found the integer multiplicativity question still explicitly open in Ghosal--Karrenbauer (SEA 2025) and in Parnas's 2026 survey. **Historical novelty and priority remain subject to an independent specialist audit before public priority is asserted.**

A second, earlier discovery dossier concerns source-pair augmentation for Boolean/binary rank. Its clean four-row Boolean certificate remains available, but it is secondary because the wording of the motivating 2018 open question admits a scope ambiguity. See [`discoveries/boolean-four-row-one-page.md`](discoveries/boolean-four-row-one-page.md) and [`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md).

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

## What is conjectural

The main foundational target is **WEIR — Witness-Enriched Interaction Reconstruction**. Roughly, it asks for natural classes of interaction laboratories in which exact contextual reduction, interface/object selection, map selection, witness reconstruction, composition, doctrine change, and local-to-global descent are all derived from interaction data, up to unavoidable Cauchy/Morita/doctrine moduli.

WEIR is **not proved**. It is stated as a falsifiable programme with explicit acceptance gates in [`theory/03-weir.md`](theory/03-weir.md).

## What is not being claimed

EIG does **not** claim that objectless category theory, syntactic monoids, Myhill--Nerode minimization, idempotent splitting, relations-as-primary, allegories, ludics, Geometry of Interaction, Interaction Graphs, or Isbell nuclei are new. Nor does it claim that every mathematical object has been reconstructed from interaction, that one doctrine-free notion of objecthood has been identified, or that scalar response suffices to recover witness multiplicity and higher coherence.

Several established lines of work are directly relevant and sharply constrain what can reasonably be claimed as new here. In particular, 2026 work of Gastaldi--Jarvis--Seiller--Terilla derives types from execution and measurement through Isbell nuclei, so **“types emerge from interaction” is not an EIG novelty claim**. See [`PRIOR_ART.md`](PRIOR_ART.md).

## Current epistemic status

| Layer | Status |
| --- | --- |
| finite exact residual quotient and elementary factor-rank laws | proved / audited; much of the algebra is classical |
| exact category reconstruction from untyped consolidation + one-bit continuation success | main-audited recognition theorem; classical ingredients |
| binary-rank Kronecker counterexample `5 x 5 -> 24 < 25` | complete finite proof + exact certificate internally checked; independent author/program recheck and novelty audit pending |
| source-pair augmentation discoveries | exact checks / written proofs available; publication scope and novelty audit pending |
| general witness-enriched, doctrine-relative, cross-domain reconstruction | conjectural / open |

The detailed boundary is in [`STATUS.md`](STATUS.md).

## Read in this order

1. [`FOUNDATIONS.md`](FOUNDATIONS.md) — the minimal interaction-first setup and design constraints.
2. [`discoveries/binary-kronecker-counterexample.pdf`](discoveries/binary-kronecker-counterexample.pdf) — the recommended typeset version of the strongest current external finite discovery; the [`Markdown version`](discoveries/binary-kronecker-counterexample.md) is kept for browsing and diffs.
3. [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md) — the smallest exact calculus.
4. [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) — a full object/typing/Hom reconstruction theorem in the category sector.
5. [`theory/03-weir.md`](theory/03-weir.md) — the open foundational theorem.
6. [`PRIOR_ART.md`](PRIOR_ART.md) — where EIG overlaps established mathematics.
7. [`discoveries/boolean-four-row-one-page.md`](discoveries/boolean-four-row-one-page.md) — an earlier handwritten factorization-atlas counterexample.
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

The checker is intentionally small and does not import the search code. It verifies the handwritten lower-bound ingredients and the exact-once 24-rectangle partition directly from the displayed data.

The typeset discovery note is generated from [`discoveries/binary-kronecker-counterexample.tex`](discoveries/binary-kronecker-counterexample.tex). The dedicated GitHub Actions workflow recompiles the TeX, uploads the compiled artifact, and publishes the checked-in PDF whenever the TeX source changes on `main`.

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
**Historical novelty:** not claimed for classical ingredients; the novelty and scope of the unified EIG programme and of the external discoveries remain subject to independent literature review.
