class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  
        
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:  
                        put = [nums[i], nums[left], nums[right]]
                        res.append(put)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > -nums[i]:  
                        right -= 1
                    else:
                        left += 1
        return res

