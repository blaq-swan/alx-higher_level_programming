#!/usr/bin/python3
"""my module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """constructor"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size ** 2

    def __str__(self):
        """string"""
        return "[{}] {}/{}".format(
                type(self).__name__, self.__size, self.__size)
