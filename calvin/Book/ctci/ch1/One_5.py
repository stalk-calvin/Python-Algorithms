class One_5(object):
    def oneEditReplace(self, s1, s2):
        found = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found:
                    return False
                found = True
        return True

    def oneEditInsert(self, s1, s2):
        idx1=0
        idx2=0
        while (idx1 < len(s1) and idx2 < len(s2)):
            if s1[idx1] != s2[idx2]:
                if idx1 != idx2:
                    return False
                idx2+=1
            else:
                idx1+=1
                idx2+=1
        return True

    def oneEditAway(self, s1, s2):
        if len(s1) == len(s2):
            return self.oneEditReplace(s1, s2)
        elif len(s1) + 1 == len(s2):
            return self.oneEditInsert(s1, s2)
        elif len(s1) - 1 == len(s2):
            return self.oneEditInsert(s2, s1)
        else:
            return False