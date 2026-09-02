# Exact Interaction Geometry — Foundational Disclosure

**Snapshot date: 2026-09-02**

This note updates the public formulation of Exact Interaction Geometry (EIG) without retroactively changing the 2026-09-01 snapshot. The public theorem status is not strengthened merely by this prose revision. The main change is conceptual precision: EIG is best stated as a programme about **identifiability boundaries**, not as the unqualified claim that structure follows from “interaction itself.”

For the detailed boundary-first discussion, see [`EIG_IDENTIFIABILITY_BOUNDARIES_20260902.md`](EIG_IDENTIFIABILITY_BOUNDARIES_20260902.md).

## 1. Primitive stance

EIG begins with a declared **operational interaction doctrine**. Depending on the domain, its primitive data may include:

- interaction fragments;
- execution, composition, or pasting laws;
- admitted continuation experiments;
- exact closed responses;
- recodings regarded as harmless;
- witness/provenance data that can be reopened when scalar response is insufficient.

The target object, map, factorization, metric, category, or semantic classifier is not supposed to be supplied merely because it is convenient for the reconstruction proof.

The doctrine itself is part of the input unless a separate theorem reconstructs it. In particular, EIG does not infer an execution grammar from bare probabilities simply by calling those probabilities “interaction data.”

## 2. The exact output schema

The sharper EIG question is:

> What is the maximal mathematical structure identifiable from the declared doctrine, what residual fibre or moduli remain operationally invisible, and what additional resource is required to identify more?

The generic form is

```text
operational doctrine
      -> exact contextual reduction
      -> maximal identifiable core + residual fibre/moduli
      -> witness-sensitive composition/descent when available
      -> either
           reconstruction up to the correct equivalence,
         or
           an exact no-go / residual-moduli theorem.
```

A failure to reconstruct the originally desired target is therefore not automatically a negative result. If the theorem identifies the largest invariant that survives all admitted observations and proves why the remaining fibre cannot be removed, the boundary itself is the mathematical answer.

## 3. Identifiability is not canonical selection

Two questions must be separated:

```text
identifiability:
  which distinctions can the doctrine detect?

selection:
  among all compatible realizations, does the doctrine canonically choose one?
```

A richer experiment doctrine can make more distinctions visible without producing a unique preferred representative. Conversely, a symmetry or normalization may select a representative while leaving other operational distinctions unresolved.

This distinction is now treated as a first-class design constraint for WEIR.

## 4. Exact contextual reduction

For a monoid-like interaction system `P` with response `r`, define

```text
a ~ b
iff
r(xay)=r(xby)
for every admitted left/right context x,y.
```

Under the standard closure hypotheses this is a congruence and gives a response-exact syntactic quotient. This is classical mathematics in important special cases; EIG does not claim contextual minimization itself as new.

For a finite response table `M : X x Y -> K`, equality of response rows gives the unique coarsest surjective deterministic exact interface. If

```text
pi : X -> R(M)
```

is the canonical quotient and

```text
q : X -> I
```

is any other surjective exact interface, then

```text
pi = h o q
```

for a unique `h : I -> R(M)`. Thus the canonical residual quotient factors through every exact interface.

## 5. Why the quotient is not enough

Contextual collapse can erase data required when an internal boundary is reopened. Examples include:

- witness multiplicity;
- provenance;
- alternative latent factorizations;
- phase/cocycle information;
- higher comparison and coherence data.

EIG therefore requires a second layer: retain exactly the witness information that later admitted interaction can still distinguish.

The intended pattern is

```text
minimal response quotient
        +
minimal sufficient witness enrichment.
```

A universal construction accomplishing this in broad doctrine classes is not known.

## 6. Doctrine-relative objecthood and geometry

EIG does not posit one universal doctrine-free formula for objects. Idempotents, projections, coreflexives, dagger idempotents, causal/sharp elements, or other stable loci may be appropriate in different doctrines.

Likewise, “geometry” in EIG means factorization, fibres, descent, obstruction, localization, and moduli of interaction structure. It does **not** mean that interaction data automatically determine physical space, a tensor-product atomization, a causal manifold, or a metric.

If a desired spatial or metric target is not identifiable, a residual orbit, coarse interaction structure, or impossibility theorem may be the correct exact output.

## 7. Exact category calibration and its boundary

For every small category `C`, erase its object set and source/target/Hom labels. Keep the raw arrows and the **totalized execution law**: ordinary composition when defined, and an absorbing failure otherwise. Observe only whether a continuation succeeds.

Two-sided continuation success recovers the ordered endpoint type of every raw arrow. Retaining the raw arrows as witness fibres then reconstructs objects, Hom sets, identities, and composition.

This is an exact operational recognition theorem built on classical consolidation/semigroup machinery.

The boundary is equally important: the execution law is supplied. The theorem does not reconstruct composition grammar from bare scalar response data, and object/Hom reconstruction does not imply exact lifting of every quotient-level factorization.

## 8. WEIR after the boundary refinement

The general open target remains **WEIR — Witness-Enriched Interaction Reconstruction**.

A successful theorem should, for natural doctrine classes, derive:

1. an explicit no-smuggling operational input boundary;
2. exact contextual reduction;
3. a maximal identifiable core plus residual fibre/moduli;
4. doctrine-relative interfaces/objecthood;
5. internally characterized maps;
6. witness multiplicity/provenance/coherence;
7. exact composition, cross-Hom reconstruction, and descent/obstructions;
8. functorial doctrine refinement;
9. blind cross-domain calibration by one frozen **meta-rule/schema** parameterized only by the declared doctrine, not by the target answer.

The last requirement is an anti-overfitting condition. Doctrine relativity does not require one literal extractor with identical internal syntax in every domain.

WEIR remains open.

## 9. What is publicly established

The 2026-09-02 wording does not change the basic public theorem ledger:

- finite exact residual quotients and elementary factor-rank laws are proved, largely as classical mathematics interpreted through EIG;
- the category calibration gives exact object/typing/Hom reconstruction from supplied totalized execution plus continuation success and witness fibres;
- the two-state max-plus comparison theorem is a conventional mathematical result with a public proof;
- the Boolean Tucker junction example is an exact finite counterexample with public verification;
- binary-Kronecker nonmultiplicativity is only a project rediscovery/calibration, not an EIG novelty claim;
- general WEIR remains conjectural.

See [`STATUS.md`](STATUS.md) for the detailed epistemic ledger.

## 10. Prior-art and novelty posture

EIG does not claim novelty for interaction-first foundations, observational equivalence, syntactic minimization, behavioral states, arrow-only categories, Karoubi/Cauchy completion, relations/allegories, Chu-style duality, ludics, Geometry of Interaction, Interaction Graphs, Isbell nuclei, fibres, descent, or obstruction geometry in isolation.

The intended programme-level contribution is narrower: test whether the recurring pattern

```text
maximal identifiable invariant
+ residual indistinguishability fibre
+ minimal additional resource
```

can organize exact reconstruction and no-go theorems across mathematically distant doctrines without target leakage, while retaining witnesses and stating reconstruction moduli honestly.

This formulation itself is not asserted to be historically unprecedented. The public claim is that this is the EIG programme formulation adopted by this repository on 2026-09-02.

---

**Author:** Keigo Oka  
**Public repository:** https://github.com/ogiekako/exact-interaction-geometry  
**Snapshot:** 2026-09-02
