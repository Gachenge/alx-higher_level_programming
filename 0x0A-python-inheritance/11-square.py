#!/usr/bin/python3
"""class square that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square that inherits rectangle"""

    def __init__(self, size):
        """instantiation of the square
        size would include both width and length
        size validated by integer_validator
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
