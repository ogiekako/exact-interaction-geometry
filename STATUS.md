# Status and epistemic boundary

Snapshot: **2026-09-01 JST**

This file is intentionally conservative. It records only claims appropriate for the public EIG surface.

Status vocabulary used here:

- **PROVED / PUBLIC** — the current public tree contains the proof or a directly checkable finite certificate/regression, as appropriate;
- **LEDGER-AUDITED / PUBLIC PROOF NOT IMPORTED** — the research ledger records an audit, but a third party cannot reproduce that audit from this repository alone;
- **OPEN / CONJECTURAL** — not promoted as a theorem.

## External theorem: two-state max-plus comparison

Let `A` be an arbitrary finite max-plus automaton over `Z_max`, and let `B` have at most two states. The current public theorem note proves that pointwise containment

```text
[[A]] <= [[B]]
```

is decidable. Consequently comparison/equivalence of two two-state max-plus automata and two-state positivity `Pos_2^k(Z_max)` are decidable for every finite alphabet size `k`.

The proof passes through an exact projective normal form. Beyond an explicit finite threshold, the unique unbounded two-state projective gap satisfies a retain/read dichotomy: a letter may retain the gap with gap-independent output increment, or read its magnitude into the output while erasing it from the successor state, but cannot do both. This yields an exact one-counter transducer, after which effective Parikh semilinearity reduces containment failure to Presburger arithmetic.

Publication posture:

```text
mathematical statement                 PROVED / PUBLIC
published d=2 open-case match          CONFIRMED against DGM 2017
fresh public finite regression         PASS
earlier independent ledger audit       PASS
prior resolution found through 2026-09-01   NO
absolute historical firstness          NOT CERTIFIED
```

Daviaud--Guillon--Merlet, MFCS 2017, explicitly leave the bounded-state range from 2 through 552 open after proving undecidability at 553 states. The theorem here closes the `d=2` endpoint and is stronger in one direction because only the right-hand automaton is required to have at most two states.

A targeted primary-source and current-literature audit through 2026-09-01 located no earlier two-state comparison/positivity theorem and no equivalent arbitrary-left/two-state-right containment or one-counter compilation. Bibliographic search cannot prove historical absence, so the repository does not use an unqualified `first known` claim.

Public files:

- [`discoveries/two-state-maxplus-comparison.md`](discoveries/two-state-maxplus-comparison.md)
- [`verification/verify_two_state_maxplus.py`](verification/verify_two_state_maxplus.py)
- [`provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md)

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

## Second external case study: Boolean Tucker junction failure

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

The source-pair material remains secondary because the motivating published wording admits an interpretive scope issue. Exact finite examples are retained for provenance, not used as the top-level external theorem.

## Firewall

```text
EIG correctness --not a dependency--> external theorem/counterexample correctness
external mathematical correctness --not a dependency--> historical novelty / priority.
```

## Explicitly open / conjectural

The following are **not** promoted as broad theorems here:

1. **WEIR in broad natural classes.** No general theorem yet derives response algebra, object/interface locus, maps, witnesses, Hom reconstruction, doctrine change, and descent in one package.
2. **Doctrine-internal interface selection.** A universal method selecting the right stable interfaces from interaction data alone is not known.
3. **General witness-enriched descent.** Multiplicity, provenance, cocycles, and higher coherence require more than scalar contextual quotients.
4. **One blind cross-domain extractor and unicity theorem.** The correct global theorem may be moduli-valued rather than literally unique.

## Verification boundary

`make verify` runs foundational regression. `make verify-discoveries` runs the two-state max-plus public regression together with the Boolean Tucker case study and the retained finite calibrations/examples.

For the max-plus theorem, the checker independently verifies closed formulas, the tail retain/read dichotomy on a complete finite letter family, and hundreds of thousands of end-to-end direct-versus-compiled word evaluations. These are regressions for the written infinite proof; finite testing is not being used as a substitute for the one-counter/Parikh argument.

A passing verifier does not establish historical novelty.

## Historical novelty boundary

Many EIG ingredients are established mathematics. Max-plus automata, projective normalization, one-counter languages, Parikh's theorem, and Presburger arithmetic are classical ingredients. The public claim is the exact composition of these ingredients into the two-state right-hand comparison theorem and its `d=2` open-case consequence, under the dated novelty audit above.

Boolean Tucker decomposition is prior work; nonnegative Tucker literature already contains non-field-like minimum-rank phenomena; and semilattice flatness/distributivity is classical. The Boolean public claim remains the explicit exact junction counterexample and its independently checkable rank region.
