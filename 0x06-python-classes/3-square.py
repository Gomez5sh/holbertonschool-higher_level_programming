#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("ize must be an integer")
        elif size < 0:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        Sq = self.__size * self.__size
        return (Sq)
