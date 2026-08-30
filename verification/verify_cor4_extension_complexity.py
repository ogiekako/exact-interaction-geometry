#!/usr/bin/env python3
"""Exact certificate that xc(COR(4)) = 16 via a 16-entry fooling set."""
from fractions import Fraction

checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)


# Coordinates: x0,x1,x2,x3,x01,x02,x03,x12,x13,x23.
points = []
for x in range(16):
    bits = [(x >> i) & 1 for i in range(4)]
    vertex = bits[:]
    for i in range(4):
        for j in range(i + 1, 4):
            vertex.append(bits[i] * bits[j])
    points.append(vertex)

# Each tuple is (designated positive-slack vertex, 10 linear coefficients + constant).
CERT = [
    (12, (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)),
    (10, (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)),
    (8, (-1, -1, -1, 2, 1, 1, -1, 1, -1, -1, 1)),
    (15, (-1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1)),
    (9, (0, 1, 0, 0, -1, 0, 1, 0, -1, 0, 0)),
    (1, (1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0)),
    (6, (1, 0, 0, 0, -1, -1, -1, 1, 1, 1, 0)),
    (14, (2, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1)),
    (11, (0, 0, 1, 0, 1, -1, 0, -1, 0, 0, 0)),
    (3, (0, 0, 0, 1, 1, 0, -1, 0, -1, 0, 0)),
    (13, (1, 0, 1, 0, -1, 1, -1, -1, 1, -1, 0)),
    (2, (0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0)),
    (0, (-1, -1, 2, -1, 1, -1, 1, -1, 1, -1, 1)),
    (4, (0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0)),
    (5, (0, 0, 1, 0, 0, 0, 0, -1, 1, -1, 0)),
    (7, (0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0)),
]


def slack(coefficients, vertex):
    return sum(coefficients[i] * vertex[i] for i in range(10)) + coefficients[10]


def rank_q(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    rows = len(work)
    cols = len(work[0]) if work else 0
    rank = 0
    for column in range(cols):
        pivot = next((i for i in range(rank, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][column]
        work[rank] = [entry / value for entry in work[rank]]
        for i in range(rows):
            if i != rank and work[i][column]:
                value = work[i][column]
                work[i] = [entry - value * pivot_entry for entry, pivot_entry in zip(work[i], work[rank])]
        rank += 1
    return rank


check(
    rank_q(
        [
            [points[i][j] - points[0][j] for j in range(10)]
            for i in range(1, 16)
        ]
    )
    == 10,
    "COR(4) dimension",
)

slack_rows = []
for k, (vertex_index, coefficients) in enumerate(CERT):
    values = [slack(coefficients, point) for point in points]
    check(min(values) >= 0, f"facet {k} validity")
    zero_vertices = [i for i, value in enumerate(values) if value == 0]
    check(len(zero_vertices) >= 10, f"facet {k} enough zero vertices")
    base = points[zero_vertices[0]]
    check(
        rank_q(
            [
                [points[z][j] - base[j] for j in range(10)]
                for z in zero_vertices[1:]
            ]
        )
        == 9,
        f"facet {k} affine dimension",
    )
    check(values[vertex_index] > 0, f"facet {k} designated positive slack")
    slack_rows.append(values)

check(len({vertex for vertex, _ in CERT}) == 16, "all sixteen vertices used once")
for i in range(16):
    vertex_i = CERT[i][0]
    for j in range(i):
        vertex_j = CERT[j][0]
        check(
            slack_rows[i][vertex_j] == 0 or slack_rows[j][vertex_i] == 0,
            f"fooling pair {i},{j}",
        )

print(f"PASS checks={checks}")
print("dim(COR4)=10; certified_facets=16; fooling_set_size=16")
print("LOWER: xc(COR4) >= rectangle_cover >= 16")
print("UPPER: 16-vertex simplex lift gives xc(COR4) <= 16")
print("CONCLUSION: xc(COR4)=16")
