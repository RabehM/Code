from abc import ABC, abstractmethod

# class for a directed, unweighted graph
class DirectedGraph:
    # Creates and adds a new vertex to the graph, provided a vertex with the
    # same label doesn't already exist in the graph. Returns the new vertex on
    # success, None on failure.
    def add_vertex(self, new_vertex_label):
        self.new_vertex_label = new_vertex_label

    # Adds a directed edge from the first to the second vertex. No changed is made
    # and false is returned if the edge already exists in the graph. Otherwise the
    # new edge is added and True is returned.
    @abstractmethod
    def add_directed_edge(self, from_vertex, to_vertex):
        pass

    # Returns a list of edges with the specified from_vertex.
    @abstractmethod
    def get_edges_from(from_vertex):
        pass

    # Returns a list of edges with the specified to_vertex
    @abstractmethod
    def get_edges_to(to_vertex):
        pass

    # Returns a vertex with a matching label, or None if no such vertex exists
    @abstractmethod
    def get_vertex(self, vertex_label):
        pass

    # Returns True if this graph has an edge from from_vertex to to_vertex, False otherwise
    @abstractmethod
    def has_edge(self, from_vertex, to_vertex):
        pass
