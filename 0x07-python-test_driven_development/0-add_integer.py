#!/usr/bin/python3

"""introduce the addition function"""

def add_integer(a, b=98):
    """Return the integer add of a and b.

    a and b are typecast to ints:

    Raises:
        TypeError: if either is neither integer nor float
        """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
