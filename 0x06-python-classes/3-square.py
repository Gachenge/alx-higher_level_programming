#!/usr/bin/python3
"""a new class square"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """ initialise the square
        size: how big
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return(pow(self.__size, 2))
