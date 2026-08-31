# Verification

The repository separates proof certificates from search machinery. Search code is not required to validate any public finite discovery.

## Foundational regression

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it. It is regression evidence for the unbounded proof in `theory/02-category-reconstruction.md`.

## Binary-Kronecker counterexample

```bash
python3 verification/verify_binary_kronecker_counterexample.py
```

Expected output:

```text
PASS: rank_bin(A)=5 and A tensor A has an exact 24-biclique partition (196/196 ones).
```

The checker is intentionally small and independent of the program that found the rectangles. It verifies:

- the displayed left and right integer null vectors;
- a unimodular `4 x 4` minor, establishing real rank four;
- the tiny local null-balance obstruction used in the handwritten proof that binary rank cannot be four;
- the trivial five-row-star upper bound implicitly from the displayed matrix;
- all 24 rectangles against a freshly reconstructed `A tensor A`;
- that no rectangle touches a zero;
- that all 196 one-entries are covered exactly once.

The machine-readable certificate is `discoveries/certificates/binary-kronecker-seed5-self-k24.json`. The complete proof is `discoveries/binary-kronecker-counterexample.md`.

## Earlier source-pair discoveries

```bash
make verify-discoveries
```

In addition to the Kronecker checker, this runs the exact finite source-pair enumeration and the unbounded Boolean-family regression. Those programs are secondary evidence; see the corresponding written notes for proof scope.

## Combined CI

```bash
make verify-all
```

CI runs this combined target in Python 3.12.

## Boundary

A verifier can establish that a displayed finite certificate has the claimed combinatorial property. It does not establish historical novelty, publication priority, or the truth of the broader EIG programme.
