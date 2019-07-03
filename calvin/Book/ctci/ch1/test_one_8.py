from unittest import TestCase

from calvin.Book.ctci.ch1.One_8 import One_8

class TestOne_8(TestCase):
    def setUp(self):
        self.fixture = One_8()

    def test_zero_matrix(self):
        input = [
            [1,2,3,4,5],
            [1,2,0,4,5],
            [1,2,3,4,5],
            [1,2,3,0,5],
            [1,2,3,4,5]
        ]

        expected = [
            [1, 2, 0, 0, 5],
            [0, 0, 0, 0, 0],
            [1, 2, 0, 0, 5],
            [0, 0, 0, 0, 0],
            [1, 2, 0, 0, 5]
        ]

        self.fixture.zero_matrix(input)

        self.assertEqual(expected, input)