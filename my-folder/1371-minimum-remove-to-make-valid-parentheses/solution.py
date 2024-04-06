class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack: 
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ''
        
        res = ''.join(s)
        
        return res
