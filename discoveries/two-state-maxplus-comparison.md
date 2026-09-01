# Two-state max-plus comparison is decidable

**Typeset PDF (recommended for reading):** [`two-state-maxplus-comparison.pdf`](two-state-maxplus-comparison.pdf)  
**TeX source:** [`two-state-maxplus-comparison.tex`](two-state-maxplus-comparison.tex)

**Author:** Keigo Oka (`ogiekako@gmail.com`) — Google. Work done in a personal capacity; no Google internal resources were used. ORCID: [`0009-0007-8119-9267`](https://orcid.org/0009-0007-8119-9267).

**Status:** proof reconstructed and independently re-audited; public regression included. A targeted primary-source and current-literature audit through **2026-09-01** located no prior resolution of the two-state bounded-state comparison case. Historical absence cannot be proved bibliographically, so no absolute `first` claim is made.

This Markdown version is kept for browser reading, search, and diff review. The PDF above is the preferred typeset presentation. The finite regression is not the proof.

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

We allow arbitrary max-plus initial/final weights and words in `Sigma*`. The MFCS 2017 convention uses Boolean-valued initial/final vectors and nonempty words; restricting to that convention only simplifies the argument.

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

## 4. The tail trichotomy

Let `E` be the finite transition, initial, and final weights of `B`, and choose

```text
K = 1 + max{|alpha-beta| : alpha,beta in E},
```

with `K=1` if fewer than two finite weights occur. This lies strictly beyond every transition breakpoint, fixed tail shift, and final readout breakpoint.

For a positive tail `z>K`, the active first row `(a,b)` gives all possibilities.

- If both `a,b` are finite, the successor gap is the fixed value `a-b` and the height increment is the constant `max(a,b)`: the old gap is **forgotten without being read**.
- If exactly one of `a,b` is finite, the successor either has an infinite gap (forget) or propagates an unbounded magnitude of the form `n+s` for a fixed integer `s`; the height increment is constant.
- If `a=b=-infinity`, the successor projective state is determined only by `(c,d)`, while the height increment is `max(c,d)-n`: the magnitude is **read and then forgotten**.

The negative tail is symmetric.

### Tail trichotomy

For `n=|z|>K`, every nondead transition has exactly one of these forms:

```text
PROPAGATE:
    n' = n+s for a fixed s,
    height increment = fixed c.

FORGET:
    successor projective state independent of n,
    height increment = fixed c.

READ-AND-FORGET:
    successor projective state independent of n,
    height increment = c-n.
```

Hence the property actually needed later is:

> **Whenever a transition's height increment depends on the unbounded gap magnitude, that magnitude is not propagated to the successor.**

For example, the all-zero matrix is a silent-forget case: the successor gap and height increment are both zero. This is the third case that a literal retain/read dichotomy would miss.

## 5. Exact functional one-counter compilation

The tail trichotomy compiles `B` exactly into a functional one-counter transducer.

The invariant is explicit:

```text
bounded or infinite projective state -> counter = 0
tail state                           -> counter = n = |z| > K
```

Finite control stores the maximal side, infinite-gap information, and every finite gap value at most `K`.

Each tail transition is implemented as follows.

- **Propagate:** emit the fixed constant and shift the counter by the fixed integer `s`. To determine whether the shifted value has entered the bounded region, destructively probe at most `K+1` decrements. If zero is reached within `K`, record the exact bounded value in finite control and leave the counter at zero. Otherwise restore `K+1` units and remain in a tail state. The probe emits zero.
- **Forget:** drain the counter to zero with **zero emission**, emit the fixed constant, and move to the fixed bounded/infinite successor.
- **Read-and-forget:** drain the counter while emitting `-1` per decrement, emit the fixed constant, and move to the fixed successor.
- **Death:** reject.

The final vector is handled by the same invariant. On a tail, either the active final coordinate contributes a constant (silent drain), or only the inactive coordinate contributes (drain with `-1` per decrement and then add a constant).

All macro-actions are forced by the current control state, counter tests, and input letter. The transducer may therefore be chosen deterministic on each input word. Consequently:

```text
[[B]](w) = -infinity
    iff there is no successful computation on w;

otherwise every successful computation on w emits exactly [[B]](w).
```

This functional strengthening rules out spurious output values in the Parikh reduction.

## 6. Deciding containment

First handle support: whether a word has a finite value in a max-plus automaton is regular. A word with finite `[[A]]` and `[[B]]=-infinity` is an immediate counterexample.

On the common finite support, choose an accepting run `rho` of `A` and synchronize it with the functional one-counter realization of `B`. Label every transition of the product by a fresh symbol. The successful transition sequences form an effectively given one-counter language, hence a context-free language.

By the effective Parikh theorem, its transition-count vectors form an effectively semilinear set. Both

```text
weight_A(rho)
[[B]](w)
```

are integer-linear functions of those transition counts. Therefore existence of a violating run

```text
weight_A(rho) > [[B]](w)
```

is an existential Presburger question over an effective semilinear set, and is decidable.

Finally, `[[A]](w) > [[B]](w)` exactly when some accepting run of `A` has weight greater than `[[B]](w)`. This proves decidability of `[[A]] <= [[B]]`.

Taking `A` to be the total zero one-state automaton gives two-state positivity.

## 7. Independent regression

Run

```bash
python3 verification/verify_two_state_maxplus.py
```

The public checker performs three exact finite regressions:

1. `22,032` direct checks of the signed-gap and height-cocycle formulas;
2. `15,552` tail checks over every `2 x 2` letter with entries in `{-infinity,-2,-1,0,1,2}` and both projective tails, explicitly classifying death / propagate / forget / read-and-forget and checking the all-zero silent-forget case;
3. `465,831` end-to-end word checks comparing direct max-plus evaluation with a separately coded projective/counter evaluator.

The infinite theorem rests on the proof above, not on finite enumeration.

## 8. Novelty audit

A fresh audit on 2026-09-01 searched the theorem under neighbouring descriptions including two-state max-plus comparison/positivity, `2 x 2` tropical formulations, one-counter compilation, few-register CRA work, and recent determinisation/unambiguisation literature. No prior theorem deciding the two-state bounded-state comparison case, no theorem deciding arbitrary-left versus two-state-right containment, and no equivalent one-counter compilation was located.

Especially relevant neighbouring work includes:

- Laure Daviaud, Pierre Guillon, Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19` — states the bounded-state open range `2..552`.
- Laure Daviaud, Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48` — the same two-state model, but identities rather than comparison.
- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2` — containment/equivalence survey; no two-state solution recorded.
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, LMCS 21(3), 2025, DOI `10.46298/lmcs-21(3:3)2025` — solves affine domination, explicitly a relaxation of exact containment.
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651` — broad frontier, not a two-state comparison theorem.
- later few-register, determinisation, unambiguisation, register-minimisation, and unary-tropical results — different restrictions or decision problems.

The detailed search record is in [`../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md).

## 9. Why it belongs in EIG

The proof itself is ordinary weighted-automata mathematics and does not depend on EIG. The result arose within the EIG research programme: its residual/interface viewpoint led to isolating the one-dimensional projective gap and asking whether one step can both expose an unbounded residual magnitude and preserve it for future computation. The tail trichotomy shows that it cannot.

## 10. AI-assisted research disclosure

This work was developed through AI-assisted mathematical research. OpenAI reasoning models, including GPT-5.6 Sol, materially contributed to theorem discovery, proof drafting, verifier generation, and literature-audit support. Keigo Oka directed the research programme, curated the final mathematical claims after adversarial checking, and takes responsibility for the contents of this note.

Model output is not treated as mathematical evidence. The theorem is intended to stand on the written proof above, together with the public regression as an independent finite check of its algebraic mechanism.
