#!/usr/bin/python3
"""module of lookup function"""


def lookup(obj):
    """return the list of available attributes and methods of an object"""
    return list(dir(obj))
