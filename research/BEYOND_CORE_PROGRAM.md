# EIG Beyond the Core: Branch Research Programme

## Status of this document

This is the stable research charter for `staging/beyond-core`.

It starts from the current EIG Core, but it is **not** a theorem statement and it is **not** a
manifesto to be protected. Every architecture below is provisional. The branch exists to discover
what survives adversarial mathematics, including the possibility that the programme collapses
into existing theory or that its present North Star is wrong.

The controlling principle is:

> Do not merely express known mathematics in interaction language. Determine what rich structure
> is genuinely forced by a substantially smaller specification of primitive interaction, and
> determine exactly when that forcing fails.

---

## 1. Baseline: EIG Core versus beyond-Core mathematics

The fixed-doctrine EIG Core is the formal kernel:

```math
\operatorname{EIGCore}(D)=\operatorname{Cl}_D(R_D),
```

with contextual reduction, an intrinsic/selected root, least simultaneous semantic closure, and
canonicality relative to a declared doctrine under the hypotheses stated in `EIG_CORE.md`.

That result does not generically imply density, a nerve theorem, operation reconstruction,
coherence, realization, or a doctrine-free selector.

This branch begins where those generic Core guarantees stop. Its question is:

> Given an actual interaction grammar or mathematical universe, what nontrivial compositional
> mathematics is forced, reconstructed, classified, obstructed, or predicted?

The goal is therefore not to make EIG Core larger by definition. It is to use the Core as a clean
foundation and ask which stronger statements are independently true.

---

## 2. The naive North Star and its first correction

A first slogan is

```math
D
\longmapsto \operatorname{Shape}(D)
\longmapsto \operatorname{Law}(D)
\longmapsto \operatorname{Alg}(D).
```

This captures the intuition that allowed composition should generate the geometry of composites,
and that the geometry should constrain the local-to-global laws of models.

But bare shape is not enough. The same indexing category can support different local-to-global
laws. `\Delta`, for example, supports ordinary Segal conditions as well as weaker decomposition
or 2-Segal-style structures depending on which decompositions are distinguished.

So the live object is richer than a set/category of shapes. A candidate is a decomposition or
algebraic pattern containing, schematically,

```math
(\text{shapes},\ \text{active maps},\ \text{inert maps},\ \text{elementary shapes}),
```

or some replacement forced by the mathematics.

This leads to a provisional architecture

```math
\boxed{
D
\longrightarrow T_D
\longrightarrow \mathsf{Pat}_D
\longrightarrow \mathsf{Seg}(\mathsf{Pat}_D)
\simeq \operatorname{Alg}(T_D)
}
```

where `T_D` is a free interaction/composition object and `\mathsf{Pat}_D` is induced arity or
decomposition data.

The branch must determine whether this architecture is substantive, overly strong, too narrow,
or merely a repackaging of known machinery.

---

## 3. The likely hard boundary: free pasting versus semantic quotient

Increasing free-shape complexity is not obviously the decisive difficulty. Existing mathematics
already handles long stretches of the free-pasting world:

```text
serial composition                 -> paths / simplices
one-output substitution            -> rooted trees
many-input/many-output wiring      -> directed graph-like composites
higher/globular composition        -> pasting diagrams
```

The more revealing boundary is where distinct free composites become semantically identified:

```text
ordered composites      -> permutation symmetry
paths                    -> inverse cancellation
wiring                   -> interchange equations
graph insertion          -> feedback/equational quotient
raw behaviours           -> observational/contextual equivalence
```

The central question is therefore:

> **What compositional geometry survives semantic identification?**

A successful theory need not always return one point-valued pattern. Depending on the exact
solution problem, the right output may be:

```math
\begin{cases}
\text{a canonical descended geometry},\\
\text{a contractible/coherently unique family of adequate geometries},\\
\text{a noncanonical moduli/fibre that must be retained},\\
\text{a canonical obstruction showing that the requested descent cannot exist}.
\end{cases}
```

This solution-space viewpoint should be aligned with the canonicality/no-go discipline already
made explicit in EIG Core, rather than asserting uniqueness merely because an example admits one
convenient presentation.

---

## 4. Minimal calibrations

### 4.1 `FinSet -> Set`

A calibration is the pattern

```math
1 \longrightarrow \mathbf{FinSet} \longrightarrow \mathbf{Set},
```

where the singleton is intrinsically tiny in the stated categorical sense, finite coproducts
generate finite sets, and filtered completion generates `Set`.

The point is not to reconstruct set theory from nothing. The useful test is whether intrinsic
recognition of the root and synthetic generation meet without putting the target category into the
input.

### 4.2 Monoids

A minimal end-to-end control is one interface type, one elementary interaction, serial composition,
and an empty interaction. Free finite composites are paths. The expected classical story is

```math
\text{serial interaction}
\to \Delta
\to \text{strict reduced Segal law}
\to \mathrm{Mon}.
```

This is valuable only if the input did not already encode `\Delta`, the Segal decomposition data,
or monoid multiplication in disguised form.

### 4.3 Categories, operads, properads

