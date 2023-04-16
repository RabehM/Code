from Vertex import Vertex

class Edge:
    def __init__(self, from_vertex, to_vertex):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex

    def equals(self, other):
        return (self.from_vertex == other.from_vertex and
                self.to_vertex == other.to_vertex)

    # Prints self edge in the form "A to B", where "A" is the from_vertex's label
    # and "B" is the to_vertex's label.
    def print(self, output):
        self.from_vertex.print(output)
        print(" to ", file=output, end='')
        self.to_vertex.print(output)
