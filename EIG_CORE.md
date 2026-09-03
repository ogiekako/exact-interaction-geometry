# Exact Interaction Geometry — Core Canonicality and Reconstruction

## Canonical semantic closure, doctrine dependence, and exact reconstruction boundaries

**Date:** 2026-09-03 JST  
**Status:** canonical research note  

This note states the generic EIG Core / EIG canonicality architecture, its exact hypotheses, reconstruction gates, and no-go boundaries.

No novelty or priority claim is made for standard constituent category theory, fixed-point theory, enriched Cauchy theory, distributive-law theory, descent theory, or higher-categorical section machinery.

---

# 0. Scope and structural synthesis

## 0.1 Structural conclusions

The framework rests on three structural conclusions:

1. **fixed-doctrine EIG Core is a simultaneous least semantic closure**, not a well-founded modality-stratified construction;
2. **doctrine selection and core descent are distinct problems**;
3. **the doctrine-free endpoint is generally moduli/fibration-valued rather than automatically point-valued**.

These conclusions are kept logically distinct and combined only where their hypotheses are compatible.

### Simultaneous closure and descent

The architecture replaces modality-stratified maximality by an order-independent simultaneous closure, and identifies descent of the doctrine-relative core along the doctrine-forgetful map as the correct doctrine-free question.

The corresponding no-go language is sharpened accordingly: noncontractibility of an undifferentiated solution/moduli space is not by itself an absolute obstruction to a canonical point.

### Closure modality, entailment, functoriality, and operation fibres

The following compatible results are included:

- the **full semantic closure modality** `Cl_D(S)` for arbitrary seeds `S`, with EIG Core as its value at the root;
- the **exact generation entailment/countermodel theorem**;
- **lax functoriality** of closure under forward doctrine morphisms, with equivalence invariance as a corollary;
- the **maximal sound law envelope** in a fixed admissible law language and the exact definability criterion;
- a useful **operation-restriction fibre** formalism.

The following formulations are excluded:

- obtaining the default semantic root by transporting a raw Tiny root through reduction, since contextual reduction need not preserve Tiny/Cauchy roots;
- treating raw nonempty noncontractible reconstruction fibres as already giving the exact final no-go;
- making internal definedness observable in a partial-context theorem unless it is explicitly admitted.

### Canonicality/no-go spine

The canonicality/no-go spine is characterized by:

- imposing the default order **REDUCE → intrinsic root in the reduced world → simultaneous closure**;
- isolating **root-exactness** as the exact bridge allowing raw-root-first computations;
- stating the maximally general **Moore-family existence criterion** before the monotone/Tarski specialization;
- separating internal least semantic closure from an external free algebraic/2-categorical completion;
- making the **full doctrine fibre**, including noninvertible maps, primary;
- applying contractibility only to a **fully specified solution problem**;
- using **problem-level homotopy fixed points/global sections** for genuine invariant-selection no-go theorems;
- distinguishing doctrine selection from common-core descent;
- identifying the **core-labelled full doctrine fibration** as the lossless doctrine-free packaging relative to the declared moduli problem;
- giving the walking-arrow counterexample showing that a noncontractible raw moduli space can nevertheless contain a canonical initial object.

## 0.2 Integration rule

The integration rule is:

> **Use reduced-world root extraction and simultaneous semantic closure as the logical spine. Retain every compatible orthogonal theorem only in a form that preserves that spine, the reduced-root ordering, and the specified-solution/invariant no-go boundary.**

The remainder of the note implements that rule.

---

# 1. Scope and canonicality convention

This note states each result together with the hypotheses under which it holds. Research-progress labels are not part of the mathematical presentation: standard inputs are identified in the text or references, statements that need additional assumptions state those assumptions directly, and stronger excluded claims are recorded as scope limits or counterexamples.

The word **canonical** will mean only one of:

- characterized by an explicit universal property;
- invariant under the declared equivalences of primitive input;
- unique through a contractible space of coherent choices;
- or, when no point is justified, canonically **moduli/fibration-valued**.

When this note uses “strongest” or “maximal,” it is relative to the declared universal problem, hypotheses, and equivalence level. It is not a novelty or priority claim.

---

# 2. The primitive doctrine and the no-smuggling firewall

## 2.1 Rebuilt coherent interaction doctrine

Fix a categorical level: ordinary, enriched, indexed, bicategorical/equipment-valued, or infinity-categorical. A coherent Level-2 EIG doctrine is schematically

$$
D=(\mathcal E_{\rm raw},\mathsf{Ctx},\mathsf{Obs},q,
\mathcal W_D,\mathsf{RootSpec},\mathsf{Op},\mathsf{Coh},
\mathcal W_D^{\rm str},\mathsf{Sub}_D,\simeq_D).
$$

The components have distinct logical roles.

### P1. Raw sectors

`E_raw` carries typed witnesses, native occurrences, provenance, ownership, histories, or other intensional structure.

### P2. Admitted contexts and observations

`Ctx` and `Obs` specify exactly which experiments and which outputs are operationally admitted. Success/failure is observable **only if explicitly included**.

### P3. Contextual reduction/exactification

`q:E_raw -> W_D` is either:

- derived from a proved universal reduction/localization/quotient property, or
- supplied semantic doctrine data.

These cases must not be conflated.

### P4. Reduced semantic world

`W_D` is the semantic world in which the EIG closure is formed.

### P5. Root-selector specification

`RootSpec` is an invariant universal predicate or Cauchy/absolute-weight notion. The **selector notion** may be primitive; the **selected root** is derived only when the selector is intrinsic/functorial in the declared setting.

### P6. Actual semantic operations

`Op` specifies each genuine semantic constructor with its arity, variance, domain, parameters, and whether it generates objects, cells, laws, or merely external valuations.

The semantic closure defining EIG Core acts only on the declared **Core-generating semantic sorts** — objects, cells, or higher cells that are components of an admissible structured subtheory. Law-producing operations are handled by the separate law layer of Section 10, and external valuations by the downstream operation/observation layer, unless a doctrine explicitly internalizes either as a semantic Core sort.

### P7. Non-forced coherence

`Coh` contains every distributive/interchange law, associator, descent datum, or higher coherence not uniquely forced by an already stated universal property.

### P8. Structural Hom/cell theory

`W_D^str` declares which maps, loose arrows, tight maps, cells, or modules constitute the associated EIG theory. Full ambient Homs are not assumed.

### P9. Admissible-subtheory universe

`Sub_D` is a set-sized complete lattice, or more generally a meet-complete Moore environment, of admissible replete/Cauchy-closed semantic subtheories/structured subobjects. This notation is reserved for semantic subtheories and is distinct from the law theories `L_D^comp` and `L_D^max` introduced in Section 10.

### P10. Equivalence level

`~_D` is explicitly one of isomorphism, categorical equivalence, Cauchy equivalence, Morita equivalence, indexed-equipment equivalence, or another specified localization.

## 2.2 Primitive/derived ledger

| Item | Status by default | Exact requirement |
|---|---|---|
| raw sectors, typing, native witnesses | primitive | supplied interaction doctrine |
| admitted contexts/observations | primitive | output-independent |
| contextual indistinguishability | derived | all admitted contexts |
| quotient/localization `q` | derived or supplied | derived only from proved universal property |
| root-selector notion | primitive notion | invariant/Cauchy specification |
| reduced root `R_D` | derived when selector applies | functorial selector |
| raw root | optional | separate from reduced root |
| `q(R_raw)` vs `R_red` comparison | conditional | root-exactness |
| semantic universal-construction values | derived when universal property exists | existence + typing |
| cross-operation BC/interchange invertibility | **not automatic** | separate exactness theorem |
| simultaneous closure modality | derived | Moore/Tarski hypotheses |
| modality order | optional computation data | factorization theorem required |
| density/nervousness | downstream recognition | separately proved |
| process/model reconstruction | downstream | all recognition/exactness gates |

## 2.3 No-smuggling condition

A doctrine or selection specification is **output-free** relative to a claimed theorem when it does not contain, under another name:

- the desired EIG arity/core subtheory;
- a predicate extensionally equal to the desired essential image without independent justification;
- target-specific coherence/laws inserted only to force the desired result.

This provenance condition is external to the fixed-point mathematics but is necessary for any substantive canonicality claim.

---

# 3. Contextual reduction: Set-like theorem and higher-level boundary

## 3.1 All-context observational equivalence

For same-typed raw cells `x,y`, define

$$
x\sim_D y
\iff
\text{every admitted closing context produces the same admitted observable result on }x,y.
$$

If failure is an admitted result, it participates in the comparison. If failure is hidden, internal definedness is **not** silently added to `Obs`.

## 3.2 Universal contextual quotient

Assume `~_D` is a typed congruence in the selected partial-algebra/restriction sense and the quotient exists:

$$
q_D:\mathcal E_{\rm raw}\twoheadrightarrow \mathcal E_{\rm raw}/\!\sim_D.
$$

It has two distinct universal properties.

### Q1. Congruence-quotient universality

If `h:E_raw -> T` is compositional and

$$
x\sim_D y\Rightarrow h(x)=h(y),
$$

then uniquely

$$
h=\bar h\,q_D.
$$

Thus `q_D` is initial among maps coequalizing contextual equivalence.

### Q2. Coarsest faithful surjective interface

If a surjective compositional interface `f:E_raw -> T` satisfies

$$
f(x)=f(y)\Rightarrow x\sim_D y,
$$

then uniquely

$$
q_D=r f.
$$

Thus, in the category of sound surjective interfaces ordered by further quotienting, `q_D` is terminal: it is the coarsest interface that loses no admitted observational distinction.

These are different factorization directions and should never be merged under one informal “initial quotient” slogan.

## 3.3 Exact contextual no-go

If an admitted closing context distinguishes `x` and `y`, every context-faithful quotient/interface must keep them distinct. Hence in the Set-like quotientable sector, positive separatedification and negative identifiability are exact dual sides of the same contextual relation.

## 3.4 Failure-observable totalization

When failure is public, replace every sort `X` by

$$
X_\bot=X+\{\bot\}
$$

and every partial context by a total map sending undefined execution to `bot`. Then equality of all totalized closing observations is exactly equality of success/failure and, upon success, the observed value. This converts the partial observational theory to an ordinary total congruence problem without smuggling definedness.

## 3.5 Hidden-failure alternative

When failure is not public, no such totalization may be used without changing the doctrine. Work instead with an explicit category of partial maps/restriction categories or partial algebras, choose the morphism notion, and prove contextual equivalence is a congruence there.

## 3.6 Greatest-fixed-point computation

