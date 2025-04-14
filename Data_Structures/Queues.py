# This file contains my observations and notes about Queues
# I have also created my own Queue Class to understand the DS

# Observations
# A good way to think of a queue is like a line, first person in the line gets attended to. This also means Queue operates as
# FIFO (First-in, first-out). When we add items to the queue, we say inqueue, and when we remove items from the list we say dequeue.
# You can use many data structures as a queue. For example with a list, when you remove/add an item from the end is time complexity of O(1).
# But on the other end (beginning of list), removing and adding is O(n).
# when comparing lists to a linked list, we see that removing an item from a LL is O(n), but adding it back on is O(1). On the other end,
# removing a node is O(1), and adding a node is O(1). 
# In order to optimize our strategy, we will add an item at the end of the list O(1), and remove an item from the beginning of the list 
# which is O(1) also. We do this to avoid O(n) time complexity.

# Helper class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Queue Class
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

# creating a Queue
my_queue = Queue(1)
my_queue.print_queue()