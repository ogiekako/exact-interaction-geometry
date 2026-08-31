# Boolean Tucker junction counterexample

**Status:** explicit finite counterexample with a solver-free checker. Historical priority is **not** asserted here; the point of this note is the mathematical statement and the EIG path that led to it.

## The EIG question

One recurring EIG question is:

> If each boundary/cut admits an independently minimal exact interface, must those minima glue through one common junction witness?

For tensors over a field, Tucker theory gives a familiar positive model: the vector of mode-unfolding ranks is the multilinear rank and is simultaneously realized by one Tucker core.

The Boolean semiring gives a clean test of the EIG question. Replace linear rank by Boolean matrix rank on each unfolding, then ask whether those individually minimal latent interfaces can be realized simultaneously by one exact Boolean Tucker core.

```text
independently minimal mode interfaces
        |
        v
try to glue them through one common Boolean core
        |
        v
local minima can be mutually incompatible
        |
        v
an explicit junction obstruction
```

## Counterexample

Let `T` be the `2 x 4 x 4` Boolean tensor whose two slices are

```text
a = 0               a = 1
0111                  1101
1101                  0111
1001                  0111
0111                  1100
```

Equivalently its 32-bit characteristic word, in bit order `16a+4b+c`, is

```text
0x3eebe9be.
```

Let

```text
beta(T) = (Boolean rank of mode-1 unfolding,
           Boolean rank of mode-2 unfolding,
           Boolean rank of mode-3 unfolding).
```

Direct exact calculation gives

```text
beta(T) = (2,3,3).
```

Nevertheless there is **no** exact Boolean Tucker decomposition of profile `(2,3,3)`.

In fact the exact feasible profile region is

\[
\operatorname{Tuck}_{\mathbb B}(T)
=\uparrow(2,3,4)\cup\uparrow(2,4,3),
\]

so it has two incomparable Pareto-minimal profiles and no componentwise least element.

## Why `(2,3,3)` fails

For the mode-2 unfolding, the minimum three-generator union basis is forced, up to latent-state permutation, to

```text
B_min = {03,06,09}
      = {{0,1},{1,2},{0,3}}.
```

For the mode-3 unfolding it is forced to

```text
C_min = {03,09,0e}
      = {{0,1},{0,3},{1,2,3}}.
```

Consider the positive entry

```text
(a,b,c) = (0,1,1).
```

The two `B` latent supports containing `b=1` are `03` and `06`; the two `C` latent supports containing `c=1` are `03` and `0e`. Hence a Boolean Tucker core entry covering this positive must choose one of four latent `B x C` pairs.

Each candidate is unsound because its Cartesian box contains a zero of the same `a=0` slice:

```text
03 x 03  hits zero (0,0,0)
03 x 0e  hits zero (0,1,2)
06 x 03  hits zero (0,2,1)
06 x 0e  hits zero (0,2,2)
```

Boolean union has no cancellation, so none of the four candidate core states may be activated. The positive `(0,1,1)` is therefore uncovered. This excludes profile `(2,3,3)`.

Profiles `(2,3,4)` and `(2,4,3)` are exact: keep one of the two rank-three factors and use literal singleton states on the other four-point mode. Together with the unfolding-rank lower bounds, this gives the displayed feasible region.

## What EIG contributed

The matrix/tensor statement above is ordinary Boolean factorization mathematics; its correctness does not depend on EIG.

The EIG contribution is the route to the question:

```text
EIG principle:
  independently minimal interfaces need not jointly descend

translation:
  minimize each Boolean unfolding separately
  then ask whether the minima share one Tucker core

failure mechanism:
  each local factorization is exact by itself,
  but its latent witnesses are not jointly compatible

finite certificate:
  one positive has only four possible latent lifts,
  and zeros block every lift.
```

This is the kind of external test the programme is intended to produce: the framework suggests a structural failure mode first, and the resulting claim is then checkable without accepting the framework.

## Structural follow-up

The research ledger contains a stronger follow-up analysis of the reduced separator problem. In the first rank-three strict-gap regime, the minimum separator bases reduce to two types, conventionally called `F` and `T`; the corresponding fiber-versus-tensor holes are completely enumerable and admit a small three-zero hook obstruction. A distributive separator semilattice is sufficient for the relevant local data to glue.

Those statements connect the example to classical semilattice flatness/distributivity, but they are not needed to verify this counterexample and are deliberately not used here as a historical-novelty claim.

## Verification

Run

```bash
python3 verification/verify_boolean_tucker_junction_counterexample.py
```

The checker uses no SAT/SMT/MIP solver, randomness, floating point, or Python `assert`. It reconstructs the tensor, derives the three mode Boolean ranks and normalized minimum bases, checks the four blocking zeros, verifies exact profiles `(2,3,4)` and `(2,4,3)`, and also checks a same-shape tensor with the same mode-rank vector `(2,3,3)` for which `(2,3,3)` *is* feasible.

## Prior-art boundary

Boolean Tucker decomposition itself is established work; see Pauli Miettinen, *Boolean Tensor Factorizations*, ICDM 2011, DOI `10.1109/ICDM.2011.28`.

The broader phenomenon that constrained Tucker decompositions can fail to possess a minimum is also not claimed here as new: nonnegative Tucker literature contains such examples, e.g. *Nonnegative canonical tensor decomposition with linear constraints: nnCANDELINC* (2022), DOI `10.1002/nla.2443`.

Likewise, the abstract equivalence between flatness and distributivity for join-semilattices is classical; see Grätzer--Wehrung, *Flat semilattices*, Colloquium Mathematicum 79 (1999), 185--191.

This repository therefore makes the deliberately narrower statement: **here is an explicit Boolean Tucker junction counterexample, here is a short exact certificate, and here is the EIG question that led to looking for it.** A specialist literature audit has not found a direct prior statement of this Boolean counterexample, but no `first` or priority claim is required for the role it plays here.
