class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        word = list(s)
        while left < right:
            while (left < right) and word[left] not in vowels:
                left += 1
            while left < right and word[right] not in vowels:
                right -= 1
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return "".join(word)
        
