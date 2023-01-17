#!/usr/bin/python3
"""function to check if its instance of """


def is_same_class(obj, a_class):
    """check if object is an instance of class"""
    if type(obj) == a_class:
        return True
    return False
