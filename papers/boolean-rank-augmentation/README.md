# A Four-Row Counterexample to a Boolean-Rank Augmentation Question

**Keigo Oka — August 30, 2026**

## Abstract

Parnas and Shraibman asked whether, when two source bases witness failure of the augmentation property for Boolean or binary rank, one can always choose one vector from each source base so that augmenting by just those two vectors already increases the rank. We give a negative answer for **Boolean rank**.

The counterexample uses only four rows and, in fact, the same `4 x 3` matrix used in their original paper. Two explicit source bases `U,V` jointly increase the Boolean rank from `3` to `4`, while every augmentation by one vector from `U` and one vector from `V` still has Boolean rank `3`. The binary-rank version is not addressed.

## Counterexample

Interpret `z in {0,...,15}` as its four-bit column, with the least significant bit in row 1. Let

```text
A = {3,7,15},
U = {3,5,8},
V = {3,5,12}.
```

Equivalently,

```text
A = [1 1 1
     1 1 1
     0 1 1
     0 0 1].
```

Then `U,V` are distinct source bases of `A` for Boolean rank,

```text
rank_B(A)=3,
rank_B(A | U | V)=4,
```

but

```text
rank_B(A | u | v)=3
```

for every `u in U`, `v in V`.

Hence the single-vector-from-each-source question posed by Parnas--Shraibman has a negative answer for Boolean rank.

## Proof

Boolean span is closure under coordinatewise OR.

Both `U` and `V` span `A`:

```text
7  = 3 OR 5,
15 = 3 OR 5 OR 8 = 3 OR 5 OR 12.
```

The Boolean rank of `A` is 3. The three columns give an upper bound. Two generators cannot span the strict chain `3 < 7 < 15`: their nonzero OR-closure is contained in `{p,q,p OR q}`; incomparable `p,q` do not form a chain, while comparable `p,q` give at most two distinct nonzero values.

Any three generators spanning `U={3,5,8}` must contain `8`, since `8` is the only nonzero vector supported only on row 4. The remaining two generators must be exactly the incomparable vectors `3` and `5`. Thus `U` is the unique rank-3 spanning set of itself and is a source.

For `V={3,5,12}`, producing `3` requires a generator carrying row 2 without rows outside `{1,2}`; producing `12` requires a distinct generator carrying row 4 without rows outside `{3,4}`. Neither can participate in an OR equal to `5=(1,0,1,0)^T`, so the third generator is `5`. It follows in turn that the first two are exactly `3` and `12`. Hence `V` is also a source.

If `A union U union V` had rank 3, its three generators would span `U`, and hence would have to equal `U`. But `U` does not span `12`. Therefore the full augmentation has rank at least 4; the four coordinate unit vectors give rank at most 4.

Finally, if `v in {3,5}`, the base `U` handles every `u in U`. If `u in {3,5}` and `v=12`, the base `V` handles the pair. The sole remaining pair `(8,12)` is handled by

```text
W={3,4,8},
```

because `7=3 OR 4`, `12=4 OR 8`, and `15=3 OR 4 OR 8`. Thus every cross-pair augmentation has rank 3.

## Literature and provenance

The question was posed in Section 6 of:

M. Parnas and A. Shraibman, *The augmentation property of binary matrices for the binary and Boolean rank*, Linear Algebra and its Applications 556 (2018), 70--99, DOI `10.1016/j.laa.2018.07.001`.

A 2026 survey by Parnas reviews the augmentation property and its base-graph characterization: arXiv:`2601.13900`. As of August 30, 2026, we are not aware of a published resolution of the specific Section-6 question.

The example was found while experimenting with the **Interaction Reconstruction** research programme. The broader programme is not used in this proof. Discovery provenance is `ogiekako/test@3806b8ea4851f6edfa7073085e929bdd868442b9`.

The binary-rank version of the question remains outside the scope of this note.
