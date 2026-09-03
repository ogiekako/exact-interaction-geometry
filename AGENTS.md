# Autonomous research instructions for `staging/beyond-core`

This branch is an autonomous research workspace for the programme in
[`research/BEYOND_CORE_PROGRAM.md`](research/BEYOND_CORE_PROGRAM.md).

The user should be able to open Codex in a clone of this branch and say only
`はじめてください`, `start`, `continue`, `go on`, or an equivalent short instruction.
That is sufficient authorization to choose the next research move, do the work, update the
branch, and push coherent results. Do not ask the user to choose a subproblem merely because
several mathematically reasonable directions are available.

This file governs work on this branch. It is intentionally stronger and more operational than
the public-facing README.

## 1. Durable goal

If the Codex interface exposes a durable `/goal` facility and no appropriate goal is active,
set the goal yourself. Do not require the user to formulate it.

The goal must be abstract enough to survive many concrete experiments. Use this as the default:

> Determine, by adversarial mathematics, the strongest non-tautological theorem or sharp
> obstruction governing when primitive interaction semantics force compositional geometry
> beyond fixed-doctrine EIG Core, especially what survives semantic identification; revise the
> research North Star when evidence requires it.

Do **not** set a goal such as "prove the commutative-monoid case" or "recover Delta". Those are
possible experiments, not the durable objective.

If the interface cannot set `/goal` programmatically, treat the paragraph above as the active
session goal and preserve its current refinement in `research/STATE.md`.

The goal is outcome-neutral. A collapse into existing theory, a no-go theorem, a proof that the
input already contains the alleged output, or a demonstration that the programme is pointed at
the wrong invariant all count as success.

## 2. Start / continue protocol

On a bare start-or-continue instruction, act rather than requesting scope.

1. Inspect `git status --short --branch` and recent history.
2. Work only on `staging/beyond-core` unless the user explicitly says otherwise.
3. Integrate remote work before beginning a new substantial unit:
   - if the worktree is clean, fetch and `git pull --rebase`;
   - if it is not clean, understand and preserve the local work first; never discard it blindly.
4. Read, at minimum:
   - `AGENTS.md`;
   - `research/STATE.md`;
   - `research/BEYOND_CORE_PROGRAM.md`;
   - the relevant parts of `EIG_CORE.md`;
   - `README.md`, `PRIOR_ART.md`, `CONTEMPORARY_NEIGHBORS.md` when novelty or positioning matters;
   - `provenance/RESEARCH_PROCESS.md` when deciding promotion/audit status.
5. Reconstruct the current mathematical frontier from the repository rather than assuming the
   last chat message described it completely.
6. Select the next attack by expected information gain: prefer a theorem, counterexample,
   reduction, prior-art identification, or finite experiment that discriminates between live
   structural hypotheses.
7. Work the chosen attack to a sharp stopping point. Do not stop after merely producing an
   agenda if a proof, counterexample search, computation, or literature check can be performed.
8. Update `research/STATE.md` before ending a meaningful session.
9. Promote mature mathematics to an appropriate stable file only when warranted.
10. Commit and push coherent units. If more useful work fits in the current run, choose the next
    highest-information unit and continue.

Use available subagents, parallel agents, delegated searches/reviews, or similar agentic tools
when you judge that they materially improve speed, independence, coverage, or adversarial checking.
This is permission, not a prescribed workflow: decide for yourself whether to use them, how many,
and for what purpose. Do not spawn agents ceremonially, and reconcile their outputs yourself
before promoting or pushing a result.

## 3. Research posture

Be adversarial toward EIG and toward this programme.

- Do not optimize for validating EIG, the current North Star, or earlier model output.
- Do not import a desired answer into the definition of the doctrine or extractor.
- Always audit what structure was explicitly supplied in the input versus what was genuinely
  recovered in the output.
- Prefer the weakest input that still forces the claimed output.
- Search for the smallest counterexample before investing in a broad positive theorem.
- When a positive theorem appears, look for the matching no-go ceiling: state exactly which
  weaker hypotheses allow failure or which solution-space obstruction prevents a stronger claim.
- Existing mature mathematics is infrastructure, not competition. Reuse it when appropriate.
  EIG earns content only when it solves an upstream, cross-framework, quotient/descent, or
  obstruction problem not already packed into that infrastructure.
- A negative literature verdict is not a novelty proof. Record search scope and uncertainty.

For every important claim, distinguish at least the following statuses when applicable:

`PROVED`, `COMPUTATIONALLY VERIFIED`, `CONDITIONAL`, `CONJECTURE`, `OPEN`, `DISPROVED`,
`PRIOR ART / REDISCOVERY`, `LITERATURE STATUS UNCERTAIN`.

Model agreement is not certification. Preserve explicit proofs, finite certificates, executable
checks, or source-level literature evidence as appropriate.

## 4. What the branch is trying to learn

The programme begins downstream of the canonical fixed-doctrine Core

```math
\operatorname{EIGCore}(D)=\operatorname{Cl}_D(R_D).
```

It asks what nontrivial mathematics is forced once one supplies genuinely small primitive
interaction semantics.

A live candidate architecture is

```math
D
\longrightarrow T_D
\longrightarrow \mathsf{Pat}_D
\longrightarrow \mathsf{Seg}(\mathsf{Pat}_D)
\simeq \operatorname{Alg}(T_D),
```

