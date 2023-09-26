#!/usr/bin/python3
"""Singly Linked Lists module.

This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.

"""


class Node():
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.

        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        """Sets the necessary attributes for the SinglyLinkedList object."""
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""
        string = ""
        node = self.__head
        while node:
            string += str(node.data)
            if node.next_node:
                string += "\n"
            node = node.next_node
        return string

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node and value >= node.next_node.data:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
