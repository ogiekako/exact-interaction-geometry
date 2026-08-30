#!/usr/bin/env python3
"""Finite regression for operational codescent and its sharp boundary fixtures."""
from itertools import product

MAX_LEN = 8


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def paths(edges, start, end, max_len):
    out = {()} if start == end else set()
    frontier = {(start, ())}
    for _ in range(max_len):
        nxt = set()
        for vertex, word in frontier:
            for source, target, label in edges:
                if source != vertex:
                    continue
                word2 = word + (label,)
                nxt.add((target, word2))
                if target == end:
                    out.add(word2)
        frontier = nxt
    return out


def concat_star(blocks, max_len):
    blocks = {b for b in blocks if b}
    out = {()}
    frontier = {()}
    while frontier:
        nxt = set()
        for prefix in frontier:
            for block in blocks:
                word = prefix + block
                if len(word) <= max_len and word not in out:
                    out.add(word)
                    nxt.add(word)
        frontier = nxt
    return out


def check_joint_star_exhaustive():
    first = [("s", "a", "1sa"), ("a", "s", "1as"), ("a", "a", "1aa"), ("s", "s", "1ss")]
    second = [("s", "b", "2sb"), ("b", "s", "2bs"), ("b", "b", "2bb"), ("s", "s", "2ss")]
    cases = 0
    for bits in product([0, 1], repeat=8):
        e1 = [e for e, keep in zip(first, bits[:4]) if keep]
        e2 = [e for e, keep in zip(second, bits[4:]) if keep]
        global_ss = paths(e1 + e2, "s", "s", MAX_LEN)
        child_blocks = paths(e1, "s", "s", MAX_LEN) | paths(e2, "s", "s", MAX_LEN)
        require(global_ss == concat_star(child_blocks, MAX_LEN), ("mixed-return mismatch", bits))
        cases += 1
    return cases


def bicyclic_mul(x, y):
    a, b = x
    c, d = y
    m = min(b, c)
    return a + c - m, b + d - m


def check_premature_neutralization():
    one, p, q = (0, 0), (0, 1), (1, 0)
    after_p = bicyclic_mul(one, p)
    require(after_p != one, "push unexpectedly neutral")
    require(bicyclic_mul(one, q) != one, "pop unexpectedly neutral")
    require(bicyclic_mul(after_p, q) == one, "raw push/pop composite did not neutralize")


def step_stack(stack, op):
    kind, value = op
    stack = list(stack)
    if kind == "p":
        stack.append(value)
        return tuple(stack)
    if kind == "q":
        if not stack or stack[-1] != value:
            return None
        stack.pop()
        return tuple(stack)
    raise ValueError(op)


def run_stack(stack, ops):
    current = tuple(stack)
    for op in ops:
        current = step_stack(current, op)
        if current is None:
            return None
    return current


def check_unsealed_macro():
    start = ("b", "a")
    e = (("q", "a"), ("p", "a"))
    f = (("q", "b"),)
    require(run_stack(start, e + f) is None, "atomic e;f became legal")
    require(run_stack(start, f + e) is None, "atomic f;e became legal")
    require(run_stack(start, (e[0],) + f + (e[1],)) == ("a",), "unsealed interleaving missing")


def retract(stack, owner):
    return tuple(x for x in stack if x == owner)


def check_factor_projections():
    c, d = ("a", "b"), ("b", "a")
    require(retract(c, "a") == retract(d, "a") == ("a",), "a projections differ")
    require(retract(c, "b") == retract(d, "b") == ("b",), "b projections differ")
    qa = (("q", "a"),)
    require(run_stack(c, qa) is None, "q_a unexpectedly legal from ab")
    require(run_stack(d, qa) == ("b",), "q_a unexpectedly illegal from ba")


if __name__ == "__main__":
    cases = check_joint_star_exhaustive()
    check_premature_neutralization()
    check_unsealed_macro()
    check_factor_projections()
    print(f"PASS operational codescent regression cases={cases}")
