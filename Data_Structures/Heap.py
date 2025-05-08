# This file contains my observations and notes about Heaps
# I have also created my own Heaps Class to understand the DS

# Observations
# A heap is a binary tree, very similar to a binary search tree; however, numbers are not distributed in the same way.
# With a heap, each node has a number that is higher than all of its descendants, which means the highest value will
# always be at the top.
# For example:
#               (99)
#             /      \ 
#           (72)     (61)
#           / \      /  \
#       (58) (55)  (27) (18)
# A key characteristic of a heap is that it is a complete tree, which means there are no gaps from left to right, all levels are complete.
# The height of a perfect tree, when it looks like the example given, is log(n).
# Another key characteristic about heaps is that you can have duplicates. For example, Node 72 could also be 99 (while the parent is also node 99).
# The diagram above is called a Max-Heap (highest value at the top), you can also have a min-heap, where it is the minimum value at the top.
# For example:
#               (18)
#             /      \ 
#           (27)     (61)
#           / \      /  \
#       (58) (55)  (72) (99)
# For any node in this tree, all of the decendants are greater than or equal the value of the parent node.
# Besides that, there is no guarentee in the order of the heap. For example, going back to the max heap:
# For example:
#               (99)
#             /      \ 
#           (72)     (61)
#           / \      /  \
#       (58) (55)  (27) (18)
# We could technically swap Node 61 and 72.
# For example:
#               (99)
#             /      \ 
#           (61)     (72)
#           / \      /  \
#       (58) (55)  (27) (18)
# You can also swap 61 and 55 (from the original max-heap):
# For example:
#               (99)
#             /      \ 
#           (72)     (55)
#           / \      /  \
#       (58) (61)  (27) (18)
# There is no particular order, other than all of the decendants are going to be less than or equal to the parent.
# Heaps are not for searching, the only thing you use a heap for is being able to keep track of the largest item at the top, and be able
# to quickly remove it.
# There is also a huge difference in how we store a heap vs a BST. A Heap will be stored in a list, however, we will not create a node class.
# The only thing the list stores is integers. Value of the root will go to index 0, than line by line we add them into the index.
# For example:
#               (99)
#             /      \ 
#           (72)     (61)
#           / \      /  \
#       (58) (55)  (27) (18)
# Will be shown as: 99 | 72 | 61 | 58 | 55 | 27 | 18
#                    0 |  1 |  2 |  3 |  4 |  5 |  6
# It is also common to see heaps where the first index is the index of one.
# Will be shown as:  X | 99 | 72 | 61 | 58 | 55 | 27 | 18
#                    0 |  1 |  2 |  3 |  4 |  5 |  6 |  7
# This is why it is so important for the tree to be complete, because gaps in the tree will cause missing values in the list.
# If you wanted to find the childern of the root node, startign with the left_child the equation would be: 2 * parent_index which is 2 -> 72.
# The right child would be 2 * parent_index + 1 = 3 --> 61. Math becomes easy when you leave the index spot of 0 open.

# Logic behind inserting values into a HEAP.
# Example Max-heap: Need to Insert Node 100.
#               (99)
#             /      \ 
#           (72)     (61)
#           /
#       (58)
# We have to start inserting a value by inserting it into the next open space.
# For example:
#               (99)
#             /      \ 
#           (72)     (61)
#           /  \
#       (58)   (100)
# The reason for this is because we need to ensure that the tree remains complete. Now compare Node 100 to its parent, since 100 is greater than 72
# we switch the nodes.
# For example:
#               (99)
#             /      \ 
#           (100)     (61)
#           /  \
#       (58)   (72)
# Then we compare it against its parent again:
# For example:
#               (100)
#             /      \ 
#           (99)     (61)
#           /  \
#       (58)   (72)
# We will move this up using a while loop, and there will be two conditionals that can break us out of the while loop. The first one is if
# we reach the top of the heap, for example, once Node 100 gets to the root we want to stop running the while loop. There is another condition
# we want to consider which is when you insert a node and it doesn't reach the top because it fails the greater than check. 
# For example inserting node 75:
#               (99)
#             /      \ 
#           (72)     (61)
#           /  \
#       (58)   (100)
# When looking at this logic from a list point of view we noticed that we'll have to use those equations again.
# Going back to the original example of inserting Node 100.
# Will be shown as:  X | 99 | 72 | 61 | 58 | 100
#                    0 |  1 |  2 |  3 |  4 |  5
# What we have to do is divide the index of 5 by 2 which is 2.5, this becomes 2 since we are doing integer division.
# Hence we now have the index location of the parent node to compare with.
# Will be shown as:  X | 99 | 100 | 61 | 58 | 72
#                    0 |  1 |  2 |  3 |  4 |  5
# Then we compare one more time:
# Will be shown as:  X |100 | 99 | 61 | 58 | 72
#                    0 |  1 |  2 |  3 |  4 |  5

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    # Starting at Node 0 instead of node 1 hence the plus 1
    def _left_child(self, index):
        return 2 * index + 1
    
    # Starting at Node 0 instead of node 1 hence the plus 2
    def _right_child(self, index):
        return 2 * index + 2
    
    # Doing integer division
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def insert(self, value):
        # adding the new value to the end of the list
        self.heap.append(value)
        # current is equal to the index value of the last node
        current = len(self.heap) - 1
        # If current is ever equal to 0 than that means current is at the root, and there is no need to continue the loop
        # We also want to run the loop if the value of current is greater than parent if not end loop
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # swapping new value with parent
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    # helper function for remove function
    def _sink_down(self, index):
        # points to the root node
        max_index = index
        while True:
            # Grabbing the child nodes
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # Comparing the max node with the left node
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            # Comparing the max node with the right node
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            # swap values as the main node traverses down
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    
    # only need to remove item from the top (doesn't matter if it is a min-heap or a max-heap)
    def remove(self):
        # if the heap is empty
        if len(self.heap) == 0:
            return None
        # only one item in the heap
        if len(self.heap) == 1:
            return self.heap.pop()
        # assigning root value to a variable
        max_value = self.heap[0]
        # now we move the last value to where the root is (and start the sink down process)
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

my_heap = MaxHeap()

print("Printing Heap Table after adding some values:")
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
print(my_heap.heap)

print("Testing remove functionality by removing a node:")
my_heap.remove()
print(my_heap.heap)