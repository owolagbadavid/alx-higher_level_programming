#!/usr/bin/python3
"""Square class definition..."""


class Square:
    """A square class
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """checks size for errors
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

    def area(self):
        """returns the current square area
        Returns:
            the square area
        """
        return self.__size ** 2
