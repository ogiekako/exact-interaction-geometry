# EIG — Identifiability Boundaries

**Snapshot: 2026-09-02**

This note sharpens the programme-level language of Exact Interaction Geometry (EIG). It does not promote a new general theorem. It records a more precise way to state what the programme is trying to compute.

## 1. The boundary-first formulation

EIG is not merely the slogan “derive structure from interaction.” Its sharper question is:

> Given a specified operational interaction doctrine, what structure is forced by all admitted responses, what residual moduli remain observationally invisible, and what additional resource is minimally required to reconstruct more?

An operational interaction doctrine may include execution or pasting laws, admitted continuation experiments, exact responses, harmless recodings, and witness data that can be reopened when scalar response is insufficient. Bare distinguishability or bare probabilities are not assumed to determine the execution grammar itself.

The intended output is therefore not always a reconstructed target. The generic schema is

```text
operational doctrine
      -> contextual reduction
      -> maximal identifiable core + residual fibre/moduli
      -> either
           (a) extra resource closes the fibre -> reconstruction, or
           (b) fibre persists -> exact no-go / moduli theorem.
```

A failed reconstruction can therefore be mathematically successful if it identifies the exact maximal invariant and the precise obstruction to going further.

## 2. Why this is stronger than a quotient slogan

A contextual quotient answers which distinctions are invisible to the declared continuations. That is only the first layer.

A serious reconstruction problem must also ask:

1. **What is the maximal identifiable invariant?**
   The answer may be a quotient, stabilizer, fixed-point object, coarse structure, cohomology class, or another doctrine-dependent invariant.

2. **What remains in the fibre?**
   Several latent implementations, factorizations, localities, metrics, representatives, or witnesses may induce exactly the same admitted responses.

3. **What additional resource closes the fibre?**
   A reference, open interface, phase-bearing control, localization assumption, witness channel, preparation class, or other extra experiment may remove part or all of the ambiguity.

4. **Was the target already encoded in the input?**
   A positive theorem is weak if the supplied doctrine contains an answer-adjacent classifier or a compressed copy of the target.

This makes answer leakage and residual nonuniqueness part of the theorem statement rather than post-hoc caveats.

## 3. Exact calibrations already in this repository

### Finite response tables

For `M : X x Y -> K`, equality of response rows gives the coarsest deterministic exact residual interface. If `q : X -> I` is any surjective exact interface and `pi : X -> R(M)` is the canonical row quotient, then

```text
pi = h o q
```

for a unique `h : I -> R(M)`.

Thus the canonical residual quotient factors through every exact interface. This is the smallest exact model of “maximal identifiable invariant.”

If latent witnesses are retained, the relevant complexity is no longer just the quotient cardinality: semiring factor rank gives a doctrine-dependent witness dimension.

### Category reconstruction

In the category calibration, the supplied primitive is the **totalized execution law** on raw arrows: composable products execute normally, noncomposable products return an absorbing failure. One-bit continuation success reconstructs endpoint types; raw-arrow witness fibres then recover Hom sets and composition.

This is an exact reconstruction theorem, but it is not reconstruction of the execution grammar from bare scalar data. It reconstructs hidden typing/object structure from a supplied execution law and its continuation profiles.

### Boolean Tucker junction failure

The explicit Boolean Tucker example shows another boundary: independently minimal interfaces need not admit one common exact junction witness. The obstruction is not noise to remove; it is intrinsic gluing geometry.

### Two-state max-plus comparison

The two-state max-plus theorem isolates one unbounded projective residual. Its propagate / forget / read-and-forget trichotomy is an exact statement about what a transition may expose now and what it may preserve for future interaction. This is a conventional mathematical theorem selected by the same boundary-first viewpoint.

## 4. “Geometry” does not mean “space follows from interaction”

EIG uses “geometry” broadly for factorization, fibres, descent, obstruction, localization, and moduli. It does not infer a physical tensor-product structure, microscopic atomization, causal manifold, or metric merely because an interaction invariant exists.

When a desired spatial or metric target is not identifiable, the correct EIG output may be a residual orbit, a coarser interaction structure, or a no-go theorem. Additional spatial principles then belong on the input side of the next theorem.

## 5. Identifiability and canonical selection are different questions

More observations can improve identifiability without producing a unique canonical representative. Conversely, a symmetry or constraint may make a selector unique while hiding other operational distinctions.

EIG therefore separates:

```text
What can the doctrine distinguish?
```

from

```text
Does the doctrine canonically select one representative among the compatible possibilities?
```

Conflating these is a recurrent source of false reconstruction claims.

## 6. The revised WEIR target

The strongest general target remains Witness-Enriched Interaction Reconstruction (WEIR), but the blind-calibration requirement should be read as a requirement on one frozen **meta-rule or schema**, parameterized only by the declared doctrine and not by the target answer. Doctrine-relative reconstruction does not require one literal extractor with identical syntax in every domain.

A successful general theorem should return, where appropriate:

```text
identifiable core
+ residual fibre/moduli
+ witness-enriched composition/descent
+ an exact statement of what extra resource closes each remaining boundary.
```

Literal reconstruction is one possible endpoint, not the only successful one.

## 7. Novelty posture

Many ingredients are classical: contextual minimization, behavioral quotients, Karoubi/Cauchy completion, factorization ranks, descent, fixed points, fibres, and interaction-first semantics all have substantial prior art.

The intended EIG discipline is narrower than a claim that nobody previously used those ingredients. The programme asks whether the same exact pattern — **maximal identifiable invariant, residual indistinguishability fibre, and minimal extra resource** — can organize reconstruction and no-go theorems across distant doctrines without target leakage.

That cross-domain programme remains open. This note records the sharpened formulation; it does not claim historical uniqueness for the formulation itself.
