# Symmetry quotients do not determine isotropy

## 0. Status and scope

This note sharpens the commutative-monoid test in
`theory/03-quotient-factorization-boundary.md`. Passing from words to multisets can mean at least
two different things:

```text
permutations become equalities;
permutations survive as reversible witnesses/coherences.
```

These have the same set of semantic components and inequivalent groupoidal geometry. The result
below is an elementary indistinguishability theorem, not a new construction of symmetric
monoidal groupoids.

## 1. Two symmetry semantics with the same quotient monoid

Fix a set `A`, regarded as a discrete category, and write

```text
M_A = N^(A)
```

for the free commutative monoid of finite `A`-labelled multisets.

Define two symmetric monoidal groupoids.

1. `Disc_A` is the discrete groupoid on `M_A`, with tensor given by multiset addition. Its
   symmetry maps are identities because addition is literally commutative. Every automorphism
   group is trivial.
2. `FinBij_A` has finite `A`-labelled sets `(S,lambda:S->A)` as objects and label-preserving
   bijections as morphisms, with tensor given by disjoint union. It is the free symmetric
   monoidal groupoid on `A`. If `m=sum_a n_a a`, then an object in component `m` has

   ```text
   Aut(m) ~= product_a S_{n_a}.
   ```

Taking isomorphism classes gives the same commutative monoid in both cases:

```text
pi_0(Disc_A) = M_A = pi_0(FinBij_A).
```

The distinguished degree-one generators `a in A` also agree after `pi_0`.

## 2. Isotropy non-reconstruction

### Theorem 2.1 — component semantics do not recover symmetry witnesses **[PROVED]**

If `A` is nonempty, `Disc_A` and `FinBij_A` have identical component monoids and primitive
generator classes but are not equivalent as groupoids, hence not equivalent as symmetric
monoidal groupoids.

Consequently, there is no reconstruction rule depending only on `(M_A,A->M_A)` that is equipped
with an equivalence to every symmetric monoidal groupoid having that lower component/generator
data, on any class containing both examples.

### Proof

Choose `a in A`. The object `2a` in `Disc_A` has trivial automorphism group. Every `A`-labelled
two-element set in the component `2a` of `FinBij_A` has automorphism group `S_2`, which is
nontrivial. An equivalence of groupoids preserves automorphism groups up to isomorphism, so the
two groupoids are inequivalent.

If a lower-data reconstruction rule recovered every compatible upper semantics, applying it to
the common input `(M_A,A->M_A)` would produce an object equivalent to both `Disc_A` and
`FinBij_A`, contradicting the first paragraph. QED.

There is also a concrete coherent splitting obstruction. Let

```text
p : FinBij_A -> Disc_A
```

send a labelled finite set to its count vector and every bijection to the identity of that
vector.

### Proposition 2.2 — no symmetric-monoidal section **[PROVED]**

For nonempty `A`, the functor `p` has no strong symmetric-monoidal section.

Choose `a in A`. If `s` were such a section, `S=s(a)` would be a one-element `a`-labelled set.
The braiding of `a+a` in `Disc_A` is the identity. Compatibility of a symmetric-monoidal functor
with braidings would therefore force the self-braiding of `S disjoint-union S`, conjugated along
the tensor constraint of `s`, to be the identity. But that self-braiding exchanges the two
elements and is nontrivial. This is a contradiction. QED.

Plain set/groupoid sections, and nonsymmetric ordered monoidal sections after choices of
skeleta, are not excluded. The obstruction is exactly to a section respecting the coherent
symmetry that the component quotient has collapsed.

Since `pi_0(p)` is an isomorphism but `p` is not an equivalence, this also gives an explicit
witness that `pi_0` does not reflect equivalences on symmetric monoidal groupoids.

### Proposition 2.3 — gaunt observations see only components **[PROVED]**

Call a category `C` gaunt if its only isomorphisms are identities. For every groupoid `G`, let

```text
c : G -> Disc(pi_0 G)
```

be the component projection. If `C` is gaunt, precomposition is an isomorphism of categories

```text
c^* : Fun(Disc(pi_0 G),C) -> Fun(G,C).
```

Indeed, a functor sends every invertible arrow of `G` to an isomorphism of `C`, hence to an
identity. Its object values and the components of every natural transformation are therefore
constant on connected components, giving a unique factorization through `c`. QED.

