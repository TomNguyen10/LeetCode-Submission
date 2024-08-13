class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7

        curr = 0

        res = 0

        for i in range(len(s)):
            if i == 0 or s[i] == s[i-1]:
                curr += 1
            else:
                curr = 1

            res = (res + curr) % mod

        return res       
