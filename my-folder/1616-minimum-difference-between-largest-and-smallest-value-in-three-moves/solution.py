class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        min1 = min2 = min3 = min4 = float('inf')
        max1 = max2 = max3 = max4 = float('-inf')

        for num in nums:
            if num <= min1:
                min1, min2, min3, min4 = num, min1, min2, min3
            elif num <= min2:
                min2, min3, min4 = num, min2, min3
            elif num <= min3:
                min3, min4 = num, min3
            elif num <= min4:
                min4 = num
            
            if num >= max1:
                max1, max2, max3, max4 = num, max1, max2, max3
            elif num >= max2:
                max2, max3, max4 = num, max2, max3
            elif num >= max3:
                max3, max4 = num, max3
            elif num >= max4:
                max4 = num
        
        if min1 == max1:  
            return 0
        
        return min(max1 - min4, max2 - min3, max3 - min2, max4 - min1)
