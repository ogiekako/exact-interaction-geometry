# Exact Interaction Geometry Core

## Canonical Level-2 formulation

**Status:** frozen candidate on the stated small/finitary Level-2 class.  
**Scope:** an independently supplied exact interaction/composition doctrine is input.  
**Non-claim:** a bare object/map world does not in general determine its interaction doctrine.

---

## 1. Executive statement

For a fixed interaction doctrine `D`, Exact Interaction Geometry separates four logically different tasks:

1. **contextual separatedification** — erase exactly the distinctions invisible to every admitted context;
2. **semantic shape generation** — close an intrinsic generic root under the doctrine's actual exact composition and universal constructions;
3. **local-law compilation** — on cellular doctrines, compile the local comparison laws forced by elementary occurrences and universal properties;
4. **recognition** — separately test whether the generated arities and laws actually reconstruct the intended world and its operations.

The central object is

\[
\boxed{
\operatorname{EIGCore}(D)
=
\mu\Psi_D
\quad\text{inside the contextually separated semantic world }S_D.
}
\]

In Set-like deterministic sectors, `S_D` is concretely the quotient by a greatest fixed point

\[
\nu\Phi_D,
\]

so the slogan becomes

\[
\boxed{
\text{least exact compositional geometry inside the greatest contextually justified quotient.}
}
\]

The fixed-point construction does **not** by itself imply reconstruction. Density, local nervousness, and operation exactness remain separate recognition gates.

---

## 2. Level boundary

### Level 1

An arity theory/monad is already supplied; one proves a nerve theorem or characterizes its models.

### Level 2 — the positive EIG theorem

The world and an exact interaction/composition doctrine are supplied, but the arity/shape theory is not. EIG reconstructs an intrinsic root, closes it under the actual doctrine, and then tests reconstruction.

### Level 3 — false in general

A bare extensional object/map world is asked to select its own interaction doctrine.

This fails in general. The same map-level world can support, for example, a witness-preserving span doctrine or a witness-forgetting relation doctrine. Map data alone does not decide whether witness multiplicity is semantically meaningful.

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
- `S`: semantic worlds and their contextual/exact reductions;
- `O`: admitted observations and closing contexts;
- `K`: actual typed constructors, possibly partial, dependent, or profile-changing;
- `U`: declared exact universal constructions, e.g. image, pullback, tabulation, support reflection, Cech/codescent, free path/Segal completion;
- `E`: the honest equivalence notion: isomorphism, equivalence, Cauchy, Morita, or moduli-valued.

The current fixed-point theorem assumes:

- all relevant profiles, root data, constructor families, and finite comparison schemes are set-sized in a fixed universe;
- constructors and universal diagrams are finitary;
- semantic reduction is characterized by a universal property, not an arbitrary chosen embedding;
- retract splitting and equivalence closure stay inside the declared universe.

For the local-law compiler, a further **cellular/occurrence-equipped** hypothesis is required; see Section 7.

---

## 4. Contextual separatedification

The general object is a contextual separatedification/reflection

\[
S_D:\mathcal R_D\longrightarrow\mathcal S_D^{\mathrm{sep}},
\]

characterized by the universal requirement that it performs the largest identification sound under all admitted contexts.

### 4.1 Set-like deterministic realization

In a many-sorted Set-like sector, let `Rel_D` be the complete lattice of typed relation candidates. Define a monotone operator

\[
\Phi_D:\mathrm{Rel}_D\to\mathrm{Rel}_D
\]

by declaring `x Phi_D(R) y` iff:

1. all immediate admitted observations agree;
2. every admitted one-step partial constructor has the same definedness on the two inputs;
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

**Proof.** Fixed-point stability propagates equality through contexts by induction on context depth. Conversely, all-context indistinguishability is a post-fixed point of `Phi_D`, hence lies below its greatest fixed point. The reverse inclusion is the first direction. ∎

The higher/enriched theory need not be forced into a Set-valued relation calculus. There `S_D` may be realized by an effective quotient, localization, homotopy image, stack quotient, or another doctrine-appropriate universal separatedification.

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

The doctrine's universal exact reduction/completion sends this raw root to a semantic root

