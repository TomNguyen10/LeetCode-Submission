class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k == 0: return 0

        count = 0
        pro = 1

        left, right = 0, 0

        while right < len(nums):
            pro *= nums[right]

            while pro >= k and left <= right:
                pro /= nums[left]
                left += 1
            
            count += right - left + 1
            right += 1
        
        return count
