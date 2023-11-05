class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = 0
        for sen in sentences:
            num = sen.split()
            words = max(words, len(num))
        return words
