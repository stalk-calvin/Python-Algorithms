from typing import List

class CombinationSum(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(comb, i, target, res):
            if target == 0:
                res.append(comb)
                return
            for j, x in enumerate(candidates[i:]):
                if x <= target:
                    target -= x
                    dfs(comb + [x], i + j, target, res)
                    target += x

        candidates.sort()
        res = []
        dfs([], 0, target, res)
        return res
