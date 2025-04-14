# This file contains my observations and notes about Stacks
# I have also created my own Stack Class to understand the DS

# Observations
# Think of Stack as a can of tennis balls. You can add one ball into the can (this is known as pushing an item onto the stack)
#       | o |
#       | o |
#       | o |
#         -
# Stacks follow LIFO (last-in, first-out) methodology, as in, as soon as you push an item onto the stack, you cannot access the first tennis ball
# without first removing the second ball. Same applies for the second tennis ball, you cannot access the second tennis ball
# without first removing the third ball. The only ball we can get to is the one that is on top.

# For something to be a stack, you just have to add and remove from the same end. That means if you are going to be using a list as a stack,
# you want to add/remove from the end of the list, ensuring that there is no need to reindex which means the time complexity will be O(1)

# The nodes I am using will be identical to the LL nodes
# Here is the helper class for the stack class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    # main constructor for stack
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

# creating a DLL
my_stack = Stack(1)

print("Testing out DLL Constructor:")
my_stack.print_stack()