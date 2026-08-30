# Interaction Reconstruction

**Local interactions, exact interfaces, and reconstruction of mathematical structure.**

This repository is the curated, audit-oriented home of a research programme that began with finite-interface recurrent dynamics and evolved toward a broader question:

> **When can a mathematical object, process, or mathematical world be reconstructed from its local interactions, interfaces, and gluing laws?**

The programme is a seven-phase chain:

```text
I    exact feedback semantics and optimal no-go boundaries
II   effective structural coastlines
III  intrinsic transactional/compositional object
IV   Grand Book: interfaces, decomposition, reconstruction, torsos, obstructions
V    interaction geometry: exact resource first, scalar second
VI   realizability: Grothendieck / normal-lax Prof
VII  interaction arities: reconstruction from small local probes
```

The name **Interaction Reconstruction** is the endpoint viewpoint, not a Phase-VII-only label. Phases I--IV are load-bearing: they explain why the later proarrow, factorization, profunctor, residual, and arity structures are forced.

## Start here

- [`book/README.md`](book/README.md) — seven-phase mathematical narrative.
- [`book/THEOREM_INDEX.md`](book/THEOREM_INDEX.md) — theorem-scale inventory.
- [`book/dossiers/`](book/dossiers/) — exact hypotheses, statements, proof skeletons, boundaries, and audit provenance.
- [`book/COUNTEREXAMPLE_ATLAS.md`](book/COUNTEREXAMPLE_ATLAS.md) — anti-theorems that shaped the theory.
- [`book/DEPENDENCY_GRAPH.md`](book/DEPENDENCY_GRAPH.md) — mathematical dependency DAG.
- [`STATUS.md`](STATUS.md) — conservative current disposition.
- [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) — only the load-bearing open theorems and promotion gates.
- [`AUDIT_PROTOCOL.md`](AUDIT_PROTOCOL.md) — how a claim is promoted.
- [`PUBLICATION_MAP.md`](PUBLICATION_MAP.md) — standalone consequences and paper readiness.
- [`bibliography/README.md`](bibliography/README.md) — closest prior art and novelty boundaries.
- [`verification/README.md`](verification/README.md) — what the finite certificates establish.
- [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md) — exact source-ledger synchronization map.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — curation, verifier, and concurrent-work discipline.
- [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md) — checklist before making the repository/public result a release artifact.

## Machine-checkable core

Run

```bash
make verify
```

or execute the files under [`verification/`](verification/). The current compact verification suite checks:

1. the Boolean and binary source-pair augmentation counterexamples;
2. operational codescent boundary fixtures and mixed-return behaviour;
3. the four-state no-choice / no-collapse calibrations;
4. finite interaction-CRT and residual-nerve reconstructions.

Every evidentiary verifier is also run under `python -O` in CI so that language-level `assert` removal cannot silently erase checks.

Build the standalone source-pair paper locally with

```bash
make paper
```

when `pdflatex` is available. Verification CI remains independent of a heavyweight TeX installation.

## First standalone consequence: both ranks

The programme's first harvested external consequence is now stronger than the initial Boolean-only note. The Parnas--Shraibman Section-6 source-pair question has explicit counterexamples for **both Boolean rank and binary rank**:

- four rows for Boolean rank;
- five rows for binary rank, with exhaustive verification that no binary example exists on at most four rows.

See:

- [`papers/source-pair-augmentation/README.md`](papers/source-pair-augmentation/README.md)
- [`papers/source-pair-augmentation/paper.tex`](papers/source-pair-augmentation/paper.tex)
- [`verification/verify_source_pair_augmentation.py`](verification/verify_source_pair_augmentation.py)

The proofs are standalone and elementary. Their correctness does **not** depend on the broader Interaction Reconstruction programme; the programme is discovery provenance only.

## Current Phase-IV caveat

The original research ledger is advancing concurrently. At the latest synchronized snapshot (`ogiekako/test@79f64b1a7634341f66482ae19250aa9fa8677d7d`), a corrected terminal G7 bundle has survived a provenance-distinct second-run adversarial audit in the normalized native protected/certifiable domain, with no identified mathematical blocker remaining in literal G7. However, that handoff explicitly says it is **not yet canonical local-main promotion**. This repository therefore records the protected G1--G7 result as `SECOND-RUN AUDITED / CANONICAL PROMOTION PENDING`, rather than silently declaring the unrestricted Grand Book closed.

## Provenance

The detailed chronological research ledger remains:

```text
ogiekako/test
experiments/repairable-tropical-north-star
```

This repository is a **curated reconstruction**, not a mirror. Its original migration baseline was `3806b8e...`; its current synchronized ledger snapshot is recorded in [`provenance/SOURCE_MAP.md`](provenance/SOURCE_MAP.md).

## Status vocabulary

- `AUDITED / ACCEPTED`
- `SECOND-RUN AUDITED / CANONICAL PROMOTION PENDING`
- `CLAIMED-PROVED; AUDIT PENDING`
- `KNOWN / PRIOR ART`
- `REFUTATION`
- `COMPUTATIONAL EVIDENCE`
- `OPEN / REDUCED`

The repository prefers a narrower theorem with a clean audit trail to a stronger slogan whose scope is ambiguous.
