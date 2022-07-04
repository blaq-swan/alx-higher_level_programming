#!/usr/bin/python3
"""my module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class"""

    def __init__(self, width, height):
        """constrcutor"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return self.__height * self.__width

    def __str__(self):
        rep = "[" + str(self.__class__.__name__) + "] "
        rep += str(self.__width) + "/" + str(self.__height)

        return rep
