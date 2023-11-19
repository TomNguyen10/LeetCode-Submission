class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = words[::-1]
        res = " ".join(reverse)
        return res

        
