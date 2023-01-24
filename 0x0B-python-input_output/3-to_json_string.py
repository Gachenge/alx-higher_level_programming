#!/usr/bin/python3
"""function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """convert a string to its JSON representation.
    won't manage any exceptions
    """
    return json.dumps(my_obj)
