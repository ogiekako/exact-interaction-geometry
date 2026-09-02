# Exact Interaction Geometry Core

## Canonical Level-2 construction schema

**Status:** candidate for independent audit on the stated small/finitary Level-2 class.  
**Scope:** an independently supplied exact interaction/composition doctrine is input.  
**Non-claim:** a bare object/map world does not in general determine its interaction doctrine.  
**Epistemic rule:** this note separates proved fixed-point/transport lemmas from definitions and recognition criteria.

---

## 1. Executive statement

For a fixed interaction doctrine `D`, Exact Interaction Geometry separates four tasks:

1. **contextual separatedification** — erase exactly the distinctions invisible to every admitted context;
2. **semantic shape generation** — close an intrinsic generic root under the doctrine's actual exact composition and universal constructions;
3. **local-law compilation** — on an explicitly cellular subclass, compile typed local laws from constructor-derived decompositions and universal properties;
4. **recognition** — separately test whether the generated arities and laws reconstruct the intended world and its operations.

The central object is

$$
\boxed{
\operatorname{EIGCore}(D)
=
\mu\Psi_D
\quad\text{inside the contextually separated semantic world }\mathcal W_D.
}
$$

In Set-like deterministic sectors, the contextual separatedification is concretely computed by a greatest fixed point `nu Phi_D`. Thus the compact slogan is

$$
\boxed{
\text{least exact compositional geometry inside the greatest contextually justified quotient.}
}
$$

The fixed-point construction does **not** imply reconstruction. Local nervousness and operation exactness are separate recognition conditions.

---

## 2. Level boundary

### Level 1

An arity theory/monad is already supplied; one proves a nerve theorem or characterizes its models.

### Level 2 — the positive EIG scope

A raw world, a reconstruction target, and an exact interaction/composition doctrine are supplied, but the arity/shape theory is not. EIG extracts an intrinsic root, closes it under the actual doctrine, and then tests reconstruction.

### Level 3 — false in general

A bare extensional object/map world is asked to select its own interaction doctrine. This fails in general: the same map-level world can support, for example, witness-preserving span semantics or witness-forgetting relation semantics. Map data alone does not determine whether witness multiplicity is meaningful.

Hence the canonical object is doctrine-relative, `EIG(D)`, not an unconditional `EIG(X)` extracted from arbitrary bare semantics.

---

## 3. Admissible Level-2 doctrine

A small/finitary Level-2 doctrine consists schematically of

$$
D=(\mathsf P,\mathcal R,\mathcal W,\mathcal C,\mathcal O,\mathcal K,\mathcal U,\mathcal E).
$$

- `P`: profiles/types;
- `R`: raw family/witness sectors `E_p`;
- `W`: the contextually separated semantic/reconstruction worlds `W_D(p)`;
- `C`: primitive one-hole context generators and their typing/parameter rules;
- `O`: primitive closing observations;
- `K`: actual typed constructors, possibly partial, dependent, or profile-changing;
- `U`: independently meaningful exact universal constructions such as image, pullback, tabulation, support reflection, Cech/codescent, or free-path completion;
- `E`: the honest equivalence notion: isomorphism, equivalence, Cauchy, Morita, or moduli-valued.

The doctrine supplies, or independently constructs, a universal contextual/exact separatedification

$$
Q_D:\mathcal R_D\longrightarrow\mathcal W_D.
$$

`Q_D` is not an arbitrary chosen quotient. It must be characterized by the universal property of making the admitted contextually sound identifications.

The doctrine also declares a structural morphism/cell class `W_D^str` used for reconstruction. It may equal the ambient semantic morphism class, but this is not assumed.

The fixed-point theorem assumes a fixed universe in which the admissible semantic object classes form the required complete lattice. The Kleene `omega` formula requires an additional continuity hypothesis.

### 3.1 No-smuggling firewall

No-smuggling is a **hypothesis/provenance obligation**, not something the tuple above can certify internally.

Permitted data must be independently justified before the extractor is run: raw sectors, admitted contexts, constructors, universal operations, semantic equivalences, and universal reductions. Forbidden inputs include the desired output arity category, desired essential image, or an equivalent classifier under another name.

In particular, `free-path completion` is a permissible constructor when independently present in the doctrine; a `Segal recognition law` belongs to the later law compiler and is not part of `U` merely because it is desired as an output.