\[
A_0(D)\subseteq\mathcal S_D^{\mathrm{sep}}.
\]

The realization must be characterized universally. If literal uniqueness fails, the correct output may be a contractible choice, equivalence class, groupoid, Morita class, or moduli object.

---

## 6. Least exact semantic geometry

### 6.1 Exactized constructors

Composition must be read in the target semantic world. Schematically, for a constructor `K`,

\[
\bar K=S_D\circ K,
\]

with the relevant separated inclusions on its inputs.

The intended order is:

```text
raw/native composition
  -> target semantic reduction/recanonicalization.
```

This matters for partial, profile-changing, or witness-sensitive composition.

### 6.2 Closure operator

On replete small semantic shape classes define

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

If `Psi_D` is monotone on the declared complete shape lattice, then

\[
\boxed{
A_D^{\mathrm{EIG}}
=\mu_{A\supseteq A_0(D)}\Psi_D(A)
}
\]

exists and is the least replete, Cauchy-closed semantic shape class containing `A_0(D)` and closed under every declared exact constructor and universal operation.

If, in addition, `Psi_D` preserves the relevant directed unions (in particular in the stated finitary sectors where this is separately verified), then

\[
A_D^{\mathrm{EIG}}
=\bigcup_{n<\omega}A_n,
\qquad
A_{n+1}=\Psi_D(A_n).
\]

The Tarski existence statement and the Kleene `omega`-iteration statement are therefore logically distinct.

### 6.3 Cauchy closure must be iterative

A final one-shot Karoubi completion can fail.

Take a semantic category containing objects `1,2,3`, with `1` a retract of `2`. Let a partial constructor be defined only on `1`, with `K(1)=3`, and start from `{2}`. Constructor closure before retract splitting never sees `1`; a final Karoubi completion adds `1` but still misses `3`. Stagewise constructor--Kar closure adds `1` and then `3`.

Hence the fixed point must interleave constructor/universal closure with retract closure.

---

## 7. Associated theory and the cellular law compiler

### 7.1 Full semantic theory

After the object class has been generated independently, define

\[
\boxed{
\Theta_D^{\mathrm{EIG}}
=
\operatorname{Full}_{\mathcal S_D}(A_D^{\mathrm{EIG}}),
}
\]

using the doctrine's intended structural morphism class when it is narrower than ambient Homs.

This avoids inventing a free mixed syntax and then separately proving that its hidden equations and Homs coincide with the semantic world.

### 7.2 Why an extra cellular hypothesis is necessary

A generic semantic shape does **not** canonically determine which maps from Tiny objects count as its elementary occurrences.

For example, for the free-category shape `[2]`, all semantic maps `[1] -> [2]` include the composite edge `0 -> 2`; the Segal spine should contain only the two immediate edges `0 -> 1` and `1 -> 2`.

Therefore the law compiler is not claimed for arbitrary Level-2 doctrines solely from the tuple in Section 3.

A **cellular/occurrence-equipped Level-2 doctrine** additionally supplies, or functorially derives from independently specified constructor structure:

- a subtheory of elementary/generic shapes `A_D^el`;
- a doctrine-invariant class of inert/occurrence maps into generated shapes;
- the restriction/overlap maps between such occurrences;
- coherence ensuring these data are preserved by doctrine equivalence.

This data may be intrinsic to a standard algebraic pattern, polynomial/operadic presentation, globular pasting theory, or a separately audited recurrent occurrence calculus. It must not be reverse-engineered from the desired essential image.

For such a doctrine define

\[
\operatorname{Occ}_D(T)
=(A_D^{el}\downarrow_{\mathrm{occ}}T)
\]

and the elementary core

\[
I_D(T)
=
\operatorname*{colim}_{e\to T\in\operatorname{Occ}_D(T)}y(e)
\longrightarrow y(T).
\]

### 7.3 Typed defect laws

For a comparison test

\[
j_\tau:B_\tau\to C_\tau
\]

and boundary instance `u:B_tau -> X`, let

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

A law records the required fibre profile, which may be:

