#!/usr/bin/python3
"""class student that defines a student"""


class Student:
    """define the student"""

    def __init__(self, first_name, last_name, age):
        """initialise the student attributes
        public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(type(ele) == str for ele in attrs):
            return ({x: getattr(self, x) for x in attrs if hasattr(self, x)})
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
