#!/usr/bin/env python3
"""Independent verifier for the 4-row Boolean-rank augmentation counterexample."""

from itertools import combinations

A = frozenset({3, 7, 15})
U = frozenset({3, 5, 8})
V = frozenset({3, 5, 12})
ALL = tuple(range(1, 16))


def span(B):
    out = {0}
    for x in B:
        out |= {y | x for y in tuple(out)}
    return out


def boolean_rank(columns):
    columns = set(columns)
    for r in range(5):
        for B in combinations(ALL, r):
            if columns <= span(B):
                return r
    raise AssertionError("unreachable")


def bases_of_A():
    r = boolean_rank(A)
    return [frozenset(B) for B in combinations(ALL, r) if A <= span(B)]


def source(B, bases):
    return all(C == B or not (set(B) <= span(C)) for C in bases)


if boolean_rank(A) != 3:
    raise RuntimeError("rank(A) check failed")

bases = bases_of_A()
if U not in bases or V not in bases:
    raise RuntimeError("U or V is not an optimal base")
if not source(U, bases) or not source(V, bases):
    raise RuntimeError("source check failed")
if boolean_rank(A | U | V) != 4:
    raise RuntimeError("full augmentation rank check failed")
for u in U:
    for v in V:
        if boolean_rank(A | {u, v}) != 3:
            raise RuntimeError(f"cross-pair rank failed for {u},{v}")

sources = [B for B in bases if source(B, bases)]
bad_pairs = []
for i, B in enumerate(sources):
    for C in sources[i + 1 :]:
        if boolean_rank(A | B | C) > 3 and all(
            boolean_rank(A | {b, c}) == 3 for b in B for c in C
        ):
            bad_pairs.append((B, C))

if len(sources) != 13:
    raise RuntimeError(f"expected 13 source bases, got {len(sources)}")
if len(bad_pairs) != 8:
    raise RuntimeError(f"expected 8 bad source-base pairs, got {len(bad_pairs)}")

print("PASS")
print("Boolean rank(A)=3")
print("U and V are source bases")
print("Boolean rank(A|U|V)=4")
print("all 9 one-from-each augmentations have rank 3")
print("source bases of A:", len(sources))
print("bad source-base pairs:", len(bad_pairs))
