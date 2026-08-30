# Interaction Reconstruction

**Local interactions, exact interfaces, and reconstruction of mathematical structure.**

This repository is the clean public-facing home of a research programme that began with finite-interface recurrent dynamics and evolved toward a broader question:

> **When can a mathematical object, process, or mathematical world be reconstructed from its local interactions, interfaces, and gluing laws?**

The programme is organized as a seven-phase chain rather than as a collection of unrelated results:

```text
Phase I   exact feedback semantics and optimal no-go boundaries
    ↓
Phase II  effective structural coastlines
    ↓
Phase III search for the intrinsic compositional object
    ↓
Phase IV  the Grand Book: exact interfaces, decomposition, reconstruction,
          torsos, obstructions, and optimal opacity
    ↓
Phase V   interaction geometry and resource laws
    ↓
Phase VI  realizability / Grothendieck-style reconstruction
    ↓
Phase VII interaction arities: reconstruction from small local probes
```

The name **Interaction Reconstruction** refers to the final viewpoint, not only to Phase VII. Phases I–IV are load-bearing: they explain why the later profunctor, factorization, residual, and arity structures are forced rather than decorative category theory.

## Current status

| Phase | Current disposition | Short description |
|---|---|---|
| I | **REACHED / audited predecessor theorem** | Exact feedback semantics, fully abstract observer quotient, hard-core localization, and two-sided non-r.e. optimality boundary. |
| II | **Audited scoped structure theorems** | Finite future-legality and one-counter/affine lifting coastlines; sharp positive/negative boundaries. |
| III | **Completed as a transition programme, with audited subtheories** | Replaced “classify Presburger syntax” by “find the intrinsic compositional object”; led directly to the Grand Book. |
| IV | **OPEN as the full Grand Book; many waves audited** | Exact storage/interface factorization, operational codescent, protected process lifting, structural order, recurrent torsos, and globalization are substantially developed. A protected/certified terminal synthesis exists but is not treated here as canonical closure until independently promoted. |
| V | **Generic/meta shell substantially closed; strong programme OPEN / REDUCED** | Exact interaction precedes scalar measurement; factorization resources, support/weight separation, modular flat sectors, and sharp no-go boundaries. The original broad decomposition/prediction ambitions are not declared closed. |
| VI | **Generic raw shell CLOSED / known; strong reduced form OPEN / REDUCED** | Categories of executions over a boundary correspond to normal-lax `Prof` semantics; reduced non-copying interaction stacks remain project-specific. |
| VII | **Generic arity shell CLOSED / known; project-specific form OPEN / REDUCED** | Presentable interaction worlds have dense/nervous arities; the unresolved strong theorem is that the programme's *actual reduced interfaces* are those arities for the intended process world. |

The distinction in the last three rows is important. An independent audit accepted the finite residual-nerve theorem and the standard `Prof`/arity categorical shell, but rejected the stronger claim that the original Phase V–VII programme was completely closed. See [`STATUS.md`](STATUS.md).

## First standalone consequence

The first harvested consequence is an explicit four-row counterexample to a question of Parnas--Shraibman on Boolean-rank augmentation.

- [`papers/boolean-rank-augmentation/`](papers/boolean-rank-augmentation/)
- [`counterexamples/boolean-rank-augmentation/`](counterexamples/boolean-rank-augmentation/)
- [`verification/verify_boolean_rank_augmentation.py`](verification/verify_boolean_rank_augmentation.py)

The counterexample has a short elementary proof and an independent exhaustive verifier. **Its correctness does not depend on the broader Interaction Reconstruction programme.** The programme is discovery provenance only.

## Read the Book

Start with [`book/README.md`](book/README.md). Each phase page is a clean-room synthesis of the currently live mathematics, with explicit status and links back to immutable source material in the original research repository.

## Provenance

The programme originated in [`ogiekako/test`](https://github.com/ogiekako/test), under

```text
experiments/repairable-tropical-north-star
```

The migration baseline for this repository is commit

```text
3806b8ea4851f6edfa7073085e929bdd868442b9
```

on 2026-08-30. The old repository remains the detailed research ledger. This repository is a **curated reconstruction**, not a byte-for-byte mirror.

## Status discipline

Every nontrivial item should be labelled as one of:

- `AUDITED / ACCEPTED`
- `CLAIMED-PROVED; AUDIT PENDING`
- `REDUCED`
- `CONJECTURE`
- `REFUTATION`
- `COMPUTATIONAL EVIDENCE`
- `KNOWN / PRIOR ART`

Counterexamples intended for standalone publication should carry an independent verifier whenever practical and should not depend on unaudited programme-wide claims.
