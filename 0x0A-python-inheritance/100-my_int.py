#!/usr/bin/python3
"""module of class MyInt"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """__eq__ method"""
        return False

    def __ne__(self, other):
        """__ne__ method"""
        return True
