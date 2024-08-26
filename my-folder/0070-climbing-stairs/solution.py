class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        ones = 1
        twos = 2

        while n > 2:
            ones, twos = twos, ones + twos
            n -= 1
        
        return twos
