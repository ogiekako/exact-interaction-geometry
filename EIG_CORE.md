# Exact Interaction Geometry Core

## Canonical Level-2 formulation

**Status:** frozen candidate on the stated small/finitary Level-2 class.  
**Scope:** an independently supplied exact interaction/composition doctrine is input.  
**Non-claim:** a bare object/map world does not in general determine its interaction doctrine.

---

## 1. Executive statement

For a fixed interaction doctrine `D`, Exact Interaction Geometry separates four tasks:

1. **contextual separatedification** — erase exactly the distinctions invisible to every admitted context;
2. **semantic shape generation** — close an intrinsic generic root under the doctrine's actual exact composition and universal constructions;
3. **local-law compilation** — on an explicitly defined cellular subclass, compile the local laws forced by constructor-derived elementary decompositions and universal properties;
4. **recognition** — separately test whether the generated arities and laws reconstruct the intended world and its operations.

The central object is

\[
\boxed{
\operatorname{EIGCore}(D)
=
\mu\Psi_D
\quad\text{inside the contextually separated semantic world }S_D.
}
\]

In Set-like deterministic sectors, `S_D` is concretely the quotient by a greatest fixed point `nu Phi_D`; thus the compact slogan is

\[
\boxed{
\text{least exact compositional geometry inside the greatest contextually justified quotient.}
}
\]

The fixed-point construction does **not** by itself imply reconstruction. Density, local nervousness, and operation exactness remain recognition gates.

---

## 2. Level boundary

### Level 1

An arity theory/monad is already supplied; one proves a nerve theorem or characterizes its models.

### Level 2 — the positive EIG theorem

A world and an exact interaction/composition doctrine are supplied, but the arity/shape theory is not. EIG extracts an intrinsic root, closes it under the actual doctrine, and then tests reconstruction.

### Level 3 — false in general

A bare extensional object/map world is asked to select its own interaction doctrine. This fails in general: the same map-level world can support, for example, witness-preserving span semantics or witness-forgetting relation semantics. Map data alone does not determine whether witness multiplicity is meaningful.

Hence the canonical object is doctrine-relative:

\[
\operatorname{EIG}(D),
\]

not an unconditional `EIG(X)` extracted from arbitrary bare semantics.

---

## 3. Admissible Level-2 doctrine

A small/finitary Level-2 doctrine consists schematically of

\[
D=(\mathsf P,\mathcal R,\mathcal S,\mathcal O,\mathcal K,\mathcal U,\mathcal E).
\]

- `P`: profiles/types;
- `R`: raw family/witness sectors `E_p`;
- `S`: semantic worlds together with a **universal contextual/exact separatedification** `S_D` (or the data from which it is independently constructed);
- `O`: admitted observations and closing contexts;
- `K`: actual typed constructors, possibly partial, dependent, or profile-changing;
- `U`: declared exact universal constructions such as image, pullback, tabulation, support reflection, Cech/codescent, or free path/Segal completion;
- `E`: the honest equivalence notion: isomorphism, equivalence, Cauchy, Morita, or moduli-valued.

The separatedification is not an arbitrary chosen quotient. It must be characterized by the universal property of making exactly the contextually sound identifications.

The fixed-point theorem assumes a fixed universe in which the relevant profile/root/constructor data are set-sized and the semantic shape classes form the required complete lattice. The Kleene `omega`-iteration formula requires the additional continuity hypothesis stated below.

---

## 4. Contextual separatedification

The general object is a doctrine-appropriate contextual separatedification

\[
S_D:\mathcal R_D\longrightarrow\mathcal S_D^{\mathrm{sep}},
\]

characterized by the largest identification sound under all admitted contexts.

### 4.1 Set-like deterministic realization

Let `Rel_D` be the complete lattice of typed relation candidates. Define a monotone operator

\[
\Phi_D:\mathrm{Rel}_D\to\mathrm{Rel}_D
\]

by requiring that `x Phi_D(R) y` iff:

1. all immediate admitted observations agree;
2. every admitted one-step partial constructor has the same definedness;
3. corresponding defined continuations have `R`-related outputs.

