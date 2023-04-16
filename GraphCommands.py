class DirectedGraphTestCommand:
    # Returns True if the test passes, else False
    def execute(self, test_feedback, graph):
        pass

    # Utility function that checks if a particular edge is in the list of edges
    def has_edge(self, edges, from_vertex, to_vertex):
        # Iterate through the list's edges
        for edge in edges:
            if edge.from_vertex == from_vertex and edge.to_vertex == to_vertex:
                return True

        return False

    def print_edges(self,
                    output,
                    edges,
                    separator = ",",
                    prefix = "[",
                    suffix = "]"):
        # Print the prefix first
        print(prefix, file=output, end='')

        # Print edges
        if len(edges):
            edges[0].print(output)
            for edge in edges[1:]:
                print(end=separator, file=output)
                edge.print(output)

        # Print suffix string
        print(end=suffix, file=output)

class AddVertexCommand(DirectedGraphTestCommand):
    def __init__(self, vertex_label, should_succeed):
        self.vertex_label = vertex_label
        self.should_succeed = should_succeed

    def execute(self, test_feedback, graph):
        # Try to add the vertex. Return True if the addition is successful else False
        new_vertex = graph.add_vertex(self.vertex_label)

        if new_vertex:
            if not self.should_succeed:
                print(f'''FAIL: add_vertex("{self.vertex_label}") \
should have returned None due to the label already being in use''',
                      file=test_feedback)
                return False

            print(f'''PASS: add_vertex("{self.vertex_label}") returned a vertex''',
                  sep='',
                  file=test_feedback)
            return True

        if self.should_succeed:
            print(f'''FAIL: add_vertex("{self.vertex_label}") incorrectly returned None''',
                  file=test_feedback)
            return False

        print(f'''PASS: add_vertex("{self.vertex_label}") returned None because the label is already in use''',
              sep='',
              file=test_feedback)
        return True

class GetVertexCommand(DirectedGraphTestCommand):
    def __init__(self, vertex_label, vertex_should_exist):
        self.vertex_label = vertex_label
        self.vertex_should_exist = vertex_should_exist

    def execute(self, test_feedback, graph):
        # Get the vertex with the specified label
        vertex = graph.get_vertex(self.vertex_label)

        # Check if get_vertex has returned None
        if vertex:
            # If the vertex shouldn't exist, then print a failure message
            if not self.vertex_should_exist:
                print(f'''FAIL: get_vertex("{self.vertex_label}") should have returned None''',
                      file=test_feedback)
                return False

            # Verify the vertex's label
            actual_label = vertex.get_label()
            if self.vertex_label != actual_label:
                print(f'''FAIL: get_vertex("{self.vertex_label}") returned a vertex with
incorrect label "{actual_label}"''',
                      file=test_feedback)
                return False

            print(f'''PASS: get_vertex("{self.vertex_label}") returned a vertex with a correct label''',
                  sep='',
                  file=test_feedback)
            return True

        # No vertex is returned, so check if a vertex is expected
        if self.vertex_should_exist:
            print(f'''FAIL: get_vertex("{self.vertex_label}") returned None, but
should have returned a vertex''',
                  file=test_feedback)
            return False

        # PASS
        print(f'''PASS: get_vertex("{self.vertex_label}") returned None''',
              sep='',
              file=test_feedback)
        return True

class AddEdgeCommand(DirectedGraphTestCommand):
    def __init__(self, from_vertex_label, to_vertex_label, should_succeed):
        self.from_vertex_label = from_vertex_label
        self.to_vertex_label = to_vertex_label
        self.should_succeed = should_succeed

    def execute(self, test_feedback, graph):
        # Find both vertices
        from_vertex = graph.get_vertex(self.from_vertex_label)
        to_vertex = graph.get_vertex(self.to_vertex_label)

        # Add the edge
        added_edge = False
        if from_vertex and  to_vertex:
            added_edge = graph.add_directed_edge(from_vertex, to_vertex)

        if added_edge == self.should_succeed:
            # PASS
            if added_edge:
                print(f'''PASS: Added edge from "{self.from_vertex_label}" to "{self.to_vertex_label}"''',
                file=test_feedback)
            else:
                print(f'''PASS: Attempt to add edge from "{self.from_vertex_label}" to "{self.to_vertex_label}" returned False''',
                      file=test_feedback)
            return True

        # FAIL
        print(f'''FAIL: Add from "{to_vertex}" to "{to_label}"''',
              file=test_feedback)
        return False

