# Verification

The public repository keeps two verification layers separate.

## Foundational regression

Run:

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it.

It checks associativity of finite category consolidations, equality of two-sided success profiles exactly at equal endpoint pairs, separation of failure `0`, object/idempotent recovery, intrinsic identity recovery, exact Hom witness fibres, all preorders on 1--3 labelled objects (`1,4,29` cases), non-thin categories with parallel arrows, and an explicit non-ULF boundary example.

The expected final line is:

```text
PASS category-reconstruction checks=14659 preorders={1: 1, 2: 4, 3: 29}
```

This is regression evidence for a theorem whose unbounded proof is written in `theory/02-category-reconstruction.md`.

## External discovery certificates

Run:

```bash
make verify-discoveries
```

`verify_source_pair_counterexamples.py` performs exact exhaustive finite enumeration for the displayed Parnas--Shraibman source-pair candidates. It independently computes the minimum rank, all optimal bases, sourcehood in the base graph, the rank of the full source-pair augmentation, and every one-from-each cross pair.

Expected summary:

```text
Boolean: PASS rows=4 rank(A)=3 bases=32 sources=13 rank(A|U|V)=4
Binary: PASS rows=5 rank(A)=4 bases=14 sources=4 rank(A|U|V)=5
PASS source-pair counterexamples
```

`verify_unbounded_boolean_augmentation.py` checks the closed-form Boolean family through `r=30`, including the tree/source witnesses, triangular lower-bound pattern, and an explicit rank-`r` witness after every one-element deletion. It then exhaustively audits the complete `r=3` instance.

Expected final line:

```text
PASS checks=24570: general formulas r=2..30; exhaustive r=3 source/minimality audit
```

## Combined CI

```bash
make verify-all
```

CI runs this combined target in Python 3.12.

## Boundary

The finite counterexample verifier is intended to be independently reimplemented before public release. The unbounded Boolean result is an infinite theorem: its written proof, not checking the first 29 parameter values, carries the general claim. None of these programs establishes historical novelty or priority.
