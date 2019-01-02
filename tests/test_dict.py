import unittest
from calvin.data_structure.dict import HistoricalDict

class TestHistoricalDict(unittest.TestCase):
    def setUp(self):
        self.fixture=HistoricalDict()

    def test_set_get(self):
        self.fixture.set('foo', 1, 2)
        self.fixture.set('foo', 2, 4)
        self.fixture.set('foo', 3, 10)
        self.fixture.print()

        self.assertEqual(2, self.fixture.get('foo', 5))
        self.assertEqual(2, self.fixture.get('foo', 4))
        self.assertEqual(1, self.fixture.get('foo', 3))
        self.assertEqual(1, self.fixture.get('foo', 2))
        self.assertEqual(3, self.fixture.get('foo', 20))
        self.assertEqual(None, self.fixture.get('foo', 1))
        self.assertEqual(None, self.fixture.get('foo', 0))
