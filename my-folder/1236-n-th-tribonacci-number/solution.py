class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1

        a, b, c = 0, 1, 1

        for i in range(2, n):
            a, b, c = b, c, a + b + c
        
        return c
