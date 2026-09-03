# Untyped monoidal interaction recovers profiles, not symmetry

## 0. Result and scope

The category reconstruction theorem in `theory/02-category-reconstruction.md` recovers objects
and endpoint types from untyped serial execution plus one-bit success. This note adds a retained
parallel operation and proves the exact next step:

```text
untyped serial execution + success + retained arrows + raw parallel operation
    -> strict monoidal category + intrinsic object monoid;

free rank-one object monoid
    -> canonical wire counts and input/output profiles.
```

The designated symmetry/braiding is not generically recoverable from this data, even when every
arrow and all isotropy are retained. Thus profile recovery is strictly weaker than PROP recovery.

This is a recognition/calibration theorem using standard category-consolidation ideas. Historical
novelty is not claimed.

## 1. Untyped serial-parallel laboratory

Begin with the consolidation laboratory of a small category: a set

```text
P = raw arrows disjoint-union {0},
```

an associative totalized serial product `xy` with absorbing failure `0`, and response

```text
r(p)=1 iff p != 0.
```

Two-sided serial continuation profiles give contextual equivalence. Assume that the hypotheses
of Theorem 3.1 in `theory/02-category-reconstruction.md` hold, so the quotient and retained raw
witnesses reconstruct a category `C`. Write `1_A` for the recovered identity at recovered object
`A`.

Now retain a second raw operation

```text
boxtimes : P x P -> P.
```

The value `0` is absorbing. On nonzero arrows impose the following checkable conditions.

1. **Nonzero preservation:** `a boxtimes b != 0` for nonzero `a,b`.
2. **Strict raw monoid:** `boxtimes` is associative and has a unique nonzero unit `iota`.
3. **Identity preservation:** `iota` is a recovered category identity, and
   `1_A boxtimes 1_B` is a recovered category identity for every recovered `A,B`.
4. **Conditional interchange:** whenever both coordinate composites `a_2 a_1` and `b_2 b_1`
   are nonzero,

   ```text
   (a_2 boxtimes b_2)(a_1 boxtimes b_1)
     = (a_2 a_1) boxtimes (b_2 b_1).                  (1.1)
   ```

Condition 4 is deliberately conditional. Unconditional interchange for the zero-totalized
serial product is false in ordinary monoidal categories: tensor endpoints can match in aggregate
even when the two coordinate pairs do not compose.

For an explicit witness, take the discrete strict monoidal category on the object monoid
`{I,A}` with `A tensor A=A`. In its consolidation set, put

```text
x=1_I,  y=1_A,  x'=y'=1_A.
```

Then `xy=0`, but

```text
(x boxtimes x')(y boxtimes y') = 1_A,
(xy) boxtimes (x'y')           = 0.
```

Thus unconditional interchange would add a componentwise composability-reflection property not
present in general monoidal interaction.

## 2. Strict monoidal reconstruction

### Theorem 2.1 — untyped strict-monoidal recognition **[PROVED / DIRECT RECOGNITION]**

The data and conditions of Section 1 determine a strict monoidal structure on the reconstructed
category `C`, without supplying its object set or source/target maps in advance.

For recovered objects define

```text
1_{A tensor B} := 1_A boxtimes 1_B,
1_I            := iota.                               (2.1)
```

On arrows use the retained raw operation `boxtimes`. Then:

- `A tensor B` and `I` are well-defined recovered objects;
- if `a:A->A'` and `b:B->B'`, then
  `a boxtimes b:A tensor B -> A' tensor B'`;
- `boxtimes` is a bifunctor;
- the object and arrow tensors are strictly associative and strictly unital.

Consequently the reconstructed strict monoidal category is isomorphic to any original strict
monoidal category from which this untyped laboratory was obtained.

### Proof

Identity preservation makes (2.1) meaningful: recovered objects are in bijection with their
unique recovered identity arrows.

For `a:A->A'` and `b:B->B'`, conditional interchange with local identities gives

```text
(1_A' boxtimes 1_B')(a boxtimes b) = a boxtimes b,
(a boxtimes b)(1_A boxtimes 1_B)   = a boxtimes b.
```