Knaster-Tarski gives

\[
R_D^\infty=\nu R.\Phi_D(R).
\]

### Theorem 4.1 — all-context characterization

For raw cells `x,y`,

\[
x\,R_D^\infty\,y
\]

iff every finite well-typed admitted context gives the same observable response on `x` and `y`.

**Proof.** Fixed-point stability propagates through contexts by induction on context depth. Conversely, all-context indistinguishability is a post-fixed point of `Phi_D`, hence is contained in the greatest fixed point. ∎

In enriched/higher sectors, `S_D` may instead be an effective quotient, localization, homotopy image, stack quotient, or another universal separatedification. No general Set-valued `nu Phi_D` claim is made there.

---

## 5. Intrinsic root

The root is not chosen by presentation-dependent atoms or primes.

For a raw family sector `E_p`, use its intrinsic Tiny/Cauchy core whenever defined:

\[
A_{\mathrm{raw}}(p)=\operatorname{Tiny}(E_p).
\]

For a presheaf category,

\[
\operatorname{Tiny}([C^{op},\mathbf{Set}])\simeq\operatorname{Kar}(C).
\]

Thus equivalent presheaf presentations recover the same root up to Cauchy equivalence.

The doctrine's universal exact reduction/completion sends the raw root to a semantic root

\[
A_0(D)\subseteq\mathcal S_D^{\mathrm{sep}}.
\]

If literal uniqueness fails, the correct output may be an equivalence class, groupoid, Morita class, or moduli object.

---

## 6. Least exact semantic geometry

### 6.1 Exactized constructors

Composition is read in the target semantic world. Schematically,

\[
\bar K=S_D\circ K,
\]

with the relevant separated inclusions on the inputs.

The intended order is

```text
raw/native composition
  -> target semantic reduction/recanonicalization.
```

### 6.2 Closure operator

On the declared complete lattice of replete semantic shape classes define

\[
\Psi_D(A)
=
\operatorname{Kar}_{\mathcal S}\operatorname{Repl}
\left(
A\cup\bar{\mathcal K}_D(A)\cup\bar{\mathcal U}_D(A)
\right).
\]

Start from `A_0(D)`.

### Theorem 6.1 — EIG Core existence

If `Psi_D` is monotone, then

\[
\boxed{
A_D^{\mathrm{EIG}}
=\mu_{A\supseteq A_0(D)}\Psi_D(A)
}
\]

exists and is the least replete, Cauchy-closed semantic shape class containing `A_0(D)` and closed under every declared exact constructor and universal operation.

If, additionally, `Psi_D` preserves the relevant directed unions, then

\[
A_D^{\mathrm{EIG}}
=\bigcup_{n<\omega}A_n,
\qquad
A_{n+1}=\Psi_D(A_n).
\]

Thus Tarski existence and the Kleene `omega`-chain formula are separate statements.

### 6.3 Cauchy closure must be iterative

A final one-shot Karoubi completion can fail. If `1` is a retract of `2`, a partial constructor is defined only on `1`, and `K(1)=3`, then starting from `{2}`, constructor closure followed by one final Karoubi completion adds `1` but misses `3`. Stagewise constructor--Kar closure adds both. Hence retract splitting must participate in the fixed point.

---

## 7. Associated theory

After the object class has been generated independently, define

\[
\boxed{
\Theta_D^{\mathrm{EIG}}
=
\operatorname{Full}_{\mathcal S_D}(A_D^{\mathrm{EIG}}),
}
\]

using the doctrine's intended structural morphism class if it is narrower than ambient Homs.

The nontrivial extraction is the object/arity class. Once that class is independently fixed, using actual semantic Homs avoids artificial free-mixed-syntax fullness obligations.

---

## 8. Cellular local-law compiler

The local-law compiler requires more structure than the generic Level-2 fixed-point theorem.

### 8.1 Cellular/occurrence-equipped doctrine

A **cellular Level-2 doctrine** additionally provides, or functorially derives from independently specified constructor semantics:

