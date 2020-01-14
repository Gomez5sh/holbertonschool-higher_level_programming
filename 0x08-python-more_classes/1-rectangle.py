#!/usr/bn/pithon3
class Rectangle:

    def __init__(self, width=0, height=0):
        """Init method variables"""
        self.height = height
        self.width = width

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
