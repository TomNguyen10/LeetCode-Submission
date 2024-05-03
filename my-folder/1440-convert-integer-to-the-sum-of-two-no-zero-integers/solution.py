class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def nonZero(num):
            while num > 0:
                if num % 10 == 0:
                    return False
                num = num // 10
            return True
        for i in range(1, n):
            if nonZero(i) and nonZero(n - i):
                return [i, n - i]
            
