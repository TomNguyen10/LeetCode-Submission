class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            if res < 2 or n > nums[res-2]:
                nums[res] = n
                res += 1
        
        return res