but this is a hypothesis to pressure-test, not a required conclusion.

The main suspected wall is semantic identification:

```text
free composition
    -> symmetry / cancellation / interchange / observational quotient / coherence
    -> canonical descended geometry, a canonical family, or an obstruction.
```

The question "what survives semantic identification?" is more important than preserving any
particular `Pattern` or `Segal` vocabulary.

## 5. Choosing concrete experiments

The programme contains a ladder of calibrations and stress tests, but the list is **not** a
mandatory sequence.

Possible discriminating contexts include:

- `FinSet -> Set` and the intrinsic singleton calibration;
- monoids from serial composition;
- categories from typed serial composition;
- operads from corollas/substitution;
- properads from multi-input/multi-output wiring;
- commutative monoids as a symmetry quotient;
- groupoids as a cancellation quotient;
- classical PROPs as interchange/symmetry stress tests;
- finitely presented/effective doctrines and contextual minimization;
- a genuinely new doctrine not reverse-engineered from a known answer.

Choose whichever context most efficiently distinguishes live hypotheses. It is acceptable to skip
easy positive controls if prior art already makes them tautological and a quotient stress test is
more informative.

## 6. Mandatory anti-tautology audit

For every proposed extractor or recognition theorem, write down an explicit input/output ledger.
Ask:

1. Which primitive interfaces, operations, plugging rules, equations, symmetries, observations,
   and quotient identifications are supplied?
2. Which shapes, arities, active/inert maps, elementary pieces, covers, laws, or coherences are
   then claimed to be recovered?
3. Could the input be functorially translated into a polynomial monad, monad with chosen arities,
   algebraic pattern, Feynman category, operadic category, or equivalent structure without doing
   the alleged EIG work?
4. If yes, what information has actually been extracted rather than renamed?
5. What happens when the same extractor meets symmetry, cancellation, or nonunique arities?

A theorem whose hypotheses contain its output in disguised form should be downgraded, rewritten,
or rejected.

## 7. Meta-EIG: optional research method, not doctrine

Meta-EIG is permitted as a **weak methodological lens**, not as a conclusion the research must
validate.

Useful version:

```text
candidate research hypothesis
    -> adversarial contexts
    -> observations / failures
    -> identify equivalent or dominated hypotheses
    -> weaken, repair, or close the programme
    -> retain the stable research core.
```

When useful, track competing hypotheses such as:

```text
H1: interaction -> Shape -> Law -> Alg
H2: interaction -> Pattern -> Segal -> Alg
H3: interaction -> FreeGeometry -> semantic reduction -> Pattern/family/obstruction
H4: EIG adds no upstream content beyond an existing framework
```

Judge them by recovery, smuggled input, canonicality, transfer, negative prediction, ad-hoc cost,
and novel prediction.

But do not force this framing. Meta-EIG is **not evidence for EIG**, is not presently a theorem,
and has its own meta-doctrine/regress problem. If ordinary mathematical research practice yields
clearer decisions, use ordinary practice. The only reason to retain Meta-EIG is demonstrated
compression, discrimination, or research-value improvement.

## 8. Repository hygiene

This is a staging research branch, but the repository is public. Keep it legible.

- Keep the number of authoritative research-control files small.
- `research/BEYOND_CORE_PROGRAM.md` is the stable charter.
- `research/STATE.md` is the compact mutable handoff and should be edited in place, not replaced
  by a stream of timestamped status files.
- Put mature foundational mathematics in `theory/` when it has a clear statement/proof boundary.
- Put conventional standalone discoveries in `discoveries/` only when they deserve independent
  presentation.
- Put reproducible verification code/certificates under `verification/` or an appropriate existing
  certificate directory.
- Avoid committing raw model transcripts, sprawling scratch prose, duplicate drafts, or files
  whose only purpose is to say that more work is needed.
- Prefer Git history over accumulating superseded documents.
- Do not casually rewrite `README.md` or `EIG_CORE.md` merely to reflect a speculative branch
  hypothesis. Change public-surface claims only when the mathematics justifies it.

## 9. Git coordination

You are authorized to commit and push research results on `staging/beyond-core`.

- Never push branch work to `main` or another staging branch unless explicitly instructed.
- Do not force-push or rewrite shared history.
- Before each push after substantial work, fetch and integrate remote changes, normally with a
  rebase when safe.
- If another agent has pushed meanwhile, preserve both lines of valid work and resolve conflicts
  semantically, not by choosing "ours" or "theirs" mechanically.
- Use small coherent commits with informative messages such as `research: ...`, `theory: ...`,
  `verify: ...`, or `docs: ...`.
- Run relevant checks before pushing. Existing repository verification should remain green unless
  a deliberate change explains otherwise.

## 10. Session completion criterion

A good session ends with at least one durable change in knowledge, for example:

- a proved theorem or lemma;
- a smallest or structurally decisive counterexample;
- a sharpened obstruction/no-go theorem;
- a precise reduction to known theory that collapses an EIG claim;
- a verified finite experiment that kills or strongly discriminates a hypothesis;
- a source-grounded prior-art boundary;
- a materially improved definition whose additional input cost is explicitly audited;
- a revised North Star forced by evidence rather than preference.

Do not end with a generic research roadmap if the current objective can be reduced further to a
specific theorem, lemma, counterexample, computation, or literature question.
