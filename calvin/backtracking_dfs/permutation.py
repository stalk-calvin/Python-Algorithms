from typing import List

class Permutation(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, permute, result):
            if nums == 0:
                result.append(permute)
            for j, x in enumerate(nums):
                dfs(nums[:j] + nums[j+1:], permute + [nums[j]], result)

        res = []
        dfs(nums, [], res)
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, permute, result):
            if nums == 0:
                result.append(permute)
            tracker = set()
            for j, x in enumerate(nums):
                if x not in tracker:
                    tracker.add(x)
                    dfs(nums[:j] + nums[j+1:], permute + [nums[j]], result)

        res = []
        dfs(nums, [], res)
        return res