import string

from calvin.data_structure.stack import Stack

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

        handle.close()
        return [bigword, bigcount]

    def wordList(self, filelocation):
        handle = open(filelocation, 'r')
        wordlist = list()
        for line in handle:
            words = line.split()
            for word in words:
                if word in wordlist: continue
                wordlist.append(word)

        handle.close()
        wordlist.sort()
        return wordlist

    def simplifyPath(self, path):
        s = Stack()
        skip = {"..", ".", ""}
        for dir in path.split("/"):
            if (dir == ".." and not s.isEmpty()):
                s.pop()
            elif dir not in skip:
                s.push(dir)
        res = ""
        siter = iter(s)
        for elem in siter:
            res = "/" + elem + res
        return "/" if not res else res

    def findNonRepeatedIndex(self, x):
        if not x: return x
        if len(x) < 2: return x[0]
        tracker = {}
        for c in x:
            if c in tracker:
                tracker[c] += 1
            else:
                tracker[c] = 1
        for c in x:
            if (tracker[c] == 1):
                return c
        return None


    def shiftVowels(self,s):
        """
        Shift vowel one to the right (non-case sensitive)
        For example, "I love her" => "e lIvo her"
        :param s: input string to shift vowels
        :return: shifted string
        """
        l = list(s)
        j = [e for e in enumerate(l) if e[1].lower() in "aeiou"]
        for k in range(len(j)): l[j[(k + 1) % len(j)][0]] = j[k][1]
        return ''.join(l)

    def compareVersion(self, v1, v2):
        """
        Compare 2 version numbers v1 and v2

        :param v1: version 1
        :param v2: version 2
        :return: if v1>v2 = 1, v1<v2 = -1, otherwise 0
        """
        v1v = v1.split('.')
        v2v = v2.split('.')
        def validateNumbers(elems):
            v = ''
            for e in elems:
                if not e.isdigit():
                    raise Exception("Must contain digits or float value")
                else:
                    v+=e
            return v

        v1 = validateNumbers(v1v)
        v2 = validateNumbers(v2v)

        p=(v1,v2)
        for i in range(max(len(v1), len(v2))):
            f = int(p[0][i]) if i < len(p[0]) else 0
            s = int(p[1][i]) if i < len(p[1]) else 0
            if f == s:
                continue
            else:
                if f > s:
                    return 1
                elif s > f:
                    return -1
                else:
                    return 0

    def countAndSay(self, n):
        s = '1'
        for i in range(1,n):
            r = ''
            c = s[0]
            count = 1
            for i in range(1,len(s)):
                if (s[i]==c):
                    count+=1
                else:
                    r+=str(count)
                    r+=c
                    c=s[i]
                    count=1
            r+=str(count)
            r+=c
            s=r
        return s