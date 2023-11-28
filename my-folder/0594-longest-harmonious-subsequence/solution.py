class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for num in nums:
            m[num] += 1
        res = 0
        for key in m:
            if key + 1 in m:
                res = max(res, m[key] + m[key+1])
        return res
        


