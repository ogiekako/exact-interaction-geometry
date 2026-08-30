# Counterexamples to a source-pair augmentation question for Boolean and binary rank

**Status:** explicit finite counterexamples; mathematical claims independently rechecked by exact enumeration in this repository. Historical novelty/priority still requires the usual publication-level literature check.

## The question

Parnas and Shraibman, *The augmentation property of binary matrices for the binary and Boolean rank*, Linear Algebra and its Applications 556 (2018), Section 6, ask the following strengthening of their base-graph characterization.

Let `A` have two source bases `U,V` for the relevant rank. If augmenting by all vectors in `U union V` raises the rank, must there always exist one `u in U` and one `v in V` such that augmenting by only `u,v` already raises the rank?

The answer is **no for both Boolean rank and binary rank**.

Throughout, an integer denotes its column bitmask, with bit `2^i` equal to row `i+1`.

---

## 1. Boolean rank: a four-row counterexample

Take

```text
A = {3,7,15}
U = {3,5,8}
V = {3,5,12}.
```

Then

```text
rank_bool(A)=3,
U and V are distinct source Boolean bases of A,
rank_bool(A | U | V)=4,
rank_bool(A | u | v)=3 for every u in U, v in V.
```

### Proof

`U` spans `A` because

```text
7  = 3 OR 5,
15 = 3 OR 5 OR 8.
```

`V` spans `A` because

```text
7  = 3 OR 5,
15 = 3 OR 5 OR 12.
```

The three columns of `A` give rank at most three. Two Boolean generators have at most the three nonzero OR-values `p,q,p OR q`; if `p,q` are incomparable these values are not a chain, while if they are comparable there are at most two distinct nonzero values. Hence two generators cannot span the strict chain

```text
3 < 7 < 15,
```

so `rank_bool(A)=3`.

To span `U={3,5,8}` with three Boolean generators, the singleton fourth-row vector `8` must itself be a generator. It cannot be used to form `3` or `5`, so the remaining two generators must be exactly `3` and `5`. Thus `U` is the unique three-generator spanning set of itself. The same support argument shows that `V={3,5,12}` is the unique three-generator spanning set of itself: producing `3` requires a row-2 generator inside rows `{1,2}`, producing `12` requires a distinct row-4 generator inside rows `{3,4}`, and neither can participate in `5=(1,0,1,0)^T`; hence the three generators are exactly `3,5,12`. Therefore `U,V` are source bases.

If `A union U union V` had Boolean rank three, some Boolean base of `A` would span `U`; uniqueness forces it to be `U`, but `U` does not span `12`. Hence the rank is at least four; the four coordinate vectors give rank at most four.

Finally, if `v` is `3` or `5`, the base `U` spans `A,u,v` for every `u in U`. If `u` is `3` or `5` and `v=12`, the base `V` does. The only remaining pair is `(8,12)`, and

```text
W = {3,4,8}
```

spans `A,8,12` because

```text
7=3 OR 4,
12=4 OR 8,
15=3 OR 4 OR 8.
```

Thus every one-from-each augmentation still has Boolean rank three.

---

## 2. Binary rank: a five-row counterexample

Take

```text
A = {10,31,27,18}
U = {4,9,10,18}
V = {9,10,18,21}.
```

For binary rank, a column is spanned by an ordinary `0/1` linear combination of base columns; because the target is binary, the selected summands must have pairwise disjoint supports.

Then

```text
rank_binary(A)=4,
U and V are distinct source binary bases of A,
rank_binary(A | U | V)=5,
rank_binary(A | u | v)=4 for every u in U, v in V.
```

### Proof

The real rank of the displayed five-by-four matrix `A` is four (for example, the minor on the first four rows has determinant `-1`), so binary rank is at least four; its four columns give binary rank at most four.

`U` spans `A`:

```text
27 = 9 + 18,
31 = 4 + 9 + 18,
```

where every displayed sum is support-disjoint. Likewise `V` spans `A` because

```text
27 = 9 + 18,
31 = 10 + 21.
```

We next show that `U` is the unique four-generator binary spanning set of itself. Write supports instead of bitmasks:

```text
4  = {3},
9  = {1,4},
10 = {2,4},
18 = {2,5}.
```

To produce `{3}`, one generator must be exactly `{3}`. The other three generators must span `{1,4}`, `{2,4}`, and `{2,5}`. The first and third of these targets are disjoint. If either were split into two nonzero generators, together their two decompositions would consume all three remaining generators. The middle target `{2,4}` intersects both shores; it would then have to reuse a generator from each decomposition. But if one of the two disjoint targets were represented by a single generator, reusing it would import an unwanted coordinate (`1` or `5`), while if both were split there would be at least four generators. Hence the disjoint targets must themselves be generators, and the remaining generator is exactly `{2,4}`. Thus the four generators are `U`.

For `V`, first observe that any three generators spanning

```text
9={1,4}, 10={2,4}, 18={2,5}
```

must be exactly those three, by the same disjoint-target argument using `9` and `18`. The fourth target

```text
21={1,3,5}
```

contains row 3, whereas the first three do not. Any generator carrying row 3 is unusable in the first three targets, so they require three row-3-free generators and force `9,10,18`; none of those can participate in a disjoint sum equal to `21` because each contains an unwanted coordinate. The fourth generator is therefore exactly `21`. Thus `V` is also source.

If `A union U union V` had binary rank four, a four-vector base spanning it would in particular span `U`, hence by uniqueness would equal `U`; but `U` does not span `21`. Therefore the rank is at least five. The five coordinate unit vectors span every five-bit vector, so the rank is exactly five.

For the pairwise claim, note

```text
U intersect V = {9,10,18}.
```

If `v` lies in the intersection, `U` spans `A,u,v`; if `u` lies in the intersection, `V` spans `A,u,v`. The only remaining pair is `(4,21)`. It is handled by

```text
W = {4,10,17,18},
```

because the sums

```text
21 = 4 + 17,
27 = 10 + 17,
31 = 4 + 10 + 17
```

are support-disjoint. Hence all sixteen one-from-each augmentations have binary rank four.

---

## 3. Exact verification and minimality

Run

```bash
python3 verification/verify_source_pair_augmentation.py
python3 -O verification/verify_source_pair_augmentation.py
```

The verifier exhaustively reconstructs all optimal bases and source bases for both displayed matrices and checks every cross pair. It also exhausts all binary column sets on at most four rows and finds no binary-rank counterexample of this form. Thus the five-row binary example is row-minimal.

The verifier is integer-only and solver-free.

---

## 4. Relation to Interaction Reconstruction

The mathematical proof above is independent of the broader programme. The discovery connection is nevertheless direct: a base graph is a finite factorization atlas, and the Section-6 question asks whether incompatibility of two source interfaces must be pairwise visible. Phase V suggested searching for the opposite pattern:

```text
jointly expensive,
pairwise cheap.
```

The two examples show that source-interface incompatibility can indeed be genuinely collective.

---

## Reference

M. Parnas and A. Shraibman, **The augmentation property of binary matrices for the binary and Boolean rank**, *Linear Algebra and its Applications* 556 (2018), 70--99. DOI: `10.1016/j.laa.2018.07.001`.

As of the 2026-08-30 literature audit recorded in this repository, no prior published resolution of the specific Section-6 source-pair question was located. That statement is a search result, not a mathematical theorem; it should be refreshed immediately before submission.
