import string

class Strings(object):
    """
    Implementation on String Manipulation
    """
    def find_the_difference(self, s, t):
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