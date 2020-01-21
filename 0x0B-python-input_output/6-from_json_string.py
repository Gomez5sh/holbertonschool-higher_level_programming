#!/usr/bin/python3

"""Write a function that returns an object"""

def from_json_string(my_str):
    import json
    return json.loads(my_str)
