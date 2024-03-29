class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0

        for item in items:
            ty, col, name = item
            if (ruleKey == "type" and ruleValue == ty) or (ruleKey == "color" and ruleValue == col) or (ruleKey == "name" and ruleValue == name):
                res += 1
        
        return res
