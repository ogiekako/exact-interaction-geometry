# Exact Interaction Geometry — Foundational Disclosure

**Snapshot date: 2026-09-01**

> **Curation note added 2026-09-02.** The Boolean Tucker “junction counterexample” mentioned later in this historical snapshot was subsequently removed from the current public theorem/case-study surface. The finite calculation was formulated against an EIG-generated universal question, but the later curation review did not identify a published conjecture or problem asserting that universal property. The old material remains recoverable from Git history (for example at commit `455c2cf0f166cdf2d822b6007f6878b3aa32f867`) as research provenance/calibration, not as a documented external problem resolution. The remainder of this file is preserved as the 2026-09-01 snapshot rather than retroactively rewritten.

This note records the strongest formulation of Exact Interaction Geometry (EIG) that is defensible from the public repository at this date. It is intended to make the programme reconstructible from one document: what the primitive stance is, what has already been proved, what is only a design constraint, what remains conjectural, and which parts are classical prior art.

It is a dated disclosure of a formulation. It does **not** assert that every ingredient below is novel, that no equivalent formulation exists elsewhere, or that the general reconstruction theorem has been proved.

## 1. What EIG means in this snapshot

EIG is the research programme of reconstructing mathematical interfaces, objecthood, typing, maps, witnesses, and compositional structure **downstream of interaction**, rather than supplying those structures as primitive whenever the interaction data suffice to recover them.

The basic stance is:

```text
raw interaction / execution
        +
admitted continuation experiments
        +
closed exact responses
        +
reopenable witness data when scalar response is insufficient
        ↓
exact contextual reduction
        ↓
derived interfaces / objecthood / maps
        ↓
witness-sensitive composition and descent
        ↓
reconstructed mathematical structure
```

The claim is not that objects never exist or that every theory should be presented objectlessly. The question is whether, in a given interaction doctrine, the structures normally supplied in advance are in fact **forced by what can compose and what future interaction can distinguish**.

At this date, the general answer is open. Several exact special cases are proved.

## 2. Primitive data and the exactness principle

The smallest EIG laboratory contains interaction fragments, an execution or pasting operation, and a class of admitted closed experiments with exact responses. A doctrine specifies which continuations and responses count as observable.

For an associative interaction semigroup `P` with closed response `r`, let `P^1` denote its unitalization (or simply `P` itself when a unit is already present). Define the full two-sided contextual relation by

```text
a ~_r b
iff
r(x a y) = r(x b y)
for all x,y in P^1.
```

Equivalently, empty left and right contexts are admitted, and the context family is closed under extension by composition. Under these assumptions the relation is a congruence: multiplying equivalent fragments on either side can be absorbed into the quantified contexts. Because the empty contexts are included, the quotient also preserves the original closed response `r(a)`.

The quotient is therefore the coarsest composition-stable identification preserving the declared closed responses in the standard syntactic-algebra sense.

This motivates the EIG exactness rule:

> **Forget only what no admitted future interaction can distinguish.**

The rule is classical in important special cases; EIG does not claim syntactic congruences, Myhill--Nerode minimization, or behavioral state minimization as new.

### Finite exact interface theorem

For a finite response table

```text
M : X × Y -> K,
```

a deterministic exact interface is a surjection `q : X -> I` through which every response row factors. Define

```text
x ~_M x'  iff  M(x,-) = M(x',-).
```

Then `X / ~_M` is the **unique coarsest surjective deterministic exact interface**, up to unique bijection: every other surjective exact interface factors through it.

This theorem is elementary and belongs to the classical minimization pattern. Its EIG role is conceptual and structural: an exact deterministic boundary need not be selected by hand; it can be forced by all future responses.

See [`theory/01-finite-exact-interactions.md`](theory/01-finite-exact-interactions.md).

## 3. Why EIG is not merely a quotient theory

A scalar contextual quotient can identify which interactions have the same closed response behavior while still losing information needed when an internal boundary is reopened.

