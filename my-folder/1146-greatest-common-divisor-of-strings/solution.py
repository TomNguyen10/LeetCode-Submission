class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b != 0:
                b, a = a % b, b
            return a
        if str1 + str2 != str2 + str1:
            return ""
        num = gcd(len(str1), len(str2))
        return str1[:num]
