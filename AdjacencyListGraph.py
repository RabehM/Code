from Edge import Edge
from DirectedGraph import DirectedGraph
from AdjacencyListVertex import AdjacencyListVertex


class AdjacencyListGraph(DirectedGraph):
    def __init__(self):
        self.vertices = []

    # Creates and adds a new vertex to the graph, provided a vertex with the
    # same label doesn't already exist in the graph. Returns the new vertex on
    # success, None on failure.
    def add_vertex(self, new_vertex_label):
        # Your code here (remove placeholder line below)
        pass

    # Adds a directed edge from the first to the second vertex. If the edge
    # already exists in the graph, no change is made and False is returned.
    # Otherwise the new edge is added and True is returned.
    def add_directed_edge(self, from_vertex, to_vertex):
        # Your code here (remove placeholder line below)
        pass

    # Returns a list of edges with the specified from_vertex.
    def get_edges_from(self, from_vertex):
        # Your code here (remove placeholder line below)
        pass

    # Returns a list of edges with the specified to_vertex.
    def get_edges_to(self, to_vertex):
        # Your code here (remove placeholder line below)
        pass

    # Returns a vertex with a matching label, or None if no such vertex exists
    def get_vertex(self, vertex_label):
        # Your code here (remove placeholder line below)
        pass

    # Returns True if self graph has an edge from from_vertex to to_vertex
    def has_edge(self, from_vertex, to_vertex):
        # Your code here (remove placeholder line below)
        pass
