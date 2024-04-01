class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        el = max(nums)
        curr = 0
        left = right = 0

        while right < len(nums):
            curr += nums[right] == el
            while curr >= k:
                curr -= nums[left] == el
                left += 1
            res += left
            right += 1
        return res
