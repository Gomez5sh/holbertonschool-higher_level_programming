#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):

    with open(filename, encoding="UTF8") as f:
        l = f.readlines()
    return len(l)

    if nb_lines <= 0 or nb_lines >= len(l):
        for n in l:
            print(l, end="")
    else:
        for n in range(0, nb_lines):
            print(l[n], end="")
