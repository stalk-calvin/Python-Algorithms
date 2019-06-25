from unittest import TestCase
from calvin.backtracking_dfs.wordsearch import WordSearch

class TestWordSearch(TestCase):
    def setUp(self):
        self.fixture = WordSearch()

    def test_exist(self):
        array = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertTrue(self.fixture.exist(array, 'ABCESE'))
        array = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertFalse(self.fixture.exist(array, 'ABFCSA'))
