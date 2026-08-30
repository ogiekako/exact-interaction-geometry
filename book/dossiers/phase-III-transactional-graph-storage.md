# Dossier III — transactional graph-storage as an intrinsic relative object

**Status:** `AUDITED / ACCEPTED` in the declared relative Book scope.

## Domain

Finite exposed transactional graph-valence processes with:

- a finite graph-product storage monoid `M_Gamma`;
- chosen generator words for atomic transactions;
- complete residual storage configurations at ports;
- occurrence/provenance data;
- optional storage-blind affine payload/action decoration;
- observers retained after raw execution;
- localization only by the justified process-bijective recodings.

## Core theorem

Raw execution composes exactly under sequential gluing, shared-port interleaving, finite union, and finite-control feedback **before** taking the neutral/public section.

For the right-invertible configuration cone

```text
C_Gamma = { c in M_Gamma : exists r, c r = 1 },
```

a neutral run is obtained by imposing source and target `1` only after the raw composite has been formed.

## Load-bearing counterexample

In the bicyclic monoid `B=<p,q | pq=1>`:

```text
1 --p--> p --q--> 1.
```

Neither one-edge component is neutral by itself, but their raw composite is. Therefore neutralization/public projection before composition is unsound.

## Relative Book result

Within the declared graph-storage scope, the exposed object supports exact raw-port composition, recursive graph-monoid tame-storage decomposition, finite intrinsic storage-capacity obstructions, proof-bearing finite-action/degree-one affine charts, and exact opaque hard storage/action atoms.

## Boundary

This is not a semantic equality classification of arbitrary Presburger presentations, not a pointwise HIGH theorem for every obstructed storage graph, and not a minimum-realization algorithm.

## Provenance

`PHASE_III_TRANSACTIONAL_GRAPH_STORAGE_BOOK_TERMINAL_20260830.md` in the original ledger.
