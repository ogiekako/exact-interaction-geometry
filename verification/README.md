# Verification suite

The verifier suite has two roles:

1. **proof certificate** for explicit finite counterexamples;
2. **finite regression/calibration** for theorem statements whose proof is mathematical rather than exhaustive.

Run everything with

```bash
make verify
```

## `verify_source_pair_augmentation.py`

Exact integer-only exhaustive verification of the Boolean and binary Parnas--Shraibman source-pair counterexamples. It reconstructs optimal bases/source bases, checks the full augmentation rank and every cross pair, and exhausts all binary column sets on `n<=4` rows to certify row-minimality of the five-row binary example.

This is a genuine finite certificate for the displayed examples and the stated finite minimality result.

## `verify_operational_codescent.py`

Finite regression for the operational-codescent dossier:

- 256 two-piece quiver fixtures through bounded path length;
- premature neutralization;
- unsealed macro interleaving;
- empty-separator factor projections not future-complete.

The free-category adjunction theorem is proved mathematically; bounded path enumeration is not its proof.

## `verify_no_choice.py`

Checks the `S_4` action on the three nontrivial `2 x 2` charts of a four-state null process, no-collapse calibration, and finite Cartesian-refinement closure fixtures.

## `verify_phase_v_vii_finite_core.py`

Checks:

- CRT bijectivity iff finite equivalence relations permute, for all partition pairs up to size five;
- difunctionality/rectangle-component calibration on all `3 x 3` relations;
- representative-independent residual products and root reconstruction on every Boolean three-bit tensor.

## Optimizer safety

CI executes maintained verifiers in normal and `python -O` modes and compiles them with `py_compile`. Evidence must not disappear when Python strips language-level `assert` statements.
