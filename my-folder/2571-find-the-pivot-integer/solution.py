class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        x = int(sqrt(total))
        if x**2 == total:
            return x
        return -1
