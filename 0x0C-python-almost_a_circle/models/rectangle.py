#!/usr/bin/python3

"""child class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise the rectangle
        width: the width of the rectangle
        height: its height
        x: x
        y: y
        Raises:
            TypeError: must be int
            ValueError: must not be negative
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the are of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """print the rectangle, using the '#'"""
        if self.height == 0 or self.width == 0:
            print("")
            return
        [print("") for i in range(self.y)]
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """the string and the print representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))

    def update(self, *args, **kwargs):
        """update the attributes of the rectangle"""
        x = 0
        if args and len(args) != 0:
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """the dictionary representation of the rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
