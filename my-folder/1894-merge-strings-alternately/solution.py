class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        p1 = p2 = 0

        for i in range(min(len(word1), len(word2))):
            res += word1[p1]
            res += word2[p2]
            p1 += 1
            p2 += 1
        
        if p1 < len(word1):
            res += word1[p1:]
        
        if p2 < len(word2):
            res += word2[p2:]
        
        return res
