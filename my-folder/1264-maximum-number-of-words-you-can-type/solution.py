class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = [False] * 26
        for letter in brokenLetters:
            arr[ord(letter) - ord('a')] = True
        res, count = 0, 0
        for c in text:
            if c == ' ':
                res += count == 0
                count = 0 
            else:
                count += arr[ord(c) - ord('a')]
        return res + (count == 0)
