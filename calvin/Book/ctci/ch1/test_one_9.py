from unittest import TestCase

from calvin.Book.ctci.ch1.One_9 import One_9

class TestOne_9(TestCase):
    def setUp(self):
        self.fixture = One_9()

    def test_find_string_rotation(self):
        s1='waterbottle'
        s2='erbottlewat'
        self.assertTrue(self.fixture.string_rotation(s1, s2))

    def test_not_find_string_rotation(self):
        s1='camera'
        s2='macera'
        self.assertFalse(self.fixture.string_rotation(s1, s2))
