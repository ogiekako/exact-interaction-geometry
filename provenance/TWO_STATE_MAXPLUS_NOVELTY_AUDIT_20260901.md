# Novelty audit: two-state max-plus comparison

Date: **2026-09-01 JST**

Target claim:

```text
Given an arbitrary max-plus automaton A over Z_max and a max-plus automaton B
with at most two states, it is decidable whether [[A]] <= [[B]] pointwise.
```

Immediate consequences include decidability of comparison/equivalence when both automata have at most two states and decidability of `Pos_2^k(Z_max)` for every finite alphabet size `k`.

## Verdict

```text
published statement leaving d=2 open:     CONFIRMED
prior two-state comparison solution:       NOT FOUND
prior arbitrary-left/two-state-right result: NOT FOUND
prior equivalent one-counter compilation: NOT FOUND
current 2026 adjacent literature conflict: NOT FOUND
historical absence / absolute firstness:   NOT CERTIFIED
```

The appropriate public wording is therefore:

> A targeted primary-source and current-literature audit through 2026-09-01 located no prior resolution of the two-state bounded-state comparison case.

Do **not** replace this with an unqualified “first proof” or “previously unsolved until this work” unless specialist feedback supplies a stronger historical basis.

## 1. The open problem is real

Laure Daviaud, Pierre Guillon, and Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19`, prove comparison undecidable with a fixed bound of 553 states and explicitly ask what happens for state counts from 2 through 552. Their conclusion specifically singles out the two-state case as difficult.

Thus the present theorem is not a problem manufactured retrospectively from a gap in terminology: `d=2` is an explicit endpoint of a published bounded-state comparison question.

## 2. Same-model two-state work

The most important same-parameter paper found is:

- Laure Daviaud and Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48`.

It studies exactly the full two-state max-plus automaton class, but its problem is semigroup/automaton **identities**: which pairs of input words cannot be distinguished by any two-state automaton. It contains no positivity, containment, comparison, or one-counter decision theorem.

Structural literature on `2 x 2` tropical matrix semigroups, including Johnson--Kambites and related identity/Green-relation work, was also checked. No route from those results to the target containment theorem was located.

## 3. Containment/equivalence surveys and general weighted-automata results

Checked:

- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2`.
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651`.
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, Logical Methods in Computer Science 21(3), 2025, DOI `10.46298/lmcs-21(3:3)2025` (conference version: LICS 2023; arXiv:2304.05229).

The 2020 survey records bounded-state undecidability but no two-state positive theorem. The Almagor--Boker--Kupferman line maps decision problems under restrictions such as weight domains and automaton structure, but no fixed two-state comparison result matching the target was found. The Big-O theorem decides an affine-domination relaxation and explicitly remains distinct from exact containment.

## 4. Ambiguity, simulation, and determinisation do not subsume the target

Known decidable classes such as finitely ambiguous max-plus automata do not cover arbitrary two-state max-plus automata: two states do not bound ambiguity.

Recent simulation/bisimulation work gives sound structural witnesses for containment or equivalence in restricted situations, but simulation is not complete for exact containment in general. The 2026 truncation/shifting work makes iterative simulation procedures more effective; it does not supply a complete two-state containment theorem.

The 2026 tropical determinisation breakthrough also does not imply the target. It decides **whether** a given tropical weighted automaton has an equivalent deterministic presentation; it does not say that every two-state automaton is determinisable, and two-state nondeterministic tropical series already include non-determinisable examples.

Relevant 2026 papers checked include:

- Shaull Almagor, Guy Arbel, Sarai Sheinvald, *Determinization of Min-Plus Weighted Automata is Decidable*, SODA 2026.
- the same authors, *A Complexity Bound for Determinisation of Min-Plus Weighted Automata*, LICS 2026.
- the same authors, *Unambiguisability and Register Minimisation of Min-Plus Models*, ICALP 2026.
- Shaull Almagor, Ismael Jecker, Filip Mazowiecki, Lukasz Orlikowski, David Purser, Henry Sinclair-Banks, *Representing One Letter Weighted Automata over the Tropical Semiring*, CONCUR 2026.

