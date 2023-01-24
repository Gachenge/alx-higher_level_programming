#!/usr/bin/python3
"""function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creating an object from a file
    will not handle any exceptions
    """
    with open(filename, 'r') as f:
        return (json.load(f))
