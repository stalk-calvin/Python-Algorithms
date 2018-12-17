from random import shuffle

import unittest

from calvin.data_structure.graph.tree import BinaryTree, BinarySearchTree, Node as tn
from calvin.data_structure.queue import Queue, QueueUsingStacks, QueueUsingNodes, CircularQueue
from calvin.data_structure.stack import Stack, StackUsingQueue, StackUsingNodes, ThreeStacks, StackMin, SetOfStacks
from calvin.data_structure.linkedlist import ListNode, LinkedList, SortedLinkedList
from calvin.data_structure.graph.graph import Graph, Node, Traversals, Sorting
from calvin.data_structure.graph.graph_build_order import BuildOrder, Graph as bo_graph

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
        self.assertEqual(None, self.fixture.find(None))
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
        result=[]
        self.fixture.printKthLastRecursive(self.fixture.head, 2, result)
        self.assertEqual(['B'], result)

    def test_getKthLastNodes(self):
        self.assertEqual(None, self.fixture.getKthLastUsingNodes(None, 5))
        self.assertEqual('B', self.fixture.getKthLastUsingNodes(self.fixture.head, 2).value)

    def test_partition(self):
        first=ListNode(0)
        head = first
        for i in range(1,10):
            second = ListNode(i)
            first.next = second
            first = second
        actual = self.fixture.partition(head, 5)
        self.assertEqual([4, 3, 2, 1, 0, 9, 8, 7, 6, 5], actual.getNodes(list()))
        self.assertEqual([5, 6, 7, 8, 9, 0], self.fixture.partition(head, 0).getNodes(list()))

    def test_sum_list(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)

        l2 = ListNode(1)
        l2.next = ListNode(0)
        l2.next.next = ListNode(0)

        expected = [0, 0, 0, 1]
        print(str(l1.getNodes(list())) + " + " + str(l2.getNodes(list())) + " = " + str(expected))

        self.assertEquals(None, self.fixture.sum_list(None, None, 0))
        self.assertEquals(expected, self.fixture.sum_list(l1,l2,0).getNodes(list()))

    def test_palindrome(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(2)
        l1.next.next.next.next = ListNode(1)

        print("From: " + str(l1.getNodes(list())))
        self.assertTrue(self.fixture.palindrome(l1))
        self.fixture.delete_middle_node(l1.next.next)

        print("From: "+str(l1.getNodes(list())))
        self.assertTrue(self.fixture.palindrome(l1))
        self.fixture.delete_middle_node(l1.next.next)

        print("From: "+str(l1.getNodes(list())))
        self.assertTrue(self.fixture.palindrome(l1))
        self.fixture.delete_middle_node(l1)
        print("Reduced: "+str(l1.getNodes(list())))

        self.assertFalse(self.fixture.palindrome(l1))
        self.fixture.delete_middle_node(l1)

        self.assertFalse(self.fixture.delete_middle_node(l1))
        self.assertFalse(self.fixture.delete_middle_node(None))

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

        self.assertEqual(None, self.fixture.intersection(None, None))
        self.assertEqual([3, 4, 5, 6, 7], self.fixture.intersection(l1, l2).getNodes(list()))

    def test_loop_detection(self):
        self.fixture.prepend(1)
        self.fixture.prepend(2)
        self.fixture.append(0, self.fixture.head.next.next)
        self.assertTrue('A', self.fixture.loop_detection().value)

class TestSortedLinkedList(unittest.TestCase):
    def setUp(self):
        self.fixture = SortedLinkedList()
        self.assertTrue(self.fixture.length()==0)

    def test_operations(self):
        self.fixture.insert(6)
        self.fixture.insert(10)
        self.fixture.insert(3)
        self.fixture.insert(6)
        self.fixture.insert(9)
        self.fixture.insert(6)
        self.fixture.insert(1)
        self.fixture.insert(5)
        self.assertEqual([1, 3, 5, 6, 6, 6, 9, 10], self.fixture.head.getNodes(list()))
        self.fixture.delete_head_node()
        self.assertEqual([3, 5, 6, 6, 6, 9, 10], self.fixture.head.getNodes(list()))
        self.assertEqual(None, self.fixture.search_node(None))
        self.assertEqual(None, self.fixture.search_node(20))
        self.assertEqual(9, self.fixture.search_node(9).value)
        self.assertTrue("3 5 6 6 6 9 10"==str(self.fixture))

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

class TestCircularQueue(unittest.TestCase):
    def setUp(self):
        self.fixture = CircularQueue()
        self.assertTrue(self.fixture.isEmpty())

    def test_push_various_types(self):
        self.fixture.enqueue(6)
        self.fixture.enqueue(True)
        self.fixture.enqueue('cat')
        self.assertEqual(6, self.fixture.peek())
        self.assertFalse(self.fixture.isEmpty())
        self.assertEqual(3, self.fixture.size)

    def test_push_pop_multiple_elements(self):
        self.fixture.enqueue(1)
        self.fixture.enqueue(2)
        self.fixture.enqueue(3)
        self.fixture.enqueue(4)
        self.fixture.enqueue(5)
        self.fixture.enqueue(6)

        self.assertEqual(1, self.fixture.peek())

        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()

        self.fixture.enqueue(1)
        self.fixture.enqueue(2)
        self.fixture.enqueue(3)
        self.fixture.enqueue(4)
        self.fixture.enqueue(5)

        self.assertEqual(4, self.fixture.peek())

        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()
        self.fixture.dequeue()

        self.assertTrue(self.fixture.isEmpty())

        self.fixture.enqueue(4)
        self.fixture.enqueue(5)
        self.assertEqual(4, self.fixture.peek())

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

    def setUp(self):
        self.fixture = BinarySearchTree()

    def shuffle_list(self, ls):
        shuffle(ls)
        return ls

    def test_size(self):
        # Size starts at 0
        self.assertEqual(self.fixture.size(), 0)
        # Doing a put increases the size to 1
        self.fixture.put("one", 1)
        self.assertEqual(self.fixture.size(), 1)
        # Putting a key that is already in doesn't change size
        self.fixture.put("one", 1)
        self.assertEqual(self.fixture.size(), 1)
        self.fixture.put("one", 2)
        self.assertEqual(self.fixture.size(), 1)

        self.fixture = BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
            size += 1
            self.assertEqual(self.fixture.size(), size)

        shuffled = self.shuffle_list(self.key_val[:])
        self.fixture = BinarySearchTree()
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)

        self.assertEqual(self.fixture.size(), size)

    def test_LCA(self):
        for pair in self.key_val2:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEquals(4, self.fixture.LCA(self.fixture.root, 1, 9).val)
        
    def test_first_common_ancestor(self):
        input=[1,2,3,4,5,6,7,8]
        root = self.fixture.create_minimal_bst_tree(input, 0, len(input) - 1)
        self.assertEqual(2, self.fixture.first_common_ancestor(root, root.left.left, root.left.right))

    def test_flip_equilvalent(self):
        #[0,3,1,None,None,None,2]
        root = tn(0)
        root.left = tn(3)
        root.right = tn(1)
        root.left.left = None
        root.left.right = None
        root.right.left = None
        root.right.right = tn(2)

        #[0,3,1,2]
        root1 = tn(0)
        root1.left = tn(3)
        root1.right = tn(1)
        root1.left.left = tn(2)
        self.assertTrue(self.fixture.flipEquiv(root, root1))

    def is_balanced_bf(self):
        for pair in self.balanced:
            k, v = pair
            self.fixture.put(k, v)
        self.assertTrue(self.fixture.is_balanced_bf(self.fixture.root))

    def test_is_not_balanced_bf(self):
        for pair in self.key_val2:
            k, v = pair
            self.fixture.put(k, v)
        self.assertFalse(self.fixture.is_balanced_bf(self.fixture.root))

    def test_is_balanced(self):
        for pair in self.balanced:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEquals(True, self.fixture.is_balanced(self.fixture.root).balanced)

    def test_is_not_balanced(self):
        for pair in self.key_val2:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEquals(False, self.fixture.is_balanced(self.fixture.root).balanced)

    def test_is_empty(self):
        self.assertTrue(self.fixture.is_empty())
        self.fixture.put("a", 1)
        self.assertFalse(self.fixture.is_empty())

    def test_get(self):
        # Getting a key not in BST returns None
        self.assertEqual(self.fixture.get("one"), None)

        # Get with a present key returns proper value
        self.fixture.put("one", 1)
        self.assertEqual(self.fixture.get("one"), 1)

        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
            self.assertEqual(self.fixture.get(k), v)

        shuffled = self.shuffle_list(self.key_val[:])

        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
            self.assertEqual(self.fixture.get(k), v)

    def test_contains(self):
        self.assertFalse(self.fixture.contains("a"))
        self.fixture.put("a", 1)
        self.assertTrue(self.fixture.contains("a"))

    def test_put(self):
        # When BST is empty first put becomes root
        self.fixture.put("bbb", 1)
        self.assertEqual(self.fixture.root.key, "bbb")
        self.assertEqual(self.fixture.root.left, None)

        # Adding a key greater than root doesn't update the left tree
        # but does update the right
        self.fixture.put("ccc", 2)
        self.assertEqual(self.fixture.root.key, "bbb")
        self.assertEqual(self.fixture.root.left, None)
        self.assertEqual(self.fixture.root.right.key, "ccc")

        self.fixture = BinarySearchTree()
        self.fixture.put("bbb", 1)
        # Adding a key less than root doesn't update the right tree
        # but does update the left
        self.fixture.put("aaa", 2)
        self.assertEqual(self.fixture.root.key, "bbb")
        self.assertEqual(self.fixture.root.right, None)
        self.assertEqual(self.fixture.root.left.key, "aaa")

        self.fixture = BinarySearchTree()
        size = 0
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
            size += 1
            self.assertEqual(self.fixture.get(k), v)
            self.assertEqual(self.fixture.size(), size)

        shuffled = self.shuffle_list(self.key_val[:])
        self.fixture = BinarySearchTree()
        size = 0
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
            size += 1
            self.assertEqual(self.fixture.get(k), v)
            self.assertEqual(self.fixture.size(), size)

    def test_min_key(self):
        for pair in self.key_val[::-1]:
            k, v = pair
            self.fixture.put(k, v)
            self.assertEqual(self.fixture.min_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEqual(self.fixture.min_key(), "a")

    def test_max_key(self):
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
            self.assertEqual(self.fixture.max_key(), k)

        shuffled = self.shuffle_list(self.key_val[:])

        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEqual(self.fixture.max_key(), "i")

    def test_floor_key(self):
        self.assertEqual(self.fixture.floor_key("a"), None)
        self.fixture.put("a", 1)
        self.fixture.put("c", 3)
        self.fixture.put("e", 5)
        self.fixture.put("g", 7)
        self.assertEqual(self.fixture.floor_key("a"), "a")
        self.assertEqual(self.fixture.floor_key("b"), "a")
        self.assertEqual(self.fixture.floor_key("g"), "g")
        self.assertEqual(self.fixture.floor_key("h"), "g")

        self.fixture.put("c", 3)
        self.fixture.put("e", 5)
        self.fixture.put("a", 1)
        self.fixture.put("g", 7)
        self.assertEqual(self.fixture.floor_key("a"), "a")
        self.assertEqual(self.fixture.floor_key("b"), "a")
        self.assertEqual(self.fixture.floor_key("g"), "g")
        self.assertEqual(self.fixture.floor_key("h"), "g")

    def test_ceiling_key(self):
        self.assertEqual(self.fixture.ceiling_key("a"), None)
        self.fixture.put("a", 1)
        self.fixture.put("c", 3)
        self.fixture.put("e", 5)
        self.fixture.put("g", 7)
        self.assertEqual(self.fixture.ceiling_key("a"), "a")
        self.assertEqual(self.fixture.ceiling_key("b"), "c")
        self.assertEqual(self.fixture.ceiling_key("g"), "g")
        self.assertEqual(self.fixture.ceiling_key("f"), "g")

        self.fixture.put("c", 3)
        self.fixture.put("e", 5)
        self.fixture.put("a", 1)
        self.fixture.put("g", 7)
        self.assertEqual(self.fixture.ceiling_key("a"), "a")
        self.assertEqual(self.fixture.ceiling_key("b"), "c")
        self.assertEqual(self.fixture.ceiling_key("g"), "g")
        self.assertEqual(self.fixture.ceiling_key("f"), "g")

    def test_select_key(self):
        shuffled = self.shuffle_list(self.key_val[:])
        self.assertEqual(self.fixture.select_key(0), None)
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
        self.assertEqual(self.fixture.select_key(0), "a")
        self.assertEqual(self.fixture.select_key(1), "b")
        self.assertEqual(self.fixture.select_key(2), "c")

    def test_rank(self):
        self.assertEqual(self.fixture.rank("a"), None)
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)

        self.assertEqual(self.fixture.rank("a"), 0)
        self.assertEqual(self.fixture.rank("b"), 1)
        self.assertEqual(self.fixture.rank("c"), 2)
        self.assertEqual(self.fixture.rank("d"), 3)

        self.fixture = BinarySearchTree()
        shuffled = self.shuffle_list(self.key_val[:])
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)

        self.assertEqual(self.fixture.rank("a"), 0)
        self.assertEqual(self.fixture.rank("b"), 1)
        self.assertEqual(self.fixture.rank("c"), 2)
        self.assertEqual(self.fixture.rank("d"), 3)

    def test_delete_min(self):
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
        for i in range(self.fixture.size() - 1):
            self.fixture.delete_min()
            self.assertEqual(self.fixture.min_key(), self.key_val[i + 1][0])
        self.fixture.delete_min()
        self.assertEqual(self.fixture.min_key(), None)

        self.fixture = BinarySearchTree()
        shuffled = self.shuffle_list(self.key_val[:])
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
        for i in range(self.fixture.size() - 1):
            self.fixture.delete_min()
            self.assertEqual(self.fixture.min_key(), self.key_val[i + 1][0])
        self.fixture.delete_min()
        self.assertEqual(self.fixture.min_key(), None)

    def test_delete_max(self):
        for pair in self.key_val:
            k, v = pair
            self.fixture.put(k, v)
        for i in range(self.fixture.size() - 1, 0, -1):
            self.fixture.delete_max()
            self.assertEqual(self.fixture.max_key(), self.key_val[i - 1][0])
        self.fixture.delete_max()
        self.assertEqual(self.fixture.max_key(), None)

        self.fixture = BinarySearchTree()
        shuffled = self.shuffle_list(self.key_val[:])
        for pair in shuffled:
            k, v = pair
            self.fixture.put(k, v)
        for i in range(self.fixture.size() - 1, 0, -1):
            self.fixture.delete_max()
            self.assertEqual(self.fixture.max_key(), self.key_val[i - 1][0])
        self.fixture.delete_max()
        self.assertEqual(self.fixture.max_key(), None)

    def test_delete(self):
        # delete key from an empty bst
        self.fixture.delete("a")
        self.assertEqual(self.fixture.root, None)
        self.assertEqual(self.fixture.size(), 0)
        # delete key not present in bst
        self.fixture.put("a", 1)
        self.fixture.delete("b")
        self.assertEqual(self.fixture.root.key, "a")
        self.assertEqual(self.fixture.size(), 1)
        # delete key when bst only contains one key
        self.fixture.delete("a")
        self.assertEqual(self.fixture.root, None)
        self.assertEqual(self.fixture.size(), 0)
        # delete parent key when it only has a left child
        self.fixture.put("b", 2)
        self.fixture.put("a", 1)
        self.assertEqual(self.fixture.root.left.key, "a")
        self.fixture.delete("b")
        self.assertEqual(self.fixture.root.key, "a")
        self.assertEqual(self.fixture.size(), 1)
        # delete parent key when it only has a right child
        self.fixture.put("b", 2)
        self.assertEqual(self.fixture.root.right.key, "b")
        self.fixture.delete("a")
        self.assertEqual(self.fixture.root.key, "b")
        self.assertEqual(self.fixture.size(), 1)
        # delete left child key
        self.fixture.put("a", 1)
        self.assertEqual(self.fixture.root.left.key, "a")
        self.fixture.delete("a")
        self.assertEqual(self.fixture.root.key, "b")
        self.assertEqual(self.fixture.size(), 1)
        # delete right child key
        self.fixture.put("a", 1)
        self.fixture.put("c", 3)
        self.assertEqual(self.fixture.root.right.key, "c")
        self.fixture.delete("b")
        self.assertEqual(self.fixture.root.key, "c")
        self.assertEqual(self.fixture.size(), 2)

        self.fixture.put("b", 2)
        self.fixture.delete("b")
        self.assertEqual(self.fixture.root.key, "c")
        self.assertEqual(self.fixture.size(), 2)

    def test_keys(self):
        self.assertEqual(self.fixture.keys(), [])

        for pair in self.key_val2:
            k, v = pair
            self.fixture.put(k, v)

        self.assertEqual(
            self.fixture.keys(),
            ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        )

    def test_create_minimal_bst_tree(self):
        input=[1,2,3,4,5,6,7,8]
        
        actual = self.fixture.create_minimal_bst_tree(input, 0, len(input) - 1)
        self.assertEqual(2, actual.left.val)
        self.assertEqual(3, actual.left.right.val)
        self.assertEqual(None, self.fixture.bfs_with_level(None))
        (bfs, level) = self.fixture.bfs_with_level(actual)
        self.assertEqual([4,2,6,1,3,5,7,8],bfs)
        self.assertEqual(4,level)

    def test_depth(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8]
        tree = self.fixture.create_minimal_bst_tree(input, 0, len(input) - 1)
        self.assertEqual(0, self.fixture.level(None))
        self.assertEqual(1, self.fixture.level(tn(0,1)))
        self.assertEqual(4, self.fixture.level(tree))

    def test_list_of_depths(self):
        array=[1,2,3,4,5,6,7,8]
        input = self.fixture.create_minimal_bst_tree(array, 0, len(array) - 1)
        actual = self.fixture.list_of_depths(input)
        self.assertEqual([4], self.fixture.list_of_depths(tn(0, 4))[0].getNodes(list()))
        self.assertEqual([4], actual[0].head.getNodes(list()))
        self.assertEqual([2,6], actual[1].head.getNodes(list()))
        self.assertEqual([1,3,5,7], actual[2].head.getNodes(list()))
        self.assertEqual([8], actual[3].head.getNodes(list()))

    def test_is_not_bst(self):
        self.fixture.root = tn(0, 3)
        self.fixture.root.left = tn(0, 2)
        self.fixture.root.right = tn(0, 2)
        self.assertFalse(self.fixture.is_bst(self.fixture.root))

    def test_is_bst(self):
        input=[1,2,3,4,5,6,7,8]
        self.fixture.create_minimal_bst_tree(input, 0, len(input) - 1)
        self.assertTrue(self.fixture.is_bst(self.fixture.root))

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
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], self.fixture.vertices)

    def test_dfs_iterative(self):
        self.fixture.dfs_iterative(self.graph.get_node()[0])
        self.assertEqual(['A', 'D', 'C', 'H', 'G', 'F', 'J', 'I', 'B', 'E'], self.fixture.vertices)

    def test_dfs(self):
        self.fixture.dfs(self.graph.get_node()[0])
        self.assertEqual(['A', 'B', 'E', 'C', 'F', 'I', 'J', 'G', 'H', 'D'], self.fixture.vertices)

    def test_topological_sort(self):
        g=Graph(4)
        tmp=[None]*4
        tmp[0] = Node('A', 0)
        tmp[1] = Node('B', 1)
        tmp[2] = Node('C', 3)
        tmp[3] = Node('D', 1)

        # B->A
        tmp[1].add_child_node(tmp[0])

        # C->A
        tmp[2].add_child_node(tmp[0])
        # C->B
        tmp[2].add_child_node(tmp[1])
        # C->D
        tmp[2].add_child_node(tmp[3])

        # D->B
        tmp[3].add_child_node(tmp[1])

        for i in range(4):
            g.add_node(tmp[i])

        ts=Sorting(g)
        self.assertEqual("[Node(C), Node(D), Node(B), Node(A)]",str(ts.topologicalSort()))

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
        tmp[2].add_child_node(tmp[7])

        tmp[3].add_child_node(tmp[0])

        tmp[4].add_child_node(tmp[1])

        tmp[5].add_child_node(tmp[8])
        tmp[5].add_child_node(tmp[9])

        for i in range(10):
            g.add_node(tmp[i])
        return g

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.fixture = BinaryTree()
        self.root = self.fixture.build_tree()

    def test_inorder(self):
        self.assertEqual([2, 1, 3], self.fixture.find_inorder_wrapper(self.root))

    def test_serialize_tree(self):
        from collections import deque
        out = []
        self.fixture.serialize_preorder(self.root, out)
        self.assertEquals(['1', '2', '#', '#', '3', '#', '#'], out)
        newroot=self.fixture.deserialize_pretree(deque(out))
        self.assertEquals(self.root.val, newroot.val)
        self.assertEquals(self.root.left.val, newroot.left.val)
        self.assertEquals(self.root.right.val, newroot.right.val)
        out=[]
        self.fixture.serialize_inorder(self.root, out)
        self.assertEquals(['2', '#', '#', '1', '3', '#', '#'], out)
        out=[]
        self.fixture.serialize_postorder(self.root, out)
        self.assertEquals(['2', '#', '#', '3', '#', '#', '1'], out)

    def test_first_common_ancestor(self):
        self.root.left.left = tn(0, 5)
        self.root.left.right = tn(0, 5)
        self.root.right.right = tn(0, 5)
        self.assertEqual(1, self.fixture.first_common_ancestor(self.root, self.root.left.left, self.root.right.right).val)

    def test_check_subtree(self):
        t1 = tn(0, 0)
        t1.left = tn(0, 1)
        t1.left.left = tn(0, 2)
        t1.left.right = tn(0, 3)

        t2 = tn(0, 1)
        t2.left = tn(0, 2)
        t2.right = tn(0, 3)
        self.assertTrue(self.fixture.check_subtree(t1,t2))

        t1.left.left = None
        self.assertFalse(self.fixture.check_subtree(t1,t2))

    def test_path_sum(self):
        tree = tn(0, 0)
        tree.left = tn(0, -1)
        tree.left.left = tn(0, 2)
        tree.left.right = tn(0, 3)

        self.assertEqual(1, self.fixture.path_sum(tree, 1, 0))

    def test_path_sum_result(self):
        tree = tn(0, 0)
        tree.left = tn(0, -1)
        tree.left.left = tn(0, 2)
        tree.left.right = tn(0, 3)
        tree.right = tn(0, 1)
        tree.right.left = tn(0, 1)
        tree.right.right = tn(0, 2)

        result=[]
        self.assertEqual([[0, -1, 2], [0, 1]], self.fixture.path_sum_result(tree, 1, 0, result, []))

class TestGraphBuildOrder(unittest.TestCase):
    def setUp(self):
        projects=["a","b","c","d","e","f"]
        dependencies = (
            ("a", "d"),
            ("f", "b"),
            ("b", "d"),
            ("f", "a"),
            ("d", "c")
        )
        graph = self.build_graph(projects, dependencies)
        self.fixture = BuildOrder(graph)

    def test_build_order(self):
        expected=['f','e','b','a','d','c']
        actual = self.fixture.get_project_order(self.fixture.graph.nodes)
        for i in range(len(actual)):
            self.assertTrue(expected[i]==actual.pop())

    def build_graph(self, projects, dependencies):
        graph = bo_graph()
        for project in projects:
            graph.create_node(project)

        for dependency in dependencies:
            first=dependency[0]
            second=dependency[1]
            graph.add_edge(first,second)

        return graph
