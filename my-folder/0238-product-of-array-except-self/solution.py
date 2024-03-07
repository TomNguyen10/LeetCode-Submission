class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = pro
            pro *= nums[i]

        pro = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pro
            pro *= nums[i]
        
        return res
