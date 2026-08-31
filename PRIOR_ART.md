# Prior art and novelty boundary

EIG sits close to several mature traditions. This is not peripheral bibliography: these theories define the boundary of what the programme may honestly claim.

## 1. Syntactic monoids, algebras, and Myhill--Nerode theory

Two-sided contextual equivalence and response-minimal quotients are classical in automata and formal-language theory. For words and Boolean acceptance, `Syn(P,r)` specializes to the syntactic congruence/monoid. Weighted and algebraic variants provide many related minimization constructions.

**EIG does not claim contextual minimization itself as new.** The question is whether the same exact-continuation principle, with witness-sensitive enrichment, can serve as one component of a broader reconstruction theorem.

## 2. Karoubi/Cauchy completion and Morita theory

Recovering typed corners `fPe` from idempotents of an untyped monoid/semigroup is the classical Karoubi construction. Cauchy completion and Morita theory already explain why presentations can determine categories only up to appropriate retract/completion equivalences.

**EIG does not claim idempotents-as-objects as new.** It uses this as a calibration and explicitly expects Cauchy/Morita moduli in any serious unicity theorem.

## 3. Arrow-only categories, consolidations, and restriction semigroups

Categories admit object-free/arrow-only presentations. Semigroup theory also studies the **consolidation** of a category: adjoin zero and send noncomposable products to zero. Restriction-semigroup and related constructions give exact correspondences in important classes.

The theorem in [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md) uses this classical shell. Its EIG role is narrower: freeze the observation to one-bit composition success, take its full two-sided contextual quotient, identify the quotient classes with endpoint types, then retain the prequotient arrows as witness fibres to reconstruct Hom sets.

## 4. Relations, allegories, ludics, and Geometry of Interaction

Relational/allegorical approaches make relations primary and recover maps internally. Girard's ludics makes interaction and orthogonality foundational. Geometry of Interaction and Seiller's Interaction Graphs study execution, measurement, orthogonality, and observational equivalence.

**EIG therefore does not claim “interaction is primitive” or “types arise by interaction” as unprecedented ideas.**

Representative references include Thomas Seiller, *Interaction Graphs: Additives*, arXiv:1205.6557, and the ludics literature on designs, interaction, and biorthogonality.

## 5. Isbell nuclei: especially close 2026 work

Juan Luis Gastaldi, Samantha Jarvis, Thomas Seiller, and John Terilla, *A calculus of types in Isbell nuclei*, arXiv:2606.03369 (2026), starts from execution and measurement and derives an orthogonality-generated type calculus through enriched Isbell nuclei.

This directly blocks any EIG novelty claim of the form

```text
execution + measurement -> emergent types.
```

The remaining EIG target is broader: simultaneous reconstruction of response-minimal algebra, doctrine-relative interfaces/objects, internally selected maps, witness multiplicity/provenance, exact Hom/composition, doctrine change, and local-to-global descent.

## 6. Boolean Tucker decomposition

Boolean tensor factorization, including Boolean Tucker decomposition, is established prior work. A basic reference is:

- Pauli Miettinen, *Boolean Tensor Factorizations*, ICDM 2011, DOI `10.1109/ICDM.2011.28`.

The EIG repository does **not** claim Boolean Tucker decomposition itself as new.

The external case study in [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md) asks a narrower structural question: whether the independently minimal Boolean ranks of all mode unfoldings must be jointly realizable by one exact Boolean Tucker core. An explicit `2 x 4 x 4` counterexample is given and checked. No historical `first` claim is required for the role this example plays in the programme.

A nearby warning is also important: constrained Tucker decompositions over other cones are already known to have non-field-like rank behaviour. In particular, nonnegative Tucker literature contains examples where a minimum nonnegative Tucker decomposition need not exist. Therefore EIG does **not** claim the generic statement “constrained Tucker rank need not have a minimum” as new.

The follow-up F/T/three-zero-hook analysis also touches classical semilattice theory. Abstract flatness/distributivity results for join-semilattices are prior art; the public EIG claim is the concrete Boolean junction application and finite obstruction analysis, not the classical theorem.

## 7. Binary-rank Kronecker nonmultiplicativity: Shitov 2026

A priority correction is load-bearing for the external-search lane:

- Yaroslav Shitov, *Factoring Kronecker squares of nonnegative matrices with GPT-5.6 Sol*, publicly posted **2026-07-25**, DOI `10.13140/RG.2.2.26449.90723`.

Shitov gives an explicit `5 x 5` binary matrix `B` with

```text
rank_01(B) = 5,
rank_01(B tensor B) <= 24 < 25.
```

The EIG search lane independently found a different `5 x 5` `5 -> 24` example on 2026-08-31. Its finite certificate is correct, but **the theorem that binary rank is nonmultiplicative under Kronecker product is not an EIG novelty claim**. The EIG example is retained only as a calibration of the parallel-composition search heuristic.

## 8. Arity/nerve and generic reconstruction machinery

Yoneda density, presheaf reconstruction, monads with arities, nervous monads, Grothendieck constructions, profunctors/equipments, and descent theory provide powerful generic reconstruction shells.

EIG may use these as representation machinery. It must not count their existence as evidence that the **correct process-generated or interaction-generated arities were derived rather than supplied**.

## Novelty policy

A result enters the EIG public core only if its statement separates:

1. the classical theorem being used;
2. the new operational interpretation or bridge, if any;
3. the exact project-specific finite statement;
4. what remains conjectural;
5. whether historical novelty has actually been checked.

At this snapshot, no blanket claim that EIG is a historically new foundation or established field is made. External examples are presented at the narrowest independently supported scope; a short counterexample is useful even without asserting priority.
