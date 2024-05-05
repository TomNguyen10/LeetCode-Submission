class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if rotated == True:
                    return False
                rotated = True
        if rotated and nums[len(nums) - 1] > nums[0]:
            return False
        return True
