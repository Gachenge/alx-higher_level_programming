#!/usr/bin/python3
"""a new class square"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """ initialise the square
        size: how big
        """
        self.__size = size
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (pow(self.__size, 2))
