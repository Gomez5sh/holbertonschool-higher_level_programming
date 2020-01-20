#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    n = 0
    if not matrix:
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(""matrix must be a matrix \
        (list of lists) of integers/floats)
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for x in matrix:
        if n != 0 and len(x) != n:
        raise TypeError("Each row of the matrix must have the same size")
    for f in x:
        if type(j) != int and type(j) != float:
            raise TypeError("matrix must be a matrix (list of lists) of \
            integers/floats")
    n = len(x)

    return list(map(lambda lamb:
                    list(map(lambda da: round(da / div, 2), lamb)), matrix))
