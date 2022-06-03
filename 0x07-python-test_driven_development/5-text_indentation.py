#!/usr/bin/python3
""" print text with 2 new lines after special characters"""


def text_indentation(text):
    """prints a text"""
    aux = True

    if type(text) != (str):
        raise TypeError("text must be a string")

    for i in text:
        if i == " " and aux is True:
            continue
        if i in [".", "?", ":"]:
            print(i, end="")
            print()
            print()
            aux = True
        else:
            print(i, end="")
            aux = False
