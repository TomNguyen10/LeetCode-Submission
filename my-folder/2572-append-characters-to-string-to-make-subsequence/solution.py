class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1 = p2 = 0
        
        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p2 += 1
            p1 += 1
        
        return len(t) - p2
