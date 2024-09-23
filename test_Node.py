import unittest

from Node import Node

class TestNode(unittest.TestCase):

    def test_node_initialization(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next)

    def test_node_data_property(self):
        node = Node(10)
        node.data = 20
        self.assertEqual(node.data, 20)

    def test_node_next_property(self):
        node1 = Node(10)
        node2 = Node(20)
        node1.next = node2
        self.assertEqual(node1.next, node2)

    def test_node_repr(self):
        node = Node(10)
        self.assertEqual(repr(node), "Node(data=10)")

    def test_node_str(self):
        node = Node(10)
        self.assertEqual(str(node), "Node with data: 10")

    def test_node_equality(self):
        node1 = Node(10)
        node2 = Node(10)
        node3 = Node(20)
        self.assertTrue(node1 == node2)
        self.assertFalse(node1 == node3)

    def test_node_inequality(self):
        node1 = Node(10)
        node2 = Node(20)
        self.assertTrue(node1 != node2)

    def test_node_hash(self):
        node = Node(10)
        self.assertEqual(hash(node), hash(10))

    def test_node_length(self):
        node = Node(10)
        self.assertEqual(len(node), 1)

if __name__ == '__main__':
    unittest.main()