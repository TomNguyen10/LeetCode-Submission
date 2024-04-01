class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        s = s.strip()
        arr = s.split(" ")
        return len(arr[-1]) 
