# A four-row Boolean source-pair obstruction

**Status:** self-contained finite claim; no program is needed for the proof below. Historical novelty and the exact scope of the 2018 open-question wording still require an independent literature check before a priority claim.

Identify a nonzero 4-bit column with a nonempty subset of `{0,1,2,3}`; Boolean addition is union. The Boolean rank of a column family is the minimum number of generators whose unions contain every column. A **base** is a minimum generating family. In the base graph, there is an arrow `B -> C` when base `B` spans base `C`; a **source** has no incoming arrow from a distinct base.

Consider

```text
A = {3,7,15},
U = {3,5,8},
V = {3,5,12}.
```

Here `3={0,1}`, `5={0,2}`, `7={0,1,2}`, `8={3}`, `12={2,3}`, and `15={0,1,2,3}`.

## Claim

`U` and `V` are source Boolean bases of `A`; adjoining `U union V` raises Boolean rank from `3` to `4`; but for every `u in U` and `v in V`, adjoining only `u,v` leaves the rank equal to `3`.

## Proof

First, `rank_B(A)=3`. Three generators suffice, namely the columns of `A`. Two generators cannot produce the strict three-term chain

```text
{0,1} < {0,1,2} < {0,1,2,3},
```

because the nonzero unions of two generators are only `x`, `y`, and `x union y`, and these cannot contain a strict chain of length three.

Both `U` and `V` span `A`:

```text
7  = 3 union 5,
15 = 3 union 5 union 8 = 3 union 5 union 12.
```

They are sources. The edge-vectors in `V` are the three edges of the tree `1-0-2-3`. More generally, the edge-vectors of a finite forest form their unique minimum Boolean base: if `m>0` edge-vectors are omitted, spanning those omitted edges without using them forces the singleton of every incident vertex, at least `m+1` singletons, so a minimum base gets larger. Thus `V` is the unique size-3 base spanning its own columns. The same argument applies to the two-edge tree in `U`, while the isolated singleton `8={3}` is forced. Hence any size-3 base spanning `U` must equal `U`, and similarly for `V`; therefore both are sources of the base graph of `A`.

If `A | U | V` had Boolean rank `3`, some size-3 base would span both `U` and `V`. By the preceding uniqueness it would have to equal both `U` and `V`, impossible. Thus the rank is at least `4`, and the four singleton columns `{1,2,4,8}` give rank at most `4`.

Finally consider one vector from each source. Every cross pair except `{8,12}` is contained in either `U` or `V`, so that source base already spans `A` and the pair. For the remaining pair, the base

```text
{3,4,8}
```

spans `A`, `8`, and `12`, since

```text
7  = 3 union 4,
12 = 4 union 8,
15 = 3 union 4 union 8.
```

Hence every cross pair has rank `3`, whereas the full source-pair augmentation has rank `4`. QED.

## Scope note on Parnas--Shraibman Section 6

The 2018 paper asks whether the obstruction obtained from two source bases always has a one-vector-from-each-source witness. Its prose says that the base graph “has two sources,” which can be read either as **two selected sources among possibly more** or as **exactly two sources in total**. The example above settles the former formulation negatively. It has more than two total sources. For the exactly-two-total-sources formulation, the source-incidence argument in the longer dossier gives a positive answer. This wording issue must be settled against the authors' intended formulation before advertising the example as a resolution of their Section-6 problem.

Optional exhaustive checker: [`../verification/verify_source_pair_counterexamples.py`](../verification/verify_source_pair_counterexamples.py). The proof above does not depend on it.