In a step-generated **failure-observable totalized** setting, define the standard relation transformer requiring equality of primitive outputs and recursive relatedness of step outputs. Its greatest fixed point is contained in all-closing-context equivalence; equality holds under the usual closing-viability hypothesis that every reachable step output admits an admitted finite closing continuation capable of exposing a difference. The direct all-context relation remains primary when that hypothesis is absent.

## 3.7 Higher/enriched boundary

In higher settings replace the Set quotient by the correct localization, coinverter, codescent object, effective quotient, stack quotient, or homotopy image. Nothing in the Set theorem proves that such an object exists or is effective in a richer doctrine.

---

# 4. Intrinsic roots: reduced-world first, with an exact bridge theorem

## 4.1 Ordinary presheaf root

For a small ordinary category `C`, in

$$
\widehat C=[C^{op},\mathbf{Set}],
$$

objects `P` for which `Hom(P,-)` preserves all small colimits are exactly retracts of representables. Therefore

$$
\mathrm{Tiny}(\widehat C)\simeq\mathrm{Kar}(C).
$$

This is equivalence-invariant in the ordinary presheaf sector.

## 4.2 Enriched root

For a suitable symmetric monoidal closed base `V`, the correct enriched replacement is the Cauchy/absolute-weight completion `Q(C)` inside `[C^op,V]`. Ordinary `Kar(C)` language is insufficient in general.

## 4.3 Indexed/equipment roots

Fibrewise roots must be preserved pseudonaturally by reindexing. In equipment/AVDC settings, the correct atomic/Cauchy notion may involve absolute modules, adjoint modules, representable proarrows, or collage-atomic objects. No theorem identifies arbitrary equipment roots with ordinary objectwise Tiny objects.

Known profunctor/equipment characterizations may be used as calibrations **inside their declared doctrine**, not as doctrine selectors from bare lower semantics.

## 4.4 Reduced root — default definition

After contextual reduction/exactification

$$
q:\mathcal E_{\rm raw}\to\mathcal W_D,
$$

define

$$
\boxed{R_D:=R_D^{\rm red}:=\mathsf{RootSpec}(\mathcal W_D).}
$$

This is the root used by the master closure theorem.

A raw root, when independently meaningful, is a separate object

$$
R_D^{\rm raw}:=\mathsf{RootSpec}_{\rm raw}(\mathcal E_{\rm raw}),
\qquad
R_D^{\rm tr}:=\mathrm{Cauchy/Repl}(qR_D^{\rm raw}).
$$

There is no default equality

$$
R_D^{\rm tr}\simeq R_D^{\rm red}.
$$

## 4.5 REDUCE need not preserve Tiny

Consider the reflection

$$
L:\mathrm{Arr}(\mathbf{Set})\to\mathbf{Set},
\qquad
(X\to Y)\mapsto X,
$$

where `Set` is identified with terminal-codomain arrows. The arrow

$$
\varnothing\to 1
$$

is Tiny in `Arr(Set)` because its Hom functor is codomain evaluation, but its image `emptyset` is not Tiny in `Set` since `Set(emptyset,-)=1` fails to preserve the empty colimit.

Therefore reflective reduction alone does not justify raw-root-first semantics.

## 4.6 Root-exactness — exact bridge

Call `q` **root-exact** when the canonical comparison

$$
\mathrm{Cauchy/Repl}(qR_D^{\rm raw})
\longrightarrow
R_D^{\rm red}
$$

is an equivalence at the declared level.

A clean sufficient package is:

1. reduction sends raw root objects to reduced root objects; and
2. their images Cauchy-generate every reduced root object.

For ordinary Tiny roots, a sufficient condition for (1) is that the right adjoint of the reflection preserve the colimits relevant to small projectivity.

**Master ordering rule:**

```text
admitted contexts/observations
    -> universal reduction/exactification
    -> intrinsic root in the reduced world
    -> semantic closure.
```

Raw-root-first is a derived computational shortcut only after root-exactness is proved.

---

# 5. The fixed-doctrine invariant: the full semantic closure modality

The strongest fixed-doctrine object is not only one root-generated class. It is the **entire closure modality** on all admissible seed subtheories. EIG Core is one distinguished value of this modality.

## 5.1 Moore-family existence theorem

Fix a complete or meet-complete admissible lattice `Sub_D`. Let `Closed_D` be the family of admissible `D`-closed elements. For any seed `S`, let

$$
\mathcal M_D(S)=\{B\in\mathrm{Closed}_D:S\le B\}.
$$

Assume:

1. `M_D(S)` is nonempty; and
2. it is closed under arbitrary meets in `Sub_D`.

Define

$$
\boxed{
\mathrm{Cl}_D(S):=\bigwedge\mathcal M_D(S).
}
$$

Then `Cl_D(S)` is the least `D`-closed admissible element above `S`.

Conversely, if every seed has a least closed upper bound, the assignment `Cl_D` is extensive, monotone, and idempotent, and its fixed elements form a Moore family.

### Proof

Meet-closure makes `∧M_D(S)` itself closed. It contains `S` and is below every closed upper bound. The closure-operator laws follow from leastness. Conversely, fixed points of any closure operator are closed under meets because `Cl(∧B_i) <= B_i` for every fixed `B_i`, while extensivity supplies the reverse inequality. ∎

### Exact existence boundary

This is more general than Tarski. It also shows what can fail: negative/exclusive choice rules need not define a Moore family, and then a least point-valued core need not exist.

## 5.2 Positive many-sorted semantic generation instance formulation

Let `Sort_D^core` be the declared family of semantic sorts that participate in EIG Core closure. These may include objects, cells, and higher cells, with the incidence/domain/codomain structure required by `W_D^str`. An admissible element

$$
A\in\mathsf{Sub}_D
$$

is therefore a structured family of components `A_sigma` for `sigma in Sort_D^core`, not merely an object class.

Let `Inst_D` be the universe-bounded family of all actual **Core-generating** positive semantic instances in the reduced world. An instance `xi` has:

- a set-sized typed support `supp(xi)`;
- any fixed structural diagram/parameters required by the doctrine;
- an output sort `sort(xi) in Sort_D^core`;
- an output `out(xi)` of that sort.

Admissibility of an instance is doctrine data and does not depend on the candidate closed structured subtheory. A candidate `A` only determines whether every typed entry of `supp(xi)` is present, with the required incidences landing in `A`.

An admissible structured subtheory `A` is **D-stable** if it is:

1. replete under the declared equivalence;
2. closed under the declared Cauchy/split-retract completion;
3. closed under every actual Core-generating semantic instance:
$$
   \mathrm{supp}(\xi)\le A
   \Rightarrow
   \mathrm{out}(\xi)\in_{\mathrm{sort}(\xi)} A.
$$

Root containment is deliberately not part of “stable”.

In the ordinary inclusion-realized presentation, meets in `Sub_D` are computed componentwise on the declared semantic sorts. Hence arbitrary meets/intersections of `D`-stable structured subtheories are again `D`-stable: if a typed support lies in the meet, it lies in every factor, so the typed output lies in every factor and therefore in the meet.

Law-producing rules are not silently folded into this semantic membership relation. They feed the separate `Law_D` / theory-model layer of Section 10 unless the doctrine has explicitly declared laws themselves to be a Core-generating semantic sort.

## 5.3 Closure modality theorem

Under the Moore-family hypotheses of Section 5.1, for every admissible seed `S in Sub_D`,

$$
\boxed{
\mathrm{Cl}_D(S)
=
\bigwedge\{B\in\mathsf{Sub}_D:S\le B,\ B\text{ is D-stable}\}.
}
$$

It is the unique least `D`-stable semantic structured subtheory above `S`, and

$$
S\le\mathrm{Cl}_D(S),
$$

$$
S\le T
\Rightarrow
\mathrm{Cl}_D(S)\le\mathrm{Cl}_D(T),
$$

$$
\mathrm{Cl}_D(\mathrm{Cl}_D(S))
=
\mathrm{Cl}_D(S).
$$

Thus a fixed doctrine canonically determines an idempotent semantic closure modality, not merely a single preferred class.

In the ordinary powerset-like/many-sorted inclusion presentation of Section 5.2, the meet is componentwise literal intersection, so the same formula may be written

$$
\mathrm{Cl}_D(S)
=
\bigcap\{B:S\subseteq B,\ B\text{ is D-stable}\}.
$$

The meet formula is primary in the general structured lattice.

## 5.4 EIG Core — fixed-doctrine definition

The EIG Core is

$$
\boxed{
\mathrm{EIGCore}(D)
:=
\mathrm{Cl}_D(R_D),
}
$$

where `R_D` is the intrinsic **reduced** root.

Equivalently, in the admissible structured lattice,

$$
\mathrm{EIGCore}(D)
=
\bigwedge
\{B\in\mathsf{Sub}_D:R_D\le B,\ B\text{ is D-stable}\}.
$$

In the inclusion-realized presentation this meet is the corresponding componentwise intersection.

This formulation is stronger than a root-specific fixed point because it remembers the whole modality `Cl_D`, while retaining the same core as its root value.

## 5.5 Exact generation entailment / countermodel theorem

For any admissible seed `S`, any generated Core sort `sigma`, and any semantic element `x` of sort `sigma`,

$$
\boxed{
x\in_\sigma\mathrm{Cl}_D(S)
\iff
\forall B\in\mathsf{Sub}_D\,[S\le B\land B\text{ D-stable}\Rightarrow x\in_\sigma B].
}
$$

Therefore

$$
\boxed{
x\notin_\sigma\mathrm{Cl}_D(S)
\iff
\exists B\in\mathsf{Sub}_D\text{ with }S\le B,\ B\text{ D-stable, and }x\notin_\sigma B.
}
$$

When `x` is outside the closure, `Cl_D(S)` itself is a countermodel.

This is an **exact no-go ceiling for generation by the declared D-stability rules on the declared Core sorts**. It must not be overread as saying that `x` cannot be canonically defined by some different, independently supplied structure.

## 5.6 Tarski operator form

Let

$$
C_D:\mathsf{Sub}_D\to\mathsf{Sub}_D
$$

be the closure operator implementing repletion plus the declared Cauchy closure. For each Core-generating rule `rho`, let

$$
G_\rho:\mathsf{Sub}_D\to\mathsf{Sub}_D
$$

be monotone. Define, for seed `S`,

$$
\Gamma_{D,S}(A)
=
C_D\left(
S\vee A\vee\bigvee_{\rho}G_\rho(A)
\right).
$$

Then

$$
\boxed{
\mathrm{Cl}_D(S)=\mu\Gamma_{D,S}.
}
$$

In particular,

$$
\mathrm{EIGCore}(D)=\mu\Gamma_{D,R_D}.
$$

