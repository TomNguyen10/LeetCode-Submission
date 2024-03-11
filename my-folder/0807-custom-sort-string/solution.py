class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}

        for char in s:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        
        res = ""

        for char in order:
            if char in dic:
                res += char * dic[char]
                dic[char] = 0
        
        for key, val in dic.items():
            if val > 0:
                res += key * val
        
        return res
