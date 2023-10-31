class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        if i < j:
            return i + n - 1 - j
        return i + n - 1 - j - 1
        
