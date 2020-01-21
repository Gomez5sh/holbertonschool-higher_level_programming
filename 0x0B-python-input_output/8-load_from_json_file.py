#!/usr/bin/python3


"""Write a function that creates an Object from a “JSON file”:"""


def load_from_json_file(filename):
    import json
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)
