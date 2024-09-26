import unittest
from Node import Node

class TestNode(unittest.TestCase):

    def test_initialization(self):
        node = Node(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

    def test_value_property(self):
        node = Node(10)
        node.value = 20
        self.assertEqual(node.value, 20)

    def test_next_property(self):
        node1 = Node(10)
        node2 = Node(20)
        node1.next = node2
        self.assertEqual(node1.next, node2)

    def test_prev_property(self):
        node1 = Node(10)
        node2 = Node(20)
        node1.prev = node2
        self.assertEqual(node1.prev, node2)

    def test_repr(self):
        node = Node(10)
        self.assertEqual(repr(node), "Node(value=10)")

    def test_str(self):
        node = Node(10)
        self.assertEqual(str(node), "Node(value=10)")

    def test_eq(self):
        node1 = Node(10)
        node2 = Node(10)
        self.assertTrue(node1 == node2)

    def test_ne(self):
        node1 = Node(10)
        node2 = Node(20)
        self.assertTrue(node1 != node2)

    def test_hash(self):
        node = Node(10)
        self.assertEqual(hash(node), hash(10))

    def test_len(self):
        node = Node(10)
        self.assertEqual(len(node), 1)

    def test_add(self):
        node1 = Node(10)
        node2 = Node(20)
        result = node1 + node2
        self.assertEqual(result.value, 30)

    def test_sub(self):
        node1 = Node(20)
        node2 = Node(10)
        result = node1 - node2
        self.assertEqual(result.value, 10)

    def test_mul(self):
        node1 = Node(10)
        node2 = Node(20)
        result = node1 * node2
        self.assertEqual(result.value, 200)

    def test_truediv(self):
        node1 = Node(20)
        node2 = Node(10)
        result = node1 / node2
        self.assertEqual(result.value, 2.0)

    def test_floordiv(self):
        node1 = Node(20)
        node2 = Node(10)
        result = node1 // node2
        self.assertEqual(result.value, 2)

    def test_mod(self):
        node1 = Node(20)
        node2 = Node(6)
        result = node1 % node2
        self.assertEqual(result.value, 2)

    def test_pow(self):
        node1 = Node(2)
        node2 = Node(3)
        result = node1 ** node2
        self.assertEqual(result.value, 8)

    def test_lshift(self):
        node1 = Node(2)
        node2 = Node(3)
        result = node1 << node2
        self.assertEqual(result.value, 16)

    def test_rshift(self):
        node1 = Node(16)
        node2 = Node(3)
        result = node1 >> node2
        self.assertEqual(result.value, 2)

    def test_and(self):
        node1 = Node(6)
        node2 = Node(3)
        result = node1 & node2
        self.assertEqual(result.value, 2)

    def test_or(self):
        node1 = Node(6)
        node2 = Node(3)
        result = node1 | node2
        self.assertEqual(result.value, 7)

    def test_xor(self):
        node1 = Node(6)
        node2 = Node(3)
        result = node1 ^ node2
        self.assertEqual(result.value, 5)

    def test_iadd(self):
        node1 = Node(10)
        node2 = Node(20)
        node1 += node2
        self.assertEqual(node1.value, 30)

    def test_isub(self):
        node1 = Node(20)
        node2 = Node(10)
        node1 -= node2
        self.assertEqual(node1.value, 10)

    def test_imul(self):
        node1 = Node(10)
        node2 = Node(20)
        node1 *= node2
        self.assertEqual(node1.value, 200)

    def test_itruediv(self):
        node1 = Node(20)
        node2 = Node(10)
        node1 /= node2
        self.assertEqual(node1.value, 2.0)

    def test_ifloordiv(self):
        node1 = Node(20)
        node2 = Node(10)
        node1 //= node2
        self.assertEqual(node1.value, 2)

    def test_imod(self):
        node1 = Node(20)
        node2 = Node(6)
        node1 %= node2
        self.assertEqual(node1.value, 2)

    def test_ipow(self):
        node1 = Node(2)
        node2 = Node(3)
        node1 **= node2
        self.assertEqual(node1.value, 8)

    def test_ilshift(self):
        node1 = Node(2)
        node2 = Node(3)
        node1 <<= node2
        self.assertEqual(node1.value, 16)

    def test_irshift(self):
        node1 = Node(16)
        node2 = Node(3)
        node1 >>= node2
        self.assertEqual(node1.value, 2)

    def test_pos(self):
        node = Node(-10)
        result = +node
        self.assertEqual(result.value, -10)

    def test_neg(self):
        node = Node(10)
        result = -node
        self.assertEqual(result.value, -10)

    def test_invert(self):
        node = Node(10)
        result = ~node
        self.assertEqual(result.value, ~10)

    def test_abs(self):
        node = Node(-10)
        result = abs(node)
        self.assertEqual(result.value, 10)

    def test_lt(self):
        node1 = Node(10)
        node2 = Node(20)
        self.assertTrue(node1 < node2)

    def test_le(self):
        node1 = Node(10)
        node2 = Node(20)
        self.assertTrue(node1 <= node2)

    def test_gt(self):
        node1 = Node(20)
        node2 = Node(10)
        self.assertTrue(node1 > node2)

    def test_ge(self):
        node1 = Node(20)
        node2 = Node(10)
        self.assertTrue(node1 >= node2)

    def test_contains(self):
        node = Node(10)
        self.assertTrue(10 in node)

    def test_getitem(self):
        node = Node(10)
        self.assertEqual(node[0], node)

    def test_setitem(self):
        node = Node(10)
        node[0] = 20
        self.assertEqual(node.value, 20)

    def test_delitem(self):
        node = Node(10)
        del node[0]
        self.assertIsNone(node.value)

    def test_call(self):
        node = Node(10)
        with self.assertLogs(level='INFO') as log:
            node(1, 2, a=3, b=4)
            self.assertIn("Node called with args: (1, 2), kwargs: {'a': 3, 'b': 4}", log.output)

    def test_iter(self):
        node = Node(10)
        self.assertEqual(next(iter(node)), 10)

    def test_bool(self):
        node = Node(10)
        self.assertTrue(node)
        node = Node(0)
        self.assertFalse(node)

    def test_float(self):
        node = Node(10)
        self.assertEqual(float(node), 10.0)

    def test_int(self):
        node = Node(10)
        self.assertEqual(int(node), 10)

    def test_reversed(self):
        node = Node(10)
        self.assertEqual(list(reversed(node)), [10])

if __name__ == '__main__':
    unittest.main()