Positive controls are expected to look roughly like

```text
typed serial composition             -> simplicial/path geometry -> categories
corollas + substitution              -> rooted trees             -> operads
multi-input/multi-output insertion   -> graph geometry           -> properads
```

These cases test transfer, but they are not by themselves a strong claim of novelty: large parts
of this downstream mathematics are classical.

---

## 5. Adversarial quotient tests

### 5.1 Monoids versus commutative monoids

The symmetry quotient

```math
(a,b) \sim (b,a)
```

turns ordered tuples into objects morally carrying symmetric-group actions or orbit data. This is
a tiny test of whether EIG knows the difference between information that should be forgotten and
isotropy that should be retained.

Questions include:

- Is the adequate geometry ordinary categorical, groupoidal, analytic, or higher?
- Is there a canonical descended pattern?
- If several arity systems work, what is their solution space?
- Which part of the answer was already supplied by the symmetry data?

### 5.2 Categories versus groupoids

Free groupoid completion adds inverses and cancellation

```math
ff^{-1}=1,\qquad f^{-1}f=1.
```

Many formal paths become equal. This is a sharp test of whether arities descend through quotient,
need to be replaced, or are intrinsically nonunique.

### 5.3 PROPs and interchange

Classical symmetric/interchange examples test whether the programme handles coherence that is not
merely tree substitution or path cancellation.

These adversarial cases are more informative than simply adding increasingly elaborate free
pasting shapes.

---

## 6. Prior-art boundary

The programme sits next to mature frameworks including, at least:

- monads with arities;
- polynomial and strongly cartesian monads;
- dendroidal and graphical nerve theories;
- algebraic patterns;
- operadic categories;
- Feynman categories;
- Segal objects and related recognition theorems;
- decomposition/2-Segal-style local-to-global formalisms;
- contextual equivalence and syntactic/minimal realizations.

This is an opportunity because EIG can reuse the downstream machinery. It is also the principal
failure mode.

If an "EIG doctrine" contains essentially the same data as a polynomial monad with chosen arities,
an algebraic pattern, or another mature input structure, then an extraction theorem may simply
unpack what was supplied.

A central research metric is therefore qualitative but strict:

```math
\frac{\text{structure genuinely forced in the output}}
     {\text{structure explicitly supplied in the input}}.
```

The weaker and more local the input while still forcing a rich transferable output, the stronger
the result.

---

## 7. Failure modes that must remain live

The programme fails or weakens in informative ways if any of the following occurs.

1. **Answer encoded in the doctrine.** Shapes, decompositions, coherence, or equations were already
   supplied.
2. **No canonical shape/pattern.** Several inequivalent adequate arity systems survive.
3. **Bare pattern does not determine the law.** More coverage/decomposition data must be added.
4. **Recognition remains case-specific.** No useful generic theorem survives across examples.
5. **Absorption by existing frameworks.** EIG adds no upstream or cross-framework content.
6. **Generality becomes vacuous.** "Suitable doctrine" silently means "one for which the theorem
   holds".
7. **Non-effectivity.** Canonical closure/quotient exists abstractly but cannot be computed or
   decided on interesting finite presentations.
8. **Scope contraction.** EIG may be important for compositional mathematics but not for all
   mathematics. That is an acceptable mature boundary.

A good theory should predict some failures rather than redefining itself until every example is
positive.

---

## 8. What would count as a strong general theorem

A substantive general result would start from a doctrine language demonstrably smaller than an
arity/pattern framework and give a theorem of the following kind on a nontrivial natural class:

```text
primitive interaction data
    -> free compositional object
    -> canonically characterized arity/decomposition solution space
    -> local-to-global semantics / recognition,
```

with explicit hypotheses for:

- existence;
- coherent canonicality;
- functoriality under doctrine change;
- recognition / essential image;
- descent through semantic reduction;
- failure/obstruction when the hypotheses are weakened.

The strongest form would make the positive theorem and no-go theorem two sides of the same
solution problem: contractible solution space when the hypotheses hold, and an explicit empty or
noncontractible invariant solution space when a stronger claim is impossible.

A restricted theorem is preferable to a vacuous universal theorem.

---

## 9. Effective EIG

For theoretical computer science, abstract existence is not enough. On finitely presented or
otherwise effective doctrines, investigate:

- decidability of contextual equivalence and semantic closure;
- computability of canonical residual/minimal realizations;
- generalized Myhill-Nerode theorems across words, trees, graphs, processes, or weighted systems;
- compositional verification induced by exact decomposition laws;
- coherence obstructions for combining effects;
- doctrine-parametric automata;
- intrinsic width/complexity parameters generated by canonical decompositions.

This lane should remain coupled to the same anti-tautology discipline: a complexity parameter is
interesting only if it is forced by interaction structure rather than selected after observing the
known algorithm.

---

## 10. Prediction test

The strongest eventual test is prospective rather than retrospective.

Choose an interaction doctrine that was not reverse-engineered from a known algebraic structure.
Run the best extractor justified by the theory. Then study the resulting geometry/model class as
mathematics in its own right.

