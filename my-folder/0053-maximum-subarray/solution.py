class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We will keep track of the current sum
        # If the current sum < 0, set it to 0
        res = nums[0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            res = max(res, curr)
            if curr < 0:
                curr = 0
        return res
