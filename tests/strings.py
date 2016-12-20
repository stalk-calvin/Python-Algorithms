from __future__ import absolute_import

import unittest

from calvin.strings import Strings

class StringsTest(unittest.TestCase):
    """
    Test Strings method
    """
    def setUp(self):
        self.fixture = Strings()

    def test_find_the_difference(self):
        s = "abcd"
        t = "abcde"
        actual = self.fixture.find_the_difference(s, t)
        self.assertEquals("e", actual)

    def test_reverse_string(self):
        input = "abcd"
        actual = self.fixture.reverseString(input)
        expected = "dcba"
        self.assertEquals(expected, actual)

    def tearDown(self):
        del self.fixture