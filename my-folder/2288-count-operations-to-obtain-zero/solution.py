class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        elif num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        return 1 + self.countOperations(num1, num2)
