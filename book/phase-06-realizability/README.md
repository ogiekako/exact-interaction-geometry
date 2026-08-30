# Phase VI — realizability and reconstruction

**Current status: generic raw shell CLOSED / KNOWN; strong reduced/non-copying form OPEN / REDUCED.**

Let

```text
p : E -> B
```

record the exposed boundary behavior of an execution category. For each boundary arrow `f:b->c`, define the profunctor of lifts

```text
M_f(x,y) = { u:x->y in E | p(u)=f }.
```

Composition gives normal-lax `Prof` structure.

## Generic theorem — prior art

Up to variance convention, categories over `B` correspond to normal-lax functors

```text
B -> Prof,
```

with converse reconstruction by the generalized Bénabou--Grothendieck construction.

The pseudo case corresponds to the Conduché/exponentiable exact-middle-factorization sector. The correct uniqueness statement is **up to the coend/fibre-zigzag equivalence**, not strict unique lifting.

Thus generic realizability/reconstruction is not a new mystery.

## Strong project-specific problem

The Grand Book does not want a tautological raw representation that can smuggle the complete global state into every witness. The strong target is a

```text
reduced + non-copying + cofinal + feedback-stable + reconstructive
```

interaction stack generated from the actual Phase-IV interfaces.

That theorem is not supplied automatically by the generic `Cat/B <-> lax Prof` correspondence and remains a high-value project-specific frontier.