For every public calibration, answer-independence of the doctrine data is therefore a separate audit obligation.

---

## 4. Contextual separatedification

### 4.1 Generated finite contexts

In the Set-like deterministic sector, define the one-hole generator family `GenCtx_D` as follows.

For every `m`-ary constructor `K` and every hole position `i`, every well-typed filling of the other `m-1` positions by admitted parameters gives a one-hole generator

$$
K(a_1,\ldots,a_{i-1},-,a_{i+1},\ldots,a_m),
$$

on exactly its legal partial/dependent domain. Primitive closing observations in `O` are also generators. If the doctrine regards a closing experiment as primitive rather than decomposable, it must appear explicitly in `GenCtx_D`.

The finite admitted one-hole contexts `Ctx_D` are, **by definition for Theorem 4.1**, the typed inductive closure of `GenCtx_D` under context composition. This generation hypothesis is load-bearing.

### 4.2 Set-like relation transformer

Let `Rel_D` be the complete lattice of typed relation candidates. Define the monotone operator

$$
\Phi_D:\mathrm{Rel}_D\to\mathrm{Rel}_D
$$

by `x Phi_D(R) y` iff:

1. every primitive closing observation applicable to both gives the same result;
2. for every one-hole constructor generator, definedness agrees on `x` and `y`;
3. whenever that generator is defined, the two resulting cells are `R`-related.

All constructor hole positions and all legal parameter fillings are quantified over.

Knaster-Tarski gives

$$
R_D^\infty=\nu R.\Phi_D(R).
$$

### Theorem 4.1 — all-context characterization

Under the context-generation convention above, for raw cells `x,y`,

$$
x\,R_D^\infty\,y
$$

iff every finite well-typed context in `Ctx_D` gives the same observable response on `x` and `y`.

**Proof.** If `x R_D^infty y`, fixed-point stability propagates through a generator; induction on the generated context depth propagates it through every finite context. Conversely, all-context indistinguishability is stable under every generator because prefixing a finite context by a generator is again a finite context. It is therefore a post-fixed point of `Phi_D` and lies below the greatest fixed point. The first implication gives the reverse inclusion. ∎

In enriched/higher sectors, `Q_D` may instead be an effective quotient, localization, homotopy image, stack quotient, or another universal separatedification. No general Set-valued `nu Phi_D` claim is made there.

---

## 5. Intrinsic root

The root is not chosen by presentation-dependent atoms or primes.

For a raw family sector `E_p`, use its intrinsic Tiny/Cauchy core whenever defined:

$$
A_{raw}(p)=\operatorname{Tiny}(E_p).
$$

For a small presheaf category,

$$
\operatorname{Tiny}([C^{op},\mathbf{Set}])\simeq\operatorname{Kar}(C).
$$

Thus equivalent presheaf presentations recover the same root up to Cauchy equivalence.

The doctrine's universal exact realization sends the raw root to a semantic root

$$
A_0(D)\subseteq \operatorname{Ob}(\mathcal W_D).
$$

If literal uniqueness fails, the correct output may be an equivalence class, groupoid, Morita class, or moduli object.

---

## 6. Least exact semantic geometry

### 6.1 Exactized semantic constructors

The doctrine must specify the semantic action induced by each raw/native constructor after target recanonicalization. We write this action as `bar K`. Schematically, when the types permit,

$$
\bar K\circ Q_D^{\times m}\simeq Q_D\circ K_{raw}.
$$

The intended order is

```text
raw/native composition
  -> target semantic reduction/recanonicalization.
```

### 6.2 One-step generating operator

Fix a complete lattice `Shape_D` of admissible replete object classes inside the declared semantic universe. Retract closure means **ambient retracts that actually split in `W_D`**. If the doctrine requires formal Cauchy completion, the semantic universe is first replaced by its declared universal Cauchy envelope so that the operation remains internal.

Define the monotone inflationary **one-step generating operator**

$$
\Psi_D(A)
=
\operatorname{Retr}_{\mathcal W_D}\operatorname{Repl}
\left(
A\cup\bar{\mathcal K}_D(A)\cup\bar{\mathcal U}_D(A)
\right).
$$

Start from `A_0(D)`.

### Theorem 6.1 — EIG Core existence

If `Psi_D` is a monotone endofunction on `Shape_D`, then