- nonempty — existence;
- contractible/singleton — existence and uniqueness;
- prescribed discrete multiplicity;
- prescribed isotropy/groupoid;
- prescribed higher homotopy/coherence type;
- a declared universal limit/colimit/tabulation property.

Ordinary orthogonality is only the contractible-filler sector.

### 7.4 Saturation

Let `ElemCmp_D(A)` consist of the occurrence-core comparisons and the comparisons canonically generated by the doctrine's declared universal properties. Let `Sat_D` close them under exactly the admitted finite operations:

- typed substitution;
- whiskering and finite pasting;
- allowed base change;
- semantic equivalence and retract;
- actual reassociation/interchange cells;
- defined composition of filler profiles.

Define

\[
\boxed{
\mathcal L_D
=
\operatorname{Sat}_D
\bigl(\operatorname{ElemCmp}_D(A_D^{\mathrm{EIG}})\bigr).
}
\]

By construction, this is exactly the finite local comparison theory generated from the independently specified occurrence and universal-property data. If the actual nerve image obeys additional genuinely global restrictions, that is not hidden inside this compiler; it is diagnosed by the local-nervousness gate below.

---

## 8. Recognition is not closure

Let

\[
J_D:\Theta_D^{\mathrm{EIG}}\hookrightarrow\mathcal W_D
\]

be the generated arity inclusion, and

\[
N_D(X)=\mathcal W_D(J_D-,X)
\]

the restricted interaction nerve.

### 8.1 Density

`J_D` is dense iff `N_D` is fully faithful, equivalently iff the density counit is invertible.

An intrinsic root can fail to be dense. For example, embed `Set` into `Set x Set` by `X |-> (X, empty)`. The intrinsic Tiny root maps to `(1,empty)`, whose nerve forgets the entire second component.

Density is therefore a recognition condition, not a consequence of root canonicality.

It also cannot in general be absorbed into an ordinary closure system: dense full subcategories need not be closed under intersection.

### 8.2 Local nervousness

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

This is stronger than density: it identifies the essential image with the blindly compiled local model theory.

### 8.3 Operation exactness

For an admitted world operation

\[
K:\mathcal W_1\times\cdots\times\mathcal W_m\to\mathcal W_0
\]

define its arity module

\[
M_K(b;a_1,\ldots,a_m)
=
\mathcal W_0\bigl(J_0b,K(J_1a_1,\ldots,J_ma_m)\bigr).
\]

There is a canonical comparison

\[
\kappa_{K,\vec X}(b):
\int^{a_1,\ldots,a_m}
M_K(b;a_1,\ldots,a_m)
\times
\prod_i\mathcal W_i(J_ia_i,X_i)
\longrightarrow
\mathcal W_0(J_0b,K(\vec X)).
\]

`K` is **arity-exact** iff every such comparison is invertible.

Density alone does not imply this. `FinSet -> Set` is dense, while the identity functor and the ultrafilter functor agree on finite sets but differ on suitable infinite sets.

If `M_K` is not representable by an honest arity functor, the canonical answer may still be the module/proarrow itself.

---

## 9. EIG-exact doctrines

A doctrine is **EIG-exact for a claimed reconstruction target** when:

1. the generated arity inclusion is dense;
2. the restricted nerve is local-nervous with respect to the compiled local law theory;
3. every claimed admitted external operation is arity-exact;
4. the declared morphism/base-change structure is coherently reconstructed.

Then the nerve reconstructs the intended world and its claimed operation structure at the declared equivalence level.

The gates are diagnosed separately. In particular, local nervousness implies density; they are separate tests, not logically independent axioms.

---

## 10. Canonicality

The canonicality claimed here is not literal uniqueness of a chosen small presentation.

The honest levels are:

1. isomorphism/equivalence;
2. Cauchy equivalence;
3. Morita/model equivalence;
4. groupoid/stack/moduli-valued uniqueness when isotropy remains.

### Theorem 10.1 — doctrine-equivalence invariance

Suppose an equivalence of Level-2 doctrines

\[
F:D\simeq D'
\]

coherently preserves the data used by the construction: profiles, observations, contextual separatedification, Tiny roots, exact reductions, typed constructors, universal operations, and the equivalence/Cauchy/Morita convention. In the cellular subclass, also require preservation of elementary objects, occurrence maps, and filler profiles.

