class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        
        one, two = 1, 2

        while n > 2:
            one, two = two, one + two
            n -= 1
        
        return two
