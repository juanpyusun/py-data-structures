import unittest
from linear.DoublyLinkedList import DoublyLinkedList, Node

class TestDoublyLinkedList(unittest.TestCase):

    def test_initialization(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(len(dll), 0)

        dll_with_value = DoublyLinkedList(10)
        self.assertEqual(dll_with_value.head.value, 10)
        self.assertEqual(dll_with_value.tail.value, 10)
        self.assertEqual(len(dll_with_value), 1)

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append(10)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(len(dll), 1)

        dll.append(20)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 20)
        self.assertEqual(len(dll), 2)

    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend(10)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(len(dll), 1)

        dll.prepend(20)
        self.assertEqual(dll.head.value, 20)
        self.assertEqual(dll.tail.value, 10)
        self.assertEqual(len(dll), 2)

    def test_get(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        self.assertEqual(dll.get(0).value, 10)
        self.assertEqual(dll.get(1).value, 20)
        self.assertEqual(dll.get(2).value, 30)
        self.assertIsNone(dll.get(3))

    def test_insert(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(30)
        dll.insert(1, 20)
        self.assertEqual(dll.get(1).value, 20)
        self.assertEqual(len(dll), 3)

    def test_pop(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        self.assertEqual(dll.pop().value, 30)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.pop().value, 20)
        self.assertEqual(len(dll), 1)
        self.assertEqual(dll.pop().value, 10)
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.pop())

    def test_pop_first(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        self.assertEqual(dll.pop_first().value, 10)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.pop_first().value, 20)
        self.assertEqual(len(dll), 1)
        self.assertEqual(dll.pop_first().value, 30)
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.pop_first())

    def test_remove(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        self.assertEqual(dll.remove(1).value, 20)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.remove(0).value, 10)
        self.assertEqual(len(dll), 1)
        self.assertEqual(dll.remove(0).value, 30)
        self.assertEqual(len(dll), 0)
        self.assertIsNone(dll.remove(0))

    def test_set_value(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        self.assertTrue(dll.set_value(1, 25))
        self.assertEqual(dll.get(1).value, 25)
        self.assertFalse(dll.set_value(3, 40))

    def test_swap_first_last(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.swap_first_last()
        self.assertEqual(dll.head.value, 30)
        self.assertEqual(dll.tail.value, 10)

    def test_reverse(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.reverse()
        self.assertEqual(dll.head.value, 30)
        self.assertEqual(dll.tail.value, 10)

    def test_is_palindrome(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(10)
        self.assertTrue(dll.is_palindrome())
        dll.append(30)
        self.assertFalse(dll.is_palindrome())

    def test_swap_pairs(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(20)
        dll.append(30)
        dll.append(40)
        dll.swap_pairs()
        self.assertEqual(dll.get(0).value, 20)
        self.assertEqual(dll.get(1).value, 10)
        self.assertEqual(dll.get(2).value, 40)
        self.assertEqual(dll.get(3).value, 30)

if __name__ == '__main__':
    unittest.main()