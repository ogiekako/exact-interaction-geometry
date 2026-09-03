# Quotient factorization: descent, saturation, and cancellation blow-up

## 0. Status and scope

This note gives a sharp first boundary for the beyond-Core question

```text
free compositional geometry -> semantic identification.
```

The mathematics is elementary monoid theory. The factorization-lifting viewpoint is standard
(and is closely related to Conduche/ULF functors). No historical novelty is claimed. Its role here
is adversarial: even the coarse set-valued semantic-factor image of word cuts generally does
**not** descend through symmetry or cancellation quotients.

The statements below concern literal set-valued descent of semantic factor tuples. They do not
rule out a different groupoidal or homotopy-coherent geometry in which failed equalities are
replaced by specified equivalences. Such extra equivalences, isotropy, and coherence must be
charged to the input/output ledger.

## 1. Representative cuts and semantic factorizations

Let `A` be an alphabet, let `A*` be the free monoid with unit `epsilon`, and let

```text
q : A* -> M
```

be a surjective monoid homomorphism. Thus `M` is a semantic quotient of freely composable words.

For `r >= 1` and a word `w`, define the set of semantic images of its ordered `r`-block cuts by

```text
Cut_r^q(w)
  = { (q(w_1),...,q(w_r)) : w = w_1 ... w_r } subseteq M^r.
```

Empty blocks are allowed. This convention retains the unit/degeneracy cuts; excluding empty
blocks gives the analogous nonunital statement.

For `m in M`, define its full semantic `r`-factorization set

```text
Fact_r^M(m)
  = { (m_1,...,m_r) in M^r : m_1 ... m_r = m }.
```

The multiplication of `M` therefore gives `Fact_r^M(m)` directly. As `r` varies, these are the
multiplication fibres inside the ordinary bar/nerve factorization geometry of the one-object
category `BM`.

There is also a presentation-relative common core

```text
CoreCut_r^q(m) = intersection_{q(w)=m} Cut_r^q(w).
```

It retains only those semantic factor tuples visible as contiguous cuts in **every** word
representing `m`.

## 2. Saturation theorem

### Theorem 2.1 — exact quotient-factorization boundary **[PROVED]**

For every `m in M` and `r >= 1`,

```text
union_{q(w)=m} Cut_r^q(w) = Fact_r^M(m).                 (2.1)
```

Consequently:

1. `Fact_r^M` is the least representative-independent enlargement of the cut images: if
   `H(m) subseteq M^r` contains `Cut_r^q(w)` for every `w` with `q(w)=m`, then
   `Fact_r^M(m) subseteq H(m)`.
2. `CoreCut_r^q` is dually the greatest representative-independent contraction: if `L(m)` is
   contained in `Cut_r^q(w)` for every representative `w` of `m`, then
   `L(m) subseteq CoreCut_r^q(m)`.
3. Every representative satisfies the exact sandwich

   ```text
   CoreCut_r^q(q(w)) subseteq Cut_r^q(w) subseteq Fact_r^M(q(w)).
   ```

4. The following are equivalent:
   - there is a function `D_r:M -> P(M^r)` with
     `Cut_r^q(w)=D_r(q(w))` for every word `w`;
   - `Cut_r^q` is constant on every fibre of `q`;
   - `Cut_r^q(w)=Fact_r^M(q(w))` for every word `w`;
   - `CoreCut_r^q(m)=Fact_r^M(m)` for every `m`;
   - for every word `w` and every semantic factorization
     `q(w)=m_1...m_r`, there is a cut `w=w_1...w_r` with `q(w_i)=m_i`.

Thus representative cut images descend literally exactly when **every representative** lifts
every semantic factorization of its value. When this fails, full semantic factorization is not
the descended value of the representative geometry; it is its forced saturation.

### Proof

Every tuple in `Cut_r^q(w)` multiplies to `q(w)`, so the left side of (2.1) is contained in the
right side. Conversely, take `(m_1,...,m_r)` with product `m`. Surjectivity gives words `w_i` with
`q(w_i)=m_i`. For `w=w_1...w_r`, one has `q(w)=m` and the displayed tuple belongs to
`Cut_r^q(w)`. This proves (2.1).

The two universal properties follow by taking the union and intersection, and the sandwich is
immediate. Literal descent is equivalent to fibre-constancy. If the cut image is constant on
`q^{-1}(m)`, its common value equals its union, which is `Fact_r^M(m)` by (2.1). Conversely,
equality with `Fact_r^M(q(w))` makes the value depend only on `q(w)`. Equality of the intersection
and union is equivalent to every member of the nonempty family being equal; the fibre is nonempty
because `q` is surjective. The last condition simply spells out equality with `Fact`. QED.

### Remark 2.2 — relation to ULF

