class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        c = abs(x)
        while c > 0:
            rem = c % 10
            res = res * 10 + rem
            c //= 10
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res if x > 0 else -res
