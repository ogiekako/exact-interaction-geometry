#!/usr/bin/env python3
"""Solver-free verification of the Boolean Tucker junction counterexample.

All Boolean unfolding bases are enumerated directly from every nonzero support
mask on the corresponding mode. No normalization lemma, SAT/MIP solver,
randomness, floating point, or Python assert is used.
"""
from itertools import combinations, product

DIMS = (2, 4, 4)
BAD_WORD = 0x3EEBE9BE
GOOD_WORD = 0xEEE3113E
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError("FAIL: " + message)


def tensor_from_word(word, dims):
    a_size, b_size, c_size = dims
    return frozenset(
        (a, b, c)
        for a in range(a_size)
        for b in range(b_size)
        for c in range(c_size)
        if (word >> ((a * b_size + b) * c_size + c)) & 1
    )


def unfolding_columns(tensor, dims, mode):
    other = tuple(i for i in range(3) if i != mode)
    columns = set()
    for opposite in product(*(range(dims[i]) for i in other)):
        mask = 0
        for x in range(dims[mode]):
            point = [0, 0, 0]
            point[mode] = x
            point[other[0]], point[other[1]] = opposite
            if tuple(point) in tensor:
                mask |= 1 << x
        columns.add(mask)
    return frozenset(columns)


def union_closure(family):
    closure = {0}
    for generator in family:
        closure |= {value | generator for value in tuple(closure)}
    return frozenset(closure)


def exact_rank_and_families(columns, dimension):
    candidates = tuple(range(1, 1 << dimension))
    for size in range(dimension + 1):
        families = frozenset(
            family
            for family in combinations(candidates, size)
            if columns <= union_closure(family)
        )
        if families:
            return size, families
    raise RuntimeError("singleton supports must generate every column")


def mode_data(tensor):
    columns = tuple(unfolding_columns(tensor, DIMS, i) for i in range(3))
    data = tuple(exact_rank_and_families(columns[i], DIMS[i]) for i in range(3))
    return columns, data


def support(mask, dimension):
    return frozenset(i for i in range(dimension) if (mask >> i) & 1)


def maximal_sound_union(tensor, a_masks, b_masks, c_masks):
    a_sets = tuple(support(x, 2) for x in a_masks)
    b_sets = tuple(support(x, 4) for x in b_masks)
    c_sets = tuple(support(x, 4) for x in c_masks)
    covered = set()
    for a_set, b_set, c_set in product(a_sets, b_sets, c_sets):
        box = frozenset(product(a_set, b_set, c_set))
        if box and box <= tensor:
            covered.update(box)
    return frozenset(covered)


def main():
    bad = tensor_from_word(BAD_WORD, DIMS)
    require(len(bad) == 22, "bad positive count")
    columns, data = mode_data(bad)
    require(tuple(rank for rank, _ in data) == (2, 3, 3), "bad mode ranks")
    require(columns[0] == frozenset((0x01, 0x02, 0x03)), "mode-1 columns")
    require(columns[1] == frozenset((0x06, 0x07, 0x09, 0x0B, 0x0F)), "mode-2 columns")
    require(columns[2] == frozenset((0x03, 0x09, 0x0B, 0x0E)), "mode-3 columns")

    expected_a = frozenset(((0x01, 0x02),))
    expected_b = frozenset(((0x03, 0x06, 0x09),))
    expected_c = frozenset(((0x03, 0x09, 0x0E),))
    require(data[0][1] == expected_a, "unique A minimum basis among all masks")
    require(data[1][1] == expected_b, "unique B minimum basis among all masks")
    require(data[2][1] == expected_c, "unique C minimum basis among all masks")

    target = (0, 1, 1)
    require(target in bad, "target positive")
    blockers = {
        (0x03, 0x03): (0, 0, 0),
        (0x03, 0x0E): (0, 1, 2),
        (0x06, 0x03): (0, 2, 1),
        (0x06, 0x0E): (0, 2, 2),
    }
    seen = set()
    b_basis = next(iter(expected_b))
    c_basis = next(iter(expected_c))
    for b_mask, c_mask in product(b_basis, c_basis):
        if ((b_mask >> 1) & 1) and ((c_mask >> 1) & 1):
            seen.add((b_mask, c_mask))
            zero = blockers[(b_mask, c_mask)]
            require(zero not in bad, f"blocking zero {b_mask:x},{c_mask:x}")
            require((b_mask >> zero[1]) & 1, "blocker lies in B support")
            require((c_mask >> zero[2]) & 1, "blocker lies in C support")
    require(seen == set(blockers), "exactly four candidate lifts")

    literal2 = (1, 2)
    literal4 = (1, 2, 4, 8)
    require(maximal_sound_union(bad, literal2, b_basis, literal4) == bad, "profile (2,3,4)")
    require(maximal_sound_union(bad, literal2, literal4, c_basis) == bad, "profile (2,4,3)")

    good = tensor_from_word(GOOD_WORD, DIMS)
    _, good_data = mode_data(good)
    require(tuple(rank for rank, _ in good_data) == (2, 3, 3), "good mode ranks")
    phi = (0, 1, 2, 2)
    core = frozenset((a, b, c) for a, b, c in bad if b < 3 and c < 3)
    rebuilt = frozenset(
        (a, b, c)
        for a in range(2)
        for b in range(4)
        for c in range(4)
        if (a, phi[b], phi[c]) in core
    )
    require(rebuilt == good, "good exact (2,3,3) Tucker decomposition")
    print(
        f"PASS boolean-tucker-junction checks={CHECKS} "
        f"bad={BAD_WORD:#x} good={GOOD_WORD:#x} exhaustive_generators=15"
    )


if __name__ == "__main__":
    main()
