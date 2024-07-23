class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        s = str(n)
        for i in range(len(s)):
            if i > 0 and (len(s) - i) % 3 == 0:
                res += '.'
            res += s[i]
        return res
