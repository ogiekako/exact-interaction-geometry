# Dossier IV-B — graph-product storage separator and dependent dynamics

**Status:** `AUDITED / ACCEPTED`, with scoped dynamic-minimality language.

## Domain

A finite graph product split as

```text
V(Gamma) = A disjoint-union S disjoint-union B,
```

with no graph edge joining `A` directly to `B`, and right-invertible storage configurations in the vertex-monoid cones. Shore-local storage words are sealed; genuinely cross-private transactions remain joint edges.

## GPSH normal form

Peeling the terminal `S`-supported upper filter and then alternating maximal shore-supported upper filters gives a unique decomposition

```text
H = r_1 ... r_q t,
```

where `t in C(M_S)` and the nonempty frames alternate owners.

For private frame lists `alpha,beta`, let

```text
P_S(alpha,beta) = C(M_S) x Phase(|alpha|,|beta|).
```

Then zipping the lists according to the phase witness gives a canonical bijection

```text
C(M_Gamma) ~= disjoint-union_(alpha,beta) P_S(alpha,beta).
```

Relative to the fixed private-list projections, this is the reduced universal quotient of every exact extensional separator code.

## State versus dynamics

A smaller equality-pullback base can reconstruct complete states, but two configurations can have the same active private list and same small shared state while an owner-local push lands in different target shared states. Thus

```text
state reconstruction < deterministic owner-local transition typing.
```

The exact dynamic object is dependent/proarrow-like. A larger `J_dyn` is a sufficient symmetric deterministic completion, but no global minimality over arbitrary joint encodings is claimed.

## Information lower bound

In the pop-complete `B_a*B_b` specialization, any equality-pullback rectangularization of the balance requires unboundedly many shared base values as frame depth grows; the synchronization charge is `Theta(log N)` bits for depth `N` in the stated family. The full future stack requires more.

## Why it matters

This is the first explicit theorem showing that the separator is not “shared variables”. It is the minimal synchronization object required to reassemble the two private histories under the declared projections.

## Provenance

`GRAPH_PRODUCT_SEPARATOR_PROARROW_MINIMALITY_20260830.md` and its independent main audit.
