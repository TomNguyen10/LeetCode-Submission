class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])

        for word in words[1:]:
            dic &= Counter(word)

        res = []

        for key, val in dic.items():
            res.extend([key] * val)

        return res
