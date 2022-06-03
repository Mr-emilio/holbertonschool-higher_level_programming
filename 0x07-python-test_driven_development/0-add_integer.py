#!/usr/bin/python3
"""
function adds 2 integers
"""


def add_integer(a, b=98):
    """return the addition of 2 integers"""

    if type(a) is float:
        a = int(a)
    if not type(a) in (int, float):
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if not type(b) in (int, float):
        raise TypeError("b must be an integer")

    return a + b
