class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(candidates, target, start, temp, res):
            if target < 0: return
            if target == 0: res.append(temp)
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(candidates, target - candidates[i], i+1, temp+[candidates[i]], res)
            
        backtrack(candidates, target, 0, [], res)
        return res

