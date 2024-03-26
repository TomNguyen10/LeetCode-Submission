class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        for num in nums:
            nums[num % n] += n
        
        for i in range(1, n):
            if nums[i] // n == 0: return i
        
        return n
