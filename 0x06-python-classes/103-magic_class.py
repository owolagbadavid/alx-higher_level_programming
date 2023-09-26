#!/usr/bin/python3
"""Defines a MagicClass class."""
import math


class MagicClass:
    """A class that stores a circle with a radius.

    Attributes:
        radius (float): radius of the circle
    """

    def __init__(self, radius=0):
        """Initializes a MagicClass instance.

        Args:
            radius (float): radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle.

        Returns:
            float: the area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.

        Returns:
            float: the circumference of the circle
        """
        return 2 * math.pi * self.__radius
