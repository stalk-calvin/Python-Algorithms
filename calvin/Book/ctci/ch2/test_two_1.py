from unittest import TestCase

from calvin.Book.ctci.ch2.Two_1 import Two_1
from calvin.data_structure.linkedlist import ListNode

class TestTwo_1(TestCase):
    def setUp(self):
        self.fixture = Two_1()
    def test_remove_dupe(self):
        first=ListNode(0)
        head = first
        for i in range(8):
            second = ListNode(i%2)
            first.next = second
            first = second
        self.fixture.remove_dupe(head)
        self.assertEquals([0, 1], head.getNodes(list()))

