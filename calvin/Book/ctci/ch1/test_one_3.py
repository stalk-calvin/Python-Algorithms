from unittest import TestCase

from calvin.Book.ctci.ch1.One_3 import One_3

class TestOne_3(TestCase):
    def setUp(self):
        self.fixture = One_3()

    def test_isPermutationUsingSort(self):
        self.assertTrue(self.fixture.isPermutationUsingSort('rabbit', 'ribbat'))

    def test_isPermutationArray(self):
        self.assertTrue(self.fixture.isPermutationArray('rabbit', 'ribbat'))

    def test_isNotPermutationUsingSort(self):
        self.assertFalse(self.fixture.isPermutationUsingSort('hello', 'llloh'))

    def test_isNotPermutationArray(self):
        self.assertFalse(self.fixture.isPermutationArray('hello', 'llloh'))
