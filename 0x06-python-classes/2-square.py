#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A square class."""

    """class instantiation"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >=0')
        self.__size = size
