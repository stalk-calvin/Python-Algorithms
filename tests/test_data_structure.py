from random import shuffle

import unittest

from calvin.data_structure.tree import BinaryTree, BinarySearchTree
from calvin.data_structure.queue import Queue, QueueUsingStacks, QueueUsingNodes
from calvin.data_structure.stack import Stack, StackUsingQueue, StackUsingNodes, ThreeStacks, StackMin, SetOfStacks
from calvin.data_structure.linkedlist import ListNode, LinkedList
from calvin.data_structure.graph import Graph, Node, Traversals

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.fixture=LinkedList()
        self.fixture.append('A')
        self.fixture.append('B')
        self.fixture.append('C')

    def test_prepend_node(self):
        self.fixture.prepend('D')
        self.assertEqual(['D', 'A', 'B', 'C'], self.fixture.head.getNodes(list()))

    def test_find_node(self):
        actual = self.fixture.find('C')
        self.assertEqual('C', actual.value)

    def test_reverse(self):
        self.fixture.reverse()
        self.assertEqual(['C','B','A'], self.fixture.head.getNodes(list()))

    def test_delete_by_value(self):
        self.fixture.delete_node_by_value('A')
        self.assertEqual("['B','C']", str(self.fixture))
        self.fixture.delete_node_by_value('C')
        self.assertEqual("['B']", str(self.fixture))
        self.fixture.delete_node_by_value('B')
        self.assertEqual("[]", str(self.fixture))

    def test_remove_dupes(self):
        first=ListNode(0)
        head = first
        for i in range(8):
            second = ListNode(i%2)
            first.next = second
            first = second
        self.fixture.head = head
        self.assertEquals([0, 0, 1, 0, 1, 0, 1, 0, 1], self.fixture.head.getNodes(list()))
        self.fixture.remove_dupes()
        self.assertEquals([0, 1], self.fixture.head.getNodes(list()))

    def test_printKthLastRecursive(self):
        self.fixture.printKthLastRecursive(self.fixture.head, 2)

    def test_getKthLastNodes(self):
        self.assertEquals('B', self.fixture.getKthLastUsingNodes(self.fixture.head, 2).value)

    def test_partition(self):
        first=ListNode(0)
        head = first
        for i in range(1,10):
            second = ListNode(i)
            first.next = second
            first = second
        actual = self.fixture.partition(head, 5)
        self.assertEquals([4, 3, 2, 1, 0, 9, 8, 7, 6, 5], actual.getNodes(list()))

    def test_sum_list(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)

        l2 = ListNode(1)
        l2.next = ListNode(0)
        l2.next.next = ListNode(0)

        expected = [0, 0, 0, 1]
        print(str(l1.getNodes(list())) + " + " + str(l2.getNodes(list())) + " = " + str(expected))

        self.assertEquals(expected, self.fixture.sum_list(l1,l2,0).getNodes(list()))

    def test_palindrome(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(2)
        l1.next.next.next.next = ListNode(1)

        print("Start: " + str(l1.getNodes(list())))
        self.assertTrue(self.fixture.palindrome(l1))

        print("From: "+str(l1.getNodes(list())))
        self.fixture.delete_middle_node(l1.next.next)
        print("Reduced: "+str(l1.getNodes(list())))

        self.assertTrue(self.fixture.palindrome(l1))

        print("From: "+str(l1.getNodes(list())))
        self.fixture.delete_middle_node(l1.next.next)
        print("Reduced: "+str(l1.getNodes(list())))

        self.assertTrue(self.fixture.palindrome(l1))

        print("From: "+str(l1.getNodes(list())))
        self.fixture.delete_middle_node(l1)
        print("Reduced: "+str(l1.getNodes(list())))

        self.assertFalse(self.fixture.palindrome(l1))

    def test_intersection(self):
        first=ListNode(0)
        second=ListNode(0)
        l1=first
        l2=second
        tmp=None
        for i in range(8):
            tmp = ListNode(i%8)
            first.next = tmp
            first = tmp

        for i in range(3):
            tmp = ListNode(i%3)
            second.next = tmp
            second = tmp

        l2.next.next = l1.next.next.next.next

        print(l1.getNodes(list()))
        print(l2.getNodes(list()))

        print(self.fixture.intersection(l1,l2).getNodes(list()))

    def test_loop_detection(self):
        self.fixture.append(0, self.fixture.head)
        self.assertTrue('A', self.fixture.loop_detection().value)

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.fixture = Queue()
        self.assertTrue(self.fixture.isEmpty())

    def test_iter(self):
        self.fixture.enqueue(1)
        self.fixture.enqueue(2)
        self.fixture.enqueue(3)
        stackiter = iter(self.fixture)
        expected = [3,2,1]
        for i in stackiter:
            self.assertEqual(expected.pop(),i)

    def test_push_various_types(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.assertFalse(self.fixture.isEmpty())
        self.assertEqual(3, self.fixture.size())

    def test_pop_items_out(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual(True, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual('cat', self.fixture.peek())
        self.fixture.dequeue()
        self.assertTrue((self.fixture.isEmpty()))
        self.assertRaises(IndexError, self.fixture.dequeue)
        self.assertRaises(Exception, self.fixture.peek)

class TestQueueUsingStacks(unittest.TestCase):
    def setUp(self):
        self.fixture = QueueUsingStacks()
        self.assertTrue(self.fixture.isEmpty())

    def test_push_various_types(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.assertFalse(self.fixture.isEmpty())
        self.assertEqual(3, self.fixture.size())

    def test_pop_items_out(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual(True, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual('cat', self.fixture.peek())
        self.fixture.dequeue()
        self.assertTrue((self.fixture.isEmpty()))
        self.assertRaises(Exception, self.fixture.dequeue)
        self.assertRaises(Exception, self.fixture.peek)

class TestQueueUsingNodes(unittest.TestCase):
    def setUp(self):
        self.fixture = QueueUsingNodes()
        self.assertTrue(self.fixture.isEmpty())

    def test_push_various_types(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.assertFalse(self.fixture.isEmpty())
        self.assertEqual(3, self.fixture.size())

    def test_pop_items_out(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual(True, self.fixture.peek())
        self.fixture.dequeue()
        self.assertEqual('cat', self.fixture.peek())
        self.fixture.dequeue()
        self.assertTrue((self.fixture.isEmpty()))
        self.assertRaises(Exception, self.fixture.dequeue)
        self.assertRaises(Exception, self.fixture.peek)

class TestStack(unittest.TestCase):
    def setUp(self):
        self.fixture = Stack()
        self.assertTrue(self.fixture.isEmpty())

    def test_iter(self):
        self.fixture.push(1)
        self.fixture.push(2)
        self.fixture.push(3)
        stackiter = iter(self.fixture)
        expected = [1,2,3]
        for i in stackiter:
            self.assertEqual(expected.pop(),i)

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
        self.assertRaises(IndexError, self.fixture.pop)
        self.assertRaises(Exception, self.fixture.peek)

    def test_sort(self):
        s1=Stack()
        s1.push(1);s1.push(2);s1.push(4);s1.push(9);s1.push(12);s1.push(11);s1.push(3)
        expected=[1, 2, 3, 4, 9, 11, 12]
        for i in enumerate(iter(self.fixture.sort(s1))):
            self.assertEquals(expected[i[0]], i[1])

class TestSetOfStacks(unittest.TestCase):
    def setUp(self):
        self.fixture = SetOfStacks()

    def test_generic_cases(self):
        self.fixture.push(10)
        self.fixture.push(11)
        self.fixture.push(13)
        self.fixture.push(21)
        self.fixture.push(22)
        self.fixture.push(23)
        self.fixture.push(33)
        self.fixture.push(34)
        self.fixture.push(35)

        self.fixture.pop()

        if self.fixture.get_last_stack():
            self.assertEquals(2, self.fixture.get_last_stack().length)

        self.fixture.pop()
        self.fixture.pop()
        self.fixture.pop()

        if self.fixture.get_last_stack():
            self.assertEquals(2, self.fixture.get_last_stack().length)

        self.fixture.pop()
        self.fixture.pop()
        self.fixture.pop()
        self.fixture.pop()
        self.fixture.pop()
        self.assertRaises(Exception, self.fixture.pop)
        self.assertTrue(self.fixture.isEmpty())


class TestStackUsingQueue(unittest.TestCase):
    def setUp(self):
        self.fixture = StackUsingQueue()
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
        self.assertRaises(Exception, self.fixture.pop)
        self.assertRaises(Exception, self.fixture.peek)

class TestStackUsingNodes(unittest.TestCase):
    def setUp(self):
        self.fixture = StackUsingNodes()
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
        self.assertRaises(Exception, self.fixture.pop)
        self.assertRaises(Exception, self.fixture.peek)

class TestThreeStacks(unittest.TestCase):
    def setUp(self):
        self.fixture = ThreeStacks()
        self.assertTrue(self.fixture.isEmpty(0))
        self.assertTrue(self.fixture.isEmpty(1))
        self.assertTrue(self.fixture.isEmpty(2))

    def test_push_items(self):
        self.fixture.push(0, 10)
        self.fixture.push(1, 20)
        self.fixture.push(2, 30)

        self.fixture.pop(0)
        self.assertRaises(Exception, self.fixture.peek, 0)

        self.fixture.push(0, 10)
        self.fixture.push(0, 20)
        self.fixture.push(0, 30)
        self.assertRaises(Exception, self.fixture.push, 0, 40)

        self.fixture.push(2,20)
        self.assertEquals(20, self.fixture.peek(2))

class TestStackMin(unittest.TestCase):
    def setUp(self):
        self.fixture = StackMin()
        self.fixture.push(1)
        self.fixture.push(2)
        self.fixture.push(3)
        self.fixture.push(4)
        self.fixture.push(5)
        self.fixture.push(5)
        self.fixture.push(5)
        self.fixture.push(9)
        self.fixture.push(5)
        self.fixture.push(5)
        self.fixture.push(3)
        self.fixture.pop()

    def test_get_min(self):
        self.assertEquals(1, self.fixture.min())

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

    balanced = [
        ("d", 4), ("f", 6), ("e", 5),
        ("b", 2), ("a", 1), ("c", 3),
        ("g", 7)
    ]

    def shuffle_list(self, ls):
        shuffle(ls)
        return ls

    def test_size(self):
        # Size starts at 0
        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.size(), 0)
        # Doing a put increases the size to 1
        self.bst.put("one", 1)
        self.assertEqual(self.bst.size(), 1)
        # Putting a key that is already in doesn't change size
        self.bst.put("one", 1)
        self.assertEqual(self.bst.size(), 1)
        self.bst.put("one", 2)
        self.assertEqual(self.bst.size(), 1)

        self.bst = BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.size(), size)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(self.bst.size(), size)

    def test_LCA(self):
        self.bst = BinarySearchTree()
        for pair in self.key_val2:
            k, v = pair
            self.bst.put(k, v)
        self.assertEquals(4, self.bst.LCA(self.bst.root, 1, 9).val)

    def test_is_balanced(self):
        self.bst = BinarySearchTree()
        for pair in self.balanced:
            k, v = pair
            self.bst.put(k, v)
        self.assertEquals(True, self.bst.is_balanced(self.bst.root).balanced)

    def test_is_not_balanced(self):
        self.bst = BinarySearchTree()
        for pair in self.key_val2:
            k, v = pair
            self.bst.put(k, v)
        self.assertEquals(False, self.bst.is_balanced(self.bst.root).balanced)

    def test_is_empty(self):
        self.bst = BinarySearchTree()
        self.assertTrue(self.bst.is_empty())
        self.bst.put("a", 1)
        self.assertFalse(self.bst.is_empty())

    def test_get(self):
        self.bst = BinarySearchTree()
        # Getting a key not in BST returns None
        self.assertEqual(self.bst.get("one"), None)

        # Get with a present key returns proper value
        self.bst.put("one", 1)
        self.assertEqual(self.bst.get("one"), 1)

        self.bst = BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.get(k), v)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.get(k), v)

    def test_contains(self):
        self.bst = BinarySearchTree()
        self.assertFalse(self.bst.contains("a"))
        self.bst.put("a", 1)
        self.assertTrue(self.bst.contains("a"))

    def test_put(self):
        self.bst = BinarySearchTree()

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

        self.bst = BinarySearchTree()
        self.bst.put("bbb", 1)
        # Adding a key less than root doesn't update the right tree
        # but does update the left
        self.bst.put("aaa", 2)
        self.assertEqual(self.bst.root.key, "bbb")
        self.assertEqual(self.bst.root.right, None)
        self.assertEqual(self.bst.root.left.key, "aaa")

        self.bst = BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.get(k), v)
            self.assertEqual(self.bst.size(), size)

        self.bst = BinarySearchTree()

        shuffled = self.shuffle_list(self.key_val[:])

        size = 0
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
            size += 1
            self.assertEqual(self.bst.get(k), v)
            self.assertEqual(self.bst.size(), size)

    def test_min_key(self):
        self.bst = BinarySearchTree()
        for pair in self.key_val[::-1]:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.min_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.min_key(), "a")

    def test_max_key(self):
        self.bst = BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
            self.assertEqual(self.bst.max_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.max_key(), "i")

    def test_floor_key(self):
        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.floor_key("a"), None)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.floor_key("a"), "a")
        self.assertEqual(self.bst.floor_key("b"), "a")
        self.assertEqual(self.bst.floor_key("g"), "g")
        self.assertEqual(self.bst.floor_key("h"), "g")

        self.bst = BinarySearchTree()
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("a", 1)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.floor_key("a"), "a")
        self.assertEqual(self.bst.floor_key("b"), "a")
        self.assertEqual(self.bst.floor_key("g"), "g")
        self.assertEqual(self.bst.floor_key("h"), "g")

    def test_ceiling_key(self):
        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.ceiling_key("a"), None)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.put("e", 5)
        self.bst.put("g", 7)
        self.assertEqual(self.bst.ceiling_key("a"), "a")
        self.assertEqual(self.bst.ceiling_key("b"), "c")
        self.assertEqual(self.bst.ceiling_key("g"), "g")
        self.assertEqual(self.bst.ceiling_key("f"), "g")

        self.bst = BinarySearchTree()
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

        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.select_key(0), None)
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        self.assertEqual(self.bst.select_key(0), "a")
        self.assertEqual(self.bst.select_key(1), "b")
        self.assertEqual(self.bst.select_key(2), "c")

    def test_rank(self):
        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.rank("a"), None)

        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(self.bst.rank("a"), 0)
        self.assertEqual(self.bst.rank("b"), 1)
        self.assertEqual(self.bst.rank("c"), 2)
        self.assertEqual(self.bst.rank("d"), 3)

        shuffled = self.shuffle_list(self.key_val[:])
        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(self.bst.rank("a"), 0)
        self.assertEqual(self.bst.rank("b"), 1)
        self.assertEqual(self.bst.rank("c"), 2)
        self.assertEqual(self.bst.rank("d"), 3)

    def test_delete_min(self):
        self.bst = BinarySearchTree()
        for pair in self.key_val:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1):
            self.bst.delete_min()
            self.assertEqual(self.bst.min_key(), self.key_val[i+1][0])
        self.bst.delete_min()
        self.assertEqual(self.bst.min_key(), None)

        shuffled = self.shuffle_list(self.key_val[:])
        self.bst = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.bst.put(k, v)
        for i in range(self.bst.size() - 1):
            self.bst.delete_min()
            self.assertEqual(self.bst.min_key(), self.key_val[i+1][0])
        self.bst.delete_min()
        self.assertEqual(self.bst.min_key(), None)

    def test_delete_max(self):
        self.bst = BinarySearchTree()
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
        self.bst = BinarySearchTree()
        self.bst.delete("a")
        self.assertEqual(self.bst.root, None)
        self.assertEqual(self.bst.size(), 0)

        # delete key not present in bst
        self.bst = BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete key when bst only contains one key
        self.bst = BinarySearchTree()
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.key, "a")
        self.bst.delete("a")
        self.assertEqual(self.bst.root, None)
        self.assertEqual(self.bst.size(), 0)

        # delete parent key when it only has a left child
        self.bst = BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.left.key, "a")
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete parent key when it only has a right child
        self.bst = BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.put("b", 2)
        self.assertEqual(self.bst.root.right.key, "b")
        self.bst.delete("a")
        self.assertEqual(self.bst.root.key, "b")
        self.assertEqual(self.bst.size(), 1)

        # delete left child key
        self.bst = BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.assertEqual(self.bst.root.left.key, "a")
        self.bst.delete("a")
        self.assertEqual(self.bst.root.key, "b")
        self.assertEqual(self.bst.size(), 1)

        # delete right child key
        self.bst = BinarySearchTree()
        self.bst.put("a", 1)
        self.bst.put("b", 2)
        self.assertEqual(self.bst.root.right.key, "b")
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "a")
        self.assertEqual(self.bst.size(), 1)

        # delete parent key when it has a left and right child
        self.bst = BinarySearchTree()
        self.bst.put("b", 2)
        self.bst.put("a", 1)
        self.bst.put("c", 3)
        self.bst.delete("b")
        self.assertEqual(self.bst.root.key, "c")
        self.assertEqual(self.bst.size(), 2)

    def test_keys(self):
        self.bst = BinarySearchTree()
        self.assertEqual(self.bst.keys(), [])

        for pair in self.key_val2:
            k, v = pair
            self.bst.put(k, v)

        self.assertEqual(
            self.bst.keys(),
            ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        )

    def test_create_minimal_bst_tree(self):
        input=[1,2,3,4,5,6,7,8]
        self.bst = BinarySearchTree()
        actual = self.bst.create_minimal_bst_tree(input, 0, len(input)-1)
        self.assertEqual(2, actual.left.val)
        self.assertEqual(3, actual.left.right.val)
        (bfs, level) = self.bst.bfs_with_level(actual)
        self.assertEqual([4,2,6,1,3,5,7,8],bfs)
        self.assertEqual(4,level)

    def test_list_of_depths(self):
        input=[1,2,3,4,5,6,7,8]
        self.bst = BinarySearchTree()
        input = self.bst.create_minimal_bst_tree(input, 0, len(input)-1)
        actual = self.bst.list_of_depths(input)
        self.assertEqual([4], actual[0].head.getNodes(list()))
        self.assertEqual([2,6], actual[1].head.getNodes(list()))
        self.assertEqual([1,3,5,7], actual[2].head.getNodes(list()))
        self.assertEqual([8], actual[3].head.getNodes(list()))

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = self.build_graph()
        self.fixture = Traversals()

    def test_route_between_two_nodes(self):
        self.assertTrue(self.fixture.route_between_two_nodes(self.graph.get_node()[0], Node('H', 0)))
        self.assertFalse(self.fixture.route_between_two_nodes(self.graph.get_node()[0], Node('X', 0)))
        self.assertFalse(self.fixture.route_between_two_nodes(None, Node('H', 0)))
        self.assertFalse(self.fixture.route_between_two_nodes(self.graph.get_node()[0], None))
        self.assertFalse(self.fixture.route_between_two_nodes(None, None))

    def test_bfs(self):
        self.fixture.bfs(self.graph.get_node()[0])
        self.assertEquals(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], self.fixture.vertices)

    def test_dfs(self):
        self.fixture.dfs(self.graph.get_node()[0])
        self.assertEquals(['A', 'B', 'E', 'C', 'F', 'I', 'J', 'G', 'H', 'D'], self.fixture.vertices)

    def build_graph(self):
        g = Graph()
        tmp = [None] * 10

        tmp[0] = Node('A', 3)
        tmp[1] = Node('B', 2)
        tmp[2] = Node('C', 4)
        tmp[3] = Node('D', 1)
        tmp[4] = Node('E', 1)
        tmp[5] = Node('F', 3)
        tmp[6] = Node('G', 0)
        tmp[7] = Node('H', 0)
        tmp[8] = Node('I', 0)
        tmp[9] = Node('J', 0)

        tmp[0].add_child_node(tmp[1])
        tmp[0].add_child_node(tmp[2])
        tmp[0].add_child_node(tmp[3])

        tmp[1].add_child_node(tmp[0])
        tmp[1].add_child_node(tmp[4])

        tmp[2].add_child_node(tmp[5])
        tmp[2].add_child_node(tmp[6])
        tmp[2].add_child_node(tmp[6])
        tmp[2].add_child_node(tmp[7])

        tmp[3].add_child_node(tmp[0])

        tmp[4].add_child_node(tmp[1])

        tmp[5].add_child_node(tmp[1])
        tmp[5].add_child_node(tmp[8])
        tmp[5].add_child_node(tmp[9])

        for i in range(10):
            g.add_node(tmp[i])
        return g

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.fixture = BinaryTree()
        self.root = self.fixture.build_tree()

    def test_serialize_tree(self):
        out = []
        self.fixture.serialize_preorder(self.root, out)
        self.assertEqual(['1', '2', '#', '#', '3', '#', '#'], out)