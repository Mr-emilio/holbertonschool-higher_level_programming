#!/usr/bin/python3
"""
function prints name
"""


def say_my_name(first_name, last_name=""):
    """function that prints the name"""
    if not type(first_name) is (str):
        raise TypeError("first_name must be a string")

    if not type(last_name) is (str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
