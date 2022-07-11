#!/usr/bin/python3
"""base module for the project"""
import json
import csv


class Base:
    """base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id: int --> id instance attribute"""

        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json representation of list of dictionaries'''

        if not list_dictionaries:
            return str([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''class method to wrote json str rep of list_objs'''

        file = f"{cls.__name__}.json"

        with open(file, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write(str([]))
            else:
                lst_dicts = [x.to_dictionary() for x in list_objs]
                jsonfile.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''

        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''

        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''

        file = f"{cls.__name__}.json"
        new = []

        try:
            with open(file) as reader:
                read = reader.read()
        except FileNotFoundError:
            return new

        json_file = Base.from_json_string(read)
        for o in json_file:
            new.append(cls.create(**o))

        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

