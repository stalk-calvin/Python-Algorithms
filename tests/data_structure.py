from __future__ import absolute_import

from random import shuffle

import unittest

from calvin.data_structure import binary_tree_search
from calvin.data_structure.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.fixture = Stack()
        self.assertTrue(self.fixture.isEmpty())

    def test_push_various_types(self):
        self.fixture.push(6)
        self.fixture.push(True)
        self.fixture.push('cat')
        self.assertEqual('cat', self.fixture.peek())
        self.assertFalse(self.fixture.isEmpty())
        self.assertEqual(3, self.fixture.size())

    def test_pop_items_out(self):
        self.fixture.push(6)
        self.fixture.push(True)
        self.fixture.push('cat')
        self.assertEqual('cat', self.fixture.peek())
        self.fixture.pop()
        self.assertEqual(True, self.fixture.peek())
        self.fixture.pop()
        self.assertEqual(6, self.fixture.peek())
        self.fixture.pop()
        self.assertTrue((self.fixture.isEmpty()))

class TestBinarySearchTree(unittest.TestCase):
    key_val = [
        ("a", 1), ("b", 2), ("c", 3),
        ("d", 4), ("e", 5), ("f", 6),
        ("g", 7), ("h", 8), ("i", 9)
    ]

    key_val2 = [
        ("d", 4), ("e", 5), ("f", 6),
        ("a", 1), ("b", 2), ("c", 3),
        ("g", 7), ("h", 8), ("i", 9)
    ]

    def shuffle_list(self, ls):
        shuffle(ls)
        return ls

    def test_size(self):
        # Size starts at 0
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.size(), 0)
        # Doing a put increases the size to 1
        self.bst.put("one", 1)
        self.assertEqual(self.bst.size(), 1)
        # Putting a key that is already in doesn't change size
        self.bst.put("one", 1)
        self.assertEqual(self.bst.size(), 1)
        self.bst.put("one", 2)
        self.assertEqual(self.bst.size(), 1)

        self.bst = binary_tree_search.BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.size(), size)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = binary_tree_search.BinarySearchTree()
        size = 0
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.size(), size)

    def test_is_empty(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertTrue(self.bst.is_empty())
        self.bst.put("a", 1)
        self.assertFalse(self.bst.is_empty())

    def test_get(self):
        self.bst = binary_tree_search.BinarySearchTree()
        # Getting a key not in BST returns None
        self.assertEqual(self.bst.get("one"), None)

        # Get with a present key returns proper value
        self.bst.put("one", 1)
        self.assertEqual(self.bst.get("one"), 1)

        self.bst = binary_tree_search.BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.get(k), v)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = binary_tree_search.BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.get(k), v)

    def test_contains(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertFalse(self.bst.contains("a"))
        self.bst.put("a", 1)
        self.assertTrue(self.bst.contains("a"))

    def test_put(self):
        self.bst = binary_tree_search.BinarySearchTree()

        # When BST is empty first put becomes root
        self.bst.put("bbb", 1)
        self.assertEqual(self.bst.root.key, "bbb")
        self.assertEqual(self.bst.root.left, None)

        # Adding a key greater than root doesn't update the left tree
        # but does update the right
        self.bst.put("ccc", 2)
        self.assertEqual(self.bst.root.key, "bbb")
        self.assertEqual(self.bst.root.left, None)
        self.assertEqual(self.bst.root.right.key, "ccc")

        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("bbb", 1)
        # Adding a key less than root doesn't update the right tree
        # but does update the left
        self.bst.put("aaa", 2)
        self.assertEqual(self.bst.root.key, "bbb")
        self.assertEqual(self.bst.root.right, None)
        self.assertEqual(self.bst.root.left.key, "aaa")

        self.bst = binary_tree_search.BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.get(k), v)
            self.assertEqual(self.bst.size(), size)

        self.bst = binary_tree_search.BinarySearchTree()

        shuffled = self.shuffle_list(self.key_val[:])

        size = 0
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.get(k), v)
            self.assertEqual(self.bst.size(), size)

    def test_min_key(self):
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in self.key_val[::-1]:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.min_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = binary_tree_search.BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.min_key(), "a")

    def test_max_key(self):
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.max_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = binary_tree_search.BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.max_key(), "i")

    def test_floor_key(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.floor_key("a"), None)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.floor_key("a"), "a")
        self.assertEqual(self.bst.floor_key("b"), "a")
        self.assertEqual(self.bst.floor_key("g"), "g")
        self.assertEqual(self.bst.floor_key("h"), "g")

        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("a", 1)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.floor_key("a"), "a")
        self.assertEqual(self.bst.floor_key("b"), "a")
        self.assertEqual(self.bst.floor_key("g"), "g")
        self.assertEqual(self.bst.floor_key("h"), "g")

    def test_ceiling_key(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.ceiling_key("a"), None)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.ceiling_key("a"), "a")
        self.assertEqual(self.bst.ceiling_key("b"), "c")
        self.assertEqual(self.bst.ceiling_key("g"), "g")
        self.assertEqual(self.bst.ceiling_key("f"), "g")

        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("a", 1)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.ceiling_key("a"), "a")
        self.assertEqual(self.bst.ceiling_key("b"), "c")
        self.assertEqual(self.bst.ceiling_key("g"), "g")
        self.assertEqual(self.bst.ceiling_key("f"), "g")

    def test_select_key(self):
        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.select_key(0), None)
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.select_key(0), "a")
        self.assertEqual(self.bst.select_key(1), "b")
        self.assertEqual(self.bst.select_key(2), "c")

    def test_rank(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.rank("a"), None)

        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(self.bst.rank("a"), 0)
        self.assertEqual(self.bst.rank("b"), 1)
        self.assertEqual(self.bst.rank("c"), 2)
        self.assertEqual(self.bst.rank("d"), 3)

        shuffled = self.shuffle_list(self.key_val[:])
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(self.bst.rank("a"), 0)
        self.assertEqual(self.bst.rank("b"), 1)
        self.assertEqual(self.bst.rank("c"), 2)
        self.assertEqual(self.bst.rank("d"), 3)

    def test_delete_min(self):
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1):
            self.bst.delete_min()
            self.assertEqual(self.bst.min_key(), self.key_val[i+1][0])
        self.bst.delete_min()
        self.assertEqual(self.bst.min_key(), None)

        shuffled = self.shuffle_list(self.key_val[:])
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1):
            self.bst.delete_min()
            self.assertEqual(self.bst.min_key(), self.key_val[i+1][0])
        self.bst.delete_min()
        self.assertEqual(self.bst.min_key(), None)

    def test_delete_max(self):
        self.bst = binary_tree_search.BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1, 0, -1):
            self.bst.delete_max()
            self.assertEqual(self.bst.max_key(), self.key_val[i-1][0])
        self.bst.delete_max()
        self.assertEqual(self.bst.max_key(), None)

        shuffled = self.shuffle_list(self.key_val[:])

        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1, 0, -1):
            self.bst.delete_max()
            self.assertEqual(self.bst.max_key(), self.key_val[i-1][0])
        self.bst.delete_max()
        self.assertEqual(self.bst.max_key(), None)

    def test_delete(self):
        # delete key from an empty bst
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.delete("a")
        self.assertEqual(self.bst.root, None)
        self.assertEqual(self.bst.size(), 0)

        # delete key not present in bst
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete key when bst only contains one key
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.key, "a")
        self.bst.delete("a")
        self.assertEqual(self.bst.root, None)
        self.assertEqual(self.bst.size(), 0)

        # delete parent key when it only has a left child
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.left.key, "a")
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete parent key when it only has a right child
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.put("b", 2)
        self.assertEqual(self.bst.root.right.key, "b")
        self.bst.delete("a")
        self.assertEqual(self.bst.root.key, "b")
        self.assertEqual(self.bst.size(), 1)

        # delete left child key
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.left.key, "a")
        self.bst.delete("a")
        self.assertEqual(self.bst.root.key, "b")
        self.assertEqual(self.bst.size(), 1)

        # delete right child key
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.put("b", 2)
        self.assertEqual(self.bst.root.right.key, "b")
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete parent key when it has a left and right child
        self.bst = binary_tree_search.BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "c")
        self.assertEqual(self.bst.size(), 2)

    def test_keys(self):
        self.bst = binary_tree_search.BinarySearchTree()
        self.assertEqual(self.bst.keys(), [])

        for pair in self.key_val2:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(
            self.bst.keys(),
            ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        )