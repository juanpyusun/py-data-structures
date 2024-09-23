import unittest
from LinkedList import LinkedList
from Node import Node

class TestLinkedList(unittest.TestCase):

    def test_initialization(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(len(ll), 0)

        ll_with_value = LinkedList(10)
        self.assertIsNotNone(ll_with_value.head)
        self.assertIsNotNone(ll_with_value.tail)
        self.assertEqual(ll_with_value.head.data, 10)
        self.assertEqual(ll_with_value.tail.data, 10)
        self.assertEqual(len(ll_with_value), 1)

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(len(ll), 1)

        ll.append(2)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 2)
        self.assertEqual(len(ll), 2)

    def test_get(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.get(0).data, 1)
        self.assertEqual(ll.get(1).data, 2)
        self.assertEqual(ll.get(2).data, 3)
        self.assertIsNone(ll.get(3))

    def test_set_value(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertTrue(ll.set_value(1, 20))
        self.assertEqual(ll.get(1).data, 20)
        self.assertFalse(ll.set_value(3, 30))

    def test_insert(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(3)

        self.assertTrue(ll.insert(1, 2))
        self.assertEqual(ll.get(1).data, 2)
        self.assertEqual(len(ll), 3)

        self.assertFalse(ll.insert(4, 4))

    def test_remove(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.remove(1).data, 2)
        self.assertEqual(len(ll), 2)
        self.assertIsNone(ll.remove(2))

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        ll.reverse()
        self.assertEqual(ll.head.data, 3)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.get(1).data, 2)

    def test_pop(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.pop().data, 3)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.pop().data, 2)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.pop().data, 1)
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.pop())

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(len(ll), 1)

        ll.prepend(0)
        self.assertEqual(ll.head.data, 0)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(len(ll), 2)

    def test_pop_first(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(ll.pop_first().data, 1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.pop_first().data, 2)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.pop_first().data, 3)
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.pop_first())

    def test_str(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(str(ll), "1 -> 2 -> 3 -> None")

    def test_repr(self):
        ll = LinkedList(1)
        self.assertEqual(repr(ll), "LinkedList(head=Node(data=1), tail=Node(data=1), length=1)")

if __name__ == '__main__':
    unittest.main()