#!/usr/bin/python3
"""class square that defines a square"""


class Square:
    """Class square
    attributes
        size: type int, the side of a square
    """
    def __init__(self, size=0):
        """instantiation of an square"""
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """method that return the area of the square"""
        return (self.__size ** 2)