$$
\boxed{
A_D^{EIG}
=\mu_{A\supseteq A_0(D)}\Psi_D(A)
}
$$

exists and is the least fixed shape class above `A_0(D)`.

By construction, its fixed-point property is exactly repletion, ambient-retract closure, and closure under every declared exact constructor/universal operation represented in `Psi_D`.

If, additionally, `Psi_D` preserves the relevant directed unions, then

$$
A_D^{EIG}
=\bigcup_{n<\omega}A_n,
\qquad
A_{n+1}=\Psi_D(A_n).
$$

Thus Tarski existence and the Kleene `omega`-chain formula are separate statements.

### 6.3 Retract closure must participate in the fixed point

A final one-shot retract completion can fail. If `1` is a retract of `2`, a partial constructor is defined only on `1`, and `K(1)=3`, then starting from `{2}`, constructor closure followed by one final retract closure adds `1` but misses `3`. Stagewise generation adds both.

---

## 7. Associated interaction theory and typing

Let `W_D^str` be the doctrine's structural semantic category/equipment used for the reconstruction problem. After the object class has been generated independently, define

$$
\boxed{
\Theta_D^{EIG}:=(\mathcal W_D^{str})\big|_{A_D^{EIG}}.
}
$$

If `W_D^str` contains all ambient semantic morphisms between these objects, this is a full subcategory/subtheory. If the intended structural morphism class is narrower, the notation above means restriction of that declared class and **not** a full ambient subcategory.

The arity inclusion is now well typed:

$$
J_D:\Theta_D^{EIG}\hookrightarrow\mathcal W_D^{str}.
$$

The nontrivial extraction is the object/arity class. Once that class is independently fixed, using the already-declared structural Homs/cells avoids artificial free-mixed-syntax fullness obligations.

---

## 8. Cellular local-law compiler

The local-law compiler requires more structure than the generic Level-2 fixed-point theorem.

### 8.1 Enrichment base

A cellular doctrine fixes a semantic law base `V` appropriate to its filler geometry, for example `Set`, `Gpd`, or `Spaces`, or another explicitly specified enriched/homotopical base with the mapping objects and fibres used below.

All `Map_V`, `Fib_V`, and model categories in this section are interpreted in that base. A Set-valued statement does not silently assert a groupoid- or space-valued theorem.

### 8.2 Cellular/occurrence data

A **cellular Level-2 doctrine** additionally provides, or functorially derives from independently specified constructor semantics:

1. a subtheory of elementary/generic shapes `A_D^el`;
2. a doctrine-invariant class of inert/occurrence maps into generated shapes;
3. restriction/overlap maps between occurrences;
4. for every constructor-generated elementary decomposition, a **local decomposition certificate**: a canonical comparison together with the filler/universal-property profile forced by the actual constructor semantics;
5. a set of typed inference schemes for composing certified local laws, each with a generic soundness proof in `V`;
6. coherent transport of these data under doctrine equivalence.

Occurrence maps alone do not imply a Segal or descent law. The certificate must come from the universal property of the supplied constructor/decomposition semantics, not from the desired essential image.

For example, in the free-category row, using all semantic maps `[1] -> [2]` would incorrectly include the composite `0 -> 2`; the doctrine must identify the immediate/inert edge occurrences. The unique assembly of a two-edge path is then certified by free path composition, not by naming a desired Segal nerve image.

### 8.3 Elementary core

For a generated shape `T`, define

$$
\operatorname{Occ}_D(T)
=(A_D^{el}\downarrow_{occ}T)
$$

and the canonical elementary-core map

$$
I_D(T)
=
\operatorname*{colim}_{e\to T\in\operatorname{Occ}_D(T)}y(e)
\longrightarrow y(T).
$$

### 8.4 Typed defect laws

A local law is a pair

$$
\ell=(j_\ell,\pi_\ell),
$$

where `j_l:B_l -> C_l` is a certified comparison test and `pi_l` is a predicate/profile on its filler object.

For a boundary instance `u:B_l -> X`, define in `V`

$$
\operatorname{Fill}_\ell(X,u)
=
\operatorname{Fib}_u
\left[
\operatorname{Map}_{\mathcal V}(C_\ell,X)
\to
\operatorname{Map}_{\mathcal V}(B_\ell,X)
\right].
$$

Examples of `pi_l` include:

- inhabited — existence;
- contractible — existence and uniqueness up to the chosen homotopical level;
- prescribed discrete multiplicity;
- prescribed groupoid/isotropy type;
- prescribed higher homotopy type;
- a declared universal limit/colimit/tabulation property.

Ordinary orthogonality is only the contractible-filler sector.

### 8.5 Profile-aware saturation

Let `Lambda_0(D,A)` be the certified elementary laws from occurrence decompositions and declared universal properties.

A saturation rule is **not** merely an operation on comparison maps. It is a typed inference scheme

$$
\rho:(\ell_1,\ldots,\ell_n)\Longrightarrow\ell
$$

with a generic proof that validity of the premise profiles for a genuine nerve object implies validity of the conclusion profile. The conclusion profile may differ from every premise profile.

Define

$$
\operatorname{Sat}_D(\Lambda)
$$

as the least law set containing `Lambda` and closed under the doctrine's certified typed inference schemes.

There is **no unconditional retract rule** for arbitrary profiles. For instance exact filler multiplicity is not retract-stable in general. A retract/substitution/base-change/pasting rule may be used only with an explicit profile transformer and a proof of soundness for that rule. Existence and contractible-filler laws often admit stronger closure rules than multiplicity or isotropy laws; the calculus records that distinction.

Define the compiled theory

$$
\boxed{
\mathcal L_D
=
\operatorname{Sat}_D\bigl(\Lambda_0(D,A_D^{EIG})\bigr).
}
$$

### Theorem 8.1 — compiler soundness

Assume every elementary certificate is valid for genuine nerve objects and every admitted typed inference scheme is sound in the sense above. Then every genuine nerve object satisfies every law in `L_D`.

**Proof.** Induct on the finite derivation of a law from `Lambda_0`. The base case is the decomposition/universal-property certificate. The induction step is exactly the soundness proof attached to the applied typed inference scheme. ∎

`L_D` is a **finitarily generated/finite-derivation local theory**; it need not be a finite set of laws.

If genuine nerve objects satisfy additional global restrictions not derivable from `L_D`, that discrepancy belongs to the local-nervousness recognition gate rather than being silently inserted into the compiler.

---

## 9. Recognition is not closure

In the ordinary `Set`-valued case, define

$$
N_D(X)=\mathcal W_D^{str}(J_D-,X).
$$

In the cellular enriched/higher case, use the declared `V`-enriched analogue.

### 9.1 Density

`J_D` is dense iff `N_D` is fully faithful, equivalently, when the standard density adjunction exists, iff the density counit is invertible.

An intrinsic root can fail to be dense. For example, the fully faithful embedding `Set -> Set x Set`, `X |-> (X, empty)`, sends the Tiny root to `(1,empty)`; the resulting nerve forgets the entire second component.

Density is therefore a recognition property, not a consequence of root canonicality.

### 9.2 Local nervousness

A cellular doctrine is **local-nervous** when the restricted nerve itself induces an equivalence

$$
\boxed{
N_D:\mathcal W_D^{str}
\xrightarrow{\simeq}
\operatorname{Mod}_{\mathcal V}(\Theta_D^{EIG},\mathcal L_D)
}
$$

onto the compiled model subcategory of the appropriate presheaf/enriched-presheaf category.

Thus local nervousness includes density and additionally identifies the essential image with the compiled local model theory. This is a recognition definition, not an existence theorem.

### 9.3 Operation exactness

For an admitted world operation

$$
K:\mathcal W_1^{str}\times\cdots\times\mathcal W_m^{str}\to\mathcal W_0^{str},
$$

define, in the ordinary case,

$$
M_K(b;a_1,\ldots,a_m)
=
\mathcal W_0^{str}\bigl(J_0b,K(J_1a_1,\ldots,J_ma_m)\bigr).
$$

The canonical comparison is

$$
\kappa_{K,\vec X}(b):
\int^{a_1,\ldots,a_m}
M_K(b;a_1,\ldots,a_m)
\times
\prod_i\mathcal W_i^{str}(J_ia_i,X_i)
\longrightarrow
\mathcal W_0^{str}(J_0b,K(\vec X)).
$$

`K` is **arity-exact** iff every `kappa_K` is invertible. The enriched version uses the corresponding enriched coend/tensor.

Density alone does not imply operation exactness: a dense root need not determine an arbitrary global operation from its restriction to arities.

