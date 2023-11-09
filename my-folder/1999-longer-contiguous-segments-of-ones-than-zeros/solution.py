class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones, zeros, maxOne, maxZero = 0, 0, 0, 0
        for c in s:
            if c == '1':
                ones += 1
                zeros = 0
            else:
                zeros += 1
                ones = 0
            maxOne = max(maxOne, ones)
            maxZero = max(maxZero, zeros)
        return maxOne > maxZero
        
