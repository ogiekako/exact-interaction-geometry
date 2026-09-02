# Exact Interaction Geometry — conservative physics boundaries

**Snapshot:** 2026-09-02  
**Status:** boundary note; no new foundational theorem is promoted here

This file records a small set of physics-facing consequences and calibrations that are useful for Exact Interaction Geometry (EIG). It is deliberately conservative. It does **not** claim that EIG is a physical theory, that interaction data determine spacetime, or that the items below are historically novel.

The inclusion rule is strict: a statement appears here only when it is either an elementary consequence that can be checked directly, or a faithful use of a cited primary result. Where an EIG-specific theorem still depends on an uncompleted audit, that dependence is stated explicitly rather than hidden.

Two different questions are tracked throughout:

```text
Programme significance:
    Does this materially constrain or clarify the EIG reconstruction programme?

External novelty posture:
    Is a theorem-level novelty claim justified by the present audit?
```

These axes should not be conflated. A result may be central to EIG while being standard mathematics or close prior art. In this file, **no external novelty claim is made unless explicitly stated**; at this snapshot none is needed.

---

## 1. Subsystem structure is not selected by unlocalized finite-dimensional process data alone

### Statement

Let `V` be an `n`-dimensional complex Hilbert space. Suppose the available finite-dimensional quantum semantics is invariant under simultaneous unitary change of basis: states, effects, channels, ancillas and composition are transformed by conjugation in the usual way, and no tensor-product factorization or implementation labels are distinguished.

Then projective unitaries act as automorphisms of that unlocalized semantics. If one asks for a fixed nontrivial factor signature

```text
n = d_1 ... d_r,
```

an embedded tensor-product structure of that signature is moved transitively by `PU(n)`. Its stabilizer is the corresponding local-unitary subgroup (with the evident finite permutations when equal factors are treated as unordered). Hence the space of such embedded factorizations is a homogeneous space

```text
PU(n) / K_d.
```

For every nontrivial factorization this orbit has more than one point. Therefore there is no `PU(n)`-invariant choice of one distinguished embedded factorization from the unlocalized semantics alone.

This is an elementary symmetry obstruction: a natural selector would have to choose a fixed point of the automorphism action, but the action on the nontrivial factorization orbit has no fixed point.

### What this does and does not say

It says only that **unlocalized semantics does not canonically select an embedded tensor-product locality**. It does not say that subsystem structure is meaningless or unrecoverable after additional operational structure is supplied.

Indeed, observable/control algebras are well-known to induce subsystem structures. Zanardi, Lidar and Lloyd explicitly develop the idea that operationally accessible interactions and measurements can induce a tensor-product structure:

- P. Zanardi, D. A. Lidar, S. Lloyd, *Quantum tensor product structures are observable-induced*, Phys. Rev. Lett. 92, 060402 (2004), arXiv:quant-ph/0308043.

So the EIG lesson is not “there are no subsystems”. It is:

```text
unlocalized process semantics
    -> no canonical embedded TPS;
additional distinguished operational structure
    -> may select an operational TPS.
```

### EIG status

**Programme significance:** CENTRAL. It is a clean example of a residual fibre: many latent localities remain compatible with the same unlocalized semantics.  
**External novelty posture:** NO NOVELTY CLAIM. The symmetry proof is elementary and the observable-relative nature of tensor-product structure has substantial prior art.

---

## 2. If atomic factors are already known, infinitesimal operator influence determines the exact interaction support

This statement starts **after** a tensor-product decomposition has been supplied or reconstructed. It therefore does not solve the previous subsystem-selection problem.

Let

```text
V = V_1 tensor ... tensor V_r
```

be finite-dimensional, and let `H` be a self-adjoint Hamiltonian. For each factor define the normalized partial-trace conditional expectation

```text
E_i(X) = (I_i / d_i) tensor Tr_i(X),
Q_i = 1 - E_i.
```

The commuting projections

```text
P_S = product_{i in S} Q_i product_{j notin S} E_j
```

give the exact orthogonal support decomposition

```text
H = sum_{S subset [r]} H_S,
H_S = P_S H.
```

For distinct sites `i,j`, define the complete first-order operator-valued cross influence

```text
D_ij(A,B) = (1/i) d/dt [ exp(itH) A exp(-itH), B ] |_{t=0}
            = [[H,A],B],
```

up to the conventional overall sign associated with the Heisenberg convention.

If `F_a` and `G_b` are Hilbert–Schmidt orthonormal bases of **traceless Hermitian operators** on factors `i` and `j`, then the standard matrix-algebra Casimir identity gives

