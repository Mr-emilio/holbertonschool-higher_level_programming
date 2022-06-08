#!/usr/bin/python3
"""module for mylist class"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """print the ascending sort list"""
        return print(sorted(self))
