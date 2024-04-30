class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        curr_sum = 0
        res = len(nums) + 1
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1

        if res == len(nums) + 1: return 0
        return res
