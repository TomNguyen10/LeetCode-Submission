class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, temp, idx, res):
            if target == 0:
                res.append(temp[:])
                return
            if target < 0 or idx == len(candidates):
                return
            
            temp.append(candidates[idx])
            backtrack(candidates, target - candidates[idx], temp, idx, res)
            temp.pop()
            backtrack(candidates, target, temp, idx+1, res)
        
        res = []
        temp = []
        backtrack(candidates, target, temp, 0, res)
        return res
        
