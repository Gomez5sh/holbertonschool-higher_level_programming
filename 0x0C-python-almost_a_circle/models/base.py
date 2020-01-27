#!/usr/bin/python3


import json
import csv


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON dic"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Return JSON dic"""
        new = []
        file = cls.__name__ + ".json"
        if list_objs:
            for n in list_objs:
                new.append(n.to_dictionary())

        tmp = cls.to_json_string(new)
        with open(file, "w", encoding="utf-8") as new_file:
            new_file.write(tmp)
