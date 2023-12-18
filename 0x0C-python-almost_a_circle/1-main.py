#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(7, 3)]
    Base.draw(list_rectangles, [])
