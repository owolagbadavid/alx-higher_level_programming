#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Function that initilizes the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise,
        all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """Function that replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__[i] = json[i]
