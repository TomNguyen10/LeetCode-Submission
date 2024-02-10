class Solution:
    def countSubstrings(self, s: str) -> int:
        def extract(string, left, right):
            count = 0
            while (left >= 0 and right < len(string)) and (string[left] == string[right]):
                count += 1
                left -= 1
                right += 1
            return count
        
        total_count = 0
        for i in range(len(s)):
            total_count += extract(s, i, i)
            total_count += extract(s, i, i+1)
        return total_count 
