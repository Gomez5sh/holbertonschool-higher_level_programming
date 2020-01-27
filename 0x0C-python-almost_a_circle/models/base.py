#!/usr/bin/python3
"""
Base module
"""


import json
import os


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON dic
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Return JSON dic
        """
        new = []
        file = cls.__name__ + ".json"
        if list_objs:
            for n in list_objs:
                new.append(n.to_dictionary())

        tmp = cls.to_json_string(new)
        with open(file, "w", encoding="utf-8") as new_file:
            new_file.write(tmp)

    def from_json_string(json_string):
        """
        return list from JSON
        """
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """
        Dictionary to Instance
        """
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        elif cls.__name__ == "Square":
            n = cls(1)
        n.update(**dictionary)
        return n

    def load_from_file(cls):
        """
        returns a list of instances of cls
        """
        new_list = []
        name = cls.__name__ + ".json"
        if os.path.isfile(name):
            with open(name, 'r') as file:
                read_line = file.read()
                list_from_clsdict = cls.from_json_string(read_line)
                for line in list_from_clsdict:
                    new_list.append(cls.create(**line))
                return new_list
        else:
            return new_list
