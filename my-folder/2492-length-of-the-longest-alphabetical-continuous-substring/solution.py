class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        curr = s[0]
        length = 1

        for i in range(1, len(s)):
            char = s[i]
            if ord(char) - ord(curr) == length:
                length += 1
            else:
                curr = s[i]
                length = 1
            res = max(res, length)

        return res
