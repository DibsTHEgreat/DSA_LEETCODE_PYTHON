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
    
    # append function
    def append(self, value):
        new_node = Node(value)
        # if the list is empty and you are adding a node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # connecting the DLL to new node
            self.tail.next = new_node
            # connecting new node to DLL
            new_node.prev = self.tail
            # moving tail pointer to last node
            self.tail = new_node
        self.length += 1
        # we need to return True so the insert function can properly return a boolean
        return True
    
    # pop function
    def pop(self):
        # if list is empty
        if self.length == 0:
            return None
        # helper variable
        temp = self.tail
        # if list only has one item
        if self.length == 1:
            self.head = None
            self.tail = None
        else: # if list has 2 or more items
            # move tail back to second last node
            self.tail = self.tail.prev
            # new tail will now be set to point to none
            self.tail.next = None
            # now we disconnect the last node from the DLLs
            temp.prev = None
        self.length -= 1            
        return temp
        
    

# creating a DLL
my_doubly_linked_list = DoublyLinkedList(1)

print("Testing out DLL Constructor:")
my_doubly_linked_list.print_list()

print("")
print("Testing out append functionality by adding node 2:")
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()

print("")
print("Testing out pop functionality by removing node 2:")
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