In a powerset-like inclusion realization, the joins above are the corresponding typed unions. No modality order, well-founded dependency relation, or separately postulated cyclic fixed point is needed.

## 5.7 Transfinite and finitary computation

Let

$$
A_0=C_D(S),\qquad
A_{\alpha+1}=\Gamma_{D,S}(A_\alpha),\qquad
A_\lambda=\bigvee_{\beta<\lambda}A_\beta.
$$

- If `Gamma_{D,S}` preserves joins of `kappa`-directed families for regular `kappa`, then `A_kappa=Cl_D(S)`.
- If it preserves directed joins, `omega` iteration suffices.
- With only monotonicity, Knaster-Tarski gives existence but no `omega`-stage claim.
- On a set-sized object skeleton, an inflationary chain stabilizes before the corresponding successor cardinal; for genuinely structured subtheories, use the size/accessibility bound of the structured lattice.

## 5.8 Retracts/Cauchy completion participate inside the fixed point

One final `Kar` after constructor generation is not sound for partial/domain-sensitive constructors. A retract may appear only after Cauchy closure and then activate a constructor that must be revisited. Therefore Cauchy/retract closure belongs in `C_D` at every stage or, equivalently, in the definition of the admissible closed lattice.

## 5.9 Schedule independence

Any generation schedule that:

1. starts from `S`;
2. adds only repletion/Cauchy consequences and outputs of currently applicable genuine `D`-instances; and
3. reaches a `D`-stable class,

ends exactly at `Cl_D(S)`.

Every intermediate object lies in every stable upper bound, hence in `Cl_D(S)`; the final stable class must conversely contain the least stable closure.

---

# 6. Functoriality: stronger than equivalence invariance

A **forward functoriality theorem** for the closure modality strengthens equivalence-only transport without altering the fixed-doctrine maximality boundary.

## 6.1 Forward doctrine morphism

A forward doctrine morphism

$$
F:D\to D'
$$

contains a semantic structural functor/cell map

