#!/usr/bin/python3
"""Module 100-singly_linked_list: Singly linked list"""


class Node:
    """Representation of a list node"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, data):
        """Property setter to set data"""
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Property to retrieve next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter to set next_node"""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representation of a singly linked list"""

    def __init__(self):
        """Simple instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """Method that inserts a Node into the correct sorted position"""
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
        elif self.__head.data > value:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None:
                if tmp.next_node.data > value:
                    new_node = Node(value, tmp.next_node)
                    tmp.next_node = new_node
                    return
                tmp = tmp.next_node
            if tmp.next_node is None:
                new_node = Node(value)
                tmp.next_node = new_node

    def __str__(self):
        """Custom __str__ method to print the entire list in stdout"""
        tmp = self.__head
        letter = ""
        while tmp is not None:
            if tmp.next_node is None:
                letter += str(tmp.data)
            else:
                letter += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return letter
