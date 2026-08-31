# Source map

This public repository is a curated extraction from the chronological research ledger:

```text
repository: ogiekako/test
subtree: experiments/repairable-tropical-north-star
```

## Public-foundation cutoff

The canonical audited EIG material used for this public snapshot is taken through the local-main checkpoint

```text
c03a402a6dc8cb3de582ea8ddcd932294a2bfba5
```

on 2026-08-31 JST.

The research ledger subsequently advanced to at least

```text
bf75064bf16aa860e76c910555a2c2a268872977
```

with additional **audit-pending** foundational work. Newer does not mean promoted: that tail is intentionally not imported into the public core until its audit status warrants it.

## Source documents

### Finite exact interaction calculus

```text
docs/EIG_FINITE_RESPONSE_AND_FACTOR_RANK_CALCULUS_20260830.md
```

Source status: `PROVED AFTER MAIN AUDIT` with scope/type repairs. Public extraction: [`../theory/01-finite-exact-interactions.md`](../theory/01-finite-exact-interactions.md).

### Interaction-first objecthood foundation

```text
docs/EIG_INTERACTION_FIRST_OBJECTHOOD_RECONSTRUCTION_20260831.md
```

Source status: finite/classical core main-audited; general WEIR conjectural. Public extraction: [`../FOUNDATIONS.md`](../FOUNDATIONS.md) and [`../theory/03-weir.md`](../theory/03-weir.md).

### Category reconstruction theorem

```text
docs/EIG_CATEGORY_OBJECTHOOD_FROM_UNTYPED_INTERACTION_20260831.md
verification/verify_eig_category_objecthood_from_interaction_20260831.py
```

Source status: `MAIN-AUDITED REPAIRED-PROVED / CATEGORY-CONSOLIDATION RECOGNITION THEOREM`. Public extraction: [`../theory/02-category-reconstruction.md`](../theory/02-category-reconstruction.md) and [`../verification/verify_category_reconstruction.py`](../verification/verify_category_reconstruction.py).

### Architecture / editorial boundary

```text
docs/EIG_TEXTBOOK_MASTER_V0_7_20260831.md
```

Used only to preserve the current reconstruction architecture and high-level open gates. The 80-chapter research textbook is not copied into the public foundation.

### Independent intake audit

```text
docs/AUDIT_INCOMING_PHASE_VIII_IX_EIG_MAIN_20260831.md
```

Used to distinguish proved, repaired, refuted, and open claims. Audit-pending or refuted material is not promoted here.

## External discovery candidates

The source-pair augmentation dossier is intentionally outside the audited-foundation cutoff because its role is different: it is a small external mathematical prediction/counterexample harvest whose correctness can be checked without accepting EIG.

Original external target:

```text
M. Parnas and A. Shraibman,
The Augmentation Property of Binary Matrices for the Binary and Boolean Rank,
Linear Algebra and its Applications 556 (2018), 70--99,
Section 6.
DOI: 10.1016/j.laa.2018.07.001
```

Immutable ledger sequence:

```text
3806b8ea4851f6edfa7073085e929bdd868442b9
  initial four-row Boolean counterexample
  docs/AUGMENTATION_SOURCE_PAIR_COUNTEREXAMPLE_20260830.md

b2601fdb843fab9c245967e1695e28419034369b
  Boolean + binary finite source-pair counterexamples
  docs/AUGMENTATION_SOURCE_PAIR_COUNTEREXAMPLES_BOTH_RANKS_20260830.md
  verification/verify_augmentation_source_pair_both_ranks_20260830.py

f5ec36c41b5d20ef3cd064097c4ec798381d433b
  source-incidence duality + unbounded Boolean family
  docs/UNBOUNDED_BOOLEAN_SOURCE_PAIR_AUGMENTATION_20260830.md
  verification/verify_unbounded_boolean_source_pair_augmentation_20260830.py
```

Public extraction: [`../discoveries/source-pair-augmentation.md`](../discoveries/source-pair-augmentation.md), [`../verification/verify_source_pair_counterexamples.py`](../verification/verify_source_pair_counterexamples.py), and [`../verification/verify_unbounded_boolean_augmentation.py`](../verification/verify_unbounded_boolean_augmentation.py).

Status: exact checked-in programs pass; **independent recheck and historical-novelty audit pending before public priority claims**.

## Curation principle

Git history preserves earlier public-curation structures, including the former `Interaction Reconstruction` seven-phase Book and standalone theorem harvests. They were removed from the current tree because they obscure the foundational EIG claim; their deletion is editorial, not historical erasure.

The source-pair dossier is retained despite that general deletion because it is compact, externally falsifiable, mathematically independent of WEIR, and directly illustrates how the interaction/factorization viewpoint generated a testable new prediction rather than only a new vocabulary.
