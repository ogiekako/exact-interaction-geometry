#!/usr/bin/env python3
"""Exact regression for the unbounded Boolean source-pair augmentation family."""

from itertools import combinations

CHECKS = 0


def check(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise RuntimeError(message)


def bor(values):
    out = 0
    for value in values:
        out |= value
    return out


def family(r):
    check(r >= 2, "r >= 2")
    A = tuple((1 << (j + 1)) - 1 for j in range(1, r + 1))
    edge = {1: 3}
    if r >= 3:
        edge[2] = 5
        for i in range(3, r):
            edge[i] = (1 << (i - 1)) | (1 << i)
    common = tuple(edge[i] for i in range(1, r))
    s = 1 << r
    t = (1 << (r - 1)) | (1 << r)
    U = common + (s,)
    V = common + (t,)
    X = tuple(edge[i] for i in range(2, r)) + (s, t)
    return A, edge, s, t, U, V, X


def bits(x):
    return {i for i in range(x.bit_length() + 1) if (x >> i) & 1}


def is_tree(edge_masks, vertices):
    vertices = set(vertices)
    adjacency = {v: set() for v in vertices}
    for mask in edge_masks:
        endpoints = bits(mask)
        check(len(endpoints) == 2, f"not edge {mask}")
        a, b = tuple(endpoints)
        check(a in vertices and b in vertices, "edge leaves vertex set")
        adjacency[a].add(b)
        adjacency[b].add(a)
    check(len(edge_masks) == len(vertices) - 1, "edge count")
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        a = stack.pop()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return seen == vertices


def general_checks(r):
    A, edge, s, t, U, V, X = family(r)
    check(len(A) == r and len(U) == r and len(V) == r and len(X) == r, "sizes")
    for j in range(1, r):
        check(
            bor(edge[i] for i in range(1, j + 1)) == A[j - 1],
            f"prefix r={r} j={j}",
        )
    check(bor(U) == A[-1], "U spans final prefix")
    check(bor(V) == A[-1], "V spans final prefix")
    for j in range(1, r + 1):
        check((A[j - 1] >> j) & 1, "fooling diagonal one")
        for k in range(j + 1, r + 1):
            check(((A[j - 1] >> k) & 1) == 0, "fooling cross zero")
    check(is_tree(U[:-1], range(r)), "U tree")
    check(U[-1] == 1 << r, "U singleton")
    check(is_tree(V, range(r + 1)), "V tree")
    check(set(X) - {s} <= set(V), "delete s witnessed by V")
    check(set(X) - {t} <= set(U), "delete t witnessed by U")
    for j in range(2, r):
        B = tuple(edge[i] for i in range(1, j)) + tuple(
            1 << k for k in range(j, r + 1)
        )
        check(len(B) == r, "B size")
        for k in range(1, r + 1):
            if k < j:
                representation = tuple(edge[i] for i in range(1, k + 1))
            else:
                representation = tuple(edge[i] for i in range(1, j)) + tuple(
                    1 << q for q in range(j, k + 1)
                )
            check(
                bor(representation) == A[k - 1],
                f"B spans A r={r} j={j} k={k}",
            )
        for x in X:
            if x == edge[j]:
                continue
            if x == s:
                representation = (1 << r,)
            elif x == t:
                representation = (1 << (r - 1), 1 << r)
            else:
                i = next(i for i in range(2, r) if edge[i] == x)
                if i < j:
                    representation = (edge[i],)
                else:
                    representation = (1 << (i - 1), 1 << i)
            check(
                bor(representation) == x,
                f"B spans X-minus r={r} j={j} x={x}",
            )


def bool_span(base):
    out = {0}
    for b in base:
        out |= {x | b for x in tuple(out)}
    return frozenset(out)


def exhaustive_r3():
    r = 3
    n = 4
    A, _, _, _, U, V, X = family(r)
    vectors = tuple(range(1, 1 << n))
    spans = {}
    for k in range(n + 1):
        for base in combinations(vectors, k):
            spans[base] = bool_span(base)
    for k in range(n + 1):
        bases = [b for b in combinations(vectors, k) if set(A) <= spans[b]]
        if bases:
            break
    check(k == r, "exhaustive rank A")
    sources = [
        b
        for b in bases
        if not any(c != b and set(b) <= spans[c] for c in bases)
    ]
    check(U in sources and V in sources, "exhaustive U,V source")

    def rank(columns):
        target = set(columns)
        for k in range(n + 1):
            for base in combinations(vectors, k):
                if target <= spans[base]:
                    return k
        raise RuntimeError("rank search failed")

    check(rank(A + X) == r + 1, "full X raises by one")
    for x in X:
        check(
            rank(A + tuple(y for y in X if y != x)) == r,
            "proper deletion rank r",
        )


for r in range(2, 31):
    general_checks(r)
exhaustive_r3()
print(
    f"PASS checks={CHECKS}: general formulas r=2..30; "
    "exhaustive r=3 source/minimality audit"
)
