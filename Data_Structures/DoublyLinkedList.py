# This file contains my observations and notes about Doubly Linked Lists
# I have also created my own Doubly Linked List Class to understand the DS


# Observations

# it is the same as a linked list however, now all the nodes also point to the previous node
# instead of it being a one-way connection (LL) now it is a two-way connection (DLL)
#                  head                   tail
#                   |                       |
#   None (null) <- (1) <-> (2) <-> (3) <-> (4) <-> None (null)

# Helper class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # main difference between LL and DLL is that now we have a arrow pointing the other way
        self.prev = None

# Class for DLL
class DoublyLinkedList:
    # As you can see the constructor is the same as LL
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # print function
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# creating a DLL
my_doubly_linked_list = DoublyLinkedList(1)

print("Testing out DLL Constructor:")
my_doubly_linked_list.print_list()