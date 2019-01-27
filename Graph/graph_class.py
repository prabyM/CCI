"""
This class defines the node of a graph
"""

class Vertex:

    """
    Function to create a new node.
    """

    def __init__(self, key):
        self.neighbors = []
        self.key = key

    """
    Function to add a new vertex
    """

    def add_neighbor(self,neighbor_vertex,weight):
        self.neighbors.append(( neighbor_vertex, weight))

    """
    Function to get connections from a graph.
    """

    def get_connections(self):
        return self.neighbors

    def get_weight(self, to_vertex):
        for neighbors in self.neighbors:
            if neighbors[0] == to_vertex:

                return neighbors[1]




"""
Usage:
v = Vertex("a")
v.add_neighbor("b",8)
print "Neighbor added"
v.add_neighbor("f",9)
print "Neighbor added"
print(v.get_connections())
print(v.get_weight("b"))

"""

"""
Below class defines a graph.
"""

class graph:

    """
    Initialize a blank graph using a dictionary
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        v = Vertex(vertex)
        """
        We created a node and added that node as  a part of the graph.
        """
        self.vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].add_neighbor(self.vertices[to_vertex],weight)

    """
    The below function gets all the vertices of a graph.
    """

    def get_vertices(self):
        vertices = self.vertices.keys()
        vertices.sort()
        return vertices

"""
Below example shows the usage of the function.
g =graph()
g.add_vertex("b")
g.add_edge("a", "b", 7)
print (g.get_vertices())

"""
