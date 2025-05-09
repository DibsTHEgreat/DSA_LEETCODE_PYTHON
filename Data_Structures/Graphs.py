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

# A huge difference between an adjacency list and adjacency matrix is that in a matrix each vertex has to store
# all of the vertices it is not connected to. For example: A: 0 0 1 0 1. Thus, from a space complexity stand-point
# the adjacency matrix is the # of vertices squared, whereas, the adjacency list is the # of vertices + the # of edges.
# Adjacency Matrix: O(|V|^2)
# Adjacency List: O(|V| + |E|)
# What is the big O for adding a vertex?
# With an adjacency list adding a vertex is quite simple. Thus the operation is O(1)
#{
#  A: [B, C],
#  B: [A],
#  C: [A]
#  D: [] <-- New Vertex
#}
# With an adjacency matrix this operation is much more complex. Since now you will have to take into account all vertices
# including inputting data for vertices that don't point at a new node.
#     A B C D
#   A 0 1 1 0
#   B 1 0 0 0
#   C 1 0 0 0
#   D 0 0 0 0
# As you can see this would result in a O(|V|^2) time complexity.
# Adding an edge to an adjaceny list is quite similar to adding a vertex. It's as simple as appending a value to a list.
# Adding an edge to an adjaceny matrix is actually less complex as compared to adding a vertex. Now that all the values are
# set to 0, all you have to do is set the value of 0 to 1 for where-ever the edge needs to be established. 
# Both of these operations are O(1).
# Removing an edge between two vertices is also important to understand.
# When you are removing a relationship between two vertices in an adjacency list, you have to iterate through the list of edges 
# that is connected with the edge you want to remove. Hence the time complexity is O(|E|).
# When you are removing an edge from a adjacency matrix the process is quite simple and very similar to adding an edge, hence it is 0(1).
# When removing a vertex from a adjaceny list we have to iterate through all dictionaries to find for possible edges.  Whereas,
# with a matrix all you have to do is remove the column/row for that specific vertex.
# Thus, for this instance: 
# Adjacency Matrix: O(|V|^2)
# Adjacency List: O(|V| + |E|)

class Graph:
    def __init__(self):
        # creating a dictionary
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        # we don't want duplicate keys within the adjacency list
        if vertex not in self.adj_list.keys():            
            # Adding the vertex as a key into the adjacency list and set it equal to an empty list
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        # Need to ensure we are adding an edge for 2 existing vertices.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # to connect these two vertices, by appending v2 to v1
            self.adj_list[v1].append(v2)
            # to connect these two vertices, by appending v1 to v2
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        # we can only remove the edge if the vertices exist
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                # removing the edges
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        # ensure that the vertex exists
        if vertex in self.adj_list.keys():
            # What we are doing here is finding the row of other_vertex from the given vertex
            # From there, we will remove the given vertex from the row of other_vertex
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            # Once we have removed all instances of vertex from the rows we can remove the entire main vertex row itself
            del self.adj_list[vertex]
            return True
        return False
                
       
my_graph = Graph()

my_graph.add_vertex('A')

print("Testing out constructor and add vertex functionality for Graph Class:")
my_graph.print_graph()

print('')
print("Adding Vertex B, C, and D into the graph:")
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.print_graph()

print('')
print("Testing out add edge functionality for Graph Class:")
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')
my_graph.print_graph()

print('')
print("Testing out remove edge functionality for Graph Class:")
my_graph.remove_edge('A', 'B')
my_graph.print_graph()

print('')
print("Testing out remove vertex functionality for Graph Class by removing Vertex A:")
my_graph.remove_vertex('A')
my_graph.print_graph()