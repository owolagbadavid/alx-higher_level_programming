#!/usr/bin/python3
"""Node class definition"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None) -> None:
        """Sets up a new node.
        Args:
            data (int): data stored inside the node
            next_node (Node): next node in the singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """Gets the data stored inside the node.
        Returns:
            int: data stored inside the node
        """
        return self.__data
    
    @data.setter
    def data(self, value: int) -> None:
        """Sets the data stored inside the node.
        Args:
            value (int): data stored inside the node
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the singly linked list.
        Returns:
            Node: next node in the singly linked list
        """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value) -> None:
        """Sets the next node in the singly linked list.
        Args:
            value (Node): next node in the singly linked list
        Returns:
            None
        """
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList():
    """Defines a singly linked list."""

    def __init__(self) -> None:
        """Sets up a new singly linked list."""
        self.__head = None

    def __str__(self) -> str:
        """Returns a string representation of the singly linked list.
        Returns:
            str: string representation of the singly linked list
        """
        string = ""
        node = self.__head
        while node:
            string += str(node.data)
            if node.next_node:
                string += "\n"
            node = node.next_node
        return string
    
    def sorted_insert(self, value: int) -> None:
        """Inserts a new node into the singly linked list.
        The singly linked list is sorted in ascending order.
        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """
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