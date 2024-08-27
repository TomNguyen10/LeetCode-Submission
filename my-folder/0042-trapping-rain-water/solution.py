class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Keep the wall on the 2 sides and flow water into lower parts
        Consider the lower side of the wall with the current index
        If it can hold water, add it to the result 
        Update the wall size
        '''

        res = 0
        left = 1
        right = len(height) - 2
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0
        while left <= right:
            if maxLeft <= maxRight:
                water = maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                water = maxRight - height[right]
                maxRight = max(maxRight, height[right])
                right -= 1
            if water > 0:
                res += water
        
        return res
