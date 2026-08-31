# Source map

This repository is a curated extraction from the chronological research ledger:

```text
repository: ogiekako/test
subtree: experiments/repairable-tropical-north-star
```

## Foundational extraction

The finite response calculus, interaction-first objecthood formulation, and category-reconstruction theorem were extracted from the main-audited EIG material of 2026-08-30/31. Public files:

- [`../theory/01-finite-exact-interactions.md`](../theory/01-finite-exact-interactions.md)
- [`../FOUNDATIONS.md`](../FOUNDATIONS.md)
- [`../theory/02-category-reconstruction.md`](../theory/02-category-reconstruction.md)
- [`../theory/03-weir.md`](../theory/03-weir.md)

The larger research ledger is intentionally not mirrored here. Newer results are imported only when they improve the public mathematical surface without importing unresolved dependencies or programme history.

## Binary-Kronecker calibration and priority correction

The EIG search infrastructure was committed in the research ledger at

```text
a7c228e3bd4fb0dcd81696dc4a4106fdfe12fd58
```

and locally hardened at

```text
f8a1c2315f33ec8dd9ed6c0e3c447de702980527.
```

A user-executed 48-core run then found a different explicit `5 x 5` binary matrix with `rank_bin(A)=5` and a 24-biclique partition of `A tensor A`. The proof/certificate/verifier handoff is reachable at

```text
ed7cd7fe5e6b02a3e7f65ebf4f3c5b31670fac0f.
```

The finite mathematics is correct, but the theorem is **not historically new to EIG**. A later literature check located Yaroslav Shitov's preprint *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted on **2026-07-25**, which gives another explicit `5 x 5` binary matrix `B` with

```text
rank_01(B)=5,
rank_01(B tensor B)<=24<25.
```

Therefore the EIG-found example is retained only as an independent rediscovery / calibration of the parallel-witness search heuristic. No priority is claimed for binary-rank Kronecker nonmultiplicativity.

Public files retained for reproducibility:

- [`../discoveries/binary-kronecker-counterexample.md`](../discoveries/binary-kronecker-counterexample.md)
- [`../discoveries/certificates/binary-kronecker-seed5-self-k24.json`](../discoveries/certificates/binary-kronecker-seed5-self-k24.json)
- [`../verification/verify_binary_kronecker_counterexample.py`](../verification/verify_binary_kronecker_counterexample.py)

The pre-correction TeX/PDF presentation and its dedicated build workflow were removed from the current tree after the priority correction; Git history preserves them.

## Current external-search frontier

The private research ledger now prioritizes finite-certificate targets that remained unresolved in the literature checked on 2026-08-31:

1. Parnas--Ron--Shraibman `U_{3,20}`: an 8-rectangle Boolean cover would refute the conjectured rank `9`.
2. `C_5 tensor C_5`: a 15-rectangle Boolean cover would settle the exceptional crown self-product strictly.
3. `C_6 tensor C_6`: same 15-rectangle target.

The corresponding 48-core/CUDA/SAT search infrastructure is kept in the research ledger, not imported into the public foundation unless it produces a new independently audited certificate.

## Earlier source-pair dossier

The source-pair augmentation material remains a secondary candidate track. Public extraction:

- [`../discoveries/boolean-four-row-one-page.md`](../discoveries/boolean-four-row-one-page.md)
- [`../discoveries/source-pair-augmentation.md`](../discoveries/source-pair-augmentation.md)
- [`../verification/verify_source_pair_counterexamples.py`](../verification/verify_source_pair_counterexamples.py)
- [`../verification/verify_unbounded_boolean_augmentation.py`](../verification/verify_unbounded_boolean_augmentation.py)

It is not a headline discovery because the wording of the motivating 2018 source-pair question requires a scope interpretation before any claim of resolving that published question.

## Curation principle

Git history preserves earlier public-curation structures and superseded claims. Their deletion or demotion from the current tree is editorial, not historical erasure.

The public repository should expose the shortest chain from EIG's foundational question to exact mathematics while keeping provenance, proof certificates, prior-art boundaries, corrections, and unresolved novelty questions explicit.
