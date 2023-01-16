#!/usr/bin/python3

"""new class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherit from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):

        """initialise a new square
        size: serves as both width and height
        x: the x coordinate
        y: the y coordinate
        id: identity of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return (self.height)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update the all the attributes of the square"""
        x = 0
        if (args and len(args) != 0):
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

        elif (kwargs and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of the square and attributes"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
