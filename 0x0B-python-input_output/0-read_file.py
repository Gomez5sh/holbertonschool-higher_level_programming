#!/usr/bin/python3


"""Opens and read file"""


def read_file(filename=""):

    with open(filename, encoding="UTF8") as f:
        text = f.read()
        print(text, end="")
