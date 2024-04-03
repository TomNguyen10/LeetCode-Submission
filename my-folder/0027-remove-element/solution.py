class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                res += 1
                left += 1
        return res