If `M_K` is not representable by an honest arity functor, the module/proarrow itself may be the correct canonical level.

---

## 10. EIG-exactness as a recognition criterion

A doctrine is **EIG-exact for a claimed reconstruction target** when:

1. its restricted nerve is local-nervous;
2. every claimed admitted external operation is arity-exact;
3. the declared morphism/base-change structure is coherently reconstructed.

Under these conditions, reconstruction is true by the meanings of the recognition conditions together with the stated operation comparisons. This section is a criterion/schema; it is not advertised as a separate deep theorem.

The conditions remain separately diagnosable even though local nervousness logically implies density.

---

## 11. Doctrine morphisms and canonicality

### 11.1 Doctrine equivalence used in this note

For the purpose of this construction, an equivalence `F:D -> D'` consists of coherent equivalences on the profile, raw, and semantic/structural worlds together with invertible comparison data preserving:

- the primitive context generators and closing observations;
- the contextual separatedification `Q_D`;
- raw Tiny/Cauchy sectors and their semantic root realizations;
- typed constructor domains and exactized semantic constructor values;
- declared universal operations;
- the equivalence/retract convention.

For cellular doctrines it additionally preserves the enrichment base up to the declared equivalence, elementary objects, occurrence maps, decomposition certificates, **and the typed inference schemes including their profile-transform rules**.

Composition and identities are the evident composites/identities of these coherent data. A doctrine equivalence is an invertible morphism up to the declared coherent 2-cells. This definition is local to this note; no claim is made that it is the unique useful category of EIG doctrines.

### Proposition 11.2 — transport invariance

A doctrine equivalence in the sense above transports the contextual separatedification and conjugates the induced one-step operator `Psi_D` with `Psi_D'`. Hence it carries the least semantic fixed point and associated interaction theory to equivalent outputs. In the cellular subclass it also transports `Lambda_0`, the typed inference calculus, and therefore `L_D`.

**Proof.** The preservation data induce order isomorphisms between the relevant relation/shape/law lattices and intertwine the corresponding operators/rules. Least/greatest fixed points and least rule-saturated subsets are invariant under such conjugacy. ∎

This is the precise presentation-invariant sense of canonicality claimed here. It is a transport theorem conditional on a doctrine equivalence, not a theorem that bare presentations determine the doctrine itself.

---

## 12. Failure coastline

- **F0 — doctrine ambiguity:** the bare world does not select a unique interaction doctrine.
- **F1 — root failure:** no essentially small intrinsic Tiny/Cauchy root exists in the declared universe.
- **F2 — reduction failure:** no canonical/universal contextual or exact reduction is available.
- **F3 — size/continuity failure:** the required closure escapes the universe or lacks continuity needed for a claimed finite-stage generation.
- **F4 — local-nervousness failure:** the compiled local model class strictly exceeds or otherwise mismatches the actual nerve image.
- **F5 — density failure:** the restricted nerve is not fully faithful / the density counit is noninvertible when available.
- **F6 — operation failure:** some `kappa_K` is noninvertible.
- **F7 — nonrepresentability:** a canonical external action exists only as a module/proarrow; this may diagnose the correct categorical level rather than a failure.
- **F8 — isotropy/moduli:** literal uniqueness fails while a canonical groupoid, Morita class, or moduli object remains; this is a unicity diagnosis rather than necessarily a failure.

---

## 13. Frozen calibrations

These rows are calibrations of the schema; each retains its own proof obligations and no-smuggling audit.

### Free categories

Walking vertex/edge roots plus independently supplied free-path composition generate finite linear paths and the simplex-type arity theory. Immediate path edges are the cellular occurrences; the universal property of free composition certifies the strict Segal comparisons.

### Fixed-colour nonsymmetric operads

Generic corollas plus operadic substitution generate planar rooted trees. Vertex corollas are the cellular occurrences; substitution semantics certifies the tree Segal-core comparisons.

### Strict globular `n`-categories

Globe roots plus strict globular composition generate pasting diagrams and a `Theta_n`-type theory. Elementary globe/cell occurrences and their constructor-derived pasting certificates yield the globular Segal comparisons.

### Normalized protected recurrent world

