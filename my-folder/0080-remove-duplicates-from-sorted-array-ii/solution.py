class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        The basic idea is of two pointers. The fast pointer will traverse the array sequentially one element at a time.
The other slower pointer is i which does not increment when there is a duplicate, but otherwise increments one position at a time.
Because this is sorted array, duplicates will be always adjacent.

To remove dupes, all we have to do is to overwrite slow pointer value with fast pointer.
At the end, point up to which slow pointer has moved, is the unique array, rest of array will be unwanted dupes.
        '''
        i = 0

        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        
        return i
