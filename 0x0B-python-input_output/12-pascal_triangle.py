#!/usr/bin/python3
"""pacal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal's triangle of n"""
    triangle = []
    tmp = []
    row = []
    prev = -1
    current = 0

    for i in range(n):
        for j in range(len(tmp) +1):
            if prev == -1 or current == len(tmp):
                row.append(1)
            else:
                row.append(tmp[prev] + tmp[current])
            prev += 1
            current += 1
        triangle.append(row)
        tmp = row.copy()
    return triangle
