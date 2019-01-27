"""
This is a basic demonstration of Graph data structures.Graph can be denoted using dictionary.
"""

graph = {
    "a" : [("b", 7), ("c", 9), ("f", 14)],
    "b" : [("a", 7), ("c", 10), ("d", 15)],
    "c" : [("a", 9), ("b", 10), ("d", 11), ("f", 2)],
    "d" : [("b", 15), ("c", 11), ("e", 6)],
    "e" : [("d", 6), ("f", 9)]


}

"""
Below function returns the vertices of a graph.
"""


def get_vertices():

    return graph.keys()

"""
Below function returns the edges of the graphs along with Cost
"""


def find_edges():
    edges = []
    for vertices in graph:
        for connected_nodes in graph[vertices]:
            edges.append((vertices, connected_nodes[0], connected_nodes[1]))

    return edges

