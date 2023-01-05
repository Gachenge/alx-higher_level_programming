#!/usr/bin/python3
" print a square"


def print_square(size):
    """print a square using '#'
    Args:
        size is the length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float less than 0
    print the square
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(1, size):
            print('#', end='')
        print('#')
