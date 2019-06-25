from unittest import TestCase

from calvin.backtracking_dfs.combinationsum import CombinationSum

class TestCombinationSum(TestCase):
    def setUp(self):
        self.fixture = CombinationSum()

    def test_combinationSum(self):
        actual = self.fixture.combinationSum([1, 2, 3, 5, 8, 7], 8)
        expected = [[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 2],
                    [1, 1, 1, 1, 1, 3],
                    [1, 1, 1, 1, 2, 2],
                    [1, 1, 1, 2, 3],
                    [1, 1, 1, 5],
                    [1, 1, 2, 2, 2],
                    [1, 1, 3, 3],
                    [1, 2, 2, 3],
                    [1, 2, 5],
                    [1, 7],
                    [2, 2, 2, 2],
                    [2, 3, 3],
                    [3, 5],
                    [8]]
        self.assertEqual(expected, actual)


