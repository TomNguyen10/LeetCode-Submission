class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        We need 2 pointers to keep track of the 0 and 2, the 1 will automatically in place.
        Loop through the array, if we find 0 swap it with the left pointer, else if we find 2, swap with the right pointer
        '''

        p1, p2 = 0, len(nums) - 1
        p = 0

        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
                p += 1
            elif nums[p] > 1:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1
