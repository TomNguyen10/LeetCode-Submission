class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Dynamic Programming Approach
        Loop through the entire array and keep track of currMax and currMin
        currMax and currMin can swtich place if we meet a negative number
        reset currMax and currMin to 1, 1 if we meet 0
        '''
        res = max(nums)
        min_val = 1
        max_val = 1

        for num in nums:
            if num == 0:
                min_val = 1
                max_val = 1
            else:
                temp = max_val
                max_val = max(max_val * num, min_val * num, num)
                min_val = min(temp * num, min_val * num, num)
                res = max(res, max_val)
        
        return res

