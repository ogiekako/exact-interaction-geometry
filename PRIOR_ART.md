# Prior art and novelty boundary

EIG sits close to several mature traditions and several recent programmes. This note separates descriptions of cited sources from this repository's interpretation of their overlap with EIG.

A more detailed input/output comparison of the closest contemporary neighbours is in [`CONTEMPORARY_NEIGHBORS.md`](CONTEMPORARY_NEIGHBORS.md).

## 1. Syntactic monoids, algebras, and Myhill--Nerode theory

Two-sided contextual equivalence and response-minimal quotients are classical in automata and formal-language theory. For words and Boolean acceptance, `Syn(P,r)` specializes to the syntactic congruence/monoid. Weighted and algebraic variants provide many related minimization constructions.

**EIG does not claim contextual minimization itself as new.** The question is whether the same exact-continuation principle, with witness-sensitive enrichment, can serve as one component of a broader reconstruction theorem.

## 2. Behavioral systems and canonical state constructions

Behavioral systems theory is a particularly important precedent for the idea that state should be characterized by continuation rather than supplied as an arbitrary coordinate. A. A. Julius and A. J. van der Schaft, *State maps of general behaviors, their lattice structure and bisimulations* (MTNS 2004), studies lattices of dynamic/state maps, Nerode and dual-Nerode constructions, and conditions for canonical minimal state maps. Their companion *A behavioral framework for compositionality: linear systems, discrete event systems and hybrid systems* (MTNS 2004) treats system composition through behavioral interconnection and generalized projection.

We regard this as close to the `CONTEXT -> REDUCE -> COMPOSE` part of EIG. The comparison is interpretive: the behavioral system, signal/time structure, and interconnection setting are already supplied, whereas WEIR asks for a broader reconstruction of object loci, maps/Hom fibres, witness provenance, and local-to-global codescent from a common interaction laboratory.

## 3. Karoubi/Cauchy completion and Morita theory

Recovering typed corners `fPe` from idempotents of an untyped monoid/semigroup is the classical Karoubi construction. Cauchy completion and Morita theory already explain why presentations can determine categories only up to appropriate retract/completion equivalences.

**EIG does not claim idempotents-as-objects as new.** It uses this as a calibration and explicitly expects Cauchy/Morita moduli in any serious unicity theorem.

## 4. Arrow-only categories, consolidations, restriction semigroups, and Interaction Categories

Categories admit object-free/arrow-only presentations. Semigroup theory also studies the **consolidation** of a category: adjoin zero and send noncomposable products to zero. Restriction-semigroup and related constructions give exact correspondences in important classes.

Abramsky's **Interaction Categories** work beginning in 1993 is an additional important warning against broad terminology claims: interaction and process composition are central there, with specifications serving as objects and suitable processes as morphisms.

The theorem in [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) uses a classical consolidation shell. Its EIG role is narrower: freeze the observation to one-bit composition success, take its full two-sided contextual quotient, identify quotient classes with endpoint types, then retain the prequotient arrows as witness fibres to reconstruct Hom sets. EIG does not claim that categories of interacting processes are new.

## 5. Relations, Chu-style observation, allegories, ludics, and Geometry of Interaction

Relational/allegorical approaches make relations primary and recover maps internally. Chu spaces and related channel/observation formalisms organize systems through dual families of states/tests and an interaction or evaluation matrix. Girard's ludics makes interaction and orthogonality foundational. Geometry of Interaction and Seiller's Interaction Graphs study execution, measurement, orthogonality, and observational equivalence.

**EIG therefore does not claim “interaction is primitive”, “objects are determined by observations”, or “types arise by interaction” as unprecedented ideas.**

Representative references include Thomas Seiller, *Interaction Graphs: Additives*, arXiv:1205.6557, and the ludics literature on designs, interaction, and biorthogonality.

## 6. Isbell nuclei: especially close 2026 work

Juan Luis Gastaldi, Samantha Jarvis, Thomas Seiller, and John Terilla, *A calculus of types in Isbell nuclei*, arXiv:2606.03369 (2026), starts from execution and measurement and derives an orthogonality-generated type calculus through enriched Isbell nuclei.

