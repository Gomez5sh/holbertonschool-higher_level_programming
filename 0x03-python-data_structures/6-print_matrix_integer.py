#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for it in matrix:
        blank = ""
        for n in it:
            print("{:s}{:d}".format(blank, n), end="")
            blank = " "
        print ()
