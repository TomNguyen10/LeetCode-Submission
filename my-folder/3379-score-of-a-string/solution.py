class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        p1 = 0
        p2 = 1
        while p2 < len(s):
            score += abs(ord(s[p1]) - ord(s[p2]))
            p1 = p2
            p2 += 1
        return score