This overlaps the broad EIG theme

```text
execution + measurement -> emergent types.
```

Accordingly, this repository does not claim novelty for that general idea. The remaining EIG target is broader: simultaneous reconstruction of response-minimal algebra, doctrine-relative interfaces/objects, internally selected maps, witness multiplicity/provenance, exact Hom/composition, doctrine change, and local-to-global descent.

## 7. Six Birds / Foundations of Emergence Calculus (Tsiokos 2026)

Ioannis Tsiokos, *Six Birds: Foundations of Emergence Calculus*, arXiv:2602.00134 (submitted 2026-01-28), is a contemporary neighbour and predates this public EIG snapshot. It studies composable processes under bounded observational access, lenses/refinement, idempotent completion/packaging, fixed-point objects, audit monotonicity, and route/holonomy defects.

The follow-up *To Lay a Stone with Six Birds: Finite-State Semantics for Packaging, Directionality, and Coarse-Graining*, DOI `10.20944/preprints202602.1699.v1` (posted 2026-02-27), describes a **no-smuggling** discipline in which externally declared quotients are disallowed, packaging equivalence is induced by an internal packaging endomap, and finite autonomous stochastic machines provide a substrate for the Six Birds primitives.

We regard these features as relevant prior art for parts of the EIG programme. In particular, it would be inaccurate to summarize Six Birds simply as “assuming the objects”. The distinction drawn here is narrower: an admissible family of deterministic observational maps/lenses remains part of that substrate, while WEIR asks whether exact interface/object/map structure and witness/Hom data can be derived from a more primitive interaction/response boundary.

Accordingly **EIG does not claim emergence by lenses, idempotent packaging, fixed-point objecthood, no-smuggling semantics, or route-mismatch/holonomy diagnostics as novel in the broad sense.**

## 8. Youvan 2026: stable quotients, admissibility, certified witnesses, and policy genesis

Douglas C. Youvan's 2026 object-formation / admissibility / ontogenesis sequence is recorded here as a possible close conceptual neighbour. The items below are recent author-uploaded works; this repository does not rely on them as independently peer-reviewed authority, and the comparison should be read as provisional unless the cited text is directly inspectable.

Relevant items include:

- *Object Formation and Conceptual Resolution: Stable Quotients, Complete Refinement Lattices, and Functorial Observation*, DOI `10.13140/RG.2.2.25921.72800`;
- *Local Observation and Global Objecthood: Sheaf Descent, Gluing Obstructions, and the Algebra of Distributed Concept Formation*, DOI `10.13140/RG.2.2.12748.99204`;
- *Admissibility Algebra: A Policy-Relative Foundation for Identity, Invariance, and Certified Transformation*, DOI `10.13140/RG.2.2.28510.40006`;
- *Admissibility Fibrations: Policy-Indexed Identity, Certified Quotients, and Lyapunov-Stable Emergence*, DOI `10.13140/RG.2.2.11130.25283`;
- *Categorical Neural Abiogenesis: Policy-Indexed Quotients, Functorial Compression, and Certified Memory in No-Corpus Artificial Intelligence*, DOI `10.13140/RG.2.2.36315.73765`;
- *Equivalence Genesis and Recursive Ontogenesis: Obstruction-Driven Identity Policies Beyond Homotopy Equivalence and Univalence*, DOI `10.13140/RG.2.2.17359.44968`.

At the level of the accessible descriptions reviewed for this repository, these works use related language concerning policy-relative quotienting, object formation, admissibility, certificates/witnesses, refinement, gluing, and obstruction-driven policy formation. We therefore record them as relevant conceptual neighbours and do **not** claim novelty for those broad themes merely because EIG reaches them from a different starting vocabulary.

The exact theorem-level overlap is not treated as settled here. In particular, this repository does not assert a formal equivalence between the Youvan constructions and EIG, nor does it rely on categorical phrases such as “direct prior art” or “very large overlap” as if they were facts stated by the cited sources.

