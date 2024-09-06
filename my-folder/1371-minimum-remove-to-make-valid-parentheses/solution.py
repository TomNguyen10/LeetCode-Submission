class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        hs = set()
        stack = []

        for i in range(len(s)):
            c = s[i]

            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    hs.add(i)
            
        while stack:
            hs.add(stack.pop())

        res = ""

        for i in range(len(s)):
            if i not in hs:
                res += s[i]
        
        return res
