#!/usr/bin/python3
def print_square(size):
    """Prints a square using the '#' character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        print('#' * size)