The theorem forgets which cut produced a tuple and retains only its semantic image. If actual cut
positions or factorization witnesses must descend to `Fact_r^M(q(w))`, the relevant map is

```text
{ (w_1,...,w_r) : w=w_1...w_r } -> Fact_r^M(q(w)).
```

Surjectivity is the lifting condition in Theorem 2.1; bijectivity is unique lifting of
factorizations. For all binary factorizations this is the usual ULF condition on the functor
`BA* -> BM`. Hence retaining provenance imposes a strictly stronger, classical exactness gate.

## 3. Symmetry already prevents literal descent

Let `A={a,b}` and let

```text
q : {a,b}* -> N^2
```

be the Parikh map to the free commutative monoid, written additively. For `m=a+b`,

```text
Cut_2^q(ab) = { (0,m), (a,b), (m,0) },
Cut_2^q(ba) = { (0,m), (b,a), (m,0) }.
```

The words have the same semantic value but different ordered cut images. So the path-cut
geometry does not descend through the basic commutativity quotient.

Merely quotienting the two factor slots by their transposition does not fix the problem globally.
For the equal representatives `aab` and `aba` of `2a+b`, the unordered cut image of `aab`
contains the factor-pair orbit `{2a,b}`, whereas that of `aba` does not. Thus even the set of
unordered contiguous bipartitions is representative-dependent.

The canonical saturation is nevertheless finite and explicit. If

```text
m = sum_a n_a a
```

has finite support in the free commutative monoid, an ordered semantic `r`-factorization amounts
to choosing, independently for every `a`, a weak composition of `n_a` into `r` parts. Therefore

```text
|Fact_r^M(m)| = product_a binomial(n_a+r-1, r-1).
```

This saturated geometry consists of allocations of primitive multiplicities among factor slots,
not cuts of any one linear representative.

### Proposition 3.1 — no relabelling-invariant ordering **[PROVED]**

If `A` has at least two elements, the Parikh quotient

```text
q : A* -> N^(A)
```

has no section `s` that is equivariant under all permutations of `A` (even as a map of sets).

Indeed, choose distinct `a,b`. The transposition exchanging them fixes the multiset `a+b`, while
its fibre under `q` is `{ab,ba}` and the transposition exchanges these two words. An equivariant
section would have to choose a fixed point in this fibre, but none exists. QED.

Thus an ordered representative can be selected only by breaking the declared relabelling
symmetry. This is a specified invariant-solution obstruction, not merely an assertion that one
ordering feels less natural than another.

## 4. Cancellation can force finite-to-infinite blow-up

Let `A={x,xbar}` and map the free monoid onto the infinite cyclic group, written additively,

```text
q(x)=1,   q(xbar)=-1,   M=Z.
```

Then `epsilon` and `x xbar` both represent `0`, but

```text
Cut_2^q(epsilon) = { (0,0) },
Cut_2^q(x xbar)  = { (0,0), (1,-1) }.
```

Hence binary cut images do not descend. More strongly,

```text
Fact_2^Z(0) = { (n,-n) : n in Z }.
```

Every representative word has only finitely many cuts, while the least
representative-independent saturated factorization set of its semantic value is infinite.
Cancellation therefore does not merely identify two finite path geometries: it can force any
literal invariant enlargement containing all representatives to acquire infinitely many
semantic excursions.

The surjectivity hypothesis is an important input charge here. Formal inverse letters were put in
the raw alphabet, so `q:{x,xbar}*->Z` is onto. The literal group-completion map from the positive
free monoid `{x}*` to `Z` is not arrow-surjective: negative semantic factors have no positive word
lifts, and equation (2.1) would be false. Adjoining inverse interactions and then imposing
cancellation is not the same operation as taking a quotient of the original positive interaction
language.

The same example also separates length from semantics. In general, word length factors as

```text
A* -q-> M -ell-> N
```

if and only if the quotient congruence is homogeneous
(`q(u)=q(v)` implies `|u|=|v|`); when it exists, `ell` is unique. The commutativity quotient is
homogeneous, but Section 3 shows that length preservation is still insufficient for cut descent.
Inverse cancellation is not homogeneous because `epsilon` and `x xbar` have different lengths.

### Proposition 4.1 — additive arity collapses on groups **[PROVED]**

Every monoid homomorphism from a group `G` to `(N,+)` is zero. Indeed,

```text
ell(g) + ell(g^{-1}) = ell(1) = 0,
```

so both nonnegative summands vanish. Therefore no nontrivial additive natural-number length or
arity grading survives from an abstract group alone. The same argument applies to a functor from
a groupoid to the one-object category `(N,+)`: every invertible arrow must map to the sole
invertible element `0`.

### Proposition 4.2 — finite geodesic cuts are presentation-relative **[PROVED]**

