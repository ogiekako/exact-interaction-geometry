# Foundations

## 1. The interaction-first question

A conventional mathematical presentation often begins with objects and then specifies arrows, processes, states, or relations between them. EIG asks whether this order can sometimes be reversed.

The minimal operational picture is:

1. there are interaction fragments;
2. some fragments can be executed or pasted with others;
3. a declared class of continuations/closed experiments produces observable responses;
4. two fragments should be identified only when every admitted future context responds identically;
5. data that remain distinguishable by reopened interaction must survive as witnesses;
6. interfaces, objects, maps, and larger compositional structure are reconstructed only when the declared doctrine actually identifies them.

The key word is **sometimes**. EIG is not assuming in advance that every mathematical or physical world satisfies such a reconstruction theorem.

It is also not assuming that “interaction itself” means bare scalar data. The execution/pasting law and the admitted experiment doctrine are primitive unless a separate theorem reconstructs them.

## 2. The identifiability boundary

The sharp EIG output is not always a target object. In general one should seek

```text
operational doctrine
  -> maximal identifiable invariant
  + residual indistinguishability fibre/moduli
  + the extra resource needed to reduce that fibre.
```

A positive reconstruction theorem is one endpoint. An exact no-go theorem can be equally complete if it proves that several targets remain operationally indistinguishable and identifies the largest invariant that survives.

This separates two questions that are often conflated:

```text
identifiability: which distinctions can the doctrine detect?
selection:       does it canonically choose one representative among the compatible possibilities?
```

More observational power may improve the first without solving the second.

## 3. Why distinguishability alone is insufficient

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

## 4. Contextual exactness

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

Moreover it is minimal in the expected direction: if a surjective monoid realization `h : P -> N` is sufficient to decode `r`, then `ker(h)` is contained in `~_r`. Equivalently, the canonical contextual quotient factors through every such exact realization.

This is classical syntactic-algebra mathematics. EIG takes it as the simplest calibration of **exact reduction by all future contexts**.

## 5. Stable interfaces are doctrine-relative

A tempting next step is to call every idempotent of `Syn(P,r)` an object. That gives the classical Karoubi/Cauchy completion:

```text
objects: e with e^2=e
arrows e -> f: m with m=f*m*e.
```

These data form a category by the standard Karoubi construction. This is useful, but it is not a doctrine-free answer to objecthood.

In relations, ordinary subset interfaces correspond naturally to coreflexive idempotents `Delta_A`, not to every idempotent relation. In Hilbert or operator settings one may privilege projections, dagger idempotents, central projections, causal idempotents, or other internally characterized stable loci. Changing the admitted experiment doctrine can also change the contextual quotient itself.

EIG therefore treats objecthood as potentially **doctrine-relative**. A general theorem must either justify Cauchy saturation as its convention or derive an internal predicate such as `Sharp_D` from the doctrine's own equations or tests.

## 6. Why scalar response is not enough

Two witness spans can have identical Boolean support while differing in witness multiplicity. Scalar support likewise need not retain provenance, cocycle data, phase information, or higher comparison cells.

Therefore

```text
closed response -> contextual quotient -> idempotent interfaces
```

cannot by itself be the full EIG architecture.

The intended exact principle is

```text
global contextual collapse
        +
coherent witness retention and descent.
```

A quotient should forget exactly what no admitted future interaction can distinguish, and no more.

## 7. Exact interfaces and witness interfaces

For a response table `M : X x Y -> K`, a deterministic exact interface is a quotient of `X` through which every response factors. The coarsest such quotient is equality of response rows.

If `pi : X -> R(M)` is that canonical quotient and `q : X -> I` is any surjective exact interface, then

```text
pi = h o q
```

for a unique `h : I -> R(M)`. Thus the canonical residual interface factors through every exact interface; it is the least informative exact deterministic boundary.

A witness interface instead factors the response through latent witness species. Over a semiring this is matrix factorization `M=UV`. The minimal witness count depends on the doctrine: ordinary rank, Boolean rank, nonnegative rank, tropical factor rank, and related invariants need not agree.

This is why EIG does not posit a single universal scalar “interaction dimension.”

## 8. Reconstruction architecture

The older linear architecture

```text
CONTEXT -> REDUCE -> WITNESS -> COMPOSE -> GLUE -> PROJECT -> STRUCTURE -> REFLECT -> RECONSTRUCT
```

is still useful, but the boundary-first form is more accurate:

```text
CONTEXT / DOCTRINE
      -> REDUCE
      -> IDENTIFIABLE CORE + RESIDUAL FIBRE
      -> WITNESS / COMPOSE / GLUE as supported by the doctrine
      -> either RECONSTRUCT or state the exact NO-GO / MODULI endpoint.
```

Not every application requires every stage.

## 9. The first strong calibration: categories

The category theorem in [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) deliberately erases all object and endpoint labels from a small category. The primitive data still include the **totalized execution law**: actual composition when defined and an absorbing failure otherwise.

Two-sided continuation success recovers endpoint types from that execution law; raw arrows retained as fibres then recover the original Hom sets and composition.

This shows that “objecthood downstream of interaction” is mathematically exact in at least one broad sector. It does **not** show that execution grammar itself can be reconstructed from bare scalar responses.

## 10. Foundational target

The open target is not “delete object symbols from category theory.” That is classical. It is to identify natural interaction laboratories for which a frozen doctrine-relative meta-rule simultaneously accounts for:

- response-minimal composition-stable semantics;
- maximal identifiable invariants and residual fibres;
- doctrine-relative interfaces/objecthood;
- internally characterized maps;
- witness multiplicity and provenance;
- exact cross-object/cross-process Hom data;
- doctrine refinement;
- local-to-global descent and its obstructions;
- blind calibration in mathematically distant domains without target leakage.

That target is formalized as WEIR in [`theory/03-weir.md`](theory/03-weir.md).

See also [`EIG_IDENTIFIABILITY_BOUNDARIES_20260902.md`](EIG_IDENTIFIABILITY_BOUNDARIES_20260902.md) for the current boundary-first formulation.