1. a subtheory of elementary/generic shapes `A_D^el`;
2. a doctrine-invariant class of inert/occurrence maps into generated shapes;
3. restriction/overlap maps between occurrences;
4. for every constructor-generated elementary decomposition, a **local decomposition certificate**: a canonical comparison together with the filler/universal-property profile forced by the actual constructor semantics;
5. coherence and doctrine-equivalence invariance of these data.

The fourth item is load-bearing. Occurrence maps alone do not imply a Segal or descent law. The required local profile must come from the universal property of the supplied constructor/decomposition semantics, not from the desired essential image.

For example, in the free-category row, using all semantic maps `[1] -> [2]` would incorrectly include the composite `0 -> 2`; the doctrine must identify the immediate/inert edge occurrences. The fact that a two-edge path is uniquely assembled from those occurrences is then supplied by the universal property of free path composition, not by naming the Segal condition as an answer.

### 8.2 Elementary core

For a generated shape `T`, define

\[
\operatorname{Occ}_D(T)
=(A_D^{el}\downarrow_{\mathrm{occ}}T)
\]

and

\[
I_D(T)
=
\operatorname*{colim}_{e\to T\in\operatorname{Occ}_D(T)}y(e)
\longrightarrow y(T).
\]

### 8.3 Typed defect profile

For a comparison test

\[
j_\tau:B_\tau\to C_\tau
\]

and boundary instance `u:B_tau -> X`, define

\[
\operatorname{Fill}_\tau(X,u)
=
\operatorname{fib}_u
\bigl[
\operatorname{Map}(C_\tau,X)
\to
\operatorname{Map}(B_\tau,X)
\bigr].
\]

The local decomposition certificate specifies the required profile, e.g.

- nonempty — existence;
- contractible/singleton — existence and uniqueness;
- prescribed discrete multiplicity;
- prescribed groupoid/isotropy;
- prescribed higher coherence type;
- a declared universal limit/colimit/tabulation property.

Ordinary orthogonality is only the contractible-filler sector.

### 8.4 Saturation and soundness

Let `ElemCmp_D(A)` be the certified occurrence-core comparisons together with comparisons generated by the doctrine's declared universal properties. Let `Sat_D` close these under exactly the admitted finite substitution, whiskering, pasting, base change, semantic equivalence, retract, reassociation/interchange, and defined filler-profile composition operations.

Define

\[
\boxed{
\mathcal L_D
=
\operatorname{Sat}_D
\bigl(\operatorname{ElemCmp}_D(A_D^{\mathrm{EIG}})\bigr).
}
\]

Because each elementary generator is certified by actual constructor/universal semantics and the saturation operations preserve validity, every genuine nerve object satisfies `L_D`.

The compiler therefore produces exactly the finite **doctrine-generated local** comparison theory. If genuine nerve objects satisfy additional global restrictions not generated this way, that discrepancy is measured by local nervousness rather than silently inserted into the compiler.

---

## 9. Recognition is not closure

Let

\[
J_D:\Theta_D^{\mathrm{EIG}}\hookrightarrow\mathcal W_D
\]

be the generated arity inclusion, and let

\[
N_D(X)=\mathcal W_D(J_D-,X)
\]

be the restricted interaction nerve.

### 9.1 Density

`J_D` is dense iff `N_D` is fully faithful, equivalently iff the density counit is invertible.

An intrinsic root can fail to be dense. For example, the fully faithful embedding `Set -> Set x Set`, `X |-> (X, empty)`, sends the Tiny root to `(1,empty)`; the resulting nerve forgets the entire second component.

Density is therefore a recognition property, not a consequence of root canonicality.

### 9.2 Local nervousness

A cellular doctrine is **local-nervous** when the restricted nerve itself induces an equivalence

\[
\boxed{
N_D:
\mathcal W_D
\xrightarrow{\simeq}
\operatorname{Mod}(\Theta_D^{\mathrm{EIG}},\mathcal L_D)
\hookrightarrow
[\Theta_D^{\mathrm{EIG},op},\mathbf{Set}]
}
\]

or the doctrine-appropriate enriched/higher analogue.

Thus local nervousness includes density and additionally identifies the essential image with the compiled local model theory.

