class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        res = 0
        curr = 0

        for right in range(len(nums)):
            num = nums[right]
            curr += num 

            while (right - left + 1) * num - curr > k:
                curr -= nums[left]
                left += 1

            res = max(res, right - left + 1)

        return res
