#!/usr/bin/env python3
"""Solver-free regression for the two-state max-plus tail theorem.

This is not the proof. It directly checks the closed forms, the exact
tail trichotomy (propagate / forget / read-and-forget), and an exact
counter-state evaluator against direct max-plus semantics on exhaustive finite
test families. In particular it contains the all-zero letter as an explicit
silent-forget regression.
"""
from itertools import product

NEG = None
INF = "INF"
ENTRIES = (NEG, -2, -1, 0, 1, 2)
SMALL = (NEG, 0, 1)


def fail(msg):
    raise RuntimeError(msg)


def mp_add(x, y):
    return NEG if x is NEG or y is NEG else x + y


def mp_max(*xs):
    ys = [x for x in xs if x is not NEG]
    return max(ys) if ys else NEG


def step(x, M):
    a, b, c, d = M
    return (
        mp_max(mp_add(x[0], a), mp_add(x[1], c)),
        mp_max(mp_add(x[0], b), mp_add(x[1], d)),
    )


def value_direct(I, mats, F, word):
    x = I
    for letter in word:
        x = step(x, mats[letter])
    return mp_max(mp_add(x[0], F[0]), mp_add(x[1], F[1]))


def normalize(x):
    if x[0] is NEG and x[1] is NEG:
        return None
    if x[1] is NEG:
        return (1, INF, x[0])
    if x[0] is NEG:
        return (2, INF, x[1])
    H = max(x)
    if x[0] >= x[1]:
        return (1, x[0] - x[1], H)
    return (2, x[1] - x[0], H)


def threshold(I, mats, F):
    finite = [v for v in I + F if v is not NEG]
    for M in mats.values():
        finite.extend(v for v in M if v is not NEG)
    if len(finite) <= 1:
        return 1
    return 1 + max(abs(x - y) for x in finite for y in finite)


def normalized_row(row):
    x, y = row
    if x is NEG and y is NEG:
        return None
    if y is NEG:
        return (1, INF)
    if x is NEG:
        return (2, INF)
    if x >= y:
        return (1, x - y)
    return (2, y - x)


def compiled_step(side, n, H, M, K):
    # Current vector is (H,H-n) for side 1, or (H-n,H) for side 2.
    if n == INF:
        active = M[:2] if side == 1 else M[2:]
        A = mp_max(*active)
        if A is NEG:
            return None
        q = normalized_row(active)
        return (q[0], q[1], H + A)

    if n <= K:
        x = (H, H - n) if side == 1 else (H - n, H)
        return normalize(step(x, M))

    active = M[:2] if side == 1 else M[2:]
    inactive = M[2:] if side == 1 else M[:2]
    A = mp_max(*active)

    # READ-AND-FORGET: the active row is absent. The old gap contributes -n
    # to the height and is absent from the successor projective state.
    if A is NEG:
        C = mp_max(*inactive)
        if C is NEG:
            return None
        q = normalized_row(inactive)
        return (q[0], q[1], H + C - n)

    # CONSTANT-OUTPUT cases. With two active finite outputs, the successor
    # gap is bounded and forgets n. With exactly one active finite output,
    # the old gap either propagates by a fixed shift or is forgotten into an
    # infinite-gap state. In every such case the height increment is constant.
    if active[0] is not NEG and active[1] is not NEG:
        q = normalized_row(active)
        return (q[0], q[1], H + A)
    if active[0] is not NEG:
        if inactive[1] is NEG:
            return (1, INF, H + A)
        n2 = n + active[0] - inactive[1]
        if n2 <= 0:
            fail(("bad positive-tail shift", side, n, M, n2))
        return (1, n2, H + A)
    if inactive[0] is NEG:
        return (2, INF, H + A)
    n2 = n + active[1] - inactive[0]
    if n2 <= 0:
        fail(("bad negative-tail shift", side, n, M, n2))
    return (2, n2, H + A)


def value_compiled(I, mats, F, word):
    q = normalize(I)
    if q is None:
        return NEG
    side, n, H = q
    K = threshold(I, mats, F)
    for letter in word:
        q = compiled_step(side, n, H, mats[letter], K)
        if q is None:
            return NEG
        side, n, H = q

    active = F[side - 1]
    other = F[2 - side]
    if n == INF:
        return NEG if active is NEG else H + active
    if n <= K:
        x = (H, H - n) if side == 1 else (H - n, H)
        return mp_max(mp_add(x[0], F[0]), mp_add(x[1], F[1]))
    if active is not NEG:
        return H + active
    if other is NEG:
        return NEG
    return H - n + other


