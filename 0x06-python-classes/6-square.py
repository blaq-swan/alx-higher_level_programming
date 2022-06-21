#!/usr/bin/python3
"""square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter Method that gets private position

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """

        return self.__position

    @position.setter
    def position(self, value):
        """"""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Public Instance Method that calculates area of a square

        Returns:
            Area of a square
        """
        return pow(self.__size, 2)

    def my_print(self):
        x = self.__size
        y = self.__position
        """
        Public Instance method that prints a size by size square
        """
        if self.__size == 0:
            print()
        else:
            a, b = 0, 0
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                print("{}{}".format(" " * y[0], "#" * x))
