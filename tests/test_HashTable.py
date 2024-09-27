import unittest
from non_linear.HashTable import (
    HashTable,
    item_in_common,
    find_duplicates,
    first_non_repeating_char,
    group_anagrams,
    two_sum,
    subarray_sum,
    remove_duplicates,
    has_unique_chars,
    find_pairs,
    longest_consecutive_sequence)

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_set_and_get_item(self):
        self.hash_table.set_item("key1", "value1")
        self.assertEqual(self.hash_table.get_item("key1"), "value1")
        self.assertIsNone(self.hash_table.get_item("key2"))

    def test_keys(self):
        self.hash_table.set_item("key1", "value1")
        self.hash_table.set_item("key2", "value2")
        self.assertListEqual(sorted(self.hash_table.keys()), ["key1", "key2"])

    def test_items(self):
        self.hash_table.set_item("key1", "value1")
        self.hash_table.set_item("key2", "value2")
        self.assertListEqual(sorted(self.hash_table.items()), [["key1", "value1"], ["key2", "value2"]])

    def test_values(self):
        self.hash_table.set_item("key1", "value1")
        self.hash_table.set_item("key2", "value2")
        self.assertListEqual(sorted(self.hash_table.values()), ["value1", "value2"])

    def test_repr_and_str(self):
        self.assertEqual(repr(self.hash_table), "HashTable(size=5)")
        self.hash_table.set_item("key1", "value1")
        self.assertIn("0: None", str(self.hash_table))
        self.assertIn("1: None", str(self.hash_table))

class TestFunctions(unittest.TestCase):
    def test_item_in_common(self):
        self.assertTrue(item_in_common([1, 2, 3], [3, 4, 5]))
        self.assertFalse(item_in_common([1, 2, 3], [4, 5, 6]))

    def test_find_duplicates(self):
        self.assertListEqual(find_duplicates([1, 2, 3, 2, 1]), [1, 2])
        self.assertListEqual(find_duplicates([1, 2, 3]), [])

    def test_first_non_repeating_char(self):
        self.assertEqual(first_non_repeating_char("aabbccdde"), "e")
        self.assertIsNone(first_non_repeating_char("aabbcc"))

    def test_group_anagrams(self):
        self.assertListEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                             [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    def test_two_sum(self):
        self.assertListEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertListEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_subarray_sum(self):
        self.assertListEqual(subarray_sum([1, 2, 3, 4, 5], 9), [1, 3])
        self.assertListEqual(subarray_sum([1, 2, 3, 4, 5], 15), [0, 4])

    def test_remove_duplicates(self):
        self.assertListEqual(sorted(remove_duplicates([1, 2, 2, 3, 4, 4, 5])), [1, 2, 3, 4, 5])

    def test_has_unique_chars(self):
        self.assertTrue(has_unique_chars("abcdef"))
        self.assertFalse(has_unique_chars("aabbcc"))

    def test_find_pairs(self):
        self.assertListEqual(find_pairs([1, 2, 3], [4, 5, 6], 7), [(3, 4), (2, 5), (1, 6)])
        self.assertListEqual(find_pairs([1, 2, 3], [4, 5, 6], 10), [])

    def test_longest_consecutive_sequence(self):
        self.assertEqual(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive_sequence([1, 2, 0, 1]), 3)

if __name__ == "__main__":
    unittest.main()