The last paper fixes the **alphabet to one letter**, not the number of states.

## 5. Cost-register automata are adjacent but not the same bounded parameter

A `d`-state max-plus automaton can be represented through `d` evolving forward values, which makes few-register cost-register automata an obvious neighbouring literature. The exact restrictions are different, however.

Checked:

- Laure Daviaud and Andrew Ryzhikov, *Universality and Forall-Exactness of Cost Register Automata with Few Registers*, MFCS 2023. Three-register universality is undecidable for a copyless/reset model and the two-register case is highlighted as an open frontier.
- Andrei Draghici, Radoslaw Piorkowski, Andrew Ryzhikov, *Boundedness of Cost Register Automata over the Integer Min-Plus Semiring*, CSL 2025. Two-register boundedness is decidable for a different CRA restriction/problem.

These results support the relevance of a two-coordinate boundary, but neither translates to the present theorem while preserving the state bound and exact containment problem.

## 6. Search vocabulary used

The audit deliberately searched beyond the notation in the research note. Queries and source checks covered combinations of:

```text
two-state / 2-state / at most two states
max-plus automata / min-plus automata / tropical weighted automata
tropical rational series / dimension-two linear representations
comparison / containment / inclusion / dominance / positivity / universality
Pos_2^k / bounded-state comparison / few states
2 x 2 tropical matrices / tropical matrix semigroups
one-counter / counter transducer / semilinear / Parikh
cost register automata / two registers / few registers
determinisation / unambiguisation / simulation / bisimulation
```

Recent 2026 publications and arXiv/Dagstuhl/DBLP-visible material were included rather than stopping at the 2020 survey.

## 7. Strongest counter-arguments considered

### Could the 2026 determinisation theorem settle it indirectly?

No. Deciding whether an automaton is determinisable is not a universal determinisation theorem, and the target includes arbitrary two-state nondeterminism.

### Could finite ambiguity settle it?

No. State count does not imply finite ambiguity.

### Could `2 x 2` tropical semigroup structure settle it algebraically?

No such implication was located. The same-parameter literature found concerns identities, Green relations, idempotents, maximal subgroups, and related structure rather than pointwise comparison over all words.

### Could a two-register CRA theorem be equivalent after a routine translation?

Not under the published restrictions inspected. The register and control restrictions differ, and the numerical register bound is not preserved by the relevant equivalences.

### Could min-plus terminology hide the result?

The audit explicitly searched the sign-dual min-plus terminology, including the newest determinisation/unambiguisation literature. No matching exact containment theorem was located.

## 8. Mathematical-status separation

Novelty and correctness are separate.

The proof of the target theorem was re-audited from the two-state projective recurrence rather than inferred from this literature search. A later adversarial pass caught an overstrong shorthand in the first public proof: a tail can silently forget the old gap with a constant height increment, so the literal retain/read dichotomy is false (the all-zero letter is the smallest example). The corrected tail statement is the exact **propagate / forget / read-and-forget trichotomy**. The property needed for decidability survives: whenever a transition's height increment depends on the unbounded gap magnitude, the successor does not propagate that magnitude. Together with the strengthened functional one-counter construction and explicit counter invariant, this yields the same effective semilinearity/Presburger decision argument.

The public theorem note and public finite regression are:

- [`../discoveries/two-state-maxplus-comparison.md`](../discoveries/two-state-maxplus-comparison.md)
- [`../verification/verify_two_state_maxplus.py`](../verification/verify_two_state_maxplus.py)

The private chronological research ledger additionally contains an earlier `825,266`-case exact regression dated 2026-08-28. Because that earlier audit used the superseded two-way shorthand, the current public repaired proof and regression are the relevant claim surface for this point.
