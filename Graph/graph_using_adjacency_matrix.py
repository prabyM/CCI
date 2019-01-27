"""
This program explains using adjacency matrix to depict a graph.
"""

graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]
"""
This function finds the vertices of the graph.
"""


def find_vertices():

    return [chr(x + ord('a')) for x in range(len(graph))]


"""
This function finds the edges of the graph.
"""

def find_edges():
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0:
                edges.append((chr(i+ord('a')), chr(j+ord('a')), graph[i][j]))

    return edges


print find_vertices()
print find_edges()