The endpoint reconstruction theorem says exactly that `a boxtimes b` therefore has source
`A tensor B` and target `A' tensor B'`. Equation (1.1) is now the bifunctor law on every
well-typed composable pair.

Raw associativity gives equality of identity arrows

```text
(1_A boxtimes 1_B) boxtimes 1_C
  = 1_A boxtimes (1_B boxtimes 1_C),
```

hence equality of the recovered objects `(A tensor B) tensor C` and
`A tensor (B tensor C)`. The raw unit law similarly gives `I tensor A=A=A tensor I` and the
corresponding arrow laws. Thus all strict monoidal axioms hold. The construction uses the original
raw arrows and operations literally, so the resulting structure is isomorphic to the source
strict monoidal category when one existed. QED.

### Corollary 2.2 — contextual classes are tensor-compatible **[PROVED / DIRECT]**

The endpoint quotient is compatible with `boxtimes`: arrows with equal recovered endpoints have
tensors with equal recovered endpoints. Thus the raw parallel operation induces the object-pair
rule

```text
[A,A'] boxtimes [B,B'] = [A tensor B, A' tensor B'].
```

This is a consequence of the recovered typing, not an extra congruence assumption on the
zero-totalized serial semigroup.

## 3. Intrinsic wire-count recovery

Let `O` be the recovered object monoid. Call it conical if

```text
A tensor B = I  implies  A=I=B,
```

and cancellative if tensor cancellation holds on both sides. An atom is a nonunit `g` such that
`g=A tensor B` forces `A=I` or `B=I`.

### Theorem 3.1 — rank-one profile recognition **[PROVED / ELEMENTARY]**

Suppose `O` is commutative, conical, cancellative, generated by its atoms, and has exactly one
atom `g`. Then

```text
n |-> g^(tensor n) : (N,+,0) -> (O,tensor,I)
```

is the unique monoid isomorphism sending `1` to the intrinsic atom `g`.

Hence every arrow acquires a canonical profile

```text
a : m -> n
```

by applying the inverse isomorphism to its recovered source and target. In particular, the
wire-count grading of a standard one-colour PROP is recovered rather than supplied as an object
label.

### Proof

Because the atoms generate and `g` is the only atom, every object is a tensor power of `g`, so
the displayed map is surjective. If `g^m=g^n` with `m<n`, cancellation gives
`I=g^(n-m)`. Conicality then forces `g=I`, contradicting that `g` is an atom. Thus the map is
injective. The generator image fixes every monoid homomorphism out of `N`, proving uniqueness.
QED.

The hypotheses matter. A unique atom alone neither says that it generates every object nor
prevents relations among its powers. The theorem charges the exact freeness content to the
recovered object monoid instead of inferring `N` from the word "PROP".

## 4. Symmetry remains extra structure

The recovered tensor need not determine a designated braiding. The following example lies
inside the object/profile format of a PROP.

Let `K` be the strict monoidal groupoid with objects `N`, no morphisms between distinct objects,
and

```text
End_K(n) = C_2 = {0,1}.
```

Composition is addition modulo `2`, object tensor is addition in `N`, and arrow tensor is
addition modulo `2`. Interchange holds because `C_2` is abelian.

For `c in C_2`, define

```text
beta^c_{m,n} = c m n mod 2  in End_K(m+n).             (4.1)
```

### Theorem 4.1 — one underlying PRO admits inequivalent PROP structures **[PROVED / DIRECT]**

The choices `c=0` and `c=1` in (4.1) define symmetric braidings on the same underlying strict
monoidal category. The resulting symmetric monoidal categories are not symmetrically monoidally
equivalent.

### Proof

Naturality is automatic from commutativity of the endomorphism groups. The two strict hexagon
identities say that `beta` is additive in each object variable, which (4.1) satisfies. The unit
conditions follow from `beta^c_{0,n}=beta^c_{m,0}=0`, and symmetry is

```text
beta^c_{m,n} + beta^c_{n,m} = 2 c m n = 0  in C_2.
```

