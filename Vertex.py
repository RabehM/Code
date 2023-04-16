class Vertex:
    def __init__(self, vertex_label):
        self.vertex_label = vertex_label

    def set_label(self, new_label):
        self.vertex_label = new_label

    def get_label(self, ):
        return self.vertex_label

    # Prints self vertex's label
    def print(self, output):
        print(self.vertex_label, file=output, end='')
