from unittest import TestCase

from calvin.Book.ctci.ch1.One_1 import One_1

class TestOne_1(TestCase):
    def setUp(self):
        self.fixture = One_1()

    def test_has_all_unique(self):
        expected = [True, False, False, True];
        words = ['abcde', 'hello', 'apple', 'kite']
        for i in range(len(words)):
            self.assertEqual(expected[i], self.fixture.has_all_unique(words[i]))

