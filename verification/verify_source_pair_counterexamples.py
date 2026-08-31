#!/usr/bin/env python3
"""Exact finite checks for source-pair augmentation counterexamples."""

from itertools import combinations


def check(cond, message):
    if not cond:
        raise RuntimeError(message)


def bool_span(base):
    out = {0}
    for b in base:
        out |= {x | b for x in tuple(out)}
    return frozenset(out)


def binary_span(base):
    base = tuple(base)
    out = {0}
    for mask in range(1, 1 << len(base)):
        total = 0
        ok = True
        for i, b in enumerate(base):
            if (mask >> i) & 1:
                if total & b:
                    ok = False
                    break
                total |= b
        if ok:
            out.add(total)
    return frozenset(out)


def all_spans(n, spanfn):
    vectors = tuple(range(1, 1 << n))
    spans = {}
    for k in range(n + 1):
        for base in combinations(vectors, k):
            spans[base] = spanfn(base)
    return vectors, spans


def analyze(n, A, U, V, spanfn):
    vectors, spans = all_spans(n, spanfn)

    def minrank(columns):
        target = set(columns)
        for k in range(n + 1):
            for base in combinations(vectors, k):
                if target <= spans[base]:
                    return k, base
        raise RuntimeError("rank search failed")

    rA, _ = minrank(A)
    bases = [b for b in combinations(vectors, rA) if set(A) <= spans[b]]

    def is_source(base):
        return not any(
            other != base and set(base) <= spans[other] for other in bases
        )

    check(U in bases and V in bases, "U or V is not a base")
    check(is_source(U) and is_source(V), "U or V is not a source base")

    rank_union, union_witness = minrank(A + U + V)
    pair_ranks = {}
    for u in U:
        for v in V:
            pair_ranks[(u, v)] = minrank(A + (u, v))[0]

    return (
        rA,
        len(bases),
        sum(is_source(b) for b in bases),
        rank_union,
        union_witness,
        pair_ranks,
    )


examples = [
    ("Boolean", 4, (3, 7, 15), (3, 5, 8), (3, 5, 12), bool_span),
    ("Binary", 5, (10, 31, 27, 18), (4, 9, 10, 18), (9, 10, 18, 21), binary_span),
]

for name, n, A, U, V, spanfn in examples:
    rA, base_count, source_count, rank_union, witness, pair_ranks = analyze(
        n, A, U, V, spanfn
    )
    check(rank_union > rA, f"{name}: union does not raise rank")
    check(
        all(rank == rA for rank in pair_ranks.values()),
        f"{name}: a cross pair raises rank",
    )
    print(
        f"{name}: PASS rows={n} rank(A)={rA} bases={base_count} "
        f"sources={source_count} rank(A|U|V)={rank_union}"
    )
    print(f"  A={A} U={U} V={V}")
    print(f"  union witness rank-{rank_union} base={witness}")

print("PASS source-pair counterexamples")
