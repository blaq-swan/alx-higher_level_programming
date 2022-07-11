#!/usr/bin/python3
"""module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """child class of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor for class Square'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''string representation for the objects of Square'''

        return '[Square] ({}) {}/{} - {}'.\
            format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        '''getter method. Retrieves size'''

        return self.height

    @size.setter
    def size(self, value):
        '''sets width and height of Square'''

        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''class private instance method for class Square'''

        if id is not None:
            self.id = id
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if size is not None:
            self.size = size

    def update(self, *args, **kwargs):
        '''updates instance attributes for Square'''
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dictioanry representation of the class Square'''

        return {'id': self.id, 'size': self.height, 'x': self.x, 'y': self.y}
