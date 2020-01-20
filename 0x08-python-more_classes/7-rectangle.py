#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """Wigth"""
    @property
    def width(self):
        w = self.__width
        return w

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    """Height"""
    @property
    def height(self):
        h = self.__height
        return h

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * (self.__width + self.__height)
        return self.__perimeter

    def __str__(self):
        sq = []
        if self.__height == 0 or self.__width == 0:
            return ''
        else:
            sq = "{}".format(self.print_symbol) * self.__width
            return '\n'.join(sq for n in range(self.__height))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
