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

# An adjacency matrix is a square matrix used to represent a finite graph.
# The rows and columns of the matrix represent vertices. The value at position [i][j] 
# tells you if there's an edge between vertex i and vertex j.
# For example:
#    (A) — (B)
#     |
#    (C)
# Adjacency matrix:
#     A B C <-- This axis represents an items it has an edge with.
#   A 0 1 1
#   B 1 0 0
#   C 1 0 0
#   ^
#   This axis represents the actual vertex
# 0 = means no edge
# 1 = means there is an edge
# Note: The example above represents a bi-directional graph. As in A points to B and B points to A.
# If the graph was not bi-directional, than there would not be a point for A-B and B-A.
# Also, if the graph is weighted, than you would store those values in the matrix and present it as 0 or x.

# An adjacency list is another way to represent a graph, and it’s especially efficient for sparse graphs.
# Instead of a big matrix, we use a list (or dictionary/map) where each vertex stores a list of its neighbors 
# (the vertices it's connected to).
# For example using the same graph as before:
#    (A) — (B)
#     |
#    (C)
# We would show the adjacency list as:
#{
#  A: [B, C],
#  B: [A],
#  C: [A]
#}
