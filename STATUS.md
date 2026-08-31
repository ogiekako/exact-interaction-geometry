# Status and epistemic boundary

Snapshot: **2026-08-31 JST**

This file is intentionally conservative. It records only claims appropriate for the public EIG surface.

Status vocabulary used here:

- **PROVED / PUBLIC** — the current public tree contains the proof or a directly checkable finite certificate, as appropriate;
- **LEDGER-AUDITED / PUBLIC PROOF NOT IMPORTED** — the private research ledger records an audit, but a third party cannot reproduce that audit from this repository alone;
- **OPEN / CONJECTURAL** — not promoted as a theorem.

## Foundation core and public-evidence status

| Claim | Status | Novelty posture |
| --- | --- | --- |
| contextual equality of finite response rows gives the unique coarsest deterministic exact interface | **PROVED / PUBLIC** | elementary / classical minimization pattern |
| semiring witness factor rank obeys serial data processing and parallel submultiplicativity | **PROVED / PUBLIC** | classical factorization algebra; EIG interpretation is organizational |
| two-sided syntactic interaction quotient is composition-stable and response-minimal | **PROVED / PUBLIC** | classical syntactic-algebra core |
| idempotent splitting gives typed interaction categories | **PROVED / PUBLIC** | classical Karoubi/Cauchy core; concise construction proof in `FOUNDATIONS.md` |
| changing the response doctrine can change the derived object spectrum | **LEDGER-AUDITED / PUBLIC PROOF NOT IMPORTED** | retained as programme provenance, not a public theorem claim |
| every small category is exactly reconstructible from its untyped consolidation, one-bit composition success, and retained raw-arrow witness fibres | **PROVED / PUBLIC** | classical consolidation ingredients; EIG operational recognition formulation |
| exact category reconstruction does not imply ULF/Conduche factorization | **PROVED / PUBLIC** | boundary theorem |

## External case study: Boolean Tucker junction failure

The clearest current external case study is an explicit exact Boolean Tucker incompatibility.

For the `2 x 4 x 4` tensor in [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md), the three mode-unfolding Boolean ranks are

```text
(2,3,3),
```

but profile `(2,3,3)` is not jointly realizable by one exact Boolean Tucker core. The displayed tensor has exact feasible profile region

```text
Tuck_B(T) = Up(2,3,4) union Up(2,4,3)
```

where `Up(p,q,r)` denotes the componentwise upward closure.

The public checker exhausts every nonzero support mask on each mode, derives the mode ranks and unique minimum bases without a normalization lemma, checks the four blocking zeros, exhausts every distinct nonzero first-arm support family to rule out all profiles with the two other arms fixed at rank three, verifies the two Pareto profiles, and checks a same-shape same-mode-ranks tensor for which `(2,3,3)` is feasible.

Publication posture: **PROVED / PUBLIC FINITE COUNTEREXAMPLE; NO HISTORICAL `FIRST` CLAIM.**

The EIG relevance is the question that selected the phenomenon: independently minimal exact interfaces need not jointly descend through one common junction witness.

### Structural follow-up in the research ledger

A later reduced-separator theorem in the private research ledger identifies two first rank-three strict-gap separator types `F` and `T`, enumerates the `FF/FT/TF/TT` fiber-versus-tensor holes, and gives a common three-zero hook certificate. A distributive separator semilattice is sufficient for joint descent in the concrete finite setting proved there.

Public-evidence posture: **LEDGER-AUDITED / PUBLIC PROOF NOT IMPORTED.** These statements are useful provenance and motivation but are not required for the public Boolean Tucker counterexample.

The ledger also keeps two broader points separate:

- classical abstract semilattice flatness/distributivity is prior art, not an EIG novelty;
- the universal identification needed to turn the reduced F/T theorem into an unrestricted all-Tucker converse remains a reduced/open bridge.

## External-search calibrations and candidates

### Binary rank under Kronecker product — calibration only

The repository retains a correct independently found `5 x 5` `5 -> 24` binary-rank example, but the nonmultiplicativity theorem is not novel to this project. Yaroslav Shitov publicly posted a different `5 x 5` example on 2026-07-25. Publication posture: **CORRECT REDISCOVERY / NO PRIORITY CLAIM.**

### Current unresolved search targets

The private search lane currently includes finite-certificate targets such as:

1. Parnas--Ron--Shraibman `U_{3,20}`: an `8`-rectangle Boolean cover would refute the conjectured rank `9`;
2. `C_5 tensor C_5` and `C_6 tensor C_6`: `15`-rectangle covers would settle the exceptional crown self-product cases strictly.

These are not public results unless a new independently checked certificate is found.

### Earlier source-pair augmentation dossier

The source-pair material remains secondary because the motivating published wording admits an interpretive scope issue. Exact finite examples are retained for provenance, not used as the top-level external case study.

## Firewall

```text
EIG correctness --not a dependency--> finite counterexample correctness
finite counterexample correctness --not a dependency--> historical novelty / priority.
```

## Explicitly open / conjectural

The following are **not** promoted as broad theorems here:

1. **WEIR in broad natural classes.** No general theorem yet derives response algebra, object/interface locus, maps, witnesses, Hom reconstruction, doctrine change, and descent in one package.
2. **Doctrine-internal interface selection.** A universal method selecting the right stable interfaces from interaction data alone is not known.
3. **General witness-enriched descent.** Multiplicity, provenance, cocycles, and higher coherence require more than scalar contextual quotients.
4. **One blind cross-domain extractor and unicity theorem.** The correct global theorem may be moduli-valued rather than literally unique.

## Verification boundary

`make verify` runs foundational regression. `make verify-discoveries` checks the Boolean Tucker case study and the finite calibration/examples retained in this public tree. A passing verifier supports the encoded finite claim; it does not establish historical novelty.

The category reconstruction regression constructs the contextual quotient, quotient multiplication, object idempotents, source/target object classes, identity witnesses, and Hom fibres from the untyped interaction data before comparing them with the hidden fixture labels.

## Historical novelty boundary

Many EIG ingredients are established mathematics. Boolean Tucker decomposition is prior work; nonnegative Tucker literature already contains non-field-like minimum-rank phenomena; and semilattice flatness/distributivity is classical. The public claim here is deliberately narrower: an explicit exact Boolean Tucker junction counterexample is given together with a small checker and the EIG question that led to it.
