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

    def test_word_list(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../data/words.txt')
        actual = self.fixture.wordList(filename)
        expected = ['If', 'Interestingly,', 'Our', 'The', 'This', 'We', 'What', 'Writing', 'You', 'a', 'activity', 'amounts', 'analysis', 'and', 'are', 'as', 'ask', 'assistants', 'assumes', 'be', 'behalf', 'best', 'book', 'boring', 'built', 'can', 'care', 'cell', 'computer', 'computers', 'continuously', 'could', 'creative', 'current-day', 'daily', 'data', 'difficult', 'do', 'else', 'essentially', 'everyone}', 'explain', 'fast', 'figure', 'find', 'for', 'from', 'fun', 'hardware', 'have', 'having', 'helpful', 'helping', 'how', 'humans', 'if', 'in', 'is', 'it', 'kinds', 'knew', 'know', 'language', 'laptops', 'like', 'lives', 'living', 'making', 'many', 'me', 'memory', 'mind-numbing', 'needs', 'newfound', 'next', 'of', 'often', 'on', 'once', 'only', 'or', 'our', 'out', 'personal', 'phones', 'problem', 'program', 'program,', 'programming', 'programs', 'question', 'ranging', 'reasons', 'reptitive', 'rewarding', 'skills', 'solve', 'solving', 'someone', 'speak', 'surrounded', 'take', 'tasks', 'tell', 'that', 'the', 'these', 'things', 'think', 'this', 'to', 'us', 'vasts', 'very', 'want', 'we', 'were', 'what', 'who', 'will', 'with', 'would', 'write', 'you', 'your', '{\\em']
        self.assertEquals(expected, actual)

    def test_simpify_path(self):
        input = "/a/./b/./../c/"
        actual = self.fixture.simplifyPath(input)
        self.assertEqual("/a/c", actual)

    def test_find_non_repeated_index(self):
        input = "teeter"
        actual = self.fixture.findNonRepeatedIndex(input)
        self.assertEqual('r', actual)

    def tearDown(self):
        del self.fixture