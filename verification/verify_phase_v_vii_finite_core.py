#!/usr/bin/env python3
"""Finite exact calibrations for interaction CRT, difunctionality, and residual arities."""
from itertools import combinations, product


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def partitions(n):
    out = []
    def rec(i, blocks):
        if i == n:
            out.append(tuple(frozenset(b) for b in blocks))
            return
        for j in range(len(blocks)):
            blocks[j].append(i); rec(i + 1, blocks); blocks[j].pop()
        blocks.append([i]); rec(i + 1, blocks); blocks.pop()
    rec(0, [])
    uniq = {tuple(sorted(tuple(sorted(b)) for b in p)) for p in out}
    return [tuple(frozenset(b) for b in p) for p in uniq]


def rel_of_partition(p):
    return {(x, y) for block in p for x in block for y in block}


def compose(r, s):
    return {(x, z) for x, y in r for y2, z in s if y == y2}


def join_rel(r, s, n):
    t = set(r) | set(s) | {(i, i) for i in range(n)}
    while True:
        add = {(x, z) for x, y in t for y2, z in t if y == y2}
        if add <= t:
            return t
        t |= add


def crt_bijective(p, q, n):
    r, s = rel_of_partition(p), rel_of_partition(q)
    meet = [a & b for a in p for b in q if a & b]
    j = join_rel(r, s, n)
    seen, join_blocks = set(), []
    for x in range(n):
        if x in seen:
            continue
        block = {y for y in range(n) if (x, y) in j}
        seen |= block; join_blocks.append(frozenset(block))
    def idx(blocks, x): return next(i for i, b in enumerate(blocks) if x in b)
    image = {(idx(p, x), idx(q, x)) for x in range(n)}
    pull = set()
    for i, a in enumerate(p):
        for k, b in enumerate(q):
            if idx(join_blocks, next(iter(a))) == idx(join_blocks, next(iter(b))):
                pull.add((i, k))
    return len(image) == len(meet) and image == pull


def difunctional(r):
    for x, y in r:
        for x2, y2 in r:
            if y2 != y:
                continue
            for x3, y3 in r:
                if x3 == x2 and (x, y3) not in r:
                    return False
    return True


def residual(f, domains, a_set, assignment):
    comp = [i for i in range(len(domains)) if i not in a_set]
    values = []
    for b in product(*[domains[i] for i in comp]):
        x = [None] * len(domains)
        for i, v in zip(sorted(a_set), assignment): x[i] = v
        for i, v in zip(comp, b): x[i] = v
        values.append(f[tuple(x)])
    return tuple(values)


def residual_classes(f, domains, a_set):
    assignments = list(product(*[domains[i] for i in sorted(a_set)])) if a_set else [()]
    rows = {a: residual(f, domains, a_set, a) for a in assignments}
    classes = {}
    for a, row in rows.items(): classes.setdefault(row, []).append(a)
    return rows, classes


def verify_tensor(f, domains):
    n = len(domains)
    rc = {}
    for r in range(n + 1):
        for comb in combinations(range(n), r):
            a = frozenset(comb); rc[a] = residual_classes(f, domains, a)
    for a in rc:
        for b in rc:
            if a & b:
                continue
            rows_a, cls_a = rc[a]; rows_b, cls_b = rc[b]; rows_u, _ = rc[a | b]
            for class_a in cls_a.values():
                for class_b in cls_b.values():
                    targets = set()
                    for x in class_a:
                        for y in class_b:
                            merged = {i: v for i, v in zip(sorted(a), x)}
                            merged.update({i: v for i, v in zip(sorted(b), y)})
                            tup = tuple(merged[i] for i in sorted(a | b))
                            targets.add(rows_u[tup])
                    require(len(targets) == 1, "residual product depends on representative")
    root = frozenset(range(n))
    for x in product(*domains):
        require(residual(f, domains, root, x) == (f[x],), "root reconstruction failed")


def main():
    crt = 0
    for n in range(1, 6):
        ps = partitions(n)
        for p in ps:
            r = rel_of_partition(p)
            for q in ps:
                s = rel_of_partition(q)
                require(crt_bijective(p, q, n) == (compose(r, s) == compose(s, r)), "CRT/permutability mismatch")
                crt += 1

    dif = 0
    edges = [(x, y) for x in range(3) for y in range(3)]
    for mask in range(1 << len(edges)):
        rel = {e for i, e in enumerate(edges) if mask >> i & 1}
        seen_left = set(); rectangular = True
        for x0 in range(3):
            if x0 in seen_left or not any(x == x0 for x, _ in rel):
                continue
            left, right = {x0}, set()
            changed = True
            while changed:
                changed = False
                nr = {y for x, y in rel if x in left}
                nl = {x for x, y in rel if y in right | nr}
                if not nr <= right: right |= nr; changed = True
                if not nl <= left: left |= nl; changed = True
            seen_left |= left
            if any((x, y) not in rel for x in left for y in right): rectangular = False
        require(difunctional(rel) == rectangular, "difunctionality/component mismatch")
        dif += 1

    domains = [(0, 1)] * 3
    points = list(product(*domains))
    tensors = 0
    for mask in range(1 << len(points)):
        f = {x: int((mask >> i) & 1) for i, x in enumerate(points)}
        verify_tensor(f, domains); tensors += 1

    print(f"PASS phase-V/VII finite core crt_pairs={crt} relations_3x3={dif} boolean_tensors={tensors}")


if __name__ == "__main__":
    main()
