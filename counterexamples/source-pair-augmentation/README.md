# Source-pair augmentation counterexamples — both ranks

Canonical finite certificates for the Parnas--Shraibman Section-6 source-pair question.

## Boolean rank

```text
rows = 4
A = {3,7,15}
U = {3,5,8}
V = {3,5,12}
rank(A)=3
rank(A|U|V)=4
rank(A|u|v)=3 for every u in U, v in V
```

## Binary rank

```text
rows = 5
A = {10,31,27,18}
U = {4,9,10,18}
V = {9,10,18,21}
rank(A)=4
rank(A|U|V)=5
rank(A|u|v)=4 for every u in U, v in V
```

The binary example is exhaustively row-minimal for this source-pair pattern: the verifier finds no counterexample on at most four rows.

Human proof: [`../../papers/source-pair-augmentation/`](../../papers/source-pair-augmentation/)

Machine verification:

```bash
python3 verification/verify_source_pair_augmentation.py
python3 -O verification/verify_source_pair_augmentation.py
```

`counterexamples.json` stores the displayed objects in a machine-readable form. Integer bit `2^i` denotes row `i+1`.
