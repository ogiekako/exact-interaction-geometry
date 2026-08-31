# Status and epistemic boundary

Snapshot: **2026-08-31 JST**

This file is intentionally conservative. It records only claims appropriate for the public EIG surface.

## Audited / proved foundation core

| Claim | Status | Novelty posture |
| --- | --- | --- |
| contextual equality of finite response rows gives the unique coarsest deterministic exact interface | **PROVED / MAIN-AUDITED** | elementary / classical minimization pattern |
| semiring witness factor rank obeys serial data processing and parallel submultiplicativity | **PROVED / MAIN-AUDITED** | classical factorization algebra; EIG interpretation is organizational |
| two-sided syntactic interaction quotient is composition-stable and response-minimal | **PROVED / MAIN-AUDITED** | classical syntactic-algebra core |
| idempotent splitting gives typed interaction categories | **PROVED / MAIN-AUDITED** | classical Karoubi/Cauchy core |
| changing the response doctrine can change the derived object spectrum | **PROVED / MAIN-AUDITED** | strict finite calibration |
| every small category is exactly reconstructible from its untyped consolidation, one-bit composition success, and retained raw-arrow witness fibres | **PROVED AFTER MAIN AUDIT** | classical consolidation ingredients; EIG operational recognition formulation |
| exact category reconstruction does not imply ULF/Conduche factorization | **PROVED / explicit counterexample** | boundary theorem |

## External-search calibrations and candidates

These are logically separate from the foundational EIG claims.

### Binary rank under Kronecker product — corrected prior-art status

For the explicit `5 x 5` matrix in [`discoveries/binary-kronecker-counterexample.md`](discoveries/binary-kronecker-counterexample.md):

```text
rank_bin(A) = 5
rank_bin(A tensor A) <= 24 < 25 = rank_bin(A)^2.
```

The finite statement is correct: it has a short handwritten lower bound and an exact 24-biclique certificate.

However, **the nonmultiplicativity theorem is not novel to this project**. Yaroslav Shitov publicly posted a different `5 x 5` binary matrix with the same `5 -> 24` separation on **2026-07-25** in *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*.

Publication posture: **CORRECT INDEPENDENT REDISCOVERY / CALIBRATION; NO THEOREM-PRIORITY CLAIM.**

The example remains useful only as evidence that the EIG factorization-atlas / parallel-composition heuristic independently selected the right failure mechanism.

### Current unresolved targets

The external-search lane now prioritizes finite certificates that would still resolve explicitly open cases:

1. **Parnas--Ron--Shraibman `U_{3,20}`.** The 2019 conjecture predicts Boolean rank `9`; an `8`-rectangle all-one cover would refute it.
2. **Exceptional crown Kronecker cases.** The 2026 Parnas survey records `C_5 tensor C_5` and `C_6 tensor C_6` as the exceptional crown self-products not covered by the known strict-submultiplicativity theorem. Since `rank_B(C_5)=rank_B(C_6)=4`, a `15`-rectangle cover would establish strictness.

### Earlier source-pair augmentation dossier

The four-row Boolean, five-row binary, and unbounded Boolean source-pair results remain available in [`discoveries/source-pair-augmentation.md`](discoveries/source-pair-augmentation.md). They are secondary because the motivating 2018 wording “has two sources” admits an interpretive scope issue for the four-row example.

## Firewall

```text
EIG correctness --not a dependency--> finite certificate correctness
finite certificate correctness --not a dependency--> historical novelty / priority.
```

The Shitov correction is a concrete example of why this firewall is necessary.

## Explicitly open / conjectural

The following are **not** promoted as broad theorems here:

1. **WEIR in broad natural classes.** No general theorem yet derives response algebra, object/interface locus, maps, witnesses, Hom reconstruction, doctrine change, and descent in one package.
2. **Doctrine-internal interface selection.** A universal method selecting the right stable interfaces from interaction data alone is not known.
3. **General witness-enriched descent.** Multiplicity, provenance, cocycles, and higher coherence require more than scalar contextual quotients.
4. **One blind cross-domain extractor and unicity theorem.** The correct global theorem may be moduli-valued rather than literally unique.

## Curation boundary

The underlying research ledger contains many broader EIG branches. They are deliberately absent from this public core unless needed to state or test the foundational EIG claim. Newer does not imply public-ready.

## Verification boundary

`make verify` runs foundational regression. `make verify-discoveries` checks finite external certificates and the earlier source-pair dossier. A passing verifier supports the encoded finite claim; it does not establish historical novelty.

## Historical novelty boundary

Many EIG ingredients are established mathematics. This repository claims a dated formulation and research programme, not historical priority over classical ingredients. The binary-Kronecker headline was corrected immediately after locating Shitov's 2026-07-25 prior counterexample. Any future external-discovery priority claim requires a dedicated independent literature audit.
