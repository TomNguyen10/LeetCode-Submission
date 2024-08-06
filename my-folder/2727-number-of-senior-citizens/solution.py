class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for word in details:
            if int(word[11:13]) > 60:
                res += 1
        
        return res
