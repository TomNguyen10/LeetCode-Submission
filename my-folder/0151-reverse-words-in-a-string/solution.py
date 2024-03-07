class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        reverse = arr[::-1]
        res = " ".join(reverse)
        return res
