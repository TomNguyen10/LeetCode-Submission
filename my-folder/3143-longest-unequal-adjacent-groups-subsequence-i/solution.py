class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = -1
        res = []

        for i in range(len(words)):
            if groups[i] != prev:
                prev = groups[i]
                res.append(words[i])
        
        return res