The root consists of Tiny boundary/cell family sectors. Exact reduction uses joint coherent images, witness/storage tabulations, pullbacks, support/context, and derived owner geometry; temporal closure uses shared-interface ULF/strict-Segal paths. Its separately audited occurrence/decomposition calculus yields the local image/evaluator/storage/context/path ledger. SYNC, STORE, SPACE, star, and observer/public projection live in the external module/comparison layer. The honest unicity endpoint is model-Morita equivalence.

The recurrent row is important because it requires existence, uniqueness, multiplicity, and retained witness geometry to remain distinct.

---

## 14. Meta-EIG

Meta-EIG is a doctrine-relative discovery formalism, not a doctrine-free selector of legitimate mathematics.

Fix a meta-doctrine `M` describing which comparison constructions, defect extractions, universal realizations, and **typed profile-transform inference schemes** are admissible. Let `Sh` and `Law` be set-sized universes of admissible semantic shapes and typed defect laws. A state is

$$
(A,\Lambda)\in\mathcal P(\mathsf{Sh})\times\mathcal P(\mathsf{Law}).
$$

Define a monotone simultaneous operator

$$
\mathbb F_{D,\mathfrak M}(A,\Lambda)
=
\bigl(\Psi_{D,\mathfrak M}(A,\Lambda),G_{D,\mathfrak M}(A,\Lambda)\bigr),
$$

where `G` uses the same profile-aware typed saturation discipline as Section 8. `Real(Lambda)` may add a derived semantic sort only when the doctrine/meta-doctrine gives a canonical universal realization; a failing example alone does not license an arbitrary new object.

### Theorem 14.1 — simultaneous fixed point

If the two universes are set-sized and the simultaneous operator is monotone, then

$$
\boxed{
(A_D^*,\Lambda_D^*)
=\mu\mathbb F_{D,\mathfrak M}
}
$$

exists by Knaster-Tarski. If the operator preserves the relevant directed unions, its least fixed point is obtained by the Kleene chain.

### Level-2 triangularization

When the exact interaction/completion doctrine is already supplied and shape generation is independent of newly discovered law data, `Psi(A,Lambda)=Psi_D(A)`. The simultaneous fixed point then triangularizes: first compute `mu Psi_D`, then compute the least law fixed point at that shape class.

---

## 15. Prior-art boundary

The constituent mechanisms include standard mathematics: Myhill-Nerode/syntactic congruence, behavioral equivalence, Knaster-Tarski/Kleene fixed points, Tiny/small-projective objects, Karoubi/Cauchy completion, restricted Yoneda and density, monads with arities, algebraic patterns/Segal objects, spans/relations/profunctors/equipments, and Morita/moduli ideas.

No priority claim is made here for those ingredients.

The project-specific synthesis currently asserted is the doctrine-indexed architecture

$$
\boxed{
Q_D
\;\triangleright\;
\mu\Psi_D
\;\triangleright\;
\mathcal L_D
\;\triangleright\;
\text{local-nervousness / operation recognition}
}
$$

with typed witness-defect profiles, external module actions, and an explicit failure coastline.

Whether this exact combined architecture already exists in the literature under another formulation is a separate specialist prior-art question.

---

## 16. Canonical Level-2 construction schema

This section is a summary of the preceding definitions and theorems, **not one additional theorem**.

Given an admissible Level-2 doctrine `D`:

1. construct or supply the universal contextual separatedification `Q_D:R_D -> W_D`; in the generated Set-like sector Theorem 4.1 identifies it with all-context equivalence;
2. form the intrinsic Tiny/Cauchy root and its universal semantic realization `A_0(D)`;
3. apply Theorem 6.1 to obtain the least semantic fixed point `A_D^EIG = mu Psi_D`;
4. restrict the declared structural semantic morphisms to obtain `Theta_D^EIG`;
5. on the strengthened cellular subclass, compile the finitarily generated local law theory `L_D` by the profile-aware calculus, whose soundness is Theorem 8.1;
6. test local nervousness and operation exactness as recognition conditions;
7. transport along doctrine equivalences by Proposition 11.2;
8. report failures using F0--F8 rather than making arbitrary choices.

None of these statements imply doctrine-free Level-3 self-generation.

The shortest defensible definition is:

> **EIG Core is the least exact compositional geometry generated from an intrinsic root inside a contextually separated semantic world, relative to an independently supplied interaction doctrine.**

For cellular doctrines, local exactness laws are additionally compiled from independently justified constructor-derived occurrence/decomposition data. Full reconstruction remains a separate recognition problem.