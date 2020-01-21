#!/usr/bin/python3


"""Write a function that writes an Object to a text file,"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
