#!/usr/bin/env python3
"""Exact source-pair counterexamples for Boolean and binary rank.

The displayed examples and binary row-minimality statement are finite theorems:
all searches below are exhaustive and integer-only.
"""
from itertools import combinations


def require(condition, message):
    if not condition:
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
        value = 0
        ok = True
        for i, b in enumerate(base):
            if mask >> i & 1:
                if value & b:
                    ok = False
                    break
                value |= b
        if ok:
            out.add(value)
    return frozenset(out)


def all_spans(n, spanfn):
    all_vectors = tuple(range(1, 1 << n))
    spans = {}
    for k in range(n + 1):
        for base in combinations(all_vectors, k):
            spans[base] = spanfn(base)
    return all_vectors, spans


def analyze(n, matrix, source_u, source_v, spanfn):
    all_vectors, spans = all_spans(n, spanfn)

    def minrank(columns):
        target = set(columns)
        for k in range(n + 1):
            for base in combinations(all_vectors, k):
                if target <= spans[base]:
                    return k, base
        raise RuntimeError("rank search failed")

    rank_a, witness_a = minrank(matrix)
    bases = [b for b in combinations(all_vectors, rank_a) if set(matrix) <= spans[b]]

    def source(base):
        return not any(other != base and set(base) <= spans[other] for other in bases)

    require(source_u in bases and source_v in bases, "U or V is not an optimal base")
    require(source(source_u) and source(source_v), "U or V is not a source base")

    rank_all, witness_all = minrank(matrix + source_u + source_v)
    pairs = {}
    for u in source_u:
        for v in source_v:
            pairs[(u, v)] = minrank(matrix + (u, v))

    return rank_a, witness_a, len(bases), sum(source(b) for b in bases), rank_all, witness_all, pairs


BOOLEAN = (4, (3, 7, 15), (3, 5, 8), (3, 5, 12))
BINARY = (5, (10, 31, 27, 18), (4, 9, 10, 18), (9, 10, 18, 21))

for name, example, spanfn in [("Boolean", BOOLEAN, bool_span), ("Binary", BINARY, binary_span)]:
    n, matrix, u, v = example
    rank_a, witness_a, nbases, nsources, rank_all, witness_all, pairs = analyze(n, matrix, u, v, spanfn)
    require(rank_all > rank_a, f"{name}: full source union does not raise rank")
    require(all(rank == rank_a for rank, _ in pairs.values()), f"{name}: a cross pair raises rank")
    print(f"{name}: PASS rows={n} rank(A)={rank_a} bases={nbases} sources={nsources} rank(A|U|V)={rank_all}")
    print(f"  A={matrix} U={u} V={v}")
    print(f"  full-union witness={witness_all}")


def has_counterexample(n, spanfn):
    all_vectors, spans = all_spans(n, spanfn)

    def bases_for(target):
        target = set(target)
        for k in range(n + 1):
            bases = [b for b in combinations(all_vectors, k) if target <= spans[b]]
            if bases:
                return k, bases
        raise RuntimeError("no base")

    for mask in range(1, 1 << len(all_vectors)):
        target = tuple(all_vectors[i] for i in range(len(all_vectors)) if mask >> i & 1)
        rank, bases = bases_for(target)
        if rank < 2:
            continue
        sources = [b for b in bases if not any(other != b and set(b) <= spans[other] for other in bases)]
        for i, u in enumerate(sources):
            for v in sources[i + 1:]:
                if any(set(u + v) <= spans[b] for b in bases):
                    continue
                if all(any({x, y} <= spans[b] for b in bases) for x in u for y in v):
                    return target, u, v
    return None


for n in range(1, 5):
    hit = has_counterexample(n, binary_span)
    require(hit is None, f"Binary: smaller-row counterexample at n={n}: {hit}")
print("Binary minimal-row check: PASS no counterexample for n<=4")
print("PASS all exact source-pair checks")
