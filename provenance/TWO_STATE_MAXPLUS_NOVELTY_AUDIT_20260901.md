# Literature review: two-state max-plus comparison

Date: **2026-09-01 JST**

Target claim:

```text
Given an arbitrary max-plus automaton A over Z_max and a max-plus automaton B
with at most two states, it is decidable whether [[A]] <= [[B]] pointwise.
```

Immediate consequences include decidability of comparison/equivalence when both automata have at most two states and decidability of `Pos_2^k(Z_max)` for every finite alphabet size `k`.

## Scope of this review

This file records a targeted literature review, not a certificate of novelty or historical firstness. It distinguishes the cited-source facts from the repository's search result.

The appropriate public wording is:

> Daviaud--Guillon--Merlet (MFCS 2017) explicitly leave the state range including `d=2` open. In the literature reviewed here through 2026-09-01, we did not identify a prior resolution of the two-state bounded-state comparison case or the stronger arbitrary-left/two-state-right theorem.

Do **not** replace this with an unqualified “first proof” or “previously unsolved until this work” unless a stronger historical basis is independently established.

## 1. The cited open problem

Laure Daviaud, Pierre Guillon, and Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19`, prove comparison undecidable with a fixed bound of 553 states and explicitly ask what happens for state counts from 2 through 552. Their conclusion specifically singles out the two-state case as difficult.

Thus `d=2` is an explicit endpoint of a published bounded-state comparison question. This source claim is distinct from any later judgment about whether the present manuscript is historically first to solve it.

## 2. Same-model two-state work

The most important same-parameter paper identified in the review is:

- Laure Daviaud and Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48`.

It studies the full two-state max-plus automaton class, but its problem is semigroup/automaton **identities** rather than positivity or pointwise containment.

Structural literature on `2 x 2` tropical matrix semigroups, including Johnson--Kambites and related identity/Green-relation work, was also considered. The review did not identify a theorem equivalent to the target containment statement.

## 3. Containment/equivalence surveys and general weighted-automata results

Checked:

- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2`.
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651`.
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, Logical Methods in Computer Science 21(3), 2025, DOI `10.46298/lmcs-21(3:3)2025` (conference version: LICS 2023; arXiv:2304.05229).

The 2020 survey records bounded-state undecidability but no two-state positive theorem was identified there. The Almagor--Boker--Kupferman line maps decision problems under restrictions such as weight domains and automaton structure; this review did not identify a fixed two-state comparison result matching the target. The Big-O theorem decides an affine-domination relaxation rather than exact containment.

## 4. Ambiguity, simulation, and determinisation

Known decidable classes such as finitely ambiguous max-plus automata do not cover arbitrary two-state max-plus automata: two states do not bound ambiguity.

Recent simulation/bisimulation work gives structural sufficient conditions in restricted settings, but no complete route to the target theorem was identified in this review.

The 2026 tropical determinisation results decide **whether** a given tropical weighted automaton has an equivalent deterministic presentation; they do not state that every two-state automaton is determinisable.

Relevant 2026 papers checked include:

- Shaull Almagor, Guy Arbel, Sarai Sheinvald, *Determinization of Min-Plus Weighted Automata is Decidable*, SODA 2026.
- the same authors, *A Complexity Bound for Determinisation of Min-Plus Weighted Automata*, LICS 2026.
- the same authors, *Unambiguisability and Register Minimisation of Min-Plus Models*, ICALP 2026.
- Shaull Almagor, Ismael Jecker, Filip Mazowiecki, Lukasz Orlikowski, David Purser, Henry Sinclair-Banks, *Representing One Letter Weighted Automata over the Tropical Semiring*, CONCUR 2026.

The last paper fixes the **alphabet to one letter**, not the number of states.

## 5. Cost-register automata are adjacent but not the same bounded parameter

A `d`-state max-plus automaton can be represented through `d` evolving forward values, which makes few-register cost-register automata an obvious neighbouring literature. The exact restrictions are different, however.

Checked:

- Laure Daviaud and Andrew Ryzhikov, *Universality and Forall-Exactness of Cost Register Automata with Few Registers*, MFCS 2023.
- Andrei Draghici, Radoslaw Piorkowski, Andrew Ryzhikov, *Boundedness of Cost Register Automata over the Integer Min-Plus Semiring*, CSL 2025.

These results are relevant to a two-coordinate boundary, but this review did not identify a routine translation yielding the target theorem while preserving the two-state condition and exact containment problem.

## 6. Search vocabulary used

The review searched beyond the notation in the research note. Queries and source checks covered combinations of:

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

## 7. Counter-arguments considered

### Could the 2026 determinisation theorem settle it indirectly?

The reviewed theorem decides whether an automaton is determinisable; it is not a universal determinisation theorem. No implication covering arbitrary two-state nondeterminism was identified.

### Could finite ambiguity settle it?

No. State count does not imply finite ambiguity.

### Could `2 x 2` tropical semigroup structure settle it algebraically?

The same-parameter literature reviewed here concerns identities, Green relations, idempotents, maximal subgroups, and related structure. No theorem equivalent to pointwise containment over all words was identified.

### Could a two-register CRA theorem be equivalent after a routine translation?

Not under the restrictions inspected in this review. The register and control restrictions differ, and no equivalence preserving the target parameterization was identified.

### Could min-plus terminology hide the result?

The review explicitly included the sign-dual min-plus terminology, including recent determinisation/unambiguisation literature. No matching exact containment theorem was identified.

## 8. Mathematical-status separation

Novelty and correctness are separate.

The proof of the target theorem was re-examined from the two-state projective recurrence rather than inferred from this literature search. A separate model-assisted adversarial pass found an overstrong shorthand in the first public proof: a tail can silently forget the old gap with a constant height increment, so the literal retain/read dichotomy is false (the all-zero letter is the smallest example). The corrected tail statement is the exact **propagate / forget / read-and-forget trichotomy**. The property needed for decidability survives: whenever a transition's height increment depends on the unbounded gap magnitude, the successor does not propagate that magnitude.

That internal review is process provenance, not independent external verification. The public mathematical claim rests on the written proof and the accompanying regression appropriate to its finite subclaims.

The public theorem note and public finite regression are:

- [`../discoveries/two-state-maxplus-comparison.md`](../discoveries/two-state-maxplus-comparison.md)
- [`../verification/verify_two_state_maxplus.py`](../verification/verify_two_state_maxplus.py)

The private chronological research ledger additionally contains an earlier exact regression dated 2026-08-28. Because that earlier internal review used the superseded two-way shorthand, the current public repaired proof and regression are the relevant public claim surface.
