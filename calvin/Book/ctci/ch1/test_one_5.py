from unittest import TestCase

from calvin.Book.ctci.ch1.One_5 import One_5

class TestOne_5(TestCase):
    def setUp(self):
        self.fixture = One_5()

    def test_oneEditAway(self):
        self.assertTrue(self.fixture.oneEditAway('acdsfdsfadsf', 'acdsfdsfads'))
        self.assertFalse(self.fixture.oneEditAway('pse', 'pale'))