The remaining EIG distinction is stated only as a current interpretation of the derivation boundary. In the formulations reviewed here, substantial structure appears to remain supplied or parameterized, including presentations/candidate transformations, policy or admissibility machinery, invariant languages, certificates/coherence, context/task structure, and in the algebraic line signatures and term syntax. We have not identified in the material reviewed a theorem that starts from one WEIR-style primitive interaction laboratory and one frozen rule and derives the entire package

```text
all-context exact contextual algebra
    + derived object/interface locus
    + internally selected maps
    + exact reopened-boundary witness provenance
    + cross-object Hom data and composition
    + doctrine change
    + intrinsic descent geometry
    + blind cross-domain recovery.
```

This is a bounded literature judgment, not a priority theorem. EIG's open target remains the simultaneous reconstruction of that package from a common interaction/continuation-response boundary, with blind calibration and explicit reconstruction moduli.

## 9. Algebraic Abiogenesis / Mathematical It from Bit (Youvan 2026)

Youvan's *Mathematical It from Bit: Algebraic Abiogenesis, Anonymous Finite Operations, and the Automated Birth of Abstract Algebra*, DOI `10.13140/RG.2.2.25987.26403`, and the public repository `DougYouvan/algebraic-abiogenesis` are relevant to the algebraic sector.

The accessible description begins with an anonymous finite signature, finite operation tables, and a free term algebra, then organizes terms extensionally across finite models. We regard this as an operation-first reconstruction precedent that is close in spirit to EIG's contextual reduction.

The supplied structure is still substantial: a signature, term syntax, variable set, and family of finite algebras. The output is an equational/free-algebra world rather than the full doctrine-relative interface/map/Hom/witness/descent package targeted by WEIR. EIG therefore does not claim that anonymous operations can first be observed extensionally and only later organized into quotient algebraic objects as an unprecedented idea.

## 10. Predictive quotients and fibre fingerprints (Wang 2026)

Qinyou Wang, *Fiber Fingerprints of Hidden Learning-State Dynamics*, arXiv:2608.15976 (submitted 2026-08-17), gives a particularly close future-context construction. A declared category of execution contexts, a state functor, a probe doctrine, and response maps induce predictive equivalence by equality under **all declared future probes**. The resulting quotient is a congruence, descends functorially, and satisfies a Nerode-type minimality theorem. The paper also studies set-level predictive fibres and richer conditional realizations.

We regard this as relevant prior art for the specific claim that all-future-response equivalence can canonically produce a minimal predictive quotient and retain informative fibre structure. The distinction is that the execution-context category, state functor, protocols, present readout, and probe doctrine are supplied. EIG's open WEIR target asks when the relevant interface/object/map structure itself is forced downstream of a more primitive interaction laboratory, with exact cross-Hom and witness descent.

## 11. Two-state max-plus comparison

Max-plus and tropical weighted automata are classical, as are projective normalization, one-counter languages, Parikh semilinearity, and Presburger arithmetic. None of those ingredients is claimed new.

The relevant published problem begins with:

- Laure Daviaud, Pierre Guillon, Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19`.

They prove bounded-state comparison undecidable at 553 states and explicitly ask what happens from 2 through 552 states, noting that even two states appears difficult. The manuscript in [`discoveries/two-state-maxplus-comparison.md`](discoveries/two-state-maxplus-comparison.md) proves the `d=2` case and in fact allows the left-hand automaton to be arbitrary.

The closest same-model two-state work identified in the review is:

- Laure Daviaud, Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48`.

That paper studies identities of the full two-state class, not positivity or pointwise comparison. Structural `2 x 2` tropical-matrix semigroup literature is likewise relevant background; the targeted review did not identify an equivalent containment theorem.

Broader containment and decision-problem references checked include:

- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2`;
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651`;
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, LICS 2023 / arXiv:2304.05229.

The Big-O theorem concerns affine domination rather than exact containment. Positive results for finitely ambiguous automata do not cover arbitrary two-state automata because state count does not bound ambiguity.

