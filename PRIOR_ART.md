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

## 4. Relations and allegories

Allegory/relational approaches make relations primary and recover ordinary maps internally using relational equations (for example, total and single-valued relations). Coreflexive relations or related idempotents can encode ordinary subobjects/interfaces.

This is strong prior evidence that map/object structure can be derivative in suitable doctrines.

## 5. Ludics

Girard's ludics makes interaction and orthogonality foundational: designs interact, behaviours/types arise by biorthogonal closure, and typing need not be primitive at the level of designs.

A useful entry point is the ludics literature on interaction/orthogonality and behaviours; for a concise description see:

- Myriam Quatrini and Christophe Fouqueré, *Incarnation in Ludics and maximal cliques of paths*, arXiv:1307.1028.

**EIG therefore does not claim “interaction is primitive” or “types arise by interaction” as unprecedented ideas.**

## 6. Geometry of Interaction and Interaction Graphs

Girard's Geometry of Interaction studies the dynamics of cut elimination through execution. Thomas Seiller's Interaction Graphs develops quantitative execution, measurement, orthogonality, observational equivalence, and graph/graphing models.

Representative reference:

- Thomas Seiller, *Interaction Graphs: Additives*, arXiv:1205.6557.

The name **Exact Interaction Geometry** is not intended to rename Geometry of Interaction. GoI and Interaction Graphs are close prior art and must be compared explicitly whenever EIG makes a logic/realisability claim.

## 7. Isbell nuclei: especially close 2026 work

The closest currently known recent reference is:

- Juan Luis Gastaldi, Samantha Jarvis, Thomas Seiller, John Terilla, *A calculus of types in Isbell nuclei*, arXiv:2606.03369 (2026).

That work starts from an associative execution and a real-valued measurement, identifies orthogonality-generated types with fixed points of an enriched Isbell adjunction, and derives an associative/residuated type calculus after repairing a naive product.

This directly blocks any EIG novelty claim of the form

```text
execution + measurement -> emergent types.
```

The remaining EIG target is different and stronger: simultaneous reconstruction of response-minimal algebra, doctrine-relative interface/object locus, internally selected maps, witness multiplicity/provenance, exact Hom/composition, doctrine change, and local-to-global descent.

## 8. Arity/nerve and generic reconstruction machinery

Yoneda density, presheaf reconstruction, monads with arities, nervous monads, Grothendieck constructions, profunctors/equipments, and descent theory provide powerful generic reconstruction shells.

EIG may use these as representation machinery. It must not count their existence as evidence that the **correct process-generated or interaction-generated arities were derived rather than supplied**.

## Novelty policy

A result enters the EIG public core only if its statement separates:

1. the classical theorem being used;
2. the new operational interpretation or bridge, if any;
3. the exact project-specific hypothesis;
4. what remains conjectural;
5. whether historical novelty has actually been checked.

At this snapshot, no blanket claim that EIG is a historically new foundation or established field is made.
