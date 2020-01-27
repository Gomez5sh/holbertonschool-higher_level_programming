#!/usr/bin/python3
"""
Base module
"""


import json
import csv


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
        my_list = []
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                        my_list.append(row)
            return([cls.create(**x) for x in my_list])
        except FileNotFoundError:
            return([[]])
