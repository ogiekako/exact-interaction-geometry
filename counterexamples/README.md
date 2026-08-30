# Counterexample harvesting

One practical goal of the programme is to use interaction/factorization structure to search for **short standalone counterexamples** to existing conjectures.

The working heuristic is:

```text
separate optimum
    ?=
joint optimum
```

and the search pipeline is:

```text
support obstruction
 -> factorization atlas
 -> hidden-middle/shared-latent opportunity
 -> weight/resource consistency
 -> exact certificate
```

A counterexample is publishable only when its proof/certificate is independent of the broader programme.

## Current targets / consequences

- [`boolean-rank-augmentation/`](boolean-rank-augmentation/) — explicit counterexample found; proof and verifier included.
- Boolean rank of `U_{3,20}` — active rectangle-cover search remains in the original research repo.
- Cartesian-product extension complexity — active support-first/NMF search remains in the original research repo.
