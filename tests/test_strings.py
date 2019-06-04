import unittest
import os

from calvin.strings import Strings

class StringsTest(unittest.TestCase):
    """
    Test Strings method
    """
    def setUp(self):
        self.fixture = Strings()

    def test_find_the_difference_XOR(self):
        s = "abcd"
        t = "abcde"
        actual = self.fixture.findTheDifferenceXOR(s, t)
        self.assertEqual("e", actual)

    def test_find_the_difference_XOR_LongText(self):
        s = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
        t = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"
        actual = self.fixture.findTheDifferenceXOR(s, t)
        self.assertEqual("t", actual)

    def test_find_the_difference(self):
        s = "abcd"
        t = "abcde"
        actual = self.fixture.findTheDifference(s, t)
        self.assertEqual("e", actual)

    def test_find_the_difference_LongText(self):
        s = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
        t = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"
        actual = self.fixture.findTheDifference(s, t)
        self.assertEqual("t", actual)

    def test_anagramCounter(self):
        self.assertEquals(4, self.fixture.anagramCounter('cde','abc'))

    def test_reverse_string(self):
        input = "abcd"
        actual = self.fixture.reverseString(input)
        expected = "dcba"
        self.assertEqual(expected, actual)

    def test_reverse_string_manual(self):
        input = "abcd"
        actual = self.fixture.reverseStringManual(input)
        expected = "dcba"
        self.assertEqual(expected, actual)

    def test_first_uniq_string(self):
        input = "eelvinlee"
        actual = self.fixture.firstUniqChar(input)
        self.assertEqual('v', actual)

    def test_first_uniq_string_manual(self):
        input = "eelvinlee"
        actual = self.fixture.firstUniqCharManual(input)
        self.assertEqual('v', actual)

    def test_is_isomorphic(self):
        self.assertTrue(self.fixture.isIsomorphic("paper", "title"))
        self.assertTrue(self.fixture.isIsomorphic("aabbcc", "ddeeff"))
        self.assertFalse(self.fixture.isIsomorphic("bar", "foo"))
        self.assertFalse(self.fixture.isIsomorphic("foo", "bar"))
        self.assertFalse(self.fixture.isIsomorphic("different", "length"))

    def test_find_longest_word_with_str(self):
        input_str='cat'
        self.assertEqual(None, self.fixture.find_longest_word_with_str(None, input_str))
        input=['act','acquaintance', 'trace']
        actual = self.fixture.find_longest_word_with_str(input, input_str)
        self.assertEqual('acquaintance', actual)

    def test_buddy_string(self):
        A='abcd'
        B='acbd'
        self.assertTrue(self.fixture.buddy_string(A,B))
        A='abcd'
        B='abcd'
        self.assertFalse(self.fixture.buddy_string(A,B))
        A='abc'
        B='abcd'
        self.assertFalse(self.fixture.buddy_string(A,B))
        A='abcdab'
        B='abcdab'
        self.assertTrue(self.fixture.buddy_string(A,B))

    def test_longest_two_unique(self):
        self.assertEqual(None, self.fixture.longest_two_unique(None))
        input='assdeeeddffffha'
        actual = self.fixture.longest_two_unique(input)
        self.assertEqual('deeedd', actual)

    def test_longest_common_prefix(self):
        self.assertEqual("", self.fixture.longestCommonPrefix(None))
        self.assertEqual("single", self.fixture.longestCommonPrefix(["single"]))
        input = ["jewgfsdasda", "jewgfsjwurf", "jew?ASD"]
        actual = self.fixture.longestCommonPrefix(input)
        self.assertEqual("jew", actual)

    def test_sort_vowels(self):
        input = 'bigger calvin'
        actual = self.fixture.sort_vowels(input)
        self.assertEqual('bagger cilvin', actual)

    def test_sort_between_given_vowel(self):
        input = 'bigger calvin'
        actual = self.fixture.sort_string_between_given_vowels(input, 'a')
        self.assertEqual('bceggi railnv', actual)

    def test_reverse_vowels(self):
        input = "calvin is a monster"
        actual = self.fixture.reverseVowels(input)
        self.assertEqual("celvon as i minstar", actual)

    def test_reverse_vowels_manual(self):
        input = "calvin is a monster"
        actual = self.fixture.reverseVowelsManual(input)
        self.assertEqual("celvon as i minstar", actual)

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

    def test_countAndSay(self):
        actual = self.fixture.countAndSay(6)
        self.assertEquals('312211', actual)

    def test_number_to_words(self):
        actual = self.fixture.number_to_words(1592837572)
        self.assertEquals("One Billion Five Hundred Ninety Two Million Eight Hundred Thirty Seven Thousand Five Hundred Seventy Two", actual)

    def test_permutation(self):
        actual = self.fixture.permutation("1234")
        expected = {'1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314', '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312', '4321'}
        for item in actual:
            if item not in expected:
                self.fail("Unexpected value: "+ item)

    def test_unique_string(self):
        self.assertTrue(self.fixture.isUnique('abcdefg'))
        self.assertFalse(self.fixture.isUnique('ebedefg'))

    def test_unique_string_english(self):
        self.assertTrue(self.fixture.isUniqueNoDs('abcdefg'))
        self.assertFalse(self.fixture.isUniqueNoDs('ebedefg'))

    def test_check_permutation(self):
        self.assertFalse(self.fixture.checkPermutation(None,None))
        self.assertFalse(self.fixture.checkPermutation('abcwde','edbca'))
        self.assertFalse(self.fixture.checkPermutation('abcde','edbcwa'))
        self.assertTrue(self.fixture.checkPermutation('abcde', 'edbca'))

    def test_checkPalindromePermutation(self):
        self.assertTrue(self.fixture.checkPalindromePermutation("Tact Coa"))

    def test_one_away(self):
        self.assertTrue(self.fixture.one_away(None, "p"))
        self.assertTrue(self.fixture.one_away("a", None))
        self.assertFalse(self.fixture.one_away(None, None))
        self.assertTrue(self.fixture.one_away("pales", "pales"))
        self.assertTrue(self.fixture.one_away("pales","pale"))
        self.assertTrue(self.fixture.one_away("ple","pale"))

    def test_string_compression(self):
        self.assertEquals(None,self.fixture.string_compression(None))
        self.assertEquals("a3b1c6a3",self.fixture.string_compression("aaabccccccaaa"))
        self.assertEquals("a", self.fixture.string_compression("a"))
        self.assertEquals("abc", self.fixture.string_compression("abc"))

    def test_string_rotation(self):
        self.assertTrue(self.fixture.string_rotation("waterbottle","erbottlewat"))
        self.assertFalse(self.fixture.string_rotation("waterbottle","erbottlewa"))

    def test_print_all_valid_paren(self):
        actual = self.fixture.print_all_valid_paren(3)
        expected = {'(())()', '()()()', '(()())', '((()))', '()(())'}
        for x in actual:
            expected.remove(x)
        self.assertTrue(len(expected)==0)

    def test_baseball_game(self):
        input=["5","2","C","D","+"]
        self.assertEqual(30, self.fixture.baseball_game(input))
        input=["5","-2","4","C","D","9","+","+"]
        self.assertEqual(27, self.fixture.baseball_game(input))

    def test_tokenize_string(self):
        s="good boy, isn't he?"
        expected="5\ngood\nboy\nisn\nt\nhe"
        self.assertEqual(expected, self.fixture.tokenize_string((s)))

    def test_operator_combo(self):
        self.assertEqual(('+', '+'),self.fixture.operator_combo(14,-58,-85,41,'+-/*'))
        self.assertEqual(('+', '/'),self.fixture.operator_combo(1,2,99,33,'+-/*'))
        self.assertEqual(('/', '*'),self.fixture.operator_combo(72,3,3,8,'+-/*'))
        self.assertEqual(('-', '-'),self.fixture.operator_combo(172,170,333,331,'+-/*'))
        self.assertEqual(('*', '*'),self.fixture.operator_combo(88,50,22,200,'+-/*'))

    def test_compare_bs_caps(self):
        self.assertTrue(self.fixture.compare_bs_caps("abcAA\\baaa","abc\caaaa"))
        self.assertFalse(self.fixture.compare_bs_caps("abcA\\b","abc\ca"))
        self.assertTrue(self.fixture.compare_bs_caps("abcA\\b","abc"))
        self.assertFalse(self.fixture.compare_bs_caps("abcA\\b","ab\ccA"))

    def test_arrange(self):
        self.assertEqual('ooggle', self.fixture.arrange("Google", "dog"))
        self.assertEqual('caaebdddf', self.fixture.arrange("abcdedadf", "cae"))

    def tearDown(self):
        del self.fixture