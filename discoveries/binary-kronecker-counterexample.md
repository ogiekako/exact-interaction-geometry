# Binary-Kronecker calibration — independent rediscovery after Shitov (2026)

**Status:** correct finite certificate; **not a historical novelty claim**.

Here **binary rank** means the minimum number of binary rank-one matrices whose ordinary integer sum is the given `0/1` matrix; equivalently, the minimum number of all-one rectangles that partition its `1` entries exactly. It is **not** rank over `GF(2)`.

This repository originally presented the following `5 x 5` binary-rank example as a candidate new refutation of Kronecker multiplicativity:

```text
A = [
  [0, 1, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1],
]

rank_bin(A) = 5,
rank_bin(A tensor A) <= 24 < 25.
```

The finite mathematics remains correct: a short handwritten lower bound proves `rank_bin(A)=5`, and the checked-in 24 rectangles partition all 196 ones of `A tensor A` exactly once.

However, this is **not the first refutation of binary-rank Kronecker multiplicativity**. Yaroslav Shitov publicly posted *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol* on **2026-07-25** and gave a different `5 x 5` binary matrix `B` with

```text
rank_01(B) = 5,
rank_01(B tensor B) <= 24 < 25.
```

Accordingly, the present example is retained only as an **independent rediscovery / computational calibration** of the EIG factorization-atlas search methodology. No historical priority is claimed for the nonmultiplicativity theorem.

The EIG provenance remains informative: the target was selected from the parallel-composition heuristic that the product of two locally minimal witness atlases need not remain globally minimal after composition, and an exact 24-rectangle certificate was then found independently. But EIG is not a logical dependency of the matrix result, and Shitov's earlier counterexample means this example is not suitable as headline external novelty evidence.

## Finite certificate

The proof that `rank_bin(A)=5` uses two null vectors

```text
ell = (-1, 1, -1, 1, 0)^T,
r   = (-1,-1,  0, 1, 1)^T,
```

with `ell^T A=0`, `A r=0`, together with a unimodular `4 x 4` minor. Under a hypothetical four-term binary factorization, the term covering `A[3,1]=1` is forced by the two balance equations to cover a zero entry, a contradiction.

The machine-readable 24-rectangle self-product certificate is:

- [`certificates/binary-kronecker-seed5-self-k24.json`](certificates/binary-kronecker-seed5-self-k24.json)

and the independent checker is:

- [`../verification/verify_binary_kronecker_counterexample.py`](../verification/verify_binary_kronecker_counterexample.py)

The JSON file is the single source of rectangle data. The checker reads it directly, reconstructs the raw Kronecker matrix, checks support containment and exact-once coverage of all 196 ones, and independently computes `rank_bin(A)=5` by enumerating all legal rectangles of the `5 x 5` support and solving the resulting exact-cover problem by dynamic programming. Thus the machine check does not depend on the handwritten null-vector lemma or on the discovery searcher.

## Prior art

- Y. Shitov, *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted 2026-07-25, DOI `10.13140/RG.2.2.26449.90723`.

The EIG-found matrix is a different explicit example, but that does not restore theorem-level novelty.

## Current search direction

The certificate-first external-search lane is now aimed at unresolved targets with equally small positive certificates, especially:

1. the Parnas--Ron--Shraibman `U_{3,20}` Boolean-rank conjecture, where an `8`-rectangle cover would refute the predicted rank `9`;
2. the exceptional Boolean crown self-products `C_5 tensor C_5` and `C_6 tensor C_6`, where a `15`-rectangle cover would prove strict submultiplicativity.

The correction itself is part of the epistemic record: finite correctness and historical novelty are separate questions.
