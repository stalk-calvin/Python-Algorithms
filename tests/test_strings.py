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
        self.assertEqual("e", actual)

    def test_reverse_string(self):
        input = "abcd"
        actual = self.fixture.reverseString(input)
        expected = "dcba"
        self.assertEqual(expected, actual)

    def test_first_uniq_string(self):
        input = "eelvinlee"
        actual = self.fixture.firstUniqChar(input)
        self.assertEqual(3, actual)

    def test_is_isomorphic(self):
        self.assertTrue(self.fixture.isIsomorphic("paper", "title"))
        self.assertTrue(self.fixture.isIsomorphic("aabbcc", "ddeeff"))
        self.assertFalse(self.fixture.isIsomorphic("bar", "foo"))
        self.assertFalse(self.fixture.isIsomorphic("foo", "bar"))
        self.assertFalse(self.fixture.isIsomorphic("different", "length"))

    def test_longest_common_prefix(self):
        self.assertEqual("", self.fixture.longestCommonPrefix(None))
        self.assertEqual("single", self.fixture.longestCommonPrefix(["single"]))
        input = ["jewgfsdasda", "jewgfsjwurf", "jew?ASD"]
        actual = self.fixture.longestCommonPrefix(input)
        self.assertEqual("jew", actual)

    def test_reverse_vowels(self):
        input = "calvin"
        actual = self.fixture.reverseVowels(input)
        self.assertEqual("cilvan", actual)

    def test_zig_zag(self):
        input = "PAYPALISHIRING"
        actual = self.fixture.zigZag(input, 3)
        self.assertEqual("PAHNAPLSIIGYIR", actual)

    def test_word_count(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../data/words.txt')
        actual = self.fixture.wordCount(filename)
        self.assertEqual(['to', 16], actual)

    def test_word_list(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../data/words.txt')
        actual = self.fixture.wordList(filename)
        expected = ['If', 'Interestingly,', 'Our', 'The', 'This', 'We', 'What', 'Writing', 'You', 'a', 'activity', 'amounts', 'analysis', 'and', 'are', 'as', 'ask', 'assistants', 'assumes', 'be', 'behalf', 'best', 'book', 'boring', 'built', 'can', 'care', 'cell', 'computer', 'computers', 'continuously', 'could', 'creative', 'current-day', 'daily', 'data', 'difficult', 'do', 'else', 'essentially', 'everyone}', 'explain', 'fast', 'figure', 'find', 'for', 'from', 'fun', 'hardware', 'have', 'having', 'helpful', 'helping', 'how', 'humans', 'if', 'in', 'is', 'it', 'kinds', 'knew', 'know', 'language', 'laptops', 'like', 'lives', 'living', 'making', 'many', 'me', 'memory', 'mind-numbing', 'needs', 'newfound', 'next', 'of', 'often', 'on', 'once', 'only', 'or', 'our', 'out', 'personal', 'phones', 'problem', 'program', 'program,', 'programming', 'programs', 'question', 'ranging', 'reasons', 'reptitive', 'rewarding', 'skills', 'solve', 'solving', 'someone', 'speak', 'surrounded', 'take', 'tasks', 'tell', 'that', 'the', 'these', 'things', 'think', 'this', 'to', 'us', 'vasts', 'very', 'want', 'we', 'were', 'what', 'who', 'will', 'with', 'would', 'write', 'you', 'your', '{\\em']
        self.assertEqual(expected, actual)

    def test_simpify_path(self):
        input = "/a/./b/./../c/"
        actual = self.fixture.simplifyPath(input)
        self.assertEqual("/a/c", actual)

    def test_find_non_repeated_index(self):
        input = "teeter"
        actual = self.fixture.findNonRepeatedIndex(input)
        self.assertEqual('r', actual)

    def test_shiftVowels(self):
        actual = self.fixture.shiftVowels('I love her')
        self.assertEqual('e lIvo her', actual)

    def test_compareVersion(self):
        actual = self.fixture.compareVersion('0.1', '0.11')
        self.assertEquals(-1, actual)

    def tearDown(self):
        del self.fixture