#!/usr/bin/python3
"""Square class definition..."""


class Square:
    """A square class
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """size instantiation
        Args:
            size (int): size of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
