class Solution:
    def firstUniqChar(self, s: str) -> int:
        hs = Counter(s)
        res = -1
        for char, count in hs.items():
            if count == 1:
                res = s.index(char)
                return res
        return res
