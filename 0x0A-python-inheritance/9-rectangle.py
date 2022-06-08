#!/usr/bin/python3
"""module for rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """init constructor method for rectangel"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method"""
        width = str(self.__width)
        height = str(self.__height)
        description = "[Rectangle] " + width + "/" + height
        return description
