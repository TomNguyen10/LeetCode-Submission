class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p2 < len(t):
            if p1 < len(s) and s[p1] == t[p2]:
                p1 += 1
            p2 +=1
        
        return p1 == len(s)
