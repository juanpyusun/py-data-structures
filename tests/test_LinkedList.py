import unittest
from linear.LinkedList import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    def test_initialization(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(len(ll), 0)

        ll_with_value = LinkedList(10)
        self.assertEqual(ll_with_value.head.value, 10)
        self.assertEqual(ll_with_value.tail.value, 10)
        self.assertEqual(len(ll_with_value), 1)

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(len(ll), 1)

        ll.append(2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)
        self.assertEqual(len(ll), 2)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(len(ll), 1)

        ll.prepend(2)
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(len(ll), 2)

    def test_get(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.get(0).value, 1)
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(ll.get(2).value, 3)
        self.assertIsNone(ll.get(3))

    def test_set_value(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertTrue(ll.set_value(1, 20))
        self.assertEqual(ll.get(1).value, 20)
        self.assertFalse(ll.set_value(3, 30))

    def test_insert(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(3)
        self.assertTrue(ll.insert(1, 2))
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(len(ll), 3)
        self.assertFalse(ll.insert(4, 4))

    def test_remove(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.remove(1).value, 2)
        self.assertEqual(len(ll), 2)
        self.assertIsNone(ll.remove(3))

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()
        self.assertEqual(ll.get(0).value, 3)
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(ll.get(2).value, 1)

    def test_pop(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.pop().value, 3)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.pop().value, 2)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.pop().value, 1)
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.pop())

    def test_pop_first(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.pop_first().value, 1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.pop_first().value, 2)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.pop_first().value, 3)
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.pop_first())

    def test_find_middle_node(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.find_middle_node().value, 2)
        ll.append(4)
        self.assertEqual(ll.find_middle_node().value, 2)

    def test_has_loop(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertFalse(ll.has_loop())
        ll.tail.next = ll.head  # Create a loop
        self.assertTrue(ll.has_loop())

    def test_find_kth_from_end(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        self.assertEqual(ll.find_kth_from_end(2).value, 4)
        self.assertIsNone(ll.find_kth_from_end(5))

    def test_partition_list(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(4)
        ll.append(3)
        ll.append(2)
        ll.append(5)
        ll.append(2)
        ll.partition_list(3)
        self.assertEqual(str(ll), "1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None")

    def test_remove_duplicates(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(2)
        ll.append(3)
        ll.append(3)
        ll.append(4)
        ll.remove_duplicates()
        self.assertEqual(str(ll), "1 -> 2 -> 3 -> 4 -> None")

    def test_binary_to_decimal(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(0)
        ll.append(1)
        self.assertEqual(ll.binary_to_decimal(), 5)

    def test_reverse_between(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.reverse_between(1, 3)
        self.assertEqual(str(ll), "1 -> 4 -> 3 -> 2 -> 5 -> None")

if __name__ == '__main__':
    unittest.main()