Then the induced equivalences intertwine the relevant operators, and therefore carry the contextual separatedification, least semantic fixed point, associated semantic theory, and compiled local law theory to the corresponding outputs for `D'`.

This is the precise sense in which superficial changes of presentation do not change EIG.

---

## 11. Failure coastline

The construction records exact failure modes rather than converting them into hidden choices.

- **F0 doctrine ambiguity:** the bare world does not select a unique interaction doctrine.
- **F1 root failure:** no essentially small intrinsic Tiny/Cauchy root exists in the declared universe.
- **F2 reduction failure:** no canonical/universal exact reduction is available.
- **F3 size/continuity failure:** the required closure escapes the universe or lacks the continuity needed for effective finite-stage generation.
- **F4 local-nervousness failure:** compiled local models strictly exceed the actual nerve image; a countermodel or essential-image mismatch witnesses the obstruction.
- **F5 density failure:** the density counit is noninvertible.
- **F6 operation failure:** some `kappa_K` is noninvertible.
- **F7 nonrepresentability:** the correct external action exists canonically only as a module/proarrow. This may identify the correct categorical level rather than a failure of EIG.
- **F8 isotropy/moduli:** literal uniqueness fails but a canonical groupoid, Morita class, or moduli object remains. This is a unicity diagnosis, not necessarily a failure.

---

## 12. Frozen calibrations

The same architecture specializes as follows.

### Free categories

- raw root: walking vertex and walking edge;
- composition: free path composition;
- generated shapes: finite linear paths;
- associated theory: `Delta`;
- cellular occurrences: immediate path edges;
- local laws: simplicial Segal conditions.

### Fixed-colour nonsymmetric operads

- raw root: generic corollas;
- composition: operadic substitution;
- generated shapes: planar rooted trees;
- cellular occurrences: vertex corollas;
- local laws: tree Segal-core conditions.

### Strict globular `n`-categories

- raw root: globe cells;
- composition: strict globular pasting;
- generated shapes: globular pasting diagrams;
- associated theory: `Theta_n`-type pasting theory;
- cellular occurrences: elementary globes/cells;
- local laws: globular Segal comparisons.

### Normalized protected recurrent world

- raw root: Tiny boundary/cell family sectors;
- exact reduction: joint coherent images, witness/storage tabulations, pullbacks, support/context, derived owner geometry;
- temporal closure: shared-interface ULF/strict-Segal paths;
- local ledger: image soundness/onto/extensionality, reduced evaluator laws, witness/storage pullback laws, FIX/NULL/EQ/LEGAL, finite context laws, glued strict-Segal path laws;
- external operations: SYNC, STORE, SPACE, star, observer/public projection are handled by module/comparison exactness rather than forced into one mixed free monad;
- unicity: model-Morita equivalence is the honest endpoint.

The recurrent row is important because it forces the compiler to distinguish existence, uniqueness, multiplicity, and retained witness geometry rather than collapse everything to ordinary Segal orthogonality.

---

## 13. Meta-EIG

Meta-EIG is a doctrine-relative discovery formalism, not a doctrine-free selector of all legitimate mathematics.

Fix a meta-doctrine `M` describing which comparison constructions, defect extractions, and universal realizations are admissible.

Let `Sh` and `Law` be set-sized universes of admissible semantic shapes and typed defect tests. A state is

\[
(A,\Lambda)\in\mathcal P(\mathsf{Sh})\times\mathcal P(\mathsf{Law}).
\]

Define a monotone simultaneous generation operator

\[
\mathbb F_{D,\mathfrak M}(A,\Lambda)
=
\bigl(\Psi_{D,\mathfrak M}(A,\Lambda),
G_{D,\mathfrak M}(A,\Lambda)\bigr),
\]

where schematically

\[
\Psi(A,\Lambda)
=
\operatorname{KarRepl}
\bigl(A_0\cup K(A)\cup U(A)\cup\operatorname{Real}(\Lambda)\bigr),
\]

and

