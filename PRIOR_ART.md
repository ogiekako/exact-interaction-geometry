# Prior art and novelty boundary

EIG sits close to several mature traditions and several unusually close 2026 programmes. This is not peripheral bibliography: these theories define the boundary of what the programme may honestly claim.

A more detailed input/output comparison of the closest contemporary neighbours is in [`CONTEMPORARY_NEIGHBORS.md`](CONTEMPORARY_NEIGHBORS.md).

## 1. Syntactic monoids, algebras, and Myhill--Nerode theory

Two-sided contextual equivalence and response-minimal quotients are classical in automata and formal-language theory. For words and Boolean acceptance, `Syn(P,r)` specializes to the syntactic congruence/monoid. Weighted and algebraic variants provide many related minimization constructions.

**EIG does not claim contextual minimization itself as new.** The question is whether the same exact-continuation principle, with witness-sensitive enrichment, can serve as one component of a broader reconstruction theorem.

## 2. Behavioral systems and canonical state constructions

Behavioral systems theory is a particularly important precedent for the idea that state should be characterized by continuation rather than supplied as an arbitrary coordinate. A. A. Julius and A. J. van der Schaft, *State maps of general behaviors, their lattice structure and bisimulations* (MTNS 2004), studies lattices of dynamic/state maps, Nerode and dual-Nerode constructions, and conditions for canonical minimal state maps. Their companion *A behavioral framework for compositionality: linear systems, discrete event systems and hybrid systems* (MTNS 2004) treats system composition through behavioral interconnection and generalized projection.

This is close to the `CONTEXT -> REDUCE -> COMPOSE` part of EIG. It does **not** make the full EIG package new: the behavioral system, signal/time structure, and interconnection setting are already supplied, and the programme is not a reconstruction of general object loci, maps/Hom fibres, witness provenance, and local-to-global codescent from one raw interaction laboratory.

## 3. Karoubi/Cauchy completion and Morita theory

Recovering typed corners `fPe` from idempotents of an untyped monoid/semigroup is the classical Karoubi construction. Cauchy completion and Morita theory already explain why presentations can determine categories only up to appropriate retract/completion equivalences.

**EIG does not claim idempotents-as-objects as new.** It uses this as a calibration and explicitly expects Cauchy/Morita moduli in any serious unicity theorem.

## 4. Arrow-only categories, consolidations, restriction semigroups, and Interaction Categories

Categories admit object-free/arrow-only presentations. Semigroup theory also studies the **consolidation** of a category: adjoin zero and send noncomposable products to zero. Restriction-semigroup and related constructions give exact correspondences in important classes.

Samson Abramsky's **Interaction Categories** programme (1993--1990s) is an additional important warning against broad terminology claims: interaction and process composition are central there, with specifications serving as objects and suitable processes as morphisms.

The theorem in [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) uses a classical consolidation shell. Its EIG role is narrower: freeze the observation to one-bit composition success, take its full two-sided contextual quotient, identify quotient classes with endpoint types, then retain the prequotient arrows as witness fibres to reconstruct Hom sets. EIG does not claim that categories of interacting processes are new.

## 5. Relations, Chu-style observation, allegories, ludics, and Geometry of Interaction

Relational/allegorical approaches make relations primary and recover maps internally. Chu spaces and related channel/observation formalisms organize systems through dual families of states/tests and an interaction or evaluation matrix. Girard's ludics makes interaction and orthogonality foundational. Geometry of Interaction and Seiller's Interaction Graphs study execution, measurement, orthogonality, and observational equivalence.

**EIG therefore does not claim “interaction is primitive”, “objects are determined by observations”, or “types arise by interaction” as unprecedented ideas.**

Representative references include Thomas Seiller, *Interaction Graphs: Additives*, arXiv:1205.6557, and the ludics literature on designs, interaction, and biorthogonality.

## 6. Isbell nuclei: especially close 2026 work

Juan Luis Gastaldi, Samantha Jarvis, Thomas Seiller, and John Terilla, *A calculus of types in Isbell nuclei*, arXiv:2606.03369 (2026), starts from execution and measurement and derives an orthogonality-generated type calculus through enriched Isbell nuclei.

This directly blocks any EIG novelty claim of the form

```text
execution + measurement -> emergent types.
```

The remaining EIG target is broader: simultaneous reconstruction of response-minimal algebra, doctrine-relative interfaces/objects, internally selected maps, witness multiplicity/provenance, exact Hom/composition, doctrine change, and local-to-global descent.

