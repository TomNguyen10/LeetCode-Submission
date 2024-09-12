class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)

        res = 0

        for word in words:
            if all(c in s for c in word):
                res += 1
        
        return res
