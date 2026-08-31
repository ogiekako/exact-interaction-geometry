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

## Two-state max-plus comparison theorem

The staged top-level conventional-mathematics theorem is extracted from the two-state max-plus lane of 2026-08-28, then re-audited for public staging on 2026-09-01.

Primary ledger theorem note:

```text
docs/TWO_STATE_TAIL_NORMAL_FORM_AND_STATE_COUNT_CALIBRATION.md
```

Independent ledger proof/literature audit:

```text
docs/AUDIT_TWO_STATE_TAIL_NORMAL_FORM_AND_STATE_COUNT_CALIBRATION.md
```

Dedicated ledger literature record:

```text
docs/LITERATURE_STATE_COUNT_DECIDABILITY_FRONTIER.md
```

Earlier exact ledger regression:

```text
verification/verify_two_state_projective_one_counter.py
```

The earlier independent audit records `825,266` exact checks and promotes the closed forms, threshold, retain/read separation, exact one-counter compilation, decorated semilinearity, right-hand containment, and two-state positivity theorem.

For the public repository, the theorem and checker were **reconstructed rather than copied wholesale**. The public note states the weighted-automata theorem without requiring EIG terminology, and the public checker independently reimplements the algebra/tail/compiler regressions.

Public staged files:

- [`../discoveries/two-state-maxplus-comparison.md`](../discoveries/two-state-maxplus-comparison.md)
- [`../verification/verify_two_state_maxplus.py`](../verification/verify_two_state_maxplus.py)
- [`TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md)

A fresh 2026-09-01 literature audit confirmed that Daviaud--Guillon--Merlet (MFCS 2017) explicitly leave bounded-state comparison open from 2 through 552 states after their 553-state undecidability theorem. Searches across same-model two-state identities, comparison/equivalence surveys, `2 x 2` tropical-matrix structure, ambiguity/simulation classes, few-register CRA work, and the 2026 determinisation/unambiguisation/unary-tropical literature located no earlier theorem resolving the two-state comparison case or the stronger arbitrary-left/two-state-right containment statement.

The curation therefore uses the wording **“published open `d=2` case resolved; no prior resolution located in the dated audit”**, not an absolute historical-first claim.

## Boolean Tucker external case study

The second external case study is extracted from the 2026-08-31 Boolean junction/Tucker lane in the research ledger.

Primary ledger note:

```text
docs/EIG_EXTERNAL_BOOLEAN_TUCKER_RANK_REGION_20260831.md
```

Solver-free ledger verifier:

```text
verification/verify_eig_external_boolean_tucker_rank_region_20260831.py
```

Follow-up structural note:

```text
docs/EIG_EXTERNAL_BOOLEAN_SEMILATTICE_FLATNESS_FORBIDDEN_HOOK_20260831.md
```

Follow-up verifier:

```text
verification/verify_eig_external_boolean_semilattice_flatness_20260831.py
```

The public extraction intentionally narrows the story. It presents the explicit `2 x 4 x 4` Boolean Tucker incompatibility, its small blocker certificate, and the EIG question that led to it. It does not rely on a historical `first` claim.

Public files:

- [`../discoveries/boolean-tucker-junction-counterexample.md`](../discoveries/boolean-tucker-junction-counterexample.md)
- [`../verification/verify_boolean_tucker_junction_counterexample.py`](../verification/verify_boolean_tucker_junction_counterexample.py)

The reduced F/T/three-zero-hook classification remains summarized as structural follow-up rather than being imported wholesale into the public core. The ledger itself records the classical semilattice flatness/distributivity boundary and the remaining universal identification bridge.

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

The finite mathematics is correct, but the theorem is **not historically new to EIG**. A later literature check located Yaroslav Shitov's preprint *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted on **2026-07-25**, which gives another explicit `5 x 5` binary matrix `B` with `rank_01(B)=5` and `rank_01(B tensor B)<=24<25`.

Therefore the EIG-found example is retained only as an independent rediscovery / calibration of the parallel-witness search heuristic. No priority is claimed for binary-rank Kronecker nonmultiplicativity.

## Current external-search frontier

The research ledger continues to hold finite-certificate search targets separately from promoted theorem material. Search infrastructure is not imported as evidence unless it returns a short independently audited mathematical result.

## Earlier source-pair dossier

The source-pair augmentation material remains a secondary candidate/calibration track. It is not the public headline because the wording of the motivating 2018 source-pair question requires a scope interpretation before any claim of resolving that published question.

## Curation principle

Git history preserves earlier public-curation structures and superseded claims. Their deletion or demotion from the current tree is editorial, not historical erasure.

The public repository should expose the shortest chain from EIG's foundational question to exact mathematics while keeping provenance, proof/regression boundaries, prior-art boundaries, corrections, and unresolved novelty questions explicit.
