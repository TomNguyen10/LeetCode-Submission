class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')

        zeros = len(s) - ones

        res = '1' * (ones - 1) + '0' * zeros + '1'

        return res
