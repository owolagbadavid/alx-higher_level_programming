#!/usr/bin/python3
"""Square class definition"""


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

    def __lt__(self, other):
        """less than comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is less than other, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """less than or equal to comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is less than or equal to other, False otherwise
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """equal to comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is equal to other, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal to comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is not equal to other, False otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is greater than other, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """greater than or equal to comparison

        Args:
            other (Square): the other square

        Returns:
            True if self is greater than or equal to other, False otherwise
        """
        return self.area() >= other.area()
