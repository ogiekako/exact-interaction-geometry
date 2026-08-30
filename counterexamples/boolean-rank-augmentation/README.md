# Historical Boolean-only certificate branch

This directory preserves the original four-row Boolean certificate found first in the search.

The canonical combined result now lives at:

[`../source-pair-augmentation/`](../source-pair-augmentation/)

and is verified by:

```bash
python3 verification/verify_source_pair_augmentation.py
```

The Boolean certificate here remains valid:

```text
A = {3,7,15}
U = {3,5,8}
V = {3,5,12}
```

but the current theorem resolves the source-pair question for **both Boolean and binary rank**. `counterexample.json` and the older Boolean-only verifier are retained for provenance/regression only.