```text
sum_a [F_a,[F_a,X]] = 2 d_i X
```

whenever `X` is traceless in factor `i`, and similarly for `j`. Consequently

```text
K_ij
  = (1 / (4 d_i d_j))
    sum_{a,b} [F_a,[G_b,D_ij(F_a,G_b)]]
  = sum_{S containing {i,j}} H_S.
```

Applying `P_S` therefore recovers every multi-site component `H_S` with `|S| >= 2`:

```text
H_S = P_S K_ij       for any i,j in S, i != j.
```

Thus complete first-order operator-valued cross-influence data determine the exact interaction-support hypergraph

```text
{ S : H_S != 0, |S| >= 2 }.
```

Scalar terms are invisible to commutators, and purely one-site terms are not determined by cross-influence alone. These are genuine scope boundaries, not defects in the calculation.

### EIG status

**Programme significance:** CENTRAL once an atomic factor structure is available. It is a literal instance of

```text
infinitesimal interaction response -> exact interaction support.
```

**External novelty posture:** UNASSESSED / NO CLAIM. Short-time commutators and Hamiltonian-learning ideas have a large prior literature. The identity above is included because it is exact and programmatically clarifying, not because historical novelty has been established.

---

## 3. Intrinsic dynamical coarse geometry is weaker than a unique metric geometry

### What is already prior art

Elokl and Jones define, for a discrete net of algebras and a quantum channel `alpha`, the commutator tail function

```text
Q_alpha(x,y)
  = sup { ||[alpha(a),b]|| : a in (A_x)_1, b in (A_y)_1 }
```

and the associated **dynamical coarse structure** `E_alpha`. They prove the corresponding universal controlled-decay property and discuss stability under quasi-local perturbations. For local Hamiltonian dynamics, Lieb–Robinson bounds imply

```text
E_{alpha_t} subset E_{(X,d)}.
```

Primary source:

- A. Elokl, C. Jones, *Universal coarse geometry of spin systems*, Lett. Math. Phys. 115, 57 (2025), arXiv:2411.07912; see Definition 4.23 and Example 4.24 in the arXiv version.

Therefore EIG must **not** claim the construction of an intrinsic dynamical coarse structure as a new idea.

### Elementary metric boundary

A bounded coarse structure does not, by itself, determine a quasi-isometry class of metrics.

Take `X = Z` and

```text
d(m,n)       = |m-n|,
d_alpha(m,n) = |m-n|^alpha,       0 < alpha < 1.
```

For any subset `E subset X x X`,

```text
sup_E d < infinity    iff    sup_E d_alpha < infinity,
```

because `t -> t^alpha` is increasing and unbounded. Hence

```text
E^d = E^{d_alpha}.
```

However the two metric spaces are not quasi-isometric. Both are uniformly discrete and have bounded geometry, while their counting-ball growth functions satisfy

```text
|B_d(0,R)|          ~ R,
|B_{d_alpha}(0,R)|  ~ R^(1/alpha).
```

Polynomial growth degree is preserved under quasi-isometry for uniformly discrete bounded-geometry spaces, so the exponents `1` and `1/alpha` cannot agree when `alpha != 1`.

Thus the implication

```text
canonical coarse structure -> canonical metric up to quasi-isometry
```

is false without additional hypotheses restricting the admissible metrics.

This is precisely the kind of boundary EIG should keep explicit:

```text
dynamics may determine an intrinsic coarse invariant
but that invariant need not select a unique radial/metric calibration.
```

A positive metric-reconstruction theorem therefore requires extra assumptions, for example a declared large-scale geodesic normalization together with a condition tying the admissible metric coarse structure tightly to the dynamical one. Those additional assumptions are part of the input of such a theorem; they are not consequences of coarse structure alone.

### EIG status

**Programme significance:** CENTRAL. It separates an identifiable invariant from a larger residual metric fibre.  
**External novelty posture:** NO NOVELTY CLAIM for the coarse-geometry construction or for the elementary snowflake observation. Any stronger literature-correction claim requires a separate source-level audit and is intentionally omitted here.

---

## 4. Local QFT measurement theory gives a precise place to ask an EIG-style operational-kernel question

Fewster and Verch formulate local QFT measurement schemes by coupling a system QFT to a probe QFT in a bounded spacetime region. The coupling induces a scattering map and hence induced system observables from probe observables. Their concrete worked example uses two linear scalar fields with a compact quadratic coupling.

- C. J. Fewster, R. Verch, *Quantum Fields and Local Measurements*, Commun. Math. Phys. 378 (2020) 851–889, arXiv:1810.06512.

