from unittest import TestCase

from calvin.backtracking_dfs.number_combinations import NumberCombination

class TestNumberCombination(TestCase):
    def setUp(self):
        self.fixture = NumberCombination()

    def test_number_combination(self):
        num=["4938532894754", "2523214567", "1234567", "0123456", "569815571556", "472844278465445"]
        self.assertEquals([['49', '38', '53', '28', '9', '47', '54'],
                           ['2', '5', '2', '32', '14', '56', '7'],
                           ['25', '2', '3', '2', '14', '56', '7'],
                           ['1', '2', '3', '4', '5', '6', '7'],
                           ['56', '9', '8', '15', '57', '15', '56']],
                          self.fixture.number_combination(num))

