# Category objecthood from untyped interaction

## 0. Statement

For every small category `C`, erase its object set and all source/target labels. Keep only the raw arrow set, an absorbing failure symbol `0`, and actual composition when defined. Observe only whether a closed execution succeeds.

Then arbitrary two-sided continuation experiments recover exactly the lost ordered source/target type of every nonzero arrow. Retaining raw arrows as witness fibres over these recovered types reconstructs the original category exactly.

This is an operational recognition theorem built on classical category consolidation / semigroup ideas. Historical novelty is not claimed for the classical ingredients.

## 1. Untyped consolidation laboratory

Let `Arr(C)` be the arrows of a small category `C` and define

```text
P_C = Arr(C) disjoint-union {0}.
```

Use the convention `xy = x after y` and set

```text
xy = x o y     if dom(x)=cod(y),
xy = 0         otherwise,
0x = x0 = 0.
```

This multiplication is associative.

Define the only primitive closed response by

```text
r_C(p) = 1 iff p != 0.
```

No object, source, target, Hom-set, identity label, or type annotation is supplied to the observer.

Define two-sided contextual equivalence

```text
a ~_C b
iff
r_C(x a y) = r_C(x b y)
for every x,y in P_C.
```

## 2. Endpoint reconstruction

### Theorem 2.1

For nonzero arrows `a,b` of `C`,

```text
a ~_C b
iff
(dom(a),cod(a)) = (dom(b),cod(b)).
```

Moreover `0` is not equivalent to any nonzero arrow.

### Proof

If `a:A->B` and `b:A->B`, then for nonzero `x,y`, the triple `xay` is nonzero exactly when

```text
dom(x)=B
and
cod(y)=A.
```

These conditions depend only on `(A,B)`, so every context gives the same success/failure for `a` and `b`.

Conversely suppose `a:A->B` and `a ~_C b`. Choose

```text
x = 1_B,
y = 1_A.
```

Then `1_B a 1_A` is nonzero. Hence `1_B b 1_A` is nonzero. Left composability forces `cod(b)=B`; right composability forces `dom(b)=A`. Thus `b:A->B`.

The same context separates any nonzero `a` from `0`. QED.

### Corollary 2.2 — endpoint quotient

The contextual quotient

```text
S_C = P_C / ~_C
```

consists of `0` and one class `[A,B]` for every ordered pair with `C(A,B)` nonempty. Multiplication is

```text
[B,C] [A,B] = [A,C]
```

when the middle endpoints match and is `0` otherwise.

Because every object has an identity, the nonzero idempotents are exactly

```text
e_A = [A,A]
```

for `A in Ob(C)`.

So the original object set is recovered after contextual reduction rather than supplied before it.

## 3. Witness fibres recover the whole category

Let

```text
q : P_C -> S_C
```

be the quotient. Do **not** quotient away the raw interactions themselves. Treat them as witnesses lying over their observable endpoint class.

For recovered objects `e_A,e_B`, define

```text
W(e_A,e_B)
  = { p != 0 : q(p)=[A,B] }.
```

Equivalently, without naming `A,B`,

```text
W(e,f) = { p != 0 : q(p)= f q(p) e }.
```

### Theorem 3.1 — witness-enriched reconstruction

The structure with

```text
objects:       nonzero idempotents e_A of S_C;
arrows e_A->e_B: W(e_A,e_B);
composition:   raw multiplication in P_C;
identity:      the unique local two-sided unit in W(e_A,e_A)
```

is isomorphic to the original category `C`.

### Proof

Theorem 2.1 gives the object correspondence `A <-> e_A`. By construction,

```text
W(e_A,e_B) = C(A,B)
```

as literal sets of original raw arrows. If `p:A->B` and `q:B->C`, their product in `P_C` is exactly `q o p`; mismatched recovered boundary types multiply to `0`.

It remains to identify identities without labels. Inside `W(e_A,e_A)`, `1_A` is characterized by acting as a two-sided unit whenever a product is defined. If another `u:A->A` had this property, apply it to `1_A`: since `u 1_A=u` is nonzero, the unit law forces `u=1_A`. Thus the identity is intrinsic and unique. QED.

Hence, in this sector,

```text
untyped execution
+ continuation success
+ retained witness fibres
    -> objects, typing, Hom sets, identities, composition.
```

## 4. Continuation profiles are boundary types

Define one-sided continuation profiles

```text
L(a) = {x : xa is defined},
R(a) = {y : ay is defined}.
```

Then

```text
L(a)=L(b) iff cod(a)=cod(b),
R(a)=R(b) iff dom(a)=dom(b),
```

because identities separate endpoints. Thus `(L(a),R(a))` is exactly the recovered ordered interface pair.

This makes the basic EIG slogan literal here:

> **A boundary is the continuation profile controlling what can still be pasted on each side.**

## 5. Factorization exactness does not follow

Object/type reconstruction does not automatically give ULF, Conduche, or unique factorization.

Take the free category on

```text
f:A->B,
g:B->C,
h:A->C
```

with `h != g o f`. The endpoint quotient records a factorization

```text
[A,C] = [B,C] [A,B].
```

But the witness `h` over `[A,C]` has no factorization through `B`; the only two-step composite through `B` is `g o f`.

Therefore exact reconstruction of objects and Hom witnesses is strictly weaker than exact lifting of every quotient-level factorization.

## 6. Prior-art boundary

Classical ingredients include:

- consolidation of a category into a semigroup with zero;
- arrow-only formulations of categories;
- Karoubi/Cauchy categories of semigroups;
- restriction-semigroup/category correspondences.

The EIG contribution claimed here is not those constructions. This theorem is used as a **calibration**: a minimal operational response — composability success — has a syntactic quotient whose classes are precisely endpoint types, while prequotient witness fibres retain the full Hom data.

## 7. Verification

`verification/verify_category_reconstruction.py` exhaustively checks finite instances including all preorders on up to three labelled objects, several non-thin categories with parallel arrows, identity recovery, Hom-fibre recovery, and the explicit non-ULF example.

The computation is regression only; Sections 2--3 are the proof.