Examples include:

- witness multiplicity;
- provenance of a successful interaction;
- alternative latent factorizations;
- cocycle or phase data;
- higher comparison/coherence data.

Two interaction systems can therefore agree at the level of scalar support while differing in witness structure.

The corresponding EIG design constraint is:

```text
global contextual collapse
        +
coherent witness retention / descent.
```

This is a constraint on any sufficiently strong reconstruction theorem, not a claim that one universal witness object has already been found.

In the finite semiring calibration, witness mediation is represented by factorizations `M = U V`. The minimum latent witness count is the usual semiring factor rank. Serial composition obeys a data-processing inequality and parallel composition is submultiplicative. The algebra is classical; the EIG point is that exact boundary complexity can be doctrine-dependent and witness-sensitive.

## 4. Doctrine-relative objecthood

EIG does not currently posit one doctrine-free formula saying which stable interactions are the objects.

Classical constructions already show several plausible stable loci:

- all idempotents followed by Karoubi/Cauchy splitting;
- coreflexive idempotents in relational settings;
- projections or dagger idempotents in operator/dagger settings;
- central, causal, sharp, or otherwise internally characterized stable loci in other doctrines.

The admitted experiments may also change which distinctions survive contextual reduction.

Accordingly the present EIG position is:

> **Objecthood may be doctrine-relative, but it should be selected internally from the interaction doctrine rather than smuggled in as the target answer.**

The general selector is not known. A successful general theorem must either justify a convention such as Cauchy saturation or derive an internal predicate selecting the intended interfaces.

## 5. Exact positive theorem: categories from untyped interaction

There is already a broad sector in which the slogan “objecthood downstream of interaction” is an exact theorem.

Let `C` be any small category. Erase:

- the object set;
- every source and target label;
- all Hom-set labels;
- all identity labels.

Keep only the raw arrows, adjoin an absorbing failure symbol `0`, and define multiplication to be ordinary composition when composable and `0` otherwise. Observe one bit:

```text
success  iff  the product is nonzero.
```

For nonzero arrows `a,b`, full two-sided continuation success satisfies

```text
a ~ b
iff
a and b have the same ordered source/target pair.
```

Therefore the contextual quotient recovers endpoint types. Its nonzero idempotent classes correspond exactly to the original objects. If the original raw arrows are retained as witness fibres over those recovered endpoint classes, then the original Hom sets, identities, and composition are recovered exactly.

Thus, for every small category,

```text
untyped execution
+ one-bit continuation success
+ retained raw-arrow witnesses
    -> objects + typing + Hom sets + identities + composition.
```

This is a genuine exact reconstruction theorem. It uses classical category consolidation / semigroup ideas, and EIG does not claim those ingredients as new. The point of the theorem in this programme is that the object and typing data are not supplied to the observer: they are recognized operationally from continuation behavior, while witness fibres prevent the quotient from destroying Hom multiplicity.

The theorem also exposes a boundary: exact object/Hom reconstruction does **not** imply ULF/Conduche or exact lifting of every quotient-level factorization.

See [`theory/02-category-reconstruction.md`](theory/02-category-reconstruction.md).

## 6. The EIG architecture

The current architecture is summarized by

```text
CONTEXT
  -> REDUCE
  -> WITNESS
  -> COMPOSE
  -> GLUE / CODESCEND
  -> PROJECT
  -> STRUCTURE
  -> REFLECT
  -> RECONSTRUCT.
```

The stages mean:

