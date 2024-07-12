class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        max_val = "ab" if x > y else "ba" 
        min_val = "ab" if x < y else "ba"
        res = 0
        for c in s:
            if stack and stack[-1] + c == max_val:
                res += max(x, y)
                stack.pop()
            else:
                stack.append(c)
        newS = "".join(stack)
        
        stack = []
        for c in newS:
            if stack and stack[-1] + c == min_val:
                res += min(x, y)
                stack.pop()
            else:
                stack.append(c)
        return res
