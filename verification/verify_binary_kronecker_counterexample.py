#!/usr/bin/env python3
"""Independent checks for the retained binary-Kronecker calibration.

The JSON certificate is the single source of rectangle data. The checker also
computes the exact binary rank of the 5 x 5 base matrix by an independent
rectangle-partition dynamic program.
"""
import json
from functools import lru_cache
from pathlib import Path

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError("FAIL: " + message)


def kron(a, b):
    ma, na = len(a), len(a[0])
    mb, nb = len(b), len(b[0])
    return tuple(
        tuple(a[i // mb][j // nb] * b[i % mb][j % nb] for j in range(na * nb))
        for i in range(ma * mb)
    )


def exact_binary_rank(matrix):
    m, n = len(matrix), len(matrix[0])
    ones = tuple((i, j) for i in range(m) for j in range(n) if matrix[i][j])
    index = {cell: k for k, cell in enumerate(ones)}
    rectangles = set()
    for row_mask in range(1, 1 << m):
        rows = tuple(i for i in range(m) if (row_mask >> i) & 1)
        for col_mask in range(1, 1 << n):
            cols = tuple(j for j in range(n) if (col_mask >> j) & 1)
            if all(matrix[i][j] for i in rows for j in cols):
                mask = 0
                for i in rows:
                    for j in cols:
                        mask |= 1 << index[(i, j)]
                rectangles.add(mask)
    rectangles = tuple(sorted(rectangles, key=int.bit_count, reverse=True))
    by_cell = [[] for _ in ones]
    for rectangle in rectangles:
        for k in range(len(ones)):
            if (rectangle >> k) & 1:
                by_cell[k].append(rectangle)
    full = (1 << len(ones)) - 1

    @lru_cache(maxsize=None)
    def dp(remaining):
        if remaining == 0:
            return 0
        cell = (remaining & -remaining).bit_length() - 1
        best = len(ones) + 1
        for rectangle in by_cell[cell]:
            if rectangle & remaining == rectangle:
                best = min(best, 1 + dp(remaining ^ rectangle))
        return best

    return dp(full), len(rectangles)


def main():
    cert_path = (
        Path(__file__).resolve().parents[1]
        / "discoveries"
        / "certificates"
        / "binary-kronecker-seed5-self-k24.json"
    )
    cert = json.loads(cert_path.read_text())
    check(cert["mode"] == "binary_partition", "certificate mode")
    left = tuple(tuple(int(x) for x in row) for row in cert["left_matrix"])
    right = tuple(tuple(int(x) for x in row) for row in cert["right_matrix"])
    check(left == right, "self-product matrices differ")
    check(len(left) == 5 and all(len(row) == 5 for row in left), "base matrix shape")
    check(all(x in (0, 1) for row in left for x in row), "base matrix is not binary")

    rank, legal_rectangle_count = exact_binary_rank(left)
    check(rank == 5, f"exact rectangle-partition DP returned rank {rank}")

    tensor = kron(left, right)
    ones = {(i, j) for i in range(25) for j in range(25) if tensor[i][j]}
    count = {cell: 0 for cell in ones}
    rectangles = cert["rectangles"]
    check(len(rectangles) <= int(cert["target_k"]), "too many certificate rectangles")
    area = 0
    for q, rectangle in enumerate(rectangles, 1):
        rows = tuple(rectangle["rows"])
        cols = tuple(rectangle["cols"])
        check(rows and cols, f"empty rectangle {q}")
        check(len(rows) == len(set(rows)) and len(cols) == len(set(cols)), f"duplicate index in rectangle {q}")
        for i in rows:
            for j in cols:
                check(0 <= i < 25 and 0 <= j < 25, f"out-of-range index in rectangle {q}")
                check(tensor[i][j] == 1, f"rectangle {q} hits zero at {(i, j)}")
                count[(i, j)] += 1
                area += 1
    check(len(ones) == 196, "unexpected tensor support size")
    check(area == len(ones), "certificate area mismatch")
    check(all(v == 1 for v in count.values()), "tensor support not partitioned exactly once")
    print(
        "PASS binary-Kronecker calibration: "
        f"rank_bin(A)={rank}, legal_base_rectangles={legal_rectangle_count}, "
        f"tensor_ones={len(ones)}, certificate_rectangles={len(rectangles)}"
    )


if __name__ == "__main__":
    main()