- **CONTEXT:** declare the admitted continuations and closed experiments;
- **REDUCE:** identify fragments only when all admitted future responses agree;
- **WITNESS:** retain multiplicity/provenance/coherence that reopened interaction can distinguish;
- **COMPOSE:** derive exact serial, parallel, and more general pasting laws;
- **GLUE/CODESCEND:** determine when local witness data reconstruct globally without duplication or loss;
- **PROJECT:** take lower-information shadows or invariants only after the exact structure is understood;
- **STRUCTURE:** study factorization, separators, obstruction patterns, localization, and complexity of the interaction geometry;
- **REFLECT:** characterize which abstract interaction presentations come from the intended mathematical world;
- **RECONSTRUCT:** recover the target object/map/Hom/process world up to the correct equivalence or moduli.

Not every application requires every stage. This sequence is a programme architecture, not a theorem asserting that every stage exists for every doctrine.

## 7. The open general theorem: WEIR

The present sharp foundational target is **WEIR — Witness-Enriched Interaction Reconstruction**.

A successful theorem should identify natural classes of interaction laboratories for which one non-circular rule derives, from interaction data rather than a supplied answer:

1. a coarsest exact contextual algebra;
2. an internally characterized interface/object locus;
3. internally characterized maps;
4. exact witness multiplicity and provenance;
5. exact composition and cross-object/cross-process Hom reconstruction;
6. functorial behavior under refinement/change of doctrine;
7. intrinsic local-to-global descent and obstruction data;
8. blind recovery in at least two mathematically distant calibration domains under one rule frozen in advance.

Literal uniqueness may be too strong. The honest endpoint may be uniqueness only up to Cauchy completion, Morita equivalence, doctrine equivalence, or a canonical moduli/groupoid of reconstructions.

**WEIR is open.** The repository does not promote it as a proved general theorem.

See [`theory/03-weir.md`](theory/03-weir.md).

## 8. What is already mathematically established

As of this snapshot, the public foundational surface supports the following claims.

| Claim | Public status | Novelty posture |
| --- | --- | --- |
| contextual equality of finite response rows gives the unique coarsest deterministic exact interface | proved | classical minimization pattern |
| semiring witness factor rank obeys serial data processing and parallel submultiplicativity | proved | classical factorization algebra |
| two-sided syntactic contextual equivalence is composition-stable and response-minimal | proved | classical syntactic algebra |
| Karoubi/Cauchy splitting supplies a standard typed category from idempotents | proved/classical | not an EIG novelty |
| every small category is exactly reconstructible from untyped consolidation + one-bit continuation success + raw-arrow witness fibres | proved | classical shell; EIG operational reconstruction formulation |
| exact category reconstruction does not imply exact factorization lifting | proved | boundary/calibration result |
| one universal doctrine-internal object selector | open | not claimed |
| general witness-enriched descent | open | not claimed |
| one blind cross-domain extractor with honest unicity/moduli | open | not claimed |
| general WEIR theorem | open | not claimed |

The detailed epistemic boundary is maintained in [`STATUS.md`](STATUS.md).

## 9. External mathematical evidence generated by the programme

EIG is intended to be falsifiable and mathematically productive, not only a vocabulary for reorganizing known structures. Two current public case studies illustrate that role without being logically required by the foundational claims.

### Two-state max-plus comparison

The programme's residual/interface viewpoint led to isolating the unique one-dimensional projective gap of a two-state max-plus automaton and asking whether a transition can simultaneously preserve that unbounded residual for future computation and expose its magnitude in the current output.

The answer is an exact tail trichotomy—propagate, forget, or read-and-forget—with the key property that a step whose output depends on the unbounded magnitude cannot also propagate that magnitude to the future. It yields an exact one-counter realization and a decidability proof for arbitrary-left / at-most-two-state-right max-plus comparison. The manuscript proves the `d=2` case of the bounded-state question explicitly posed by Daviaud--Guillon--Merlet (MFCS 2017). The theorem itself is ordinary weighted-automata mathematics and does not depend on EIG.

See [`discoveries/two-state-maxplus-comparison.pdf`](discoveries/two-state-maxplus-comparison.pdf).

### Boolean Tucker junction failure

