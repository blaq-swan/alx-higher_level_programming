#!/usr/bin/python3
"""square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size: the length of a square
       """
        self.__size = size

    @property
    def size(self):
        """
        Getter Method that gets the value of size

        Args:
            Magic arg. Self ref to object

        Raises:
            TypeError: size must be an integer
            ValueError : size must be >= 0

        Returns:
            size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method. Sets size to value

        Args:
            value: new dimension for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public Instance Method that calculates area of a square

        Returns:
            Area of a square
        """
        return pow(self.__size, 2)

    def my_print(self):
        """
        Public Instance method that prints a size by size square
        """
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="\n" if y is self.size - 1 and x != y else "")
        print()