class HasEdgeCommand(DirectedGraphTestCommand):
    def __init__(self, from_vertex_label, to_vertex_label, expected_return_value):
        self.from_vertex_label = from_vertex_label
        self.to_vertex_label = to_vertex_label
        self.expected_return_value = expected_return_value

    def execute(self, test_feedback, graph):
        # Find both vertices
        from_vertex = graph.get_vertex(self.from_vertex_label)
        to_vertex = graph.get_vertex(self.to_vertex_label)

        # Call has_edge() to get the actual return value
        actual = graph.has_edge(from_vertex, to_vertex)

        if actual != self.expected_return_value:
            print(f'''FAIL: has_edge() should have returned {"True " if expected else "False"}
for an edge from {from_vertex.get_label() if to_vertex else "None"}, but
instead returned {"True " if actual else "False"}''',
                  file=test_feedback)
            return False

        print(f'''PASS: has_edge() returned {"True " if self.expected_return_value else "False"} \
for an edge from {from_vertex.get_label() if from_vertex else "None"} \
to {to_vertex.get_label() if to_vertex else "None"}''',
              file=test_feedback)
        return True

class VerifyEdgesFromCommand(DirectedGraphTestCommand):
    def __init__(self, from_vertex_label, to_vertex_labels):
        self.from_vertex_label = from_vertex_label
        self.to_vertex_labels = to_vertex_labels

    def execute(self, test_feedback, graph):
        # Find from_vertex
        from_vertex = graph.get_vertex(self.from_vertex_label)
        if not from_vertex:
            print(f'''FAIL: get_vertex("{to_vertex}") returned None for \
a vertex that should exist''',
                  file=test_feedback)
            return False

        # Ask the graph for edges from from_vertex
        actual = graph.get_edges_from(from_vertex)

        passed = True
        if len(actual) == len(self.to_vertex_labels):
            for to_label in self.to_vertex_labels:
                # Get the expected to-vertex
                expected_to = graph.get_vertex(to_label)

                # If the actual list of vertices does not have the edge then the
                # test fails
                if not self.has_edge(actual, from_vertex, expected_to):
                    passed = False
                    break
        else:
            passed = False

        # Print pass or fail message along with the actual and expected collections
        print(f'''{"PASS:" if passed else "FAIL:"} Get edges from "{self.from_vertex_label}"''',
              file=test_feedback)
        self.print_edges(test_feedback, actual, ", ", "  Actual:   [", "]\n")
        print("  Expected: [", file=test_feedback, end='')
        if len(self.to_vertex_labels) > 0:
            print(f'''{self.from_vertex_label} to {self.to_vertex_labels[0]}''',
                  file=test_feedback,
                  end='')
            for to_label in self.to_vertex_labels[1:]:
                print(f''', {self.from_vertex_label} to {to_label}''',
                      file=test_feedback, end='')
        print(']', file=test_feedback)
        return passed

class VerifyEdgesToCommand(DirectedGraphTestCommand):
    def __init__(self, to_vertex_label, from_vertex_labels):
        self.to_vertex_label = to_vertex_label
        self.from_vertex_labels = from_vertex_labels

    def execute(self, test_feedback, graph):
        # Find to_vertex
        to_vertex = graph.get_vertex(self.to_vertex_label)
        if not to_vertex:
            print(f'''FAIL: get_vertex("{self.to_vertex_label}") returned None for \
a vertex that should exist''',
                  file=test_feedback)
            return False

        # Ask the graph for edges from from_vertex
        actual = graph.get_edges_to(to_vertex)

        passed = True
        if len(actual) == len(self.from_vertex_labels):
            for from_label in self.from_vertex_labels:
                # Get the expected to-vertex
                expected_from = graph.get_vertex(from_label)

                # If the actual list of vertices does not have the edge then the
                # test fails
                if not self.has_edge(actual, expected_from, to_vertex):
                    passed = False
                    break
        else:
            passed = False

        # Print pass or fail message along with actual and expected collections
        print(f'''{"PASS:" if passed else "FAIL:"} Get edges to "{self.to_vertex_label}"''',
              file=test_feedback)
        self.print_edges(test_feedback, actual, ", ", "  Actual:   [", "]\n")
        print("  Expected: [", file=test_feedback, end='')
        if len(self.from_vertex_labels) > 0:
            print(f'''{self.from_vertex_labels[0]} to {self.to_vertex_label}''',
                  file=test_feedback, end='')
            for from_label in self.from_vertex_labels[1:]:
                print(f''', {from_label} to {self.to_vertex_label}''',
                      file=test_feedback, end='')
        print(']', file=test_feedback)
        return passed
