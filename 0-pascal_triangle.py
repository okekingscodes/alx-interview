#!/usr/bin/python3
"""Pascal Triangle Interview Challenge for Alx project"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):

            row.append(triangle[-1][j-1] + triangle[-1][j])
        row.append(1)
    triangle.append(row)

    return triangle