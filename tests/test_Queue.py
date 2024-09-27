import unittest
from linear.Queue import Queue, Node

class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()
        self.assertTrue(q.enqueue(1))
        self.assertTrue(q.enqueue(2))
        self.assertTrue(q.enqueue(3))
        self.assertEqual(str(q), "<- 1 <- 2 <- 3 <- ")

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        node = q.dequeue()
        self.assertEqual(node.__repr__(), "Node(value=1)")
        self.assertEqual(str(q), "<- 2 <- 3 <- ")
        node = q.dequeue()
        self.assertEqual(node.__repr__(), "Node(value=2)")
        self.assertEqual(str(q), "<- 3 <- ")
        node = q.dequeue()
        self.assertEqual(node.__repr__(), "Node(value=3)")
        self.assertEqual(str(q), "<- ")

    def test_dequeue_empty(self):
        q = Queue()
        self.assertIsNone(q.dequeue())

    def test_initial_value(self):
        q = Queue(10)
        self.assertEqual(str(q), "<- 10 <- ")
        self.assertEqual(q.dequeue().__repr__(), "Node(value=10)")
        self.assertIsNone(q.dequeue())

if __name__ == '__main__':
    unittest.main()