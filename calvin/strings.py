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