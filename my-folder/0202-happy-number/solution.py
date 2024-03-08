class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        elif n == 4: return False

        happy = 0
        while n > 0:
            happy += (n % 10) * (n % 10)
            n //= 10
        return self.isHappy(happy)
