class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = s + s
        return s in doubled_s[1:-1]
