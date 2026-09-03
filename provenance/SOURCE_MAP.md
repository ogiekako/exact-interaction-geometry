# Source map

This repository is a curated extraction from the chronological research ledger:

```text
repository: ogiekako/test
subtree: experiments/repairable-tropical-north-star
```

References to the ledger below describe research provenance. They are not validation badges, and material absent from this public repository should not be treated as publicly verified mathematics.

## Foundational extraction

The finite response calculus and category-reconstruction theorem were extracted from EIG material developed on 2026-08-30/31. The current canonical EIG Core formulation was reconstructed and audited separately on 2026-09-03. Public files:

- [`../EIG_CORE.md`](../EIG_CORE.md)
- [`../theory/01-finite-exact-interactions.md`](../theory/01-finite-exact-interactions.md)
- [`../theory/02-category-reconstruction.md`](../theory/02-category-reconstruction.md)

Earlier programme-level foundation, boundary-atlas, WEIR, roadmap, and status documents are preserved in Git history rather than kept as competing current formulations. The larger research ledger is intentionally not mirrored here.

## Two-state max-plus comparison theorem

The top-level conventional-mathematics theorem is extracted from the two-state max-plus lane of 2026-08-28, then separately reviewed and repaired for public release on 2026-09-01.

Primary internal theorem note:

```text
docs/TWO_STATE_TAIL_NORMAL_FORM_AND_STATE_COUNT_CALIBRATION.md
```

Separate internal proof/literature review:

```text
docs/AUDIT_TWO_STATE_TAIL_NORMAL_FORM_AND_STATE_COUNT_CALIBRATION.md
```

Dedicated internal literature record:

```text
docs/LITERATURE_STATE_COUNT_DECIDABILITY_FRONTIER.md
```

Earlier exact internal regression:

```text
verification/verify_two_state_projective_one_counter.py
```

The earlier internal review used the shorthand “retain/read separation” for the tail mechanism. During a separate model-assisted adversarial review on 2026-09-01, the literal two-way formulation was found to omit a third logically necessary case: **silent forget**, where the old unbounded gap is erased while the height increment is constant (the all-zero letter is the minimal example). The public proof was therefore repaired to the exact **propagate / forget / read-and-forget trichotomy**. The theorem mechanism that survives is the one-way property needed by the one-counter reduction: a transition whose output increment depends on the unbounded magnitude does not propagate that magnitude to the future.

The public one-counter lemma was simultaneously strengthened to a functional construction with an explicit counter invariant and separate zero-emission drain for forget versus `-1`-emission drain for read-and-forget. The public checker directly classifies the trichotomy and contains the all-zero silent-forget regression.

For the public repository, the theorem and checker were **reconstructed rather than copied wholesale**. Public files:

- [`../discoveries/two-state-maxplus-comparison.md`](../discoveries/two-state-maxplus-comparison.md)
- [`../verification/verify_two_state_maxplus.py`](../verification/verify_two_state_maxplus.py)
- [`TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md)

A dated literature review on 2026-09-01 checked the DGM 2017 problem statement and nearby same-model and adjacent literature. The review did not identify an earlier theorem resolving the two-state comparison case or the stronger arbitrary-left/two-state-right containment statement. This is bounded search evidence, not proof of historical absence.

The curation therefore uses wording equivalent to **“the manuscript proves the `d=2` case of the published DGM 2017 question; no prior resolution was identified in the dated review”**, not an absolute historical-first claim.

## Retired Boolean Tucker calibration

The 2026-08-31 research ledger contains a finite Boolean Tucker rank-profile incompatibility example and verifier. The lane was motivated by the EIG-generated question whether independently minimal Boolean unfolding ranks must always be jointly realizable by one exact Tucker core.

It was briefly extracted into the public repository as a “Boolean Tucker junction counterexample.” A later curation review did not identify a published conjecture or problem asserting that universal property. To avoid implying an external problem resolution that had not been established, the note and checker were removed from the current public tree on 2026-09-02.

Git history and the research ledger preserve the material as project calibration/provenance only. This retirement does not assert that the finite calculation was false; it separates an internally generated finite example from a documented external mathematical problem.

Internal provenance files included:

```text
docs/EIG_EXTERNAL_BOOLEAN_TUCKER_RANK_REGION_20260831.md
verification/verify_eig_external_boolean_tucker_rank_region_20260831.py
docs/EIG_EXTERNAL_BOOLEAN_SEMILATTICE_FLATNESS_FORBIDDEN_HOOK_20260831.md
verification/verify_eig_external_boolean_semilattice_flatness_20260831.py
```

No current EIG theorem or external novelty claim depends on this lane.

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

The public finite certificate is retained, but the theorem is **not presented as historically new to EIG**. A later literature check located Yaroslav Shitov's preprint *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted on **2026-07-25**, which gives another explicit `5 x 5` binary matrix `B` with `rank_01(B)=5` and `rank_01(B tensor B)<=24<25`.

Therefore the EIG-found example is retained only as a project rediscovery / calibration of the parallel-witness search heuristic. No priority is claimed for binary-rank Kronecker nonmultiplicativity.

## Current external-search frontier

The research ledger continues to hold finite-certificate search targets separately from promoted theorem material. Search infrastructure is not evidence unless and until it produces a public proof or certificate appropriate to the claim.

## Earlier source-pair dossier

The source-pair augmentation material remains a secondary candidate/calibration track. It is not the public headline because the wording of the motivating 2018 source-pair question requires a scope interpretation before any claim of resolving that published question.

## Curation principle

Git history preserves earlier public-curation structures and superseded claims. Their deletion or demotion from the current tree is editorial, not historical erasure.

The public repository should expose the shortest chain from EIG's foundational question to exact mathematics while keeping provenance, proof/regression boundaries, prior-art boundaries, corrections, and unresolved novelty questions explicit.
