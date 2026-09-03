# Parallel continuation profiles recover object tensor, not arrow tensor

## 0. Result and scope

The preceding monoidal reconstruction theorem retained the complete arrow-level tensor table.
This note weakens that input: for each pair of arrows, retain only the success profile of the
hidden parallel output under serial continuations. In fact, after the serial category has been
reconstructed, continuations by recovered identities alone contain the entire profile.

The exact boundary is:

```text
parallel continuation profiles
    -> endpoints of every hidden tensor output
    -> tensor on objects and wire profiles;

parallel continuation profiles
    -/-> arrow-level tensor or its coherent monoidal structure.
```

An explicit pair of inequivalent PROP structures has identical serial semantics, object tensor,
and every parallel continuation profile. Thus this is a lossless-reconstruction obstruction, not
merely a counting argument.

## 1. Profile-only parallel observation

Start after the untyped serial laboratory has reconstructed a category `C` as in
`theory/02-category-reconstruction.md`. For a nonzero arrow `h`, write its two-sided success row

```text
rho_h(x,y) = 1 iff x h y != 0.
```

The endpoint theorem says

```text
rho_h = rho_k
  iff
(dom(h),cod(h)) = (dom(k),cod(k)).                     (1.1)
```

Now suppose a hidden parallel operation sends nonzero arrows `(a,b)` to a nonzero arrow, but the
arrow itself is not exposed. The observed datum is only

```text
Tau(a,b;x,y) = rho_{hidden(a,b)}(x,y).                 (1.2)
```

Equivalently, each row `Tau(a,b;-, -)` is promised to be representable by at least one retained
raw arrow. No representative of that row is selected.

## 2. Exact endpoint theorem

### Theorem 2.1 — parallel profiles recover exactly output endpoints **[PROVED / DIRECT]**

For every pair `(a,b)`, the row `Tau(a,b;-, -)` determines a unique ordered pair of recovered
objects

```text
(S_Tau(a,b), T_Tau(a,b)),
```

and determines no further arrow information: its full pointwise realization set is exactly

```text
Real_Tau(a,b)
  = C(S_Tau(a,b), T_Tau(a,b)).                        (2.1)
```

For all pairs simultaneously, before imposing functorial or monoidal coherence, the realization
set is therefore

```text
product_{a,b} C(S_Tau(a,b), T_Tau(a,b)).              (2.2)
```

Once the serial identities have been recovered, arbitrary continuations are redundant: the
ordered pair is characterized by

```text
Tau(a,b;1_T,1_S)=1
  iff
(S,T)=(S_Tau(a,b),T_Tau(a,b)).                        (2.3)
```

### Proof

Representability gives some arrow `h` with row `Tau(a,b;-, -)`. Equation (1.1) makes the source
and target of every such representative equal, proving that the ordered endpoint pair is unique.
Conversely, every arrow with those endpoints has the same success row by (1.1), so every member of
the displayed Hom set realizes the observation and no arrow outside it does. Taking the product
gives (2.2). Choosing identity contexts as in the proof of the serial endpoint theorem gives
(2.3). QED.

The product formula is a **STANDARD SET-THEORETIC FIBRE / TAUTOLOGICAL ORGANIZING LEMMA**: it is
the finite-level operation-restriction fibre principle of `EIG_CORE.md`, made literal for the
one-bit continuation language. Coherence restricts (2.2) to a smaller solution space; it is not
manufactured by the endpoint rows. The non-tautological boundary will be that even this coherent
subspace need not have a unique component.

In particular, if every Hom set occurring in (2.2) is a singleton, then a coherent realization,
if it exists, is unique as an arrow table. This thinness gate is sufficient, not necessary:
global equations can in principle select a unique coherent table from larger pointwise fibres.

## 3. Object tensor and wire profiles do survive

First suppose only that every identity-pair row has equal recovered source and target. For
recovered objects `A,B`, define

```text
A tensor_Tau B
```

to be the common source and target determined by the row `Tau(1_A,1_B;-, -)`. This table can be
tested directly for associativity, a two-sided unit, commutativity, or other object-level laws.
The row alone does **not** say that its hidden representative is the identity of that object.

### Theorem 3.1 — profile-only object-tensor reconstruction **[PROVED / DIRECT]**

If `Tau` is realizable by a strict monoidal tensor, the diagonal condition above holds, and
`tensor_Tau` is exactly its object tensor. The table is independent of the realizing arrow-level
tensor. Every strict-monoidal realization has the endpoint rule

```text
a:A->A', b:B->B'
  implies
hidden(a,b):A tensor_Tau B -> A' tensor_Tau B'.       (3.1)
```

The associativity and unit of `tensor_Tau` are consequently observable and common to every such
solution. If this recovered object monoid satisfies the rank-one hypotheses of Theorem 3.1 in
`theory/06-untyped-monoidal-profile-reconstruction.md`, its unique atom again gives canonical wire
counts and input/output profiles.

### Proof

Every realizing bifunctor sends `(1_A,1_B)` to `1_{A tensor B}`, so the identity-pair row fixes its
object product. For arbitrary arrows, a realizing bifunctor has source and target obtained by
tensoring their sources and targets; those object products are already fixed by the identity
rows, giving (3.1). Strict associativity and the unit hold in every coherent realization and are
equalities in the common recovered object table. The rank-one conclusion is exactly the cited
theorem. QED.

Without the realizability promise one can still check the diagonal condition, object laws, and
endpoint compatibility (3.1) directly from `Tau`, but those profile-level checks do not verify
identity preservation, bifunctoriality, arrow-level associativity/unit, or symmetry. Arbitrary
representable rows may admit no coherent arrow-level tensor at all.

