from unittest import TestCase

from calvin.backtracking_dfs.permutation import Permutation


class TestPermutation(TestCase):
    def setUp(self):
        self.fixture = Permutation()

    def test_permute(self):
        input = [1, 2, 3, 2, 1]
        self.assertEqual('aaa', self.fixture.permute(input))

    def test_permute_unique(self):
        input = [1, 2, 3, 2, 1]
        self.assertEqual('aaa', self.fixture.permuteUnique(input))
