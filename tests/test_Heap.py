import unittest
from non_linear.Heap import (
    MaxHeap,
    MinHeap,
    find_kth_smallest,
    stream_max)

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

class TestHeapFunctions(unittest.TestCase):
    def test_find_kth_smallest(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(find_kth_smallest(nums, k), 5)

        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(find_kth_smallest(nums, k), 4)

    def test_stream_max(self):
        nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        expected_stream = [1, 3, 5, 7, 9, 9, 9, 9, 9, 9]
        self.assertEqual(stream_max(nums), expected_stream)


if __name__ == '__main__':
    unittest.main()