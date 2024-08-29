class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) < 2:
            return nums[0]
        n = len(nums)
        return max(helper(nums[:n-1]), helper(nums[1:]))
