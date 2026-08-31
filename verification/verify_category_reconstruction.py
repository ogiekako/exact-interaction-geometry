#!/usr/bin/env python3
"""Exact finite regression for category recovery from untyped interaction."""

from itertools import product

CHECKS = 0


def check(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise RuntimeError(message)


def make_preorder(n, rel):
    arrows = [(f"a{i}_{j}", i, j) for i, j in sorted(rel)]
    comp = {}
    for a in arrows:
        for b in arrows:
            na, sa, ta = a
            nb, sb, tb = b
            if sa == tb:
                comp[(na, nb)] = f"a{sb}_{ta}"
    ids = {i: f"a{i}_{i}" for i in range(n)}
    return arrows, comp, ids


def all_preorders(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for mask in range(1 << len(pairs)):
        rel = {pairs[k] for k in range(len(pairs)) if (mask >> k) & 1}
        if any((i, i) not in rel for i in range(n)):
            continue
        ok = True
        for i, j, k in product(range(n), repeat=3):
            if (i, j) in rel and (j, k) in rel and (i, k) not in rel:
                ok = False
                break
        if ok:
            yield rel


def verify_category(arrows, comp, ids):
    data = {a[0]: a for a in arrows}
    names = list(data)
    zero = "0"
    elems = [zero] + names

    def mul(x, y):
        if x == zero or y == zero:
            return zero
        return comp.get((x, y), zero)

    def resp(x):
        return x != zero

    for x, y, z in product(elems, repeat=3):
        check(mul(mul(x, y), z) == mul(x, mul(y, z)), "associativity failed")

    profile = {
        u: tuple(resp(mul(mul(x, u), y)) for x, y in product(elems, repeat=2))
        for u in elems
    }
    for a in names:
        for b in names:
            same = profile[a] == profile[b]
            ea = data[a]
            eb = data[b]
            check(same == ((ea[1], ea[2]) == (eb[1], eb[2])), "endpoint recovery failed")
    for a in names:
        check(profile[a] != profile[zero], "zero not separated")

    q = {zero: None}
    for a in names:
        q[a] = (data[a][1], data[a][2])
    qvals = {q[a] for a in names}
    idem = {s for s in qvals if s[0] == s[1]}
    check(idem == {(i, i) for i in ids}, "recovered object idempotents wrong")

    for i, identity in ids.items():
        candidates = []
        for p in names:
            if q[p] != (i, i):
                continue
            good = True
            for x in names:
                px = mul(p, x)
                if px != zero and px != x:
                    good = False
                xp = mul(x, p)
                if xp != zero and xp != x:
                    good = False
            if good:
                candidates.append(p)
        check(candidates == [identity], f"identity recovery failed at {i}: {candidates}")

    for i, j in product(ids, repeat=2):
        fibre = {a for a in names if q[a] == (i, j)}
        hom = {a[0] for a in arrows if a[1] == i and a[2] == j}
        check(fibre == hom, "Hom witness fibre recovery failed")


counts = {}
for n in range(1, 4):
    count = 0
    for rel in all_preorders(n):
        arrows, comp, ids = make_preorder(n, rel)
        verify_category(arrows, comp, ids)
        count += 1
    counts[n] = count
check(counts == {1: 1, 2: 4, 3: 29}, f"unexpected preorder counts: {counts}")

for k in range(1, 8):
    arrows = [("idA", "A", "A"), ("idB", "B", "B")] + [
        (f"f{t}", "A", "B") for t in range(k)
    ]
    comp = {("idA", "idA"): "idA", ("idB", "idB"): "idB"}
    for t in range(k):
        f = f"f{t}"
        comp[("idB", f)] = f
        comp[(f, "idA")] = f
    verify_category(arrows, comp, {"A": "idA", "B": "idB"})

# Explicit non-ULF fixture: h:A->C differs from the only two-step composite g f.
arrows = [
    ("iA", "A", "A"), ("iB", "B", "B"), ("iC", "C", "C"),
    ("f", "A", "B"), ("g", "B", "C"), ("gf", "A", "C"), ("h", "A", "C"),
]
comp = {
    ("iA", "iA"): "iA", ("iB", "iB"): "iB", ("iC", "iC"): "iC",
    ("iB", "f"): "f", ("f", "iA"): "f",
    ("iC", "g"): "g", ("g", "iB"): "g",
    ("iC", "gf"): "gf", ("gf", "iA"): "gf",
    ("iC", "h"): "h", ("h", "iA"): "h",
    ("g", "f"): "gf",
}
verify_category(arrows, comp, {"A": "iA", "B": "iB", "C": "iC"})
check(comp[("g", "f")] != "h", "ULF counterexample collapsed unexpectedly")

print(f"PASS category-reconstruction checks={CHECKS} preorders={counts}")
