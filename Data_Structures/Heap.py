# This file contains my observations and notes about Heaps
# I have also created my own Heaps Class to understand the DS

# Observations
# A heap is a binary tree, very similar to a binary search tree; however, numbers are not distributed in the same way.
# With a heap, each node has a number that is higher than all of its descendants, which means the highest value will
# always be at the top.
# For example:
#              (99)
#             /      \ 
#           (72)     (61)
#           /\       /  \
#       (58) (55)  (27) (18)
# A key characteristic of a heap is that it is a complete tree, which means there are no gaps from left to right, all levels are complete.
# The height of a perfect tree, when it looks like the example given, is log(n)