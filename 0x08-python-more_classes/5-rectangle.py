#!/usr/bin/python3

"""class Rectangle"""


class Rectangle:
    """define the Rectangle"""

    def __init__(self, width=0, height=0):
        """ initialise the Rectangle
        width: how wide the rectangle
        height: how high
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def pprint(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ('\n'.join('#' * self.__width for _ in range(self.__height)))

    def __str__(self):
        return f"{self.pprint()}"

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