For inequivalence, any underlying categorical equivalence compatible with tensor induces an
additive bijection `N->N`, hence is the identity on objects. Every automorphism of the group
`C_2` is also the identity, so it is the identity on morphisms. A strong monoidal functor may
still have a tensor constraint `phi_{m,n} in C_2`, but the braided-functor square at `(m,n)=(1,1)`
uses the same `phi_{1,1}` on both sides. It would force

```text
beta^0_{1,1} = beta^1_{1,1},
```

i.e. `0=1`, a contradiction. QED.

Thus the complete untyped serial-parallel laboratory—including all raw arrows and their
isotropy—is identical for the two symmetric structures. What was forgotten is which coherent
family of existing arrows is designated as the braiding.

This is a no-go for **lossless recovery of an unknown supplied symmetry**, not for every canonical
choice. In this example `beta^0` is itself a canonical identity braiding. As in the earlier
canonicality results, an independently specified universal property may select a point even when
the forgetful fibre contains inequivalent structures.

## 5. Input/output ledger

### Supplied

- the raw arrow/witness set and absorbing failure;
- totalized serial execution and its success/failure response;
- the raw parallel operation, its unit, associativity, identity preservation, and conditional
  interchange behavior;
- exact equality of retained raw arrows.

### Genuinely recovered

- objects, source/target profiles, Hom fibres, identities, and serial composition, as in the
  category reconstruction theorem;
- tensor on objects and its unit;
- typed bifunctoriality of the retained raw tensor;
- wire counts when the recovered object monoid satisfies the exact intrinsic rank-one
  hypotheses of Theorem 3.1.

### Not recovered

- serial composition or parallel composition themselves: both are supplied as raw execution;
- a designated symmetry/braiding or its coherence;
- proof that an arbitrary recovered object monoid is free commutative of rank one;
- graphical arities, a PROP nerve/Segal recognition theorem, or reconstruction from scalar
  responses after raw arrow witnesses are discarded.

### Anti-tautology verdict

The profile theorem is nontrivial but narrow: typing and wire labels are not inputs, yet serial
success encodes composability and the parallel operation is fully supplied. The theorem recovers
the typed strict-monoidal organization of those operations. It does not derive tensor or
interchange from weaker observations.

The symmetry counterexample is stronger than the preceding `pi_0` obstruction: even retaining the
full monoidal groupoid and all isotropy does not specify how existing arrows assemble into a
braiding. Coherent symmetry is structure, not a property, unless an additional uniqueness theorem
is proved in the chosen class.

## 6. Prior-art/framework boundary

The categorical shell is established object-free/consolidation mathematics. Cranch, Doherty, and
Struth, [*Relational Semigroups and Object-Free
Categories*](https://arxiv.org/abs/2001.11895), compare partial-semigroup, multiple-unit, and
source/target presentations and discuss adjoining zero. Kostin and Novikov,
[*On categorical semigroups*](https://arxiv.org/abs/1312.1511), study semigroups that are
categorical at zero. The base category reconstruction is already separated from these classical
ingredients in `theory/02-category-reconstruction.md`.

Pirashvili, [*On the PROP corresponding to
bialgebras*](https://arxiv.org/abs/math/0110014), uses the standard PROP convention with objects
`N` and tensor addition. Hackney and Robertson,
[*On the category of props*](https://arxiv.org/abs/1207.2773), develop colored props and free prop
constructions.

Accordingly, Theorems 2.1 and 3.1 are **DIRECT / ELEMENTARY calibrations**, not a novelty claim
for object-free categories, strict monoidal categories, PROPs, or atomic commutative monoids. The
project-specific point is the audited operational boundary: serial success recovers hidden
profiles, while the arrow tensor and its laws remain supplied.

## 7. Consequence for the beyond-Core programme

The profile/typing question has a conditional positive answer:

```text
serial continuation success recovers endpoints;
raw parallel interaction transports to recovered endpoints;
intrinsic rank-one object algebra recovers wire count.
```

The semantic wall moves one step downstream. For PROP-like systems, the next irreducible datum is
not necessarily the wire profile: it is the coherent selection of permutation/interchange
witnesses and, beyond that, the arity/recognition structure. A stronger EIG theorem must either
derive those witnesses from observations capable of distinguishing them or explicitly retain
them as doctrine input.
