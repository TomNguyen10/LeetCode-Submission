class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def calculate(word):
            val = 0
            for char in word:
                val = val * 10 + (ord(char) - ord('a'))
            return val
        
        num1 = calculate(firstWord)
        num2 = calculate(secondWord)
        res = calculate(targetWord)
        return num1 + num2 == res
        
        