### 9.3 Operation exactness

For an admitted world operation

\[
K:\mathcal W_1\times\cdots\times\mathcal W_m\to\mathcal W_0
\]

define

\[
M_K(b;a_1,\ldots,a_m)
=
\mathcal W_0\bigl(J_0b,K(J_1a_1,\ldots,J_ma_m)\bigr).
\]

The canonical comparison is

\[
\kappa_{K,\vec X}(b):
\int^{a_1,\ldots,a_m}
M_K(b;a_1,\ldots,a_m)
\times
\prod_i\mathcal W_i(J_ia_i,X_i)
\longrightarrow
\mathcal W_0(J_0b,K(\vec X)).
\]

`K` is **arity-exact** iff every `kappa_K` is invertible.

Density alone does not imply this: `FinSet -> Set` is dense, while identity and ultrafilter functors agree on finite sets but differ on suitable infinite sets.

If `M_K` is not representable by an honest arity functor, the module/proarrow itself may be the correct canonical level.

---

## 10. EIG-exact doctrines

A doctrine is **EIG-exact for a claimed reconstruction target** when:

1. its restricted nerve is local-nervous (hence dense);
2. every claimed admitted external operation is arity-exact;
3. the declared morphism/base-change structure is coherently reconstructed.

Then the nerve reconstructs the intended world and its claimed operation structure at the declared equivalence level.

The conditions remain separately diagnosable even though local nervousness logically implies density.

---

## 11. Canonicality

The canonicality claimed here is not literal uniqueness of a chosen small presentation. The honest endpoint may be equivalence, Cauchy equivalence, Morita/model equivalence, or a groupoid/stack/moduli object.

### Theorem 11.1 — doctrine-equivalence invariance

Suppose an equivalence

\[
F:D\simeq D'
\]

coherently preserves the data used by the construction: profiles, observations, contextual separatedification, Tiny roots, exact reductions, typed constructors, universal operations, and the declared equivalence convention. In the cellular subclass, also require preservation of elementary objects, occurrence maps, local decomposition certificates, and filler profiles.

Then the induced equivalences intertwine the relevant monotone operators and carry the contextual separatedification, least semantic fixed point, associated semantic theory, and compiled local law theory to the corresponding outputs for `D'`.

This is the precise presentation-invariant sense in which EIG is canonical.

---

## 12. Failure coastline

- **F0 — doctrine ambiguity:** the bare world does not select a unique interaction doctrine.
- **F1 — root failure:** no essentially small intrinsic Tiny/Cauchy root exists in the declared universe.
- **F2 — reduction failure:** no canonical/universal contextual or exact reduction is available.
- **F3 — size/continuity failure:** the required closure escapes the universe or lacks continuity needed for the claimed finite-stage generation.
- **F4 — local-nervousness failure:** the compiled local model class strictly exceeds the actual nerve image; a countermodel/essential-image mismatch is the witness.
- **F5 — density failure:** the density counit is noninvertible.
- **F6 — operation failure:** some `kappa_K` is noninvertible.
- **F7 — nonrepresentability:** a canonical external action exists only as a module/proarrow; this may diagnose the correct categorical level rather than a failure.
- **F8 — isotropy/moduli:** literal uniqueness fails while a canonical groupoid, Morita class, or moduli object remains; this is a unicity diagnosis rather than necessarily a failure.

---

## 13. Frozen calibrations

### Free categories

Walking vertex/edge roots plus free path composition generate finite linear paths and the simplex theory. Immediate path edges are the cellular occurrences; the free-composition universal property certifies the simplicial Segal comparison.

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

Fix a meta-doctrine `M` describing which comparison constructions, defect extractions, and universal realizations are admissible. Let `Sh` and `Law` be set-sized universes of admissible semantic shapes and typed defect tests. A state is

\[
(A,\Lambda)\in\mathcal P(\mathsf{Sh})\times\mathcal P(\mathsf{Law}).
\]

Define a monotone simultaneous operator

