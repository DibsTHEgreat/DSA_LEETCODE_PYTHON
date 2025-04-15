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

# Big 0 Notation about BST:
# The # of nodes within this tree is one: (47), we can represent this as: 2^1 - 1 = 1 node.
# Now suppose our tree has a second level.
#                   (47) 
#                  /    \
#                (21)  (76)
# We represent this as 2^2 - 1 = 3 nodes. As the levels continue to progress we had +1 to the power (suppose we label it as n) of 2.
# Overtime as n approaches infinity, the - 1 becomes insignificant. Thus for each level, it's better to drop the constant, and
# approximate our calculation by saying 2^n for each level. 
# When you want to find a node, or remove a node, or add, it all depends on the value of n. For example, if you want to remove a node
# at the very bottom it will take you n steps (levels) to get to that node and than remove the value. Same applies for finding and adding.
# Thus, we can say that the big O for all of these operations is O(log n). Why O(log n) and not O(n)? We are dividing our search parameter
# hence the O(log n) this is divide and conquer.
#                   (47) 
#                  /    \
#                (21)  (76)
#                / \    / \
#            (9) (22) (56) (78)
# For example if we wanted to look for the node 78, we would divide our search parameter by only looking on the right side. Than
# we continue from there, and ignore 56 since 78 is greater than 76. This is O(log n) time complexity. When you think about it,
# imagine if there actually was 5 million nodes. By removing one half of a tree, you are removing 2.5 million nodes, greatly
# reducing the search parameter and increasing efficiency.
# Worst case scenario, you have an instance where all the nodes in the tree are greater than each other, thus resulting in a long list
# (8) -> (9) -> (17) -> (45) -> (88)
# Thus, each operation will take you n levels at a time (at this point it's a Linked List). Which means technically the Big O for a BST is O(n).
# What we assume with a BST is that it's not going to be a straight line of those greater than conditions passing true. We won't have that
# worst case scenario, making us treat the BST as if it is O(log n).
# Thus, for these functions:
# lookup() - O(log n)
# insert() - O(log n)
# remove() - O(log n)
# When comparing this with a LL, we observe that:
# lookup() - O(n) --> since we are iterating through a list; thus a BST is better than a LL in terms of looking up nodes
# remove() - O(n) --> since we are iterating through a list to remove a value this is also O(n) thus a BST is better than a LL in this situation
# insert() - O(1) --> when adding a node you would append it to the end, thus, this act is O(1), which is better than BST
# A LL is better for inputting a burst of data into the DS, there is no other ds that is the best answer in all situations.
# As you can see, BST has some advantages, and LL also has it advantage. Hence why it is important to understand the big O of all operations.

# Helper Class
# Since we are dealing with tree nodes there will be a left and right pointer.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        # initializing a BST
        self.root = None
        
# Logic behind inserting a node into a BST
# First we would have to create a new_node
# There are some edge cases to consider, for example what if the tree is empty
    # if root == none then root = new_node
# we need to compare the value of the new_node with the root
# We need to declare temp before we iterate through the tree. temp = self.root
# while loop:
    # if new_node == temp return false
    # if: the new_node is less than root go left
    # else: the new_node is greater than root go right
    # On the next level:
    # if there is no node, simply insert the new node
    # else if there is a node, compare and move to the next level
# As you can see, the if else statement is used on each level, 
# thus, we need to create a while loop so there is no need to repeat code.
    def insert(self, value):
        new_node = Node(value)
        # if tree is empty
        if self.root == None:
            self.root = new_node
            return True
        # creating helper variable
        temp = self.root
        while (True):
            # cannot enter duplicates into the tree
            if new_node.value == temp.value:
                return False
            # if new node is less than temp value move left
            if new_node.value < temp.value:
                # if there is no left child node
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: # if new node is greater than temp value move right
                # if there is no left child node
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

# logic behind finding a value within the tree
# edge case: empty tree
    # if root == None return false
# temp = self.root
# while temp is not None
    # there are three scenarios
    # if temp is less than go left
    # else if temp is greater than go right
    # else = return True
# return False
    def contains(self, value):
        # if tree is empty
        #    if self.root == None:
        #        return False
        # Since our while loop only runs when temp is not none, the code above is redundant
        # creating temp variable
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: # item is equal
                return True
        # item is not in the tree
        return False
    
my_tree = BinarySearchTree()

print("Testing out basic constructor:")
print(my_tree.root)

print("")
print("Testing out Insert Function for BST by inserting node 2 as the root.")
my_tree.insert(2)
print(my_tree.root.value)

print("")
print("Testing out Insert Function for BST by inserting node 1 to the left")
my_tree.insert(1)
print(my_tree.root.left.value)

print("")
print("Testing out Insert Function for BST by inserting node 3 to the right")
my_tree.insert(3)
print(my_tree.root.right.value)

my_tree.insert(12)
my_tree.insert(4)

print("")
print("Testing out Contains Function by checking for if 4 is in the tree")
print(my_tree.contains(3))

print("")
print("Testing out Contains Function by checking for if 17 is in the tree")
print(my_tree.contains(17))