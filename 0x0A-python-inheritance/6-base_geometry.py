#!/usr/bin/python3
"""Module to create a class"""


class BaseGeometry:
    """Class with public instance method"""
    def area(self):
        """Public instance method that raises an Exception with the message
        area() is not implemented"""
        raise Exception("area() is not implemented")
