class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        prev = 1
        while n >= prev:
            n -= prev
            prev += 1
            res += 1
        return res
