#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string representation """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary()
                                            for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of JSON string representation """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV
        Format of the CSV:
        Rectangle: <id>,<width>,<height>,<x>,<y>
        Square: <id>,<size>,<x>,<y>
        """
        with open("{}.csv".format(cls.__name__), "w") as f:
            if cls.__name__ == "Rectangle":
                f.write("id,width,height,x,y\n")
            else:
                f.write("id,size,x,y\n")
            if list_objs is not None:
                for i in list_objs:
                    if cls.__name__ == "Rectangle":
                        f.write("{},{},{},{},{}\n".format(i.id, i.width,
                                                          i.height,
                                                          i.x, i.y))
                    else:
                        f.write("{},{},{},{}\n".format(i.id, i.size,
                                                       i.x, i.y))

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV
        Format of the CSV:
        Rectangle: <id>,<width>,<height>,<x>,<y>
        Square: <id>,<size>,<x>,<y>
        """
        try:
            with open("{}.csv".format(cls.__name__), "r") as f:
                if cls.__name__ == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                else:
                    attrs = ["id", "size", "x", "y"]
                return [cls.create(**dict(zip(attrs, [int(i) for i in
                                                      line.split(",") if
                                                      i != "\n"])))
                        for line in f.readlines()[1:]]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws rectangles and squares """
        import turtle
        import random

        turtle.bgcolor("black")
        turtle.title("Rectangles and Squares")
        turtle.speed(0)
        turtle.hideturtle()
        turtle.pensize(3)

        for i in list_rectangles:
            turtle.color(random.random(), random.random(), random.random())
            turtle.penup()
            turtle.goto(i.x, i.y)
            turtle.pendown()
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)

        for i in list_squares:
            turtle.color(random.random(), random.random(), random.random())
            turtle.penup()
            turtle.goto(i.x, i.y)
            turtle.pendown()
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)

        turtle.exitonclick()
