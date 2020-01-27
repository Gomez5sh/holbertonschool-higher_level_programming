#!/usr/bin/python3


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
        """ Height """
        return self.__height

    @property
    """ Width """
    def width(self):
        return self.__width

    @property
    def y(self):
        """ Y """
        return self.__y

    @property
    def x(Self):
        """ X """
        return self.__x

    @width.setter
    """ sets width """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{}must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{}must be > 0".format("width"))
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("{}must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Sets x"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("x"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("x"))
        self.__x = value

    @y.setter
    def y(self, value):
        """ Sets y """
        if not isinstance(valuse, int):
            raise TypeError("{} must be an integer".format("y"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("y"))
        self.__y = value

    def area(self):
        """ Returns area"""
        return self.__width * self.__height

    def display(self):
        """ displays rectangle """
        print('\n' * self.__y, end="")
        for n in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ str returns """
        print("[Rectangle] ({}) {}/{} - {}/{}"
              .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """ assigns arguments """
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
        Dic = {}
        keys = ['id', 'width', 'height', 'x', 'y']

        for ite in kays:
            dic[ite] = getattr(self, ite)
        return dic
