class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Dynamic Programming approach, we have 2 options:
        1. Rob the current house -> cannot rob [curr-1] house
        2. Not rob the current house -> can rob [curr-1] house
        Calculate what is more profitable:
        1. Current house + loot from houses before previous
        2. Loot from the previous and any loot before that
        rob(i) = max(rob(i-2) + curr, rob(i-1))
        '''
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
