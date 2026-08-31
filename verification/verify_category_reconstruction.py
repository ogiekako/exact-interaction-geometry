#!/usr/bin/env python3
"""End-to-end finite regression for category recovery from untyped interaction.

The reconstruction phase uses only the untyped multiplication table, zero, and
one-bit success response. Original source/target labels and the expected object
count are consulted only in the final comparison step.
"""
from itertools import product

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(message)


def make_preorder(n, relation):
    arrows = [(f"a{i}_{j}", i, j) for i, j in sorted(relation)]
    comp = {}
    for left in arrows:
        for right in arrows:
            nl, sl, tl = left
            nr, sr, tr = right
            if sl == tr:
                comp[(nl, nr)] = f"a{sr}_{tl}"
    ids = {i: f"a{i}_{i}" for i in range(n)}
    return arrows, comp, ids


def all_preorders(n):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for mask in range(1 << len(pairs)):
        relation = {pairs[k] for k in range(len(pairs)) if (mask >> k) & 1}
        if any((i, i) not in relation for i in range(n)):
            continue
        if all(
            not ((i, j) in relation and (j, k) in relation) or (i, k) in relation
            for i, j, k in product(range(n), repeat=3)
        ):
            yield relation


def verify_category(arrows, comp, ids):
    original = {name: (source, target) for name, source, target in arrows}
    names = tuple(original)
    zero = "0"
    elems = (zero,) + names

    def mul(x, y):
        if x == zero or y == zero:
            return zero
        return comp.get((x, y), zero)

    def response(x):
        return x != zero

    for x, y, z in product(elems, repeat=3):
        check(mul(mul(x, y), z) == mul(x, mul(y, z)), "associativity failed")

    profile = {
        u: tuple(response(mul(mul(x, u), y)) for x, y in product(elems, repeat=2))
        for u in elems
    }
    classes_by_profile = {}
    for u in elems:
        classes_by_profile.setdefault(profile[u], set()).add(u)
    classes = tuple(frozenset(v) for v in classes_by_profile.values())
    q = {u: cls for cls in classes for u in cls}
    zero_class = q[zero]
    check(zero_class == frozenset((zero,)), "zero contextual class not singleton")

    qmul = {}
    for left_class, right_class in product(classes, repeat=2):
        images = {q[mul(x, y)] for x in left_class for y in right_class}
        check(len(images) == 1, "contextual quotient multiplication not well-defined")
        qmul[(left_class, right_class)] = next(iter(images))

    nonzero_classes = tuple(cls for cls in classes if cls != zero_class)
    object_classes = tuple(cls for cls in nonzero_classes if qmul[(cls, cls)] == cls)

    recovered_endpoints = {}
    for cls in nonzero_classes:
        left_units = [e for e in object_classes if qmul[(e, cls)] == cls]
        right_units = [e for e in object_classes if qmul[(cls, e)] == cls]
        check(len(left_units) == 1, "target object class not unique")
        check(len(right_units) == 1, "source object class not unique")
        recovered_endpoints[cls] = (right_units[0], left_units[0])

    recovered_identity = {}
    for obj in object_classes:
        candidates = []
        for p in obj:
            if p == zero:
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
        check(len(candidates) == 1, f"identity witness not unique: {candidates}")
        recovered_identity[obj] = candidates[0]

    # Only from here on do we consult the hidden fixture labels.
    original_object_class = {obj: q[identity] for obj, identity in ids.items()}
    check(len(object_classes) == len(ids), "wrong number of reconstructed object classes")
    check(set(original_object_class.values()) == set(object_classes), "object recovery mismatch")
    for obj, identity in ids.items():
        check(recovered_identity[original_object_class[obj]] == identity, "identity recovery mismatch")

    for name in names:
        source, target = original[name]
        recovered_source, recovered_target = recovered_endpoints[q[name]]
        check(recovered_source == original_object_class[source], "source recovery failed")
        check(recovered_target == original_object_class[target], "target recovery failed")

    for source_obj, target_obj in product(object_classes, repeat=2):
        fibre = {
            name
            for name in names
            if recovered_endpoints[q[name]] == (source_obj, target_obj)
        }
        expected = {
            name
            for name in names
            if original_object_class[original[name][0]] == source_obj
            and original_object_class[original[name][1]] == target_obj
        }
        check(fibre == expected, "Hom witness fibre recovery failed")

    for left, right in product(names, repeat=2):
        left_source, _left_target = recovered_endpoints[q[left]]
        _right_source, right_target = recovered_endpoints[q[right]]
        should_compose = left_source == right_target
        check((mul(left, right) != zero) == should_compose, "recovered typing/composability mismatch")
        if should_compose:
            result = mul(left, right)
            right_source, _ = recovered_endpoints[q[right]]
            _, left_target = recovered_endpoints[q[left]]
            check(
                recovered_endpoints[q[result]] == (right_source, left_target),
                "recovered composition typing mismatch",
            )


counts = {}
for n in range(1, 4):
    count = 0
    for relation in all_preorders(n):
        arrows, comp, ids = make_preorder(n, relation)
        verify_category(arrows, comp, ids)
        count += 1
    counts[n] = count
check(counts == {1: 1, 2: 4, 3: 29}, f"unexpected preorder counts: {counts}")

for k in range(1, 8):
    arrows = [("idA", "A", "A"), ("idB", "B", "B")] + [(f"f{t}", "A", "B") for t in range(k)]
    comp = {("idA", "idA"): "idA", ("idB", "idB"): "idB"}
    for t in range(k):
        f = f"f{t}"
        comp[("idB", f)] = f
        comp[(f, "idA")] = f
    verify_category(arrows, comp, {"A": "idA", "B": "idB"})

# One object with a nontrivial endomorphism: the group C2 as a one-object category.
arrows = [("id", "A", "A"), ("s", "A", "A")]
comp = {
    ("id", "id"): "id",
    ("id", "s"): "s",
    ("s", "id"): "s",
    ("s", "s"): "id",
}
verify_category(arrows, comp, {"A": "id"})

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