Thus a doctrine whose admitted groupoid probes take values only in gaunt targets cannot detect
isotropy at all. This is not true for arbitrary targets: for example, `Set` admits nontrivial
group actions, so `Set`-valued functors on `BG` can detect `G`.

### Exact canonicality reading

The theorem does **not** say that `M_A` admits no canonical groupoidal lift. The discrete lift is
canonical for the problem "regard all equations literally", while `FinBij_A` is canonical for
the different problem "take the free symmetric monoidal groupoid on `A`". The lower data does not
say which problem was intended and cannot reconstruct an unknown source correctly in both cases.

Equivalently, the moduli of groupoidal lifts of the fixed component data has at least these two
inequivalent points. Its noncontractibility alone would not rule out an independently specified
initial/free selector; the proved no-go concerns simultaneous recovery of the forgotten
isotropy.

This obstruction is logically independent of the cut-saturation obstruction in the preceding
note.

- For the quotient `q:A*->1`, every semantic cut-image set is already constant and equal to its
  full factorization set, but the one-point lower semantics still admits inequivalent groupoidal
  lifts such as the terminal groupoid and the one-object strict symmetric monoidal groupoid
  `B C_2` (using the abelian group law for tensor).
- The Parikh quotient has failed representative cut descent even when its semantic monoid is
  given the discrete lift with no isotropy at all.

The two results concern adjacent truncation levels: cut saturation studies factor elements in a
quotient monoid, whereas the present theorem studies automorphisms of those factorization objects
that disappear under `pi_0`.

## 3. What coherent symmetry does force when supplied

Fix `m=sum_a n_a a`. Let `FinBij_A[m]` be the full component groupoid of `A`-labelled finite sets
with count vector `m`. It is equivalent to

```text
B(product_a S_{n_a}).
```

For `r>=1`, define `Dec_r^A(m)` to be the groupoid whose objects are triples

```text
(S, lambda:S->A, p:S->[r])
```

with label count `m`, and whose morphisms are bijections preserving both `lambda` and `p`.
The map `p` is an ordered allocation of the primitive occurrences to `r` factor slots; empty
slots are allowed.

### Proposition 3.1 — coherent saturated decomposition **[PROVED / STANDARD]**

The connected components of `Dec_r^A(m)` are indexed by the semantic factorizations

```text
m = m_1 + ... + m_r
```

in `M_A`. If `k_{a,i}` is the multiplicity of label `a` in factor slot `i`, the automorphism
group of that component is

```text
product_{a,i} S_{k_{a,i}}.
```

Hence

```text
pi_0 Dec_r^A(m) = Fact_r^{M_A}(m),
```

the saturated set-valued factorization family of Theorem 2.1 in the preceding note.

### Proof

Two objects are isomorphic exactly when they have the same number `k_{a,i}` of elements with
each pair of labels `(a,i)`. The row sums are the prescribed multiplicities `n_a`; the columns
form the factor multisets `m_i`, and this is precisely an ordered factorization of `m`. A
structure-preserving automorphism independently permutes the `k_{a,i}` elements in every cell,
giving the displayed product of symmetric groups. QED.

For a fixed labelled set `(S,lambda)`, the fibre of

```text
Dec_r^A(m) -> FinBij_A[m]
```

is the discrete set of functions `S->[r]`. The automorphism group
`product_a S_{n_a}` acts by permuting occurrences, and `Dec_r^A(m)` is the corresponding action
groupoid. Thus the component set records only multiplicity allocations, while the groupoid also
retains their stabilizers.

Naming the target set in this way kills isotropy in the fibre. Its part with fixed counts
`k_{a,i}` has

```text
product_a n_a! / product_{a,i} k_{a,i}!
```

elements; summing over all count matrices gives `r^|S|`. Isotropy reappears only in the unframed
full preimage over the component `FinBij_A[m]`, obtained as the action groupoid by
`product_a S_{n_a}`.

This is a coherent **saturation** of linear cuts: any allocation can be made contiguous after
choosing a linear order on `S`. It is not literal descent of the cut set of each representative
word, which failed in the preceding note.

## 4. Why the isotropy is input, not recovered

To obtain `FinBij_A` rather than `Disc_A`, the doctrine must retain permutations as morphisms and
specify their coherence. In an adjacent-transposition presentation, the relations

