class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) - 1

        res = [-1] * 2

        if not nums:
            return res

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] != target:
            return res
        
        res[0] = left

        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        
        res[1] = right

        return res
