from unittest import TestCase

from calvin.Book.ctci.ch1.One_6 import One_6

class TestOne_6(TestCase):
    def setUp(self):
        self.fixture = One_6()

    def test_compress1(self):
        input = 'aa'
        self.assertEqual(self.fixture.compress(input), 'aa')

    def test_compress2(self):
        input = 'aaa'
        self.assertEqual(self.fixture.compress(input), 'a3')

    def test_compress3(self):
        input = 'aaaabbc'
        self.assertEqual(self.fixture.compress(input), 'a4b2c1')