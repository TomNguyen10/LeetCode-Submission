class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for i in range(1, len(words)):
            word = words[i]
            c &= Counter(word)
        
        res = []

        for key, val in c.items():
            res.extend([key] * val)
        
        return res

