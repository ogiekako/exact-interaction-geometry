# Two-state max-plus comparison is decidable

**Status:** proof reconstructed and independently re-audited; public regression included. A targeted primary-source and current-literature audit through **2026-09-01** located no prior resolution of the two-state bounded-state comparison case. Historical absence cannot be proved bibliographically, so no absolute `first` claim is made.

This note is self-contained at the level needed to check the mathematical mechanism. The finite regression is not the proof.

## 1. Result

Work over the max-plus semiring

```text
Z_max = (Z union {-infinity}, max, +).
```

A max-plus automaton `A` computes a function `[[A]]` from words to `Z_max` by taking the maximum weight of an accepting run.

### Theorem

Let `A` be an arbitrary finite max-plus automaton over `Z_max`, and let `B` be a max-plus automaton with at most **two states**. It is decidable whether

```text
[[A]](w) <= [[B]](w)   for every word w.
```

Consequently:

1. comparison of two max-plus automata with at most two states is decidable;
2. equivalence of two such automata is decidable;
3. for every finite alphabet size `k`, two-state positivity `Pos_2^k(Z_max)` is decidable.

No useful complexity bound is claimed here.

## 2. The published open case

Laure Daviaud, Pierre Guillon, and Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, proved bounded-state undecidability at 553 states and explicitly left the interval from 2 through 552 open. Their conclusion asks what happens “between 2 and 552 states” and notes that even the two-state case appears difficult.

The theorem above closes the `d=2` endpoint of that stated bounded-state comparison question. It is slightly stronger than needed for that endpoint because only the **right-hand** automaton is required to have at most two states.

## 3. Two-state projective coordinates

Let the current forward row of `B` be

```text
x = (x_1, x_2).
```

When it is not identically `-infinity`, split it into a common height and a projective gap:

```text
H(x) = max(x_1,x_2),
z(x) = x_1 - x_2.
```

The signed gap may be an integer or `+/- infinity`. After subtracting the common height, every finite projective state is therefore one of

```text
(0,-n)  or  (-n,0),   n >= 0.
```

Thus the unbounded part of the two-state dynamics is one-dimensional.

For a letter matrix

```text
M = [[a,b],
     [c,d]],
```

use the representative `(z,0)` for a finite signed gap. Direct max-plus multiplication gives

```text
F_M(z) = max(z+a,c) - max(z+b,d).                 (3.1)
```

The height increment `delta = H(x M)-H(x)` is

```text
delta(z) = max(max(a,b),     max(c,d)-z)    for z >= 0,
delta(z) = max(max(a,b)+z,   max(c,d))      for z <= 0.       (3.2)
```

These identities are immediate from the two coordinates of `(z,0) M`.

## 4. The retain/read lemma

Let `E` be the finite transition, initial, and final weights of `B`, and choose

```text
K = 1 + max{|alpha-beta| : alpha,beta in E},
```

with `K=1` if fewer than two finite weights occur. This is strictly beyond every transition breakpoint, every fixed tail shift, and the final readout breakpoint.

Consider first a positive tail `z>K`. The four possibilities for the active first row `(a,b)` of `M` give the entire phenomenon.

- If both `a,b` are finite, the successor gap is the fixed value `a-b` and the height increment is the constant `max(a,b)`.
- If exactly one of `a,b` is finite, the successor either has an infinite gap or retains an unbounded gap of the form `z + constant` (possibly on the opposite side). The height increment is still constant.
- If `a=b=-infinity`, the successor projective state is determined only by `(c,d)`, hence is independent of `z`, while the height increment is

```text
max(c,d) - z.
```

The negative tail is the same argument with the two current-state coordinates exchanged.

Therefore:

### Retain/read separation

For `|z|>K`, a letter can do one of two things with the unbounded gap magnitude:

```text
RETAIN it into the next projective state, with a gap-independent height increment,

or

READ it into the height increment, in which case the successor projective state forgets it.
```

It cannot both retain and read the same unbounded gap in one letter step.

This is the only nontrivial structural lemma in the decision argument. It is a finite case split on a `2 x 2` max-plus matrix.

## 5. Exact one-counter compilation

The retain/read lemma compiles `B` exactly into a one-counter transducer.

Finite control stores:

```text
which coordinate is currently maximal,
whether the other coordinate is at finite or infinite gap,
and every gap value <= K.
```

For a finite gap larger than `K`, one nonnegative counter stores its magnitude.

Each letter is implemented as follows.

- A bounded successor is a finite-control update.
- A retained tail gap changes by a fixed integer, implemented by finitely many counter increments or blocking decrements.
- A read/erase step drains the counter; each decrement emits `-1`, followed by one fixed emission. The successor gap is then bounded or infinite and no longer depends on the old counter value.
- Death enters a rejecting/dead control state.

The final vector is handled by the same threshold. If the active final coordinate is finite, readout adds a constant. If only the inactive final coordinate survives, readout drains the gap once and then adds a constant.

Hence there is an effectively constructible one-counter transducer `T_B` whose emitted integer on every word is exactly `[[B]](w)` whenever that value is finite, and which rejects exactly the words on which `B` has value `-infinity`.

