#!/usr/bin/python3
"""create the base of all other classes in project"""
import json


class Base:
    """all other classes in the project will be based on this
    this is what all other instances are based
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the base
        id: is an int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string representation of list_dictionaries
        if list_dictionaries is none or empty return string"[]"
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """if list_obj is none save an empty list
        filename must be classname.jason
        overwrite the file if it already exists
        """
        filename = cls.__name__ + ".json"

        with open (filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                new = [item.to_dictionary() for item in list_objs]
                f.write(Base.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """json string is a list of dictionaries
        if json_string is none or empty return an empty list
        """

        if json_string is None or json_string == []:
            return"[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """update the class with all attributes set
        create dummy first
        """
        if (dictionary and dictionary != {}):
            if cls.__name__ == 'Rectangle':
                new = cls(7, 4)
            else:
                new = cls(8)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """filename must be cls.json
        if file doesnt exist, return an empty list
        return list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**k) for k in list_dicts]
        except:
            return []