\[
\mathbb F_{D,\mathfrak M}(A,\Lambda)
=
\bigl(\Psi_{D,\mathfrak M}(A,\Lambda),G_{D,\mathfrak M}(A,\Lambda)\bigr),
\]

schematically by

\[
\Psi(A,\Lambda)
=
\operatorname{KarRepl}
\bigl(A_0\cup K(A)\cup U(A)\cup\operatorname{Real}(\Lambda)\bigr),
\]

\[
G(A,\Lambda)
=
\operatorname{Sat}_{D,\mathfrak M}
\bigl(\Lambda\cup\operatorname{ElemCmp}_{D,\mathfrak M}(A)\bigr).
\]

`Real(Lambda)` may add a derived semantic sort only when the doctrine/meta-doctrine gives a canonical universal realization; a failing example alone does not license an arbitrary new object.

### Theorem 14.1 — simultaneous fixed point

If the two universes are set-sized and the operator is monotone, then

\[
\boxed{
(A_D^*,\Lambda_D^*)
=
\mu\mathbb F_{D,\mathfrak M}
}
\]

exists by Knaster-Tarski. If the operator preserves the relevant directed unions, its least fixed point is obtained by the Kleene chain.

### Level-2 triangularization

When the exact interaction/completion doctrine is already supplied and shape generation is independent of newly discovered law data,

\[
\Psi(A,\Lambda)=\Psi_D(A).
\]

Then first compute `a* = mu Psi_D`, and next compute the least law fixed point at `a*`. This explains the successful Level-2 order:

```text
contextual separatedification
  -> Tiny / exact reduction
  -> least semantic shape closure
  -> cellular local-law compilation
  -> recognition gates.
```

---

## 15. Prior-art boundary

The constituent mechanisms include standard mathematics: Myhill-Nerode/syntactic congruence, behavioral equivalence, Knaster-Tarski/Kleene fixed points, Tiny/small-projective objects, Karoubi/Cauchy completion, restricted Yoneda and density, monads with arities, algebraic patterns/Segal objects, spans/relations/profunctors/equipments, and Morita/moduli ideas.

No priority claim is made here for those ingredients.

The project-specific synthesis currently asserted is the doctrine-indexed architecture

\[
\boxed{
S_D
\;\triangleright\;
\mu\Psi_D
\;\triangleright\;
\mathcal L_D
\;\triangleright\;
\text{local-nervousness / operation recognition},
}
\]

with typed witness-defect profiles, external module actions, and an explicit failure coastline.

Whether this exact combined architecture already exists in the literature under another formulation is a separate specialist prior-art question.

---

## 16. Final theorem and definition

### Final Level-2 EIG Core theorem

Let `D` be a small Level-2 exact interaction doctrine satisfying the hypotheses above.

1. The doctrine has, or independently constructs, a universal contextual separatedification `S_D`; in Set-like deterministic sectors it is computed by the all-context greatest fixed point `nu Phi_D`.
2. The exactized semantic closure operator has a least fixed point
   \[
   A_D^{\mathrm{EIG}}=\mu\Psi_D.
   \]
3. The associated interaction theory is the doctrine-appropriate full semantic theory on that independently generated object class.
4. If `D` is cellular in the strengthened sense of Section 8, the certified elementary decomposition comparisons generate a sound finite local law theory `L_D`.
5. Equivalent doctrines preserving the relevant structure give equivalent EIG outputs at the declared equivalence/Cauchy/Morita/moduli level.
6. If the restricted nerve is local-nervous and every claimed external operation is arity-exact, the intended world and claimed operation structure are reconstructed.
7. If recognition or unicity fails, the obstruction is reported by the relevant diagnostic F4--F8 rather than repaired by an arbitrary choice.
8. None of this implies doctrine-free Level-3 self-generation; that stronger claim is false in general.

The shortest defensible definition is:

> **EIG Core is the least exact compositional geometry generated from an intrinsic root inside a contextually separated semantic world, relative to an independently supplied interaction doctrine.**

For cellular doctrines, local exactness laws are additionally compiled from independently specified constructor-derived occurrence/decomposition data. Full reconstruction remains a separate theorem controlled by local nervousness and operation exactness.
