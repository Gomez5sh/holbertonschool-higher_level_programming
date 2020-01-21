#!/usr/bin/python3


"""laods adds and saves a file"""


import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

Myfile = len(sys.argv)


try:
    n = load_from_json_file("add_item.json")
except:
    n = []


for it in range(1, Myfile):
    n.append(sys.argv[it])
save_to_json_file(n, "add_item.json")
