#!/usr/bin/python3
"""print number of lines"""
def number_of_lines(filename=""):

    poimt = 0
    with open(filename, encoding="UTF8") as f:
        l = f.readlines()
    return len(l)
