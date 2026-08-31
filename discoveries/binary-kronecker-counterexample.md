# Binary rank is not multiplicative under Kronecker product

**Status:** complete finite proof and exact positive certificate; independent author/program recheck and historical-novelty audit pending before public priority is asserted.

> **Recommended for reading:** [`binary-kronecker-counterexample.pdf`](binary-kronecker-counterexample.pdf) — the same note, typeset from the checked-in [`TeX source`](binary-kronecker-counterexample.tex). The Markdown version below is retained for convenient GitHub browsing, search, and diffs. GitHub Actions recompiles and publishes the PDF when the TeX source changes.

This note is deliberately self-contained. The search procedure that found the certificate is not part of the proof.

## Result

Let `A` be the following `5 x 5` binary matrix, written explicitly as five rows:

```text
A = [
  [0, 1, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 1, 0, 1, 1],
]
```

For a binary matrix, `rank_bin` is the least number of all-one rectangles whose disjoint union is its set of `1` entries; equivalently it is the least `r` for a factorization `A = U V` with binary `U,V` under ordinary integer multiplication.

The claim is

```text
rank_bin(A) = 5,
rank_bin(A tensor A) <= 24,
```

and therefore

> **`rank_bin(A tensor A) < rank_bin(A)^2`.**

Thus binary rank is not multiplicative under Kronecker product.

## A short proof that `rank_bin(A) = 5`

Five row-stars partition the support of `A`, so `rank_bin(A) <= 5`.

Put

```text
ell = (-1, 1, -1, 1, 0)^T,
r   = (-1,-1,  0, 1, 1)^T.
```

Direct calculation gives

```text
ell^T A = 0,
A r     = 0.
```

The submatrix on rows `1,2,3,5` and columns `1,2,3,4` has determinant `-1`, hence the ordinary real rank of `A` is `4`.

Assume for contradiction that `rank_bin(A) <= 4`, so

```text
A = U V,
U in {0,1}^{5 x 4},
V in {0,1}^{4 x 5}.
```

Because the real rank of `A` is `4`, both factors have real rank four. Therefore every column `u` of `U` and corresponding row `v^T` of `V` obey

```text
ell^T u = 0,
v^T r   = 0.          (1)
```

Some rank-one term `u v^T` covers `A[3,1] = 1`, so `u_3 = v_1 = 1` (one-based indices).

From `ell^T u = 0`,

```text
u_2 + u_4 = u_1 + u_3 = u_1 + 1.
```

Since `A[4,1] = 0` and `v_1 = 1`, support containment forces `u_4 = 0`; binary-valuedness then forces `u_1 = 0` and `u_2 = 1`.

Likewise `v^T r = 0` gives

```text
v_4 + v_5 = v_1 + v_2 = 1 + v_2.
```

Since `A[3,5] = 0` and `u_3 = 1`, support containment forces `v_5 = 0`; hence `v_2 = 0` and `v_4 = 1`.

But then `u_2 = v_4 = 1`, so the same rank-one term covers `A[2,4]`, while `A[2,4] = 0`. Contradiction. Thus `rank_bin(A) = 5`.

## The 24-rectangle certificate for `A tensor A`

Index rows and columns of `A tensor A` by `0,...,24` in lexicographic order on pairs in `{0,...,4}^2`. The following 24 all-one rectangles partition all `196 = 14^2` ones exactly once:

```text
 1  R={2,7,9}          C={10,13,20,23}
 2  R={10,14,20}       C={1,4,16,19}
 3  R={5,9}            C={1,4,11,14,21,24}
 4  R={7,9,12,14,22}   C={0,3}
 5  R={18,19}          C={6,8,16,18}
 6  R={13,23,24}       C={1,3,16,18}
 7  R={3,23,24}        C={6,8,21,23}
 8  R={1}              C={5,7,9,20,22,24}
 9  R={8}              C={1,3,11,13,21,23}
10  R={2,17}           C={5,8}
11  R={0,1,5,6}        C={12}
12  R={10,11}          C={2,17}
13  R={0}              C={6,7,9,11,14,21,22,24}
14  R={5,6,20,21}      C={2,22}
15  R={16,19,21,24}    C={5,9,15,19}
16  R={4,22}           C={5,8,20,23}
17  R={3,4}            C={11,13}
18  R={4,20}           C={6,9,21,24}
19  R={15}             C={6,7,9,16,17,19}
20  R={11}             C={0,4,15,19}
21  R={6,21,24}        C={0,4,20,24}
22  R={16,20,21}       C={7,17}
23  R={1,4,6}          C={10,14}
24  R={12,14,17,22}    C={15,18}
```

The machine-readable copy is [`certificates/binary-kronecker-seed5-self-k24.json`](certificates/binary-kronecker-seed5-self-k24.json).

A small independent checker reconstructs the raw Kronecker matrix and verifies that every listed rectangle is contained in the support and every one-entry occurs exactly once:

```bash
python3 verification/verify_binary_kronecker_counterexample.py
```

The checker also verifies the two null vectors, the unimodular `4 x 4` minor, and exhaustively checks the tiny local balance obstruction used in the handwritten lower bound. It does **not** import or trust the search program that found the certificate.

## Why this belongs here

The target was selected from the EIG factorization/parallel-composition viewpoint. A product of individually minimal witness atlases always gives a product-size witness family, but EIG specifically suggests testing whether composition permits new cross-factor witness sharing that is invisible in either factor separately. Binary rank under Kronecker product is an exact finite model of that question.

That motivation is provenance only. The proof above is ordinary finite matrix and biclique-partition mathematics and does not depend on EIG being correct.

## Literature and novelty firewall

A targeted literature check on 2026-08-31 found the integer multiplicativity problem still stated as open in, among other sources:

- Angikar Ghosal and Andreas Karrenbauer, *Engineering Insights into Biclique Partitions and Fractional Binary Ranks of Matrices*, SEA 2025, LIPIcs 338, Article 18, DOI `10.4230/LIPIcs.SEA.2025.18`;
- Michal Parnas, *Mathematical and computational perspectives on the Boolean and binary rank and their relation to the real rank*, arXiv:`2601.13900` (2026).

The SEA 2025 paper disproves multiplicativity for the **fractional** binary rank and explicitly leaves the integer binary-rank question open. The present certificate concerns the integer binary rank.

No historical-priority claim is made here until an independent specialist search has ruled out an earlier unpublished, differently phrased, or insufficiently indexed counterexample.
