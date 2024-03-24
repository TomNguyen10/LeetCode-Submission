class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack: return False
                top = stack[-1]
                if (char == ')' and top == '(') or (char == ']' and top == '[') or (char == '}' and top == '{'):
                    stack.pop()
                else:
                    stack.append(char)

        return not stack

