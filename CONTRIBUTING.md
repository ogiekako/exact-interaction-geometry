# Contributing / research hygiene

This repository is a curated mathematical record, not the chronological scratch ledger. Contributions should preserve the distinction between theorem, audit, computation, prior art, and conjecture.

## Claim labels

Use one primary label near every theorem-scale claim:

- `AUDITED / ACCEPTED`
- `SECOND-RUN AUDITED / CANONICAL PROMOTION PENDING`
- `CLAIMED-PROVED; AUDIT PENDING`
- `KNOWN / PRIOR ART`
- `OPEN / REDUCED`
- `REFUTATION`
- `COMPUTATIONAL EVIDENCE`

Do not write `CLOSED`, `canonical`, or unqualified `PROVED` without stating the exact mathematical domain and the audit basis.

## Dossier checklist

A major theorem imported into the Book should state:

1. exact domain / exposed input structure;
2. hypotheses and quantifiers;
3. output object and theorem statement;
4. theorem dependencies versus motivation;
5. load-bearing proof skeleton;
6. nearest stronger false or unproved statement;
7. what finite verification checks and what it does **not** prove;
8. immutable source-ledger commit/path;
9. prior-art boundary;
10. dependency into the next theorem/phase.

## Source synchronization

The detailed ledger is:

```text
ogiekako/test
experiments/repairable-tropical-north-star
```

When importing a new ledger result:

1. read later audits/handoffs before copying the strongest historical status;
2. record the exact inspected commit in `provenance/SOURCE_MAP.md`;
3. import the current theorem, not every intermediate candidate;
4. preserve failed statements only when they explain a load-bearing design choice, normally in `book/COUNTEREXAMPLE_ATLAS.md`;
5. if canonical disposition changes, update `STATUS.md`, the affected dossier, and `book/THEOREM_INDEX.md` atomically;
6. never overwrite a provenance-distinct audit with an older same-run claim.

## Verifier rules

- Use explicit exception-based checks, never bare Python `assert`, for evidentiary conditions.
- Run both normal Python and `python -O`.
- Run `python -m py_compile`.
- Prefer exact integer/rational arithmetic for finite certificates.
- State whether a program is an exhaustive finite proof, an independent certificate, or only regression/calibration evidence.
- Do not infer an infinite theorem from a successful finite test suite.

## Standalone harvested results

A result intended for external publication must be decoupled from the programme:

```text
explicit object/certificate
+ elementary or standalone proof
+ independent verifier
+ fresh literature audit.
```

It is fine to state that a result was discovered while experimenting with Interaction Reconstruction, but correctness must not depend on a programme claim whose status is weaker than the standalone theorem.

## Prior-art discipline

Generic category theory, graph-product normal forms, decomposition frameworks, automata minimization, or abstract tangle machinery should be cited as scaffold. A novelty claim should identify the process-specific bridge: partial legality, noncopying interface information, recurrent recrossing, observer/action decoration, active hardness, or process-generated arities.

## Concurrent work

The research ledger and this curated repository may be edited concurrently. Before a write:

1. refresh `main`;
2. compare the intended parent with current head;
3. do not force-push over a concurrent advance;
4. reapply/merge only the nonduplicative delta;
5. rerun `make verify` after integration.

This rule is substantive: audit status can change while a documentation bundle is being prepared.
