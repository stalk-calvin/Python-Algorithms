class One_3(object):
    def isPermutationUsingSort(self, a, b):
        return sorted(a) == sorted(b)

    def isPermutationArray(self, a, b):
        if len(a) != len(b):
            return False

        letters = [0] * 128 # ascii
        for x in a:
            letters[ord(x) - ord('a')]+=1

        for x in b:
            idx = ord(x) - ord('a')
            letters[idx]-=1
            if letters[idx] < 0:
                return False

        return True