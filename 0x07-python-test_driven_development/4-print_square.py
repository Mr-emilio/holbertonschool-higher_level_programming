#!/usr/bin/python3
"""print a square"""


def print_square(size):
    """print a square"""

    if not type(size) is (int) or type(size) == float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
