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

    def to_json(self):
        return (self.__dict__)
