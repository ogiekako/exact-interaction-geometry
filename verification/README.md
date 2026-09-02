# Verification

The repository separates mathematical proofs from finite regressions and search machinery. Search code is not required to validate any public theorem statement or finite example.

## Foundational regression

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it. The regression reconstructs contextual quotient classes from the untyped multiplication/response table, builds quotient multiplication, identifies object idempotents, recovers source/target object classes and identity witnesses, reconstructs Hom witness fibres, and only then compares the result with the hidden fixture labels. It also includes a one-object category with a nontrivial endomorphism to ensure that an object class need not be a singleton. It is regression evidence for the unbounded proof in `theory/02-category-reconstruction.md`.

## Two-state max-plus comparison theorem

```bash
python3 verification/verify_two_state_maxplus.py
```

Expected output is of the form

```text
PASS two-state max-plus tail/compiler regression
closed-form cases: 22032
tail cases: 15552 {'death': ..., 'propagate': ..., 'forget': ..., 'read-and-forget': ...}
end-to-end word cases: 465831
```

The checker was written separately for the curated public repository rather than copied from the earlier discovery/review program. It uses exact integer/max-plus arithmetic, no external solver, no floating point, and no randomness. This separation is a software-engineering provenance fact, not a claim of independent third-party verification.

It checks three finite layers:

1. every displayed signed-gap and height-cocycle formula over all `2 x 2` letters with entries in `{-infinity,-2,-1,0,1,2}` and signed gaps in a fixed interval;
2. both projective tails for every such letter, classifying each nondead tail as **propagate**, **forget**, or **read-and-forget**, with an explicit regression asserting that the all-zero letter is a silent-forget case;
3. `465,831` direct-versus-compiled word evaluations on exhaustive one- and two-letter stress families.

The trichotomy distinction matters. A transition may forget an unbounded projective gap while emitting a gap-independent constant; such a transition is neither propagation nor read-and-forget. The infinite proof therefore uses zero-emission counter drain for silent forget, `-1`-per-decrement drain only for read-and-forget, and an explicit counter invariant for tail versus bounded control states.

The checker is a **regression for the proof**, not a proof by exhaustion. The infinite theorem additionally uses the written threshold argument, functional one-counter construction, effective Parikh theorem, and Presburger decision step in [`../discoveries/two-state-maxplus-comparison.md`](../discoveries/two-state-maxplus-comparison.md).

Historical novelty is discussed separately in [`../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](../provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md); no program can establish bibliographic priority.

## Retained binary-Kronecker calibration

```bash
python3 verification/verify_binary_kronecker_counterexample.py
```

The machine-readable JSON certificate is the single source of the 24 rectangle list. The checker reads that file, reconstructs the self-Kronecker product, and checks exact-once coverage. Separately from the handwritten null-vector proof, it also computes the exact binary rank of the `5 x 5` base matrix by exhaustive legal-rectangle generation plus exact-cover dynamic programming.

This is a correctness/calibration check only; the nonmultiplicativity theorem is not claimed novel here.

## Other retained calibrations

`make verify-discoveries` also checks the earlier source-pair examples. Those are retained for reproducibility and methodology calibration; they are not the headline external theorem.

A Boolean Tucker rank-profile checker that had briefly been part of this public verification surface was retired on 2026-09-02 together with its external-case-study wording. The curation review did not identify a published conjecture/problem corresponding to the universal statement the finite example refuted. Git history preserves that calibration; it is not part of the current public theorem surface.

## Combined CI

```bash
make verify-all
```

CI runs the combined target in Python 3.12, including the two-state max-plus regression in normal and optimized Python.

## Boundary

A finite regression can catch algebraic, indexing, threshold, or certificate errors and can provide separate computational evidence for finite subclaims of a proof. It cannot replace an unbounded mathematical argument, establish historical novelty, certify publication priority, or prove the broader EIG programme.