## 4. Two inequivalent tensors with identical profiles

Let `C` have objects `N`, no morphisms between distinct objects, and

```text
End_C(0) = {0},
End_C(n) = C_2 = {0,1}  for n>0.
```

Here `0` is a genuine identity arrow, not the absorbing failure symbol of the earlier
consolidation laboratory. Composition is addition modulo `2`. Fix object tensor to be addition
in `N`.

Define two arrow tensors. When one object is `0`, both tensors use the forced unit projection.
For `m,n>0` and `f in End(m)`, `g in End(n)`, set

```text
f tensor_sum g  = f+g,
f tensor_zero g = 0.                                  (4.1)
```

### Proposition 4.1 — both operations define strict symmetric PROP structures **[PROVED]**

Both tensors in (4.1) are strictly associative and unital bifunctors with object tensor `+`.
Both admit the identity braiding. Hence each makes the same underlying category into a strict
symmetric monoidal category with objects `N`.

### Proof

On positive object pairs, `tensor_sum` is the addition homomorphism
`C_2 x C_2 -> C_2`, while `tensor_zero` is the zero homomorphism; on pairs involving `0`, the unit
projection is a homomorphism. Thus both preserve identities and composition.

Associativity of `tensor_sum` is associativity of addition. An iterated `tensor_zero` returns the
unique positive-degree input arrow if exactly one factor has positive object degree, and returns
zero if at least two factors do; this description is independent of parenthesization. If all
degrees are zero there is only the identity arrow. The unit object is `0`.

The identity arrow in `End(m+n)` is a braiding because both tensors are unchanged by exchanging
their two arguments: addition is commutative and the zero map is symmetric. Naturality, the
hexagons, and involutivity are then immediate. QED.

### Proposition 4.2 — the two PROP structures are not monoidally equivalent **[PROVED]**

Any categorical equivalence compatible with the object tensor induces an additive bijection
`N->N`, hence is the identity on objects. It is also the identity on every endomorphism group,
since `C_2` has no nonidentity automorphism.

Suppose a strong monoidal equivalence from `tensor_sum` to `tensor_zero` had tensorator
`phi_{m,n}`. Naturality at positive `m,n` would give

```text
phi_{m,n} + (f tensor_zero g)
  = (f tensor_sum g) + phi_{m,n}.
```

Taking `f=1,g=0` yields `phi_{m,n}=1+phi_{m,n}`, impossible in `C_2`. The reverse direction is
the same. QED.

### Corollary 4.3 — exact profile non-identifiability **[PROVED]**

For either tensor and every `f in End(m),g in End(n)`, the output lies in `End(m+n)`. By (1.1),
its entire two-sided success row depends only on the endpoint pair `(m+n,m+n)`. Therefore the two
inequivalent PROP structures induce exactly the same `Tau`.

The coherent solution groupoid for this profile-only problem has at least two inequivalent
components. This proves failure of lossless tensor recovery. It does not rule out a stronger
independently specified universal property selecting one tensor.

A finite two-object version replaces `(N,+)` by the idempotent object monoid `{0,e}` with
`e+e=e`, keeps `End(0)` trivial and `End(e)=C_2`, and uses the same sum/zero definitions at
`(e,e)`. One object cannot witness this distinction: the common unit and strict interchange then
give the Eckmann--Hilton collapse. The `N` version above is retained because it lies in the usual
one-colour PROP object profile.

## 5. Input/output audit

### Supplied

- the reconstructed serial category, or equivalently the untyped serial laboratory with retained
  arrows;
- for every arrow pair, its hidden parallel output's success under pairs of recovered identity
  continuations (equivalently, by (2.3), its complete two-sided success row);
- when arrow-level reconstruction is requested, the chosen class of coherent solutions whose
  fibre is to be considered.

### Forced

- the source and target of every hidden parallel output;
- a candidate object tensor whenever the identity-pair rows are diagonal;
- the candidate's object-level laws, which are directly checkable;
- the original object tensor and its unit/associativity laws when a strict-monoidal realization
  exists;
- wire profiles under the separately verified intrinsic rank-one object-monoid hypotheses.

### Not forced

- which arrow in the matching Hom set is the parallel output;
- functoriality, associativity, or coherence of an arbitrary pointwise choice;
- a unique arrow-level tensor, even after strict symmetric-monoidal coherence is required;
- a preferred solution merely because the coherent solution space is noncontractible.

### Anti-tautology verdict

Compared with `theory/06-untyped-monoidal-profile-reconstruction.md`, the arrow tensor table and
conditional interchange equations have genuinely been removed from the observation input. What
remains is exactly enough to recover tensor **profiles**, because one-bit serial continuations
classify endpoints. The pointwise product fibre itself is standard bookkeeping. The counterexample
is the sharp project-level content: even the strict symmetric-monoidal subfibre has multiple
inequivalent components, so no arrow-level tensor is hidden in those rows.

## 6. Consequence for the North Star

The profile frontier is now exact at the one-bit level:

```text
serial continuation rows are complete for boundary typing;
parallel continuation rows therefore recover boundary tensor;
arrow-level parallel composition lives in a separate coherent realization fibre.
```

This separates two beyond-Core tasks that should no longer be conflated:

1. **geometry of interfaces/profiles**, forced by exact continuation behavior under the stated
   representability/realizability hypotheses;
2. **geometry of witnesses and operations**, requiring a point in a generally noncontractible
   coherent solution space or a stronger universal property.

The next useful theorem must constrain that coherent fibre using observations richer than
success/failure, rather than treating endpoint recovery as operation recovery.
