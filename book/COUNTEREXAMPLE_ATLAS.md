# Counterexample atlas

The programme was shaped as much by false stronger statements as by positive theorems. This page records the counterexamples that should be checked before proposing a new universal principle.

## C1. Premature neutralization

**Fixture.** In the bicyclic monoid `B=<p,q | pq=1>`, a component executing one `p` has no neutral run from `1`, and a component executing one `q` has no neutral run from `1`. But their raw ports compose:

```text
1 --p--> p --q--> 1.
```

**Kills.** “Project to neutral/public behaviour before composition.”

**Forces.** Full residual storage ports and raw composition before external projection.

---

## C2. Factor projections lose cross-order

In `B_a * B_b`, words with the same factorwise projections can have different future legality because cross-factor alternation/order is invisible to the two projections.

**Kills.** “A separator is just the tuple of shared/factor variables.”

**Forces.** Alternating owner/zipper synchronization or the equivalent GPSH compatibility proarrow.

---

## C3. State separator is not a dynamic separator

In the storage-separator audit, two configurations can have the same active private list and the same small state-reconstruction base, yet a left push lands in different target shared states.

**Kills.** “If a quotient reconstructs states, it is automatically sufficient for owner-local transition typing.”

**Forces.** Dependent/proarrow-like dynamics, or a larger deterministic completion.

---

## C4. No natural choice of one exact chart

A bare four-state null process has three nontrivial `2 x 2` Cartesian coordinate systems permuted transitively by its automorphism group.

**Kills.** “Every process has a canonically selected nontrivial decomposition chart.”

**Forces.** Equivariant atlases/moduli of exact charts.

---

## C5. Exact structure and fully abstract semantics cannot generally be one object

If contextual equivalence is nontrivial, a lossless exact representation and the least-information fully abstract observer quotient have incompatible universal properties.

**Kills.** “The canonical structural object should already be the observer-minimal semantic quotient.”

**Forces.** Two stages: lossless structural representation, then `Omega_O`.

---

## C6. No exhaustive effective LOW/HIGH atlas

A fixed transparent scalar family has both Presburger and non-Presburger truth sides non-r.e.

**Kills.** Any claimed exhaustive sound c.e. classification of unrestricted recurrent presentations.

**Forces.** Exact opaque atoms / residuals and doctrine-relative positive compilers.

---

## C7. Universal exact cut submodularity fails

For

```text
R = {x in N^4 : x1=x2 OR x3=x4},
```

the audited exact cut-channel values include

```text
lambda({1,2})   = 0,
lambda({2,3})   = 1,
lambda({2})     = 1,
lambda({1,2,3}) = 1,
```

so

```text
0 + 1 < 1 + 1.
```

**Kills.** “Every exact interaction information measure is submodular.”

**Mechanism.** Different cuts can exploit different disjunctive components.

**Forces.** Structural hypotheses for uncrossing; exact residual defects when submodularity fails.

---

## C8. Flat legs can compose to an arbitrary relation

Every relation `R subseteq X x Y` factors through its edge set `E=R` as

```text
R = graph(q) o graph(p)^op.
```

Both legs are functional/difunctional.

**Kills.** “Difunctional support relations form a proper compositionally closed universal flat ontology containing ordinary functions.”

**Forces.** Retention of hidden-middle witness data.

---

## C9. Arbitrary invented recodings defeat finite/cofinal chart selection

The null one-counter radix charts

```text
d_n(x)=(floor(x/n), x mod n)
```

form an infinite shorewise antichain under the nonvacuous comparison notion in the original ledger.

**Kills.** “There is a finite/cofinal nontrivial atlas covering all possible invented coordinate recodings.”

**Forces.** Declared intrinsic/protected doctrines; whole-state normalization is otherwise vacuous.

---

## C10. Fixed probes cannot reconstruct arbitrary category extensions

Given any fixed probe family `A` in `C`, extend the category by two isolated nonisomorphic objects `x,y`. Then every probe sees the same empty hom-data into both.

**Kills.** “One fixed probe language reconstructs every possible future mathematical world.”

**Forces.** World-relative / world-generating arity theorems.

---

## C11. First harvested external counterexample: Boolean-rank augmentation

For

```text
A={3,7,15},
U={3,5,8},
V={3,5,12}
```

as four-bit Boolean columns,

```text
rank_B(A)=3,
rank_B(A | U | V)=4,
rank_B(A | u | v)=3 for every u in U, v in V,
```

while `U,V` are source bases.

**Consequence.** The one-vector-from-each-source question posed by Parnas--Shraibman has a negative answer for Boolean rank, assuming no prior resolution is found in the final publication audit.

**Why it belongs here.** It was found by searching the factorization atlas for “jointly expensive but pairwise cheap” augmentation patterns — exactly the kind of synergy emphasized in Phase V.
