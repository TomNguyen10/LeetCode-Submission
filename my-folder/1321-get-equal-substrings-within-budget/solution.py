class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0 
        right = 0 
        res = 0
        total = 0
        
        while right < len(s):
            total += abs(ord(t[right]) - ord(s[right]))
            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res
