# Verification

The repository separates proof certificates from search machinery. Search code is not required to validate any public finite example.

## Foundational regression

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it. It is regression evidence for the unbounded proof in `theory/02-category-reconstruction.md`.

## Boolean Tucker junction counterexample

```bash
python3 verification/verify_boolean_tucker_junction_counterexample.py
```

Expected output begins

```text
PASS boolean-tucker-junction
```

The checker uses no external solver, floating point, randomness, or Python `assert`. It derives the mode Boolean ranks and normalized minimum bases from the explicit `2 x 4 x 4` tensor, checks the four blocking zeros, verifies exact profiles `(2,3,4)` and `(2,4,3)`, and checks a same-shape same-mode-ranks tensor for which `(2,3,3)` is feasible.

The complete human-readable counterexample is [`../discoveries/boolean-tucker-junction-counterexample.md`](../discoveries/boolean-tucker-junction-counterexample.md).

## Retained calibrations

`make verify-discoveries` also checks the binary-Kronecker rediscovery and the earlier source-pair examples. Those are retained for reproducibility and methodology calibration; they are not the headline external case study.

## Combined CI

```bash
make verify-all
```

CI runs the combined target in Python 3.12.

## Boundary

A verifier can establish that a displayed finite certificate has the claimed combinatorial property. It does not establish historical novelty, publication priority, or the truth of the broader EIG programme.
