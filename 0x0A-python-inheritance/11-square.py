#!/usr/bin/python3
"""Module to create a class"""


class Square(__import__('9-rectangle').Rectangle):
    """Class that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def print(self):
        """Prints the square with size"""
        print(self.__str__())
