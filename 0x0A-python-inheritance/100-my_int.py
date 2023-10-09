#!/usr/bin/python3
"""Module to create a class"""


class MyInt(int):
    """Class that inherits from int"""
    def __eq__(self, other):
        """Method to invert == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Method to invert != operator"""
        return super().__eq__(other)
