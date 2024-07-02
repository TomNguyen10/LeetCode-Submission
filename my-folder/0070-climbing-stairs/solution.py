class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        one = 1
        two = 2
        for i in range(2, n):
            one, two = two, one + two
        return two
