import unittest
from non_linear.BinarySearchTree import BinarySearchTree, Node

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert(self):
        self.assertTrue(self.bst.insert(10))
        self.assertTrue(self.bst.insert(5))
        self.assertTrue(self.bst.insert(15))
        self.assertFalse(self.bst.insert(10))  # Duplicate value

    def test_search(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.search(10))
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(15))
        self.assertFalse(self.bst.search(20))

    def test_recursive_contains(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.r_contains(10))
        self.assertTrue(self.bst.r_contains(5))
        self.assertTrue(self.bst.r_contains(15))
        self.assertFalse(self.bst.r_contains(20))

    def test_recursive_insert(self):
        self.assertTrue(self.bst.r_insert(10))
        self.assertTrue(self.bst.r_insert(5))
        self.assertTrue(self.bst.r_insert(15))
        self.assertTrue(self.bst.r_contains(10))
        self.assertTrue(self.bst.r_contains(5))
        self.assertTrue(self.bst.r_contains(15))

    def test_delete_node(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.bst.insert(12)
        self.bst.insert(20)
        
        self.assertTrue(self.bst.r_delete_node(10))
        self.assertFalse(self.bst.search(10))
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(15))

    def test_find_min(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.bst.insert(12)
        self.bst.insert(20)
        
        self.assertEqual(self.bst.find_min(self.bst._BinarySearchTree__root), 2)

    def test_str(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        expected_str = " 10 \n 5  15 "
        self.assertEqual(str(self.bst), expected_str)

    def test_repr(self):
        self.bst.insert(10)
        self.assertEqual(repr(self.bst), "BinarySearchTree(length=1)")

if __name__ == '__main__':
    unittest.main()