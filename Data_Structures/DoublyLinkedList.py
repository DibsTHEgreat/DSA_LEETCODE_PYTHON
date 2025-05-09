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
    
    # prepend function
    def prepend(self, value):
        new_node = Node(value)
        # no items in DLLs
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else: # DLL with items in it
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # pop_first function
    def pop_first(self):
        # DLL is empty edge case
        if self.length == 0:
            return None
        # creating helper variable
        temp = self.head
        # DLL is only 1 node
        if self.length == 1:
            self.head = None
            self.tail = None
        else: # DLL is 2 or more nodes big
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # get function
    def get(self, index):
        # validating index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # we only want to do this for loop if our index is within the first half of the list 
        if index < self.length / 2:
            for _ in range(index):
                temp =  temp.next
        else: # if it's in the second half of the list
            temp =  self.tail
            # within this range function we can specify: where we want to start (self.length - 1), index specifies where we want to stop,decrement by 1
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # set_value function
    def set_value(self, index, value):
        temp = self.get(index)
        # if temp exists
        if temp is not None:
            temp.value = value
            return True
        return False        
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        # if index is the first node
        if index == 0:
            return self.prepend(value)
        # if the index is the last node
        if index == self.length:
            return self.append(value)
        # creating a new node
        new_node = Node(value)
        # the get method is O(N)
        before = self.get(index - 1)
        # assigning via this way is O(1)
        after = before.next
        # connecting new node to the main list
        new_node.prev = before
        new_node = after
        # connecting the nodes to new node
        before.next = new_node
        after.prev = new_node
        # increasing length 
        self.length += 1
        return True
    
    def remove(self, index):
        # if index is invalid
        if index < 0 or index >= self.length:
            return None
        # if index is for the first node
        if index == 0:
            return self.pop_first()
        # if index is the last node:
        if index == self.length - 1:
            return self.pop()
        # assigning target node to temp
        temp = self.get(index)
        # assigning the previous pointer from the next node to the previous node of temp from the context of temp
        temp.next.prev = temp.prev
        # assigning the next pointer from the previous node to the next node of temp from the context of temp
        temp.prev.next = temp.next
        # removing temp from list
        temp.next = None
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

print("")
print("Testing out preprend functionality by adding node 2 to the front:")
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.print_list()

print("")
print("Testing out pop_first functionality by removing the first node:")
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()

print("")
print("Testing out get functionality:")
my_doubly_linked_list.get(1)
my_doubly_linked_list.print_list()

print("")
print("Testing out set_value functionality by changing the first node value from 1 to a 2:")
my_doubly_linked_list.set_value(0, 2)
my_doubly_linked_list.print_list()

print("")
print("Testing out insert functionality by adding a new node:")
my_doubly_linked_list.insert(1, 3)
my_doubly_linked_list.print_list()

print("")
print("Testing out remove functionality by removing second node:")
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()