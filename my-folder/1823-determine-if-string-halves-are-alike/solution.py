class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first = 0
        second = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] in vowels:
                first +=1
            if s[right] in vowels:
                second += 1
            left +=1
            right -= 1
        return first == second        
