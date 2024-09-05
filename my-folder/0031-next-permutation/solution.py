class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        If the sequence already in descending order, no larger permutation is possible
        We need to find a 2 neighbors number a[i] and a[i-1] from the right to satisfy a[i] > a[i-1]. 
        To find the rearrangement producing the next larger number, we need to replace the a[i-1] with the number larger than itself among the numbers lying to its right a[j]. Swap a[i-1] and a[j]. 
        We need the smallest permutation so we need to place those numbers on the right in ascending order
        '''
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        i = len(nums) - 2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i+1)
        

