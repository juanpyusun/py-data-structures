import unittest
from Graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_vertex(self):
        self.assertTrue(self.graph.add_vertex('A'))
        self.assertFalse(self.graph.add_vertex('A'))  # Vertex already exists

    def test_add_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.assertTrue(self.graph.add_edge('A', 'B', 5))
        self.assertFalse(self.graph.add_edge('A', 'C'))  # Vertex 'C' does not exist

    def test_remove_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 5)
        self.assertTrue(self.graph.remove_edge('A', 'B'))
        self.assertFalse(self.graph.remove_edge('A', 'B'))  # Edge already removed

    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 5)
        self.assertTrue(self.graph.remove_vertex('A'))
        self.assertFalse(self.graph.remove_vertex('A'))  # Vertex already removed

    def test_graph_str(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 5)
        expected_str = "{\n  A: [('B', 5)]\n  B: [('A', 5)]\n}"
        self.assertEqual(str(self.graph), expected_str)

if __name__ == '__main__':
    unittest.main()