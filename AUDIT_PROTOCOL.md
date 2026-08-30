# Audit protocol

This repository separates mathematical truth, machine evidence, novelty, and governance. They are not interchangeable.

## 1. Claim states

### `CLAIMED-PROVED; AUDIT PENDING`
A proof or exact finite certificate exists, but it has not survived the required independent reconstruction.

### `AUDITED / ACCEPTED`
A provenance-distinct audit or canonical main audit has reconstructed the load-bearing argument, checked scope, and found no mathematical blocker.

### `SECOND-RUN AUDITED / CANONICAL PROMOTION PENDING`
A provenance-distinct adversarial audit accepts the corrected result, but the original ledger's governance explicitly requests a final canonical local-main promotion. This is currently used for protected/certifiable terminal G7.

### `KNOWN / PRIOR ART`
The statement is standard or published mathematics used as scaffold. It must not be advertised as programme novelty.

### `REFUTATION`
A stronger tempting statement has an explicit counterexample or no-go theorem.

### `COMPUTATIONAL EVIDENCE`
Finite regression or search evidence only; never promoted to an infinite theorem by itself.

## 2. Promotion checklist

A theorem-scale claim is promoted only after the following are explicit:

1. **Domain.** Exact input class and exposed structure.
2. **Statement.** Quantifiers and output object.
3. **Dependencies.** Which upstream results are theorem dependencies versus motivation.
4. **Proof skeleton.** The load-bearing steps, not merely a theorem name.
5. **Boundary.** The nearest stronger false statement or excluded scope.
6. **Verification role.** What code checks and, equally important, what it does not prove.
7. **Provenance.** Immutable source commit/path.
8. **Literature boundary.** Which ingredients are prior art and where the claimed bridge begins.

## 3. Verifier discipline

Every evidentiary Python verifier in this repository should:

- use explicit exception-based checks for theorem evidence;
- pass in normal mode;
- pass under `python -O`;
- pass `python -m py_compile`;
- avoid floating point when an exact finite certificate is available;
- state whether it is a proof certificate, exhaustive finite theorem, or regression fixture.

CI runs these modes on each maintained verifier.

## 4. Counterexample publication rule

A harvested counterexample is intentionally decoupled from the broader programme:

```text
programme correctness  --not a dependency-->  counterexample correctness
```

A standalone counterexample paper should contain:

- the original question;
- the explicit finite object;
- an elementary verification whenever possible;
- an independent exact verifier;
- discovery provenance only as a note/acknowledgment;
- a fresh literature search immediately before public priority claims.

## 5. Curation rule

The old research ledger preserves failed routes and chronological detail. This repository preserves the **currently live mathematical spine**. A historical file is not copied merely because it once said “terminal”; it is represented only if its statement remains live after later audit.
