class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr = [0] * len(s)
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c == ')' and stack and s[stack[-1]] == '(':
                arr[i] = 1
                arr[stack[-1]] = 1
                stack.pop()
            else:
                stack.append(i)
        
        res = 0
        curr = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                curr = 0
            else:
                curr += 1
            res = max(res, curr)
        
        return res

