class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for num in nums:
            val = dic.get(num, 0)
            res += val
            dic[num] = val + 1
        return res
