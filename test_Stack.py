import unittest
from Stack import Stack, is_balanced_parentheses, reverse_string, sort_stack

class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 1)
        self.assertIsNone(stack.pop())

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_str(self):
        stack = Stack()
        self.assertEqual(str(stack), "||")
        stack.push(1)
        self.assertEqual(str(stack), "<- 1 ||")
        stack.push(2)
        self.assertEqual(str(stack), "<- 2 |<- 1 ||")

    def test_is_balanced_parentheses(self):
        self.assertTrue(is_balanced_parentheses("()"))
        self.assertTrue(is_balanced_parentheses("(())"))
        self.assertFalse(is_balanced_parentheses("(()"))
        self.assertFalse(is_balanced_parentheses("())"))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

    def test_sort_stack(self):
        stack = Stack()
        stack.push(3)
        stack.push(1)
        stack.push(2)
        sort_stack(stack)
        self.assertEqual(stack.pop().value, 1)
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 3)

if __name__ == '__main__':
    unittest.main()