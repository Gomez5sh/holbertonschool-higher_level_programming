#!/usr/bin/python3
"""
Square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init for square args"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str return"""
        return('[Square] ({}) {}/{} - {}'
            .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, width):
        """size setter"""
        self.width = width
        self.height = width

    def update(self, *args, **kwargs):
        """Update the class Square
        by
        adding the public method"""
        if args:
            for y in range(len(args)):
                if y == 0:
                    self.id = args[0]
                if y == 1:
                    self.size = args[1]
                if y == 2:
                    self.x = args[2]
                if y == 3:
                    self.y = args[3]

            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Square  Dictionary"""
        dic = {}
        keys = ['id', 'size', 'x', 'y']

        for ite in keys:
            dic[ite] = getattr(self, ite)
        return dic
