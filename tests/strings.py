from __future__ import absolute_import

import unittest
import os

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
        actual = self.fixture.findTheDifference(s, t)
        self.assertEquals("e", actual)

    def test_reverse_string(self):
        input = "abcd"
        actual = self.fixture.reverseString(input)
        expected = "dcba"
        self.assertEquals(expected, actual)

    def test_first_uniq_string(self):
        input = "eelvinlee"
        actual = self.fixture.firstUniqChar(input)
        self.assertEquals(3, actual)

    def test_is_isomorphic(self):
        self.assertTrue(self.fixture.isIsomorphic("paper", "title"))
        self.assertTrue(self.fixture.isIsomorphic("aabbcc", "ddeeff"))
        self.assertFalse(self.fixture.isIsomorphic("bar", "foo"))
        self.assertFalse(self.fixture.isIsomorphic("foo", "bar"))
        self.assertFalse(self.fixture.isIsomorphic("different", "length"))

    def test_longest_common_prefix(self):
        self.assertEquals("", self.fixture.longestCommonPrefix(None))
        self.assertEquals("single", self.fixture.longestCommonPrefix(["single"]))
        input = ["jewgfsdasda", "jewgfsjwurf", "jew?ASD"]
        actual = self.fixture.longestCommonPrefix(input)
        self.assertEquals("jew", actual)

    def test_reverse_vowels(self):
        input = "calvin"
        actual = self.fixture.reverseVowels(input)
        self.assertEquals("cilvan", actual)

    def test_zig_zag(self):
        input = "PAYPALISHIRING"
        actual = self.fixture.zigZag(input, 3)
        self.assertEquals("PAHNAPLSIIGYIR", actual)

    def test_word_count(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../data/words.txt')
        actual = self.fixture.wordCount(filename)
        self.assertEquals(['to', 16], actual)

    def tearDown(self):
        del self.fixture