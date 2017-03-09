import string

class Strings(object):
    """
    Implementation on String Manipulation
    """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aiueo"
        i = 0
        j = len(s) - 1
        sChars = list(s)
        while (i < j):
            if (sChars[i].lower() in vowels and sChars[j].lower() in vowels):
                tmp = sChars[i]
                sChars[i] = sChars[j]
                i += 1
                sChars[j] = tmp
                j -= 1
            elif sChars[j].lower() not in vowels:
                j -= 1
            elif sChars[i].lower() not in vowels:
                i += 1
        return ''.join(sChars)

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: boolean
        """
        size = len(s)
        if size != len(t):
            return False

        sMap = {}
        tMap = {}
        for i in range(size):
            tChar = t[i]
            sChar = s[i]
            if sChar in sMap and sMap[sChar] != tChar:
                return False
            if tChar in tMap and tMap[tChar] != sChar:
                return False
            sMap[sChar] = tChar
            tMap[tChar] = sChar

        return True

    def longestCommonPrefix(self, s):
        """
        :type s: String array
        :rtype: String
        """
        if (not s):
            return ""

        if (len(s) == 1):
            return s[0]

        compare = s[0]
        for i in range(1, len(s)):
            while (compare not in s[i]):
                compare = compare[0:len(compare) - 1]

        return compare

    def zigZag(self, s, numRows):
        """
        :type s: string
        :type numRows: int
        :rtype: string
        """
        if (numRows <= 1):
            return s
        sb = ["" for x in range(numRows)]
        incre = 1
        index = 0
        for i in range(0, len(s)):
            sb[index] += s[i]
            if (index == 0):
                incre = 1
            if (index == numRows - 1):
                incre = -1
            index += incre
        re = ""
        for i in range(0, len(sb)):
            re += sb[i]
        return re

    def wordCount(self, filelocation):
        handle = open(filelocation, 'r')
        counts = dict()

        for line in handle:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1

        bigcount = None
        bigword = None
        for word, count in list(counts.items()):
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count

        return [bigword, bigcount]

    def wordList(self, filelocation):
        handle = open(filelocation, 'r')
        wordlist = list()
        for line in handle:
            words = line.split()
            for word in words:
                if word in wordlist: continue
                wordlist.append(word)

        wordlist.sort()
        return wordlist