A genuinely nontrivial output that was not named or encoded in advance would be much stronger
evidence for the programme than recovering another familiar nerve theorem.

Failure here is equally informative: it may identify the exact point at which the extractor was
really using hidden prior structure.

---

## 11. Meta-EIG as a provisional methodology

The North Star itself may be treated as revisable.

Candidate hypotheses such as

```text
H1: D -> Shape -> Law -> Alg
H2: D -> Pattern -> Segal -> Alg
H3: D -> FreeGeometry -> semantic reduction -> Pattern/family/obstruction
H4: the apparent EIG extractor is fully absorbed by existing machinery
```

can be tested against contexts such as Mon, Cat, Operad, Properad, CommMon, Gpd, PROP, and later
new doctrines.

For a context `C` and hypothesis `H`, useful observations include:

- correct recovery or correct negative prediction;
- amount of target structure smuggled into the input;
- canonicality actually obtained;
- ad-hoc clauses required;
- transfer to nearby examples;
- obstruction quality;
- novelty/predictive value.

Repeated failures may force operations on the research programme itself:

```text
weaken a false theorem;
add a genuinely missing datum and charge it to the input ledger;
replace strict uniqueness by coherent/contractible choice;
turn a failure into an obstruction theorem;
demand functoriality under doctrine change;
identify contextually indistinguishable research formulations;
generalize only proof patterns that recur independently.
```

This can be summarized heuristically as

```math
\text{research hypothesis}
\to \text{contexts}
\to \text{failures/observations}
\to \text{reduction}
\to \text{closure}
\to \text{stable research core}.
```

But this is **not** presently a theorem and must not become circular self-justification. Any
meta-level method depends on a chosen scientific meta-doctrine and inherits a possible regress.
Use Meta-EIG only when it produces better research decisions or genuine conceptual compression.

---

## 12. Practical research ladder

The following is a useful pool of experiments, not a rigid schedule.

### Phase I — small calibrations

1. `FinSet -> Set`.
2. The monoid end-to-end example.
3. Explicit input-data audit for each.

### Phase II — free-pasting extraction

4. Category/path geometry.
5. Operad/tree geometry.
6. Properad/graph geometry.
7. Exact comparison with existing arity/pattern frameworks.

### Phase III — quotient/coherence stress tests

8. `Mon -> CommMon`.
9. `Cat -> Gpd`.
10. PROP/interchange/symmetry examples.
11. Classify the surviving geometry or prove noncanonicality.

### Phase IV — theorem/no-go synthesis

12. Isolate the largest natural doctrine class supporting a real extraction theorem.
13. Match existence/canonicality/functoriality/recognition/descent with sharp counterexamples or
    obstruction statements outside the hypotheses.

### Phase V — effective EIG

14. Finitely presented doctrines.
15. Decidability and contextual minimization.
16. Generalized residual/minimality theorems.
17. Verification/automata/complexity consequences.

### Phase VI — prospective prediction

18. Choose a doctrine not reverse-engineered from a known answer.
19. Run the extractor without adding example-specific clauses.
20. Study the resulting geometry/algebra independently.
21. Decide whether the output is new, known under another name, degenerate, or obstructed.

At every phase, jump to the experiment with the highest expected information value rather than
completing the list ceremonially.

---

## 13. Success criteria

A strong beyond-Core theory should exhibit most of the following.

- **Weak input:** substantially less structure is supplied than recovered.
- **Correct recovery:** classical controls come out correctly.
- **Transfer:** one mechanism handles genuinely different contexts.
- **Negative prediction:** the theory says no in the right places.
- **Obstruction quality:** failure is explained by symmetry, cancellation, non-cartesianness,
  descent failure, density failure, non-effectivity, nonuniqueness, or another exact mechanism.
- **Canonicality discipline:** uniqueness is stated at the correct equivalence/homotopy level.
- **Prior-art honesty:** established machinery is cited and reused rather than renamed.
- **Prospective content:** at least eventually, the extractor generates mathematics not selected in
  advance.

---

## 14. Provisional mature form

A plausible mature description, to be earned rather than assumed, is:

> **EIG is a theory for extracting intrinsic arities, decomposition patterns, canonical
> quotients, coherent families, and obstructions from compositional interaction systems.**

One possible pipeline is

```math
\boxed{
\text{primitive interaction semantics}
\to \text{free composition}
\to \text{arity/decomposition geometry}
\to \text{Segal/nerve semantics}
\to \text{recognition}
}
```

with a second, potentially more distinctive layer

```math
\boxed{
\text{semantic identification}
\to
\begin{cases}
\text{canonical descended geometry},\\
\text{canonical/coherent family},\\
\text{retained moduli},\\
\text{obstruction}.
\end{cases}
}
```

The shortest current North-Star question is therefore:

> **Can canonical interaction geometry survive semantic identification, and can we say exactly
> when it cannot?**

Even this wording remains provisional. The purpose of the branch is not to prove this sentence.
It is to discover, through increasingly adversarial mathematics, what the sentence is forced to
become.
