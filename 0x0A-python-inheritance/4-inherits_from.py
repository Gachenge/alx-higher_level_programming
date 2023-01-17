#!/usr/bin/python3
"""check if inherited"""


def inherits_from(obj, a_class):
    """check if obj inherits from a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
