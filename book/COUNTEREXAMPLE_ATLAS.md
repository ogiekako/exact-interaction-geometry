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

In `B_a * B_b`, the configurations `p_a p_b` and `p_b p_a` have the same factorwise projections, but `q_a` is illegal from the former and legal from the latter.

**Kills.** “A separator is just the tuple of factor/shared variables.”

**Forces.** Alternating owner/zipper synchronization or an equivalent compatibility proarrow.

---

## C3. State separator is not a dynamic separator

Two configurations can have the same active private list and the same small state-reconstruction base, yet the same owner-local push lands in different target shared states.

**Kills.** “If a quotient reconstructs states, it automatically types local transitions.”

**Forces.** Dependent/proarrow-like dynamics, or a larger deterministic completion.

---

## C4. No natural choice of one exact chart

A bare four-state null process has three nontrivial `2 x 2` Cartesian coordinate systems permuted transitively by `S_4`.

**Kills.** “Every process has a canonically selected nontrivial decomposition chart.”

**Forces.** Equivariant atlases/moduli of exact charts, unless additional protected structure legitimately breaks the symmetry.

---

## C5. Exact structure and fully abstract semantics cannot generally be one object

If contextual observer equivalence is nontrivial, lossless raw reconstruction requires distinguishing states that the least-information fully abstract quotient must identify.

**Kills.** “The canonical structural object should already equal the observer-minimal semantic quotient.”

**Forces.** Two stages:

```text
lossless structure -> exact raw semantics -> Omega_O.
```

---

## C6. No exhaustive effective LOW/HIGH atlas

A fixed transparent scalar family has both Presburger and non-Presburger truth sides non-c.e.

**Kills.** Any claimed exhaustive sound c.e. LOW/HIGH classification of unrestricted recurrent presentations.

**Forces.** Exact opaque residuals and doctrine-relative positive compilers.

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

**Forces.** Structural hypotheses for uncrossing and an explicit defect/curvature theory outside flat sectors.

---

## C8. Flat legs can compose to an arbitrary relation

Every relation `R subseteq X x Y` factors through its edge set `E=R` as

```text
R = graph(q) o graph(p)^op.
```

Both legs are functional/converse-functional and difunctional.

**Kills.** “Difunctional support relations form a proper compositionally closed universal flat ontology containing ordinary functions.”

**Forces.** Retention of hidden-middle witness data.

---

## C9. Arbitrary invented recodings defeat finite/cofinal chart selection

The null one-counter radix charts

```text
d_n(x)=(floor(x/n), x mod n)
```

form an infinite antichain under the nonvacuous comparison notion used in the research ledger.

**Kills.** “A finite/cofinal nontrivial atlas covers all invented coordinate recodings.”

**Forces.** Intrinsic/protected admissibility. Whole-state normalization is otherwise exact but vacuous.

---

## C10. Fixed probes cannot reconstruct arbitrary category extensions

Given fixed probes `A` in `C`, extend the category by two isolated nonisomorphic objects `x,y`. Every probe sees the same empty hom-data into both.

**Kills.** “One fixed local probe language reconstructs every arbitrary mathematical category extension.”

**Forces.** World-relative/world-generating arity theorems.

---

## C11. External harvested counterexample: source-pair augmentation fails for both ranks

Parnas--Shraibman ask whether, when two source bases jointly raise Boolean/binary rank, some single vector from each source already raises the rank.

### Boolean rank — four rows

```text
A={3,7,15},
U={3,5,8},
V={3,5,12}.
```

Then

```text
rank_bool(A)=3,
rank_bool(A|U|V)=4,
rank_bool(A|u|v)=3 for every u in U, v in V,
```

and `U,V` are source bases.

### Binary rank — five rows

```text
A={10,31,27,18},
U={4,9,10,18},
V={9,10,18,21}.
```

Then

```text
rank_binary(A)=4,
rank_binary(A|U|V)=5,
rank_binary(A|u|v)=4 for every u in U, v in V,
```

and `U,V` are source bases. Exact exhaustive search finds no binary example of this form on at most four rows, so the displayed binary example is row-minimal.

**Consequence.** The Section-6 source-pair strengthening is false for both Boolean and binary rank, subject only to the ordinary final literature/priority refresh before publication.

**Why Phase V found it.** The base graph is a finite factorization atlas. The question asserts that incompatibility of two source interfaces is pairwise visible. The counterexamples realize the opposite pattern:

```text
jointly expensive,
pairwise cheap.
```

This is exactly the no-choice/factorization-synergy mechanism that Phase V suggests searching for.

Standalone paper and verifier:

- `papers/source-pair-augmentation/`
- `verification/verify_source_pair_augmentation.py`
