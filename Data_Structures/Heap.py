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