class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = 10 ** 6
        for i in nums:
            x = abs(i-0)
            if x < m:
                m = x
                val = i
            elif x == m and val < i:
                val = i
        return val
