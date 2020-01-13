#!/usr/bin/python3
def add_integer(a, b=98):
    """Sum of a int
    b and a = int
    """

    if not isinstance(a (int, float)):
        raise TypeError("a must be an intege")
    elif not isinstance(b (int, float)):
        raise TypeError("b must be an integer")
    else:
        sum = (int(a) + int(b))
        return (sum)
