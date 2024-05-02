class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = 0
        s = set()
        for num in nums:
            if num < 0:
                s.add(num)
        for num in nums:
            if -num in s:
                res = max(res, num)
        if res == 0:
            return -1
        return res
