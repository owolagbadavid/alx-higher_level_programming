#!/usr/bin/python3
"""Square class definition...
This class defines a square based on 5-square.py
it adds a new private instance attribute position
it adds a public getter and setter for position
it adds a public instance method that prints the square
taking into account position

"""


class Square:
    """A square class
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    @property
    def position(self):
        """returns the current square position
        Returns:
            the square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the square position
        Args:
            value (int): the new square position
        Returns:
            None
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints the square, takes into account position"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
