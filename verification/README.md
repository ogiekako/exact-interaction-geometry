# Verification

The checked-in verifier is deliberately small and tied to a theorem whose proof is also written out.

Run:

```bash
make verify
```

This executes `verification/verify_category_reconstruction.py` in normal Python and with `python -O`, then byte-compiles it.

The regression checks:

- associativity of finite category consolidations;
- equality of two-sided success profiles exactly at equal endpoint pairs;
- separation of failure `0`;
- recovery of one quotient idempotent per object;
- intrinsic local identity recovery;
- exact Hom witness fibres;
- all preorders on 1, 2, and 3 labelled objects (`1, 4, 29` cases);
- non-thin two-object categories with 1 through 7 parallel arrows;
- an explicit category where object reconstruction holds but ULF factorization fails.

The expected final line is:

```text
PASS category-reconstruction checks=14659 preorders={1: 1, 2: 4, 3: 29}
```

Finite regression is supporting evidence, not the proof of the unbounded theorem.