\[
G(A,\Lambda)
=
\operatorname{Sat}_{D,\mathfrak M}
\bigl(\Lambda\cup\operatorname{ElemCmp}_{D,\mathfrak M}(A)\bigr).
\]

`Real(Lambda)` may add a derived semantic sort only when the doctrine/meta-doctrine gives a canonical universal realization; a failing example alone never licenses an arbitrary new object.

### Theorem 13.1 — simultaneous fixed point

If the two universes are set-sized and `F` is monotone, then

\[
\boxed{
(A_D^*,\Lambda_D^*)
=
\mu\mathbb F_{D,\mathfrak M}
}
\]

exists by Knaster-Tarski.

If the generation operator preserves the relevant directed unions, the least fixed point is obtained by its Kleene chain.

### Level-2 triangularization

When the exact interaction/completion doctrine is already supplied, semantic shape generation is independent of newly discovered law data:

\[
\Psi(A,\Lambda)=\Psi_D(A).
\]

Then the simultaneous fixed point triangularizes: first compute

\[
a^*=\mu\Psi_D,
\]

then compute the least law fixed point at `a*`.

This explains the successful Level-2 order:

```text
contextual separatedification
  -> Tiny / exact reduction
  -> least semantic shape closure
  -> cellular local-law compilation
  -> recognition gates.
```

---

## 14. What is standard and what is project-specific

The following ingredients are standard mathematics in their established scopes:

- Myhill-Nerode / syntactic congruence / coalgebraic behavioral equivalence;
- Knaster-Tarski and Kleene fixed-point theorems;
- Tiny/small-projective objects and Karoubi/Cauchy completion;
- restricted Yoneda, density, nerve-realization adjunctions;
- monads with arities and associated theories;
- algebraic patterns and Segal-object formalisms;
- spans, relations, profunctors, Grothendieck constructions, equipments;
- Cauchy/Morita completion and moduli-valued unicity.

No priority claim is made here for those ingredients.

The project-specific synthesis currently being asserted is the doctrine-indexed architecture

\[
\boxed{
S_D
\;\triangleright\;
\mu\Psi_D
\;\triangleright\;
\mathcal L_D
\;\triangleright\;
\text{density/local-nervousness/operation recognition},
}
\]

with typed witness-defect laws, external module actions, and an explicit failure coastline.

Whether this entire combined architecture already exists in the literature under another formulation remains a separate specialist prior-art question. It is not settled merely by the present fixed-point theorem.

---

## 15. Final theorem

### Final Level-2 EIG Core theorem

Let `D` be a small Level-2 exact interaction doctrine satisfying the hypotheses above.

1. A doctrine-appropriate contextual separatedification `S_D` is part of the admissible Level-2 setup; in Set-like deterministic sectors it is computed by the all-context greatest fixed point `nu Phi_D`.
2. The exactized semantic closure operator has a least fixed point
   \[
   A_D^{\mathrm{EIG}}=\mu\Psi_D.
   \]
3. The associated interaction theory is the doctrine-appropriate full semantic theory on that independently generated object class.
4. If `D` is cellular/occurrence-equipped, its doctrine-generated finite local law theory is compiled from elementary occurrence cores and declared universal comparisons, with typed filler profiles.
5. Equivalent doctrines preserving the relevant structure give equivalent EIG outputs at the declared equivalence/Cauchy/Morita/moduli level.
6. If the restricted nerve is dense, is local-nervous with respect to the compiled law theory, and every claimed external operation is arity-exact, then the intended world and claimed operation structure are reconstructed.
7. If recognition or unicity fails, the obstruction is recorded by the appropriate diagnostic F4--F8 rather than repaired by an arbitrary choice.
8. None of this implies doctrine-free Level-3 self-generation; that stronger claim is false in general.

---

## 16. Compact definition

The shortest defensible formulation is:

> **EIG Core is the least exact compositional geometry generated from an intrinsic root inside a contextually separated semantic world, relative to an independently supplied interaction doctrine.**

For cellular doctrines, local exactness laws are then compiled from intrinsic occurrence/universal comparison data. Full reconstruction is a separate theorem, controlled by density, local nervousness, and operation exactness.

This is the canonical Level-2 formulation to use unless a concrete counterexample forces another structural distinction.
