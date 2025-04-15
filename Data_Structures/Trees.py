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