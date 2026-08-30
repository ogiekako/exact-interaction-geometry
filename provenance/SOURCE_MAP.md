# Source map to the original research ledger

This repository is curated. The original chronological ledger is `ogiekako/test`, subtree `experiments/repairable-tropical-north-star`.

## Snapshots

```text
original migration baseline:
  3806b8ea4851f6edfa7073085e929bdd868442b9

latest inspected synchronization snapshot:
  c25815e82faba9beb8b9deb96d740ee345138872

latest phase-status-changing checkpoint:
  79f64b1a7634341f66482ae19250aa9fa8677d7d
```

The later `c25815e...` commit adds a standalone exact `xc(COR(4))=16` certificate and does not alter the imported Phase-I--VII dispositions from `79f64b1...`.

When a source below existed at the original baseline, links may still point to that immutable commit. Later status corrections are explicitly keyed to the later snapshot.

## Phase I

- `docs/NORTH_STAR.md`
- canonical synthesis referenced there: `OPTIMAL_RELATIVE_NORTH_STAR_TERMINAL_SYNTHESIS_20260829.md`

## Phase II

- `docs/AUDIT_EFFECTIVE_STRUCTURE_COASTLINE_MAIN_20260830.md`
- `docs/AUDIT_EFFECTIVE_STRUCTURE_COASTLINE_INDEPENDENT_20260830.md`

## Phase III

- `docs/PHASE_III_INTRINSIC_OBJECT_PROGRAM_20260830.md`
- `docs/PHASE_III_TRANSACTIONAL_GRAPH_STORAGE_BOOK_TERMINAL_20260830.md`
- `docs/AUDIT_POST_PHASE_III_INTRINSIC_AFFINE_MAP_SPECTRUM_20260830.md`

## Phase IV structural spine

- `docs/GRAPH_MINORS_SCALE_GRAND_BOOK.md`
- `docs/AUDIT_POST_PHASE_III_OPERATIONAL_CODESENT_GRAND_BOOK_REDUCTION_20260830.md`
- `docs/GRAPH_PRODUCT_SEPARATOR_PROARROW_MINIMALITY_20260830.md`
- `docs/UNIVERSAL_BOOK_MAXIMALITY_NO_CHOICE_20260830.md`
- `docs/AUDIT_UNIVERSAL_BOOK_MAXIMALITY_MAIN_20260830.md`
- protected G1 repair/audit chain recorded in `.handoff/STATE.md`

## Protected G7 status checkpoint at `79f64b1...`

- `.handoff/20260830-2020-jst-terminal-g7-second-run-audit.md`
- `docs/AUDIT_TERMINAL_G7_SECOND_RUN_20260830.md`
- `docs/TERMINAL_G7_ADVERSARIAL_REPAIR_20260830.md`
- `docs/CANONICAL_EVALUATOR_CORES_G7_20260830.md`
- `docs/G7_NONHEREDITARY_EVALUATOR_BOUNDARY_20260830.md`

Disposition imported here: **second-run adversarial audit accepted the corrected literal G7 in `Proc_prot^0`; canonical local-main promotion still requested.**

## Phase V--VII

- `docs/PHASE_V_WHY_STRUCTURE_GOAL_CRITERIA_20260830.md`
- `docs/PHASE_V_VI_VII_TERMINAL_INTERACTION_ARITY_CLOSURE_20260830.md`
- `docs/AUDIT_PHASE_V_VI_VII_TERMINAL_CLOSURE_20260830.md`
- `verification/verify_phase_v_vii_interaction_arity_closure_20260830.py`

## Literature audit

- `docs/CATEGORICAL_GRAND_BOOK_LITERATURE_AUDIT_20260830.md`

This audit maps structured decompositions, monoidal width, open Petri/network semantics, Span(Graph), graph-product Foata theory, abstract tangles, bialgebraic semantics, functorial minimization, and Grothendieck/sheaf machinery. It explicitly warns that these ambient theories are prior art.

## Source-pair augmentation counterexamples

At `b2601fdb...` and later:

- `docs/AUGMENTATION_SOURCE_PAIR_COUNTEREXAMPLES_BOTH_RANKS_20260830.md`
- `verification/verify_augmentation_source_pair_both_ranks_20260830.py`

The curation independently replayed the exact enumeration and rewrote the combined paper so that both displayed counterexample theorems have elementary proof bodies independent of exhaustive search.

## Exact `COR(4)` extension complexity harvest

At `c25815e82faba9beb8b9deb96d740ee345138872`:

- `docs/COR4_EXACT_EXTENSION_COMPLEXITY_16_20260830.md`
- `verification/verify_cor4_extension_complexity_16_20260830.py`
- `.handoff/20260830-2037-jst-cor4-exact-extension-complexity.md`

Source disposition:

```text
mathematics:
  CLAIMED-PROVED / exact 16-fooling-set certificate;

curation replay:
  normal Python PASS;
  python -O PASS;
  py_compile PASS;
  186 explicit exact checks;

historical novelty:
  UNVERIFIED; specialist CUTP_5 / correlation-polytope literature audit pending.
```

This is an external theorem harvest, not a dependency of the Grand Book.
