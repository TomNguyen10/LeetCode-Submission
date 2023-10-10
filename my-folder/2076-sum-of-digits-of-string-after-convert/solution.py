class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def charToNum(char):
            return ord(char) - ord('a') + 1

        num = ''.join(str(charToNum(char)) for char in s)

        for i in range(k):
            num = str(sum(int(digit) for digit in num))


        return int(num)

        
        
