# Public release checklist

The repository is currently curated as if it may become public. Before changing repository visibility or citing it in a paper, run this checklist.

## Mathematical state

- [ ] `STATUS.md` matches the latest inspected `ogiekako/test` canonical state.
- [ ] `provenance/SOURCE_MAP.md` records the exact latest inspected source commit.
- [ ] Every headline theorem has a dossier or an explicit reason it is only background.
- [ ] No `AUDIT PENDING` claim is described as canonical closure elsewhere in the repository.
- [ ] Prior-art scaffold is separated from programme-specific claims.

## Verification

- [ ] `make verify` passes locally.
- [ ] latest `verify` GitHub Actions run is green.
- [ ] source-pair counterexample verifier passes in normal and `python -O` modes.
- [ ] no evidentiary verifier relies on bare Python `assert`.
- [ ] generated caches / auxiliary files are not committed.

## Standalone source-pair paper

- [ ] `make paper` successfully compiles `papers/source-pair-augmentation/paper.tex` with `pdflatex`.
- [ ] re-read the exact Section-6 wording/definitions in Parnas--Shraibman against the final note.
- [ ] refresh the post-2018 literature search immediately before posting.
- [ ] check citing papers / author publication lists / current survey for any prior resolution.
- [ ] freeze and cite the exact repository commit containing the verifier.
- [ ] decide whether to contact the original authors before or concurrently with posting.
- [ ] keep the Interaction Reconstruction discussion as discovery provenance, not proof dependency.

## Repository presentation

- [ ] root README links all canonical entry points and contains no stale phase status.
- [ ] `RESEARCH_FRONTIER.md` distinguishes mathematical frontiers from governance-only promotion gates.
- [ ] `PUBLICATION_MAP.md` separates standalone results from programme-level synthesis.
- [ ] `bibliography/README.md` includes the closest known scaffold and explicit novelty warnings.
- [ ] `CITATION.cff` metadata is correct.
- [ ] repository description/topics are set appropriately in GitHub UI if desired.
- [ ] decide on a license before public reuse is invited; do not assume one silently.

## Privacy / provenance

- [ ] scan for credentials, tokens, private URLs, or unintended personal information.
- [ ] confirm every linked source-ledger path is intended to be public or can safely remain an inaccessible provenance reference.
- [ ] do not publish scratch-agent logs merely to make the history complete; the public repository is the curated mathematical spine.

## Release principle

A public snapshot should satisfy two independent properties:

```text
programme claims are honestly scoped and auditable;
standalone finite results are verifiable without trusting the programme.
```
