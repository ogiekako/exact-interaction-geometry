# Foundations

## 1. The interaction-first question

A conventional mathematical presentation often begins with objects and then specifies arrows, processes, states, or relations between them. EIG asks whether this order can sometimes be reversed.

The minimal experimental picture is:

1. there are interaction fragments;
2. some fragments can be executed or pasted with others;
3. closed executions produce observable responses;
4. two fragments should be identified only when every admitted future context responds identically;
5. data that remain distinguishable by future interaction must survive as witnesses;
6. interfaces, objects, maps, and larger compositional structure are reconstructed only after this exact reduction.

The key word is **sometimes**. EIG is not assuming in advance that every mathematical world satisfies such a reconstruction theorem.

## 2. Why distinguishability alone is insufficient

An equivalence relation saying which fragments are observationally indistinguishable does not determine how interactions compose.

For example, on the same carrier `{1,a}` with an injective observation, compare

```text
a^2 = 1
```

with

```text
a^2 = a.
```

The observational equivalence is equality in both cases, but the stable/idempotent interactions differ. Any objecthood theory sensitive to stable interactions therefore needs at least **execution plus response**, not a bare distinguishability relation.

## 3. Contextual exactness

Let `(P,*,1)` be a monoid of raw interaction fragments and let

```text
r : P -> O
```

be a closed-experiment response. Define two-sided contextual equivalence by

```text
a ~_r b
iff
r(x*a*y) = r(x*b*y) for every x,y in P.
```

This is a congruence: multiplying equivalent fragments on either side merely absorbs the multiplier into the quantified contexts. The quotient

```text
Syn(P,r) = P / ~_r
```

is therefore a composition-stable response quotient.

Moreover it is minimal in the expected direction: if a surjective monoid realization `h : P -> N` is sufficient to decode `r`, then `ker(h)` is contained in `~_r`, hence `N` maps onto `Syn(P,r)`.

This is classical syntactic-algebra mathematics. EIG takes it as the simplest calibration of **exact reduction by all future contexts**.

## 4. Stable interfaces are doctrine-relative

A tempting next step is to call every idempotent of `Syn(P,r)` an object. That gives the classical Karoubi/Cauchy completion:

```text
objects: e with e^2=e
arrows e -> f: m with m=f*m*e.
```

For completeness, these data really do form a category. If `m:e->f` and `n:f->g`, then

```text
n*m = g*n*f*m*e = g*(n*m)*e,
```

so composition is closed. The idempotent `e` is the identity at object `e`, because `m*e=m` and `f*m=m`; associativity is inherited from the ambient monoid. This is the standard Karoubi construction, not a new EIG theorem.

This is useful, but it is not a doctrine-free answer to objecthood.

In relations, ordinary subset interfaces correspond naturally to coreflexive idempotents `Delta_A`, not to every idempotent relation. In Hilbert or operator settings one may privilege projections, dagger idempotents, central projections, causal idempotents, or other internally characterized stable loci. Changing the admitted experiment doctrine can also change the contextual quotient itself.

EIG therefore treats objecthood as potentially **doctrine-relative**. A general theorem must either justify Cauchy saturation as its convention or derive an internal predicate such as `Sharp_D` from the doctrine's own interaction equations or tests.

## 5. Why scalar response is not enough

Two witness spans can have identical Boolean support while differing in witness multiplicity. Scalar support likewise need not retain provenance, cocycle data, or higher comparison cells.

Therefore

```text
closed response -> contextual quotient -> idempotent interfaces
```

cannot by itself be the full EIG architecture.

The intended exact principle is:

```text
global contextual collapse
        +
coherent witness retention and descent.
```

A quotient should forget exactly what no admitted future interaction can distinguish, and no more.

## 6. Exact interfaces and witness interfaces

There are already two distinct finite notions.

For a response table `M : X x Y -> K`, a deterministic exact interface is a quotient of `X` through which every response factors. The coarsest such quotient is equality of response rows.

A witness interface instead factors the response through latent witness species. Over a semiring this is matrix factorization `M=UV`. The minimal witness count depends on the doctrine: ordinary rank, Boolean rank, nonnegative rank, tropical factor rank, and related invariants need not agree.

This is why EIG does not posit a single universal scalar "interaction dimension".

## 7. Reconstruction architecture

The current field-level architecture is:

```text
CONTEXT
  -> REDUCE
  -> WITNESS
  -> COMPOSE
  -> GLUE / CODESCEND
  -> PROJECT
  -> STRUCTURE
  -> REFLECT
  -> RECONSTRUCT.
```

A useful informal reading is:

- **CONTEXT:** specify admitted continuations/experiments.
- **REDUCE:** take the coarsest exact contextual identification.
- **WITNESS:** retain multiplicity/provenance invisible to the quotient but visible to reopened boundaries.
- **COMPOSE:** define exact serial/parallel/pasting laws.
- **GLUE/CODESCEND:** prove local witness data reconstruct globally without duplication or loss.
- **PROJECT:** pass to selected shadows/invariants only after exact reconstruction.
- **STRUCTURE:** study separators, factorization, obstructions, and localization orders.
- **REFLECT:** characterize when the abstract interaction presentation comes from the intended world.
- **RECONSTRUCT:** recover objects, maps, Hom data, or process worlds up to the correct equivalence/moduli.

Not every application needs every stage.

## 8. The first strong calibration: categories

The category theorem in [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) deliberately erases all object and endpoint labels from a small category. Partial composability, encoded as success/failure in an untyped semigroup with zero, recovers endpoint types through two-sided continuation profiles; raw arrows retained as fibres then recover the original Hom sets and composition.

This shows that "objecthood downstream of interaction" is mathematically exact in at least one broad sector. It does **not** establish the general EIG theorem.

## 9. Foundational target

The open target is not "delete object symbols from category theory". That is classical. It is to identify natural interaction laboratories for which a single non-circular reconstruction principle simultaneously accounts for:

- response-minimal composition-stable semantics;
- doctrine-relative interfaces/objecthood;
- internally characterized maps;
- witness multiplicity and provenance;
- exact cross-object/cross-process Hom data;
- doctrine refinement;
- local-to-global descent and its obstructions;
- blind recovery in mathematically distant domains.

That target is formalized as WEIR in [`theory/03-weir.md`](theory/03-weir.md).