The EIG question “do independently minimal exact interfaces necessarily descend through one common junction witness?” led to an explicit Boolean Tucker example in which all three mode unfoldings attain their separate minimum Boolean ranks but those minima cannot be realized simultaneously by one exact core.

See [`discoveries/boolean-tucker-junction-counterexample.md`](discoveries/boolean-tucker-junction-counterexample.md).

These examples are evidence that the interaction-first questions can select nontrivial conventional mathematics. They are not evidence that the general WEIR theorem is already true.

## 10. Explicit prior-art boundary

The following broad ideas are **not** claimed as EIG inventions:

- interaction/process composition as a primitive viewpoint;
- observational or contextual equivalence;
- Myhill--Nerode and syntactic minimization;
- behavioral state constructions;
- objectless/arrow-only category presentations;
- category consolidation into semigroups with zero;
- Karoubi/Cauchy completion and Morita phenomena;
- relations/allegories and internally characterized maps;
- Chu-style state/test duality;
- ludics, Geometry of Interaction, and Interaction Graphs;
- “types emerge from execution/measurement” in the broad sense;
- idempotent packaging, stable quotient objecthood, or local-to-global quotient descent in the broad sense;
- generic Yoneda/nerve, profunctor, Grothendieck, sheaf, stack, or descent machinery.

The nearest contemporary programmes and the repository's comparisons with them are discussed in [`PRIOR_ART.md`](PRIOR_ART.md) and [`CONTEMPORARY_NEIGHBORS.md`](CONTEMPORARY_NEIGHBORS.md). Those comparison judgments are interpretations by this repository unless a cited source itself states the relationship.

## 11. The dated EIG formulation being disclosed

For priority and interpretability, the content intended to be fixed by this snapshot is the following.

> **Exact Interaction Geometry, as used in this repository on 2026-09-01, is the interaction-first reconstruction programme whose core requirements are:**
>
> 1. **exact contextual reduction** — quotient only distinctions invisible to every admitted continuation;
> 2. **witness-sensitive reconstruction** — retain multiplicity, provenance, and coherence whenever reopened interaction can distinguish them;
> 3. **doctrine-relative interface/object selection** — derive the relevant stable/sharp object locus internally rather than presupposing one universal object notion;
> 4. **compositional reconstruction** — recover typing, maps, Hom/process data, and composition from the interaction presentation where possible;
> 5. **descent and obstruction as intrinsic structure** — treat failures of compatible local witness realization as part of the geometry rather than as unrelated diagnostics;
> 6. **honest reconstruction equivalence** — state Cauchy/Morita/doctrine or moduli ambiguity explicitly rather than claiming false literal uniqueness;
> 7. **blind calibration** — ultimately require one rule, frozen before seeing the target answers, to recover structurally distant domains.

This seven-part package is the intended meaning of the named programme at this date. Some components have exact special-case theorems; the simultaneous general theorem remains open.

This note makes **no absolute historical-priority claim** for that package. Its purpose is narrower and mechanically checkable: to record that this is the formulation publicly disclosed in this repository at this date, with the theorem/conjecture/prior-art boundaries stated explicitly.

## 12. What a reader should be able to recover from this repository

A reader using only the public repository should be able to determine:

- what primitive stance EIG takes;
- the exact finite residual theorem;
- why witness retention is a separate requirement from scalar quotienting;
- why the programme refuses a universal doctrine-free object selector at present;
- a complete exact category reconstruction theorem;
- the current multi-stage architecture;
- the WEIR acceptance gates and falsification boundary;
- which nearby classical and contemporary theories are relevant to broader novelty questions;
- which external theorem/counterexample arose from the programme;
- exactly which claims are proved, classical, open, or only provenance.

If future work materially strengthens or changes the programme, it should do so in a new dated revision rather than retroactively changing what this snapshot claimed.

---

**Author:** Keigo Oka  
**Public repository:** https://github.com/ogiekako/exact-interaction-geometry  
**Snapshot:** 2026-09-01
