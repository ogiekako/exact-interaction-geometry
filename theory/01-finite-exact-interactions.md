# Finite exact interactions

This note isolates the smallest exact EIG calculus.

## 1. Response tables

Let `K=(K,+,*,0,1)` be a commutative semiring and let `X,Y` be finite sets. A finite `K`-interaction is a response table

```text
M : X x Y -> K.
```

Think of `x in X` as a preparation/left state, `y in Y` as an admitted continuation/test, and `M(x,y)` as the exact closed response.

## 2. Deterministic exact interfaces

A deterministic exact interface consists of a surjection

```text
q : X -> I
```

and decoder

```text
d : I x Y -> K
```

such that

```text
M(x,y) = d(q(x),y)
```

for all `x,y`.

Define contextual equivalence

```text
x ~_M x'  iff  M(x,-)=M(x',-)
```

and let

```text
R(M) = X / ~_M.
```

### Theorem 2.1 — exact residual universal property

`pi : X -> R(M)` is the unique coarsest surjective deterministic exact interface, up to unique bijection. More precisely, every surjective exact interface `q : X -> I` factors uniquely through a map

```text
h : I -> R(M)
```

with `pi = h o q`.

### Proof

If `q(x)=q(x')`, exact decoding gives

```text
M(x,y)=d(q(x),y)=d(q(x'),y)=M(x',y)
```

for every `y`, hence `x ~_M x'`. Therefore `[x]` depends only on `q(x)`, so define

```text
h(q(x))=[x].
```

Surjectivity of `q` makes `h` unique. Conversely, `pi` itself is exact because

```text
d([x],y)=M(x,y)
```

is well-defined by the definition of `~_M`. QED.

Thus the deterministic exact boundary is not chosen: it is the quotient by indistinguishability under every admitted right continuation.

## 3. Witness interfaces

A `K`-witness interface of size `r` is a factorization

```text
M = U V,
```

with `U in K^(X x [r])` and `V in K^([r] x Y)`, equivalently

```text
M(x,y) = sum_i U(x,i) V(i,y).
```

Define

```text
rho_K(M) = minimum r admitting such a factorization.
```

This is the classical factor/Schein rank over a semiring. Its EIG interpretation is simply: `r` is the least number of latent witness species needed to mediate the exact response in doctrine `K`.

Choosing one witness for each distinct response row immediately gives

```text
rho_K(M) <= |R(M)|.
```

No novelty is claimed for factor rank itself.

## 4. Serial composition: data processing

For `M:X x Y -> K` and `N:Y x Z -> K`, define serial pasting by semiring matrix multiplication:

```text
(M odot N)(x,z) = sum_y M(x,y) N(y,z).
```

### Theorem 4.1 — witness data processing

```text
rho_K(M odot N) <= min(rho_K(M), rho_K(N)).
```

### Proof

If `M=UV`, then `MN=U(VN)`, so `rho_K(MN)<=rho_K(M)`. If `N=PQ`, then `MN=(MP)Q`, so `rho_K(MN)<=rho_K(N)`. QED.

There is also a deterministic one-sided law:

```text
|R(MN)| <= |R(M)|,
```

because equal rows remain equal after postcomposition.

Interpretation: **serial composition cannot create boundary information that was absent before the cut.**

## 5. Parallel composition

Define parallel juxtaposition by the Kronecker product

```text
(M boxtimes N)((x,x'),(y,y')) = M(x,y) N(x',y').
```

### Theorem 5.1 — parallel submultiplicativity

```text
rho_K(M boxtimes N) <= rho_K(M) rho_K(N).
```

### Proof

If `M=UV` has `r` witnesses and `N=PQ` has `s`, then

```text
M tensor N = (U tensor P)(V tensor Q),
```

which has `rs` latent witnesses. QED.

When the three ranks are finite and nonzero one may define the tensor defect

```text
kappa_K(M,N)
  = log rho_K(M) + log rho_K(N) - log rho_K(M boxtimes N)
  >= 0.
```

At this foundational stage `kappa` is only a factorization defect. Calling it curvature would require additional transformation/localization theorems.

## 6. Doctrine spectrum

The same raw response pattern can carry different witness dimensions under different doctrines. Standard calibrations include:

| doctrine | witness rank |
| --- | --- |
| field | ordinary linear rank |
| Boolean semiring | Boolean/Schein rank / rectangle-cover rank |
| nonnegative reals | nonnegative rank |
| tropical semiring | tropical factor/Barvinok-type rank |
| suitable saturated Hankel setting over a field | weighted-automaton linear dimension |

This is the first reason EIG treats geometry as **doctrine-relative** rather than postulating one universal interaction dimension.

## 7. Boundary of this note

Nothing here reconstructs witness provenance beyond a latent index, chooses a general object locus, proves local-to-global descent, or establishes the general WEIR conjecture. Those are later gates.
