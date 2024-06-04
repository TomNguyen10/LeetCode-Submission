class Solution:
    def longestPalindrome(self, s: str) -> int:
        hs = set()
        res = 0
        for c in s:
            if c in hs:
                res += 1
                hs.remove(c)
            else:
                hs.add(c)
        if hs:
            return res * 2 + 1
        return res * 2