For the real linear scalar field, Fewster–Jubb–Ruep subsequently construct asymptotic compact-coupling measurement schemes for every local observable:

- C. J. Fewster, I. Jubb, M. H. Ruep, *Asymptotic Measurement Schemes for Every Observable of a Quantum Field Theory*, Ann. Henri Poincaré 24 (2023) 1137–1184, arXiv:2203.09529.

Mandrysch and Navascués further analyze field measurements in the FV framework, including locally smeared linear scalar fields:

- J. Mandrysch, M. Navascués, *Quantum Field Measurements in the Fewster–Verch Framework*, arXiv:2411.13605 (published in Lett. Math. Phys.).

These results justify treating **physical realizability of response functionals** as a separate question from algebraic availability of observables. They do not by themselves prove a completeness theorem for perturbatively interacting `phi^4`.

### A safe formal lifting lemma

There is nevertheless a simple formal fact that is independent of the unresolved physical-realizability step.

Let `C[[hbar]]` and `R[[hbar]]` be separated, complete, topologically free `C[[hbar]]`-modules. Suppose

```text
d_hat = d_0 + O(hbar),
rho    = rho_0 + O(hbar),
```

and suppose every `d_hat`-exact element is response-null:

```text
rho(d_hat B) = 0.
```

Assume also the classical kernel theorem

```text
ker rho_0 = im d_0
```

on the quotient under consideration (for example after separately quotienting compact total derivatives and declared field-independent terms).

Then

```text
ker rho = im d_hat.
```

**Proof.** Let `A in ker rho`. At order `hbar^0`, `rho_0(A_0)=0`, so `A_0=d_0 B_0`. Subtract the full quantum exact element `d_hat B_0`. The remainder is still response-null and begins at order `hbar`. Divide only conceptually by its first `hbar` valuation, apply the same classical kernel statement to the first nonzero coefficient, and subtract `hbar^N d_hat B_N`. Iterating produces a convergent formal sum `B=sum_N hbar^N B_N` in the `hbar`-adic topology with `A=d_hat B`. QED.

Fredenhagen and Rejzner construct the renormalized BV complex in perturbative AQFT and identify the finite operator replacing the ill-defined BV Laplacian with the anomaly term of the anomalous Master Ward Identity:

- K. Fredenhagen, K. Rejzner, *Batalin–Vilkovisky formalism in perturbative algebraic quantum field theory*, Commun. Math. Phys. 317 (2013) 697–725, arXiv:1110.5232.

Accordingly, in a nongauge scalar theory, **if** one has already proved the classical operational detector theorem and **if** the full probe/renormalization prescription is transported so that renormalized KT-exact changes are operationally null, then no additional mysterious higher-loop kernel can first appear at order `hbar^N`: the coefficient-by-coefficient argument above lifts the classical kernel theorem to the formal quantum complex.

This conclusion is formal. It is not a theorem about convergent numerical probabilities at fixed physical coupling, and it does not prove that a physically preparable family of interacting states separates the relevant response algebra.

### What is deliberately not promoted here

Current internal work suggests a stronger restricted-probe statement for interacting scalar `phi^4`, using a free Klein–Gordon probe and compact bilinear couplings. That result requires a focused independent audit of the mixed retarded-product formula, support/time-slice construction, protocol transport, and probability/state-preparation interpretation. It is therefore **not** recorded here as an established physical theorem.

### EIG status

**Programme significance:** CENTRAL as a model for the distinction

```text
algebraic response completeness
vs.
physically realizable measurement/preparation completeness.
```

**External novelty posture:** NO NOVELTY CLAIM for the FV framework, the linear-scalar measurement results, the renormalized BV machinery, or the `hbar`-adic induction mechanism. Any novelty claim for their exact combination with an interacting restricted-probe completeness theorem must wait for an independent theorem-level and literature audit.

---

## 5. What this note supports

The four examples above support only the following modest conclusion.

In physical reconstruction problems, an EIG-style analysis can usefully distinguish three layers:

```text
(1) supplied operational doctrine,
(2) maximal structure actually identifiable from its responses,
(3) residual structure that requires additional physical input.
```

The resulting output can be a positive reconstruction theorem, an exact support/invariant, or a no-go/moduli statement. None of those outcomes licenses the stronger slogan that “interaction alone determines physical reality”.

At this snapshot the safest physics-facing research posture is therefore:

```text
use physical examples as boundary tests of the EIG discipline;
keep standard prior art explicitly attributed;
separate algebraic identifiability from physical realizability;
do not promote candidate novelty until it survives a dedicated specialist audit.
```

That posture is intentionally narrower than the larger private research programme.
