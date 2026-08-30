# Exact extension complexity of the four-variable correlation polytope

**Mathematical status:** explicit exact finite certificate, independently replayed in this curation.  
**Historical novelty:** **UNVERIFIED / specialist literature audit pending.**  
**Programme dependency:** none; Interaction Reconstruction is discovery provenance only.

## Theorem

Let

```text
COR(4) = conv{ (x_i, x_i x_j)_(1<=i<j<=4) : x in {0,1}^4 } subset R^10.
```

Then

```text
xc(COR(4)) = 16.
```

The upper bound is immediate: `COR(4)` has sixteen vertices, so it is an affine image of the 15-simplex, which has sixteen facets.

The lower bound is certified by sixteen genuine facets and sixteen positive slack entries forming a fooling set. A rank-one nonnegative rectangle contains at most one fooling-set entry, hence every rectangle cover of the slack support has size at least sixteen. By Yannakakis' factorization theorem,

```text
16 <= rectangle_cover(S) <= rank_+(S) = xc(COR(4)).
```

## Coordinates

Use

```text
x0,x1,x2,x3,x01,x02,x03,x12,x13,x23,1
```

and index the sixteen correlation vertices by integers `0,...,15` (bit `i` is `x_i`). Each pair below gives the designated positive-slack vertex and the eleven integer coefficients of an affine slack form `a.z >= 0`:

```text
v=12 : ( 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
v=10 : ( 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
v= 8 : (-1,-1,-1, 2, 1, 1,-1, 1,-1,-1, 1)
v=15 : (-1,-1,-1,-1, 1, 1, 1, 1, 1, 1, 1)
v= 9 : ( 0, 1, 0, 0,-1, 0, 1, 0,-1, 0, 0)
v= 1 : ( 1, 0, 0, 0, 0,-1, 0, 0, 0, 0, 0)
v= 6 : ( 1, 0, 0, 0,-1,-1,-1, 1, 1, 1, 0)
v=14 : ( 2,-1,-1,-1,-1,-1,-1, 1, 1, 1, 1)
v=11 : ( 0, 0, 1, 0, 1,-1, 0,-1, 0, 0, 0)
v= 3 : ( 0, 0, 0, 1, 1, 0,-1, 0,-1, 0, 0)
v=13 : ( 1, 0, 1, 0,-1, 1,-1,-1, 1,-1, 0)
v= 2 : ( 0, 1, 0, 0, 0, 0, 0, 0,-1, 0, 0)
v= 0 : (-1,-1, 2,-1, 1,-1, 1,-1, 1,-1, 1)
v= 4 : ( 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0)
v= 5 : ( 0, 0, 1, 0, 0, 0, 0,-1, 1,-1, 0)
v= 7 : ( 0, 0, 1, 0, 0, 0, 0, 0, 0,-1, 0)
```

## What the verifier checks

`verification/verify_cor4_extension_complexity.py` uses exact rational arithmetic and checks:

1. `dim(COR(4))=10`;
2. every displayed affine form is nonnegative on all sixteen vertices;
3. the zero vertices of every form affinely span dimension nine, hence each form is a facet inequality;
4. each designated diagonal vertex has strictly positive slack;
5. all sixteen designated vertices are distinct;
6. for each of the 120 unordered pairs, at least one cross slack is zero.

Thus the sixteen positive entries are an exact fooling set.

Run:

```bash
python3 verification/verify_cor4_extension_complexity.py
python3 -O verification/verify_cor4_extension_complexity.py
```

The curation independently replayed the certificate in normal mode, optimized mode, and bytecode compilation; all 186 explicit checks passed.

## Literature boundary

Known relevant prior art includes:

- Kaibel--Weltge, *A Short Proof that the Extension Complexity of the Correlation Polytope Grows Exponentially* (arXiv:1307.3543), proving an exponential lower bound;
- Aboulker--Fiorini--Huynh--Macchia--Seif, *Extension complexity of the correlation polytope*, Operations Research Letters 47 (2019), giving graph/treewidth upper and lower bounds;
- classical complete facet descriptions of `CUTP_5`, affinely equivalent to `COR(4)`.

A targeted search on 2026-08-30 did **not** surface a paper explicitly stating `xc(COR(4))=16` or this sixteen-entry fooling set. This is not a priority proof. Because the `CUTP_5` incidence structure is classical, the consequence could be folklore or implicit in older tables.

Correct publication posture:

```text
mathematics: exact finite certificate replayed;
historical novelty: specialist audit pending;
priority claim: do not make yet.
```

## Provenance

Source research-ledger commit:

```text
ogiekako/test@c25815e82faba9beb8b9deb96d740ee345138872
```

Source files:

```text
docs/COR4_EXACT_EXTENSION_COMPLEXITY_16_20260830.md
verification/verify_cor4_extension_complexity_16_20260830.py
```
