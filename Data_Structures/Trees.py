# This file contains my observations and notes about Trees
# I have also created my own Trees Class to understand the DS

# Observations
# Each node in a Binary tree will have a value of left and right
#               o
#       left  /   \ right
#            o     o
#           /\
#          o o
# The Binary tree you see above is called a Full tree. In a full-tree, every node either points to 0 nodes or two nodes.
#               o
#       left  /   \ right
#            o     o
#           /
#          o 
# For example something like that above, would not be considered a full tree because there is a node that only points to one node.
#               o
#       left  /   \ right
#            o     o
# The Binary tree above is called a perfect tree (still also a full tree) because with these types of trees any level that has nodes is completely
# filled all the way across.
#               o
#       left  /   \ right
#            o     o
#           /\    /\
#          o o   o  o
# This would also be a perfect tree, since all levels within this tree are completely filled. Besides that, a perfect tree is also complete.
#               o
#       left  /   \ right
#            o     o
#           /\    
#          o o  
# This would not be considered a perfect tree (still full).
#               o
#       left  /   \ right
#            o     o
#           /\    /\
#          o o   o  o
# Going back to the term complete. With a complete tree, you are filling the tree from left to right with no gaps.
#               o
#       left  /   \ right
#            o     o
#           /
#          o 
# For example the Binary tree above is: (-) full, (-) perfect, (X) complete. It is still complete since we are filling the tree from left to right
# with no gaps.
#               o
#       left  /   \ right
#            o     o
#           / \
#          o   o
# By adding one more node to the Binary tree above: (X) full, (-) perfect, (X) complete. It remains complete, but it is now also Full.
#               o
#       left  /   \ right
#            o     o
#           / \   / \
#          o   o o   o
# By completing the Binary tree above: (X) full, (X) perfect, (X) complete, we now also have a perfect tree.
# Some other terms to consider is:
#               o <-- Parent
#             /   \
#            o     o <-- Child
#           / \   / \
#          o   o o   o
# Since two nodes share the same parent, those two nodes can also be considered siblings. Every node can only have one parent.

# What is a binary search tree?
# With a binary search tree, if you are to add a node, the number of the node will determine the placement. For example,
# if the number is greater than the parent it goes onto the right, if the number is less than the parent it goes on the left.\
#                   (47)
#                       \
#                       (76)
# For example, if we were to add Node 52 to the BST, we would have to do this:
#                   (47) <-- Start by comparing with the top node, since 52 is greater than 47 we go to the right side
#                       \
#                       (76) <-- Since there is already a node here, we compare the 52 to the 76. Since 52 < 76, we put 52 on the left side.
#                       /
#                     (52)
# For example, if we were to add Node 21 to the BST, we would have to do this:
#                   (47) <-- Start by comparing with the top node, since 21 is less than 47 we go to the left side
#                  /    \
#                (21)  (76)
#                       /
#                     (52)
# For example, if we were to add Node 82 to the BST, we would have to do this:
#                   (47) <-- Start by comparing with the top node, since 82 is greater than 47 we go to the right side
#                  /    \
#                (21)  (76) <-- Now we compare 76 to the new node 82, since 82 is greater than 76 we go to the right side
#                       /  \
#                     (52) (82)
# Some things to point out in the BST:
# If you take any node in the BST, all nodes below the main node (or any given node) on the right side are going to be
# greater than the chosen node. Likewise applies for when all nodes below the main node on the left side will be
# less than the chosen node.

