# Dossier V — interaction geometry

**Status:** accepted generic/meta boundary; broader external programme remains scope-sensitive.

## Principle

Do not define the interface by first choosing a scalar. The primitive datum is exact compatibility/factorization:

```text
exact interaction kernel/proarrow
    -> factorization/compression atlas
    -> valuation/resource spectrum
    -> scalar shadow if desired.
```

For witness proarrows,

```text
(Psi odot Phi)(a,c) = coproduct_b Phi(a,b) x Psi(b,c).
```

Different valuations produce different decategorified semirings: Boolean existence, cardinality `(+ , x)`, and Presburger dimension `(max,+)` are distinct shadows of the same witness composition.

## Hidden-middle no-go

Every relation factors through its edge set as

```text
R = graph(q) o graph(p)^op.
```

Both legs are functional/converse-functional and hence difunctional. Therefore bare support-difunctionality cannot be a proper relation class containing functions and converses and closed under ordinary composition. Hidden-middle witness structure is load-bearing.

## Exact flat sector

For equivalence relations `alpha,beta`, the canonical CRT map

```text
X/(alpha intersect beta)
 -> X/alpha x_(X/(alpha join beta)) X/beta
```

is bijective iff `alpha beta = beta alpha`.

With observation kernels satisfying

```text
theta_(A union B)=theta_A meet theta_B,
theta_A join theta_B <= theta_(A intersect B),
```

and a monotone modular valuation `d`, `r(A)=D-d(theta_A)` is submodular with exact slack

```text
d(theta_(A intersect B)) - d(theta_A join theta_B).
```

Permutable/Mal'tsev settings provide a clean sufficient common-interface sector.

## Failure sector

Universal exact submodularity is false. The Presburger disjunction

```text
x1=x2 OR x3=x4
```

already violates the natural cut-channel inequality. Thus interaction curvature/defect is meaningful precisely because flatness is not automatic.

## Verification

`verification/verify_phase_v_vii_finite_core.py` exhaustively checks finite partition CRT/permutability and finite residual-nerve coherence fixtures. It is calibration, not the general algebraic proof.

## External consequence

The source-pair augmentation counterexamples were found by treating optimal bases as a factorization atlas and searching for collective incompatibility that is pairwise invisible.
