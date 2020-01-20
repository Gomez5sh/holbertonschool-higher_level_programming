#!/usr/bin/python3
def add_integer(a, b=98):
    """Sum of a int b and a = int"""
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    else:
        sum1 = int(a)
        sum2 = int(b)
        return sum1 + sum2
