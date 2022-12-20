#!/usr/bin/python3
"""a new class square"""


class Square:
    """define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ initialise the square
        size: how big
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(x, int) for x in value)
                or not all(x >= 0 for x in value)):
            raise TypeError("position must be atuple of 2 positive integers")
        self.__position = value

    def area(self):
        return(pow(self.__size, 2))
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(1, self.__size + 1):
            for j in range(self.__position[0]):
                print(' ' , end='')
            for k in range(1, self.__size + 1):
                print('#', end='')
            print()