def check_closed_forms():
    count = 0
    for M in product(ENTRIES, repeat=4):
        a, b, c, d = M
        for z in range(-8, 9):
            x = (z, 0)
            y = step(x, M)
            u1 = mp_max(mp_add(z, a), c)
            u2 = mp_max(mp_add(z, b), d)
            if y != (u1, u2):
                fail(("closed step", M, z, y, (u1, u2)))
            if y != (NEG, NEG):
                delta = max(v for v in y if v is not NEG) - max(z, 0)
                A = mp_max(a, b)
                C = mp_max(c, d)
                pred = (
                    mp_max(A, NEG if C is NEG else C - z)
                    if z >= 0
                    else mp_max(NEG if A is NEG else A + z, C)
                )
                if delta != pred:
                    fail(("height increment", M, z, delta, pred))
            count += 1
    return count


def classify_tail(M, side):
    finite = [v for v in M if v is not NEG]
    K = (
        1
        if len(finite) <= 1
        else 1 + max(abs(x - y) for x in finite for y in finite)
    )
    ns = list(range(K + 1, K + 7))
    seq = []
    for n in ns:
        x = (0, -n) if side == 1 else (-n, 0)
        seq.append(normalize(step(x, M)))

    if all(q is None for q in seq):
        return "death", K, ns, seq
    if any(q is None for q in seq):
        fail(("mixed death in tail", M, side, K, seq))

    states = [(q[0], q[1]) for q in seq]
    heights = [q[2] for q in seq]

    if len(set(heights)) == 1:
        if len(set(states)) == 1:
            return "forget", K, ns, seq
        sides = [q[0] for q in seq]
        mags = [q[1] for q in seq]
        if (
            len(set(sides)) == 1
            and all(m != INF for m in mags)
            and len({m - n for m, n in zip(mags, ns)}) == 1
        ):
            return "propagate", K, ns, seq
        fail(("constant-output tail is neither propagate nor forget", M, side, K, seq))

    if len(set(states)) == 1 and len({h + n for h, n in zip(heights, ns)}) == 1:
        return "read-and-forget", K, ns, seq

    fail(("tail trichotomy violation", M, side, K, seq))


def check_tail():
    count = 0
    kinds = {"death": 0, "propagate": 0, "forget": 0, "read-and-forget": 0}
    for M in product(ENTRIES, repeat=4):
        for side in (1, 2):
            kind, _, ns, _ = classify_tail(M, side)
            kinds[kind] += 1
            count += len(ns)

    # Explicitly check the silent-forget case.
    for side in (1, 2):
        kind, _, _, _ = classify_tail((0, 0, 0, 0), side)
        if kind != "forget":
            fail(("all-zero letter must silently forget", side, kind))

    return count, kinds


def check_compiler():
    count = 0
    mats1 = list(product(SMALL, repeat=4))
    vectors = list(product(SMALL, repeat=2))

    # Exhaust every one-letter automaton in this finite family through length 10.
    for M in mats1:
        mats = {0: M}
        for I in vectors:
            for F in vectors:
                for n in range(11):
                    w = (0,) * n
                    a = value_direct(I, mats, F, w)
                    b = value_compiled(I, mats, F, w)
                    if a != b:
                        fail(("unary compiler", M, I, F, n, a, b))
                    count += 1

    # Two-letter stress family: every ordered matrix pair, four endpoint pairs,
    # and every word of length at most 3.
    endpoints = [
        ((0, 0), (0, 0)),
        ((0, NEG), (0, NEG)),
        ((NEG, 0), (NEG, 0)),
        ((0, 1), (1, 0)),
    ]
    words = [()]
    for n in range(1, 4):
        words.extend(product((0, 1), repeat=n))
    for M0 in mats1:
        for M1 in mats1:
            mats = {0: M0, 1: M1}
            for I, F in endpoints:
                for w in words:
                    a = value_direct(I, mats, F, w)
                    b = value_compiled(I, mats, F, w)
                    if a != b:
                        fail(("binary compiler", M0, M1, I, F, w, a, b))
                    count += 1
    return count


def main():
    c1 = check_closed_forms()
    c2, kinds = check_tail()
    c3 = check_compiler()
    print("PASS two-state max-plus tail/compiler regression")
    print("closed-form cases:", c1)
    print("tail cases:", c2, kinds)
    print("end-to-end word cases:", c3)


if __name__ == "__main__":
    main()
