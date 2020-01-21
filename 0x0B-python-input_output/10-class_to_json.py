#!/usr/bin/pthon3


"""Write a function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    New_obj = obj.__dict__
    return New_obj
