#!/usr/bin/env python3
"""Finite calibrations for NO-CHOICE, NO-COLLAPSE, and Cartesian refinement."""
from itertools import combinations, permutations, product

checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)


X = tuple(range(4))


def canon_partition(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


parts22 = set()
for pair in combinations(X, 2):
    a = set(pair)
    parts22.add(canon_partition([a, set(X) - a]))
parts22 = sorted(parts22)
require(len(parts22) == 3, "expected three 2+2 partitions")

charts = {tuple(sorted((p, q))) for p, q in combinations(parts22, 2)}
require(len(charts) == 3, "expected three 2x2 charts")


def permute_partition(partition, sigma):
    return canon_partition([{sigma[i] for i in block} for block in partition])


def permute_chart(chart, sigma):
    return tuple(sorted((permute_partition(chart[0], sigma), permute_partition(chart[1], sigma))))


perms = [{i: tup[i] for i in X} for tup in permutations(X)]
require(len(perms) == 24, "S4 size")
for chart in charts:
    require({permute_chart(chart, s) for s in perms} == charts, "chart orbit not transitive")
    require(any(permute_chart(chart, s) != chart for s in perms), "unexpected globally fixed chart")

raw = {0, 1}
observer = {0: 0, 1: 0}
require(len(raw) == 2, "raw fixture")
require(len({observer[x] for x in raw}) == 1, "observer quotient fixture")


def set_partitions(items):
    if not items:
        yield []
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        yield [{first}] + [set(b) for b in rest]
        for i in range(len(rest)):
            new = [set(b) for b in rest]
            new[i].add(first)
            yield new


def canon_set_partition(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))


all_parts = {}
for p in set_partitions([0, 1, 2]):
    all_parts[canon_set_partition(p)] = [set(b) for b in p]
all_parts = list(all_parts.values())
require(len(all_parts) == 5, "Bell(3)=5")
cube = list(product((0, 1), repeat=3))


def projection(rel, block):
    idx = sorted(block)
    return {tuple(row[i] for i in idx) for row in rel}


def factors(rel, partition):
    if not rel:
        return True
    pieces = [projection(rel, b) for b in partition]
    generated = set()
    for vals in product(*[list(s) for s in pieces]):
        row = [None] * 3
        for block, value in zip(partition, vals):
            for i, v in zip(sorted(block), value):
                row[i] = v
        generated.add(tuple(row))
    return generated == set(rel)


def refinement(p, q):
    return [a & b for a in p for b in q if a & b]


for mask in range(1 << len(cube)):
    rel = [cube[i] for i in range(len(cube)) if mask >> i & 1]
    fps = [p for p in all_parts if factors(rel, p)]
    for p, q in combinations(fps, 2):
        require(factors(rel, refinement(p, q)), "factor partitions not closed under common refinement")

print(f"PASS no-choice calibrations checks={checks} charts={len(charts)} relations={1<<len(cube)}")
