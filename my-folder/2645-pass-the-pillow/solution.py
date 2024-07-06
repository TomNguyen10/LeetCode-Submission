class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res = 1
        pos = 1
        for i in range(time):
            res += pos
            if res == n or res == 1:
                pos *= -1
        return res
