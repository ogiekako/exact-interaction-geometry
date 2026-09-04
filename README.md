# Two-state max-plus comparison

This repository contains one manuscript and a finite implementation check for its main calculation.

The manuscript proves the following statement.

> Let `A` be an arbitrary finite max-plus automaton over
> `Z_max = (Z union {-infinity}, max, +)`, and let `B` have at most two states.
> It is decidable whether `[[A]](w) <= [[B]](w)` for every word `w`.

The result also gives decidability of comparison, equivalence, and positivity when both automata have at most two states. No complexity bound is claimed.

- [Paper (PDF)](paper/two-state-maxplus-comparison.pdf)
- [TeX source](paper/two-state-maxplus-comparison.tex)

## Proof idea

After subtracting the common height from a two-state forward vector, the remaining unbounded state is one signed integer gap. Outside an effectively computable finite interval, each transition has one of three forms:

1. it propagates the gap by a fixed shift and adds a fixed output;
2. it forgets the gap and adds a fixed output;
3. it uses the gap in the output and then forgets it.

In particular, a transition cannot both use the unbounded magnitude in its output and preserve that magnitude for later transitions. This permits an exact functional one-counter implementation of the right-hand automaton. Synchronizing it with a run of `A`, applying effective Parikh semilinearity, and deciding the resulting Presburger condition gives the theorem.

This argument uses the one-dimensional projective state available with two states. With three states, two independent gaps can coexist, so the proof does not extend as written.

## Finite check

Run:

```bash
make check
```

The [script](checks/check_two_state_maxplus.py) checks the projective formulas, exhaustively classifies a finite family of transition tails, and compares direct and projective evaluators on finite test families. It is a regression for calculations used in the proof, not a proof of the theorem and not formal verification.

## Status

The manuscript is an unrefereed preprint. AI systems materially assisted in finding and drafting the argument and in writing the code. Readers should check the written proof; agreement between model runs and a passing regression are not independent evidence.

## License

Mathematical writing is available under CC BY 4.0. Code and workflow files are available under Apache 2.0. See [LICENSE.md](LICENSE.md).
