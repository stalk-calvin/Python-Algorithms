class NumberCombination(object):
    def number_combination(self, nums):
        result = []
        tracker = []
        for x in nums:
            for i in range(1,3):
                if self.__ni_helper(x[0:i], x[i:], tracker):
                    result.append(tracker)
                    tracker = []
        return result

    # 569815571556
    # 4938532894754
    # 49 38 53 28 9 47 54
    # 0123456
    def __ni_helper(self, x, rest, tracker):
        if x and (0 < int(x) < 60):
            tracker.append(x)
        else:
            return False

        if not rest and len(tracker)==7:
            return True
        elif len(tracker)>=7 and rest:
            tracker.pop()
            return False

        for i in range(1,3):
            if self.__ni_helper(rest[0:i], rest[i:], tracker):
                return True

        tracker.pop()
        return False