## 7. Six Birds / Foundations of Emergence Calculus (Tsiokos 2026)

Ioannis Tsiokos, *Six Birds: Foundations of Emergence Calculus*, arXiv:2602.00134 (submitted 2026-01-28), is a close contemporary neighbour and predates this public EIG snapshot. It studies composable processes under bounded observational access, lenses/refinement, idempotent completion/packaging, fixed-point objects, audit monotonicity, and route/holonomy defects.

The follow-up *To Lay a Stone with Six Birds: Finite-State Semantics for Packaging, Directionality, and Coarse-Graining*, DOI `10.20944/preprints202602.1699.v1` (posted 2026-02-27), is closer still. It explicitly adopts a **no-smuggling** discipline: externally declared quotients are disallowed, packaging equivalence is induced by an internal packaging endomap, and finite autonomous stochastic machines provide a canonical substrate for the Six Birds primitives.

This materially overlaps EIG and must be cited. The current technical distinction is not that Six Birds merely “assumes objects”. In its no-smuggling substrate, objects are fixed points of internally induced packaging. The remaining difference is that an admissible family of deterministic observational maps/lenses is still part of the substrate, and the programme does not presently reconstruct the EIG package of all-context exact interfaces, internally selected maps, cross-object Hom fibres, and witness multiplicity/provenance from raw execution/response alone.

Accordingly **EIG does not claim emergence by lenses, idempotent packaging, fixed-point objecthood, no-smuggling semantics, or route-mismatch/holonomy diagnostics as novel in the broad sense.**

## 8. Youvan 2026: stable quotients, admissibility, certified witnesses, and policy genesis

Douglas C. Youvan's 2026 object-formation / admissibility / ontogenesis sequence is a close contemporary neighbour and materially overlaps several WEIR gates. Relevant papers include:

- *Object Formation and Conceptual Resolution: Stable Quotients, Complete Refinement Lattices, and Functorial Observation*, DOI `10.13140/RG.2.2.25921.72800`;
- *Local Observation and Global Objecthood: Sheaf Descent, Gluing Obstructions, and the Algebra of Distributed Concept Formation*, DOI `10.13140/RG.2.2.12748.99204`;
- *Admissibility Algebra: A Policy-Relative Foundation for Identity, Invariance, and Certified Transformation*, DOI `10.13140/RG.2.2.28510.40006`;
- *Admissibility Fibrations: Policy-Indexed Identity, Certified Quotients, and Lyapunov-Stable Emergence*, DOI `10.13140/RG.2.2.11130.25283`;
- *Categorical Neural Abiogenesis: Policy-Indexed Quotients, Functorial Compression, and Certified Memory in No-Corpus Artificial Intelligence*, DOI `10.13140/RG.2.2.36315.73765`;
- *Equivalence Genesis and Recursive Ontogenesis: Obstruction-Driven Identity Policies Beyond Homotopy Equivalence and Univalence*, DOI `10.13140/RG.2.2.17359.44968`.

The distributed-objecthood construction is direct prior art for policy-relative quotient objecthood, generated globalization, faithful descent, gluing defects, and explicit obstruction witnesses.

The later admissibility work strengthens the overlap substantially. *Admissibility Algebra* treats presentations, candidate transformations, policies, admissibility selectors, invariants, certificates, and coherence laws as foundational ingredients. *Admissibility Fibrations* develops policy-indexed identity and certified quotients in a proof-relevant setting where certificate spaces can retain multiple witnesses and higher coherence, and where policy refinement induces functorial comparison between identity doctrines. Therefore **proof-relevant witnesses, policy-indexed objecthood, and functorial doctrine/policy refinement are not EIG novelty claims in isolation.**

*Categorical Neural Abiogenesis* likewise keeps quotient objects together with governing policies, certificates/witnesses, countermodels, canonical representatives, known failure conditions, and coherence information in certified memory. It is therefore too strong to characterize the Youvan programme generically as a set-quotient theory that erases provenance or witness structure.

Finally, *Equivalence Genesis and Recursive Ontogenesis* explicitly treats policy formation itself as endogenous to failure analysis. Its core mechanism is obstruction-driven identity-policy formation: failed equivalences generate obstructions, obstructions induce invariants, invariants induce new policies, and new policies induce new objecthood. Thus **obstruction-driven policy generation itself is also prior art** and cannot serve as a generic firewall for EIG.