If a free group `F(A)` is supplied together with its free basis `A`, every element `g` has a unique
reduced word. Define `GeoFact_r^A(g)` to consist of the semantic tuples obtained by cutting that
reduced word into `r` contiguous blocks. Equivalently, these are the factorizations with no
cross-boundary cancellation. If the reduced length of `g` is `L`, then

```text
|GeoFact_r^A(g)| = binomial(L+r-1, r-1).
```

This follows because cuts are exactly weak compositions of `L` into `r` block lengths, and
uniqueness of reduced words makes distinct cuts give distinct factor tuples.

This finite geometry is canonical only relative to the basis/presentation. For example, the free
group `F(a,b)` has bases `{a,b}` and `{a,c}` with `c=ab`. The element `b` has reduced length `1`
in the first basis and `2` in the second because `b=a^{-1}c`. Hence the abstract quotient group
does not recover this geodesic cut geometry.

## 5. Input/output audit

### Supplied input

- the primitive alphabet `A`;
- free serial composition `A*`, whose words have canonical linear cuts;
- the entire semantic congruence, equivalently the quotient map `q:A*->M`;
- multiplication and unit in `M`.

In the cancellation example, the primitive alphabet also includes formal inverse letters. If
only positive generators are supplied, group completion adds interactions and is not covered by
the surjective-quotient theorem without enlarging the raw language.

### Requested or obtained output

- **requested and generally disproved:** a literal representative-independent set of semantic
  cut tuples;
- **always obtained:** the least invariant saturation `Fact_r^M(m)`;
- **also always definable from the presentation:** the greatest common contraction
  `CoreCut_r^q(m)`;
- **not obtained:** a uniquely forced groupoidal/higher replacement, a Segal recognition theorem,
  or recovery of the quotient equations from weaker observations.
- **available only with extra presentation data:** finite reduced-word/geodesic geometry for a
  chosen free-group basis.

### Anti-tautology verdict

The negative boundary is genuine: Theorem 2.1 gives an exact factorization-lifting test, and the
two quotient examples fail it for different reasons despite the commutative example preserving
length.

The positive saturation should **not** be advertised as a new EIG extractor. Once the quotient
monoid multiplication has been supplied, `Fact_r^M(m)` is standard bar/nerve factorization data.
The theorem identifies it as the forced least enlargement of representative cuts; it does not
derive multiplication, arities, active/inert structure, coverage, or recognition from smaller
input. The common contraction is a second canonical construction but depends on the chosen free
presentation and deliberately discards every cut absent from even one representative. Without an
independently specified preservation requirement, `CoreCut` and `Fact` demonstrate that
"canonical shadow" is not yet one well-posed output problem.

## 6. Prior-art/framework boundary

The positive constructions in this note sit inside established categorical machinery:

- Gálvez-Carrillo, Kock, and Tonks, [*Decomposition Spaces, Incidence Algebras and Möbius
  Inversion*](https://arxiv.org/abs/1404.3202), develop decomposition spaces and conservative ULF
  maps; the witness-sensitive pullback/bijectivity gate above is part of that standard
  factorization-exactness world.
- Berger, Melliès, and Weber, [*Monads with arities and their associated
  theories*](https://arxiv.org/abs/1101.3064), give arities for the free-groupoid monad and recover
  the symmetric simplicial nerve characterization of groupoids.
- Bourke and Garner, [*Monads and theories*](https://arxiv.org/abs/1805.04346), characterize the
  monads for which a fixed arity nerve theorem holds; Chu and Haugseng,
  [*Homotopy-coherent algebra via Segal conditions*](https://arxiv.org/abs/1907.03977), relate
  polynomial monads and extendable algebraic patterns.

These results are not consequences of Theorem 2.1, but they delimit its interpretation. The
ordinary nerve of the particular quotient object `BM` is not an extracted pattern whose Segal
objects recognize all algebras of a quotient doctrine. Obtaining that stronger bridge still
requires arity/nervousness, polynomiality, algebraic-pattern, or comparable hypotheses.

## 7. Consequence for the beyond-Core programme

The naive point-valued pipeline

```text
free word/path geometry -> quotient -> the same descended path geometry
```

is false already for commutativity and cancellation. Three routes remain logically open:

1. impose the factorization-lifting condition (and ULF when provenance is required);
2. replace representative geometry by the canonical saturated semantic factorization family,
   accepting that cancellation may make finite geometry infinite;
3. supply and justify a groupoidal/higher quotient geometry whose isotropy and coherence record
   the identifications.

The first is a restrictive classical exactness hypothesis, the second is standard structure
already determined by the quotient multiplication, and the third requires additional mathematics
and an explicit input charge. Therefore the result supports a sharpened quotient-first posture:
semantic identification canonically yields a **descent test and extremal lossy/completive
shadows**, but does not by itself force a unique richer compositional geometry.
