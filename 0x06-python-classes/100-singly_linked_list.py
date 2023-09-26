#!/usr/bin/python3
"""Node class definition
defines a node of a singly linked list
defines a singly linked list
uses a sorted insert in the singly linked list

"""


class Node():
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Sets up a new node.

        Args:
            data (int): data stored inside the node
            next_node (Node): next node in the singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data stored inside the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data stored inside the node."""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the singly linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the singly linked list."""
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList():
    """Defines a singly linked list."""

    def __init__(self):
        """Sets up a new singly linked list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the singly linked list."""
        string = ""
        node = self.__head
        while node:
            string += str(node.data)
            if node.next_node:
                string += "\n"
            node = node.next_node
        return string

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
