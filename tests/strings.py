from __future__ import absolute_import

import unittest

from calvin import strings

class TestStrings(unittest.TestCase):
    """
    Test Strings method
    """
    def test_find_the_difference(self):
        s = "abcd"
        t = "abcde"
        actual = strings.find_the_difference(s, t)
        self.assertEqual("e", actual)