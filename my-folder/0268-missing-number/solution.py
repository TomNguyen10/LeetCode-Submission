class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += num
        n = len(nums)
        return n*(n+1)//2 - total_sum
