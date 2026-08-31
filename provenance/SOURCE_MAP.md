# Source map

This repository is a curated extraction from the chronological research ledger:

```text
repository: ogiekako/test
subtree: experiments/repairable-tropical-north-star
```

## Foundational extraction

The finite response calculus, interaction-first objecthood formulation, and category-reconstruction theorem were extracted from the main-audited EIG material of 2026-08-30/31. The relevant public files are:

- [`../theory/01-finite-exact-interactions.md`](../theory/01-finite-exact-interactions.md)
- [`../FOUNDATIONS.md`](../FOUNDATIONS.md)
- [`../theory/02-category-reconstruction.md`](../theory/02-category-reconstruction.md)
- [`../theory/03-weir.md`](../theory/03-weir.md)

The much larger research ledger is intentionally not mirrored here. Newer results are imported only when they improve the public mathematical surface without importing unresolved dependencies or programme history.

## Binary-Kronecker external discovery

The current headline external discovery was produced after the public foundation snapshot.

Search infrastructure was first committed in the research ledger at:

```text
a7c228e3bd4fb0dcd81696dc4a4106fdfe12fd58
```

A local-main audit then hardened the search/certificate infrastructure at:

```text
f8a1c2315f33ec8dd9ed6c0e3c447de702980527
```

The user-executed 48-core run returned the 24-rectangle certificate on 2026-08-31 JST. The proof/certificate/verifier handoff is reachable at:

```text
ed7cd7fe5e6b02a3e7f65ebf4f3c5b31670fac0f
```

Source paths in the ledger:

```text
docs/EIG_EXTERNAL_BINARY_KRONECKER_COUNTEREXAMPLE_20260831.md
counterexample_search/eig_kronecker_rank/certificates/seed5_self_k24.json
verification/verify_eig_binary_kronecker_counterexample_20260831.py
.handoff/20260831-2046-jst-eig-binary-kronecker-counterexample.md
```

The public extraction deliberately simplifies the verifier: it retains only the null-vector/minor certificate and direct rectangle check, not the discovery searcher or an unnecessary exact rank-minimization routine.

Public files:

- [`../discoveries/binary-kronecker-counterexample.md`](../discoveries/binary-kronecker-counterexample.md)
- [`../discoveries/certificates/binary-kronecker-seed5-self-k24.json`](../discoveries/certificates/binary-kronecker-seed5-self-k24.json)
- [`../verification/verify_binary_kronecker_counterexample.py`](../verification/verify_binary_kronecker_counterexample.py)

Status: complete finite argument and certificate internally checked; **independent author/program recheck and specialist historical-novelty audit remain pending before public priority is asserted**.

## Earlier source-pair dossier

The source-pair augmentation material remains a secondary external discovery track. Its immutable ledger sequence begins with the four-row Boolean example and continues through binary and unbounded Boolean variants. Public extraction:

- [`../discoveries/boolean-four-row-one-page.md`](../discoveries/boolean-four-row-one-page.md)
- [`../discoveries/source-pair-augmentation.md`](../discoveries/source-pair-augmentation.md)
- [`../verification/verify_source_pair_counterexamples.py`](../verification/verify_source_pair_counterexamples.py)
- [`../verification/verify_unbounded_boolean_augmentation.py`](../verification/verify_unbounded_boolean_augmentation.py)

It is not the headline discovery because the wording of the motivating 2018 source-pair question requires a scope interpretation before any claim of resolving that published question.

## Curation principle

Git history preserves earlier public-curation structures, including the former `Interaction Reconstruction` seven-phase Book and standalone theorem harvests. Their deletion from the current tree is editorial, not historical erasure.

The public repository should expose the shortest chain from EIG's foundational question to exact mathematics, while keeping provenance, proof certificates, prior-art boundaries, and unresolved novelty questions explicit.