The construction uses only finite control, one nonnegative counter, increment, blocking decrement, zero test, and fixed integer emissions.

## 6. Deciding containment

It remains to compare an arbitrary max-plus automaton `A` with the exact one-counter realization of `B`.

First handle support: whether a word has a finite value in a max-plus automaton is a regular-language question. A word with finite `[[A]]` and `[[B]]=-infinity` is an immediate counterexample, and existence of such a word is decidable by ordinary finite automata.

On the common finite support, choose an accepting run `rho` of `A`. Synchronize the finite run automaton of `A` with `T_B`. Label every transition of this product by a fresh transition symbol. The successful transition sequences form an effectively given **one-counter language**, hence a context-free language.

By the effective Parikh theorem, its transition-count vectors form an effectively semilinear set. Both quantities

```text
weight_A(rho)
output_B(w)
```

are integer-linear functions of those transition counts (initial/final contributions can be encoded by fixed start/end transitions).

Therefore existence of a violating run

```text
weight_A(rho) > output_B(w)
```

is an existential Presburger question over an effective semilinear set, and is decidable.

Finally,

```text
[[A]](w) > [[B]](w)
```

holds exactly when some accepting run `rho` of `A` has weight greater than `[[B]](w)`. This proves decidability of `[[A]] <= [[B]]`.

Taking `A` to be the total zero one-state automaton gives two-state positivity.

## 7. Independent regression

Run

```bash
python3 verification/verify_two_state_maxplus.py
```

The public checker is deliberately independent of any search procedure. It performs three exact finite regressions:

1. `22,032` direct checks of the signed-gap and height-cocycle formulas;
2. `15,552` tail checks over every `2 x 2` letter with entries in `{-infinity,-2,-1,0,1,2}` and both projective tails, looking directly for a retain/read violation;
3. `465,831` end-to-end word checks comparing direct max-plus evaluation with a separately coded tail/counter evaluator.

The infinite theorem rests on the proof above, not on finite enumeration.

The private chronological research ledger also contains an earlier, larger independent regression with `825,266` exact checks and a separate proof audit. The public checker was written afresh for this curated note rather than importing the discovery/audit code as an oracle.

## 8. Novelty audit

A fresh audit on 2026-09-01 searched the theorem under the following neighbouring descriptions:

```text
two-state / 2-state max-plus automata
bounded-state max-plus comparison and containment
positivity / universality for two-state tropical weighted automata
2 x 2 tropical matrix / rational-series formulations
min-plus sign-dual formulations
one-counter compilation and effective semilinear spectra
few-register cost-register automata
recent determinisation / unambiguisation / simulation literature
```

No prior theorem deciding the two-state bounded-state comparison case, no theorem deciding arbitrary-left versus two-state-right containment, and no equivalent one-counter compilation was located.

Especially relevant neighbouring work is:

- Laure Daviaud, Pierre Guillon, Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19` — states the bounded-state open range `2..552`.
- Laure Daviaud, Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48` — exact same two-state model, but identities rather than positivity/comparison.
- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2` — survey of containment/equivalence and restricted classes; no two-state solution recorded.
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651` — broad decidability frontier, not a two-state bounded-state comparison theorem.
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, LICS 2023 / arXiv:2304.05229 — decides an affine-domination relaxation, not exact containment.
- Laure Daviaud, Andrew Ryzhikov, *Universality and Forall-Exactness of Cost Register Automata with Few Registers*, MFCS 2023 — nearby few-register frontier in a differently restricted CRA model.
- Andrei Draghici, Radoslaw Piorkowski, Andrew Ryzhikov, *Boundedness of Cost Register Automata over the Integer Min-Plus Semiring*, CSL 2025 — a two-register decidability result for a different problem/model.
- Shaull Almagor, Guy Arbel, Sarai Sheinvald, *Determinization of Min-Plus Weighted Automata is Decidable*, SODA 2026 — determinisability, not containment.
- the same authors' LICS/ICALP 2026 work on determinisation complexity, unambiguisability, and register minimisation — again different decision problems.
- Shaull Almagor et al., *Representing One Letter Weighted Automata over the Tropical Semiring*, CONCUR 2026 — unary alphabet rather than two states.

The current novelty posture is therefore:

```text
mathematical correctness:        PROVED / independently re-audited
public finite regression:        PASS
published open-case match:       YES, d=2 of DGM 2017 bounded-state comparison
prior resolution located:        NO, in targeted audit through 2026-09-01
absolute historical priority:    NOT CERTIFIED
```

The detailed search record is in [`../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md).

## 9. Why it belongs in EIG

The proof itself is ordinary weighted-automata mathematics and does not depend on EIG.

The EIG connection is discovery provenance. Projectivizing the two-state forward response isolates one exact unbounded residual coordinate. The decisive question is then whether an interaction step can both preserve that residual information for future continuation and expose its magnitude to the current response. In dimension two the answer is no: the retain/read lemma forces a one-counter boundary. That structural separation suggested the normal form and the decision procedure.

This is the kind of external test the programme wants: an interaction-first question selects a conventional mathematical problem, and the final theorem is independently stated and checkable without EIG vocabulary.
