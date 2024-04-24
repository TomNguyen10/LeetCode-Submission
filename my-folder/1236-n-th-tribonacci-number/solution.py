class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        c = 1
        while n > 2:
            d = a + b + c
            a = b
            b = c 
            c = d
            n -= 1
        return c
