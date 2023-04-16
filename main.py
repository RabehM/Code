import sys

from AdjacencyListGraph import AdjacencyListGraph
from AdjacencyMatrixGraph import AdjacencyMatrixGraph

from GraphCommands import *

def main():
    graph1 =  AdjacencyListGraph()
    graph2 =  AdjacencyMatrixGraph()


    # Test AdjacencyListGraph first
    print("AdjacencyListGraph: ")
    adj_pass = test_graph(sys.stdout, graph1)
    print()

    # Test AdjacencyMatrixGraph second
    print("AdjacencyMatrixGraph: ")
    mat_pass = test_graph(sys.stdout, graph2)

    print(f"""
Summary:
  AdjacencyListGraph:   {"PASS" if adj_pass else "FAIL"}
  AdjacencyMatrixGraph: {"PASS" if mat_pass else "FAIL"}""",
          )

def test_graph(test_feedback, graph):
    commands = (
        AddVertexCommand("A", True),
        AddVertexCommand("B", True),

        # exist, C, D, E
        GetVertexCommand("C", False),
        GetVertexCommand("A", True),
        GetVertexCommand("B", True),
        GetVertexCommand("E", False),
        GetVertexCommand("D", False),

        # vertices
        AddVertexCommand("C", True),
        AddVertexCommand("D", True),
        AddVertexCommand("E", True),

        # edges
        AddEdgeCommand("B", "C", True),
        AddEdgeCommand("C", "A", True),
        AddEdgeCommand("C", "D", True),
        AddEdgeCommand("C", "E", True),
        AddEdgeCommand("D", "C", True),
        AddEdgeCommand("E", "A", True),
        AddEdgeCommand("E", "D", True),

        # fail
        AddEdgeCommand("C", "E", False),
        AddEdgeCommand("D", "C", False),

        VerifyEdgesFromCommand("A", ()),
        VerifyEdgesFromCommand("B", ("C" )),
        VerifyEdgesFromCommand("C", ("A", "D", "E" )),
        VerifyEdgesFromCommand("D", ("C" )),
        VerifyEdgesFromCommand("E", ("A", "D" )),

        VerifyEdgesToCommand("A", ("C", "E" )),
        VerifyEdgesToCommand("B", ()),
        VerifyEdgesToCommand("C", ("B", "D" )),
        VerifyEdgesToCommand("D", ("C", "E" )),
        VerifyEdgesToCommand("E", ("C")),

        # edges
        HasEdgeCommand("A", "C", False),
        HasEdgeCommand("A", "E", False),
        HasEdgeCommand("B", "C", True),
        HasEdgeCommand("C", "A", True),
        HasEdgeCommand("C", "B", False),
        HasEdgeCommand("C", "D", True),
        HasEdgeCommand("C", "E", True),
        HasEdgeCommand("D", "C", True),
        HasEdgeCommand("E", "A", True),
        HasEdgeCommand("E", "C", False),
        HasEdgeCommand("E", "D", True)
    )

    # command, fails
    for command in commands:
        if not command.execute(test_feedback, graph):
            return False

    return True

if __name__ == '__main__':
    main()
