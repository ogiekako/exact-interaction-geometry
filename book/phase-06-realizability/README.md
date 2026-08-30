# Phase VI — realizability and reconstruction

**Current status: generic raw shell CLOSED / KNOWN; strong reduced/noncopying form OPEN / REDUCED.**

Phase VI asks which abstract interaction systems are actual execution systems and how to reconstruct them.

## 1. From execution categories to profunctors

Let

```text
p : E -> B
```

record the exposed boundary behaviour of an execution category. For `b in B`, let `E_b` be the fibre. For a boundary arrow `f:b->c`, define

```text
M_f(x,y)={u:x->y in E | p(u)=f}.
```

Composition in `E` induces comparison maps

```text
M_g odot M_f -> M_(gf),
```

so the fibres form a normal-lax `Prof`-valued functor, up to the standard variance convention.

## 2. Generic reconstruction theorem

### Theorem VI.1 — generalized Grothendieck shell
**KNOWN / PRIOR ART.**

Categories over `B` correspond to normal-lax functors

```text
B -> Prof,
```

and the generalized Bénabou--Grothendieck construction reconstructs the category over `B` from the lax interaction data.

This closes the generic questions “what is the raw dynamic interaction object?”, “which abstract such objects are realizable?”, and “can the execution category be reconstructed?” once the intended datum is allowed to be the full normal-lax profunctor.

## 3. Exact middle factorization

### Theorem VI.2 — pseudo / Conduche sector
**KNOWN / PRIOR ART.**

When the lax comparison maps are invertible, the corresponding functor is in the Conduche/exponentiable exact-factorization sector.

The correct operational reading is not strict uniqueness of a lifted middle state. Factorizations are unique only up to the equivalence encoded by coend/fibre zigzags.

## 4. Why this does not finish the project

The generic construction is too permissive for the Grand Book. A witness in a profunctor can carry complete global state and thereby make reconstruction tautological.

The strong Phase-VI target is therefore:

```text
actual Phase-IV exact interfaces
      |
      v
reduced + noncopying + cofinal + feedback-stable interaction stack
      |
      v
exact reconstruction of the same process world.
```

The GPSH theorem shows that noncopying reduced interaction can exist in a substantial sector. The radix-antichain no-go shows that it cannot be demanded uniformly over every invented coordinate recoding.

Hence “reduced” must be tied to an intrinsic/protected process doctrine rather than to arbitrary presentation syntax.

## 5. Strong theorem still open

### Target VI.3 — **OPEN / REDUCED**
Construct from the actual Phase-IV process theory an interaction stack that is simultaneously lossless for raw execution, noncopying, generated/cofinal in an intrinsic class of interfaces, stable under required feedback/composition, equivariant under admitted recodings, and strong enough to feed the Phase-VII arity theorem.

The cleanest route is likely to prove VI.3 and the strong Phase-VII theorem together: the reduced interfaces should be shown directly to form a dense arity system for the explicit raw dynamic world.

## 6. Boundaries

- A whole-state apex proves realizability but is structurally vacuous.
- An arbitrary finite/cofinal atlas over all recodings is false.
- Observer-minimal quotients cannot replace a dense lossless probe system without losing exact reconstruction.
- `Prof` is the generic shell, not by itself the project-specific compression theorem.

## 7. Source / prior-art boundary

Project-side audit:

- `docs/AUDIT_PHASE_V_VI_VII_TERMINAL_CLOSURE_20260830.md`

External shell: generalized Bénabou--Street/Grothendieck construction for lax `Prof`, and the Conduche/exponentiable correspondence. No novelty is claimed for that categorical machinery.
