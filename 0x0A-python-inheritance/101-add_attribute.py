#!/usr/bin/python3
"""Module to create a class"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
