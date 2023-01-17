#!/usr/bin/python3
"""class rectangle that inherits from baseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """new class inherits basegeometry"""

    def __init__(self, width, height):
        """instantiation of the class
        width: the width of the rectangle
        height: the height of the rectangle
        check with integer_validator if the height and width are integers
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """find the are of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