$$
F_W:\mathcal W_D^{\rm str}\to\mathcal W_{D'}^{\rm str}.
$$

For every admissible structured seed/subtheory `A in Sub_D`, assume the image admits a least target-admissible hull

$$
F_\sharp(A)
:=
\mathrm{AdmHull}_{D'}(F_W(A))
\in\mathsf{Sub}_{D'}.
$$

The forward-morphism hypotheses are:

1. declared equivalences are preserved;
2. the admissible hulls `F_sharp(A)` required above exist;
3. for every `D'`-closed admissible `B in Sub_{D'}`, the structured inverse image `F_W^{-1}(B)` is an admissible replete/Cauchy-closed element of `Sub_D`;
4. every source Core-generating semantic instance transports to an admissible target Core-generating instance with transported support and equivalent transported output;
5. all typing, domains, incidences, and coherence required for this transport are preserved;
6. for the root-specific theorem,
$$
   F_\sharp(R_D)\le \mathrm{Cl}_{D'}(R_{D'}).
$$

For arbitrary-seed functoriality, condition 6 is unnecessary. Conditions 2–3 are the admissibility hypotheses that make both sides of the comparison and the inverse-image proof well typed; they are not implied by preservation of equivalences alone.

## 6.2 Lax naturality of closure

For every admissible seed `S in Sub_D`,

$$
\boxed{
F_\sharp(\mathrm{Cl}_D(S))
\le
\mathrm{Cl}_{D'}(F_\sharp(S)).
}
$$

### Proof

Let

$$
C=\mathrm{Cl}_{D'}(F_\sharp(S)),
\qquad
B=F_W^{-1}(C).
$$

By hypothesis 3, `B` is an admissible replete/Cauchy-closed element of `Sub_D`. Since `F_W(S)` lies in its admissible hull `F_sharp(S)`, and `F_sharp(S) <= C`, we have `S <= B`.

If a source Core-generating instance has typed support in `B`, hypothesis 4 transports it to a target instance with support in `C`; target stability puts its output in `C`, hence the source output lies in `B`. Therefore `B` is `D`-stable. Leastness gives

$$
\mathrm{Cl}_D(S)\le B.
$$

Applying `F_W`, its image lies in `C`; by leastness of the target admissible hull,

$$
F_\sharp(\mathrm{Cl}_D(S))\le C
=
\mathrm{Cl}_{D'}(F_\sharp(S)).
$$

This is the claimed typed forward comparison. ∎

## 6.3 Core functoriality

If `F` also satisfies the root condition 6 above, then

$$
\boxed{
F_\sharp(\mathrm{EIGCore}(D))
\le
\mathrm{EIGCore}(D').
}
$$

Indeed, Section 6.2 gives

$$
F_\sharp(\mathrm{Cl}_D(R_D))
\le
\mathrm{Cl}_{D'}(F_\sharp(R_D))
\le
\mathrm{Cl}_{D'}(\mathrm{EIGCore}(D'))
=
\mathrm{EIGCore}(D').
$$

Thus on the category of forward doctrine morphisms satisfying these hypotheses, EIG Core is a typed lax-functorial assignment rather than merely an equivalence invariant.

## 6.4 Equivalence invariance **[COROLLARY]**

If `F` is an equivalence of primitive coherent doctrines with a structure-preserving quasi-inverse satisfying the same admissibility/transport hypotheses, the two lax comparisons yield

$$
F_\sharp(\mathrm{Cl}_D(S))
\simeq
\mathrm{Cl}_{D'}(F_\sharp(S)),
$$

and in particular

$$
\boxed{
\mathrm{EIGCore}(D)
\simeq
\mathrm{EIGCore}(D').
}
$$

No separate preservation axiom for a genuinely derived reduced root or core is needed once the primitive selector/reduction data and admissible-subtheory structure are transported.

## 6.5 Exact functoriality boundary

If the doctrine category contains maps that do **not** preserve generation instances, roots, or coherence sufficiently to define the comparison, no generic noninvertible-map functor `K:D_2->C` has been proved. In every later descent theorem, use:

- the full forward-morphism category when this functoriality has been established;
- otherwise the maximal subgroupoids/equivalence cores.

This prevents descent notation from silently assuming stronger functoriality than the closure theorem provides.

---

# 7. The exact meaning of “free” and the strongest universal property

## 7.1 Construction-independent completion problem

Let

$$
\mathrm{Comp}_D(R_D)
$$

be the declared category/2-category/infinity-category of admissible coherent `D`-closed realizations receiving `R_D`.

### Theorem 7.1 — abstract maximal criterion

A free coherent completion exists **iff** `Comp_D(R_D)` has an initial object. When it exists, the infinity-groupoid of initial objects is contractible.

This is the strongest construction-independent statement. It does not itself prove existence.

## 7.2 Internal reflection theorem

Inside the semantic world, let `RootSub_D(W_D)` be admissible rooted subtheories and `Closed_D(W_D)` its full subposet of `D`-closed subtheories. Then

$$
\mathrm{Cl}_D\dashv
\bigl(\mathrm{Closed}_D(W_D)\hookrightarrow\mathrm{RootSub}_D(W_D)\bigr).
$$

Equivalently, `EIGCore(D)=Cl_D(R_D)` is initial among **internal semantic** `D`-closed subtheories receiving the root.

This is an unconditional genuine free/least universal property under the Moore hypotheses.

## 7.3 Why this is not automatically an external free algebra

The semantic operations already live in `W_D` and may satisfy identifications not forced by a free syntax. If an external free syntax exists,

$$
F_D(R_D)\to W_D,
$$

the internal core is generally the replete/Cauchy closure of its semantic image. It is equivalent to the free syntax only when the interpretation is fully faithful at the declared level.

Therefore:

> **Strongest unconditional statement:** internal least semantic closure/reflection.  
> **Stronger external free-algebra/2-categorical completion:** conditional on a separately proved algebraic presentation, existence theorem, and appropriate faithfulness.

## 7.4 Accessible monadic/2-monadic completion

If the doctrine is presented by a suitable accessible monad, 2-monad, pseudomonad, relative pseudomonad, or sketch on a locally presentable ambient setting, the corresponding forgetful functor may admit a left adjoint/free completion. KZ/lax-idempotence is a further theorem, not a consequence of the word “completion”.

---

# 8. Modality stratification is only a factorization/computation theorem

## 8.1 Individual closure operators

Suppose modalities determine closure operators

$$
c_1,\ldots,c_n:\mathsf{Sub}_D\to\mathsf{Sub}_D.
$$

Let `c_vee` denote the least common closure.

## 8.2 Ordered factorization theorem

If for every `i<j`, the later closure `c_j` preserves `c_i`-closed objects, equivalently

$$
c_i c_j\le c_j c_i,
$$

then

$$
\boxed{c_\vee=c_n\cdots c_1.}
$$

For two closures, `dc(A)` is simultaneously `c`-closed and `d`-closed under the preservation hypothesis and is below every common closed upper bound. Induction gives the finite statement.

If all closures commute, every ordering computes the same simultaneous closure.

## 8.3 Cycles

When no acyclic orientation satisfies the preservation conditions, use the joint least fixed point. Cyclic dependence is not an existence obstruction under the Moore/Tarski hypotheses.

## 8.4 Higher-categorical replacement

In a 2/higher setting, order inequalities are replaced by distributive/comparison transformations. Three separate gates are required:

1. existence of comparison transformations;
2. invertibility/preservation of local objects when needed;
3. Yang-Baxter and higher coherence sufficient to compose the closures.

In the strict ordinary-monad setting, Cheng’s iterated distributive-law theorem shows that pairwise laws satisfying all triple Yang-Baxter equations yield the iterated composite. This strict result cannot be silently transferred to arbitrary pseudomonads, partial operations, or equipments.

## 8.5 Strongest conclusion

A historical SYNC/STORE/SPACE/SEQ order may be extremely useful, but it is **not the source of EIG canonicality**. Its strongest role is:

> a theorem that a particular ordered composite computes the already-defined simultaneous closure.

---

# 9. Coherence and the exact single-monad boundary

## 9.1 Universality: what is and is not forced

Universal properties can force representing objects and canonical comparison maps/mates. They do **not** automatically force:

- Beck-Chevalley invertibility;
- pullback stability of images/codescent;
- effective descent;
- interchange with unrelated constructors;
- representability of modules/proarrows;
- chosen higher coherence across several universal constructions.

Each such strengthening is an independent exactness/coherence theorem.

## 9.2 Distributive laws may fail to exist

There are pairs of ordinary monads with no distributive law; published no-go results include the failure of the list monad to distribute over itself in the required sense. Therefore a mixed-monad package cannot be presumed from the separate existence of two modalities.

## 9.3 Pairwise laws require independent Yang-Baxter coherence

For three or more monads, the standard iterated-distributive-law theorem requires the pairwise distributive laws to satisfy the Yang-Baxter equations. Pairwise law existence by itself is therefore not a theorem of coherent triple composition; Yang-Baxter is separate coherence data.

This note does **not** claim the earlier writer-monad “noncommuting actions” slogan as a proof-complete calibration. For writer monads arising from monoids, the modern monadic-container characterization identifies writer-writer distributive laws with **matching pairs of monoid actions**, not one undifferentiated naive action datum. The exact boundary used here is imported from the standard iterated-distributive-law and no-go literature: Cheng proves composition from pairwise laws satisfying Yang-Baxter, while Zwart–Marsden give obstructions showing that proposed iterated compositions can fail. Section 19.4 records the references.

## 9.4 Higher coherence may be nonunique

`G`-graded vector spaces admit associators twisted by inequivalent normalized `3`-cocycles. Thus identical object labels and binary tensor skeletons can support inequivalent higher coherence.

## 9.5 Coherent mixed packages may be nonunique

Trivial versus inversion actions of `C_2` on `C_3` yield distinct semidirect composites (`C_6` versus `S_3`) from the same constituent writer modalities.

## 9.6 Exact single-monad adjudication

The statement

```text
different variance/roles imply that no single monad can encode EIG
```

is **FALSE**.

The strongest correct statement is:

> **No canonical homogeneous BMW-style endomonad compression is forced merely by the primitive EIG constructor list.** A monadic package requires a chosen base/sorting scheme, distributive/interchange laws, the appropriate coherence, and a presentation convention. It may fail to exist; when it exists it may be nonunique.

Multi-sorted monads, colored polynomial monads, 2-monads, sketches, relative pseudomonads, or monads in equipments may encode particular doctrines. Such encodings are additional structures/constructions, not doctrine-free consequences.

---

# 10. Associated EIG theory and the maximal law envelope

## 10.1 Associated structural theory

After generating the core, define

$$
\boxed{
\Theta_D
:=
\mathcal W_D^{\rm str}\big|_{\mathrm{EIGCore}(D)}.
}
$$

This is the restriction of the **declared structural** Hom/cell doctrine. It is not automatically the full ambient Hom category. In witness-sensitive or equipment-valued semantics, using all ambient Homs can erase precisely the provenance/loose-arrow structure EIG intends to retain.

Let

$$
J_D:\Theta_D\hookrightarrow\mathcal W_D^{\rm str}
$$

be the arity inclusion.

## 10.2 Certified cellular law compiler

Suppose a calibration supplies, independently of the desired recognition result:

1. elementary/generic shapes;
2. invariant occurrence maps;
3. incidence/restriction/overlap data;
4. constructor-derived decomposition certificates;
5. typed sound inference schemes.

Let `Lambda_0` be all elementary laws certified by these data and `Sat_D` the least closure under the certified inference rules. Define

$$
\mathcal L_D^{\rm comp}
:=
\mathrm{Sat}_D(\Lambda_0).
$$

Every genuine restricted-nerve object satisfies every law in `L_D^comp` by induction on certified derivations.

This compiler is constructive and provenance-controlled. It must not be declared complete merely because its target laws look natural.

## 10.3 Fixed admissible law language

Fix independently an admissible law language `Law_D` and satisfaction relation `X |= ell`. For classes `S` and law sets `Lambda`, define

$$
\mathrm{Th}_D(S)
:=
\{\ell\in\mathsf{Law}_D:\forall X\in S,\ X\models\ell\},
$$

$$
\mathrm{Mod}_D(\Lambda)
:=
\{X:\forall\ell\in\Lambda,\ X\models\ell\}.
$$

Then

$$
\Lambda\subseteq\mathrm{Th}_D(S)
\iff
S\subseteq\mathrm{Mod}_D(\Lambda),
$$

the standard antitone theory/model Galois connection.

## 10.4 Maximal sound law theory

Let

$$
G_D:=\mathrm{EssIm}(N_D)
$$

be the genuine restricted-nerve image, whenever the nerve is defined. Set

$$
\boxed{
\mathcal L_D^{\max}
:=
\mathrm{Th}_D(G_D).
}
$$

This is the **maximal sound theory expressible in the fixed law language**. Compiler soundness gives

$$
\mathcal L_D^{\rm comp}
\subseteq
\mathcal L_D^{\max}.
$$

This semantic maximum is a ceiling/diagnostic, not a construction of the EIG Core and not a license to smuggle the desired essential image into the doctrine.

## 10.5 Definability closure and exact law-language recognition

Define

$$
\mathrm{Def}_D(S)
:=
\mathrm{Mod}_D(\mathrm{Th}_D(S)).
$$

This is the smallest class containing `S` that is definable by arbitrary law sets in `Law_D`.

Then the genuine nerve image is exactly recognizable in that language **iff**

$$
\boxed{
G_D
=
\mathrm{Def}_D(G_D)
=
\mathrm{Mod}_D(\mathcal L_D^{\max}).
}
$$

### Proof

If `G_D=Mod_D(Lambda)`, then `Lambda subseteq Th_D(G_D)`, hence

$$
\mathrm{Mod}_D(\mathrm{Th}_D(G_D))
\subseteq
\mathrm{Mod}_D(\Lambda)=G_D.
$$

The reverse inclusion always holds. Conversely, if `G_D=Mod_D(Th_D(G_D))`, the maximal sound theory defines the image. ∎

## 10.6 Exact language no-go

If

$$
G_D
\subsetneq
\mathrm{Def}_D(G_D),
$$

then **no law set in the chosen admissible language** exactly characterizes the genuine nerve image.

This is stronger than failure of one proof calculus.

Two distinct failures are therefore separated:

- **compiler incompleteness:** `L_comp subsetneq L_max`;
- **language insufficiency:** `G_D subsetneq Def_D(G_D)`.

The first may be repaired by stronger independently justified inference rules. The second cannot be repaired without changing the law language.

---

# 11. Recognition, density, and external operations

Construction and recognition remain logically separate.

## 11.1 Restricted nerve

In the ordinary case,

$$
N_D(X)=\mathcal W_D^{\rm str}(J_D-,X).
$$

Density means `N_D` is fully faithful at the declared level. A canonical root/least closure need not be dense.

A decisive ordinary example is `Ab` with the “all small colimits” Tiny notion: `Hom(P,0)` is always a singleton, while the empty colimit in `Set` is empty, so no object is Tiny. The resulting empty-root nerve cannot reconstruct `Ab`. Hence **intrinsic root canonicality and density are independent**.

## 11.2 Exact local-law recognition

At a fixed law language, exact local recognition requires at least:

1. `N_D` fully faithful;
2. `G_D=Def_D(G_D)`.

If the **constructive compiler itself** is claimed to present the image, additionally require

$$
\mathrm{Mod}_D(\mathcal L_D^{\rm comp})=G_D.
$$

## 11.3 Operation restriction map

Let `Op_D` be the declared category/infinity-category of admissible external/world operations of a fixed signature, and let `Data_J` be the category of arity-level data retained by restriction, including modules/proarrows when representability is not assumed.

Define

$$
\mathrm{Res}_J:\mathrm{Op}_D\to\mathrm{Data}_J.
$$

For data `d`, let

$$
\mathrm{Fib}_J(d)
:=
\mathrm{hofib}_d(\mathrm{Res}_J).
$$

## 11.4 Corrected operation-identifiability theorem

The strongest valid form is the same specified-solution principle used later for doctrine canonicality.

### Bare arity-only problem

If the requested reconstruction problem is **only**

> choose an admissible operation realizing exactly the arity datum `d`, with no further intrinsic condition,

then the maximal subgroupoid of `Fib_J(d)` is the exact bare solution space:

- empty: no admitted realization exists;
- contractible: the operation is uniquely determined up to coherent equivalence by that bare arity datum;
- nonempty noncontractible: the bare restriction datum alone does not force uniqueness.

For `d=Res_J(K)`, the fibre is automatically nonempty.

### Specified operation problem

If a stronger independently justified universal condition `P_op` is part of what “the operation” means, restrict to the `P_op`-solutions inside the full fibre and test **that** solution space. A noncontractible raw fibre does not rule out a canonical initial/minimal/reflective operation inside it.

### Sharp invariant no-go

If the declared whole operation-reconstruction problem has an automorphism action and the corresponding specified invariant-solution space/homotopy-fixed-point space is empty, no equivalence-invariant reconstruction exists from that declared problem.

This is the specified-solution form of the operation-restriction fibre statement.

## 11.5 Fully faithful restriction **[SUFFICIENT]**

If `Res_J` is fully faithful on a subcategory of admissible operations, the operation and its morphisms/coherences are identifiable there from arity data.

## 11.6 Coend/module reconstruction

For an operation

$$
K:\mathcal W_1\times\cdots\times\mathcal W_m\to\mathcal W_0,
$$

define the arity module

$$
M_K(b;a_1,\ldots,a_m)
=
\mathcal W_0^{\rm str}
(J_0b,K(J_1a_1,\ldots,J_ma_m)).
$$

The canonical comparison

$$
\int^{a_1,\ldots,a_m}
M_K(b;\vec a)
\otimes
\prod_i N_i(X_i)(a_i)
\longrightarrow
N_0(K(\vec X))(b)
$$

being invertible is a strong constructive operation-exactness theorem. Its failure is **not** the maximal abstract no-go: another invariant reconstruction might exist. The correct general boundary is the specified operation-solution problem above.

If the natural arity datum is a module/proarrow and is not representable by a functor, the module/proarrow is the correct canonical output rather than a failed functor representation.

## 11.7 Reconstruction gates

A process/model reconstruction theorem is downstream of:

1. valid reduced root;
2. valid semantic closure;
3. density/faithfulness;
4. exact essential-image recognition;
5. operation exactness for each claimed operation;
6. indexed/equipment coherence and exactness;
7. realization in the intended semantic class.

Failure of a recognition gate does not refute fixed-doctrine EIG Core canonicality.

---

# 12. Universal canonicality principle

The slogan “canonicality is contractibility of the reconstruction fibre” becomes exactly correct only after the **entire requested universal property has been built into the solution problem**.

## 12.1 Specified solution category

For a declared mathematical problem `P`, let

$$
\mathrm{Sol}(P)
$$

be the full category/infinity-category of solutions satisfying **all** conditions that define the requested object, including initiality, terminality, minimality, reflection, exactness, or any other independently justified universal property.

Let

$$
\mathrm{Sol}(P)^{\simeq}
$$

be its maximal infinity-groupoid.

### Theorem 12.1 — exact specified-solution trichotomy

- `Sol(P)^simeq = emptyset` iff no `P`-solution exists.
- `Sol(P)^simeq` contractible iff the `P`-solution is canonical up to contractible coherent choice.
- nonempty noncontractible means the **stated conditions P** do not uniquely determine a solution.

The third clause is deliberately local to `P`: a stronger independently justified specification `P'` may still select one point.

## 12.2 Why raw moduli noncontractibility is not an absolute no-go

Let the full candidate category be the walking arrow

$$
[1]=(0\to1).
$$

Its maximal subgroupoid is a discrete two-point space, hence noncontractible. Nevertheless `0` is an initial object, and the space of initial objects is contractible.

Therefore:

$$
\boxed{
\text{raw noncontractible moduli}
\centernot\Rightarrow
\text{no canonical point exists}.
}
$$

Passing immediately to the maximal subgroupoid can erase the noninvertible arrows that witness universal canonicality.

## 12.3 Problem-level invariance

Fix a category/infinity-category `M` of declared reconstruction problems and their equivalences. If solution spaces vary functorially over `M`, automorphisms of a problem act on its specified solution space.

On a connected equivalence component, an **equivalence-invariant** specified solution is a homotopy fixed point

$$
\mathrm{Sol}(P)^{\simeq,h\mathrm{Aut}_{\mathcal M}(P)}.
$$

If this invariant-solution space is empty, there is a sharp symmetry no-go.

Across noninvertible maps of problems, the exact naturality condition is a global section of the universal solution fibration, not merely objectwise fixed points.

---

# 13. Doctrine fibres: exact selection theorem

## 13.1 Forgetful doctrine fibration

Let

$$
U:\mathcal D_2\to\mathcal S_1
$$

forget coherent Level-2 interaction structure down to an admissible lower semantic base. Restrict `S_1` to objects admitting at least one compatible doctrine and maps along which the selected variance supports reindexing.

In the contravariant convention, model `U` as a cartesian fibration classified by

$$
\mathcal F:\mathcal S_1^{op}\to\mathbf{Cat}_\infty.
$$

Write

$$
\mathcal F_X=\mathcal F(X),
\qquad
\mathfrak F_X=\mathcal F_X^{\simeq}.
$$

The **full fibre** `F_X`, not only its groupoid core, is primary because noninvertible maps can encode refinement, localization, reflection, initiality, or terminality.

## 13.2 Doctrine selection = section

A coherent doctrine selector is exactly a cartesian section

$$
s:\mathcal S_1\to\mathcal D_2,
\qquad
Us\simeq1_{\mathcal S_1},
$$

or cocartesian section in the covariant convention.

The category of sections is the corresponding limit of the fibre functor.

## 13.3 Equivalence component = homotopy fixed points

On the equivalence component of `X`, equivalent to `B Aut(X)`, the space of **bare** doctrine selections is

$$
\boxed{
\mathfrak F_X^{h\mathrm{Aut}(X)}.
}
$$

This classifies bare equivalence-invariant choices on that component. It does not by itself solve naturality over noninvertible semantic maps.

## 13.4 Specified doctrine selection

For an invariant selection property `P` — e.g. pointwise initial, reflective, minimal under an independently defined order, or exact in a specified sense — let

$$
\mathrm{Sel}_P(U)
$$

be the space of coherent sections satisfying `P`.

Then the exact trichotomy of Section 12 applies. For the **whole problem** `(U,P)`, the problem-level homotopy-fixed-point/global-section criterion supplies the exact invariant-selection no-go.

## 13.5 Always-defined doctrine output

Even without a section, the doctrine fibration `U` itself is canonical relative to the fixed moduli problem. Fibrewise it retains:

- all compatible doctrines;
- noninvertible doctrine maps;
- equivalences and isotropy;
- monodromy/reindexing.

Call it a stack only after descent for a specified topology is proved.

---

# 14. Core descent: exact doctrine-free EIG Core theorem

## 14.1 Doctrine-relative core functor

On the category of doctrine morphisms for which Section 6 functoriality is established, define

$$
K:\mathcal D_2\to\mathcal C,
\qquad
K(D)=\mathrm{EIGCore}(D),
$$

where `C` is the category/infinity-category/localization of shape theories at the declared equivalence level.

If only equivalence transport is proved, replace `D_2,S_1` by their equivalence cores for this theorem.

## 14.2 Factorization category

Let `Fact_U(K)` have objects

$$
(\bar K,\eta),
\qquad
\bar K:\mathcal S_1\to\mathcal C,
\qquad
\eta:\bar K U\simeq K,
$$

with coherently compatible morphisms. Define

$$
\mathrm{Desc}_U(K):=\mathrm{Fact}_U(K)^{\simeq}.
$$

## 14.3 Exact common-core criterion

- `Desc_U(K)` is nonempty iff `K` factors coherently through `U`.
- If the **bare factorization problem** is the full requested problem, contractibility means the common semantics-only core is unique up to contractible choice.
- Nonempty noncontractibility says bare factorization alone does not force uniqueness.
- A stronger intrinsic descent specification may still select a distinguished factorization.

For a specified descent property `P`, apply the trichotomy to

$$
\mathrm{Desc}_{U,P}(K).
$$

## 14.4 Selection and descent are independent

A doctrine section `s` yields a selected core `Ks`, but does not imply

$$
\bar K U\simeq K
$$

for **all** doctrines. Conversely, all doctrine cores may descend even when no doctrine can be selected.

Hence:

$$
\boxed{
\text{doctrine noncanonical}
\centernot\Rightarrow
\text{EIG Core noncanonical},
}
$$

and

$$
\boxed{
\text{canonical doctrine selector}
\centernot\Rightarrow
\text{common-core descent}.
}
$$

This is the exact correction to the slogan that “Level 2 is the irreducible core boundary.”

The two nonimplications have separate witnesses. CE7 witnesses doctrine nonselection with contractible core descent. For the converse, let

$$
U:[1]\to *
$$

be the unique functor and let `K:[1]->[1]` be the identity. The section category is `[1]`; its initial section selects `0`, so the specified **initial-section** selection problem is contractibly canonical. But any `bar K:*->[1]` is constant, and no constant functor is naturally equivalent to `id_[1]` because `0` and `1` are not equivalent in `[1]`. Hence `Desc_U(K)` is empty. Thus a canonical specified doctrine selector still need not imply common-core descent.

## 14.5 Coherent isotropy can obstruct descent

A representative obstruction is the inclusion

$$
BC_3\to BS_3
$$

and `K:BC_3->BC_3` induced by the identity of `C_3`. A descent would require a homomorphism `S_3->C_3` restricting to the identity on `A_3=C_3`, but every homomorphism from `S_3` to an abelian group factors through `S_3^{ab}=C_2` and kills `A_3`. Hence `Desc_U(K)` is empty.

This is a genuine descent obstruction, not merely failure to choose a representative.

## 14.6 Kan-extension shadows

If `C` has the required limits/colimits, one can form

$$
\mathrm{Ran}_U K,
\qquad
\mathrm{Lan}_U K.
$$

These are canonical invariant/coinvariant **shadows** at lower semantics, with universal comparison maps to/from `K`. They are not common-core descent unless the relevant comparison is an equivalence.

---

# 15. Doctrine-free EIG object: the full labelled fibration

EIG is richer than EIG Core. A fixed doctrine carries not only `Core(D)` but the reduction, root-selector value, full closure modality, structural arity theory, and any separately certified recognition/operation layers.

## 15.1 Fixed-doctrine EIG package

The mandatory fixed-doctrine package is

$$
\mathsf{EIG}(D)
:=
\bigl(
q_D,
R_D,
\mathrm{Cl}_D,
\mathrm{EIGCore}(D),
\Theta_D
\bigr),
$$

with optional certified extensions:

$$
(N_D,\mathcal L_D^{\rm comp},\mathcal L_D^{\max},
\text{density certificates},
\text{operation-exactness certificates},\ldots).
$$

These optional layers are included only with their actual status; closure does not manufacture recognition.

## 15.2 Doctrine-indexed EIG

Across forward doctrine maps preserving the relevant structure, the closure/core layer is functorial by Section 6. Other package components are functorial only when their own transport hypotheses are proved.

Thus the unconditional cross-doctrine object justified by the generic theory is not a fictitious strict functor containing every optional layer, but a **doctrine-indexed system with a proved core functor and separately certified extensions**.

## 15.3 Lossless doctrine-free core packaging

At lower semantic object `X`, define the core-labelled full doctrine fibre

$$
\boxed{
\mathcal M_K(X)
=
\left(
\mathcal F_X,
K_X:\mathcal F_X\to\mathcal C
\right).
}
$$

Globally this is the information carried by

$$
(U,K):\mathcal D_2\to\mathcal S_1\times\mathcal C.
$$

It retains every compatible doctrine, noninvertible doctrine map, core label, equivalence, isotropy, and reindexing map. It is therefore a **lossless doctrine-free packaging relative to the fixed moduli problem `(U,K)`**: the packaging is simply the supplied doctrine fibration together with the proved core label, so no doctrine/core information present in `(U,K)` is discarded.

This is an information-preservation statement, not a terminal/initial maximality theorem in a category of all possible doctrine-free outputs. Any further canonical aggregate is a new universal problem whose solution space must be audited.

## 15.4 Lossless full-EIG packaging

Where the richer fixed-doctrine package has been proved functorial, label the same doctrine fibre by that package rather than only by its core:

$$
\boxed{
\mathcal M_{\mathsf{EIG}}(X)
=
\left(
\mathcal F_X,
D\mapsto\mathsf{EIG}(D)
\right).
}
$$

This is the corresponding lossless doctrine-indexed form of **EIG itself** relative to the proved package data. It is generally richer than a semantics-only core because doctrine ambiguity may survive in witness structure, coherence, law/operation data, or presentation even when the core descends.

## 15.5 Exact hierarchy of possible point-valued outputs

From lower semantics `X`, increasingly strong collapses require increasingly strong theorems:

1. **selected doctrine:** a section of `U`;
2. **selected EIG package:** a section together with the relevant package transport;
3. **common EIG Core:** descent/factorization of `K` through `U`;
4. **common full EIG package:** descent of the entire proved package functor — strictly stronger than core descent;
5. **strict representative/equality:** an additional rigidification/strictification selection problem.

This hierarchy explains why EIG Core can be canonical at a thinner level than full EIG.

---

# 16. Canonicality/no-go theorem

Fix:

1. an admissible lower semantic base `S_1`;
2. a coherent doctrine fibration `U:D_2->S_1` with declared variance;
3. a declared equivalence notion;
4. the doctrine-relative core functor `K` at the functorial level actually proved;
5. any explicitly stated output-free selection/descent specification `P`;
6. the category `M` of doctrine/core problems whose equivalences/noninvertible maps define what “invariant” means;
7. whenever a global naturality statement is invoked, a functorial specified-solution assignment
$$
   \mathrm{Sol}_P:\mathcal M^{op}\to\mathbf{Spc}
$$
   (or an appropriate `\mathbf{Cat}_\infty`-valued assignment followed by maximal groupoids), together with its unstraightening/universal solution fibration
$$
   \pi_P:\int_{\mathcal M}\mathrm{Sol}_P\to\mathcal M.
$$

## Theorem 16.1 — canonicality boundary

Then:

1. coherent doctrine extractors are exactly sections of `U`;
2. semantics-only cores agreeing with all compatible doctrine-relative cores are exactly objects of `Fact_U(K)`;
3. a specified doctrine/core extraction is canonical up to contractible coherent choice exactly when its **specified** solution space is contractible;
4. on an equivalence component of the whole problem category, equivalence-invariant extractions are exactly homotopy fixed points of that specified solution space under problem automorphisms;
5. under hypothesis 7, over noninvertible maps of problems, invariant extraction is exactly a global section of the universal solution fibration `\pi_P`;
6. regardless of point selection, the full core-labelled doctrine fibration `M_K` is the always-defined lossless core packaging relative to `(U,K)`.

### Exact impossibility tests

The genuine generic no-go forms are:

- **empty section/factorization space:** no point-valued extraction of the requested kind exists;
- **empty invariant-solution space:** solutions exist only after symmetry-breaking choice; no extraction invariant under the declared problem exists;
- **noncontractible specified solution space:** the currently stated specification fails to determine a unique solution, but this alone does not forbid a stronger independently justified universal selector.

No stronger unconditional trichotomy follows from raw fibre noncontractibility alone.

---

# 17. Protected recurrent EIG: currently justified specialization

The historical recurrent row is

```text
RAW(SYNC + protected STORE)
  -> target REDUCE / witness descent
  -> target-context canonicalization
  -> owner-Cech SPACE
  -> strict-Segal SEQ
  -> recurrent product/star
  -> observer/public projection.
```

The strongest safe classification is as follows.

## 17.1 RAW

Native occurrences, owners, witnesses, leaf identities, storage labels, and private projections are primitive Level-2 presentation/doctrine data unless independently reconstructed.

## 17.2 SYNC

Once typed legs are fixed, synchronized cells may be derived by pullbacks. Pullback objects and canonical associativity comparisons are universal. Their compatibility with REDUCE, STORE, codescent, or images is a separate exactness theorem.

## 17.3 protected STORE

Private projections/provenance retained by storage are primitive doctrine choices. Fibres/tabulations may be derived universal objects. Preservation through reduction is not automatic.

## 17.4 target REDUCE / witness descent

Admitted target observations are primitive. The contextual quotient/reflector is derived when Section 3 applies. Witness descent requires a separate effectiveness/exactness theorem.

## 17.5 target-context canonicalization

A comparison

$$
\bar K(qx_1,\ldots,qx_m)
\to/\simeq
qK_{\rm raw}(x_1,\ldots,x_m)
$$

is derived when raw composition respects contextual equivalence. Invertibility is a separate exactness condition.

## 17.6 owner-Cech SPACE

The owner cover is primitive unless an earlier theorem derives it. Given the cover, its Cech nerve/codescent is derived when it exists. Effectivity and Beck-Chevalley/base-change preservation remain separate gates.

## 17.7 strict-Segal SEQ

Free finite-word/path generation is an object-generating constructor when independently present. Strict-Segal/ULF/discrete-Conduche conditions are recognition/exactness properties of the realization/nerve, not definitions of the root or core.

## 17.8 product/star and observer projection

These are naturally external operations/modules/valuations unless represented by internal semantic objects and explicitly included among the object-generating rules.

## 17.9 Strongest historical equivalence endpoint

For the recurrent specialization, the retained equivalence endpoint is

$$
\boxed{
\text{generated recurrent theory}
\simeq_{\rm model\text{-}Morita/indexed\text{-}equipment}
\text{historical recurrent theory},
}
$$

followed by the previously audited process-nerve equivalence on its stated essential image.

No result established here upgrades this generically to literal equality or to a stronger equivalence level.

## 17.10 Historical ordered factorization

Let `c_SS`, `c_SPACE`, `c_SEQ` be the corresponding closures **in the reduced recurrent semantic world**. The historical factorization formula

$$
\mathrm{EIGCore}(D_{\rm rec})
\simeq
c_{\rm SEQ}c_{\rm SPACE}c_{\rm SS}(R_{\rm rec})
$$

holds under the following factorization hypotheses:

1. all three are closure operators on one common admissible Cauchy lattice;
2. `c_SPACE` preserves `c_SS`-closed objects;
3. `c_SEQ` preserves both earlier fixed-point classes;
4. all comparison cells satisfy the required coherence;
5. these closures exhaust every global object-generating rule;
6. if a raw-root presentation is used, REDUCE is root-exact and commutes with the required generation steps.

Under these hypotheses, the historical order is a factorization/normal-form presentation of the already-canonical simultaneous closure. Without them, the simultaneous closure remains the definition and no ordered presentation is asserted.

## 17.11 Reconstruction noncircularity

The downstream process nerve remains noncircular only if:

1. root/core are defined without the desired nerve essential image;
2. Segal/ULF and owner-descent laws are proved from constructor semantics;
3. density and operation exactness are checked after core construction;
4. process realization is not used to prove root-exactness for the same core.

---

# 18. Sharp counterexample stack: why each boundary is necessary

The following examples prevent every tempting stronger generic theorem.

## CE1. REDUCE does not commute with Tiny

The `Arr(Set)->Set` reflection sends the Tiny arrow `emptyset->1` to non-Tiny `emptyset`. Therefore root-exactness is real content.

## CE2. Pairwise distributive laws do not by themselves establish coherent triple composition

The iterated-distributive-law theorem requires the pairwise laws to satisfy Yang-Baxter. This is a **standard/dependent boundary**, not a writer-monad counterexample proved in this note; concrete iterated-composition obstructions are supplied by the cited no-go literature.

## CE3. Distributive laws may not exist

Published no-go examples show that separate modalities need not admit any ordinary distributive law.

## CE4. Same lower map semantics, inequivalent interaction doctrines

`Span` and `Rel` share the ordinary function/map locus in the standard sense but differ in loose interactions: a span `1 <- A -> 1` retains witness multiplicity and automorphisms while its image relation records only truth. Bare extensional maps do not determine witness doctrine.

## CE5. Symmetry can forbid invariant root/doctrine selection

For an unlabelled two-point set, the fibre of pointings is a two-element discrete set with transitive `S_2` action. Its homotopy-fixed-point space is empty.

## CE6. Two compatible doctrines may exist but no invariant selector

For a terminal semantic base with a discrete two-doctrine fibre `{d0,d1}`, a problem automorphism swapping them makes the invariant selector space empty.

## CE7. Doctrine noncanonical, core canonical

In the same symmetric two-doctrine problem, take the core functor constant at a terminal object. Doctrine selection has no invariant point, while core descent is contractible.

## CE8. Pointwise cores may fail coherent descent

`BC_3 -> BS_3` with identity core label on `BC_3` has no descent, by the homomorphism obstruction of Section 14.5.

## CE9. Intrinsic root need not be dense

The ordinary all-small-colimit Tiny root of `Ab` is empty, so intrinsic root canonicality does not imply reconstruction.

## CE10. One final Cauchy completion can miss generated outputs

A retract appearing only after completion may activate a partial constructor, so final-only `Kar` is insufficient.

## CE11. Single-monad packaging can be nonunique

The same pair of writer modalities can combine to `C_6` or `S_3` under different actions.

## CE12. Higher coherence can be nonunique

Cocycle-twisted associators produce inequivalent coherent structures with the same lower binary skeleton.

## CE13. Noncontractible raw moduli can still contain a canonical point; selection need not imply descent

The walking-arrow category `[1]` has a noncontractible maximal groupoid but a canonical initial object. Therefore raw noncontractibility is not an absolute canonicality no-go.

For the selection/descent independence witness, take the unique

$$
U:[1]\to *
$$

and `K=id_[1]`. The section category of `U` is `[1]`, whose initial section is the choice of `0`; hence the specified initial-section problem is contractibly canonical. A factorization `bar K U ~= K`, however, would make `id_[1]` naturally equivalent to a constant functor, which is impossible because `0` and `1` are not equivalent. Thus **canonical specified doctrine selection need not imply common-core descent**.

## CE14. Non-Moore choice rules can destroy least closure

On `P({a,b})`, declare a class closed iff it contains exactly one of `a,b`. The closed extensions `{a}` and `{b}` have nonclosed intersection and neither is least. Thus a point-valued least core need not exist for genuinely exclusive/negative generation constraints.

---

# 19. Prior-art boundary and what is project-specific

This note intentionally separates standard machinery from the project-specific synthesis.

## 19.1 Standard constituent machinery

The following are standard or established prior art at their proper scope:

- Knaster-Tarski and closure/Moore-family theory;
- ordinary/enriched Cauchy completion and absolute weights;
- monads with supplied arities and dense generators (Berger-Mellies-Weber);
- monads/theories and nervousness with supplied arities (Bourke-Garner);
- relative monads/pseudomonads and nerve theorems with a supplied root/dense functor;
- distributive laws, iterated distributive laws, Yang-Baxter conditions, and no-go theorems;
- polynomial/familial/multi-sorted packaging under suitable hypotheses;
- equipments/virtual double categories, proarrows, tabulations, restrictions, formal cocompletion;
- modern collage-atomic/profunctor characterizations under their stated AVDC hypotheses;
- straightening/unstraightening, cartesian sections, limits of category-valued functors, and homotopy fixed points;
- theory/model Galois connections;
- Kan extensions and coend reconstruction;
- restriction categories/partial map formalisms.

## 19.2 What these results do not supply automatically

They do not, in general:

- select an EIG doctrine from bare lower semantics;
- select `Tiny(E)` as a canonical root in an arbitrary ambient category/equipment;
- prove contextual REDUCE preserves a raw root;
- force cross-modality Beck-Chevalley invertibility;
- force a coherent/unique mixed monad;
- prove density/nervousness from least closure;
- prove recurrent factorization from the existence of a historical normalization order;
- turn Morita equivalence into literal equality;
- make a noncontractible raw moduli space an absolute no-go against every universal selector.

## 19.3 Project-specific synthesis represented by this stack

The substantive combined EIG architecture is the conjunction of:

```text
universal contextual reduction
  -> intrinsic reduced root
  -> full simultaneous semantic closure modality
  -> EIGCore = closure(root)
  -> associated structural theory
  -> independently audited recognition/operation layers

plus

forward doctrine functoriality
  -> doctrine fibration
  -> exact section / specified-selection problem
  -> exact core factorization/descent problem
  -> full labelled doctrine fibration as lossless doctrine-free packaging relative to `(U,K)`.
```

This note does not claim that this whole synthesis already has an established literature-priority status. A dedicated exact-isomorphism/prior-art search is separate from proving the internal theorem stack.

## 19.4 Selected references for the distributive-law boundary

- Eugenia Cheng, **“Iterated distributive laws,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 150(3), 459–487 (2011), DOI `10.1017/S0305004110000599`. This is the standard source for composing multiple monads from pairwise distributive laws satisfying Yang-Baxter coherence.
- Maaike Zwart and Dan Marsden, **“No-Go Theorems for Distributive Laws,”** *Logical Methods in Computer Science* 18(1):13 (2022), DOI `10.46298/lmcs-18(1:13)2022`. Besides pairwise no-go theorems, its iterated-distributive-law discussion gives concrete obstructions to proposed Yang-Baxter-compatible iteration; it also proves that the list monad does not distribute over itself.
- Chris Purdy and Stefania Damato, **“Distributive Laws of Monadic Containers,”** CALCO 2025, LIPIcs 342, Article 4, DOI `10.4230/LIPIcs.CALCO.2025.4`. This provides a modern explicit characterization of distributive laws for monadic containers; in particular, writer-writer distributive laws correspond to matching pairs of monoid actions.

---

# 20. Proof dependency DAG

The dependency structure is deliberately acyclic at the theorem level even though semantic generation itself may contain cycles.

```text
A0  declare categorical level, equivalence, size universe
 |
 +--> A1  declare raw doctrine + admitted contexts/observations
 |      |
 |      +--> A2  contextual equivalence
 |              |
 |              +--> A3  universal REDUCE/exactification q
 |                      |
 |                      +--> A4  RootSpec on reduced world
 |                              |
 |                              +--> A5  reduced root R_D
 |                                      |
 |                                      +--> A6  Moore family / monotone generators
 |                                              |
 |                                              +--> A7  closure modality Cl_D(S)
 |                                              |      |
 |                                              |      +--> A8  EIGCore(D)=Cl_D(R_D)
 |                                              |      +--> A9  exact generation entailment
 |                                              |      +--> A10 forward lax functoriality
 |                                              |              |
 |                                              |              +--> A11 equivalence invariance
 |                                              |              +--> A12 doctrine-relative core functor K
 |                                              |
 |                                              +--> A13 optional modality factorization
 |                                                     (requires preservation/coherence)
 |
 +--> B1  structural Hom/cell doctrine W^str
        |
        +--> B2  associated theory Theta_D on Core(D)
                |
                +--> B3  restricted nerve N_D
                       |
                       +--> B4 density gate
                       +--> B5 maximal law envelope / definability gate
                       +--> B6 operation restriction / exactness gate

C0  choose doctrine-moduli problem U:D2->S1
 |
 +--> C1 doctrine selection = section(U)
 |      |
 |      +--> C2 specified selection space
 |             +--> C3 problem-level invariant HFP/global-section test
 |
 +--> C4 core functor K (from A12)
        |
        +--> C5 common Core = factorization of K through U
        |      +--> C6 specified descent space
        |             +--> C7 invariant HFP/global-section test
        |
        +--> C8 lossless core-labelled doctrine packaging M_K

D0  recurrent specialization
 |
 +--> D1 reduced-world closures c_SS,c_SPACE,c_SEQ
        |
        +--> D2 preservation + coherence + exhaustion
               |
               +--> D3 historical ordered factorization = global Core
                      (under the Section 17.10 factorization hypotheses)
```

No recognition theorem is used to define the root or closure. No modality factorization is used to prove existence of the global core. No doctrine-free selection is used to prove fixed-doctrine canonicality.

---

# 21. Scope summary

The generic fixed-doctrine result is the least-closure theorem of Section 22. Once the reduced semantic world, intrinsic root, admissible Moore environment, Core-generating semantic operations and coherence, structural theory, and equivalence level are fixed as specified, the closure modality `Cl_D` and the Core `EIGCore(D)` are determined by the least-closure universal property.

Density, nerve or essential-image recognition, operation reconstruction, process/model realization, historical ordered factorizations, and doctrine-free point selection are separate statements with the additional hypotheses given in their respective sections. None of them is used to define or prove the fixed-doctrine Core.

After forgetting doctrine data, the generic result is therefore formulated as the exact section/selection and descent/factorization problems, together with the full labelled doctrine fibration when no point-valued selection or descent is justified. For the recurrent specialization, the ordered row is an optional factorization presentation under Section 17.10; the simultaneous closure remains primary.

---

# 22. Main theorem for EIG Core

> ## THEOREM — Fixed-doctrine EIG Core closure theorem
>
> Fix an output-free coherent Level-2 interaction doctrine `D` at a declared categorical/equivalence level. Assume:
>
> 1. admitted contexts/observations determine a universal contextual reduction/exactification `q:E_raw->W_D`, or equivalent reduced semantic data are explicitly supplied;
> 2. an invariant root specification applies **in the reduced world**, producing `R_D`;
> 3. the admissible replete/Cauchy semantic structured subtheories form a set-sized environment `Sub_D` in which the `D`-closed upper bounds of every admissible seed form a nonempty Moore family — in particular, it suffices that a complete lattice and monotone positive generation operators are given;
> 4. every actual Core-generating semantic object/cell/higher-cell generator is typed, its output sort is declared, and its non-forced comparison/higher coherence is included in the doctrine; law-producing rules and external valuations are kept in their separately typed downstream layers unless explicitly internalized as Core sorts;
> 5. the structural Hom/cell doctrine and equivalence localization are declared.
>
> Then the doctrine determines a canonical closure modality
>
> \[
> \boxed{
> \mathrm{Cl}_D(S)
> =
> \bigwedge\{B\in\mathsf{Sub}_D:S\le B,\ B\text{ is }D\text{-closed}\}
> }
> \]
>
> for every admissible seed `S in Sub_D`. In the monotone complete-lattice presentation,
>
> \[
> \mathrm{Cl}_D(S)=\mu\Gamma_{D,S}.
> \]
>
> The EIG Core is
>
> \[
> \boxed{
> \mathrm{EIGCore}(D)=\mathrm{Cl}_D(R_D).
> }
> \]
>
> It is the initial/least internal semantic `D`-closed structured subtheory receiving `R_D`; the space of solutions to that fully specified internal least-closure problem is contractible. For every generated Core sort `sigma` and every semantic element `x` of that sort,
>
> \[
> x\in_\sigma\mathrm{Cl}_D(S)
> \iff
> x\text{ belongs in sort }\sigma\text{ to every }D\text{-closed upper bound of }S,
> \]
>
> so nonmembership has an exact stable countermodel. Forward doctrine morphisms satisfying the explicit admissible-hull, inverse-image, generation, and root transport conditions induce canonical typed lax comparisons
>
> \[
> F_\sharp\mathrm{Cl}_D(S)
> \le
> \mathrm{Cl}_{D'}(F_\sharp S),
> \]
>
> and doctrine equivalences induce equivalences of the entire closure modality and of EIG Core.
>
> No modality order or well-foundedness is required. Any historical/modality-stratified construction is only a factorization theorem for this closure and is correct exactly under the corresponding preservation/distributive/coherence hypotheses. Density, nervousness, law definability, operation exactness, and process/model reconstruction are downstream gates and do not weaken the fixed-doctrine canonicality theorem.

### Scope

The statement is made for the **entire seed-wise closure modality**, not only the root-specific least closure, and includes exact generation entailment and forward lax functoriality. It preserves the reduced-root ordering, Moore-family existence boundary, internal-vs-external free distinction, and exact doctrine-free no-go architecture.

---

# 23. Main theorem for EIG as a whole

> ## THEOREM — Doctrine-indexed EIG and lossless doctrine-free packaging
>
> For each coherent doctrine `D`, the mandatory generic EIG package determined by the theory is
>
> \[
> \mathsf{EIG}(D)
> =
> (q_D,R_D,\mathrm{Cl}_D,
> \mathrm{EIGCore}(D),\Theta_D),
> \]
>
> supplemented only by independently certified density, law-recognition, operation-exactness, descent, and realization data.
>
> Across structure-preserving doctrine maps, the closure/core component is lax-functorial; across doctrine equivalences it is invariant at the declared equivalence level. A full richer package is functorial only to the extent that its additional certificates are themselves transported.
>
> After forgetting the doctrine along
>
> \[
> U:\mathcal D_2\to\mathcal S_1,
> \]
>
> an always-defined lossless doctrine-free packaging is therefore not generally one point-valued shape theory. It is the full doctrine fibration labelled by the EIG outputs that have actually been proved, in particular the core-labelled fibre
>
> \[
> \boxed{
> X\longmapsto
> (\mathcal F_X,K_X:\mathcal F_X\to\mathcal C).
> }
> \]
>
> A selected doctrine/full EIG package is a section/selection problem. A common EIG Core is the separate descent/factorization problem `bar K U ~= K`. A common full EIG package would require descent of the richer package and is strictly stronger. Thus EIG Core may canonically descend even while EIG retains irreducible doctrine/witness/coherence moduli.

---

# 24. Canonicality/no-go theorem

> ## THEOREM — Exact specified-solution / invariant no-go ceiling
>
> Let `P` be any explicitly declared, output-free doctrine-selection, core-descent, operation-reconstruction, presentation, or coherence problem derived from the supplied data. Form the full solution category and then the space of solutions satisfying **all** properties that define `P`.
>
> 1. If this specified solution space is empty, no solution of the requested kind exists.
> 2. If it is contractible, the requested solution is canonical up to contractible coherent choice.
> 3. If it is nonempty and noncontractible, the conditions stated in `P` do not determine a unique solution; this alone does **not** forbid a stronger independently justified universal specification.
> 4. If equivalence invariance of the whole problem is required, the exact local criterion on a connected problem component is the corresponding problem-level homotopy-fixed-point space. If that invariant-solution space is empty, no equivalence-invariant point can be extracted from the declared problem.
> 5. Across noninvertible maps of problems, **when the specified solution spaces assemble functorially over the declared problem category**, the exact naturality criterion is a global section of the corresponding unstraightened universal solution fibration.
>
> In particular:
>
> - doctrine selection is the section problem for `U`;
> - common EIG Core is the factorization/descent problem for `K` along `U`;
> - bare arity-only operation reconstruction is the restriction-fibre problem;
> - coherent mixed packaging is a distributive/coherence solution problem.
>
> The full labelled doctrine fibration remains the uncollapsed canonical output when point selection/descent is not established. Empty invariant-solution spaces are genuine no-go theorems. Raw noncontractibility by itself is not.

---

# 25. Why the positive and negative boundaries coincide exactly

There is one universal architecture behind both sides.

For a fixed doctrine, the declared internal completion problem is:

```text
find a D-closed admissible semantic subtheory
containing the reduced root,
and choose the least/initial such object.
```

The Moore/Tarski theorem proves that the initial solution exists. The space of initial solutions is contractible. This is the positive EIG Core theorem.

After forgetting doctrine data, one obtains new solution problems:

```text
select a doctrine     -> section(U)
find a common Core    -> factorization(K through U)
select invariantly    -> problem-level HFP / global section
```

These problems need not be solvable. Their empty invariant solution spaces are the matching negative theorems. When they are not point-solvable, the full labelled doctrine fibration retains exactly the unresolved information instead of discarding it.

Thus the fixed-doctrine positive theorem and doctrine-free no-go ceiling are not competing stories. They are two instances of the same rule:

> **Specify the entire universal problem first; then existence, contractible uniqueness, residual moduli, and invariant impossibility are properties of its actual solution category/space.**

---

# 26. Scope limits

The generic theorem does not assert the following without the additional hypotheses identified elsewhere in this note.

1. Bare lower/extensional semantics canonically determine a unique interaction doctrine.
2. Level 2 is always the exact irreducible boundary for the Core.
3. Raw Tiny/root extraction commutes with contextual reduction without root-exactness.
4. Every EIG doctrine has a least point-valued core even with arbitrary negative/exclusive constraints.
5. Every internal semantic closure is an external free algebraic/2-categorical completion.
6. Every heterogeneous EIG package is a canonical KZ doctrine or one canonical monad.
7. Universal construction alone implies Beck-Chevalley/exactness/interchange invertibility.
8. Intrinsic root/least closure implies density or a nerve theorem.
9. Noncontractibility of an unqualified moduli/groupoid is an absolute no-go against canonical initial/terminal/minimal points.
10. A canonical doctrine selector implies common-core descent.
11. Failure to select a doctrine implies failure of Core descent.
12. A Kan-extension aggregate is automatically the common EIG Core.
13. The recurrent target-first order equals the global simultaneous closure without the Section 17.10 factorization hypotheses.
14. The recurrent model-Morita/indexed-equipment endpoint is literal equality or a stronger equivalence without an additional theorem.
15. The law compiler is complete merely because it is sound.
16. Failure of one coend reconstruction proves abstract operation non-identifiability.

Each item has either an explicit counterexample in the stack or a precise additional theorem that would be required.

---

# 27. Canonical repository formulation

A public-facing EIG Core should state the theory in this order:

```text
1. Freeze admitted contexts/observations and categorical/equivalence level.
2. Form/declare the universal contextual reduction.
3. Extract the intrinsic root in the reduced semantic world.
4. Define the entire closure modality Cl_D on arbitrary seeds.
5. Define EIGCore(D)=Cl_D(R_D).
6. State the internal reflection and exact generation-countermodel theorem.
7. State forward lax functoriality and equivalence invariance.
8. Only then state optional modality-factorization theorems.
9. Define the associated structural theory Theta_D.
10. Separately audit density, law recognition, operation exactness, and process realization.
11. Introduce the doctrine fibration U and core functor K.
12. State doctrine selection as a section problem and common Core as a descent problem.
13. State specified-solution/problem-level invariance as the exact canonicality/no-go language.
14. Use the labelled doctrine fibration as the lossless doctrine-free packaging relative to the declared moduli problem.
15. Present the recurrent SYNC/STORE/SPACE/SEQ row as a specialization whose ordered factorization remains conditional until its exact lemma is proved.
```

This order makes every strong claim downstream of exactly the hypotheses that justify it, and prevents recognition or historical presentation choices from contaminating the maximal fixed-doctrine theorem.

---

# 28. Summary statement

**EIG Core.** For every independently meaningful coherent interaction doctrine, first pass to the contextually reduced semantic world, extract its intrinsic reduced root, and then apply the doctrine’s full simultaneous semantic closure modality. Under the Moore-family hypothesis — in particular under the complete-lattice/monotone-generator hypotheses — this yields the unique least internal semantic structured subtheory closed under every actual Core-generating semantic operation. EIG Core is the value of that closure modality at the reduced root. It is order-independent, admits cyclic generation, is an internal reflection/free semantic closure, has an exact generation-countermodel semantics, is lax-functorial under forward doctrine maps satisfying the stated transport conditions, and is invariant under doctrine equivalence. Stratified modality orders are optional computation/factorization theorems only.

**EIG.** The generic discipline is doctrine-indexed: reduction, root, closure modality, Core, associated structural theory, and only those recognition/operation layers separately certified. From thinner lower semantics, an always-defined lossless information-preserving packaging is the full compatible-doctrine fibration labelled by these outputs. A point-valued doctrine is a section/selection theorem; a doctrine-independent common Core is a distinct descent/factorization theorem; full-EIG descent is stronger still. Canonicality is tested only after the requested universal property has been included in the solution problem. Contractible specified solution spaces give coherent uniqueness; empty invariant-solution spaces give exact no-go theorems; noncontractible raw moduli by themselves do not rule out canonical initial, terminal, minimal, or reflective selections.

This is the form established here under the stated hypotheses, without adding unproved assumptions or weakening the maximality boundary.

---

# Appendix A. EIG-exactness labels: nonconflating form

The term **EIG-exact** should never be used without naming the target layer.

## A.1 Context exactness

The contextual quotient/localization is exact when it has the declared universal separatedification property and the required typing/descent structure exists.

## A.2 Root exactness

Reduction is root-exact exactly when the transported raw root and intrinsic reduced root agree at the declared Cauchy/equivalence level.

## A.3 Generation exactness

Under the closure hypotheses,

$$
\mathrm{EIGCore}(D)=\mathrm{Cl}_D(R_D)
$$

with exact stable-countermodel semantics. This is the generic fixed-doctrine exactness that is always present once the hypotheses of Section 5 hold.

## A.4 Nerve faithfulness

Semantic objects/morphisms are recoverable from arity observations only after density/full faithfulness of the restricted nerve is proved.

## A.5 Language recognition exactness

For fixed law language,

$$
G_D=\mathrm{Def}_D(G_D)
$$

is the exact criterion for some theory in that language to define the genuine nerve image.

## A.6 Compiler exactness

If the certified compiler itself is claimed to present the image, require

$$
\mathrm{Mod}_D(\mathcal L_D^{\rm comp})=G_D.
$$

This is stronger than language recognizability.

## A.7 Operation exactness

State the requested reconstruction problem explicitly:

- bare arity-only uniqueness: contractibility of the bare restriction solution fibre;
- specified universal operation: contractibility of the specified operation-solution space;
- invariant operation: existence/contractibility of the corresponding problem-level invariant solution;
- constructive coend/Kan exactness: invertibility of the stated comparison.

These are different claims.

## A.8 Primitive/lower-level exactness

At thinner semantics distinguish:

- **descent-exact Core:** `K` factors through `U`;
- **selection-exact doctrine/EIG:** a canonical specified section exists;
- **moduli-exact:** the full labelled doctrine fibration is the canonical endpoint;
- **full-package descent-exact:** the richer EIG package, not merely its Core, descends.

No label silently implies another.

## A.9 Auxiliary ambiguity versus output ambiguity

A constructor extension, raw root, presentation, or witness doctrine may be nonunique while its closure output is constant. Conversely, a canonical auxiliary choice need not make all other compatible outputs agree. Therefore every ambiguity must be tested **after projection to the output actually being claimed**.

This is one of the central reasons the Core descent problem is strictly different from doctrine selection.

---

# Appendix B. Frozen calibration obligations

The generic theorem stack does not replace row-specific proofs.

## B.1 Free categories

A complete calibration should separately prove:

1. intrinsic reduced root;
2. independent semantic justification of free path composition;
3. root closure equals the intended finite linear path arities;
4. correct occurrence/incidence maps;
5. strict Segal laws from the free-composition semantics;
6. density and exact essential-image recognition;
7. lower-level canonicality classified as selection, descent, or moduli.

## B.2 Fixed-colour nonsymmetric operads

Prove that intrinsic corollas plus independently justified planar substitution close to the intended planar trees, then prove the tree-Segal recognition theorem separately.

## B.3 Strict globular `n`-categories

Prove that globe roots plus strict globular composition close to the intended pasting shapes/`Theta_n`-type arities at the stated equivalence level, then separately prove the nerve theorem.

## B.4 Protected recurrent / richer witness worlds

Keep distinct:

- existence;
- uniqueness;
- multiplicity;
- witness/provenance geometry;
- support/context structure;
- external observation;
- Morita versus literal equivalence.

The generic Core theorem does not collapse these profiles.

## B.5 Calibration rule

For every row, compute or characterize as sharply as possible:

- contextual quotient/localization;
- reduced-root space and root-exactness if raw roots are used;
- semantic closure modality;
- auxiliary-extension dependence of that closure;
- law definability closure;
- operation restriction/specification solution spaces;
- doctrine selection space;
- Core descent space.

A row is not “fully canonical” merely because its fixed-doctrine closure is canonical.

---

# Appendix C. Meta-EIG under the same canonicality discipline

A meta-discovery envelope is mathematically legitimate only if it obeys the same separation principles.

Fix a meta-doctrine `M` that independently specifies allowed:

- semantic-generation moves;
- law-extraction moves;
- realization moves;
- typed inference schemes;
- coherence transformations.

A monotone operator on a set-sized shape/law universe may have a least fixed point by Knaster-Tarski. That proves only **formal closure existence**.

The substantive obligations are:

1. every generated shape/law is independently admissible;
2. the meta-operator is invariant under the declared equivalences;
3. when a Level-2 semantic doctrine is already fixed, the shape component agrees with the semantic closure modality `Cl_D` rather than defining a competing weaker core;
4. the law component is compared against the maximal sound theory `Th_D(G_D)`;
5. any newly generated semantic realization is selected by a fully specified universal solution problem or retained as moduli;
6. any claim of primitive-level canonicality is evaluated through section/descent/invariant-solution machinery.

When shape generation is independent of newly generated laws, the system triangularizes:

$$
R_D
\xrightarrow{\mathrm{Cl}_D}
\mathrm{EIGCore}(D)
$$

first, followed by law saturation/recognition. This triangular form is preferable because it guarantees that a stronger law theory cannot retroactively redefine the already maximal fixed-doctrine Core.

Tarski gives existence of a formal fixed point. It does not prove discovery, semantic soundness, law completeness, density, or doctrine-free canonicality.
