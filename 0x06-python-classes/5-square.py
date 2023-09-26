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
    @property
    def size(self):
        """returns the current square size
        Returns:
            the square size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """sets the square size
        Args:
            value (int): the new square size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
