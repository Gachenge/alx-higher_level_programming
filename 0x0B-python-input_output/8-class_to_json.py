#!/usr/bin/python3
"""function that returns dictionary description"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    obj is an instance of a class
    all attributes of obj are serializable
    """
    return obj.__dict__
