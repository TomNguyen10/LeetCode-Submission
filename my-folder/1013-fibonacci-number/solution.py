class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        one = 0
        two = 1
        for i in range(1, n):
            one, two = two, one + two
        return two
