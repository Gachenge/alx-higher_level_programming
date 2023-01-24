#!/usr/bin/python3
"""function that returns an object from json string"""
import json


def from_json_string(my_str):
    """convert a json string into a python object.
    we won't handle exceptions
    """
    return json.loads(my_str)
