#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Returns area of rectangle """
        return self.width * self.height

    def display(self):
        """ Prints rectangle """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ String representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ Updates attributes """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation """
        attrs = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
