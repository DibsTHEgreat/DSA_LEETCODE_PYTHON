# This file contains my observations and notes about Hash Table
# I have also created my own Hash Table Class to understand the DS

# Observations
# For graphs, each node is usually referred to as a vertex. Between multiple vertices is 
# a connection or better known as a edge.
#
#               (82) <-- Vertex
#               / |
#             /   | <-- Edge
#  4 -->    /     | <-- 15 <-- weighted edge
#         /       |
#      (44) --- (76)
#            ^
#            |
#            5 <-- weighted edge
# Suppose you wanted to from vertex 76 to 82, it doesn't make sense to go around vertex 44 when
# you can go directly to vertex 82. However, with graphs, there is an important distinction,
# which is weighted edges. (This doesn't always happen, however, it is something important to consider)
# For example, on any maps app, traffic could be considered the weighted edge value. The app
# will pick the route with the least amount of traffic (lowest values per edge).
# Network routing protocols, it would be better to have an extra router hop and have two very
# fast links, then to go the way with the very slow link.
# Important to remember, edges can we weighted or not wighted.
# Another important concept about graphs are relationships between vertexes. For example,
# (YOU) <--> (FRIEND)
# You are friends with your friend and vice versa. This would be a bidirectional relationship.
# In a graph where all the edges are bidirectional, you'll often see it without arrows.
# Another example could be when you follow a celebrity on Instagram. Most likely, they don't 
# follow you back. This is a directional relationship.
# Trees are another form of graphs, but they have the limitation that each node can only point
# to two other nodes. If you want to continue down this rabbit hole, Linked Lists are a form
# of a tree, and a tree is a form of a graph. Therefore, a linked list is a form of a graph
# with the limitation that they can only point to one other node.