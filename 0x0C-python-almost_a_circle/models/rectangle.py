#!/usr/bin/python3
'''module for class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Child Class for Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor for class Rectangle'''

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''retrieves width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets width to value'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if 0 >= value:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        '''retrieves height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height to value'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if 0 >= value:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        '''retrieves x'''

        return self.__x

    @x.setter
    def x(self, value):
        '''sets x to value'''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if 0 > value:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''retrieves y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y to value'''

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if 0 > value:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        '''calculates area of rectangle'''

        return self.width * self.height

    def display(self):
        '''prints a string representation of the rectangle'''

        if self.width == 0 or self.height == 0:
            print("")
            return

        x = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(x, end='')

    def __str__(self):
        """overiding str method from Base Class"""

        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """private instance method to update attributes with args and kwargs"""

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dict representation of the class'''

        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
