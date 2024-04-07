class Solution:
    def checkValidString(self, s: str) -> bool:
        lMin, lMax = 0, 0

        for c in s:
            if c == '(':
                lMax += 1
                lMin += 1
            elif c == ')':
                lMax -= 1
                lMin -= 1
            else:
                lMax += 1
                lMin -= 1
            if lMax < 0:
                return False
            
            lMin = max(lMin, 0)
        
        return lMin == 0