The remaining EIG distinction is narrower and should be stated at the derivation boundary. In the cited Youvan formalisms, substantial structure remains primitive or parameterized: universes of presentations and candidate transformations, policy/admissibility machinery, invariant languages, certificates/coherence, task/context structure, and in the algebraic line signatures and term syntax. The current audit has not identified there a theorem deriving, from one WEIR-style primitive interaction laboratory and one rule frozen in advance, the entire package

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

Accordingly EIG does **not** claim stable quotient objecthood, policy-indexed identity, certified quotient/witness spaces, functorial policy refinement, gluing obstruction theory, or obstruction-driven policy genesis as unprecedented. Its open target is the **simultaneous reconstruction of the full package from a common interaction/continuation-response boundary, with blind calibration and explicit reconstruction moduli**.

## 9. Algebraic Abiogenesis / Mathematical It from Bit (Youvan 2026)

Youvan's *Mathematical It from Bit: Algebraic Abiogenesis, Anonymous Finite Operations, and the Automated Birth of Abstract Algebra*, DOI `10.13140/RG.2.2.25987.26403`, and the public repository `DougYouvan/algebraic-abiogenesis` are especially relevant to the algebraic sector.

The formalism begins with an anonymous finite signature, finite operation tables, and a free term algebra. Exact equality of term functions across the finite model ecology defines a fully invariant congruence; quotienting the term algebra by that congruence produces algebraic objects and operations. The methodology then uses countermodels, basis compression, and structural maturation.

This is a real **operation-first reconstruction** precedent. Its exact term-function congruence is close in spirit to EIG's contextual reduction. It nevertheless starts with a supplied signature, term syntax, variable set, and family of finite algebras, and it reconstructs an equational/free-algebra world rather than the full doctrine-relative interface/map/Hom/witness/descent package targeted by WEIR.

EIG therefore does not claim that anonymous operations can first be observed extensionally and only later organized into quotient algebraic objects as an unprecedented idea.

## 10. Predictive quotients and fibre fingerprints (Wang 2026)

Qinyou Wang, *Fiber Fingerprints of Hidden Learning-State Dynamics*, arXiv:2608.15976 (submitted 2026-08-17), gives a particularly close future-context construction. A declared category of execution contexts, a state functor, a probe doctrine, and response maps induce predictive equivalence by equality under **all declared future probes**. The resulting quotient is a congruence, descends functorially, and satisfies a Nerode-type minimality theorem. The paper also studies set-level predictive fibres and richer conditional realizations.

This is strong prior art for the claim that all-future-response equivalence can canonically produce a minimal predictive quotient and retain informative fibre structure. The distinction is that the execution-context category, state functor, protocols, present readout, and probe doctrine are supplied. EIG's open WEIR target asks when the relevant interface/object/map structure itself is forced downstream of a more primitive interaction laboratory, with exact cross-Hom and witness descent.

## 11. Two-state max-plus comparison

Max-plus and tropical weighted automata are classical, as are projective normalization, one-counter languages, Parikh semilinearity, and Presburger arithmetic. None of those ingredients is claimed new.

The relevant published problem begins with:

- Laure Daviaud, Pierre Guillon, Glenn Merlet, *Comparison of Max-Plus Automata and Joint Spectral Radius of Tropical Matrices*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.19`.

They prove bounded-state comparison undecidable at 553 states and explicitly ask what happens from 2 through 552 states, noting that even two states appears difficult. The theorem in [`discoveries/two-state-maxplus-comparison.md`](discoveries/two-state-maxplus-comparison.md) closes the `d=2` endpoint and in fact allows the left-hand automaton to be arbitrary.

The closest same-model two-state work found is:

- Laure Daviaud, Marianne Johnson, *The Shortest Identities for Max-Plus Automata with Two States*, MFCS 2017, DOI `10.4230/LIPIcs.MFCS.2017.48`.

That paper studies identities of the full two-state class, not positivity or pointwise comparison. Structural `2 x 2` tropical-matrix semigroup literature is likewise directly relevant background, but no containment theorem equivalent to the public result was located.

Broader containment and decision-problem references checked include:

- Laure Daviaud, *Containment and Equivalence of Weighted Automata: Probabilistic and Max-Plus Cases*, LATA 2020, DOI `10.1007/978-3-030-40608-0_2`;
- Shaull Almagor, Udi Boker, Orna Kupferman, *What's decidable about weighted automata?*, Information and Computation 282 (2022), DOI `10.1016/j.ic.2020.104651`;
- Laure Daviaud, David Purser, Marie Tcheng, *The Big-O Problem for Max-Plus Automata is Decidable (PSPACE-Complete)*, LICS 2023 / arXiv:2304.05229.

The Big-O theorem concerns affine domination rather than exact containment. Known positive results for finitely ambiguous automata do not cover arbitrary two-state automata because state count does not bound ambiguity.

The 2026 tropical/min-plus decision literature was also checked. In particular, Almagor--Arbel--Sheinvald decide **determinisability** and study its complexity, unambiguisability, and register minimisation; those results do not say that every two-state weighted automaton is determinisable. The 2026 one-letter representation theorem fixes alphabet size rather than state count. Nearby few-register cost-register-automata results use different model restrictions and decision problems, and do not translate to the theorem while preserving the two-state bound.

The fresh audit is recorded in [`provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md`](provenance/TWO_STATE_MAXPLUS_NOVELTY_AUDIT_20260901.md). Its conclusion is deliberately bounded:

```text
published d=2 open case:       confirmed
prior resolution located:      no, in targeted audit through 2026-09-01
absolute historical firstness: not certified
```

Accordingly the public claim is the **proved two-state comparison theorem and its resolution of the stated `d=2` open case under a dated literature audit**, not a blanket claim of historical priority over every unpublished or differently indexed source.

## 12. Boolean Tucker decomposition

Boolean tensor factorization, including Boolean Tucker decomposition, is established prior work. A basic reference is:

- Pauli Miettinen, *Boolean Tensor Factorizations*, ICDM 2011, DOI `10.1109/ICDM.2011.28`.

The EIG repository does **not** claim Boolean Tucker decomposition itself as new.

The external case study in [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md) asks a narrower structural question: whether the independently minimal Boolean ranks of all mode unfoldings must be jointly realizable by one exact Boolean Tucker core. An explicit `2 x 4 x 4` counterexample is given and checked. No historical `first` claim is required for the role this example plays in the programme.

A nearby warning is also important: constrained Tucker decompositions over other cones are already known to have non-field-like rank behaviour. In particular, nonnegative Tucker literature contains examples where a minimum nonnegative Tucker decomposition need not exist. Therefore EIG does **not** claim the generic statement “constrained Tucker rank need not have a minimum” as new.

The follow-up F/T/three-zero-hook analysis also touches classical semilattice theory. Abstract flatness/distributivity results for join-semilattices are prior art; the public EIG claim is the concrete Boolean junction application and finite obstruction analysis, not the classical theorem.

## 13. Binary-rank Kronecker nonmultiplicativity: Shitov 2026

An important priority correction for the external-search lane is:

- Yaroslav Shitov, *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted **2026-07-25**, DOI `10.13140/RG.2.2.26449.90723`.

Shitov gives an explicit `5 x 5` binary matrix `B` with

```text
rank_01(B) = 5,
rank_01(B tensor B) <= 24 < 25.
```

The EIG search lane independently found a different `5 x 5` `5 -> 24` example on 2026-08-31. Its finite certificate is correct, but **the theorem that binary rank is nonmultiplicative under Kronecker product is not an EIG novelty claim**. The EIG example is retained only as a calibration of the parallel-composition search heuristic.

## 14. Arity/nerve and generic reconstruction machinery

Yoneda density, presheaf reconstruction, monads with arities, nervous monads, Grothendieck constructions, profunctors/equipments, sheaves/stacks, and descent theory provide powerful generic reconstruction shells.

EIG may use these as representation machinery. It must not count their existence as evidence that the **correct process-generated or interaction-generated arities were derived rather than supplied**.

## What remains distinctive in the present EIG formulation

After these exclusions, the strongest honest EIG target is not any single slogan above. It is the simultaneous package formalized as WEIR:

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

Several neighbouring theories cover large and important parts of this chain, including policy-relative objecthood, proof-relevant witnesses/certificates, policy refinement, and obstruction-driven policy formation. **No claim is made here that an exhaustive historical search has proved the whole package unique.** The current literature audit has not identified a direct predecessor that derives this entire package from one frozen interaction laboratory without supplying the target object/map world or equivalent domain structure.

## Novelty policy

A result enters the EIG public core only if its statement separates:

1. the classical theorem being used;
2. the new operational interpretation or bridge, if any;
3. the exact project-specific statement;
4. what remains conjectural;
5. whether historical novelty has actually been checked.

At this snapshot, no blanket claim that EIG is a historically new foundation or established field is made. External results are presented at the narrowest independently supported scope, with dated novelty audits where priority matters.