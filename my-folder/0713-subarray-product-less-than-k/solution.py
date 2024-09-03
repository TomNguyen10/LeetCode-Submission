class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0

        pro = 1
        left = 0
        res = 0
        for right in range(len(nums)):
            pro *= nums[right]
            while pro >= k and left <= right:
                pro /= nums[left]
                left += 1
            res += right - left + 1
        return res