```text
s_i^2 = 1,
s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1},
s_i s_j = s_j s_i  when |i-j|>1
```

are what produce the symmetric groups. A bare equality quotient of words records none of these
witnesses or relations. Other choices (free swap paths, braid relations without involutivity,
or complete proof-irrelevance) can have the same component quotient and different isotropy.

This remains true even if the entire set-level equivalence relation is retained. For the Parikh
map `q:A*->M_A`, form the thin kernel-pair groupoid with words as objects and exactly one arrow
`w->w'` when `q(w)=q(w')`. Every automorphism in this groupoid is trivial. The permutation action
groupoid

```text
coproduct_n A^n // S_n
```

has the same component set `M_A`, but the word `aa` has stabilizer `S_2`. Thus knowing which
words are equal does not determine how many identification witnesses exist or which relations
hold between them.

In particular, the one-generator case is already decisive. Its word monoid and commutative
quotient are both `N`, so there is no nontrivial equality `ab=ba` to observe. Nevertheless,
`FinBij_{a}` has automorphism group `S_n` at `n`, whereas `Disc_{a}` has none. Permutation
isotropy is therefore not encoded in the equality classes even when the primitive generator is
known.

## 5. Prior-art/framework boundary

The groupoids and homotopy-versus-orbit distinction here are standard:

- Kock, [*Data types with symmetries and polynomial functors over
  groupoids*](https://arxiv.org/abs/1210.0828), treats finite sets and bijections as the basic
  groupoid of finite cardinalities and explicitly distinguishes homotopy quotients from their
  component-set quotients.
- Baez and Dolan, [*From Finite Sets to Feynman
  Diagrams*](https://arxiv.org/abs/math/0004133), develop finite-set groupoids/species as
  categorified combinatorial data.
- Elgueta, [*The groupoid of finite sets is biinitial in the 2-category of rig
  categories*](https://arxiv.org/abs/2004.08684), explicitly records the finite-set groupoid and
  discrete natural numbers as inequivalent categorifications of the same rig.

Accordingly, the groupoid formulas are **PRIOR ART / STANDARD**. Their project-specific role is
to give the beyond-Core programme a sharp 0-truncation obstruction and an honest input ledger.
No historical novelty is claimed.

## 6. Input/output audit

### Lower input shared by the counterexamples

- the commutative monoid `M_A=N^(A)`;
- its multiplication and unit;
- the distinguished primitive generator classes `A->M_A`.

### Additional input in the coherent positive construction

- permutations retained as reversible morphisms rather than collapsed to equality;
- symmetric-group coherence, equivalently the free symmetric monoidal groupoid problem;
- label-preserving bijections as the declared equivalences.

### Outputs and non-outputs

- **not recoverable from the lower input:** automorphism groups, swap witnesses, their higher
  equalities, or whether proof-irrelevant and proof-relevant symmetry was intended;
- **forced after the stronger input is declared:** `FinBij_A`, the decomposition groupoids
  `Dec_r^A(m)`, their factorization components, and their stabilizer isotropy;
- **still not obtained:** an algebraic pattern/Segal theorem classifying all commutative-monoid
  objects in an ambient category, or a proof that observations weaker than coherent symmetry
  force that input.

### Anti-tautology verdict

Theorem 2.1 is a genuine information-loss obstruction: decategorification to the component
monoid is non-injective even after primitive classes are retained. Proposition 3.1 is a standard
unpacking of coherent symmetric-monoidal input, not recovery of coherence from equality data.

## 7. Consequence for the North Star

Replacing a set quotient by a groupoid does repair the loss only when the quotient construction
retains the actual identification witnesses and their coherence. The set-level semantic quotient
does not canonically determine that repair.

Thus the question "what survives semantic identification?" must specify at least the truncation
level of identification:

```text
equations only          -> component monoid, trivialized witnesses possible;
coherent permutations  -> symmetric isotropy and decomposition action groupoids;
unspecified witnesses  -> a nontrivial lift/reconstruction problem with no lossless inverse.
```

The sharpened quotient-first output is therefore not one geometry but a declared truncation-level
descent problem. Any theorem claiming intrinsic isotropy must derive coherent witnesses from
strictly weaker operational data or charge them as input.
