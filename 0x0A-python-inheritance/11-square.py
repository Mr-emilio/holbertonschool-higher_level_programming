#!/usr/bin/python3
"""module for square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init constructor method for square"""
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle_width = size
        self._Rectangle_height = size

    def area(self):
        """area method"""
        return self.__size ** 2

    def __str__(self):
        """__str__ method"""
        size = str(self.__size)
        description = "[Square] " + size + "/" + size
        return description