The 2026 tropical/min-plus decision literature was also reviewed. In particular, Almagor--Arbel--Sheinvald decide **determinisability** and study its complexity, unambiguisability, and register minimisation; those results do not say that every two-state weighted automaton is determinisable. The 2026 one-letter representation theorem fixes alphabet size rather than state count. Nearby few-register cost-register-automata results use different model restrictions and decision problems.

The dated review is recorded in [`provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md). Its conclusion is deliberately bounded:

```text
DGM 2017 statement leaving d=2 in the open range: supported by cited source
prior resolution identified: no, in targeted review through 2026-09-01
absolute historical firstness: not claimed
```

Accordingly the public claim is the **proved two-state comparison theorem and its `d=2` consequence for the stated DGM 2017 question**, together with the bounded statement that the targeted review did not identify a prior resolution. This is not a blanket claim of historical priority over every unpublished or differently indexed source.

## 12. Boolean Tucker decomposition — retired calibration

Boolean tensor factorization, including Boolean Tucker decomposition, is established prior work. A basic reference is:

- Pauli Miettinen, *Boolean Tensor Factorizations*, ICDM 2011, DOI `10.1109/ICDM.2011.28`.

A 2026-08-31 EIG search lane produced a finite Boolean Tucker rank-profile incompatibility example by asking whether independently minimal Boolean unfolding ranks must always be jointly realizable by one exact Tucker core. The finite example may be mathematically correct, but the curation review did not identify a published conjecture or problem asserting that universal property. The item was therefore removed from the current public theorem/case-study surface on 2026-09-02 so that the word “counterexample” could not be mistaken for a documented external conjecture resolution.

The material remains in Git history as research provenance/calibration only. No historical priority, external problem resolution, or EIG novelty claim is made for it.

## 13. Binary-rank Kronecker nonmultiplicativity: Shitov 2026

An important priority correction for the external-search lane is:

- Yaroslav Shitov, *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted **2026-07-25**, DOI `10.13140/RG.2.2.26449.90723`.

The cited preprint gives an explicit `5 x 5` binary matrix `B` with

```text
rank_01(B) = 5,
rank_01(B tensor B) <= 24 < 25.
```

The EIG search lane separately found a different `5 x 5` `5 -> 24` example on 2026-08-31. Its public finite certificate is retained, but **binary-rank Kronecker nonmultiplicativity is not presented as an EIG novelty claim**. The EIG example is a calibration of the parallel-composition search heuristic.

## 14. Arity/nerve and generic reconstruction machinery

Yoneda density, presheaf reconstruction, monads with arities, nervous monads, Grothendieck constructions, profunctors/equipments, sheaves/stacks, and descent theory provide powerful generic reconstruction shells.

EIG may use these as representation machinery. It must not count their existence as evidence that the **correct process-generated or interaction-generated arities were derived rather than supplied**.

## What remains distinctive in the present EIG formulation

After these exclusions, the strongest current EIG target is not any single slogan above. It is the simultaneous package formalized as WEIR:

```text
raw execution / admitted continuation response
        -> exact contextual algebra
        -> doctrine-relative interfaces / objecthood
        -> internally characterized maps
        -> witness multiplicity / provenance
        -> exact Hom and composition reconstruction
        -> doctrine refinement
        -> intrinsic descent / obstruction geometry
        -> blind calibration in distant domains under one frozen rule.
```

Several neighbouring theories cover important parts of this chain. **No claim is made here that an exhaustive historical search has proved the whole package unique.** In the literature reviewed for this snapshot, we did not identify a source proving this exact entire-package reconstruction from one frozen interaction laboratory without supplying the target object/map world or equivalent domain structure.

## Novelty policy

A result enters the EIG public core only if its statement separates:

1. the classical theorem being used;
2. the new operational interpretation or bridge, if any;
3. the exact project-specific statement;
4. what remains conjectural;
5. whether historical novelty has actually been checked.

At this snapshot, no blanket claim that EIG is a historically new foundation or established field is made. Literature descriptions and EIG's own comparison judgments should remain visibly distinct, and dated searches are not treated as certificates of historical firstness.