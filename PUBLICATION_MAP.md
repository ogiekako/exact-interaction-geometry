# Publication map

This page separates results that can be published independently from programme-level synthesis that still depends on audit and exposition.

## A. Standalone external results

### A1. Source-pair augmentation counterexamples — Boolean and binary rank

**Readiness:** highest; short standalone note after final literature refresh.

**Mathematics:** explicit and independently replayed.

- Boolean: 4-row counterexample.
- Binary: 5-row counterexample.
- Binary row-minimality: exhaustive `n<=4` finite check.
- Proof body: elementary; does not rely on Interaction Reconstruction.

Files:

```text
papers/source-pair-augmentation/README.md
papers/source-pair-augmentation/paper.tex
verification/verify_source_pair_augmentation.py
```

**Remaining publication work:** refresh citation search, recheck original Section-6 terminology line-by-line, choose venue/arXiv category, compile final PDF, freeze a public commit, and optionally contact the original authors before/at posting.

### A2. Exact extension complexity of `COR(4)`

**Readiness:** mathematics has a compact exact certificate; historical novelty requires specialist audit before priority/publication claims.

The current certificate proves

```text
xc(COR(4)) = 16
```

using sixteen explicit genuine facets and a sixteen-entry fooling set, together with the trivial sixteen-vertex simplex upper bound. The curation independently replayed all 186 exact rational checks in normal and optimized Python modes.

Files:

```text
external-results/cor4-extension-complexity/README.md
verification/verify_cor4_extension_complexity.py
```

**Literature posture:** Kaibel--Weltge give exponential lower bounds; Aboulker--Fiorini--Huynh--Macchia--Seif give graph/treewidth bounds; `CUTP_5` facet incidence is classical. A targeted 2026-08-30 search did not surface an explicit published statement `xc(COR(4))=16`, but this may be folklore or implicit in old facet tables. Do not claim novelty until that is resolved.

**Next action:** independent mathematical main audit is straightforward because the certificate is finite; the harder step is specialist historical literature checking around `CUTP_5` / correlation-polytope tables.

## B. Potential theorem papers after scope-specific canonical audit

### Transactional graph-storage interfaces
Natural paper unit:

```text
raw operational ports
+ graph-product right-cone/GPSH separator
+ state-vs-dynamic interface separation
+ exact dependent shore action
+ lower bounds
```

This has a much cleaner standalone mathematical spine than the chronological Phase-III/IV ledger.

### Operational codescent for recurrent open processes
Natural paper unit:

```text
labelled-quiver colimits
--Free--> exact execution-category codescent
--black box--> mixed-return relation star
```

with the `B_a*B_b` obstruction showing why compact process interfaces are a separate theorem.

### Interaction geometry and uncrossing
Natural paper unit:

```text
exact interaction kernel / factorization atlas
+ hidden-middle no-go
+ CRT/permutability sector
+ modular residual formula
+ explicit non-submodular counterexamples
```

The main novelty claim must be phrased around the project-specific synthesis/bridge, not around standard Mal'tsev or modular-lattice facts.

## C. Protected/certifiable Grand Book

The protected G1--G7 theorem is now **SECOND-RUN AUDITED / CANONICAL PROMOTION PENDING** at the current phase-status checkpoint. It is therefore closer to a theorem paper/monograph chapter than earlier `AUDIT PENDING` versions, but the source ledger still explicitly requests canonical local-main promotion.

Do not publish it as `REACHED` until that governance/mathematical integration pass is complete and the exact `Proc_prot^0` domain is frozen.

## D. Monograph / programme paper

The seven-phase Interaction Reconstruction Book is best treated as a research monograph/compendium until:

1. protected G1--G7 receives canonical promotion in its exact domain;
2. the strong Phase-VI reduced process-generated realization theorem is final;
3. the Phase-VII actual-interface arity theorem is stated/proved or explicitly left as the final frontier.

The generic Phase-VI/VII shells are prior art and should appear as organizing context, not claimed novelty.

## E. Results that should not be advertised as novelty by themselves

- generalized Grothendieck / category-over-base to normal-lax `Prof`;
- Conduche/exponentiable pseudo-Prof correspondence;
- Yoneda/density and finitely presentable arities in presheaf categories;
- nervous monads / monads with arities;
- Foata normal forms for graph products of monoids;
- structured decompositions, abstract tangle duality, monoidal width, functorial automata minimization.

Their role is scaffold. The research claim is in the exact bridge to partial legality, recurrent feedback, observer/action decoration, noncopying interfaces, active hardness, and process-generated arities.
