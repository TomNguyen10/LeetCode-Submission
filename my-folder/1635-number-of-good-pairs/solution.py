class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                val = dic[num]
                res += val
                dic[num] = val + 1
        return res
