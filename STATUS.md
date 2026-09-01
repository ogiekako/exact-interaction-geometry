# Status and epistemic boundary

Snapshot: **2026-09-01 JST**

This file is intentionally conservative. It records only claims appropriate for the public EIG surface.

Status vocabulary used here:

- **PUBLIC PROOF / CERTIFICATE AVAILABLE** — the current public tree contains the proof or a directly checkable finite certificate/regression, as appropriate;
- **PRIVATE / NOT PUBLICLY VERIFIABLE** — an internal research note records an observation, but the proof/checker is not present in this repository and the observation is not relied upon for public theorem claims;
- **OPEN / CONJECTURAL** — not promoted as a theorem.

## External theorem: two-state max-plus comparison

Let `A` be an arbitrary finite max-plus automaton over `Z_max`, and let `B` have at most two states. The current public theorem note proves that pointwise containment

```text
[[A]] <= [[B]]
```

is decidable. Consequently comparison/equivalence of two two-state max-plus automata and two-state positivity `Pos_2^k(Z_max)` are decidable for every finite alphabet size `k`.

The proof passes through an exact projective normal form. Beyond an explicit finite threshold, the unique unbounded two-state projective gap has a three-way tail classification: **propagate**, **forget**, or **read-and-forget**. Propagation has gap-independent output increment; silent forgetting also has gap-independent output increment; and only read-and-forget makes the output depend on the unbounded magnitude. Thus a transition cannot both read an unbounded magnitude into the output and preserve it for future computation. This yields an exact functional one-counter transducer, after which effective Parikh semilinearity reduces containment failure to Presburger arithmetic.

Public-evidence posture:

```text
mathematical statement                 public proof available
DGM 2017 leaves d=2 in stated open range   supported by cited source
fresh public finite regression         accompanying regression available
separate model-assisted adversarial review  internal process record only
prior resolution identified through 2026-09-01   no, in targeted literature review
absolute historical firstness          not claimed
```

Daviaud--Guillon--Merlet, MFCS 2017, explicitly leave the bounded-state range from 2 through 552 open after proving undecidability at 553 states. The manuscript here proves the `d=2` case of that published question and is stronger in one direction because only the right-hand automaton is required to have at most two states.

A targeted primary-source and current-literature review through 2026-09-01 did not identify an earlier two-state comparison/positivity theorem or an equivalent arbitrary-left/two-state-right containment or one-counter compilation. Bibliographic search cannot prove historical absence, so the repository does not use an unqualified `first known` claim.

Public files:

- [`discoveries/two-state-maxplus-comparison.md`](discoveries/two-state-maxplus-comparison.md)
- [`verification/verify_two_state_maxplus.py`](verification/verify_two_state_maxplus.py)
- [`provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md)

## Foundation core and public-evidence status

| Claim | Status | Novelty posture |
| --- | --- | --- |
| contextual equality of finite response rows gives the unique coarsest deterministic exact interface | **PUBLIC PROOF AVAILABLE** | elementary / classical minimization pattern |
| semiring witness factor rank obeys serial data processing and parallel submultiplicativity | **PUBLIC PROOF AVAILABLE** | classical factorization algebra; EIG interpretation is organizational |
| two-sided syntactic interaction quotient is composition-stable and response-minimal | **PUBLIC PROOF AVAILABLE** | classical syntactic-algebra core |
| idempotent splitting gives typed interaction categories | **PUBLIC PROOF AVAILABLE** | classical Karoubi/Cauchy core; concise construction proof in `FOUNDATIONS.md` |
| changing the response doctrine can change the derived object spectrum | **PRIVATE / NOT PUBLICLY VERIFIABLE** | internal observation only; not relied upon for any public theorem claim |
| every small category is exactly reconstructible from its untyped consolidation, one-bit composition success, and retained raw-arrow witness fibres | **PUBLIC PROOF AVAILABLE** | classical consolidation ingredients; EIG operational recognition formulation |
| exact category reconstruction does not imply ULF/Conduche factorization | **PUBLIC PROOF AVAILABLE** | boundary theorem |

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

Public-evidence posture: **public finite counterexample and accompanying solver-free checker; no historical `first` claim.**

The EIG relevance is the question that selected the phenomenon: independently minimal exact interfaces need not jointly descend through one common junction witness.

### Unpublished structural follow-up

An internal research note explores structural refinements of the Boolean Tucker example, including a reduced-separator classification and a small obstruction pattern. The proof/checker for that follow-up is not included in this repository.

Public-evidence posture: **PRIVATE / NOT PUBLICLY VERIFIABLE.** These observations are not part of the public theorem record and are not required for the Boolean Tucker counterexample above.

The internal notes also distinguish the following points, which are not promoted here as public results:

- classical abstract semilattice flatness/distributivity is prior art;
- a broader universal bridge from the reduced analysis to unrestricted Boolean Tucker structure remains unresolved.

## External-search calibrations and candidates

### Binary rank under Kronecker product — calibration only

The repository retains a separately found `5 x 5` `5 -> 24` binary-rank example, but the nonmultiplicativity theorem is not novel to this project. Yaroslav Shitov publicly posted a different `5 x 5` example on 2026-07-25. Public posture: **project rediscovery / no priority claim.**

### Current unresolved search targets

The private search lane currently includes finite-certificate targets such as:

1. Parnas--Ron--Shraibman `U_{3,20}`: an `8`-rectangle Boolean cover would refute the conjectured rank `9`;
2. `C_5 tensor C_5` and `C_6 tensor C_6`: `15`-rectangle covers would settle the exceptional crown self-product cases strictly.

These are not public results unless a new public certificate or proof is produced.

### Earlier source-pair augmentation dossier

The source-pair material remains secondary because the motivating published wording admits an interpretive scope issue. Exact finite examples are retained for provenance, not used as the top-level external theorem.

## Separation of claim types

```text
EIG foundational claims are assessed on their own public proofs/statements.
External theorem/counterexample correctness is assessed on its own proof or certificate.
Historical novelty and priority are separate literature questions.
```

## Explicitly open / conjectural

The following are **not** promoted as broad theorems here:

1. **WEIR in broad natural classes.** No general theorem yet derives response algebra, object/interface locus, maps, witnesses, Hom reconstruction, doctrine change, and descent in one package.
2. **Doctrine-internal interface selection.** A universal method selecting the right stable interfaces from interaction data alone is not known.
3. **General witness-enriched descent.** Multiplicity, provenance, cocycles, and higher coherence require more than scalar contextual quotients.
4. **One blind cross-domain extractor and unicity theorem.** The correct global theorem may be moduli-valued rather than literally unique.

## Verification boundary

`make verify` runs foundational regression. `make verify-discoveries` runs the two-state max-plus public regression together with the Boolean Tucker case study and the retained finite calibrations/examples.

For the max-plus theorem, the checker separately checks closed formulas, the propagate/forget/read-and-forget tail trichotomy on a complete finite letter family (including the all-zero silent-forget case), and hundreds of thousands of end-to-end direct-versus-compiled word evaluations. These are regressions for the written infinite proof; finite testing is not being used as a substitute for the functional one-counter/Parikh argument.

A passing verifier does not establish historical novelty.

## Historical novelty boundary

Many EIG ingredients are established mathematics. Max-plus automata, projective normalization, one-counter languages, Parikh's theorem, and Presburger arithmetic are classical ingredients. The public claim is the exact composition of these ingredients into the two-state right-hand comparison theorem and its `d=2` consequence for the DGM 2017 question, with historical priority stated only at the bounded scope of the dated literature review above.

Boolean Tucker decomposition is prior work; nonnegative Tucker literature already contains non-field-like minimum-rank phenomena; and semilattice flatness/distributivity is classical. The Boolean public claim remains the explicit exact junction counterexample and its publicly checkable rank region.
