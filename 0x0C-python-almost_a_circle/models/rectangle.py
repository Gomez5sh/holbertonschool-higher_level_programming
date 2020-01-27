#!/usr/bin/python3
"""
Rectangle Class
"""

from models.base import Base
import sys


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Height"""
        return self.__height

    @property
    def width(self):
        """Width"""
        return self.__width

    @property
    def y(self):
        """Y"""
        return self.__y

    @property
    def x(self):
        """X"""
        return self.__x

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """X setter"""
        if type(value) == int and value >= 0:
            self.__x = value
        elif type(value) != int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """Sets y"""
        if type(value) == int and value >= 0:
            self.__y = value
        elif type(value) != int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle"""
        print('\n' * self.y, end="")
        for n in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """str returns"""
        print("[Rectangle] ({}) {}/{} - {}/{}"
              .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """assigns arguments"""
        if args:
            for x in range(len(args)):
                if n == 0:
                    self.id = args[0]
                if n == 1:
                    self.width = args[1]
                if n == 2:
                    self.height = args[2]
                if n == 3:
                    self.x = args[3]
                if n == 4:
                    self.y = args[4]
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Class dictionary"""
        dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for ite in keys:
            dic[ite] = getattr(self, ite)
        return dic
