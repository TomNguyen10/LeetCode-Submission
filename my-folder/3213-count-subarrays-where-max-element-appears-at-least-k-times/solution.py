class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        el = max(nums)
        res = cur = left = 0
        for right in range(len(nums)):
            cur += nums[right] == el
            while cur >= k:
                cur -= nums[left] == el
                left += 1
            res += left
        return res
