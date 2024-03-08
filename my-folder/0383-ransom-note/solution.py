class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}

        for char in magazine:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        
        for char in ransomNote:
            val = dic.get(char, 0)
            if val == 0:
                return False
            dic[char] = val - 1
        
        return True
