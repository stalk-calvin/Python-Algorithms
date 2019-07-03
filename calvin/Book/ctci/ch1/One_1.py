
class One_1(object):
    def has_all_unique(self, s):
        if len(s) > 26:
            return False

        checker = 0
        for i in range(len(s)):
            val = ord(s[i]) - ord('a')
            if checker & (1 << val) > 0:
                return False
            checker |= 1<<val

        return True