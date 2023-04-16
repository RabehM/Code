from Vertex import Vertex

class AdjacencyListVertex(Vertex):
    # List of vertices adjacent to this vertex. For each vertex V in this list, V is
    # adjacent to this vertex, meaning an edge from this vertex to V exists in the graph.
    def __init__(self, label):
        super().__init__(label)
        self.adjacent = []
