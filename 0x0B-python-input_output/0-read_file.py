#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """read a text file (UTF) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
