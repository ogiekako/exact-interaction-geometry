# Verification

The repository separates proof certificates from search machinery. Search code is not required to validate any public finite example.

## Foundational regression

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it. The regression reconstructs contextual quotient classes from the untyped multiplication/response table, builds quotient multiplication, identifies object idempotents, recovers source/target object classes and identity witnesses, reconstructs Hom witness fibres, and only then compares the result with the hidden fixture labels. It is regression evidence for the unbounded proof in `theory/02-category-reconstruction.md`.

## Boolean Tucker junction counterexample

```bash
python3 verification/verify_boolean_tucker_junction_counterexample.py
```

Expected output begins

```text
PASS boolean-tucker-junction
```

The checker uses no external solver, floating point, randomness, normalization lemma, or Python `assert`. For each mode it exhausts every nonzero Boolean support mask directly, derives the exact mode Boolean rank and all minimum bases, verifies their uniqueness for the displayed tensor, checks the four blocking zeros, verifies exact profiles `(2,3,4)` and `(2,4,3)`, and checks a same-shape same-mode-ranks tensor for which `(2,3,3)` is feasible.

The complete human-readable counterexample is [`../discoveries/boolean-tucker-junction-counterexample.md`](../discoveries/boolean-tucker-junction-counterexample.md).

## Retained binary-Kronecker calibration

```bash
python3 verification/verify_binary_kronecker_counterexample.py
```

The machine-readable JSON certificate is the single source of the 24 rectangle list. The checker reads that file, reconstructs the self-Kronecker product, and checks exact-once coverage. Independently of the handwritten null-vector proof, it also computes the exact binary rank of the `5 x 5` base matrix by exhaustive legal-rectangle generation plus exact-cover dynamic programming.

This is a correctness/calibration check only; the nonmultiplicativity theorem is not claimed novel here.

## Other retained calibrations

`make verify-discoveries` also checks the earlier source-pair examples. Those are retained for reproducibility and methodology calibration; they are not the headline external case study.

## Combined CI

```bash
make verify-all
```

CI runs the combined target in Python 3.12.

## Boundary

A verifier can establish that a displayed finite certificate has the claimed combinatorial property. It does not establish historical novelty, publication priority, or the truth of the broader EIG programme.
