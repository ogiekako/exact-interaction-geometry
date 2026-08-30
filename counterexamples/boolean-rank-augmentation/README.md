# Boolean-rank augmentation counterexample

This directory contains the machine-readable certificate for the four-row Boolean-rank counterexample.

The human proof is in [`../../papers/boolean-rank-augmentation/`](../../papers/boolean-rank-augmentation/).

Verify with:

```bash
python3 verification/verify_boolean_rank_augmentation.py
```

Expected output includes:

```text
PASS
Boolean rank(A)=3
U and V are source bases
Boolean rank(A|U|V)=4
all 9 one-from-each augmentations have rank 3
```

The verifier exhaustively enumerates Boolean spanning sets on four rows and is independent of the Interaction Reconstruction programme.
