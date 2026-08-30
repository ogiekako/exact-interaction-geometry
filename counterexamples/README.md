# Counterexample harvesting

One practical goal of the programme is to use interaction/factorization structure to search for **short standalone counterexamples** to existing conjectures and open questions.

The working heuristic is

```text
separate optimum
    ?=
joint optimum
```

and the search pipeline is

```text
support obstruction
 -> factorization atlas
 -> hidden-middle/shared-latent opportunity
 -> weight/resource consistency
 -> exact certificate.
```

A harvested result is publication-ready only when its correctness is independent of the broader programme.

## Harvested consequence

- [`source-pair-augmentation/`](source-pair-augmentation/) — canonical explicit counterexamples to the Parnas--Shraibman source-pair augmentation question for **both Boolean and binary rank**. The Boolean example has four rows; the binary example has five rows and is exhaustively row-minimal among examples of this form.
- [`boolean-rank-augmentation/`](boolean-rank-augmentation/) — historical Boolean-only first branch, retained for provenance.

Standalone paper:

[`../papers/source-pair-augmentation/`](../papers/source-pair-augmentation/)

Exact verifier:

```bash
python3 verification/verify_source_pair_augmentation.py
```

## Active search portfolio retained in the original research ledger

- Boolean rank of uniform-intersection matrices such as `U_{3,20}` — exact rectangle-cover search.
- Cartesian-product extension complexity — support-first, weight-second factorization search.
- Regular polygon nonnegative-rank tightness — lower-priority exact-NMF search.

Search output belongs here only after it becomes an independently checkable mathematical certificate.
