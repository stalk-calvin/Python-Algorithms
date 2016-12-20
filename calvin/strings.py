class Strings(object):
    """
    Implementation on String Manipulation
    """
def find_the_difference(s, t):
    ans = 0
    for c in s + t:
        ans ^= ord(c)
    return chr(ans)