import unittest
from non_linear.Heap import MaxHeap, MinHeap

class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.max_heap = MaxHeap()

    def test_insert(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(5)
        self.assertEqual(self.max_heap.heap, [20, 10, 5])

    def test_remove(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(5)
        max_value = self.max_heap.remove()
        self.assertEqual(max_value, 20)
        self.assertEqual(self.max_heap.heap, [10, 5])

    def test_remove_empty(self):
        self.assertIsNone(self.max_heap.remove())

    def test_remove_single_element(self):
        self.max_heap.insert(10)
        max_value = self.max_heap.remove()
        self.assertEqual(max_value, 10)
        self.assertEqual(self.max_heap.heap, [])

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap()

    def test_insert(self):
        self.min_heap.insert(10)
        self.min_heap.insert(20)
        self.min_heap.insert(5)
        self.assertEqual(self.min_heap.heap, [5, 20, 10])

    def test_remove(self):
        self.min_heap.insert(10)
        self.min_heap.insert(20)
        self.min_heap.insert(5)
        min_value = self.min_heap.remove()
        self.assertEqual(min_value, 5)
        self.assertEqual(self.min_heap.heap, [10, 20])

    def test_remove_empty(self):
        self.assertIsNone(self.min_heap.remove())

    def test_remove_single_element(self):
        self.min_heap.insert(10)
        min_value = self.min_heap.remove()
        self.assertEqual(min_value, 10)
        self.assertEqual(self.min_heap.heap, [])

if __name__ == '__main__':
    unittest.main()